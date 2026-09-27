"""Read package guidance and install deterministic agent skill stubs.

Run with ``python -m ionbus_utils.agent_skill`` in the selected environment.
This module uses only the standard library; importing a target package still
requires that package's normal runtime dependencies.
"""

from __future__ import annotations

import argparse
import importlib
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from importlib import resources
from pathlib import Path, PureWindowsPath
from typing import Sequence

SUCCESS = 0
CONFLICT = 1
OPERATIONAL_ERROR = 2
MAX_SKILL_NAME_LENGTH = 64
PLATFORMS = {
    "claude": Path(".claude") / "skills",
    "codex": Path(".agents") / "skills",
}
_PACKAGE_NAME = re.compile(
    r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*"
)
_SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
_OWNER = re.compile(
    r"^  import-package: ([A-Za-z_][A-Za-z0-9_.]*)$", re.MULTILINE
)


class SkillError(Exception):
    """An operational failure that the CLI reports without a traceback."""


class SkillConflict(SkillError):
    """Existing content or a package-name collision prevents installation."""


@dataclass(frozen=True)
class Installation:
    """One destination and its completed installation outcome."""

    platform: str
    path: Path
    status: str


def skill_name(import_package: str) -> str:
    """Normalize an import package into a safe skill directory name."""
    if not _PACKAGE_NAME.fullmatch(import_package):
        raise SkillError(f"Invalid import package name: {import_package!r}")
    name = import_package.lower().replace("_", "-").replace(".", "-")
    if len(name) > MAX_SKILL_NAME_LENGTH or not _SKILL_NAME.fullmatch(name):
        raise SkillError(
            f"Package {import_package!r} produces an unsafe skill name"
        )
    return name


def resource_parts(relative_resource: str) -> list[str]:
    """Validate package-relative paths on both Windows and POSIX."""
    if (
        not relative_resource
        or "\x00" in relative_resource
        or PureWindowsPath(relative_resource).drive
        or relative_resource.startswith(("/", "\\"))
        or ":" in relative_resource
    ):
        raise SkillError(
            f"Resource must be a relative package path: {relative_resource!r}"
        )
    parts = relative_resource.replace("\\", "/").split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise SkillError(f"Unsafe resource path: {relative_resource!r}")
    return parts


def read_resource(
    import_package: str, relative_resource: str = "README_AI.md"
) -> str:
    """Read a UTF-8 resource from a package, including zip imports."""
    skill_name(import_package)
    parts = resource_parts(relative_resource)
    context = (
        f"{sys.executable}: package {import_package!r}, "
        f"resource {relative_resource!r}"
    )
    try:
        package = importlib.import_module(import_package)
        if not hasattr(package, "__path__"):
            raise ValueError("target is a module, not an import package")
        resource = resources.files(package)
    except Exception as exc:
        raise SkillError(f"{context}: {exc}") from exc
    try:
        for part in parts:
            resource = resource.joinpath(part)
        if not resource.is_file():
            raise FileNotFoundError("resource does not exist or is not a file")
        return resource.read_text(encoding="utf-8")
    except Exception as exc:
        raise SkillError(f"{context}: {exc}") from exc


def generate_skill(import_package: str) -> str:
    """Generate a portable stub with explicit package ownership."""
    name = skill_name(import_package)
    return (
        "---\n"
        f"name: {name}\n"
        f"description: Use when code imports or integrates {import_package}; "
        "load the installed package's agent-facing API and usage guide "
        "before choosing APIs "
        "or recreating its functionality.\n"
        "metadata:\n"
        f"  import-package: {import_package}\n"
        "---\n\n"
        f"# {import_package} package guidance\n\n"
        "Use the Python environment selected for the current project.\n\n"
        "Run:\n\n"
        f"    python -m ionbus_utils.agent_skill show {import_package}\n\n"
        "If `README_AI.md` references another packaged document, "
        "read it with:\n\n"
        f"    python -m ionbus_utils.agent_skill show {import_package} "
        "<relative-resource>\n"
    )


def select_platforms(platforms: Sequence[str]) -> list[str]:
    """Expand explicit 'all' and deduplicate destinations deterministically."""
    if not platforms:
        raise SkillError("At least one platform is required")
    unknown = set(platforms) - set(PLATFORMS) - {"all"}
    if unknown:
        raise SkillError(f"Unknown platforms: {', '.join(sorted(unknown))}")
    selected = set(PLATFORMS) if "all" in platforms else set(platforms)
    return [platform for platform in PLATFORMS if platform in selected]


def destination(root: Path, platform: str, name: str) -> Path:
    """Construct a destination that cannot escape its selected scope."""
    try:
        root = root.resolve()
        skills_root = (root / PLATFORMS[platform]).resolve()
        candidate = skills_root / name / "SKILL.md"
        resolved = candidate.resolve()
    except (OSError, RuntimeError) as exc:
        raise SkillError(f"Cannot resolve skill destination: {exc}") from exc
    if root.exists() and not root.is_dir():
        raise SkillError(f"Destination root is not a directory: {root}")
    if (
        not skills_root.is_relative_to(root)
        or not resolved.is_relative_to(skills_root)
        or candidate.is_symlink()
    ):
        raise SkillError(f"Unsafe skill destination: {candidate}")
    return candidate


def _preflight(
    import_package: str, path: Path, expected: bytes, *, force: bool
) -> str:
    if not path.exists():
        return "created"
    try:
        current = path.read_bytes()
        owner = _OWNER.search(current.decode("utf-8"))
    except (OSError, UnicodeError) as exc:
        raise SkillError(f"Cannot preflight {path}: {exc}") from exc
    if owner and owner.group(1) != import_package:
        raise SkillConflict(
            f"Skill name collision at {path}: {owner.group(1)!r} and "
            f"{import_package!r}; --force cannot merge different packages"
        )
    if current == expected:
        return "unchanged"
    if force:
        return "replaced"
    raise SkillConflict(
        f"Different content at {path}; use --force to replace it"
    )


def write_atomic(path: Path, content: bytes) -> None:
    """Replace a destination only after a complete temporary write beside it."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=".SKILL.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            stream.write(content)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def _apply_installation(
    item: Installation, root: Path, name: str, expected: bytes
) -> None:
    if item.status == "unchanged":
        return
    # Recheck containment immediately before creating directories.
    if destination(root, item.platform, name) != item.path:
        raise SkillError(
            f"Destination changed during installation: {item.path}"
        )
    item.path.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(item.path, expected)


def install(
    import_package: str,
    platforms: Sequence[str],
    *,
    project: str | Path | None = None,
    user: bool = False,
    force: bool = False,
) -> list[Installation]:
    """Preflight every destination, then install one package's skill stubs.

    Raises SkillConflict for content conflicts or normalization collisions.
    Raises SkillError for operational failures; partial writes are named in
    the error. Identical destinations are never rewritten.
    """
    if (project is None) == (not user):
        raise SkillError("Choose exactly one scope: --project <path> or --user")
    selected = select_platforms(platforms)
    name = skill_name(import_package)
    read_resource(import_package)
    expected = generate_skill(import_package).encode("utf-8")
    root = Path.home() if user else Path(project)
    plan = []
    for platform in selected:
        path = destination(root, platform, name)
        status = _preflight(import_package, path, expected, force=force)
        plan.append(Installation(platform, path, status))

    completed = []
    for index, item in enumerate(plan):
        try:
            _apply_installation(item, root, name, expected)
            completed.append(item)
        except (OSError, SkillError) as exc:
            successes = (
                "; ".join(
                    f"{result.status}: {result.path}" for result in completed
                )
                or "none"
            )
            pending = (
                "; ".join(str(result.path) for result in plan[index + 1 :])
                or "none"
            )
            raise SkillError(
                f"Installation failed at {item.path}: {exc}. "
                f"Completed: {successes}. "
                f"Not attempted: {pending}"
            ) from exc
    return completed


def _run(arguments: argparse.Namespace) -> None:
    if arguments.command == "show":
        content = read_resource(
            arguments.import_package, arguments.relative_resource
        )
        sys.stdout.write(content)
        if not content.endswith("\n"):
            sys.stdout.write("\n")
    else:
        for result in install(
            arguments.import_package,
            arguments.platform,
            project=arguments.project,
            user=arguments.user,
            force=arguments.force,
        ):
            sys.stdout.write(f"{result.status}: {result.path}\n")


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point: 0 success, 1 conflict, 2 operational/argument error."""
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    show = commands.add_parser(
        "show", help="Read a package's agent guide or linked resource"
    )
    show.add_argument("import_package")
    show.add_argument("relative_resource", nargs="?", default="README_AI.md")
    deploy = commands.add_parser(
        "install", help="Install one import package's skill"
    )
    deploy.add_argument("import_package")
    deploy.add_argument(
        "--platform", choices=[*PLATFORMS, "all"], nargs="+", required=True
    )
    scope = deploy.add_mutually_exclusive_group(required=True)
    scope.add_argument("--project", type=Path)
    scope.add_argument("--user", action="store_true")
    deploy.add_argument("--force", action="store_true")
    arguments = parser.parse_args(argv)
    try:
        _run(arguments)
    except SkillConflict as exc:
        sys.stderr.write(f"agent_skill: {exc}\n")
        return CONFLICT
    except (SkillError, OSError, UnicodeError) as exc:
        sys.stderr.write(f"agent_skill: {exc}\n")
        return OPERATIONAL_ERROR
    return SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())
