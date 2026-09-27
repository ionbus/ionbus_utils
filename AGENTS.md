# Working on ionbus_utils

Read [README_AI.md](README_AI.md) for package intent and recommended APIs before
changing public behavior. Inspect the actual source and tests involved; guides
and generated graphs are aids, and source and tests remain the authority.

## Environment

Confirm the Python environment for the current session before running Python
commands. Use the user's stated environment; ask if none is stated. Do not
hardcode an environment name here or reuse one from a previous session.

Use the project's normal Pixi/uv runner. Where the Ionbus environment-management
scripts are installed, the Windows Command Prompt form is:

```bat
call "%USERPROFILE%\bin\python_env_management\run-env.bat" <confirmed-environment> python <arguments>
```

The PowerShell form is:

```powershell
& "$env:USERPROFILE\bin\python_env_management\run-env.bat" <confirmed-environment> python <arguments>
```

For a raw checkout or Git submodule, the directory containing `ionbus_utils`
must be on the selected interpreter's `sys.path`. Run tests from this repository
root; the test configuration makes the checkout importable. The skill installer
uses the selected interpreter and does not choose or activate an environment.

## Investigation and validation

Use the existing Graphify graph for relationships, callers, dependencies, and
change impact when useful. Verify findings against source, especially dynamic
Python behavior. Use direct file inspection for small documentation changes.

Before completing code changes, run in the confirmed environment:

```text
python -m pytest tests/ -q
python -m ruff check <changed-python-files>
python -m ruff format --check <changed-python-files>
```

Installer and packaging coverage lives in `tests/test_agent_skill.py` and
`tests/test_agent_skill_packaging.py`. Packaging tests build disposable copies
and inspect the wheel and source archive. Report failures and distinguish
unavailable platform/interpreter checks from passing checks. There is no separate
type-check command configured for this repository.

Update `README_AI.md` when public APIs, recommended usage, or constraints change.
Refresh Graphify after implementation changes, using the Graphify environment
confirmed for the session; it can differ from the runtime environment.

## Agent skills and Graphify

See [README_AGENT_SKILLS.md](README_AGENT_SKILLS.md) for the shared installer,
resource contract, and rationale. Use `ionbus_utils.agent_skill` to deploy one
package's skill at a time. Use Graphify's own installer for Graphify skills.

Agent prompt forms for incremental deep refresh:

- Codex: `$graphify . --update --mode deep`
- Claude Code: `/graphify . --update --mode deep`

The terminal form is `graphify . --update --mode deep`. A terminal semantic pass
uses its configured backend; an agent skill can use the agent session. Prefer
local stdio MCP; see the setup examples in `README_AGENT_SKILLS.md`.

## Editing constraints

Ask the user before modifying `.gitignore`. Do not stage or commit changes unless
requested. On Windows, use two `git mv` commands through a temporary name for
case-only renames. These commands stage the renames, so confirm that effect is
authorized if the user has prohibited staging.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
