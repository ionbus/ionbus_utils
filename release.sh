#!/usr/bin/env bash
# Build and publish ionbus-utils to PyPI and Anaconda.
# Prereqs: activate an env that has: build, twine, conda-build, anaconda-client.
# Auth: ~/.pypirc for PyPI, `anaconda login` for Anaconda (or ANACONDA_API_TOKEN).

set -euo pipefail

ANACONDA_USER="ionbus"

show_help() {
    cat <<'EOF'
Usage: ./release.sh [options]

Builds and publishes ionbus-utils to PyPI and Anaconda.

By default: requires HEAD to be tagged, then builds+uploads BOTH the pip
wheel (to PyPI) and the conda package (to Anaconda under "ionbus").

Options:
  -h, --help      Show this help and exit.
  --tag           Before building, run auto_tag to create and push a new
                  tag from commit-message hashtags (#Major/#Minor/#Inc/
                  #Fix/#RC/#Prod).
  --test          Upload the pip wheel to TestPyPI instead of PyPI.
                  Ignored if --pip-only is not used and the conda step
                  still runs normally. No effect with --conda-only.
  --pip-only      Build and upload ONLY the pip wheel. Skip the conda
                  build and Anaconda upload entirely.
  --conda-only    Build and upload ONLY the conda package. Skip the pip
                  wheel build and PyPI upload entirely.
  --skip-pip      Build the pip wheel but do not upload it. The conda
                  build and upload still run. Useful for verifying the
                  wheel builds cleanly.
  --any-branch    Skip the requirement to be on the main branch.

Flags can be combined, e.g. --tag --conda-only.
Mutually exclusive: --pip-only and --conda-only.

Examples:
  ./release.sh                       # full release (pip + conda)
  ./release.sh --tag                 # auto-create tag, then full release
  ./release.sh --pip-only            # pip only, to PyPI
  ./release.sh --pip-only --test     # pip only, to TestPyPI
  ./release.sh --conda-only          # conda only
  ./release.sh --skip-pip            # build wheel (no upload), push conda
  ./release.sh --any-branch          # release from a non-main branch
EOF
}

do_tag=0
test_pypi=0
conda_only=0
pip_only=0
skip_pip_upload=0
any_branch=0
for arg in "$@"; do
    case "$arg" in
        -h|--help)    show_help; exit 0 ;;
        --tag)        do_tag=1 ;;
        --test)       test_pypi=1 ;;
        --conda-only) conda_only=1 ;;
        --pip-only)   pip_only=1 ;;
        --skip-pip)   skip_pip_upload=1 ;;
        --any-branch) any_branch=1 ;;
        *) echo "Unknown arg: $arg" >&2; echo "Run with --help for usage." >&2; exit 2 ;;
    esac
done

if [ "$pip_only" -eq 1 ] && [ "$conda_only" -eq 1 ]; then
    echo "ERROR: --pip-only and --conda-only are mutually exclusive." >&2
    exit 2
fi

cd "$(dirname "$0")"

echo "=== Verifying branch ==="
CURRENT_BRANCH=$(git branch --show-current)
if [ "$any_branch" -eq 0 ] && [ "$CURRENT_BRANCH" != "main" ]; then
    echo "ERROR: on branch '$CURRENT_BRANCH', not 'main'. Use --any-branch to override." >&2
    exit 1
fi
echo "Branch: $CURRENT_BRANCH"

if [ "$do_tag" -eq 1 ]; then
    echo "=== Running auto_tag ==="
    python git_utils/auto_tag.py . --throw-on-failure
fi

echo "=== Verifying HEAD is tagged ==="
if ! git describe --exact-match --tags HEAD >/dev/null 2>&1; then
    echo "ERROR: HEAD is not tagged. Create a new tag (e.g. re-run with --tag)." >&2
    exit 1
fi
TAG=$(git describe --exact-match --tags HEAD)
echo "HEAD tag: $TAG"
export GIT_DESCRIBE_TAG="$TAG"

verify_built_package_version() {
    python -c '
import email.parser
import pathlib
import re
import sys
import zipfile

tag = sys.argv[1]
wheels = sorted(pathlib.Path("dist").glob(f"*{tag}*.whl"))
if len(wheels) != 1:
    raise SystemExit(f"expected exactly one wheel for {tag}, found {len(wheels)}")

version_re = re.compile("__version__\\s*=\\s*([\\\"\\x27])([^\\\"\\x27]+)\\1")

with zipfile.ZipFile(wheels[0]) as zf:
    names = zf.namelist()
    metadata_names = [n for n in names if n.endswith(".dist-info/METADATA")]
    if len(metadata_names) != 1:
        raise SystemExit(
            f"expected exactly one wheel METADATA file, found {len(metadata_names)}"
        )
    version_names = [n for n in names if n == "ionbus_utils/_version.py"]
    if len(version_names) != 1:
        raise SystemExit(
            f"expected exactly one wheel _version.py, found {len(version_names)}"
        )

    metadata = email.parser.Parser().parsestr(
        zf.read(metadata_names[0]).decode("utf-8")
    )
    metadata_version = metadata["Version"]
    version_text = zf.read(version_names[0]).decode("utf-8")
    runtime_match = version_re.search(version_text)
    runtime_version = runtime_match.group(2) if runtime_match else None

if runtime_version is None:
    raise SystemExit("could not read runtime version from wheel _version.py")
if metadata_version != runtime_version:
    raise SystemExit(
        "package metadata version does not match runtime version: "
        f"{metadata_version!r} != {runtime_version!r}"
    )
if metadata_version != tag:
    raise SystemExit(
        f"package metadata version {metadata_version!r} does not match tag {tag!r}"
    )
    ' "$1"
}

echo "=== Cleaning previous build artifacts ==="
rm -rf dist build
rm -rf ./*.egg-info

if [ "$conda_only" -eq 1 ]; then
    echo "=== Skipping pip build+upload (--conda-only) ==="
else
    echo "=== Building pip wheel ==="
    python -m build --wheel
    verify_built_package_version "$TAG"

    if [ "$skip_pip_upload" -eq 1 ]; then
        echo "=== Skipping pip upload (--skip-pip) ==="
    elif [ "$test_pypi" -eq 1 ]; then
        echo "=== Uploading to TestPyPI ==="
        python -m twine upload --repository testpypi dist/*
    else
        echo "=== Uploading to PyPI ==="
        python -m twine upload dist/*
    fi
fi

if [ "$pip_only" -eq 1 ]; then
    echo "=== Skipping conda build+upload (--pip-only) ==="
    echo "=== Done: released $TAG (pip only) ==="
    exit 0
fi

# Force win-64 solver on Windows ARM (conda-forge lacks win-arm64 python).
# Harmless on other platforms that already have native python builds.
case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*) export CONDA_SUBDIR="win-64" ;;
esac

echo "=== Resolving conda output path ==="
CONDA_PKG=$(conda build conda-recipe -c conda-forge --output)
echo "Will build: $CONDA_PKG"

echo "=== Building conda package ==="
conda build conda-recipe -c conda-forge

echo "=== Uploading to Anaconda (user: $ANACONDA_USER) ==="
anaconda upload --user "$ANACONDA_USER" "$CONDA_PKG"

echo "=== Done: released $TAG ==="
