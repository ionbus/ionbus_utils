#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="${ENV_NAME:-pixi_313_pd22}"
RUN_ENV="${HOME}/bin/python_env_management/run_env.sh"
MODE="${1:-build-pip}"
TAG_FLAG=""
ANY_BRANCH=""
ALLOW_DIRTY=""
CREATED_TAG=""
RELEASE_TAG=""
ANACONDA_USER="ionbus"

usage() {
  echo "Usage:"
  echo "  $0 [all|build|send|build-pip|send-pip|build-conda|send-conda]"
  echo "     [--tag] [--any-branch] [--allow-dirty]"
  echo "  all: build and publish Python and conda artifacts"
  echo "  build: build Python and conda artifacts locally"
  echo "  send: publish Python and conda artifacts"
  echo "  build-pip: build Python artifacts locally"
  echo "  send-pip: publish Python artifacts"
  echo "  build-conda: build conda artifact locally"
  echo "  send-conda: publish conda artifact"
  echo "  --tag: create and verify a new local git tag before running"
  echo "  --any-branch: skip the main-branch check"
  echo "  --allow-dirty: allow only build-conda to build a local test artifact"
}

for arg in "$@"; do
  case "$arg" in
    -h|--help|help) usage; exit 0 ;;
  esac
done

for arg in "${@:2}"; do
  case "$arg" in
    --tag) TAG_FLAG="--tag" ;;
    --any-branch) ANY_BRANCH="--any-branch" ;;
    --allow-dirty) ALLOW_DIRTY="--allow-dirty" ;;
    *) usage; exit 2 ;;
  esac
done

if [[ ! -x "$RUN_ENV" ]]; then
  echo "ERROR: could not find run_env.sh at $RUN_ENV"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONDA_BLD_DIR="${CONDA_BLD_DIR:-$(dirname "$ROOT_DIR")/ionbus_utils_conda-bld}"
cd "$ROOT_DIR"

case "$MODE" in
  all|build|send|build-pip|send-pip|build-conda|send-conda) ;;
  *) usage; exit 2 ;;
esac

if [[ -n "$ALLOW_DIRTY" && "$MODE" != "build-conda" ]]; then
  echo "ERROR: --allow-dirty is only supported with build-conda." >&2
  exit 2
fi
if [[ -n "$ALLOW_DIRTY" && -n "$TAG_FLAG" ]]; then
  echo "ERROR: --allow-dirty cannot be combined with --tag." >&2
  exit 2
fi

verify_main_branch() {
  local branch

  branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
  if [[ "$branch" != "main" ]]; then
    echo "ERROR: not on main branch (currently on '$branch')." >&2
    echo "Use --any-branch to override." >&2
    exit 1
  fi
}

verify_clean_tree() {
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "ERROR: release requires a clean git tree." >&2
    git status --short >&2
    exit 1
  fi
}

verify_head_tag() {
  local expected_tag="${1:-}"
  local current_tag

  current_tag="$(git describe --tags --exact-match 2>/dev/null || true)"
  if [[ -z "$current_tag" ]]; then
    echo "ERROR: HEAD is not tagged." >&2
    exit 1
  fi
  if [[ -n "$expected_tag" && "$current_tag" != "$expected_tag" ]]; then
    echo "ERROR: expected HEAD tag '$expected_tag' but found '$current_tag'" >&2
    exit 1
  fi
}

get_next_tag_name() {
  local output tag

  output="$(
    "$RUN_ENV" "$ENV_NAME" \
      python3 -m ionbus_utils.git_utils.auto_tag . --name-only 2>&1
  )"
  tag="$(
    printf '%s\n' "$output" \
      | sed -nE "s/.*tag='([^']+)'.*/\1/p" \
      | tail -n 1
  )"
  if [[ -z "$tag" ]]; then
    tag="$(printf '%s\n' "$output" | awk 'NF { print }' | tail -n 1)"
  fi
  printf '%s\n' "$tag"
}

maybe_tag_release() {
  if [[ "$TAG_FLAG" == "--tag" ]]; then
    verify_clean_tree
    CREATED_TAG="$(get_next_tag_name)"
    if [[ -z "$CREATED_TAG" ]]; then
      echo "ERROR: failed to compute new tag name"
      exit 1
    fi
    if git rev-parse -q --verify "refs/tags/$CREATED_TAG" >/dev/null; then
      echo "ERROR: tag '$CREATED_TAG' already exists locally"
      exit 1
    fi
    git tag -a "$CREATED_TAG" -m "auto-tag $CREATED_TAG"
    verify_head_tag "$CREATED_TAG"
    echo "Created local tag: $CREATED_TAG"
  fi
}

ensure_release_context() {
  if [[ -z "$ALLOW_DIRTY" ]]; then
    verify_clean_tree
  else
    echo "WARNING: building local conda test artifact from a dirty tree." >&2
  fi
  verify_head_tag
  RELEASE_TAG="$(git describe --tags --exact-match)"
  export GIT_DESCRIBE_TAG="$RELEASE_TAG"
}

cleanup_python_artifacts() {
  rm -rf build dist
  find . -maxdepth 1 -name "*.egg-info" -exec rm -rf {} +
}

cleanup_conda_artifacts() {
  rm -rf "$CONDA_BLD_DIR"
}

verify_python_artifacts() {
  local tag="$1"

  "$RUN_ENV" "$ENV_NAME" python3 - "$tag" <<'PY' || {
import pathlib
import sys

tag = sys.argv[1]
dist = pathlib.Path("dist")
files = sorted(dist.iterdir()) if dist.is_dir() else []
wheel = [path for path in files if path.suffix == ".whl" and tag in path.name]
sdist = [
    path
    for path in files
    if path.name.endswith(".tar.gz") and tag in path.name
]
sys.exit(0 if wheel and sdist else 1)
PY
    echo "ERROR: expected wheel and sdist for tag $tag in dist/"
    exit 1
  }
}

verify_built_package_versions() {
  local tag="$1"

  "$RUN_ENV" "$ENV_NAME" python3 - "$tag" <<'PY' || {
import email.parser
import io
import pathlib
import re
import sys
import tarfile
import zipfile

tag = sys.argv[1]
wheels = sorted(pathlib.Path("dist").glob(f"*{tag}*.whl"))
if len(wheels) != 1:
    raise SystemExit(f"expected exactly one wheel for {tag}, found {len(wheels)}")

sdists = sorted(pathlib.Path("dist").glob(f"*{tag}*.tar.gz"))
if len(sdists) != 1:
    raise SystemExit(f"expected exactly one sdist for {tag}, found {len(sdists)}")

version_re = re.compile("__version__\\s*=\\s*([\\\"\\x27])([^\\\"\\x27]+)\\1")


def parse_metadata_version(text):
    metadata = email.parser.Parser().parsestr(text)
    return metadata["Version"]


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
    metadata_version = parse_metadata_version(
        zf.read(metadata_names[0]).decode("utf-8")
    )
    version_text = zf.read(version_names[0]).decode("utf-8")
    runtime_match = version_re.search(version_text)
    runtime_version = runtime_match.group(2) if runtime_match else None

with tarfile.open(sdists[0], "r:gz") as tf:
    names = tf.getnames()
    pkg_info_names = [
        n for n in names if n.count("/") == 1 and n.endswith("/PKG-INFO")
    ]
    if len(pkg_info_names) != 1:
        raise SystemExit(
            f"expected exactly one sdist PKG-INFO file, found {len(pkg_info_names)}"
        )
    member = tf.extractfile(pkg_info_names[0])
    if member is None:
        raise SystemExit(f"could not read {pkg_info_names[0]}")
    sdist_metadata_version = parse_metadata_version(
        io.TextIOWrapper(member, encoding="utf-8").read()
    )

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
if sdist_metadata_version != tag:
    raise SystemExit(
        f"sdist metadata version {sdist_metadata_version!r} does not match tag {tag!r}"
    )
PY
    echo "ERROR: built package metadata/runtime version verification failed"
    exit 1
  }
}

build_pip_artifacts() {
  local tag

  ensure_release_context
  tag="$RELEASE_TAG"
  cleanup_python_artifacts

  if "$RUN_ENV" "$ENV_NAME" python3 -c "import build" >/dev/null 2>&1; then
    if ! "$RUN_ENV" "$ENV_NAME" python3 -m build \
      --no-isolation \
      --skip-dependency-check; then
      "$RUN_ENV" "$ENV_NAME" python3 setup.py sdist bdist_wheel
    fi
  else
    "$RUN_ENV" "$ENV_NAME" python3 setup.py sdist bdist_wheel
  fi

  if "$RUN_ENV" "$ENV_NAME" python3 -c "import twine" >/dev/null 2>&1; then
    "$RUN_ENV" "$ENV_NAME" python3 -m twine check dist/*
  else
    echo "WARNING: twine is not installed in $ENV_NAME; skipping twine check"
  fi

  verify_python_artifacts "$tag"
  verify_built_package_versions "$tag"
  echo "Built Python artifacts in: $ROOT_DIR/dist"
}

get_conda_build_exe() {
  local conda_build_exe

  conda_build_exe="$(
    "$RUN_ENV" "$ENV_NAME" which conda-build 2>/dev/null || true
  )"
  if [[ -n "$conda_build_exe" ]]; then
    printf '%s\n' "$conda_build_exe"
    return 0
  fi
  if command -v conda >/dev/null 2>&1; then
    printf '%s\n' "conda"
    return 0
  fi
  echo "ERROR: conda-build is not available in $ENV_NAME and conda is not on PATH"
  exit 1
}

get_anaconda_exe() {
  local anaconda_exe

  anaconda_exe="$(
    "$RUN_ENV" "$ENV_NAME" which anaconda 2>/dev/null || true
  )"
  if [[ -n "$anaconda_exe" ]]; then
    printf '%s\n' "$anaconda_exe"
    return 0
  fi
  if command -v anaconda >/dev/null 2>&1; then
    printf '%s\n' "anaconda"
    return 0
  fi
  echo "ERROR: anaconda-client is not available in $ENV_NAME and anaconda is not on PATH"
  exit 1
}

get_conda_output_path() {
  local conda_build_exe

  conda_build_exe="$(get_conda_build_exe)"
  if [[ "$conda_build_exe" == "conda" ]]; then
    conda build conda-recipe \
      -c conda-forge \
      --croot "$CONDA_BLD_DIR" \
      --output \
      | tail -n 1
  else
    "$conda_build_exe" conda-recipe \
      -c conda-forge \
      --croot "$CONDA_BLD_DIR" \
      --output \
      | tail -n 1
  fi
}

verify_conda_artifact() {
  local conda_output_path="$1"
  local tag="$2"

  if [[ ! -f "$conda_output_path" ]]; then
    echo "ERROR: expected conda artifact is missing:" >&2
    echo "  $conda_output_path" >&2
    exit 1
  fi
  if [[ "$(basename "$conda_output_path")" != *"$tag"* ]]; then
    echo "ERROR: conda artifact does not contain tag $tag:" >&2
    echo "  $conda_output_path" >&2
    exit 1
  fi
}

build_conda_artifacts() {
  local conda_build_exe conda_output_path tag

  ensure_release_context
  tag="$RELEASE_TAG"
  cleanup_conda_artifacts

  conda_build_exe="$(get_conda_build_exe)"
  conda_output_path="$(get_conda_output_path)"
  if [[ "$conda_build_exe" == "conda" ]]; then
    conda build conda-recipe -c conda-forge --croot "$CONDA_BLD_DIR"
  else
    "$conda_build_exe" conda-recipe \
      -c conda-forge \
      --croot "$CONDA_BLD_DIR"
  fi

  verify_conda_artifact "$conda_output_path" "$tag"
  echo "Built conda artifact: $conda_output_path"
}

send_pip_artifacts() {
  local tag

  ensure_release_context
  tag="$RELEASE_TAG"
  verify_python_artifacts "$tag"
  verify_built_package_versions "$tag"

  "$RUN_ENV" "$ENV_NAME" python3 -m twine upload dist/*
}

send_conda_artifacts() {
  local anaconda_exe conda_output_path tag

  ensure_release_context
  tag="$RELEASE_TAG"
  conda_output_path="$(get_conda_output_path)"
  verify_conda_artifact "$conda_output_path" "$tag"

  anaconda_exe="$(get_anaconda_exe)"
  "$anaconda_exe" -s anaconda.org upload \
    -u "$ANACONDA_USER" \
    "$conda_output_path"
}

build_release() {
  build_pip_artifacts
  build_conda_artifacts
  echo
  echo "Version/tag used: $RELEASE_TAG"
}

send_release() {
  send_pip_artifacts
  send_conda_artifacts
}

all_release() {
  build_release
  send_release
}

[[ -n "$ANY_BRANCH" ]] || verify_main_branch
maybe_tag_release

case "$MODE" in
  all) all_release ;;
  build) build_release ;;
  send) send_release ;;
  build-pip) build_pip_artifacts ;;
  send-pip) send_pip_artifacts ;;
  build-conda) build_conda_artifacts ;;
  send-conda) send_conda_artifacts ;;
esac
