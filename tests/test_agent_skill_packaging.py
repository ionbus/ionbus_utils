"""Inspect actual distributions and import resources from a built wheel."""

# Pytest fixtures supply the argument types; test names describe each behavior.
# ruff: noqa: ANN001, ANN201, D103

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def built_artifacts(tmp_path_factory):
    source = Path(__file__).resolve().parents[1]
    workspace = tmp_path_factory.mktemp("agent_skill_build")
    checkout = workspace / "checkout"
    shutil.copytree(
        source,
        checkout,
        ignore=shutil.ignore_patterns(
            ".git",
            ".agents",
            ".claude",
            ".vscode",
            "graphify-out",
            "build",
            "dist",
            "*.egg-info",
            "__pycache__",
            ".pytest_cache",
            ".ruff_cache",
        ),
    )
    environment = dict(
        os.environ, GIT_DESCRIBE_TAG="0.0.0", PYTHONDONTWRITEBYTECODE="1"
    )
    build = subprocess.run(
        [sys.executable, "-B", "setup.py", "sdist", "bdist_wheel"],
        cwd=checkout,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert build.returncode == 0, build.stdout[-5000:] + build.stderr[-5000:]
    return (
        next((checkout / "dist").glob("*.whl")),
        next((checkout / "dist").glob("*.tar.gz")),
        checkout,
    )


def test_wheel_and_sdist_package_guides_without_graph_outputs(built_artifacts):
    wheel, sdist, _ = built_artifacts
    resources = [
        "README.md",
        "README_AI.md",
        "README_PIP.md",
        "README_AGENT_SKILLS.md",
        "logging.md",
        "cache_utils.md",
        "file_utils.md",
        "pandas_utils.md",
        "subprocess_utils.md",
        "time_utils.md",
        "crypto_utils/README.md",
        "git_utils/README.md",
        "yaml_utils/README.md",
        "agent_skill.py",
        "agent_skill_template.py",
    ]
    with zipfile.ZipFile(wheel) as bundle:
        names = set(bundle.namelist())
    for resource in resources:
        assert "ionbus_utils/" + resource in names
    assert not any(
        "graphify-out" in name or "/tests/" in name for name in names
    )
    assert "ionbus_utils/APS_todo.md" not in names
    assert "ionbus_utils/AGENT_PROJECT_SETUP.md" not in names
    with tarfile.open(sdist) as bundle:
        source_names = {
            "/".join(name.split("/")[1:]) for name in bundle.getnames()
        }
    for resource in resources:
        assert resource in source_names
    assert not any("graphify-out" in name for name in source_names)


def test_guide_and_linked_resource_readable_from_wheel(
    built_artifacts, tmp_path
):
    wheel, _, _ = built_artifacts
    script = (
        "import sys; sys.path.insert(0, sys.argv[1]); "
        "from ionbus_utils.agent_skill import read_resource; "
        "import ionbus_utils; "
        "assert '.whl' in ionbus_utils.__file__; "
        "assert 'ionbus_utils' in read_resource('ionbus_utils'); "
        "assert 'logger' in read_resource('ionbus_utils', 'logging.md'); "
        "print('wheel resource imports passed')"
    )
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    environment.pop("PYTHONPATH", None)
    result = subprocess.run(
        [sys.executable, "-B", "-c", script, str(wheel)],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_editable_install_reads_source_guides(built_artifacts, tmp_path):
    _, _, checkout = built_artifacts
    editable_dist = tmp_path / "editable_dist"
    editable_dist.mkdir()
    environment = dict(
        os.environ, GIT_DESCRIBE_TAG="0.0.0", PYTHONDONTWRITEBYTECODE="1"
    )
    build = subprocess.run(
        [
            sys.executable,
            "-B",
            "-c",
            (
                "import sys; from setuptools.build_meta import build_editable; "
                "build_editable(sys.argv[1])"
            ),
            str(editable_dist),
        ],
        cwd=checkout,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert build.returncode == 0, build.stdout[-3000:] + build.stderr[-3000:]
    site_directory = tmp_path / "site_packages"
    site_directory.mkdir()
    with zipfile.ZipFile(next(editable_dist.glob("*.whl"))) as bundle:
        bundle.extractall(site_directory)
    environment.pop("PYTHONPATH", None)
    script = (
        "import site, sys; site.addsitedir(sys.argv[1]); "
        "from ionbus_utils.agent_skill import read_resource; "
        "import ionbus_utils; "
        "assert sys.argv[2] in ionbus_utils.__file__; "
        "assert 'ionbus_utils' in read_resource('ionbus_utils'); "
        "assert 'logger' in read_resource('ionbus_utils', 'logging.md')"
    )
    result = subprocess.run(
        [
            sys.executable,
            "-B",
            "-c",
            script,
            str(site_directory),
            str(checkout),
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
