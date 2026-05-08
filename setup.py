"""used to package ionbus_utils"""

from __future__ import annotations

import os
import re
import subprocess
from glob import glob
from pathlib import Path

from setuptools import setup

VERSION_FILE = Path("_version.py")
VERSION_RE = re.compile(r'__version__\s*=\s*["\']([^"\']+)["\']')


def get_release_tag() -> str | None:
    """Return the exact release tag from env/git, or None if unavailable."""
    env_tag = os.environ.get("GIT_DESCRIBE_TAG", "").strip()
    if env_tag:
        return env_tag

    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--exact-match"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def write_version_file(version: str) -> None:
    """Write the package runtime version source."""
    VERSION_FILE.write_text(
        f'__version__ = "{version}"\n',
        encoding="utf-8",
    )


def read_version_file() -> str:
    """Read the package runtime version source."""
    if not VERSION_FILE.exists():
        write_version_file("0.0.0")
    match = VERSION_RE.search(VERSION_FILE.read_text(encoding="utf-8"))
    if not match:
        raise RuntimeError(f"Could not read version from {VERSION_FILE}")
    return match.group(1)


avoid_regexes = [
    re.compile(f"^{x}$")
    for x in [
        r"\d+",
        "build",
        "egg-info",
        "__pycache__",
        "log",
        ".+egg-info",
        "dist",
    ]
]


def ok_dir(name: str) -> bool:
    """Returns ok if we should keep"""
    return all(not regex.search(name) for regex in avoid_regexes)


if release_tag := get_release_tag():
    write_version_file(release_tag)

package_version = read_version_file()

all_dirs = [x for x in glob("*") if os.path.isdir(x) and ok_dir(x)]
packages = ["ionbus_utils"] + [f"ionbus_utils/{x}" for x in all_dirs]
package_dirs = {
    "ionbus_utils": ".",
}
package_dirs.update({f"ionbus_utils/{x}": f"./{x}" for x in all_dirs})

# Read the pip-specific readme for PyPI
with open("readme_pip.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="ionbus-utils",
    version=package_version,
    packages=packages,
    package_dir=package_dirs,
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        "ionbus_utils": [
            "resources/*.pem",
            "resources/*.pkl.gz",
            "*.md",
            "*/*.md",
        ]
    },
)
