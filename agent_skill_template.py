"""Copy-and-adapt outline for a package-owned agent skill mechanism.

This is a design template, not an executable fallback. Copy this file and
adapt it for your package; use agent_skill.py as the working implementation
reference. The real Ionbus installer does not import this template.
"""

from __future__ import annotations

from importlib import resources


def read_guide(import_package: str) -> str:
    """Example resource access; validate inputs when adapting this template."""
    return (
        resources.files(import_package)
        .joinpath("README_AI.md")
        .read_text(encoding="utf-8")
    )


def generate_stub(
    import_package: str, skill_identifier: str, reader_module: str
) -> str:
    """Example stub using your own validated reader module name."""
    return (
        "---\n"
        f"name: {skill_identifier}\n"
        f"description: Use when integrating {import_package}; "
        "read its installed API guide.\n"
        "---\n\n"
        f"# {import_package} package guidance\n\n"
        "Use the Python environment selected for the current project.\n\n"
        f"    python -m {reader_module} show {import_package}\n"
    )


# Before making an adapted installer runnable, implement and validate:
# - safe package identifiers, normalization collisions, and resource paths;
# - explicit platform and scope selection, with destination containment;
# - import/resource preflight followed by all-destination content preflight;
# - identical-file no-ops, explicit --force, and atomic UTF-8/LF writes;
# - named partial successes and distinct success/conflict/operational exits;
# - packaged-resource and cross-platform tests.
