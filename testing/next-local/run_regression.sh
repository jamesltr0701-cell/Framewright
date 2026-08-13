#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)
VALIDATOR="$REPO_ROOT/skill/framewright/scripts/validate_framewright.py"
PYTHON_BIN=${FRAMEWRIGHT_PYTHON:-/Users/jameslee/Documents/Codex/_shared-tools/python/yaml-runtime/bin/python}

"$PYTHON_BIN" -c "import yaml"
"$PYTHON_BIN" "$VALIDATOR" core \
  --core "$REPO_ROOT/skill/framewright/references/framewright.md" \
  --skill "$REPO_ROOT/skill/framewright/SKILL.md" \
  --profile "$REPO_ROOT/skill/framewright/references/runtime_profiles/seedance_2_5.md" \
  --manifest "$SCRIPT_DIR/expected/protected_anchors.yaml"
"$PYTHON_BIN" "$VALIDATOR" regression "$SCRIPT_DIR/fixtures"
