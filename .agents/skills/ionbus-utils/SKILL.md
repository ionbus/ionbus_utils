---
name: ionbus-utils
description: Use when code imports or integrates ionbus_utils; load the installed package's agent-facing API and usage guide before choosing APIs or recreating its functionality.
metadata:
  import-package: ionbus_utils
---

# ionbus_utils package guidance

Use the Python environment selected for the current project.

Run:

    python -m ionbus_utils.agent_skill show ionbus_utils

If `README_AI.md` references another packaged document, read it with:

    python -m ionbus_utils.agent_skill show ionbus_utils <relative-resource>
