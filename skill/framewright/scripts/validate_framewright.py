#!/usr/bin/env python3
"""Deterministic Framewright artifact, state, and regression validation."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - explicit runtime diagnostic
    raise SystemExit(
        "PyYAML is required. Run this validator with the project's declared Python "
        "environment or the approved shared YAML runtime."
    ) from exc


MODE_RE = re.compile(r"^\[MODE: (AUTEUR|APPRENTICE|SCREENWRITER)\]$")
NATIVE_MENTION_RE = re.compile(r"@(Image|Video|Audio)\s+\d+")
UNRESOLVED_RE = re.compile(
    r"\[(?:resolved|required|insert|todo|tbd)[^\]\n]*\]", re.IGNORECASE
)
FORBIDDEN_PROMPT_TERMS = (
    "INTENT DELTA",
    "UNRESOLVED DECISION",
    "WHY IT MATTERS",
    "FRAMEWRIGHT INFERENCES",
    "RESIDUAL RISK",
    "semantic_trace",
    "intent_ledger",
    "framewright_state",
    "RUN CARD",
)
STATE_REQUIRED = (
    "schema_version",
    "core_version",
    "project_slug",
    "current_scope",
    "active_stage",
    "director_mode",
    "approved_generation_units",
    "active_artifacts",
    "superseded_artifacts",
    "active_intent_entries",
    "intentional_freedom",
    "unresolved_material_decisions",
    "active_material_roles",
    "cross_gu_continuity",
    "selected_generated_takes",
    "last_approved_revision",
    "last_updated",
)
ARTIFACT_REQUIRED = (
    "artifact_id",
    "stage",
    "generation_unit",
    "revision",
    "locator",
    "change_class",
)
CHANGE_CLASSES = {
    "director_refinement",
    "compiler_inference",
    "repair",
    "model_workaround",
}
RISKS = {"low", "medium", "high"}


def issue(code: str, message: str, **context: Any) -> dict[str, Any]:
    result: dict[str, Any] = {"code": code, "message": message}
    if context:
        result["context"] = context
    return result


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"missing YAML frontmatter: {path}")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"frontmatter must be a mapping: {path}")
    return data, text


def validate_prompt_text(
    text: str,
    character_limit: int = 10_000,
    native_bindings: list[str] | None = None,
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    lines = text.splitlines()
    nonempty = [line.strip() for line in lines if line.strip()]
    mode_lines = [line.strip() for line in lines if MODE_RE.fullmatch(line.strip())]

    keyframe_headers = [index for index, line in enumerate(lines) if re.fullmatch(r"KEYFRAME_\d+", line.strip())]
    if keyframe_headers:
        for index in keyframe_headers:
            next_line = lines[index + 1].strip() if index + 1 < len(lines) else ""
            if not MODE_RE.fullmatch(next_line):
                errors.append(issue("mode_line_missing", "Every keyframe block must place one exact mode line after its header."))
        if len(mode_lines) != len(keyframe_headers):
            errors.append(issue("mode_line_count", "Every keyframe block must own exactly one mode line.", count=len(mode_lines)))
    else:
        if not nonempty or not MODE_RE.fullmatch(nonempty[0]):
            errors.append(issue("mode_line_missing", "Prompt must begin with one exact mode line."))
        if len(mode_lines) != 1:
            errors.append(issue("mode_line_count", "Prompt must contain exactly one mode line.", count=len(mode_lines)))
    if len(text) > character_limit:
        errors.append(
            issue(
                "character_limit_exceeded",
                "Prompt exceeds the active character limit.",
                actual=len(text),
                limit=character_limit,
            )
        )
    unresolved = sorted(set(UNRESOLVED_RE.findall(text)))
    if unresolved:
        errors.append(
            issue("unresolved_placeholder", "Prompt contains unresolved instructional placeholders.", values=unresolved)
        )
    for token in FORBIDDEN_PROMPT_TERMS:
        if token.lower() in text.lower():
            errors.append(
                issue("workflow_language_in_prompt", "Assistant-facing workflow language entered the clean prompt.", token=token)
            )

    brace_placeholders = sorted(set(re.findall(r"\{\{[^{}]+\}\}", text)))
    invalid_braces = [value for value in brace_placeholders if value != "{{HANDLE}}"]
    if invalid_braces:
        errors.append(
            issue("invalid_handle_placeholder", "Only {{HANDLE}} is allowed as a generic unresolved handle.", values=invalid_braces)
        )
    if "{{HANDLE}}" in text:
        refs_match = re.search(r"(?:^|\n)REFS:?\s*\n(?P<body>.*?)(?=\n[A-Z][A-Z +/_-]*\n|\Z)", text, re.DOTALL)
        if refs_match is None or "{{HANDLE}}" not in refs_match.group("body"):
            errors.append(issue("handle_outside_refs", "{{HANDLE}} is allowed only inside the generic REFS block."))

    used_mentions = sorted(set(NATIVE_MENTION_RE.findall(text)))
    # The regex above captures types; use full matches for binding comparison.
    used_full = sorted(set(match.group(0) for match in NATIVE_MENTION_RE.finditer(text)))
    if native_bindings is not None:
        declared = sorted(set(native_bindings))
        missing = sorted(set(used_full) - set(declared))
        unused = sorted(set(declared) - set(used_full))
        if missing:
            errors.append(issue("native_mention_unmapped", "A native mention has no declared binding.", values=missing))
        if unused:
            errors.append(issue("native_binding_unused", "A declared native binding is unused.", values=unused))
    del used_mentions
    return errors


def validate_state_data(
    document: Any,
    state_path: Path | None = None,
    check_locators: bool = False,
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    if not isinstance(document, dict) or not isinstance(document.get("framewright_state"), dict):
        return [issue("state_root_missing", "State must contain a framewright_state mapping.")]
    state = document["framewright_state"]
    for key in STATE_REQUIRED:
        if key not in state:
            errors.append(issue("state_key_missing", "Required state key is missing.", key=key))

    active = state.get("active_artifacts", [])
    superseded = state.get("superseded_artifacts", [])
    if not isinstance(active, list) or not isinstance(superseded, list):
        errors.append(issue("artifact_collection_invalid", "Active and superseded artifacts must be lists."))
        return errors

    def validate_artifacts(items: list[Any], status: str) -> list[tuple[str, str, Any]]:
        identities: list[tuple[str, str, Any]] = []
        for index, artifact in enumerate(items):
            if not isinstance(artifact, dict):
                errors.append(issue("artifact_record_invalid", "Artifact record must be a mapping.", status=status, index=index))
                continue
            for key in ARTIFACT_REQUIRED:
                if artifact.get(key) in (None, ""):
                    errors.append(issue("artifact_key_missing", "Artifact record is incomplete.", status=status, index=index, key=key))
            change_class = artifact.get("change_class")
            if change_class not in CHANGE_CLASSES:
                errors.append(issue("change_class_invalid", "Artifact change_class is not approved.", value=change_class))
            identity = (
                str(artifact.get("artifact_id", "")),
                str(artifact.get("generation_unit", "")),
                artifact.get("revision"),
            )
            identities.append(identity)
            if check_locators and artifact.get("locator") and state_path is not None:
                locator = Path(str(artifact["locator"]))
                resolved = locator if locator.is_absolute() else state_path.parent / locator
                if not resolved.exists():
                    errors.append(issue("artifact_locator_missing", "Artifact locator does not exist.", locator=str(locator)))
        return identities

    active_ids = validate_artifacts(active, "active")
    superseded_ids = validate_artifacts(superseded, "superseded")
    active_keys = [(artifact_id, unit) for artifact_id, unit, _ in active_ids]
    if len(active_keys) != len(set(active_keys)):
        errors.append(issue("duplicate_active_revision", "More than one active revision exists for one artifact identity."))
    overlap = set(active_ids) & set(superseded_ids)
    if overlap:
        errors.append(issue("active_superseded_overlap", "The same artifact revision is both active and superseded.", values=sorted(overlap)))

    for take in state.get("selected_generated_takes", []) or []:
        if not isinstance(take, dict) or take.get("director_selected") is not True:
            errors.append(issue("take_not_director_selected", "Only a director-selected generated take may become continuity truth."))
    return errors


def validate_compile_trace(data: dict[str, Any]) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    prompt = data.get("prompt")
    if isinstance(prompt, str):
        errors.extend(
            validate_prompt_text(
                prompt,
                int(data.get("character_limit", 10_000)),
                data.get("native_bindings"),
            )
        )

    owners = data.get("serialization_owners")
    if owners is not None and (not isinstance(owners, list) or len(owners) != 1):
        errors.append(issue("serialization_owner_count", "Exactly one serialization owner must be active."))
    for field, code in (
        ("active_stages", "active_stage_count"),
        ("director_modes", "director_mode_count"),
        ("production_spines", "production_spine_count"),
        ("material_registries", "material_registry_count"),
    ):
        values = data.get(field)
        if values is not None and (not isinstance(values, list) or len(values) != 1):
            errors.append(issue(code, f"{field} must contain exactly one active owner."))

    for unit in data.get("split_units", []) or []:
        if not isinstance(unit, dict) or not unit.get("unit_label"):
            errors.append(issue("split_unit_invalid", "Split unit record must be a labeled mapping."))
            continue
        if not unit.get("start_state") or not unit.get("end_state"):
            errors.append(issue("split_state_missing", "Every approved split unit needs its own start and end state.", unit=unit.get("unit_label")))
        if unit.get("independently_executable") is not True:
            errors.append(issue("split_unit_not_executable", "Every approved split unit must be independently executable.", unit=unit.get("unit_label")))

    for intent in data.get("material_intents", []) or []:
        carriers = intent.get("carriers", []) if isinstance(intent, dict) else []
        if not carriers:
            errors.append(issue("observable_intent_orphan", "A material abstract intent has no observable carrier."))

    for beat in data.get("performance_beats", []) or []:
        if not isinstance(beat, dict):
            errors.append(issue("performance_beat_invalid", "Performance beat must be a mapping."))
            continue
        carriers = beat.get("physical_carriers", []) or []
        if not 1 <= len(carriers) <= 3:
            errors.append(
                issue("performance_carrier_density", "A material performance beat must keep one to three carriers.", beat_id=beat.get("beat_id"), count=len(carriers))
            )
        if beat.get("shot_scale") and beat.get("carrier_legible") is not True:
            errors.append(issue("shot_scale_illegible", "A selected carrier is not legible at the committed shot scale.", beat_id=beat.get("beat_id")))
        if beat.get("exact_dialogue"):
            embodied = any(
                beat.get(key)
                for key in ("onset", "dialogue_delivery", "release_or_aftermath", "listener_response")
            )
            if not embodied:
                errors.append(issue("embodied_dialogue_missing", "Material dialogue has no executable performance causality.", beat_id=beat.get("beat_id")))

    feasibility = data.get("feasibility")
    if isinstance(feasibility, dict):
        systems = feasibility.get("systems", {})
        if not isinstance(systems, dict) or not systems:
            errors.append(issue("feasibility_systems_missing", "Feasibility must assess relevant attention systems."))
        else:
            high_pressure = False
            for system_name, assessment in systems.items():
                if not isinstance(assessment, dict) or assessment.get("risk") not in RISKS or not assessment.get("reason"):
                    errors.append(issue("feasibility_assessment_invalid", "Each relevant system needs low/medium/high risk and a reason.", system=system_name))
                    continue
                high_pressure = high_pressure or assessment["risk"] in {"medium", "high"}
            if high_pressure and not feasibility.get("weakest_beat"):
                errors.append(issue("weakest_beat_missing", "Material feasibility risk must identify the weakest beat."))
            if high_pressure and not feasibility.get("competing_objectives"):
                errors.append(issue("competing_objectives_missing", "Material feasibility risk must identify competing objectives."))
            if feasibility.get("competing_objectives") and not feasibility.get("experience_priority_stack"):
                errors.append(issue("priority_stack_missing", "Competing objectives require a scene-local Experience Priority Stack."))

    for change in data.get("structural_changes", []) or []:
        if not isinstance(change, dict):
            continue
        if change.get("applied") is True:
            if not change.get("function_before") or not change.get("function_transfer"):
                errors.append(issue("structural_function_unaccounted", "Applied structural subtraction has no function transfer."))
            if change.get("user_approved") is not True:
                errors.append(issue("structural_change_unapproved", "Material deletion, merge, split, or loss was applied without director approval."))

    camera = data.get("camera_agency")
    if isinstance(camera, dict) and camera.get("required") is True:
        for key in ("operator_goal", "body_path", "lens_target", "viewer_attachment"):
            if not camera.get(key):
                errors.append(issue("camera_agency_incomplete", "Required embodied camera is missing an execution field.", key=key))
        if camera.get("body_path") == camera.get("lens_target") and camera.get("opposed_paths") is True:
            errors.append(issue("camera_path_conflated", "Operator body path was conflated with an opposed lens target."))

    handoff = data.get("motion_state_handoff")
    if isinstance(handoff, dict):
        if not handoff.get("camera_velocity_and_direction") or not handoff.get("subject_and_world_motion"):
            errors.append(issue("motion_handoff_incomplete", "A relevant cross-unit handoff lacks motion state."))
        source = handoff.get("selected_take_source")
        if source and handoff.get("director_selected_take") is not True:
            errors.append(issue("unselected_take_as_truth", "An unselected generated take became continuity truth."))
        opening = set(handoff.get("opening_only_constraints", []) or [])
        persistent = set(handoff.get("persistent_constraints", []) or [])
        forbidden_overlap = opening & persistent & set(handoff.get("must_not_persist", []) or [])
        if forbidden_overlap:
            errors.append(issue("opening_constraint_persisted", "An opening-only constraint was incorrectly made persistent.", values=sorted(forbidden_overlap)))

    for chain in data.get("physical_causality", []) or []:
        if not isinstance(chain, dict):
            errors.append(issue("physical_chain_invalid", "Physical causality entry must be a mapping."))
            continue
        if chain.get("production_critical") is True:
            for key in ("initial_state", "trigger", "contact", "release_or_lock", "rebound_or_settling", "aftermath"):
                if not chain.get(key):
                    errors.append(issue("physical_chain_incomplete", "A production-critical physical chain is incomplete.", key=key, object=chain.get("object_or_system")))
            if chain.get("mechanical_transformation") is True:
                if not chain.get("part_provenance") or not chain.get("load_bearing_state"):
                    errors.append(issue("transformation_topology_missing", "A critical mechanical transformation lacks provenance or load-bearing state.", object=chain.get("object_or_system")))

    for reference in data.get("reference_admission", []) or []:
        if not isinstance(reference, dict):
            continue
        if not reference.get("conditioning_risk") or not reference.get("practical_loss_if_withheld"):
            errors.append(issue("reference_risk_unassessed", "Runtime reference admission lacks conditioning risk or practical-loss analysis."))
        changed = reference.get("requested_strategy") and reference.get("strategy") != reference.get("requested_strategy")
        if reference.get("director_requested") is True and changed and reference.get("user_approved") is not True:
            errors.append(issue("requested_reference_changed_silently", "A director-requested runtime material strategy changed without approval."))

    prompt_text = prompt if isinstance(prompt, str) else ""
    vocal_events = data.get("vocal_events", []) or []
    seen_events: set[str] = set()
    for event in vocal_events:
        if not isinstance(event, dict):
            errors.append(issue("vocal_event_invalid", "Vocal event must be a mapping."))
            continue
        event_id = str(event.get("event_id", ""))
        if not event_id or event_id in seen_events:
            errors.append(issue("vocal_event_duplicate", "Vocal event IDs must be unique.", event_id=event_id))
        seen_events.add(event_id)
        for key in ("speaker", "exact_text", "language", "beat", "allowed_count"):
            if event.get(key) in (None, ""):
                errors.append(issue("vocal_event_incomplete", "Vocal event is missing ownership data.", event_id=event_id, key=key))
        exact_text = str(event.get("exact_text", ""))
        allowed = event.get("allowed_count")
        if exact_text and isinstance(allowed, int) and prompt_text.count(exact_text) != allowed:
            errors.append(issue("vocal_event_count_mismatch", "Exact vocal text count differs from its approved event count.", event_id=event_id, expected=allowed, actual=prompt_text.count(exact_text)))
    for reaction in data.get("silent_reaction_beats", []) or []:
        if isinstance(reaction, dict) and (reaction.get("speech") or reaction.get("subtitle_or_visible_text")):
            errors.append(issue("silence_ownership_violation", "A silent reaction acquired speech or visible text.", beat_id=reaction.get("beat_id")))

    state = data.get("state")
    if state is not None:
        errors.extend(validate_state_data(state, check_locators=False))
    return errors


def validate_fixture(path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        return [issue("fixture_invalid", "Fixture must be a mapping.")], {}
    kind = data.get("kind")
    if kind == "compile_trace":
        errors = validate_compile_trace(data)
    elif kind == "state":
        errors = validate_state_data(data.get("document"), check_locators=False)
    elif kind == "prompt":
        errors = validate_prompt_text(
            str(data.get("prompt", "")),
            int(data.get("character_limit", 10_000)),
            data.get("native_bindings"),
        )
    else:
        errors = [issue("fixture_kind_invalid", "Fixture kind is not supported.", kind=kind)]
    return errors, data


def validate_core(core: Path, skill: Path, profile: Path, manifest: Path) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    try:
        core_meta, core_text = frontmatter(core)
        skill_meta, skill_text = frontmatter(skill)
        profile_meta, profile_text = frontmatter(profile)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [issue("frontmatter_invalid", str(exc))]

    if core_meta.get("version") != "3.5.1":
        errors.append(issue("candidate_version_mismatch", "Core candidate must identify as 3.5.1.", actual=core_meta.get("version")))
    if skill_meta.get("name") != "framewright" or not skill_meta.get("description"):
        errors.append(issue("skill_frontmatter_invalid", "Skill frontmatter name or description is invalid."))
    if not profile_meta.get("profile_version"):
        errors.append(issue("profile_frontmatter_invalid", "Runtime profile version is missing."))

    for name, text in (("core", core_text), ("skill", skill_text), ("profile", profile_text)):
        if len(re.findall(r"^```", text, re.MULTILINE)) % 2:
            errors.append(issue("markdown_fence_unbalanced", "Markdown fences are unbalanced.", file=name))

    manifest_data = load_yaml(manifest)
    anchors = manifest_data.get("protected_anchors", []) if isinstance(manifest_data, dict) else []
    for anchor in anchors:
        if str(anchor) not in core_text and str(anchor) not in skill_text and str(anchor) not in profile_text:
            errors.append(issue("protected_anchor_missing", "A protected semantic anchor is missing.", anchor=anchor))
    return errors


def emit(path: str, errors: list[dict[str, Any]], json_output: bool = False) -> int:
    status = "PASS" if not errors else "FAIL"
    if json_output:
        print(json.dumps({"path": path, "status": status, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        print(f"{status}: {path}")
        for item in errors:
            print(f"  {item['code']}: {item['message']}")
    return 0 if not errors else 1


def run_regression(fixtures: Path, json_output: bool = False) -> int:
    results: list[dict[str, Any]] = []
    suite_errors = 0
    for path in sorted(fixtures.glob("*.yaml")):
        errors, data = validate_fixture(path)
        expected = data.get("expected", "pass")
        expected_codes = set(data.get("expected_errors", []) or [])
        actual_codes = {item["code"] for item in errors}
        passed = (expected == "pass" and not errors) or (
            expected == "fail" and bool(errors) and expected_codes.issubset(actual_codes)
        )
        if not passed:
            suite_errors += 1
        results.append(
            {
                "fixture": path.name,
                "expected": expected,
                "status": "PASS" if passed else "FAIL",
                "observed_errors": sorted(actual_codes),
            }
        )
    if not results:
        print(f"FAIL: no fixtures found in {fixtures}")
        return 1
    if json_output:
        print(json.dumps({"status": "PASS" if suite_errors == 0 else "FAIL", "results": results}, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(f"{result['status']}: {result['fixture']} (expected {result['expected']})")
        print(f"SUMMARY: {len(results) - suite_errors}/{len(results)} fixtures matched expectations")
    return 0 if suite_errors == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prompt_parser = subparsers.add_parser("prompt")
    prompt_parser.add_argument("path", type=Path)
    prompt_parser.add_argument("--character-limit", type=int, default=10_000)

    state_parser = subparsers.add_parser("state")
    state_parser.add_argument("path", type=Path)
    state_parser.add_argument("--check-locators", action="store_true")

    fixture_parser = subparsers.add_parser("fixture")
    fixture_parser.add_argument("path", type=Path)

    regression_parser = subparsers.add_parser("regression")
    regression_parser.add_argument("directory", type=Path)

    core_parser = subparsers.add_parser("core")
    core_parser.add_argument("--core", type=Path, required=True)
    core_parser.add_argument("--skill", type=Path, required=True)
    core_parser.add_argument("--profile", type=Path, required=True)
    core_parser.add_argument("--manifest", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "prompt":
        return emit(str(args.path), validate_prompt_text(args.path.read_text(encoding="utf-8"), args.character_limit), args.json)
    if args.command == "state":
        return emit(str(args.path), validate_state_data(load_yaml(args.path), args.path, args.check_locators), args.json)
    if args.command == "fixture":
        errors, _ = validate_fixture(args.path)
        return emit(str(args.path), errors, args.json)
    if args.command == "regression":
        return run_regression(args.directory, args.json)
    if args.command == "core":
        return emit(
            str(args.core),
            validate_core(args.core, args.skill, args.profile, args.manifest),
            args.json,
        )
    return 2


if __name__ == "__main__":
    sys.exit(main())
