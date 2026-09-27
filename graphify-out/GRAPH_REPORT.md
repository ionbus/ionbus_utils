# Graph Report - ionbus_utils  (2026-09-27)

## Corpus Check
- Corpus is ~45,350 words - fits in a single context window. You may not need a graph.

## Summary
- 1722 nodes · 2610 edges · 140 communities (119 shown, 21 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 385 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Git Repository Operations
- Time Scheduling and Zones
- DataFrame Transformations
- Authentication File Creation
- In Memory Caching
- File Times and Logfiles
- YAML Tree Lifecycle
- Dictionary Attribute Objects
- Exception Formatting and Logging
- Integer Base Conversion
- Test Imports and Bootstrap
- Date and Time Tests
- Conditional Severity Logging
- DataFrame Utility Tests
- Subprocess Utility Tests
- YAML Defaults and Serialization
- Date Conversion and Partitioning
- File Hashing
- Date Conversion Tests
- Enums and Compression
- Disk Cache Loading
- General Platform Helpers
- Authentication Credential Retrieval
- Password Encryption
- Numeric String Parsing
- Value Hashing
- Logger Configuration
- ISO Date String Tests
- Documented Time and Identifiers
- YAML File Loading
- Logging Registration and Warnings
- Git Tag and Status Tests
- Enumerate Objects
- Argument Count Validation
- Base Utility Imports
- Git Branch Workspace Creation
- Base String Parsing
- Platform Detection
- Date String Parsing
- Gzip File Compression
- User Name Lookup
- Sequence Type Detection
- Cache File Selection Tests
- Package API Overview
- Package Usage and Concurrency
- Runtime Dependency Contracts
- CLI Parser Dependencies
- Enumeration Key Operations
- JSON Comment Removal
- Package Build and Versioning
- User Group Lookup
- Documented Logging and Exceptions
- Documented YAML Configuration
- YAML Thread Root Tracking
- Subprocess Object Lifecycle
- Compact UUID Generation
- Authentication Environment Parsing
- File Touch Operations
- Username Cleanup
- Comma List Formatting
- String Enum Conversion
- Release Script Validation
- Test Files and Crypto Fixtures
- Hierarchical YAML Value Lookup
- Shared Logging Imports
- Module File Path Lookup
- YAML Initialization Tests
- Proposed Agent Skill Installation
- Byte String Conversion
- Generic Attribute Objects
- JSON File Loading
- JSON String Loading
- Temporary Directory Changes
- Group Membership Lookup
- Month Start Calculation
- Month End Calculation
- ISO Date Normalization
- Comma and Semicolon Splitting
- Leading Underscore Removal
- Newline Splitting
- YAML Parent Child Relationships
- Cryptography Dependency Imports
- Documented Cache Contracts
- Single File Moving
- Named Tuple Conversion
- Git CLI Argument Setup
- Command Execution
- Whitespace Regex Replacement
- Authentication YAML Registration
- Enumeration Value Validation
- Comma String Conversion
- Multiline Comma Formatting
- Recursive Dictionary Key Normalization
- Timestamped Unique Identifiers
- Timestamped Identifiers
- Documented Subprocess Contracts
- Next Month Calculation
- Warn Once Behavior
- Notice Logging Registration
- Word Character Filtering
- Digit Filtering
- Documented Authentication Contracts
- Module Name Lookup
- Documented Git Release Contracts
- Base Conversion Round Trips
- Git Remote Name Parsing
- String Enum Compatibility
- Batch Git Command Execution
- Log Level Configuration
- Logging Configuration Exceptions
- YAML String Factories
- Encryption Key Retrieval
- Git Utility Entrypoints
- Authentication Test Fixtures
- Conditional Debug Logging
- Conditional Info Logging
- Conditional Notice Logging
- YAML Object Factories
- YAML Package Exports
- Shared Regex Patterns
- Linux Child Process Discovery
- Latest Cache File Selection
- Current Cache File Loading
- Test Package Metadata
- Enumeration Key Validation Tests
- Enumeration Value Validation Tests
- Enumeration Value Collection Tests
- Enumeration Iteration Tests
- Enumeration Callable Lookup Tests
- Enumeration String Representation Tests
- Enumeration Attribute Error Tests
- Enumeration String Initialization Tests
- Enumeration List Initialization Tests
- Enumeration Dictionary Initialization Tests
- Enumeration Integer Mode Tests
- Enumeration Bitflag Mode Tests
- Enumeration Key Value Tests
- Enumeration Integer Value Tests
- Enumeration Prefix Value Tests
- Package Metadata

## God Nodes (most connected - your core abstractions)
1. `Enumerate` - 36 edges
2. `TestEnumerate` - 25 edges
3. `PDYaml` - 23 edges
4. `Human package documentation` - 22 edges
5. `int_to_base()` - 20 edges
6. `to_date()` - 18 edges
7. `DictClass` - 17 edges
8. `Agent package usage reference` - 16 edges
9. `to_date_isoformat()` - 15 edges
10. `get_logfile_name()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Legacy ionbus.yaml_utils imports in YAML examples` --conceptually_related_to--> `Agent package usage reference`  [AMBIGUOUS]
  yaml_utils/readme.md → readme_ai.md
- `Explicit Python environment selection` --semantically_similar_to--> `Pytest package test workflow`  [INFERRED] [semantically similar]
  AGENT_PROJECT_SETUP.md → readme.md
- `Proposed skill write preflight and atomic replacement` --semantically_similar_to--> `verify_ready_to_push documented contract`  [INFERRED] [semantically similar]
  AGENT_PROJECT_SETUP.md → git_utils/readme.md
- `Command string vetting invariant` --semantically_similar_to--> `Proposed relative resource path validation`  [INFERRED] [semantically similar]
  subprocess_utils.md → AGENT_PROJECT_SETUP.md
- `Date-named compressed pickle cache` --semantically_similar_to--> `gzip_file documented contract`  [INFERRED] [semantically similar]
  cache_utils.md → file_utils.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Proposed environment-bound installed agent guidance** — agent_project_setup_import_package_resources, agent_project_setup_environment_selection, agent_project_setup_generated_skill_stub, agent_project_setup_artifact_validation [EXTRACTED 1.00]
- **Concurrency contracts across cache, logging, scheduler and configuration** — cache_utils_inmemorycache_contract, logging_warn_once_contract, readme_ai_timepriorityqueue_contract, yaml_utils_readme_tree_init_contract [EXTRACTED 1.00]
- **Time and identity conventions in persisted operational artifacts** — cache_utils_dated_pickle_cache, file_utils_logfile_name_contract, readme_ai_timestamped_id_contract, time_utils_timezone_contract [INFERRED 0.75]

## Communities (140 total, 21 thin omitted)

### Community 0 - "Git Repository Operations"
Cohesion: 0.05
Nodes (54): main(), Namespace, all_submodule_status(), auto_generate_tag(), BadStages, _get_branch(), get_current_branch(), get_git_command_output() (+46 more)

### Community 1 - "Time Scheduling and Zones"
Cohesion: 0.06
Nodes (43): datetime64, queue, time, datetime_from_date_and_time(), datetime_from_time_and_date_start_time(), ensure_time(), ensure_timezone(), ensure_timezone_or_none() (+35 more)

### Community 2 - "DataFrame Transformations"
Cohesion: 0.06
Nodes (44): DataFrame, filter_string_rep_of_dict(), filter_string_rep_of_list(), Pattern, Regex filtering of string representation of list. Parameters: * the_list -…, Regex filtering of dictionary using string representation of keys. See…, add_and_remove_from_frame(), create_rolled_up_frame() (+36 more)

### Community 3 - "Authentication File Creation"
Cohesion: 0.05
Nodes (33): create_auth_file(), Namespace, Creates a auth file with the given data., Updates a auth file with the given data., Creates an auth config file from command line options and keyboard input., update_auth_file(), update_auth_from_command_line(), generate_key() (+25 more)

### Community 4 - "In Memory Caching"
Cohesion: 0.12
Nodes (18): InMemoryCache, Any, Gets multiple requested items, Gets state dictionary, Pushes many pieces of data into cache. If prefix_keys are given, should be…, puts multiple state items. Returns autogen_key, In memory cache singleton class, Designed to convert * args into a single list. For args, it expects one of the… (+10 more)

### Community 5 - "File Times and Logfiles"
Cohesion: 0.08
Nodes (20): file_modify_time(), get_logfile_name(), datetime, Gives name of log file to write to. Will gzip old log files if requested, Returns last modify datetime if file exists, otherwise returns None. Returns…, Tests for get_logfile_name function., Test returns string path., Test creates year/month directory structure. (+12 more)

### Community 6 - "YAML Tree Lifecycle"
Cohesion: 0.09
Nodes (18): BaseModel, model_validator, PDYaml, Any, T, Called after model initialization. Only the root object of a tree construction…, Get a value with hierarchical lookup. Lookup order: 1. Check if this object has…, Call tree_init() on all PDYaml children, followed by their children's tree_init… (+10 more)

### Community 7 - "Dictionary Attribute Objects"
Cohesion: 0.09
Nodes (15): dict, DictClass, Any, A generic class built off of a dictionary., returns shallow copy of self, Test DictClass inherits dict methods., Tests for DictClass class., Test initializing from dictionary. (+7 more)

### Community 8 - "Exception Formatting and Logging"
Cohesion: 0.09
Nodes (20): Exception, exception_to_string(), log_exception(), Converts exception to a string, Test with different stack level., Tests for exception_to_string function., Test returns a string., Test result contains exception type. (+12 more)

### Community 9 - "Integer Base Conversion"
Cohesion: 0.11
Nodes (15): int_to_base(), Converts non-negative integer to string requested base. NOTE: bases bigger than…, Test that minimum_width pads with zeros on the left., Test that minimum_width pads with a custom pad_char., Test that minimum_width=None (default) applies no padding., Tests for int_to_base function., Test conversion to base 10., Test conversion to base 2 (binary). (+7 more)

### Community 10 - "Test Imports and Bootstrap"
Cohesion: 0.13
Nodes (17): argparse, ArgumentParser, Automatically generates and tags release., setup_args(), ionbus_utils_enumerate, ionbus_utils_exceptions, ionbus_utils_general_classes, ionbus_utils_regex_utils (+9 more)

### Community 11 - "Date and Time Tests"
Cohesion: 0.10
Nodes (20): datetime, pandas, Tests for date_utils.py module., Tests for time_utils module., ensure_time handles strings and minute counts., Numeric with timedelta_number_unit is relative to now., Combines date and time respecting timezone optionality., Target time on same trade date when before start time. (+12 more)

### Community 12 - "Conditional Severity Logging"
Cohesion: 0.11
Nodes (16): log_critical_if(), log_error_if(), log_if(), log_warning_if(), Logs a message, if verbosity contains at least one flag bit set by "flags"…, log_ifs at the WARNING level., log_ifs at the ERROR level., log_ifs at the CRITICAL level. (+8 more)

### Community 13 - "DataFrame Utility Tests"
Cohesion: 0.09
Nodes (20): numpy, Tests for pandas_utils module., create_rolled_up_frame produces expected totals., Rows are replaced/removed appropriately., Rows present in new_frame are filtered out of orig_frame., Rows are replaced based on column key., get_first_value respects query and optional default., Columns are reordered according to regex filters. (+12 more)

### Community 14 - "Subprocess Utility Tests"
Cohesion: 0.09
Nodes (16): Tests for subprocess_utils module., Parses ps output and recurses for descendants., get_command_output delegates to subprocess.run with expected arguments., Returns stdout string from completed process., kill_proc uses os.kill on Windows., kill_proc uses os.killpg on Linux., proc_still_running returns True when poll is None., SubProcessPopenObject monitors process and captures output. (+8 more)

### Community 15 - "YAML Defaults and Serialization"
Cohesion: 0.11
Nodes (14): Simple config for testing., Tests for serialization methods., Test model_dump returns dict., Test model_dump_json returns JSON string., Test model_dump_yaml returns YAML string., Test parent is excluded from serialization., Tests for basic PDYaml functionality., Test automatic name generation. (+6 more)

### Community 16 - "Date Conversion and Partitioning"
Cohesion: 0.22
Nodes (19): date_partition_range(), date_partition_value(), ensure_date_is_iso_string(), first_day_of_month(), first_day_of_next_month(), last_day_of_month(), date, datetime (+11 more)

### Community 17 - "File Hashing"
Cohesion: 0.14
Nodes (12): get_file_hash(), Returns file hexadecimal hash (blake2b if use_md5 is false, else md5), Tests for get_file_hash function., Test returns hexadecimal string., Test uses blake2b by default., Test uses MD5 when requested., Test same content produces same hash., Test different content produces different hash. (+4 more)

### Community 18 - "Date Conversion Tests"
Cohesion: 0.10
Nodes (11): Test raises for empty string when None is disallowed., Tests for to_date function., Test converting date object., Test converting datetime object., Test converting pandas Timestamp., Test converting string., Test converting string with None disallowed., Test returns None for None input. (+3 more)

### Community 19 - "Enums and Compression"
Cohesion: 0.11
Nodes (15): backports_strenum, Enum, C++ style enum with more functionality than Python 3's enum. Also includes…, compress_and_encode_as_base64(), decompress_and_decode_from_base64(), Compresses a string using gzip and encodes it with base64. Returns The…, Decompresses a base64-encoded string that was compressed with gzip. Returns The…, sys (+7 more)

### Community 20 - "Disk Cache Loading"
Cohesion: 0.14
Nodes (17): cache_filename(), get_latest_cache_filename(), load_cache(), date, datetime, Timestamp, TimeType, Module to help with both in memory and on disk caching (+9 more)

### Community 21 - "General Platform Helpers"
Cohesion: 0.12
Nodes (17): collections, contextlib, copy, get_https_cert_filename(), open_using(), package_version_tuple(), Converts python package version into tuple of integers, Function that returns either open or gzip open based on filename ending. To be… (+9 more)

### Community 22 - "Authentication Credential Retrieval"
Cohesion: 0.13
Nodes (13): get_auth_credentials(), get_auth_credentials_pdyaml(), T, Returns the credentials for the given name as a PDYaml object. This is a…, Returns the credentials for the given name. If name is not specified, then the…, Tests for get_auth_credentials function., Test returns a dictionary., Test result contains decrypted password. (+5 more)

### Community 23 - "Password Encryption"
Cohesion: 0.15
Nodes (12): decrypt_password(), encrypt_password(), Encrypt `password` with AES-128-GCM. Returns a Base-64 string containing:…, Reverse of `encrypt_password`. Accepts the Base-64 token produced earlier and…, Test missing key raises error., Tests for encrypt_password and decrypt_password functions., Test encrypt returns a string., Test decrypt returns original password. (+4 more)

### Community 24 - "Numeric String Parsing"
Cohesion: 0.15
Nodes (11): convert_string_to_float(), Converts a string into a float. * Commas are removed * k (1e3), MM (1e6), and…, Tests for convert_string_to_float function., Test converting simple number., Test removing commas., Test handling k suffix., Test handling MM suffix., Test handling B suffix. (+3 more)

### Community 25 - "Value Hashing"
Cohesion: 0.15
Nodes (11): get_value_hash(), Returns value hash for strings or bytes. Uses blake2b unless use_md5 is True.…, Tests for get_value_hash function., Test default string hash uses blake2b hex., Test UTF-8 string bytes produce the same hash., Test MD5 value hashing., Test base36 value hash output., Test base62 value hash output. (+3 more)

### Community 26 - "Logger Configuration"
Cohesion: 0.14
Nodes (12): Logger, get_logger(), Sets format for the default logger, setup_logger_format(), Tests for logger setup functions., Test that get_logger returns a Logger instance., Test that the default logger is available., Test setup_logger_format returns a Logger. (+4 more)

### Community 27 - "ISO Date String Tests"
Cohesion: 0.11
Nodes (10): Tests for to_date_isoformat function., Test returns ISO format string., Test returns format without symbols., Test returns ISO format when None is disallowed., Test returns compact format when None is disallowed., Test converts datetime to date isoformat., Test returns None for None input., Test raises for None when None is disallowed. (+2 more)

### Community 28 - "Documented Time and Identifiers"
Cohesion: 0.17
Nodes (17): File utilities guide, get_file_hash documented contract, touch_file and file_modify_time contracts, gzip_file documented contract, IBU_LOG_DIR log directory override, get_logfile_name documented contract, Caller-derived module path utilities, File timestamps depend on NYC timezone utilities (+9 more)

### Community 29 - "YAML File Loading"
Cohesion: 0.12
Nodes (14): ionbus_utils_yaml_utils, ChildConfig, DefaultValuesConfig, ParentConfig, Tests for yaml_utils module (PDYaml)., Tests for from_yaml_file factory method., Test loading from YAML file., Child config for testing parent-child relationships. (+6 more)

### Community 30 - "Logging Registration and Warnings"
Cohesion: 0.19
Nodes (16): add_log_file(), BadLogConfigError, _ensure_notice_level(), _get_log_level_int(), _get_log_level_str(), _notice(), Provide easy logging., Attach a file handler/sink to the module logger using its current format.… (+8 more)

### Community 31 - "Git Tag and Status Tests"
Cohesion: 0.13
Nodes (14): ionbus_utils_git_utils, ionbus_utils_git_utils_deploy, Tests for git_utils modules with external calls mocked., git_branch_locations returns None when not a git repo., git_branch_locations parses worktree output., git_arg_parser builds parser with expected options., auto_generate_tag increments version per hash tag., Terminal GitHub PR suffixes should not be treated as version tags. (+6 more)

### Community 32 - "Enumerate Objects"
Cohesion: 0.12
Nodes (9): Test value_to_key method., Test keys method returns list of keys., Test that enum values cannot be modified., Test that duplicate names raise an error., Tests for the Enumerate class., Test enum with prefix., Test enum with integer values and offset., Test enum where value equals name. (+1 more)

### Community 33 - "Argument Count Validation"
Cohesion: 0.12
Nodes (9): Tests for ArgParseRangeAction class., Test accepts arguments within range., Test accepts minimum number of arguments., Test accepts maximum number of arguments., Test rejects too few arguments., Test rejects too many arguments., Test min_args=0 allows empty list., Test no max_args allows unlimited. (+1 more)

### Community 34 - "Base Utility Imports"
Cohesion: 0.16
Nodes (11): Utilities for converting integers to different bases, getpass, Group membership utilities., grp, ionbus_utils_base_utils, ionbus_utils_group_utils, os, pwd (+3 more)

### Community 35 - "Git Branch Workspace Creation"
Cohesion: 0.23
Nodes (15): _clean_branch_name(), create_new_repo(), _finish_new_branch_setup(), pull_latest(), Namespace, Path, Creates new directory structure and clones repo, Pulls latest changes from remote repository (+7 more)

### Community 36 - "Base String Parsing"
Cohesion: 0.19
Nodes (9): base_to_int(), Converts string base representation back to integer, Tests for base_to_int function., Test conversion from base 10., Test that surrounding whitespace is stripped., Test conversion from base 2., Test conversion from base 16., Test that invalid base raises error. (+1 more)

### Community 37 - "Platform Detection"
Cohesion: 0.15
Nodes (11): is_mac(), is_windows(), is_wsl(), Returns true if windows else false (linux), Returns true if running in WSL (Windows Subsystem for Linux), Returns true if running on macOS, Tests for platform detection functions., Test is_windows returns boolean. (+3 more)

### Community 38 - "Date String Parsing"
Cohesion: 0.19
Nodes (9): Converts a string of format yyyyy-mm-dd to a date object. All punctuation/non…, yyyymmdd_to_date(), Tests for yyyymmdd_to_date function., Test parsing YYYY-MM-DD format., Test parsing YYYYMMDD format., Test parsing format with slashes., Test returns None for empty string., Test returns None for None input. (+1 more)

### Community 39 - "Gzip File Compression"
Cohesion: 0.19
Nodes (9): gzip_file(), Gzips given file. By default, the original file is removed. unlink_orig: when…, Tests for gzip_file function., Test creates .gz file., Test removes original file by default., Test keeps original file when unlink_orig=False., Test skips empty files., Test gzipped content can be decompressed. (+1 more)

### Community 40 - "User Name Lookup"
Cohesion: 0.18
Nodes (10): get_user_email(), Returns current user email address. Returns empty string if no user is found, get_user_name(), Returns current users username. On a container, this may return None, Tests for get_user_name function., Test returns string or None., Test returns uppercase by default., Test returns lowercase when upper_case=False. (+2 more)

### Community 41 - "Sequence Type Detection"
Cohesion: 0.19
Nodes (9): is_non_string_sequence(), Returns true if it is a sequence (including dictionary keys) that is NOT a…, Tests for is_non_string_sequence function., Test returns True for list., Test returns True for tuple., Test returns False for string., Test returns False for bytes., Test returns True for dict keys. (+1 more)

### Community 42 - "Cache File Selection Tests"
Cohesion: 0.14
Nodes (11): ionbus_utils - A collection of Python utilities for common development tasks.…, ionbus_utils, ionbus_utils_cache_utils, ionbus_utils_version, Tests for cache_utils module., Raises when no cache exists and allow_no_data is False., cache_filename returns expected path for today., When keep_date_as_string is True, date is used verbatim. (+3 more)

### Community 43 - "Package API Overview"
Cohesion: 0.16
Nodes (14): Pandas utilities guide, dataframe_to_markdown documented contract, Regex-driven DataFrame column order, DataFrame row identity and update contracts, stringify_dataframe documented contract, DictClass and argparse utility contracts, Human package documentation, General JSON, compression and hashing utilities (+6 more)

### Community 44 - "Package Usage and Concurrency"
Cohesion: 0.21
Nodes (13): Separate human, agent and package index guides, Graphify structural understanding workflow, Agent guide IBU_AUTH registry name, Agent guide cache usage examples, Agent package usage reference, Dynamic Python class loading, Automatic optional loguru interoperability, Optional presentation and logging dependencies (+5 more)

### Community 45 - "Runtime Dependency Contracts"
Cohesion: 0.26
Nodes (13): Conda conditional Python backports, Conda package recipe, Conda ionbus_utils import smoke test, Conda noarch pip build, Conda ionbus-utils distribution metadata, Conda runtime dependencies, cryptography runtime dependency, Python dependency requirements (+5 more)

### Community 46 - "CLI Parser Dependencies"
Cohesion: 0.15
Nodes (10): ArgumentParser, Utilities for creating and updating authentication files., Create an argument parser. Should always have at least --debug option, setup_args(), ArgParseRangeAction, ArgumentParser, Namespace, An argparse action that requires a range of arguments in argparse. min_args… (+2 more)

### Community 47 - "Enumeration Key Operations"
Cohesion: 0.17
Nodes (6): Enumerate, Returns true if this value is a valid enum key, Returns copy of valid keys, returns copy of values, This only gets called for undefined attributes. So this function won't usually…, Similar to C++'s 'enum', but with a few extra toys. Takes a string with spaces…

### Community 48 - "JSON Comment Removal"
Cohesion: 0.19
Nodes (8): Removes comments and trailing commas from JSON string, remove_comments(), Tests for remove_comments function., Test removing // comments., Test removing /* */ comments., Test removing trailing commas., Test preserves strings with comment-like content., TestRemoveComments

### Community 49 - "Package Build and Versioning"
Cohesion: 0.17
Nodes (12): glob, get_release_tag(), ok_dir(), used to package ionbus_utils, Return the exact release tag from env/git, or None if unavailable., Write the package runtime version source., Read the package runtime version source., Returns ok if we should keep (+4 more)

### Community 50 - "User Group Lookup"
Cohesion: 0.19
Nodes (9): get_groups_for_user(), _get_uid_for_username_linux_only(), Returns the groups a user is a member of. Returns empty list if user does not…, Gets uid for username. Only works on linux., Test that group names are strings., Tests for get_groups_for_user function., Test nonexistent user returns empty list., Test current user has at least one group. (+1 more)

### Community 51 - "Documented Logging and Exceptions"
Cohesion: 0.22
Nodes (13): Logging guide, add_log_file file logging contract, log_exception usage contract, Conditional logging verbosity masks, Parent and worker logger initialization, setup_logger_format documented contract, Logging severity hierarchy, Structured default logger (+5 more)

### Community 52 - "Documented YAML Configuration"
Cohesion: 0.31
Nodes (13): rolled_up_frame documented contract, Hierarchical rollups for tree-grid UI, PDYaml automatic instance names, PDYaml guide, PDYaml.get_value hierarchical defaults, Legacy ionbus.yaml_utils imports in YAML examples, PDYaml automatic parent-child tree, PDYaml hierarchical configuration model (+5 more)

### Community 53 - "YAML Thread Root Tracking"
Cohesion: 0.17
Nodes (11): pydantic, threading, urllib_parse, urllib_request, yaml, _get_root(), PDYaml - A Pydantic BaseModel extension with YAML support and hierarchical…, Get the current root object being constructed in this thread. (+3 more)

### Community 54 - "Subprocess Object Lifecycle"
Cohesion: 0.17
Nodes (10): kill_proc(), popen(), proc_still_running(), Tries to kill process. Returns True if successful, Returns true if process is still running, A class to hole a subprocess Popen object that works both on linux and windows.…, Tries to kill subprocess, checks whether or not process is running. Copies stdout/stderr if appropriate.… (+2 more)

### Community 55 - "Compact UUID Generation"
Cohesion: 0.21
Nodes (8): Returns a UUID encoded in the specified base (default is 62). This is (almost)…, uuid_baseN(), Tests for uuid_baseN function., Test UUID generation in base 62., Test that generated UUIDs are unique., Test UUID generation in base 64., Test that different bases produce different length strings., TestUuidBaseN

### Community 56 - "Authentication Environment Parsing"
Cohesion: 0.21
Nodes (8): get_auth_dictionary(), Returns the credentials dictionary from the environment variable. Raises…, Tests for get_auth_dictionary function., Test raises when environment variable not set., Test returns empty dict when empty_dict_on_failure=True., Test parses environment variable correctly., Test invalid env entry handling., TestGetAuthDictionary

### Community 57 - "File Touch Operations"
Cohesion: 0.21
Nodes (8): Updates modify time of file 'path'. will create if necessary, but otherwise…, touch_file(), Tests for touch_file function., Test touch creates a new file., Test touch updates modification time., Test touch with None does nothing., Test touch with file permissions., TestTouchFile

### Community 58 - "Username Cleanup"
Cohesion: 0.21
Nodes (8): cleanup_username(), Extracts user name from email, Tests for cleanup_username function., Test removes email domain., Test lowercases result., Test returns empty for None., Test returns empty for empty string., TestCleanupUsername

### Community 59 - "Comma List Formatting"
Cohesion: 0.23
Nodes (7): comma_join_list(), Returns a string representing the list using English syntax. Examples: [] -> ""…, Tests for comma_join_list function., Test empty list returns empty string., Test two items with 'and'., Test three items with Oxford comma., TestCommaJoinList

### Community 60 - "String Enum Conversion"
Cohesion: 0.21
Nodes (8): Given enum class and a string, will return value for enum where label matches…, string_to_enum_value(), Tests for string_to_enum_value function., Test finds enum by name., Test case insensitive matching., Test returns None if not found., Test throws if not found and throw_if_not_found=True., TestStringToEnumValue

### Community 61 - "Release Script Validation"
Cohesion: 0.26
Nodes (7): ensure_release_context(), get_next_tag_name(), maybe_tag_release(), release.sh script, usage(), verify_clean_tree(), verify_head_tag()

### Community 62 - "Test Files and Crypto Fixtures"
Cohesion: 0.21
Nodes (11): tempfile, auth_env(), crypto_key_env(), fixture, Shared pytest fixtures for ionbus_utils tests., Create a temporary directory for tests., Create a temporary file for tests., Set up a test encryption key in the environment. (+3 more)

### Community 63 - "Hierarchical YAML Value Lookup"
Cohesion: 0.17
Nodes (7): Tests for hierarchical get_value lookup., Test returns own value if present., Test returns default when value not found., Test searches up parent chain., Test uses default_values member for lookup., Test own value takes precedence over parent., TestGetValue

### Community 64 - "Shared Logging Imports"
Cohesion: 0.20
Nodes (9): Utilities for working with exceptions, format_size(), Format a byte count as a human-readable string. Args: size_bytes: Number of…, hashlib, inspect, ionbus_utils_logging_utils, shutil, socket (+1 more)

### Community 65 - "Module File Path Lookup"
Cohesion: 0.22
Nodes (8): get_module_filepath(), Path, Returns absolute pathname of file passed in, Tests for get_module_filepath function., Test returns Path object., Test returns absolute path., Test returns correct file path., TestGetModuleFilepath

### Community 66 - "YAML Initialization Tests"
Cohesion: 0.18
Nodes (7): Tests for tree_init functionality., Test tree_init is called after construction., Test tree_init is called when loading from YAML., Test tree_init is called on nested children., Config for testing tree_init., TestTreeInit, TreeInitConfig

### Community 67 - "Proposed Agent Skill Installation"
Cohesion: 0.38
Nodes (10): Proposed package resource validation matrix, Canonical entry point filename casing, Agent setup architecture proposal, Explicit Python environment selection, Proposed deterministic generated SKILL.md stub, Proposed import package resource contract, Proposed explicit destination and platform scope, Proposed relative resource path validation (+2 more)

### Community 68 - "Byte String Conversion"
Cohesion: 0.24
Nodes (7): as_string(), If string_or_bytes is bytes, will convert to string., Tests for as_string function., Test returns string unchanged., Test converts bytes to string., Test strips whitespace from bytes., TestAsString

### Community 69 - "Generic Attribute Objects"
Cohesion: 0.27
Nodes (7): GenObject, Very general class to create a dummy object, Tests for GenObject class., Test creating empty GenObject., Test setting attributes dynamically., Test attributes persist after setting., TestGenObject

### Community 70 - "JSON File Loading"
Cohesion: 0.20
Nodes (9): load_class_from_file(), load_json(), Any, Path, Dynamically load a class from a Python file. Useful for plugin systems where…, Reads json from filename, dealing with both comments and trailing commas, Test loading JSON from file., Tests for load_json function. (+1 more)

### Community 71 - "JSON String Loading"
Cohesion: 0.24
Nodes (7): load_json_string(), Reads json from string 'contents' dealing with both comments and trailing commas, Tests for load_json_string function., Test loading valid JSON., Test loading JSON with comments., Test loading JSON with trailing comma., TestLoadJsonString

### Community 72 - "Temporary Directory Changes"
Cohesion: 0.22
Nodes (8): PathLike, Context manager to temporarily change directory. Note: There is no concern…, temporarily_change_dir(), main_deploy_func(), Tests for temporarily_change_dir context manager., Test changes directory temporarily., Test restores directory on exception., TestTemporarilyChangeDir

### Community 73 - "Group Membership Lookup"
Cohesion: 0.24
Nodes (7): get_group_members(), Get the members of a group. Returns empty list if group does not exist., skipif, Tests for get_group_members function., Test nonexistent group returns empty list., Test with an existing Unix group., TestGetGroupMembers

### Community 74 - "Month Start Calculation"
Cohesion: 0.20
Nodes (6): Tests for first_day_of_month function., Test returns first day of month., Test when input is already first day., Test with datetime input., Test with string input., TestFirstDayOfMonth

### Community 75 - "Month End Calculation"
Cohesion: 0.20
Nodes (6): Tests for last_day_of_month function., Test returns last day for 31-day month., Test returns last day for 30-day month., Test February in leap year., Test February in non-leap year., TestLastDayOfMonth

### Community 76 - "ISO Date Normalization"
Cohesion: 0.20
Nodes (6): Tests for ensure_date_is_iso_string function., Test converts date to ISO string., Test converts datetime to ISO string., Test converts Timestamp to ISO string., Test returns None for None input., TestEnsureDateIsIsoString

### Community 77 - "Comma and Semicolon Splitting"
Cohesion: 0.20
Nodes (6): Test splitting without surrounding spaces., Tests for COMMA_SEMI_RE pattern., Test splitting on commas., Test splitting on semicolons., Test splitting on mixed separators., TestCommaSemiRe

### Community 78 - "Leading Underscore Removal"
Cohesion: 0.20
Nodes (6): Tests for LEADING_UNDER_RE pattern., Test removing single leading underscore., Test removes only the first underscore., Test text without leading underscore., Test underscore in middle is not removed., TestLeadingUnderRe

### Community 79 - "Newline Splitting"
Cohesion: 0.20
Nodes (6): Tests for NEWLINE_RE pattern., Test splitting on Unix newlines., Test splitting on Windows newlines., Test splitting on mixed newlines., Test text without newlines., TestNewlineRe

### Community 80 - "YAML Parent Child Relationships"
Cohesion: 0.20
Nodes (6): Tests for automatic parent-child relationships., Test parent is set for singleton child., Test parent is set for children in list., Test parent is set for children in dict., Test dictionary keys override child names., TestParentChildRelationships

### Community 81 - "Cryptography Dependency Imports"
Cohesion: 0.25
Nodes (6): base64, Cryptography utilities, cryptography_hazmat_primitives_ciphers_aead, ionbus_utils_crypto_utils_auth_utils, ionbus_utils_crypto_utils_crypto_utils, Tests for crypto_utils module.

### Community 82 - "Documented Cache Contracts"
Cohesion: 0.42
Nodes (9): cache_filename documented contract, Cache mutable-value copy isolation, Date-named compressed pickle cache, Cache utilities guide, InMemoryCache documented contract, get_latest_cache_filename documented contract, load_cache documented contract, Cache OpsGenie error alerting (+1 more)

### Community 83 - "Single File Moving"
Cohesion: 0.25
Nodes (7): move_single_file(), PathLike, Moves a single file. If new_name exists, it will be deleted before moving., Tests for move_single_file function., Test moves file to new location., Test overwrites existing destination file., TestMoveSingleFile

### Community 84 - "Named Tuple Conversion"
Cohesion: 0.25
Nodes (7): dict_to_namedtuple(), Converts dictionary into named tuple. Warning: If values of dictionary are not…, namedtuple, Tests for dict_to_namedtuple function., Test converts dict to namedtuple., Test with custom name., TestDictToNamedtuple

### Community 85 - "Git CLI Argument Setup"
Cohesion: 0.28
Nodes (7): deploy_arg_parser(), OneOrTwoAction, ArgumentParser, Command line git deploy functionality, Sets the default branch from environment variable if it exists, Argument parser for git utilities, _setup_defaults()

### Community 86 - "Command Execution"
Cohesion: 0.25
Nodes (8): signal, get_command_output(), get_command_output_as_string(), CompletedProcess, Handles windows/linux subprocess differences, # TODO: Implement checking of successful, Runs command (waiting for it to finish) and returns output as subprocess…, runs command (waiting for it to finihs) and returns output as string.…

### Community 87 - "Whitespace Regex Replacement"
Cohesion: 0.22
Nodes (5): Tests for SPACE_RE pattern., Test replacing single spaces., Test replacing multiple consecutive spaces., Test replacing mixed whitespace., TestSpaceRe

### Community 88 - "Authentication YAML Registration"
Cohesion: 0.29
Nodes (6): add_auth_yaml_file(), Adds the given YAML file to the environment variable IBU_AUTH. If the…, Tests for add_auth_yaml_file function., Test that an entry is added with correct format., Test updating existing nickname rewrites value and keeps others., TestAddAuthYamlFile

### Community 89 - "Enumeration Value Validation"
Cohesion: 0.25
Nodes (4): Any, Returns the key (if it exists) for a given enum value, Lets me set internal values, but throws an error if any of the enum values are…, Returns true if this value is a valid enum value

### Community 90 - "Comma String Conversion"
Cohesion: 0.29
Nodes (6): list_to_comma_string(), Converts list to string. Uses quote character if provided, Tests for list_to_comma_string function., Test joins with comma., Test with quote character., TestListToCommaString

### Community 91 - "Multiline Comma Formatting"
Cohesion: 0.29
Nodes (6): multiline_comma_join(), Does a multiline comma join, Tests for multiline_comma_join function., Joins with newlines and spacing., Respects use_quotes flag., TestMultilineCommaJoin

### Community 92 - "Recursive Dictionary Key Normalization"
Cohesion: 0.29
Nodes (6): Input is nested dictionary with possible dictionary and other values. Any…, recursively_uppercase_dict_keys(), Tests for recursively_uppercase_dict_keys function., Test uppercases string keys., Test recursive uppercasing of nested dicts., TestRecursivelyUppercaseDictKeys

### Community 93 - "Timestamped Unique Identifiers"
Cohesion: 0.32
Nodes (5): Returns timestamped unique ID based on unique uuid, timestamped_unique_id(), Tests for timestamped_unique_id function., Test contains underscore separator., TestTimestampedUniqueId

### Community 94 - "Timestamped Identifiers"
Cohesion: 0.32
Nodes (5): Returns timestamped ID. This ID is NOT guaranteed to be unique. Uses…, timestamped_id(), Tests for timestamped_id function., Test generates unique IDs., TestTimestampedId

### Community 95 - "Documented Subprocess Contracts"
Cohesion: 0.43
Nodes (8): Git command execution utilities, Command execution and stdout capture contracts, Subprocess utilities guide, Documented forceful termination limitation, SubProcessPopenObject documented contract, Cross-platform popen documented contract, Linux subprocess session and group lifecycle, Command string vetting invariant

### Community 96 - "Next Month Calculation"
Cohesion: 0.25
Nodes (5): Tests for first_day_of_next_month function., Test returns first day of next month., Test December rolls to January of next year., Test with datetime input., TestFirstDayOfNextMonth

### Community 97 - "Warn Once Behavior"
Cohesion: 0.25
Nodes (5): Tests for warn_once function., Test warn_once logs the first time., Test warn_once doesn't log same location+message twice., Test warn_once logs different messages., TestWarnOnce

### Community 98 - "Notice Logging Registration"
Cohesion: 0.25
Nodes (5): Tests for NOTICE level registration., Test NOTICE level has correct value., Test NOTICE level is registered., Test logger has notice method., TestNoticeLevelRegistered

### Community 99 - "Word Character Filtering"
Cohesion: 0.25
Nodes (5): Tests for NON_LETTER_LIKE_RE pattern., Test removing non-word characters., Test keeping letters and numbers., Test keeping underscores (part of \\w)., TestNonLetterLikeRe

### Community 100 - "Digit Filtering"
Cohesion: 0.25
Nodes (5): Tests for NON_DIGIT_RE pattern., Test removing letters., Test removing punctuation., Test keeping only digits., TestNonDigitRe

### Community 101 - "Documented Authentication Contracts"
Cohesion: 0.52
Nodes (7): IBU_AESGCM named encryption keys, IBU_AUTH_FILES credential file registry, Encrypted authentication YAML files, Cryptography and authentication guide, get_auth_credentials documented contract, get_auth_credentials_pdyaml typed credentials, Windows persistent environment refresh

### Community 102 - "Module Name Lookup"
Cohesion: 0.33
Nodes (5): get_module_name(), Returns module name of the filename passed in. If nothing passed in, the module…, Tests for get_module_name function., Test returns parent directory name., TestGetModuleName

### Community 103 - "Documented Git Release Contracts"
Cohesion: 0.43
Nodes (7): auto_generate_tag documented contract, auto_tag CLI workflow, Git utilities guide, Git repository and branch status, Git submodule issue detection, verify_ready_to_push documented contract, Commit hashtag versioning policy

### Community 104 - "Base Conversion Round Trips"
Cohesion: 0.29
Nodes (5): parametrize, Tests for round-trip conversion., Test that int_to_base and base_to_int are inverses., Test round trip with large number., TestRoundTrip

### Community 105 - "Git Remote Name Parsing"
Cohesion: 0.33
Nodes (6): get_base_and_info(), get_repo_name(), Get the base directory of the git repository., Extract repository name from a git remote URL., Repository name extraction works for common URL formats., test_get_repo_name_handles_ssh_and_https()

### Community 106 - "String Enum Compatibility"
Cohesion: 0.33
Nodes (4): Tests for StrEnum import., Test that StrEnum is available., Test creating a StrEnum subclass., TestStrEnum

### Community 107 - "Batch Git Command Execution"
Cohesion: 0.33
Nodes (5): run_many_git_commands returns True when all commands succeed., run_many_git_commands raises when throw_on_error=True and a command fails., test_run_many_git_commands_success(), fake_get(), test_run_many_git_commands_throws_on_error()

### Community 108 - "Log Level Configuration"
Cohesion: 0.33
Nodes (4): Tests for set_log_level function., Test setting log level with integer., Test setting log level with string., TestSetLogLevel

### Community 109 - "Logging Configuration Exceptions"
Cohesion: 0.33
Nodes (4): Tests for BadLogConfigError., Test BadLogConfigError is a RuntimeError., Test error message is preserved., TestBadLogConfigError

### Community 110 - "YAML String Factories"
Cohesion: 0.33
Nodes (4): Tests for from_yaml_string factory method., Test loading from YAML string., Test loading with explicit name., TestFromYamlString

### Community 111 - "Encryption Key Retrieval"
Cohesion: 0.40
Nodes (5): AESGCM, _get_crypto_aesgcm(), _get_crypto_key(), Returns an AESGCM object for the given name, Returns the key for the given name from the IBU_AESGCM environment variable

### Community 112 - "Git Utility Entrypoints"
Cohesion: 0.40
Nodes (3): Init file for git utils, main function for git utils, ionbus_utils_git_utils_base_git

### Community 113 - "Authentication Test Fixtures"
Cohesion: 0.40
Nodes (3): fixture, Set up auth file and environment., Set up a valid encryption key.

### Community 114 - "Conditional Debug Logging"
Cohesion: 0.50
Nodes (3): log_debug_if(), log_ifs at the DEBUG level., Test log_debug_if function.

### Community 115 - "Conditional Info Logging"
Cohesion: 0.50
Nodes (3): log_info_if(), log_ifs at the INFO level., Test log_info_if function.

### Community 116 - "Conditional Notice Logging"
Cohesion: 0.50
Nodes (3): log_notice_if(), log_ifs at the NOTICE level., Test log_notice_if function.

### Community 117 - "YAML Object Factories"
Cohesion: 0.50
Nodes (3): Tests for create factory method., Test create is equivalent to constructor., TestCreate

### Community 120 - "Linux Child Process Discovery"
Cohesion: 0.67
Nodes (3): get_child_pids_linux(), Any, Returns a list lf all child process IDs in linux

## Ambiguous Edges - Review These
- `Agent package usage reference` → `Legacy ionbus.yaml_utils imports in YAML examples`  [AMBIGUOUS]
  yaml_utils/readme.md · relation: conceptually_related_to
- `cache_filename documented contract` → `Agent guide cache usage examples`  [AMBIGUOUS]
  readme_ai.md · relation: conceptually_related_to
- `load_cache documented contract` → `Agent guide cache usage examples`  [AMBIGUOUS]
  readme_ai.md · relation: conceptually_related_to
- `Conda runtime dependencies` → `PDYaml Python compatibility requirements`  [AMBIGUOUS]
  yaml_utils/readme.md · relation: conceptually_related_to
- `IBU_AUTH_FILES credential file registry` → `Agent guide IBU_AUTH registry name`  [AMBIGUOUS]
  readme_ai.md · relation: conceptually_related_to
- `Public utility module catalog` → `Legacy core_utils names in time examples`  [AMBIGUOUS]
  time_utils.md · relation: conceptually_related_to

## Knowledge Gaps
- **3 isolated node(s):** `ionbus-utils`, `Caller-derived module path utilities`, `DictClass and argparse utility contracts`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 777 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Agent package usage reference` and `Legacy ionbus.yaml_utils imports in YAML examples`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `cache_filename documented contract` and `Agent guide cache usage examples`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `load_cache documented contract` and `Agent guide cache usage examples`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Conda runtime dependencies` and `PDYaml Python compatibility requirements`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `IBU_AUTH_FILES credential file registry` and `Agent guide IBU_AUTH registry name`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Public utility module catalog` and `Legacy core_utils names in time examples`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `TestEnumerate` connect `Enumerate Objects` to `Enumeration Callable Lookup Tests`, `Enumeration String Representation Tests`, `Enumeration Attribute Error Tests`, `Enumeration String Initialization Tests`, `Enumeration List Initialization Tests`, `Enumeration Dictionary Initialization Tests`, `Enumeration Integer Mode Tests`, `Enumeration Bitflag Mode Tests`, `Enumeration Key Value Tests`, `Enumeration Integer Value Tests`, `Test Imports and Bootstrap`, `Enumeration Prefix Value Tests`, `Enumeration Key Operations`, `Enumeration Key Validation Tests`, `Enumeration Value Validation Tests`, `Enumeration Value Collection Tests`, `Enumeration Iteration Tests`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._

## Codex Skill Extraction Audit

Deep semantic extraction was performed by the Codex session. No external LLM API requests were made by this pipeline. Host-session token counts are unavailable; the zero token counters above are placeholders, not measured session usage.

Semantic extraction covered all 15 documentation/configuration files and added 124 nodes, 250 relationships, and 3 hyperedges. The final graph retains 2,219 EXTRACTED, 385 INFERRED, and 6 AMBIGUOUS relationships. The summary rounds the ambiguous share down to 0%; the six uncertain links remain explicitly tagged in the graph.

## Graph Health

The raw extraction integrity check flagged 270 relationships with endpoints absent from the original node list, 6 self-loops, and 58 extra undirected same-endpoint edge records. These flags originate in the structural extraction; the semantic fragment was separately verified to have present endpoints and no self-loops. Graphify's builder added 67 nodes while resolving the extraction. The exported graph was verified to contain every endpoint of its 2,610 relationships, unique node IDs, all 140 curated community names, and relative source-file paths. The raw integrity flags remain a limitation: inferred reference nodes and combined edge records should be checked against source before assuming full dependency coverage. Full local diagnostics are in graph_health.json.

## Context Size Benchmark

The default CLI benchmark estimated the corpus at 86,100 words and reported 30.2x context reduction. The actual scan counted 45,350 words (approximately 60,466 tokens). Using that measured word count and the benchmark's estimated average query context of 3,803 tokens gives approximately 15.9x smaller context for its four sample questions. This compares estimated context sizes; it does not measure answer accuracy or actual session token billing.
