# Agent Setup for Ionbus-Style Python Libraries

## Goal

This repository is designed to work well with coding agents such as
Codex and Claude.

The project may be consumed either:

-   as a normal installed Python package, or
-   directly from Git, including as a Git submodule.

Python source may live directly at the repository top level; do **not**
assume a `src/` layout.

## Canonical Filenames

Use these names and this exact casing throughout the Ionbus package
family:

-   `README.md` — human-facing package documentation;
-   `README_AI.md` — agent-facing package API and usage guide;
-   `README_PIP.md` — the concise package-index description used for
    PyPI and, where a Conda recipe is explicitly configured to use it,
    Conda package metadata;
-   `AGENTS.md` — instructions for agents developing the repository;
-   `SKILL.md` — an installed agent skill (generated, see below); and
-   `README_AGENT_SKILLS.md` — the canonical explanation, living only in
    `ionbus_utils`, of how and why the shared skill-installation
    mechanism works. Other packages link to it; they don't each carry
    their own copy.

Uppercase basenames are reserved for conventional entry-point and
agent-control documents (`README*.md`, `AGENTS.md`, `SKILL.md`).
Topical documents use lowercase snake_case names, such as `logging.md`,
`cache_utils.md`, and `file_utils.md`. The `.md` extension stays
lowercase in every case.

Exact casing matters on case-sensitive filesystems and keeps different
repositories referring to the same conceptual file with the same name.
When applying this to an existing Git repository on Windows, perform
case-only renames through a temporary intermediate filename so Git
records the rename reliably.

## Documentation Roles

Keep these files conceptually separate:

### `README.md` — Human documentation

For people using or developing the package: installation, public API,
examples, and normal project documentation.

### `README_AI.md` — Agent-facing package usage guide

The primary guide for an agent **using this library from another
project**. It should explain:

-   what the package does;
-   when to use it and when not to;
-   important concepts and design intent;
-   public/recommended APIs;
-   common workflows and recipes;
-   examples of correct usage;
-   important constraints and invariants;
-   common mistakes and APIs/patterns to avoid.

Prefer task-oriented guidance. This file teaches an agent how to *use*
the package — it is not the place for internal architecture or design
rationale aimed at people developing the package itself. `ionbus_utils`
is the one exception that needs to explain a design rationale (why its
skill-installation mechanism works the way it does), and that lives in
`README_AGENT_SKILLS.md`, not here.

### `README_PIP.md` — Package-index description

Intentionally separate from the full `README.md`. It provides the
shorter distribution description selected by the Python build
metadata and uploaded to PyPI. A Conda recipe may reuse it for its own
package description when explicitly configured to do so; the Python
project's `readme` setting alone does not guarantee every Conda build
workflow consumes it.

### `AGENTS.md` — Instructions for agents developing this repository

Tells Codex, Claude, and other coding agents **how to work on this
package itself**. It should tell agents to:

1.  Read `README_AI.md` for package intent and usage before changing
    public behavior.
2.  Use Graphify when investigating code relationships, dependencies,
    callers, or change impact.
3.  Inspect actual source and tests before editing; generated
    documentation and graphs are aids, not source of truth.
4.  Use the project's normal Pixi/uv environment and commands. Don't
    hardcode a specific environment name in this file — the same
    repository is worked on across different machines whose
    environment names differ. Instead, **confirm which environment
    applies to the current session before running commands** (ask if
    it isn't already stated), rather than assuming or reusing a name
    from a prior session (see "Environment selection" below).
5.  Run the required tests, linting, typing, etc. before completing
    changes.

Do not duplicate the full `README_AI.md` in `AGENTS.md`.

Claude Code reads `AGENTS.md` directly as of v2.1.277; v2.1.281 or
later additionally fixes sessions on some backends (e.g. Amazon
Bedrock) that couldn't read it in the initial release. When direct
support is unavailable or uncertain, put an actual import in
`CLAUDE.md`:

```markdown
@AGENTS.md
```

Don't use a prose instruction such as "See AGENTS.md" — Claude only
opens a file it's told about in words if it decides to, while an
`@path` import is expanded and loaded into context at launch
unconditionally. Codex reads `AGENTS.md` natively with no version gate
documented.

## Agent Skill Installation

Each Ionbus package can be discovered by coding agents as an installed
skill. The mechanism is deliberately centralized rather than
reimplemented per package.

### No bulk discovery

There is no command that scans the environment and installs every
available package's skill. Each package is installed explicitly, one
at a time. No entry-point registry or distribution-metadata discovery
is involved.

### One shared implementation

The implementation lives once, in `ionbus_utils.agent_skill`, and uses
only the Python standard library. It exposes `main()` plus the reusable
functions, and supports execution with `python -m`.

`ionbus_utils` is a normal part of every release and is assumed to be
installed wherever another Ionbus package is. The standard
skill-installation command assumes `ionbus_utils` is importable. No
other package needs its own `agent_skill` module or its own
`install()` — they're just named as the target argument:

```bash
python -m ionbus_utils.agent_skill install <import_package> \
    --platform <platform> [<platform> ...] \
    (--project <path> | --user)
```

`ionbus_utils` installs its own skill the same way, with no
special-casing — the package-name argument is always required
explicitly, including for `ionbus_utils` installing itself:

```bash
python -m ionbus_utils.agent_skill install ionbus_utils --platform all --project .
```

Behavior when `ionbus_utils` isn't installed — developing
`ionbus_utils` itself before it's installed anywhere, or a non-Ionbus
package that wants this mechanism without the dependency — is left for
a later revision of this document rather than specified now.

A generic, deliberately Ionbus-agnostic template for that eventual
fallback — meant to be copied and adapted, not run as-is — lives
alongside the real implementation as `agent_skill_template.py`, next to
`ionbus_utils/agent_skill.py`. It is a separate file from the one
`ionbus_utils` itself runs, precisely so it can stay free of the
Ionbus-specific assumptions the real module doesn't need to avoid.

### Target-package contract

The target argument is an **import package name** (e.g. `ionbus_utils`),
not a PyPI/Conda distribution name — the mechanism resolves it through
Python's import system, not installer metadata. A participating package
must:

1.  be importable in the selected Python environment;
2.  ship `README_AI.md` as a resource at its import-package root;
3.  ship any Markdown files referenced by `README_AI.md` as package
    resources at their corresponding relative paths; and
4.  include those resources in wheels, sdists, editable installs, and
    Conda packages as applicable.

The installer never inspects installer-generated distribution metadata
(`.dist-info`/`.egg-info`). A raw checkout or Git submodule works
identically to an installed package as long as its parent directory is
on the selected interpreter's `sys.path` and both `ionbus_utils` and
the target package are importable from there.

### Resource reading

```python
from importlib import resources

resource = resources.files(import_package).joinpath("README_AI.md")
content = resource.read_text(encoding="utf-8")
```

Use `importlib.resources.files()` (added in Python 3.9) and its
`Traversable.read_text()` method. Do **not** use the older,
module-level `importlib.resources.read_text(package, resource)`
function — it was deprecated in Python 3.11 in favor of `files()`.

The installed skill invokes a stable, dedicated command rather than
hand-assembling this snippet:

```bash
python -m ionbus_utils.agent_skill show <import_package>
python -m ionbus_utils.agent_skill show <import_package> <relative-resource>
```

The resource argument defaults to `README_AI.md`; the second form lets
an agent follow a relative link such as `[logging.md](logging.md)`
found inside `README_AI.md` without knowing the package's physical
install location. Resource names must be relative package-resource
paths — reject absolute paths, `..` components, empty components, and
resources that don't exist. Read text as UTF-8. A missing package or
resource produces a concise error naming the selected interpreter, the
target import package, and the missing resource.

### Environment selection

`agent_skill` runs inside whichever environment the invoker — human or
agent — is already targeting. It does not guess, activate, or prefer a
Pixi, uv, Conda, venv, or system interpreter. This isn't a limitation
to route around: if two environments on the same machine have
different versions of a package installed, there is no safe way to
guess which one is correct, only whichever one the current task is
actually about. This is why a consuming repository's own `AGENTS.md`
should state how agents run commands in that repository's managed
environment.

### Generated `SKILL.md`

The installed skill is an intentionally generated, deterministic stub
— it never copies `README_AI.md` content, so it can never go stale
against the installed package's guide. Installing `ionbus_utils`
generates content conceptually equivalent to:

```markdown
---
name: ionbus-utils
description: Use when code imports or integrates ionbus_utils; load the installed package's agent-facing API and usage guide before choosing APIs or recreating its functionality.
---

# ionbus_utils package guidance

Use the Python environment selected for the current project.

Run:

    python -m ionbus_utils.agent_skill show ionbus_utils

If `README_AI.md` references another packaged document, read it with:

    python -m ionbus_utils.agent_skill show ionbus_utils <relative-resource>
```

Derive the skill name from the import package by lowercasing it and
replacing underscores and dots with hyphens; validate the result as a
safe skill identifier before constructing any path. Treat a
normalization collision between two different packages as an error —
never silently merge or overwrite one package's skill with another's.

This generic, templated description is sufficient for the initial
design: the skill triggers when an agent is working with the named
import package, while the actual capabilities and recipes stay in
`README_AI.md`. Add a package-specific description override only if
real discovery failures demonstrate the need.

Because the stub's content is deterministic, no separate version marker
is needed. Re-running `install` compares the complete generated content
with the existing file: identical content is a successful no-op, while
different content is a conflict unless `--force` was supplied. That
direct comparison provides both drift detection and idempotence.

### Destination scope

Exactly one scope is required:

-   `--project <path>` writes project skills below the explicitly
    supplied directory. Use `--project .` for the current directory —
    the path is always required, so an arbitrary subdirectory is never
    silently treated as the repository root.
-   `--user` writes below the user's home directory, using each
    platform's documented user-level skill directory.

Resolve and validate the destination root before writing. Construct
child paths only from validated skill and platform identifiers, and
verify every resolved destination remains below its intended root.

A user-scoped stub may be visible in a project whose current Python
environment doesn't contain its target package — that's expected. The
`show` command fails clearly in that case and tells the agent to use an
environment where the target package is importable, rather than
failing silently or resolving the wrong thing.

### Platform selection

`--platform` is required — there is no default to `all`. Requiring the
option means a future addition to the platform table can't silently
broaden the filesystem effects of an old, already-scripted command.
Recognized values:

-   `claude`;
-   `codex`; and
-   `all`, meaning every platform currently present in the
    implementation's platform table (so `all` doesn't need updating at
    call sites when a new platform is added later).

```bash
python -m ionbus_utils.agent_skill install ionbus_utils \
    --platform claude codex --project .

python -m ionbus_utils.agent_skill install ionbus_utils \
    --platform all --user
```

Initial destinations:

| Platform    | Project destination                          | User destination                        |
| ----------- | --------------------------------------------- | ---------------------------------------- |
| Claude Code | `<root>/.claude/skills/<skill-name>/SKILL.md` | `~/.claude/skills/<skill-name>/SKILL.md` |
| Codex       | `<root>/.agents/skills/<skill-name>/SKILL.md` | `~/.agents/skills/<skill-name>/SKILL.md` |

The platform table owns these mappings and any version caveats; call
sites don't reproduce the paths themselves.

### Write safety

Before generating or writing any skill files, verify that the target
package is importable in the selected Python environment and that its
`README_AI.md` resource exists and is readable. If either check fails,
report the error and write nothing.

Generate the complete expected content for every selected destination
and preflight all of them before writing anything:

-   missing file — plan to create it;
-   identical file — a successful no-op; leave its timestamp and
    content untouched;
-   different file — report a conflict and write nothing unless
    `--force` was supplied.

`--force` is the only overwrite authorization — no interactive prompt,
no separate `--yes` alias. One explicit flag behaves predictably for
humans, agents, and CI alike.

After a successful preflight, create parent directories as needed and
write each file atomically (temporary file in the destination
directory, then `os.replace()`). Emit deterministic UTF-8 with LF
newlines and a single trailing newline, so comparisons behave the same
across platforms. Preflighting prevents a known conflict on one
destination from causing a partial multi-platform write; an operating
system failure between individual replacements can still occur, so
report exactly which destinations succeeded and which failed rather
than claiming a cross-directory transaction.

Suggested exit behavior:

-   `0` — created, overwritten with `--force`, or already identical;
-   nonzero conflict code — different content exists and `--force` was
    not supplied;
-   nonzero operational code — invalid arguments, import/resource
    failure, unsafe path, or filesystem error.

An uninstall command isn't needed initially — removing a small
generated directory by hand is adequate until an actual need justifies
more management machinery.

## Documentation and Rationale

`ionbus_utils/README_AGENT_SKILLS.md` is the canonical explanation of
the shared mechanism. It should cover:

-   why skills are thin, generated stubs rather than copied guides;
-   why the selected Python environment is always explicit;
-   why the install target is an import package name, not a
    distribution name;
-   why installation is one package at a time, with no bulk driver;
-   why `--platform` and destination scope are both required rather
    than defaulted;
-   how write-safety/conflict protection works; and
-   how another project can copy and adapt the stdlib-only
    implementation from Git if it doesn't want the `ionbus_utils`
    dependency.

Every other Ionbus package's `AGENTS.md` links to this document instead
of duplicating its rationale. This doesn't prohibit a package from
keeping separate design documentation for its own internal
architecture if it ever needs one — there's just no speculative
placeholder for that today.

## Graphify

Graphify provides structural understanding of the repository to coding
agents. It manages its own paths and installation — Ionbus doesn't
invent competing conventions on top of it:

-   Install its project skill with Graphify's own installer, e.g.
    `graphify install --project` for Claude Code or `graphify install
    --project --platform codex` for Codex. This writes
    `.claude/skills/graphify/SKILL.md` and/or
    `.agents/skills/graphify/SKILL.md` itself.
-   Its persistent graph/output lives in `graphify-out/` (`graph.html`,
    `GRAPH_REPORT.md`, `graph.json`) — Graphify's own documented
    location. Commit the documented portable outputs and ignore
    machine/run-specific files per Graphify's own guidance.

Graphify complements the documentation:

-   `README_AI.md` describes **what the library means and how to use
    it**.
-   `AGENTS.md` describes **how an agent should work on the
    repository**.
-   Graphify describes **how the current implementation is
    structurally connected**.
-   Source code and tests remain the final authority.

Do not expect Graphify to replace source inspection, particularly for
dynamic Python behavior such as registries, decorators, dependency
injection, runtime configuration, dynamic imports, or reflection.

## Graphify MCP

Use Graphify's local MCP integration so Codex/Claude can query the code
graph directly.

For a normal local setup, prefer the stdio MCP mode rather than
maintaining a permanent HTTP service. The coding-agent client starts the
Graphify MCP process as needed and communicates with it locally. The
persistent artifact is the graph on disk, not a long-running server.

Graphify itself may be installed globally with Pixi rather than UV. It
is a developer tool and does not need to be part of every project's
Python runtime environment.

## Recommended Agent Workflow

When modifying this package:

1.  Read `AGENTS.md`.
2.  Read relevant parts of `README_AI.md`.
3.  Use Graphify for structural/dependency questions when useful.
4.  Inspect the actual source and tests involved.
5.  Make the change.
6.  Run the repository's required validation/tests.
7.  Update `README_AI.md` if the agent-facing API, recommended usage,
    or constraints changed.
8.  Refresh Graphify output when required by the repository workflow.

When using this package from another project:

1.  Discover its skill under `.claude/skills/<skill-name>/` (Claude
    Code) or `.agents/skills/<skill-name>/` (Codex) — installed by
    running `python -m ionbus_utils.agent_skill install <import_package>`.
2.  Read the skill's instructions.
3.  Run the skill's `show` command to read the installed package's
    `README_AI.md` for detailed usage guidance.
4.  Prefer the documented public APIs and recipes instead of recreating
    package functionality.
5.  Inspect installed source/API when documentation is insufficient
    rather than guessing.

## Validation Matrix

Before adopting this convention across packages, test at least:

-   Python 3.9 and the newest supported Python version;
-   wheel, editable install, and raw checkout/submodule on `sys.path`;
-   Windows and one POSIX platform;
-   `--project` and `--user` destinations;
-   each platform individually and explicit `--platform all`;
-   missing, identical, conflicting, and `--force` destination files;
-   preflight behavior when one of multiple destinations conflicts;
-   missing target package and missing `README_AI.md` errors;
-   `README_AI.md` plus a linked relative resource;
-   rejection of absolute paths and `..` traversal;
-   deterministic skill-name normalization and collision handling; and
-   a smoke test confirming that Claude Code and Codex each discover
    the generated skill from their documented project directories.

Inspect the built wheel or Conda artifact during testing — a
source-tree test alone doesn't prove `README_AI.md` and its linked
documents were actually packaged.

## Guiding Principle

Keep this system simple:

**Human docs + agent usage guide + agent development instructions + one
shared, package-owned skill mechanism + Graphify.**

Avoid adding vector databases, additional code indexes, centralized
skill registries, or other infrastructure unless a demonstrated need
justifies the extra complexity.
