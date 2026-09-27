# Graph Report - ionbus_utils  (2026-09-27)

## Corpus Check
- 71 files · ~50,682 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1814 nodes · 2713 edges · 128 communities (107 shown, 21 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 377 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Git Repository Operations
- Time Scheduling and Zones
- Skill Installer Tests
- DataFrame Transformations
- Authentication File Creation
- Subprocess Utility Tests
- Documented Time and Identifiers
- Authentication Credential Retrieval
- File Times and Logfiles
- Git Branch Workspace Creation
- In Memory Caching
- Agent Skill Installation
- Platform Detection
- Exception Formatting and Logging
- Integer Base Conversion
- Cryptography Dependency Imports
- YAML Tree Lifecycle
- Disk Cache Loading
- Test Imports and Bootstrap
- General Platform Helpers
- Date and Time Tests
- Conditional Severity Logging
- DataFrame Utility Tests
- YAML Defaults and Serialization
- Authentication Environment Parsing
- Date Conversion and Partitioning
- File Hashing
- Date Conversion Tests
- YAML File Loading
- Package Skill Contracts
- Numeric String Parsing
- Value Hashing
- Logger Configuration
- ISO Date String Tests
- Enums and Compression
- Logging Registration and Warnings
- Enumerate Objects
- Argument Count Validation
- YAML Thread Root Tracking
- Test Files and Crypto Fixtures
- Date String Parsing
- User Name Lookup
- Sequence Type Detection
- Cache File Selection Tests
- Runtime Dependency Contracts
- String Enum Conversion
- Enumeration Key Operations
- JSON Comment Removal
- User Group Lookup
- Package Usage and Concurrency
- Agent Development Workflow
- Compact UUID Generation
- Shared Logging Imports
- File Touch Operations
- Username Cleanup
- Comma List Formatting
- Base Utility Imports
- Release Script Validation
- Command Execution
- Dictionary Attribute Objects
- Hierarchical YAML Value Lookup
- Module File Path Lookup
- YAML Initialization Tests
- Agent Setup Checklist
- Documented YAML Configuration
- Byte String Conversion
- Generic Attribute Objects
- JSON String Loading
- Group Membership Lookup
- Month Start Calculation
- Month End Calculation
- ISO Date Normalization
- Comma and Semicolon Splitting
- Leading Underscore Removal
- Newline Splitting
- YAML Parent Child Relationships
- Documented Authentication Contracts
- Dictionary Attribute Objects
- Single File Moving
- Named Tuple Conversion
- Package Build and Versioning
- Packaged Guide Validation
- Whitespace Regex Replacement
- Enumeration Value Validation
- Comma String Conversion
- JSON File Loading
- Multiline Comma Formatting
- Recursive Dictionary Key Normalization
- Timestamped Unique Identifiers
- Timestamped Identifiers
- Next Month Calculation
- Warn Once Behavior
- Notice Logging Registration
- Word Character Filtering
- Digit Filtering
- Module Name Lookup
- CLI Parser Dependencies
- Documented Git Release Contracts
- Package API Overview
- String Enum Compatibility
- Log Level Configuration
- Logging Configuration Exceptions
- YAML String Factories
- YAML Tree Lifecycle
- Conditional Debug Logging
- Conditional Info Logging
- Conditional Notice Logging
- YAML Package Exports
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
- Dictionary Attribute Objects
- Dictionary Attribute Objects
- Dictionary Attribute Objects
- Package Metadata

## God Nodes (most connected - your core abstractions)
1. `Enumerate` - 36 edges
2. `TestEnumerate` - 25 edges
3. `PDYaml` - 23 edges
4. `int_to_base()` - 20 edges
5. `to_date()` - 18 edges
6. `DictClass` - 17 edges
7. `package_factory()` - 16 edges
8. `Package-owned agent skill mechanism` - 16 edges
9. `to_date_isoformat()` - 15 edges
10. `get_logfile_name()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Legacy core_utils names in time examples` --conceptually_related_to--> `Utility module documentation catalog`  [AMBIGUOUS]
  time_utils.md → README.md
- `Concise utility module overview` --semantically_similar_to--> `Utility module documentation catalog`  [INFERRED] [semantically similar]
  README_PIP.md → README.md
- `Date-named compressed pickle cache` --semantically_similar_to--> `gzip_file documented contract`  [INFERRED] [semantically similar]
  cache_utils.md → file_utils.md
- `Conda runtime dependencies` --semantically_similar_to--> `Pip runtime dependency constraints`  [INFERRED] [semantically similar]
  conda-recipe/meta.yaml → requirements.txt
- `Conda conditional Python backports` --semantically_similar_to--> `Pip conditional Python backports`  [INFERRED] [semantically similar]
  conda-recipe/meta.yaml → requirements.txt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Time and identity conventions in persisted operational artifacts** — cache_utils_dated_pickle_cache, file_utils_logfile_name_contract, time_utils_timezone_contract [INFERRED 0.75]
- **PDYaml typed credentials and hierarchical configuration** — crypto_utils_readme_typed_credentials, yaml_utils_readme_pdyaml, yaml_utils_readme_hierarchical_lookup, yaml_utils_readme_tree_initialization, readme_ai_pdyaml_defaults [INFERRED 0.85]
- **Environment-bound package guide delivery** — agent_project_setup_deterministic_stub, readme_agent_skills_thin_stub, readme_ai_guide_reader, agents_session_environment [INFERRED 0.95]
- **Resource contract, write safety and artifact verification** — agent_project_setup_import_package_contract, readme_agent_skills_preflight, readme_agent_skills_atomic_writes, aps_todo_artifact_checks, aps_todo_windows_validation [INFERRED 0.95]

## Communities (128 total, 21 thin omitted)

### Community 0 - "Git Repository Operations"
Cohesion: 0.05
Nodes (54): main(), Namespace, all_submodule_status(), auto_generate_tag(), BadStages, _get_branch(), get_current_branch(), get_git_command_output() (+46 more)

### Community 1 - "Time Scheduling and Zones"
Cohesion: 0.06
Nodes (43): datetime64, queue, time, datetime_from_date_and_time(), datetime_from_time_and_date_start_time(), ensure_time(), ensure_timezone(), ensure_timezone_or_none() (+35 more)

### Community 2 - "Skill Installer Tests"
Cohesion: 0.05
Nodes (37): generate_stub(), Copy-and-adapt outline for a package-owned agent skill mechanism. This is a…, Example resource access; validate inputs when adapting this template., Example stub using your own validated reader module name., read_guide(), base_to_int(), Converts string base representation back to integer, importlib (+29 more)

### Community 3 - "DataFrame Transformations"
Cohesion: 0.06
Nodes (44): DataFrame, filter_string_rep_of_dict(), filter_string_rep_of_list(), Pattern, Regex filtering of string representation of list. Parameters: * the_list -…, Regex filtering of dictionary using string representation of keys. See…, add_and_remove_from_frame(), create_rolled_up_frame() (+36 more)

### Community 4 - "Authentication File Creation"
Cohesion: 0.05
Nodes (35): create_auth_file(), Namespace, Creates a auth file with the given data., Updates a auth file with the given data., Creates an auth config file from command line options and keyboard input., update_auth_file(), update_auth_from_command_line(), generate_key() (+27 more)

### Community 5 - "Subprocess Utility Tests"
Cohesion: 0.04
Nodes (39): ionbus_utils_git_utils, ionbus_utils_git_utils_deploy, Tests for git_utils modules with external calls mocked., Repository name extraction works for common URL formats., Branch names are sanitized for filesystem usage., run_many_git_commands returns True when all commands succeed., run_many_git_commands raises when throw_on_error=True and a command fails., git_branch_locations returns None when not a git repo. (+31 more)

### Community 6 - "Documented Time and Identifiers"
Cohesion: 0.07
Nodes (47): cache_filename documented contract, Cache mutable-value copy isolation, Date-named compressed pickle cache, Cache utilities guide, InMemoryCache documented contract, get_latest_cache_filename documented contract, load_cache documented contract, Cache OpsGenie error alerting (+39 more)

### Community 7 - "Authentication Credential Retrieval"
Cohesion: 0.06
Nodes (31): AESGCM, get_auth_credentials(), get_auth_credentials_pdyaml(), T, Returns the credentials for the given name as a PDYaml object. This is a…, Returns the credentials for the given name. If name is not specified, then the…, decrypt_password(), encrypt_password() (+23 more)

### Community 8 - "File Times and Logfiles"
Cohesion: 0.06
Nodes (29): file_modify_time(), get_logfile_name(), gzip_file(), datetime, Gives name of log file to write to. Will gzip old log files if requested, Returns last modify datetime if file exists, otherwise returns None. Returns…, Gzips given file. By default, the original file is removed. unlink_orig: when…, Tests for gzip_file function. (+21 more)

### Community 9 - "Git Branch Workspace Creation"
Cohesion: 0.08
Nodes (35): PathLike, Context manager to temporarily change directory. Note: There is no concern…, temporarily_change_dir(), _clean_branch_name(), create_new_repo(), deploy_arg_parser(), _finish_new_branch_setup(), get_base_and_info() (+27 more)

### Community 10 - "In Memory Caching"
Cohesion: 0.12
Nodes (18): InMemoryCache, Any, Gets multiple requested items, Gets state dictionary, Pushes many pieces of data into cache. If prefix_keys are given, should be…, puts multiple state items. Returns autogen_key, In memory cache singleton class, Designed to convert * args into a single list. For args, it expects one of the… (+10 more)

### Community 11 - "Agent Skill Installation"
Cohesion: 0.12
Nodes (31): _apply_installation(), destination(), generate_skill(), install(), Installation, main(), _preflight(), Path (+23 more)

### Community 12 - "Platform Detection"
Cohesion: 0.08
Nodes (23): is_mac(), is_windows(), is_wsl(), Utilities for converting integers to different bases, Returns true if windows else false (linux), Returns true if running in WSL (Windows Subsystem for Linux), Returns true if running on macOS, kill_proc() (+15 more)

### Community 13 - "Exception Formatting and Logging"
Cohesion: 0.09
Nodes (20): Exception, exception_to_string(), log_exception(), Converts exception to a string, Test with different stack level., Tests for exception_to_string function., Test returns a string., Test result contains exception type. (+12 more)

### Community 14 - "Integer Base Conversion"
Cohesion: 0.11
Nodes (15): int_to_base(), Converts non-negative integer to string requested base. NOTE: bases bigger than…, Test that minimum_width pads with zeros on the left., Test that minimum_width pads with a custom pad_char., Test that minimum_width=None (default) applies no padding., Tests for int_to_base function., Test conversion to base 10., Test conversion to base 2 (binary). (+7 more)

### Community 15 - "Cryptography Dependency Imports"
Cohesion: 0.11
Nodes (18): argparse, base64, ArgumentParser, Utilities for creating and updating authentication files., Create an argument parser. Should always have at least --debug option, setup_args(), Cryptography utilities, cryptography_hazmat_primitives_ciphers_aead (+10 more)

### Community 16 - "YAML Tree Lifecycle"
Cohesion: 0.11
Nodes (14): BaseModel, model_validator, PDYaml, T, Call tree_init() on all PDYaml children, followed by their children's tree_init…, Called after the entire tree has been constructed and parent links are set.…, Internal method to run tree_init once per instance. Prevents duplicate calls…, Manually trigger tree_init on this object and all children. NOTE: This method… (+6 more)

### Community 17 - "Disk Cache Loading"
Cohesion: 0.12
Nodes (19): cache_filename(), get_latest_cache_filename(), load_cache(), date, datetime, Timestamp, TimeType, Module to help with both in memory and on disk caching (+11 more)

### Community 18 - "Test Imports and Bootstrap"
Cohesion: 0.13
Nodes (17): gzip, ionbus_utils_enumerate, ionbus_utils_exceptions, ionbus_utils_file_utils, ionbus_utils_general_classes, ionbus_utils_regex_utils, logging, pathlib (+9 more)

### Community 19 - "General Platform Helpers"
Cohesion: 0.10
Nodes (19): backports_strenum, collections, contextlib, copy, C++ style enum with more functionality than Python 3's enum. Also includes…, get_https_cert_filename(), open_using(), package_version_tuple() (+11 more)

### Community 20 - "Date and Time Tests"
Cohesion: 0.10
Nodes (20): datetime, pandas, Tests for date_utils.py module., Tests for time_utils module., ensure_time handles strings and minute counts., Numeric with timedelta_number_unit is relative to now., Combines date and time respecting timezone optionality., Target time on same trade date when before start time. (+12 more)

### Community 21 - "Conditional Severity Logging"
Cohesion: 0.11
Nodes (16): log_critical_if(), log_error_if(), log_if(), log_warning_if(), Logs a message, if verbosity contains at least one flag bit set by "flags"…, log_ifs at the WARNING level., log_ifs at the ERROR level., log_ifs at the CRITICAL level. (+8 more)

### Community 22 - "DataFrame Utility Tests"
Cohesion: 0.09
Nodes (20): numpy, Tests for pandas_utils module., create_rolled_up_frame produces expected totals., Rows are replaced/removed appropriately., Rows present in new_frame are filtered out of orig_frame., Rows are replaced based on column key., get_first_value respects query and optional default., Columns are reordered according to regex filters. (+12 more)

### Community 23 - "YAML Defaults and Serialization"
Cohesion: 0.11
Nodes (14): Simple config for testing., Tests for serialization methods., Test model_dump returns dict., Test model_dump_json returns JSON string., Test model_dump_yaml returns YAML string., Test parent is excluded from serialization., Tests for basic PDYaml functionality., Test automatic name generation. (+6 more)

### Community 24 - "Authentication Environment Parsing"
Cohesion: 0.13
Nodes (14): add_auth_yaml_file(), get_auth_dictionary(), Adds the given YAML file to the environment variable IBU_AUTH. If the…, Returns the credentials dictionary from the environment variable. Raises…, Tests for get_auth_dictionary function., Test raises when environment variable not set., Test returns empty dict when empty_dict_on_failure=True., Test parses environment variable correctly. (+6 more)

### Community 25 - "Date Conversion and Partitioning"
Cohesion: 0.22
Nodes (19): date_partition_range(), date_partition_value(), ensure_date_is_iso_string(), first_day_of_month(), first_day_of_next_month(), last_day_of_month(), date, datetime (+11 more)

### Community 26 - "File Hashing"
Cohesion: 0.14
Nodes (12): get_file_hash(), Returns file hexadecimal hash (blake2b if use_md5 is false, else md5), Tests for get_file_hash function., Test returns hexadecimal string., Test uses blake2b by default., Test uses MD5 when requested., Test same content produces same hash., Test different content produces different hash. (+4 more)

### Community 27 - "Date Conversion Tests"
Cohesion: 0.10
Nodes (11): Test raises for empty string when None is disallowed., Tests for to_date function., Test converting date object., Test converting datetime object., Test converting pandas Timestamp., Test converting string., Test converting string with None disallowed., Test returns None for None input. (+3 more)

### Community 28 - "YAML File Loading"
Cohesion: 0.10
Nodes (16): ChildConfig, DefaultValuesConfig, ParentConfig, Tests for yaml_utils module (PDYaml)., Tests for from_yaml_file factory method., Test loading from YAML file., Child config for testing parent-child relationships., Tests for create factory method. (+8 more)

### Community 29 - "Package Skill Contracts"
Cohesion: 0.14
Nodes (18): Deterministic thin SKILL.md stub, Agent Setup for Ionbus-Style Python Libraries, Separate human, agent-usage and repository guidance, Required scope and platform selection, Separate adaptation template with deferred fallback, Graphify local stdio MCP, Traversable UTF-8 resource reading, Preflight and atomic replacement contract (+10 more)

### Community 30 - "Numeric String Parsing"
Cohesion: 0.15
Nodes (11): convert_string_to_float(), Converts a string into a float. * Commas are removed * k (1e3), MM (1e6), and…, Tests for convert_string_to_float function., Test converting simple number., Test removing commas., Test handling k suffix., Test handling MM suffix., Test handling B suffix. (+3 more)

### Community 31 - "Value Hashing"
Cohesion: 0.15
Nodes (11): get_value_hash(), Returns value hash for strings or bytes. Uses blake2b unless use_md5 is True.…, Tests for get_value_hash function., Test default string hash uses blake2b hex., Test UTF-8 string bytes produce the same hash., Test MD5 value hashing., Test base36 value hash output., Test base62 value hash output. (+3 more)

### Community 32 - "Logger Configuration"
Cohesion: 0.14
Nodes (12): Logger, get_logger(), Sets format for the default logger, setup_logger_format(), Tests for logger setup functions., Test that get_logger returns a Logger instance., Test that the default logger is available., Test setup_logger_format returns a Logger. (+4 more)

### Community 33 - "ISO Date String Tests"
Cohesion: 0.11
Nodes (10): Tests for to_date_isoformat function., Test returns ISO format string., Test returns format without symbols., Test returns ISO format when None is disallowed., Test returns compact format when None is disallowed., Test converts datetime to date isoformat., Test returns None for None input., Test raises for None when None is disallowed. (+2 more)

### Community 34 - "Enums and Compression"
Cohesion: 0.12
Nodes (14): compress_and_encode_as_base64(), decompress_and_decode_from_base64(), Compresses a string using gzip and encodes it with base64. Returns The…, Decompresses a base64-encoded string that was compressed with gzip. Returns The…, ionbus_utils_general, Tests for general.py module., Tests for compress_and_encode_as_base64 function., Test compresses and encodes string. (+6 more)

### Community 35 - "Logging Registration and Warnings"
Cohesion: 0.19
Nodes (16): add_log_file(), BadLogConfigError, _ensure_notice_level(), _get_log_level_int(), _get_log_level_str(), _notice(), Provide easy logging., Attach a file handler/sink to the module logger using its current format.… (+8 more)

### Community 36 - "Enumerate Objects"
Cohesion: 0.12
Nodes (9): Test value_to_key method., Test keys method returns list of keys., Test that enum values cannot be modified., Test that duplicate names raise an error., Tests for the Enumerate class., Test enum with prefix., Test enum with integer values and offset., Test enum where value equals name. (+1 more)

### Community 37 - "Argument Count Validation"
Cohesion: 0.12
Nodes (9): Tests for ArgParseRangeAction class., Test accepts arguments within range., Test accepts minimum number of arguments., Test accepts maximum number of arguments., Test rejects too few arguments., Test rejects too many arguments., Test min_args=0 allows empty list., Test no max_args allows unlimited. (+1 more)

### Community 38 - "YAML Thread Root Tracking"
Cohesion: 0.15
Nodes (12): pydantic, threading, urllib_parse, urllib_request, yaml, _get_root(), PDYaml - A Pydantic BaseModel extension with YAML support and hierarchical…, Called after model initialization. Only the root object of a tree construction… (+4 more)

### Community 39 - "Test Files and Crypto Fixtures"
Cohesion: 0.21
Nodes (13): collections_abc, MonkeyPatch, auth_env(), crypto_key_env(), fixture, Path, Shared pytest fixtures for ionbus_utils tests., Create a temporary directory for tests. (+5 more)

### Community 40 - "Date String Parsing"
Cohesion: 0.19
Nodes (9): Converts a string of format yyyyy-mm-dd to a date object. All punctuation/non…, yyyymmdd_to_date(), Tests for yyyymmdd_to_date function., Test parsing YYYY-MM-DD format., Test parsing YYYYMMDD format., Test parsing format with slashes., Test returns None for empty string., Test returns None for None input. (+1 more)

### Community 41 - "User Name Lookup"
Cohesion: 0.18
Nodes (10): get_user_email(), Returns current user email address. Returns empty string if no user is found, get_user_name(), Returns current users username. On a container, this may return None, Tests for get_user_name function., Test returns string or None., Test returns uppercase by default., Test returns lowercase when upper_case=False. (+2 more)

### Community 42 - "Sequence Type Detection"
Cohesion: 0.19
Nodes (9): is_non_string_sequence(), Returns true if it is a sequence (including dictionary keys) that is NOT a…, Tests for is_non_string_sequence function., Test returns True for list., Test returns True for tuple., Test returns False for string., Test returns False for bytes., Test returns True for dict keys. (+1 more)

### Community 43 - "Cache File Selection Tests"
Cohesion: 0.14
Nodes (11): ionbus_utils - A collection of Python utilities for common development tasks.…, ionbus_utils, ionbus_utils_cache_utils, ionbus_utils_version, Tests for cache_utils module., Raises when no cache exists and allow_no_data is False., cache_filename returns expected path for today., When keep_date_as_string is True, date is used verbatim. (+3 more)

### Community 44 - "Runtime Dependency Contracts"
Cohesion: 0.26
Nodes (13): Conda conditional Python backports, Conda package recipe, Conda ionbus_utils import smoke test, Conda noarch pip build, Conda ionbus-utils distribution metadata, Conda runtime dependencies, cryptography runtime dependency, Python dependency requirements (+5 more)

### Community 45 - "String Enum Conversion"
Cohesion: 0.19
Nodes (9): Enum, Given enum class and a string, will return value for enum where label matches…, string_to_enum_value(), Tests for string_to_enum_value function., Test finds enum by name., Test case insensitive matching., Test returns None if not found., Test throws if not found and throw_if_not_found=True. (+1 more)

### Community 46 - "Enumeration Key Operations"
Cohesion: 0.17
Nodes (6): Enumerate, Returns true if this value is a valid enum key, Returns copy of valid keys, returns copy of values, This only gets called for undefined attributes. So this function won't usually…, Similar to C++'s 'enum', but with a few extra toys. Takes a string with spaces…

### Community 47 - "JSON Comment Removal"
Cohesion: 0.19
Nodes (8): Removes comments and trailing commas from JSON string, remove_comments(), Tests for remove_comments function., Test removing // comments., Test removing /* */ comments., Test removing trailing commas., Test preserves strings with comment-like content., TestRemoveComments

### Community 48 - "User Group Lookup"
Cohesion: 0.19
Nodes (9): get_groups_for_user(), _get_uid_for_username_linux_only(), Returns the groups a user is a member of. Returns empty list if user does not…, Gets uid for username. Only works on linux., Test that group names are strings., Tests for get_groups_for_user function., Test nonexistent user returns empty list., Test current user has at least one group. (+1 more)

### Community 49 - "Package Usage and Concurrency"
Cohesion: 0.18
Nodes (13): Package agent skill installation, Sortable unique base62 identifiers, ionbus_utils agent API and usage guide, Reuse general-purpose utilities in consuming projects, Thread-safe TimePriorityQueue scheduling, Contextual logger and warn_once behavior, Thread-safe singleton cache with copy-on-read, Concurrent utility safety guarantees (+5 more)

### Community 50 - "Agent Development Workflow"
Cohesion: 0.18
Nodes (12): Raw checkout parent on sys.path, Working on ionbus_utils, Gitignore and staging authorization, Graphify scoped structural queries, Pytest and Ruff validation, Source and tests remain the authority, Windows Python 3.11 implementation validation, Explicit @AGENTS.md import (+4 more)

### Community 51 - "Compact UUID Generation"
Cohesion: 0.21
Nodes (8): Returns a UUID encoded in the specified base (default is 62). This is (almost)…, uuid_baseN(), Tests for uuid_baseN function., Test UUID generation in base 62., Test that generated UUIDs are unique., Test UUID generation in base 64., Test that different bases produce different length strings., TestUuidBaseN

### Community 52 - "Shared Logging Imports"
Cohesion: 0.18
Nodes (10): Utilities for working with exceptions, format_size(), Format a byte count as a human-readable string. Args: size_bytes: Number of…, glob, hashlib, inspect, ionbus_utils_logging_utils, shutil (+2 more)

### Community 53 - "File Touch Operations"
Cohesion: 0.21
Nodes (8): Updates modify time of file 'path'. will create if necessary, but otherwise…, touch_file(), Tests for touch_file function., Test touch creates a new file., Test touch updates modification time., Test touch with None does nothing., Test touch with file permissions., TestTouchFile

### Community 54 - "Username Cleanup"
Cohesion: 0.21
Nodes (8): cleanup_username(), Extracts user name from email, Tests for cleanup_username function., Test removes email domain., Test lowercases result., Test returns empty for None., Test returns empty for empty string., TestCleanupUsername

### Community 55 - "Comma List Formatting"
Cohesion: 0.23
Nodes (7): comma_join_list(), Returns a string representing the list using English syntax. Examples: [] -> ""…, Tests for comma_join_list function., Test empty list returns empty string., Test two items with 'and'., Test three items with Oxford comma., TestCommaJoinList

### Community 56 - "Base Utility Imports"
Cohesion: 0.18
Nodes (9): getpass, Group membership utilities., grp, ionbus_utils_base_utils, ionbus_utils_group_utils, pwd, subprocess, Tests for base_utils.py module. (+1 more)

### Community 57 - "Release Script Validation"
Cohesion: 0.26
Nodes (7): ensure_release_context(), get_next_tag_name(), maybe_tag_release(), release.sh script, usage(), verify_clean_tree(), verify_head_tag()

### Community 58 - "Command Execution"
Cohesion: 0.18
Nodes (11): signal, get_child_pids_linux(), get_command_output(), get_command_output_as_string(), Any, CompletedProcess, Handles windows/linux subprocess differences, # TODO: Implement checking of successful (+3 more)

### Community 59 - "Dictionary Attribute Objects"
Cohesion: 0.17
Nodes (7): Test DictClass inherits dict methods., Tests for DictClass class., Test initializing from keyword arguments., Test setting values as attributes., Test accessing values as dictionary., Test as_dict returns regular dict., TestDictClass

### Community 60 - "Hierarchical YAML Value Lookup"
Cohesion: 0.17
Nodes (7): Tests for hierarchical get_value lookup., Test returns own value if present., Test returns default when value not found., Test searches up parent chain., Test uses default_values member for lookup., Test own value takes precedence over parent., TestGetValue

### Community 61 - "Module File Path Lookup"
Cohesion: 0.22
Nodes (8): get_module_filepath(), Path, Returns absolute pathname of file passed in, Tests for get_module_filepath function., Test returns Path object., Test returns absolute path., Test returns correct file path., TestGetModuleFilepath

### Community 62 - "YAML Initialization Tests"
Cohesion: 0.18
Nodes (7): Tests for tree_init functionality., Test tree_init is called after construction., Test tree_init is called when loading from YAML., Test tree_init is called on nested children., Config for testing tree_init., TestTreeInit, TreeInitConfig

### Community 63 - "Agent Setup Checklist"
Cohesion: 0.20
Nodes (10): Canonical README and agent filenames, Shared standard-library agent_skill installer, Cross-platform and distribution validation matrix, Agent Project Setup implementation checklist, Post-implementation Graphify refresh, Shared skill deployment implementation, Unfinished Conda, interpreter and client checks, Six authorized case-only Git renames (+2 more)

### Community 64 - "Documented YAML Configuration"
Cohesion: 0.27
Nodes (10): Credentials returned as a PDYaml subclass, Hierarchical DataFrame rollup for tree-grid UIs, PDYaml hierarchical defaults and tree initialization, PDYaml hierarchical Pydantic configuration, YAML file, URL and string factory methods, Hierarchical get_value search order, Exclude parent references from serialized data, PDYaml Pydantic v2 model (+2 more)

### Community 65 - "Byte String Conversion"
Cohesion: 0.24
Nodes (7): as_string(), If string_or_bytes is bytes, will convert to string., Tests for as_string function., Test returns string unchanged., Test converts bytes to string., Test strips whitespace from bytes., TestAsString

### Community 66 - "Generic Attribute Objects"
Cohesion: 0.27
Nodes (7): GenObject, Very general class to create a dummy object, Tests for GenObject class., Test creating empty GenObject., Test setting attributes dynamically., Test attributes persist after setting., TestGenObject

### Community 67 - "JSON String Loading"
Cohesion: 0.24
Nodes (7): load_json_string(), Reads json from string 'contents' dealing with both comments and trailing commas, Tests for load_json_string function., Test loading valid JSON., Test loading JSON with comments., Test loading JSON with trailing comma., TestLoadJsonString

### Community 68 - "Group Membership Lookup"
Cohesion: 0.24
Nodes (7): get_group_members(), Get the members of a group. Returns empty list if group does not exist., skipif, Tests for get_group_members function., Test nonexistent group returns empty list., Test with an existing Unix group., TestGetGroupMembers

### Community 69 - "Month Start Calculation"
Cohesion: 0.20
Nodes (6): Tests for first_day_of_month function., Test returns first day of month., Test when input is already first day., Test with datetime input., Test with string input., TestFirstDayOfMonth

### Community 70 - "Month End Calculation"
Cohesion: 0.20
Nodes (6): Tests for last_day_of_month function., Test returns last day for 31-day month., Test returns last day for 30-day month., Test February in leap year., Test February in non-leap year., TestLastDayOfMonth

### Community 71 - "ISO Date Normalization"
Cohesion: 0.20
Nodes (6): Tests for ensure_date_is_iso_string function., Test converts date to ISO string., Test converts datetime to ISO string., Test converts Timestamp to ISO string., Test returns None for None input., TestEnsureDateIsIsoString

### Community 72 - "Comma and Semicolon Splitting"
Cohesion: 0.20
Nodes (6): Test splitting without surrounding spaces., Tests for COMMA_SEMI_RE pattern., Test splitting on commas., Test splitting on semicolons., Test splitting on mixed separators., TestCommaSemiRe

### Community 73 - "Leading Underscore Removal"
Cohesion: 0.20
Nodes (6): Tests for LEADING_UNDER_RE pattern., Test removing single leading underscore., Test removes only the first underscore., Test text without leading underscore., Test underscore in middle is not removed., TestLeadingUnderRe

### Community 74 - "Newline Splitting"
Cohesion: 0.20
Nodes (6): Tests for NEWLINE_RE pattern., Test splitting on Unix newlines., Test splitting on Windows newlines., Test splitting on mixed newlines., Test text without newlines., TestNewlineRe

### Community 75 - "YAML Parent Child Relationships"
Cohesion: 0.20
Nodes (6): Tests for automatic parent-child relationships., Test parent is set for singleton child., Test parent is set for children in list., Test parent is set for children in dict., Test dictionary keys override child names., TestParentChildRelationships

### Community 76 - "Documented Authentication Contracts"
Cohesion: 0.22
Nodes (9): Per-session environment confirmation, Encrypted authentication YAML creation, Named credential file registry with custom env_name, Crypto utilities and authentication management, Named AES-GCM keys in IBU_AESGCM, Windows setx requires new process environments, Portable graph outputs and local run data, AES-GCM credential files and environment discovery (+1 more)

### Community 77 - "Dictionary Attribute Objects"
Cohesion: 0.28
Nodes (5): dict, DictClass, Any, A generic class built off of a dictionary., returns shallow copy of self

### Community 78 - "Single File Moving"
Cohesion: 0.25
Nodes (7): move_single_file(), PathLike, Moves a single file. If new_name exists, it will be deleted before moving., Tests for move_single_file function., Test moves file to new location., Test overwrites existing destination file., TestMoveSingleFile

### Community 79 - "Named Tuple Conversion"
Cohesion: 0.25
Nodes (7): dict_to_namedtuple(), Converts dictionary into named tuple. Warning: If values of dictionary are not…, namedtuple, Tests for dict_to_namedtuple function., Test converts dict to namedtuple., Test with custom name., TestDictToNamedtuple

### Community 80 - "Package Build and Versioning"
Cohesion: 0.25
Nodes (8): get_release_tag(), used to package ionbus_utils, Return the exact release tag from env/git, or None if unavailable., Write the package runtime version source., Read the package runtime version source., read_version_file(), write_version_file(), setuptools

### Community 81 - "Packaged Guide Validation"
Cohesion: 0.22
Nodes (5): tarfile, built_artifacts(), fixture, Inspect actual distributions and import resources from a built wheel., zipfile

### Community 82 - "Whitespace Regex Replacement"
Cohesion: 0.22
Nodes (5): Tests for SPACE_RE pattern., Test replacing single spaces., Test replacing multiple consecutive spaces., Test replacing mixed whitespace., TestSpaceRe

### Community 83 - "Enumeration Value Validation"
Cohesion: 0.25
Nodes (4): Any, Returns the key (if it exists) for a given enum value, Lets me set internal values, but throws an error if any of the enum values are…, Returns true if this value is a valid enum value

### Community 84 - "Comma String Conversion"
Cohesion: 0.29
Nodes (6): list_to_comma_string(), Converts list to string. Uses quote character if provided, Tests for list_to_comma_string function., Test joins with comma., Test with quote character., TestListToCommaString

### Community 85 - "JSON File Loading"
Cohesion: 0.25
Nodes (7): load_class_from_file(), load_json(), Any, Path, Dynamically load a class from a Python file. Useful for plugin systems where…, Reads json from filename, dealing with both comments and trailing commas, Test loading JSON from file.

### Community 86 - "Multiline Comma Formatting"
Cohesion: 0.29
Nodes (6): multiline_comma_join(), Does a multiline comma join, Tests for multiline_comma_join function., Joins with newlines and spacing., Respects use_quotes flag., TestMultilineCommaJoin

### Community 87 - "Recursive Dictionary Key Normalization"
Cohesion: 0.29
Nodes (6): Input is nested dictionary with possible dictionary and other values. Any…, recursively_uppercase_dict_keys(), Tests for recursively_uppercase_dict_keys function., Test uppercases string keys., Test recursive uppercasing of nested dicts., TestRecursivelyUppercaseDictKeys

### Community 88 - "Timestamped Unique Identifiers"
Cohesion: 0.32
Nodes (5): Returns timestamped unique ID based on unique uuid, timestamped_unique_id(), Tests for timestamped_unique_id function., Test contains underscore separator., TestTimestampedUniqueId

### Community 89 - "Timestamped Identifiers"
Cohesion: 0.32
Nodes (5): Returns timestamped ID. This ID is NOT guaranteed to be unique. Uses…, timestamped_id(), Tests for timestamped_id function., Test generates unique IDs., TestTimestampedId

### Community 90 - "Next Month Calculation"
Cohesion: 0.25
Nodes (5): Tests for first_day_of_next_month function., Test returns first day of next month., Test December rolls to January of next year., Test with datetime input., TestFirstDayOfNextMonth

### Community 91 - "Warn Once Behavior"
Cohesion: 0.25
Nodes (5): Tests for warn_once function., Test warn_once logs the first time., Test warn_once doesn't log same location+message twice., Test warn_once logs different messages., TestWarnOnce

### Community 92 - "Notice Logging Registration"
Cohesion: 0.25
Nodes (5): Tests for NOTICE level registration., Test NOTICE level has correct value., Test NOTICE level is registered., Test logger has notice method., TestNoticeLevelRegistered

### Community 93 - "Word Character Filtering"
Cohesion: 0.25
Nodes (5): Tests for NON_LETTER_LIKE_RE pattern., Test removing non-word characters., Test keeping letters and numbers., Test keeping underscores (part of \\w)., TestNonLetterLikeRe

### Community 94 - "Digit Filtering"
Cohesion: 0.25
Nodes (5): Tests for NON_DIGIT_RE pattern., Test removing letters., Test removing punctuation., Test keeping only digits., TestNonDigitRe

### Community 95 - "Module Name Lookup"
Cohesion: 0.33
Nodes (5): get_module_name(), Returns module name of the filename passed in. If nothing passed in, the module…, Tests for get_module_name function., Test returns parent directory name., TestGetModuleName

### Community 96 - "CLI Parser Dependencies"
Cohesion: 0.29
Nodes (4): ArgParseRangeAction, ArgumentParser, Namespace, An argparse action that requires a range of arguments in argparse. min_args…

### Community 97 - "Documented Git Release Contracts"
Cohesion: 0.38
Nodes (7): Generate, create and push an annotated tag, Git command output and batch execution, Git repository, version and submodule utilities, Pre-push verification and BadStages, Submodule state inspection, Hashtag-driven version tag generation, Commit-hashtag Git auto-versioning

### Community 98 - "Package API Overview"
Cohesion: 0.33
Nodes (6): Import-package resource contract, Wheel, source archive and editable resource checks, Utility module documentation catalog, Pip distribution and editable installation, ionbus_utils package-index description, Concise utility module overview

### Community 99 - "String Enum Compatibility"
Cohesion: 0.33
Nodes (4): Tests for StrEnum import., Test that StrEnum is available., Test creating a StrEnum subclass., TestStrEnum

### Community 100 - "Log Level Configuration"
Cohesion: 0.33
Nodes (4): Tests for set_log_level function., Test setting log level with integer., Test setting log level with string., TestSetLogLevel

### Community 101 - "Logging Configuration Exceptions"
Cohesion: 0.33
Nodes (4): Tests for BadLogConfigError., Test BadLogConfigError is a RuntimeError., Test error message is preserved., TestBadLogConfigError

### Community 102 - "YAML String Factories"
Cohesion: 0.33
Nodes (4): Tests for from_yaml_string factory method., Test loading from YAML string., Test loading with explicit name., TestFromYamlString

### Community 103 - "YAML Tree Lifecycle"
Cohesion: 0.40
Nodes (3): Any, Get a value with hierarchical lookup. Lookup order: 1. Check if this object has…, Serialize the model to a YAML string. This is a convenience method that…

### Community 104 - "Conditional Debug Logging"
Cohesion: 0.50
Nodes (3): log_debug_if(), log_ifs at the DEBUG level., Test log_debug_if function.

### Community 105 - "Conditional Info Logging"
Cohesion: 0.50
Nodes (3): log_info_if(), log_ifs at the INFO level., Test log_info_if function.

### Community 106 - "Conditional Notice Logging"
Cohesion: 0.50
Nodes (3): log_notice_if(), log_ifs at the NOTICE level., Test log_notice_if function.

## Ambiguous Edges - Review These
- `Legacy core_utils names in time examples` → `Utility module documentation catalog`  [AMBIGUOUS]
  time_utils.md · relation: conceptually_related_to

## Knowledge Gaps
- **19 isolated node(s):** `get_file_hash documented contract`, `Caller-derived module path utilities`, `Regex-driven DataFrame column order`, `Conda ionbus_utils import smoke test`, `log_exception usage contract` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 825 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Legacy core_utils names in time examples` and `Utility module documentation catalog`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Enumerate` connect `Enumeration Key Operations` to `Enumeration Key Value Tests`, `Enumerate Objects`, `Enumeration Prefix Value Tests`, `Enumeration Key Validation Tests`, `Enumeration Value Validation Tests`, `Enumeration Value Collection Tests`, `Enumeration Iteration Tests`, `Enumeration Callable Lookup Tests`, `Enumeration String Representation Tests`, `Enumeration Value Validation`, `General Platform Helpers`, `Enumeration String Initialization Tests`, `Enumeration Dictionary Initialization Tests`, `Enumeration Integer Mode Tests`, `Enumeration Bitflag Mode Tests`, `Enumeration Attribute Error Tests`, `Enumeration Integer Value Tests`, `Enumeration List Initialization Tests`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Why does `TestEnumerate` connect `Enumerate Objects` to `Enumeration Value Collection Tests`, `Enumeration Key Validation Tests`, `Enumeration Key Operations`, `Enumeration Value Validation Tests`, `Enumeration Iteration Tests`, `Enumeration Callable Lookup Tests`, `Test Imports and Bootstrap`, `Enumeration Attribute Error Tests`, `Enumeration String Initialization Tests`, `Enumeration List Initialization Tests`, `Enumeration Dictionary Initialization Tests`, `Enumeration Integer Mode Tests`, `Enumeration Bitflag Mode Tests`, `Enumeration Key Value Tests`, `Enumeration Integer Value Tests`, `Enumeration Prefix Value Tests`, `Enumeration String Representation Tests`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Why does `PDYaml` connect `YAML Tree Lifecycle` to `YAML Thread Root Tracking`, `YAML Tree Lifecycle`, `YAML Defaults and Serialization`, `YAML File Loading`, `YAML Initialization Tests`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `Enumerate` (e.g. with `TestEnumerate` and `.test_as_bit()`) actually correct?**
  _`Enumerate` has 23 INFERRED edges - model-reasoned connections that need verification._
- **What connects `get_file_hash documented contract`, `Caller-derived module path utilities`, `Regex-driven DataFrame column order` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Git Repository Operations` be split into smaller, more focused modules?**
  _Cohesion score 0.05143191116306254 - nodes in this community are weakly interconnected._
## Refresh validation

Incremental deep refresh used the Codex session for semantic extraction; no external API call was made. Token usage is unavailable from this host's agent tool; reported zeros are placeholders, not measured zero usage. AST extraction health warnings are recorded below; unresolved dynamic calls are not proven code relationships.

```text
[graphify] MultiDiGraph edge-collapse diagnostic
input: <in-memory>
input_stage: provided JSON (normal graph.json is post-build)
effective_directed: <direct-call>
nodes: 176
unverified_code_nodes: 0
raw_edges: 296
valid_candidate_edges: 261
missing_endpoint_edges: 0
dangling_endpoint_edges: 35
external_reference_edges: 0
self_loop_edges: 0
exact_duplicate_edges: 0
directed_unique_endpoint_pairs: 255
directed_same_endpoint_collapsed_edges: 6
undirected_unique_endpoint_pairs: 255
undirected_same_endpoint_collapsed_edges: 6
same_endpoint_group_count: 6
relation_variant_groups: 3
source_file_variant_groups: 0
source_location_variant_groups: 0
context_variant_groups: 3
post_build_graph_type: Graph
post_build_edges: 289
producer_suppression_sites: 12
producer_suppression_examples:
  - L1646 seen_ids arity=unknown
  - L2179 seen_ids arity=unknown
  - L2181 seen_doc_refs arity=unknown
  - L2551 seen_ids arity=unknown
  - L2698 seen_ids arity=unknown
  - L3424 seen_keys arity=unknown
  - L3593 seen_keys arity=unknown
  - L5669 seen_ids arity=unknown
examples:
  - agent_skill_destination -> agent_skill_py_path edges=2 relations=['references'] locations=['L147'] contexts=['parameter_type', 'return_type']
  - agent_skill_install -> agent_skill_installation edges=2 relations=['calls', 'references'] locations=['L224', 'L249'] contexts=['call', 'generic_arg']
  - tests_conftest_temp_file -> tests_conftest_py_path edges=2 relations=['references'] locations=['L24'] contexts=['parameter_type', 'return_type']
  - tests_conftest_auth_env -> tests_conftest_py_path edges=2 relations=['references'] locations=['L42'] contexts=['generic_arg', 'parameter_type']
  - tests_test_agent_skill_test_atomic_failure_preserves_existing_file -> tests_test_agent_skill_test_atomic_failure_preserves_existing_file_fail_replace edges=2 relations=['contains', 'indirect_call'] locations=['L223', 'L226'] contexts=['', 'argument']
note: normal graph.json is post-build; raw producer loss must be measured earlier.
```
