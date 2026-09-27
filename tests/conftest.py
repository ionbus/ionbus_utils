"""Shared pytest fixtures for ionbus_utils tests."""

from __future__ import annotations

import sys
import tempfile
from collections.abc import Iterator
from pathlib import Path

import pytest

# Prefer this checkout over another installed version of ionbus_utils.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


@pytest.fixture
def temp_dir() -> Iterator[Path]:
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def temp_file(temp_dir: Path) -> Path:
    """Create a temporary file for tests."""
    filepath = temp_dir / "test_file.txt"
    filepath.write_text("test content")
    return filepath


@pytest.fixture
def crypto_key_env(monkeypatch: pytest.MonkeyPatch) -> str:
    """Set up a test encryption key in the environment."""
    # This is a test key - do not use in production
    # cSpell: ignore Gtle
    test_key = "personal:dGVzdGtleTEyMzQ1Njc4"
    monkeypatch.setenv("IBU_AESGCM", test_key)
    return test_key


@pytest.fixture
def auth_env(
    temp_dir: Path,
    crypto_key_env: str,  # noqa: ARG001 -- pytest dependency sets up encryption.
    monkeypatch: pytest.MonkeyPatch,
) -> dict[str, Path | str]:
    """Set up test authentication environment."""
    auth_file = temp_dir / "test_auth.yaml"
    auth_content = """username: testuser
key_name: personal
encrypted_salt: test_encrypted_value
"""
    auth_file.write_text(auth_content)
    env_value = f"test::{auth_file}"
    monkeypatch.setenv("IBU_AUTH", env_value)
    return {"file": auth_file, "env_value": env_value}
