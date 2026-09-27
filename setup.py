"""used to package ionbus_utils"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

from setuptools import find_packages, setup

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


if release_tag := get_release_tag():
    write_version_file(release_tag)

package_version = read_version_file()

# Source lives at the repository root. Include only real subpackages;
# developer outputs, build directories, and tests are not runtime packages.
subpackages = find_packages(
    exclude=("tests", "tests.*", "build", "build.*", "dist", "dist.*")
)
packages = ["ionbus_utils"] + [f"ionbus_utils.{name}" for name in subpackages]
package_dirs = {"ionbus_utils": "."}

# Read the pip-specific readme for PyPI
with open("README_PIP.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="ionbus-utils",
    version=package_version,
    packages=packages,
    package_dir=package_dirs,
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        "": ["README*.md"],
        "ionbus_utils": [
            "resources/*.pem",
            "resources/*.pkl.gz",
            "logging.md",
            "cache_utils.md",
            "file_utils.md",
            "pandas_utils.md",
            "subprocess_utils.md",
            "time_utils.md",
        ],
    },
    include_package_data=False,
)
