# Package-owned agent skills

`ionbus_utils.agent_skill` installs one import package's guide as a discoverable
agent skill. Run it with the Python interpreter selected for the current task.
The installer uses the standard library; importing a target package still loads
that package's initializer and needs its normal dependencies.

## Install and read

The target is an import package name, such as `ionbus_utils`, not its distribution
name (`ionbus-utils`). It must be importable and ship `README_AI.md` at its import
root, plus the Markdown resources that guide links to.

```text
python -m ionbus_utils.agent_skill install ionbus_utils --platform claude codex --project .
python -m ionbus_utils.agent_skill install another_package --platform all --user
python -m ionbus_utils.agent_skill show ionbus_utils
python -m ionbus_utils.agent_skill show ionbus_utils logging.md
```

Both `--platform` and exactly one scope (`--project <path>` or `--user`) are
required. There is no automatic environment selection, distribution-metadata
scan, registry, or bulk installer. A checkout or submodule works when its parent
directory is on the selected interpreter's `sys.path`.

The platform table in `agent_skill.py` owns these destinations:

| Platform | Project | User |
|---|---|---|
| Claude Code | `<project>/.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` |
| Codex | `<project>/.agents/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` |

`all` explicitly selects every platform currently in that table. Packages are
lowercased and their underscores/dots become hyphens for the skill identifier.
Unsafe identifiers and collisions between different import package names are
errors; `--force` cannot overwrite another package's ownership.

## Why the skill is a thin stub

Generated skills tell the agent to run `show` using the current project's Python
environment. They contain no copied API guide and no interpreter path, so they
read the documentation installed with the package version actually being used.
A user-level skill can be visible in an environment without that package; `show`
then reports the selected interpreter, package, and resource rather than guessing
another environment.

Resources are read as UTF-8 with `importlib.resources.files()`. Linked resource
paths are package-relative, using `/` (Windows `\` is also accepted). Absolute
paths, drive-qualified paths, empty components, `.` and `..` are rejected.
Missing guides and resources produce concise errors. No `.dist-info` or
`.egg-info` discovery is involved.

## Write behavior and exit codes

The package and guide are checked first. All selected destinations are then
preflighted before any directory or file is created:

- A missing file is created.
- An identical file is a no-op, preserving its bytes and timestamp.
- Different content is a conflict unless `--force` is supplied.
- A normalized-name collision remains a conflict even with `--force`.

Writes use a temporary file beside the destination followed by `os.replace()`.
Content is deterministic UTF-8 with LF newlines and one trailing newline. Known
conflicts cause no writes. An operating-system error during installation can
leave earlier destinations completed; the error names completed, failed, and
unattempted destinations. This is not a transaction across directories.

| Exit code | Meaning |
|---|---|
| `0` | Successful creation, forced replacement, or identical-file no-op |
| `1` | Content conflict or package-name collision |
| `2` | Argument, import/resource, path, or filesystem error |

## Reusing the mechanism

Other Ionbus packages use this shared installer instead of duplicating it, and
link to this guide for the rationale. `agent_skill_template.py` is a separate
Ionbus-agnostic outline for copying and adaptation. It is not a runnable fallback
for environments without `ionbus_utils`. Use `agent_skill.py` as the working
reference and implement the template's validation and write behavior before
using an adapted installer.

## Graphify integration

Use Graphify's own installer in the confirmed Graphify environment:

```text
graphify install --project --platform claude
graphify install --project --platform codex
graphify install --project --platform agents
```

Graphify 0.9.69's project `codex` target installs its Codex instructions and hook
under `.codex/`. Its `agents` target also installs the skill in `.agents/skills/`,
the directory current Codex uses for project skill discovery. The extra command
uses Graphify's installer rather than maintaining another copy by hand. Check
the installed Graphify version's destinations when upgrading.

Graphify's generated hooks invoke `graphify` on `PATH`. Launch the client from
the confirmed Graphify environment, or adapt its local configuration to use
that environment's runner. Project skill files alone do not prove discovery in
an already running client; restart it and check its skill list.

Keep the portable graph, report, HTML, and manifest in `graphify-out/`. Local
cache, interpreter/root paths, and run diagnostics stay local. Agent prompts are
`$graphify . --update --mode deep` in Codex and `/graphify . --update --mode deep`
in Claude Code. Terminal sessions use `graphify . --update --mode deep`, without
an agent trigger prefix; semantic extraction there uses the configured backend.

For MCP, configure each client on its own machine to start a stdio server. The
portable launch shape is:

```text
python -m graphify.serve --graph <absolute-path-to-checkout>/graphify-out/graph.json
```

Select the Graphify environment explicitly, using its interpreter or environment
runner. Graphify need not be a runtime dependency of this library. Keep actual
machine-specific interpreter paths in local client configuration. The graph on
disk persists; the client starts and stops the stdio process as needed.
