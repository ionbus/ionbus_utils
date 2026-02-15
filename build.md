# Building and Publishing ionbus-utils

This guide covers building and uploading ionbus-utils to both PyPI (pip) and
Anaconda (conda).

## Prerequisites

Create a conda environment with build tools:

```bash
conda create -n py311_dev python=3.11 -c conda-forge build wheel twine conda-build anaconda-client cryptography duckdb packaging "pandas<3.0.0" polars pyarrow pydantic pytest pyyaml requests setuptools typing_extensions -y
```

Activate the environment:

```bash
conda activate py311_dev
```

## PyPI (pip)

### Build

```bash
# Clean previous builds
rmdir /s /q dist build *.egg-info

# Build wheel
python -m build --wheel
```

The wheel will be created in the `dist/` directory.

### Upload to Test PyPI

```bash
python -m twine upload --repository testpypi dist/*
```

When prompted:
- **Username:** `__token__`
- **Password:** Your TestPyPI API token (starts with `pypi-`)

To get an API token:
1. Go to https://test.pypi.org/manage/account/token/
2. Click "Add API token"
3. Name it and select scope
4. Copy the token (you won't see it again)

### Upload to Production PyPI

```bash
python -m twine upload dist/*
```

Use your production PyPI token from https://pypi.org/manage/account/token/

### Optional: Configure ~/.pypirc

Create `~/.pypirc` to avoid entering credentials each time:

```ini
[pypi]
username = __token__
password = pypi-YOUR_PRODUCTION_TOKEN

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_TOKEN
```

### Version Note

PyPI does not allow local versions (e.g., `1.0.0+git.abc123`). If you get this
error, either:
1. Tag the current commit: `git tag 1.0.x`
2. Or use `--no-isolation` when building: `python -m build --wheel --no-isolation`

## Anaconda (conda)

### Setup (One-time)

1. Create an account at https://anaconda.org/
2. Your channel is automatically created at `https://anaconda.org/<username>`

### Build

```bash
# From the ionbus_utils directory
conda build conda-recipe -c conda-forge
```

The package will be built to `C:\Users\<user>\conda-bld\win-64\` (or
`noarch/` for pure Python packages).

### Login to Anaconda

```bash
anaconda login
```

Enter your Anaconda.org username and password.

### Upload

```bash
anaconda upload C:\Users\cplag\conda-bld\win-64\ionbus-utils-<version>-py<pyver>_0.conda
```

Or with explicit user:

```bash
anaconda upload --user ionbus C:\Users\cplag\conda-bld\win-64\ionbus-utils-<version>-py<pyver>_0.conda
```

### Install from Your Channel

```bash
conda install -c ionbus ionbus-utils
```

## Tagging a Release

Before building, tag the release:

```bash
# Manual tag
git tag 1.0.x
git push --tags

# Or use auto_tag (generates version from commit message hashtags)
python -m ionbus_utils.git_utils.auto_tag .
```

See [git_utils/readme.md](git_utils/readme.md#version-hashtags) for hashtag
conventions (`#Major`, `#Minor`, `#Inc`, `#Fix`, `#RC`, `#Prod`).

## Quick Reference

| Task | Command |
|------|---------|
| Build wheel | `python -m build --wheel` |
| Upload to TestPyPI | `twine upload --repository testpypi dist/*` |
| Upload to PyPI | `twine upload dist/*` |
| Build conda | `conda build conda-recipe -c conda-forge` |
| Login to Anaconda | `anaconda login` |
| Upload to Anaconda | `anaconda upload <path-to-.conda>` |
| Create tag | `git tag 1.0.x && git push --tags` |