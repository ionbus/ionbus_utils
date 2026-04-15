#!/usr/bin/env bash
# Build and publish ionbus-utils to PyPI and Anaconda.
# Prereqs: activate an env that has: build, twine, conda-build, anaconda-client.
# Auth: ~/.pypirc for PyPI, `anaconda login` for Anaconda (or ANACONDA_API_TOKEN).
#
# Usage:
#   ./release.sh               # requires HEAD to already be tagged
#   ./release.sh --tag         # run auto_tag to create+push a new tag first
#   ./release.sh --test        # upload pip wheel to TestPyPI instead of PyPI
#   ./release.sh --conda-only  # skip pip build/upload; only build + upload conda
#   ./release.sh --skip-pip    # build pip wheel but don't upload (still do conda)
#   flags can be combined: ./release.sh --tag --conda-only

set -euo pipefail

ANACONDA_USER="ionbus"

do_tag=0
test_pypi=0
conda_only=0
skip_pip_upload=0
for arg in "$@"; do
    case "$arg" in
        --tag)        do_tag=1 ;;
        --test)       test_pypi=1 ;;
        --conda-only) conda_only=1 ;;
        --skip-pip)   skip_pip_upload=1 ;;
        *) echo "Unknown arg: $arg" >&2; exit 2 ;;
    esac
done

cd "$(dirname "$0")"

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

echo "=== Cleaning previous build artifacts ==="
rm -rf dist build
rm -rf ./*.egg-info

if [ "$conda_only" -eq 1 ]; then
    echo "=== Skipping pip build+upload (--conda-only) ==="
else
    echo "=== Building pip wheel ==="
    python -m build --wheel

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

echo "=== Resolving conda output path ==="
CONDA_PKG=$(conda build conda-recipe -c conda-forge --output)
echo "Will build: $CONDA_PKG"

echo "=== Building conda package ==="
conda build conda-recipe -c conda-forge

echo "=== Uploading to Anaconda (user: $ANACONDA_USER) ==="
anaconda upload --user "$ANACONDA_USER" "$CONDA_PKG"

echo "=== Done: released $TAG ==="
