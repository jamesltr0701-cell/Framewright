#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)
VALIDATOR="$REPO_ROOT/skill/framewright-merge/scripts/validate_framewright.py"
PYTHON_BIN=${FRAMEWRIGHT_PYTHON:-/Users/jameslee/Documents/Codex/_shared-tools/python/yaml-runtime/bin/python}

"$PYTHON_BIN" -c "import yaml"
"$PYTHON_BIN" "$VALIDATOR" core \
  --core "$REPO_ROOT/skill/framewright-merge/references/framewright.md" \
  --skill "$REPO_ROOT/skill/framewright-merge/SKILL.md" \
  --profile "$REPO_ROOT/skill/framewright-merge/references/runtime_profiles/seedance_2_0.md" \
  --profile "$REPO_ROOT/skill/framewright-merge/references/runtime_profiles/seedance_2_5.md" \
  --profile "$REPO_ROOT/skill/framewright-merge/references/runtime_profiles/minimax_h3.md" \
  --image-profile "$REPO_ROOT/skill/framewright-merge/references/keyframe_profiles/midjourney_v7.md" \
  --image-profile "$REPO_ROOT/skill/framewright-merge/references/keyframe_profiles/chatgpt_image_2_edit.md" \
  --registry "$REPO_ROOT/skill/framewright-merge/references/runtime_profiles/adapter_registry.yaml" \
  --image-registry "$REPO_ROOT/skill/framewright-merge/references/keyframe_profiles/adapter_registry.yaml" \
  --manifest "$SCRIPT_DIR/expected/protected_anchors.yaml"
"$PYTHON_BIN" "$VALIDATOR" regression "$SCRIPT_DIR/fixtures"

PROMPT_PATH=$(mktemp /private/tmp/framewright-merge-seedance20-adapter.XXXXXX)
KEYFRAME_PROMPT_PATH=$(mktemp /private/tmp/framewright-merge-midjourney-v7-adapter.XXXXXX)
trap 'rm -f -- "$PROMPT_PATH" "$KEYFRAME_PROMPT_PATH"' EXIT HUP INT TERM
printf '%s\n' 'A woman crosses the room. Quiet ventilation and synchronized footsteps; no music.' > "$PROMPT_PATH"
"$PYTHON_BIN" "$VALIDATOR" video-prompt "$PROMPT_PATH" \
  --target-model seedance_2_0 \
  --serialization-owner framewright_merge_adapter_seedance_2_0 \
  --adapter-id seedance_2_0 \
  --profile-contract seedance_2_0 \
  --registry "$REPO_ROOT/skill/framewright-merge/references/runtime_profiles/adapter_registry.yaml"

printf '%s\n' 'A woman motionless at the rain-lit window, medium close-up, spherical 50mm perspective, quiet blue-grey dawn, wet glass reflections, restrained natural texture --ar 16:9 --v 7' > "$KEYFRAME_PROMPT_PATH"
"$PYTHON_BIN" "$VALIDATOR" keyframe-prompt "$KEYFRAME_PROMPT_PATH" \
  --adapter-id midjourney_v7 \
  --image-registry "$REPO_ROOT/skill/framewright-merge/references/keyframe_profiles/adapter_registry.yaml"
