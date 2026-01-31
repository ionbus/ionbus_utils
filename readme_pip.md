# ionbus_utils

A collection of Python utilities for common development tasks including
logging, cryptography, file operations, date/time handling, caching,
pandas operations, subprocess management, and configuration management.

## Installation

```bash
pip install ionbus-utils
```

Or install from source:

```bash
pip install -e .
```

## Modules

| Module | Description |
|--------|-------------|
| `logging_utils` | Enhanced logging with timestamps, custom levels, and `warn_once()` |
| `file_utils` | File operations, hashing, compression, log file management |
| `yaml_utils` | `PDYaml` class extending Pydantic with YAML support |
| `crypto_utils` | AES-128-GCM encryption and authentication file management |
| `time_utils` | DateTime/Timestamp utilities, timezone handling, time rounding |
| `subprocess_utils` | Cross-platform subprocess management and process control |
| `cache_utils` | File-based and in-memory caching with thread-safe operations |
| `pandas_utils` | DataFrame manipulation, rollup operations, markdown export |
| `base_utils` | Base conversion (2-64) and platform detection |
| `enumerate` | C++-style enumerations with bit flags and key-value support |
| `group_utils` | User and group utilities (cross-platform) |
| `exceptions` | Exception formatting and logging helpers |
| `regex_utils` | Pre-compiled regex patterns for common string operations |
| `date_utils` | Date conversion, month boundaries, ISO formatting |
| `general` | JSON loading, string/list utilities, compression helpers |
| `general_classes` | Generic utility classes (DictClass, ArgParseRangeAction) |
| `git_utils` | Git repository management, tagging, submodule handling |

## Requirements

- Python >= 3.9
- See `requirements.txt` for dependencies

## License

MIT License
