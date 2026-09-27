"""Behavioral coverage for package guidance and skill deployment."""

# Pytest fixtures supply the argument types; test names describe each behavior.
# ruff: noqa: ANN001, ANN201, ANN202, D103

from __future__ import annotations

import importlib
import sys
import zipfile
from pathlib import Path

import pytest

from ionbus_utils import agent_skill as skills


@pytest.fixture
def package_factory(tmp_path, monkeypatch):
    """Create real importable packages, independent of installer metadata."""
    packages = tmp_path / "packages"
    packages.mkdir()
    monkeypatch.syspath_prepend(str(packages))
    names = []

    def create(name="aps_demo", guide="A guide with Unicode: caf\u00e9\n"):
        directory = packages
        for component in name.split("."):
            directory /= component
            directory.mkdir(exist_ok=True)
            (directory / "__init__.py").write_text("", encoding="utf-8")
        if guide is not None:
            (directory / "README_AI.md").write_text(guide, encoding="utf-8")
        (directory / "docs").mkdir(exist_ok=True)
        (directory / "docs" / "usage.md").write_text(
            "Linked guide\n", encoding="utf-8"
        )
        names.append(name)
        importlib.invalidate_caches()
        return name

    yield create
    for name in list(sys.modules):
        if any(name == item or item.startswith(name + ".") for item in names):
            sys.modules.pop(name, None)


def test_read_package_and_linked_resource(package_factory):
    package = package_factory()
    assert "caf\u00e9" in skills.read_resource(package)
    assert skills.read_resource(package, "docs/usage.md") == "Linked guide\n"
    assert skills.read_resource(package, "docs\\usage.md") == "Linked guide\n"


@pytest.mark.parametrize(
    "resource",
    [
        "",
        "/README_AI.md",
        "C:\\README_AI.md",
        "C:README_AI.md",
        "\\\\server\\share\\guide.md",
        "../guide.md",
        "docs/../guide.md",
        "docs//guide.md",
        "docs/",
        "docs/./guide.md",
        "docs\\..\\guide.md",
    ],
)
def test_reject_unsafe_resources(package_factory, resource):
    with pytest.raises(skills.SkillError):
        skills.read_resource(package_factory(), resource)


def test_missing_package_error_names_interpreter_and_resource(capsys):
    assert (
        skills.main(["show", "aps_missing_package"]) == skills.OPERATIONAL_ERROR
    )
    error = capsys.readouterr().err
    assert sys.executable in error
    assert "aps_missing_package" in error
    assert "README_AI.md" in error


def test_missing_resource_writes_nothing(package_factory, tmp_path):
    package = package_factory(guide=None)
    project = tmp_path / "project"
    with pytest.raises(skills.SkillError, match=r"README_AI\.md"):
        skills.install(package, ["all"], project=project)
    assert not project.exists()


def test_read_zip_package(tmp_path, monkeypatch):
    archive = tmp_path / "package.zip"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("aps_zip/__init__.py", "")
        bundle.writestr("aps_zip/README_AI.md", "Zip guide\n")
        bundle.writestr("aps_zip/docs/usage.md", "Zip detail\n")
    monkeypatch.syspath_prepend(str(archive))
    try:
        assert skills.read_resource("aps_zip") == "Zip guide\n"
        assert (
            skills.read_resource("aps_zip", "docs/usage.md") == "Zip detail\n"
        )
    finally:
        sys.modules.pop("aps_zip", None)


@pytest.mark.parametrize(
    ("platforms", "expected"),
    [
        (["claude"], ["claude"]),
        (["codex"], ["codex"]),
        (["all"], ["claude", "codex"]),
        (["codex", "claude", "codex"], ["claude", "codex"]),
    ],
)
def test_platform_destinations(package_factory, tmp_path, platforms, expected):
    package = package_factory()
    project = tmp_path / "project"
    results = skills.install(package, platforms, project=project)
    assert [result.platform for result in results] == expected
    for result in results:
        assert (
            result.path
            == project
            / skills.PLATFORMS[result.platform]
            / "aps-demo"
            / "SKILL.md"
        )
        data = result.path.read_bytes()
        assert b"\r" not in data
        assert data.endswith(b"\n") and not data.endswith(b"\n\n")
        assert b"python -m ionbus_utils.agent_skill show aps_demo" in data
        assert b"caf" not in data  # Guide content is not copied into the stub.


def test_user_scope_and_identical_noop(package_factory, tmp_path, monkeypatch):
    package = package_factory()
    home = tmp_path / "home"
    monkeypatch.setattr(Path, "home", classmethod(lambda _cls: home))
    created = skills.install(package, ["all"], user=True)
    snapshots = [
        (item.path.read_bytes(), item.path.stat().st_mtime_ns)
        for item in created
    ]
    repeated = skills.install(package, ["all"], user=True)
    assert all(item.status == "unchanged" for item in repeated)
    assert snapshots == [
        (item.path.read_bytes(), item.path.stat().st_mtime_ns)
        for item in repeated
    ]


def test_all_destinations_preflight_before_writing(package_factory, tmp_path):
    package = package_factory()
    project = tmp_path / "project"
    codex = project / ".agents/skills/aps-demo/SKILL.md"
    codex.parent.mkdir(parents=True)
    codex.write_text("Custom content\n", encoding="utf-8")
    with pytest.raises(skills.SkillConflict):
        skills.install(package, ["all"], project=project)
    assert not (project / ".claude").exists()
    assert codex.read_text(encoding="utf-8") == "Custom content\n"
    results = skills.install(package, ["all"], project=project, force=True)
    assert [item.status for item in results] == ["created", "replaced"]


@pytest.mark.parametrize("force", [False, True])
def test_normalization_collision_cannot_be_forced(
    package_factory, tmp_path, force
):
    first = package_factory("aps_demo")
    second = package_factory("aps.demo")
    original = skills.install(first, ["codex"], project=tmp_path)[0].path
    content = original.read_bytes()
    with pytest.raises(skills.SkillConflict, match="collision"):
        skills.install(second, ["codex"], project=tmp_path, force=force)
    assert original.read_bytes() == content


@pytest.mark.parametrize(
    "name", ["../escape", "bad-name", "_leading", "foo__bar", "a" * 65]
)
def test_reject_unsafe_skill_names(name):
    with pytest.raises(skills.SkillError):
        skills.skill_name(name)


def test_scope_and_platform_are_required(package_factory, tmp_path):
    package = package_factory()
    with pytest.raises(skills.SkillError, match="scope"):
        skills.install(package, ["all"])
    with pytest.raises(skills.SkillError, match="scope"):
        skills.install(package, ["all"], project=tmp_path, user=True)
    with pytest.raises(skills.SkillError, match="platform"):
        skills.install(package, [], project=tmp_path)


def test_reject_destination_symlink_escape(package_factory, tmp_path):
    package = package_factory()
    project = tmp_path / "project"
    external = tmp_path / "external"
    project.mkdir()
    external.mkdir()
    try:
        (project / ".agents").symlink_to(external, target_is_directory=True)
    except OSError:
        pytest.skip("This Windows account cannot create directory symlinks")
    with pytest.raises(skills.SkillError, match="Unsafe"):
        skills.install(package, ["codex"], project=project)
    assert not list(external.iterdir())


def test_atomic_failure_preserves_existing_file(
    package_factory, tmp_path, monkeypatch
):
    package = package_factory()
    original = skills.install(package, ["codex"], project=tmp_path)[0].path
    original.write_text("Keep this\n", encoding="utf-8")

    def fail_replace(_source, _target):
        raise OSError("simulated replacement failure")

    monkeypatch.setattr(skills.os, "replace", fail_replace)
    with pytest.raises(
        skills.SkillError, match="simulated replacement failure"
    ):
        skills.install(package, ["codex"], project=tmp_path, force=True)
    assert original.read_text(encoding="utf-8") == "Keep this\n"
    assert list(original.parent.iterdir()) == [original]


def test_partial_failure_reports_completed_and_failed_destinations(
    package_factory, tmp_path, monkeypatch, capsys
):
    package = package_factory()
    real_write = skills.write_atomic

    def fail_second(path, content):
        if ".agents" in path.parts:
            raise OSError("simulated second-platform failure")
        real_write(path, content)

    monkeypatch.setattr(skills, "write_atomic", fail_second)
    code = skills.main(
        ["install", package, "--platform", "all", "--project", str(tmp_path)]
    )
    assert code == skills.OPERATIONAL_ERROR
    error = capsys.readouterr().err
    assert "Completed: created:" in error and ".claude" in error
    assert "failed at" in error and ".agents" in error
    assert (tmp_path / ".claude/skills/aps-demo/SKILL.md").is_file()
    assert not (tmp_path / ".agents/skills/aps-demo/SKILL.md").exists()


def test_cli_exit_contract(package_factory, tmp_path, capsys):
    package = package_factory()
    arguments = [
        "install",
        package,
        "--platform",
        "codex",
        "--project",
        str(tmp_path),
    ]
    assert skills.main(arguments) == skills.SUCCESS
    assert skills.main(arguments) == skills.SUCCESS
    path = tmp_path / ".agents/skills/aps-demo/SKILL.md"
    path.write_text("Different\n", encoding="utf-8")
    assert skills.main(arguments) == skills.CONFLICT
    assert skills.main([*arguments, "--force"]) == skills.SUCCESS
    assert (
        skills.main(["show", package, "missing.md"]) == skills.OPERATIONAL_ERROR
    )
    with pytest.raises(SystemExit) as invalid:
        skills.main(["install", package])
    assert invalid.value.code == skills.OPERATIONAL_ERROR
    assert "missing.md" in capsys.readouterr().err
