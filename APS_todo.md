# Agent Project Setup To-do

Implementation checklist for `AGENT_PROJECT_SETUP.md` in `ionbus_utils`.

## Current validation

Implemented and validated in the session's `pixi_311_pd22` environment on
Windows/Python 3.11. The full suite passed with 410 tests and 3 skips; the new
editable-install test also passed. All three artifact checks and Ruff checks
pass. Self-installation created both platform stubs, then repeated without
changing bytes or timestamps. Only the six requested case-only Git renames are
staged; no `git add` or commit has run, and `.gitignore` has not been modified.

Remaining checks need other interpreters/platforms, a Conda build, or fresh
client sessions. Project skill files have been installed, but their presence
is not a claim that an already running client has discovered them.

## 1. Rename documentation

- [x] Rename `readme.md` to `README.md`.
- [x] Rename `readme_ai.md` to `README_AI.md`.
- [x] Rename `readme_pip.md` to `README_PIP.md`.
- [x] Rename `crypto_utils/readme.md` to `crypto_utils/README.md`.
- [x] Rename `git_utils/readme.md` to `git_utils/README.md`.
- [x] Rename `yaml_utils/readme.md` to `yaml_utils/README.md`.
- [x] Perform case-only renames through temporary intermediate filenames on Windows so Git records the new casing.

Keep topical documentation such as `logging.md` and `cache_utils.md` in lowercase snake_case.

## 2. Update filename references

- [x] Update Markdown links and other references to the renamed files.
- [x] Update the package description filename in `pyproject.toml` and `setup.py` to `README_PIP.md`.
- [x] Check build/release configuration and documentation for remaining references to the old names.

## 3. Add repository agent instructions

- [x] Create `AGENTS.md` with instructions for agents developing this repository.
- [x] Require reading relevant parts of `README_AI.md` and inspecting source and tests before changing public behavior.
- [x] Require confirming the development environment for the current session before running commands; ask if it is not already stated, and do not hardcode an environment name or assume one from a prior session.
- [x] Document how to invoke the project's environment runner with the confirmed environment.
- [x] State the required test, lint, and other validation commands.
- [x] Explain when to use Graphify for relationships and change impact, and when to refresh the graph.
- [x] Link to `README_AGENT_SKILLS.md` for the shared installer rationale.
- [x] If Claude needs a compatibility entry point, add `CLAUDE.md` containing the actual `@AGENTS.md` import.

## 4. Implement the shared skill deployment script

- [x] Add the standard-library-only `agent_skill.py` module with reusable functions and `main()`, supporting `python -m ionbus_utils.agent_skill`.
- [x] Implement `show <import_package> [relative-resource]`, defaulting to `README_AI.md`.
- [x] Read UTF-8 package resources through `importlib.resources.files()`.
- [x] Reject absolute resource paths, `..` components, empty components, and missing resources.
- [x] Implement `install <import_package> --platform <platform> [<platform> ...] (--project <path> | --user)`.
- [x] Require an explicit import package name, platform selection, and exactly one destination scope.
- [x] Support `claude`, `codex`, and explicit `all` through one platform destination table.
- [x] Use the selected interpreter without guessing or activating a different environment.
- [x] Generate deterministic thin `SKILL.md` stubs that invoke `show`; do not copy guide content into the skills.
- [x] Normalize and validate skill names, and reject collisions between different import packages.
- [x] Verify package importability and guide readability before any writes.
- [x] Validate that resolved destinations remain beneath their intended roots.
- [x] Preflight every selected destination before writing: missing files can be created, identical files are unchanged, and conflicting files require `--force`.
- [x] Write files atomically using UTF-8, LF newlines, and one trailing newline.
- [x] Report concise errors and exact partial successes if an operating-system failure interrupts a multi-destination installation.
- [x] Define and document exit codes: `0` for successful creation, forced replacement, or an identical-file no-op; distinct nonzero codes for conflicts and operational failures.
- [x] Keep installation explicit and one package at a time; do not add bulk discovery or a registry.

## 5. Add the generic template

- [x] Add `agent_skill_template.py` beside `agent_skill.py` as a separate, Ionbus-agnostic template for copying and adaptation.
- [x] Keep the real installer independent of this template.

The template is specified by `AGENT_PROJECT_SETUP.md`. A runnable fallback for environments without `ionbus_utils` remains deferred; this template does not implement that fallback.

## 6. Document skill installation

- [x] Create `README_AGENT_SKILLS.md` as the canonical explanation of the shared mechanism.
- [x] Explain thin generated stubs, explicit environment selection, import-package targets, and installation one package at a time.
- [x] Document required platform and scope options, destination paths, idempotence, conflicts, and `--force`.
- [x] Include installation and resource-reading examples for this package and other packages.
- [x] Explain how another project can copy and adapt the generic template.
- [x] Review `README_AI.md` examples against current public APIs before making it the installed agent guide.

## 7. Correct packaging

- [x] Restrict package discovery to actual Python packages so directories such as `graphify-out/` are not treated as packages.
- [x] Verify guides and linked resources in wheels, sdists, and editable installs.
- [ ] Inspect an actual Conda artifact for the same resources; the recipe uses the verified Python packaging path, but no Conda artifact has been built.
- [x] Preserve support for Python source at the repository root and raw checkout/submodule imports.
- [x] Keep the existing Conda description unless explicitly choosing to make it consume `README_PIP.md`.
- [x] Inspect built artifacts to verify resource paths and exact filename casing.

## 8. Add validation

- [x] Add `tests/test_agent_skill.py` with tests for `show`, default and linked resources, missing packages/resources, and unsafe resource paths.
- [x] Test project and user scopes; each platform individually; and explicit `--platform all`.
- [x] Test missing, identical, conflicting, and forced destination writes, including conflicts in a multi-platform preflight.
- [x] Test safe name normalization, normalization collisions, and destination containment.
- [x] Verify deterministic generated content and no timestamp changes for identical files.
- [x] Test the documented success, conflict, and operational-failure exit codes.
- [x] Test wheel, editable-install, and raw checkout/submodule resource access.
- [ ] Validate Python 3.9 and the newest supported Python version on Windows and a POSIX platform.
- [ ] Smoke-test discovery of generated skills in Claude Code and Codex.
- [x] Use the finished installer against `ionbus_utils` itself in the confirmed environment: `python -m ionbus_utils.agent_skill install ionbus_utils --platform all --project .`.
- [x] Verify that `python -m ionbus_utils.agent_skill show ionbus_utils` reads the guide, including linked resources.
- [ ] Verify discovery in a fresh Claude Code and Codex session.
- [x] Repeat the self-installation to verify an identical-file no-op with unchanged content and timestamps.
- [x] Run the repository's required checks before completing the implementation.

## 9. Finish Graphify integration

- [x] Generate and commit the portable graph outputs and manifest.
- [x] Ignore local Graphify cache and machine/run-specific files.
- [x] Install project Graphify skills using Graphify's own installer for the intended platforms.
- [x] Document the local stdio MCP launch using the selected Graphify environment; configure each client separately as needed.
- [x] Document the incremental refresh command for each context, since the trigger notation differs by tool, not just by shell: `$graphify . --update --mode deep` as a Codex skill prompt, `/graphify . --update --mode deep` as a Claude Code skill prompt, and plain `graphify . --update --mode deep` with no prefix when run directly from a Command Prompt or PowerShell session outside either agent.
- [x] Refresh the graph after implementing this checklist.

## Change constraints

- [ ] Ask the user before any further modification to `.gitignore`.
- [x] Keep machine-specific interpreter paths and MCP configuration out of shared repository artifacts.

## Graph refresh result

The incremental deep refresh completed with 1,814 nodes, 2,713 edges, and 128
communities. Semantic extraction used the Codex session without an external API
call. Raw extraction diagnostics reported 35 dangling endpoint edges and 6
collapsed edge pairs; the report records these limitations. The exported graph
has valid endpoints. Vendored skills are excluded through `.graphifyignore`;
`.gitignore` remains unchanged.
