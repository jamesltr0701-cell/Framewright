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
H3_LABEL_RE = re.compile(r"<(Subject|Picture|Video|Audio)\s+\d+>")
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
    "generation_evidence",
    "take_disposition",
    "attempt_budget",
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
    "beat_scope",
    "continuation_contracts",
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
PROMPT_IR_REQUIRED = (
    "ir_schema_version",
    "core_version",
    "target_model",
    "generation_unit",
    "directing_intention",
    "scene_grammar",
    "final_look",
    "active_references",
    "start_state",
    "end_state",
    "endpoint_purpose",
    "visible_actions",
    "shot_or_phase_plan",
    "camera_contract",
    "performance_contract",
    "sound_contract",
    "continuity_locks",
    "completed_beats",
    "current_beats",
    "reserved_future_beats",
    "hard_constraints",
    "intentional_freedom",
    "unresolved_material_decisions",
    "adapter_input_status",
)
CHANGE_CLASSES = {
    "director_refinement",
    "compiler_inference",
    "repair",
    "model_workaround",
}
RISKS = {"low", "medium", "high"}
OBSERVATION_PROVENANCE = {"observed", "reported"}
OBSERVATION_CONFIDENCE = {"low", "medium", "high"}
CONTINUATION_TYPES = {"seamless_extension", "next_shot", "bridge", "tail_repair", "re_anchor"}
TAKE_DISPOSITIONS = {"accept", "post_fix", "local_edit", "retry", "rewrite_or_split", "do_not_generate"}
ROOT_CAUSE_CLASSES = {"planning", "serialization", "rendering", "reference_authority", "runtime_or_surface", "model_behavior"}
SEEDANCE_ROUTES = {"omni_reference", "smart_edit", "long_video", "first_last_frames", "extend"}
SEEDANCE_CONTROLS = {"multi_keyframe", "blockout_coarse", "blockout_fine", "seamless_transition"}
H3_ROUTES = {"t2va", "i2va", "fl2va", "l2va", "ref2va"}
H3_API_ROLES = {"first_frame", "last_frame", "reference_image", "reference_video", "reference_audio"}
H3_VISIBLE_RELATIONSHIPS = {"fully_preserved", "partially_preserved", "attribute_transfer", "weak_reference"}
H3_AUDIO_RELATIONSHIPS = {"fully_copy", "partially_copy", "reference", "weak_reference"}
DRAMATIC_LENSES = {
    "turn_or_progression",
    "objective_obstacle_tactic",
    "subtext_contradiction",
    "power_or_information_change",
}
INSTRUMENT_RELATIONSHIPS = {"support", "counterpoint", "neutral"}
DEFAULT_REGISTRY = (
    Path(__file__).resolve().parent.parent
    / "references"
    / "runtime_profiles"
    / "adapter_registry.yaml"
)
OWNERSHIP_PROMPT_TERMS = (
    "target_model",
    "serialization_owner",
    "adapter_id",
    "compiler_instruction_sources",
    "framewright_merge_adapter_seedance_2_0",
    "framewright_merge_adapter_seedance_2_5",
    "framewright_merge_adapter_minimax_h3",
)
PLATFORM_SERIALIZER_KEY_RE = re.compile(
    r"(?:platform|surface|provider|jimeng|libtv).*(?:dialect|serializ|owner)"
    r"|(?:dialect|serializ|owner).*(?:platform|surface|provider|jimeng|libtv)",
    re.IGNORECASE,
)


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


def validate_registry_data(document: Any, registry_path: Path) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    if not isinstance(document, dict):
        return [issue("adapter_registry_invalid", "Adapter registry must be a mapping.")]
    sources = document.get("compiler_instruction_sources")
    if not isinstance(sources, list) or not sources or any(not isinstance(value, str) or not value for value in sources):
        errors.append(issue("compiler_source_registry_invalid", "Registry compiler instruction sources must be non-empty scalar paths."))
    targets = document.get("registered_targets")
    if not isinstance(targets, dict) or not targets:
        return errors + [issue("adapter_registry_targets_missing", "Adapter registry has no registered target mappings.")]

    owners: list[str] = []
    adapter_ids: list[str] = []
    package_root = registry_path.resolve().parents[2]
    repository_root = package_root.parents[1]
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, str) or not source:
                continue
            resolved_source = (repository_root / source).resolve()
            if (resolved_source != package_root and package_root not in resolved_source.parents) or not resolved_source.is_file():
                errors.append(issue("compiler_source_registry_path_invalid", "Registered compiler instruction source is missing or outside the Framewright package.", source=source))
    for target_model, record in targets.items():
        if not isinstance(target_model, str) or not target_model or not isinstance(record, dict):
            errors.append(issue("adapter_registry_record_invalid", "Every registered target requires a mapping.", target_model=target_model))
            continue
        owner = record.get("serialization_owner")
        if not isinstance(owner, str) or not owner:
            errors.append(issue("adapter_registry_owner_invalid", "Every target requires one scalar serialization owner.", target_model=target_model))
        else:
            owners.append(owner)
        adapter_id = record.get("adapter_id")
        profile = record.get("profile")
        if "core_native_profile" in record:
            errors.append(issue("legacy_core_native_profile_forbidden", "Every target must use a formal adapter; Core Native profile records are forbidden.", target_model=target_model))
        if not isinstance(adapter_id, str) or not adapter_id:
            errors.append(issue("adapter_registry_id_invalid", "Every target requires one non-empty adapter ID.", target_model=target_model))
        else:
            adapter_ids.append(adapter_id)
        if not isinstance(profile, str) or not profile:
            errors.append(issue("adapter_registry_profile_invalid", "Every target requires one adapter profile path.", target_model=target_model))
        else:
            resolved = (registry_path.parent / profile).resolve()
            if package_root not in resolved.parents or not resolved.is_file():
                errors.append(issue("adapter_registry_profile_missing", "Registered adapter profile is missing or outside the Framewright package.", target_model=target_model, profile=profile))
    if len(owners) != len(set(owners)):
        errors.append(issue("adapter_registry_owner_duplicate", "Serialization owners must be unique across registered targets."))
    if len(adapter_ids) != len(set(adapter_ids)):
        errors.append(issue("adapter_registry_id_duplicate", "Adapter IDs must be unique across registered targets."))
    return errors


def load_adapter_registry(path: Path = DEFAULT_REGISTRY) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    try:
        document = load_yaml(path)
    except (OSError, yaml.YAMLError) as exc:
        return {}, [issue("adapter_registry_unreadable", str(exc), path=str(path))]
    errors = validate_registry_data(document, path)
    return document if isinstance(document, dict) else {}, errors


def registered_profile_source(profile: str) -> str:
    return f"skill/framewright-merge/references/runtime_profiles/{profile}"


def ownership_validation_required(data: dict[str, Any]) -> bool:
    return data.get("artifact_stage") == "video_prompt" or any(
        key in data
        for key in (
            "target_model",
            "serialization_owner",
            "serialization_owners",
            "adapter_id",
            "compiler_instruction_sources",
            "adapter_profile_contract",
            "core_native_profile_contract",
            "seedance25",
            "minimax_h3",
        )
    )


def find_platform_serializer_fields(value: Any, prefix: str = "") -> list[str]:
    matches: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            if PLATFORM_SERIALIZER_KEY_RE.search(str(key)):
                matches.append(path)
            matches.extend(find_platform_serializer_fields(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            matches.extend(find_platform_serializer_fields(child, f"{prefix}[{index}]"))
    return matches


def validate_serialization_ownership(
    data: dict[str, Any],
    prompt: str,
    registry_path: Path = DEFAULT_REGISTRY,
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    registry, registry_errors = load_adapter_registry(registry_path)
    errors.extend(registry_errors)
    targets = registry.get("registered_targets", {}) if isinstance(registry, dict) else {}

    if "serialization_owners" in data:
        errors.append(issue("serialization_owner_plural_forbidden", "Use one scalar serialization_owner; plural owner lists are forbidden."))
    owner = data.get("serialization_owner")
    if owner is None:
        errors.append(issue("serialization_owner_missing", "Video Prompt validation requires one scalar serialization_owner."))
    elif not isinstance(owner, str):
        errors.append(issue("serialization_owner_not_scalar", "serialization_owner must be a scalar string."))
    elif not owner.strip():
        errors.append(issue("serialization_owner_empty", "serialization_owner must not be empty."))

    target_model = data.get("target_model")
    if target_model is None:
        errors.append(issue("target_model_missing", "Video Prompt validation requires a resolved target_model."))
    elif not isinstance(target_model, str) or not target_model.strip():
        errors.append(issue("target_model_invalid", "target_model must be a non-empty scalar string."))

    registered = targets.get(target_model) if isinstance(targets, dict) and isinstance(target_model, str) else None
    if target_model is not None and not isinstance(registered, dict):
        errors.append(issue("target_model_unregistered", "Target model is not registered for Framewright serialization.", target_model=target_model))
    if isinstance(owner, str) and owner and targets:
        owners = {
            record.get("serialization_owner")
            for record in targets.values()
            if isinstance(record, dict)
        }
        if owner not in owners:
            errors.append(issue("serialization_owner_unregistered", "Serialization owner is not registered for Framewright.", serialization_owner=owner))
    if isinstance(registered, dict) and isinstance(owner, str) and owner != registered.get("serialization_owner"):
        errors.append(issue("target_owner_mismatch", "Target model and serialization owner do not match the registry.", target_model=target_model, serialization_owner=owner))

    expected_adapter = registered.get("adapter_id") if isinstance(registered, dict) else None
    actual_adapter = data.get("adapter_id")
    if data.get("core_native_profile_contract") is not None:
        errors.append(issue("legacy_core_native_contract_forbidden", "Serialization may not claim a Core Native profile contract."))
    if actual_adapter is None:
        errors.append(issue("adapter_id_missing", "Every target serialization requires the registered adapter ID.", expected=expected_adapter))
    elif actual_adapter != expected_adapter:
        errors.append(issue("adapter_id_mismatch", "Adapter ID does not match the registered target and owner.", expected=expected_adapter, actual=actual_adapter))
    matching_contract = (
        isinstance(data.get("seedance25"), dict)
        if expected_adapter == "seedance_2_5"
        else isinstance(data.get("minimax_h3"), dict)
        if expected_adapter == "minimax_h3"
        else data.get("adapter_profile_contract") == expected_adapter
    )
    if not matching_contract and data.get("adapter_profile_contract") != expected_adapter:
        errors.append(issue("adapter_profile_contract_missing", "Adapter owner requires its matching profile contract.", expected=expected_adapter))
    foreign_contract = (
        expected_adapter == "seedance_2_5" and "minimax_h3" in data
    ) or (
        expected_adapter == "minimax_h3" and "seedance25" in data
    )
    if foreign_contract:
        errors.append(issue("adapter_profile_contract_mismatch", "A foreign adapter profile contract is present."))

    sources = data.get("compiler_instruction_sources")
    if not isinstance(sources, list) or not sources or any(not isinstance(value, str) or not value for value in sources):
        errors.append(issue("compiler_instruction_sources_invalid", "Compiler instruction sources must be a non-empty list of scalar paths."))
    else:
        base_sources = registry.get("compiler_instruction_sources", []) if isinstance(registry, dict) else []
        required_sources = set(base_sources if isinstance(base_sources, list) else [])
        allowed_sources = set(required_sources)
        allowed_sources.add("skill/framewright-merge/references/runtime_profiles/adapter_registry.yaml")
        profile = registered.get("profile") if isinstance(registered, dict) else None
        if isinstance(profile, str):
            profile_source = registered_profile_source(profile)
            required_sources.add(profile_source)
            allowed_sources.add(profile_source)
        missing_sources = sorted(required_sources - set(sources))
        foreign_sources = sorted(set(sources) - allowed_sources)
        if missing_sources:
            errors.append(issue("compiler_instruction_source_missing", "Required compiler instruction source is missing.", values=missing_sources))
        if foreign_sources:
            errors.append(issue("compiler_instruction_source_unregistered", "Compiler instruction source is not registered for this ownership route.", values=foreign_sources))

    platform_fields = sorted(set(find_platform_serializer_fields(data)))
    if platform_fields:
        errors.append(issue("platform_serializer_forbidden", "Platform or surface fields may not own or select Framewright serialization.", values=platform_fields))

    leaked = sorted(token for token in OWNERSHIP_PROMPT_TERMS if token.lower() in prompt.lower())
    if leaked:
        errors.append(issue("ownership_metadata_leak", "Clean prompt contains compiler ownership metadata.", values=leaked))
    return errors


def validate_prompt_text(
    text: str,
    character_limit: int = 10_000,
    native_bindings: list[str] | None = None,
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    lines = text.splitlines()
    mode_lines = [line.strip() for line in lines if MODE_RE.fullmatch(line.strip())]
    if mode_lines:
        errors.append(
            issue(
                "mode_metadata_leak",
                "Director Mode is conversation-visible internal metadata and must not enter a clean Prompt.",
                values=mode_lines,
            )
        )
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


def validate_prompt_ir_data(document: Any) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    if not isinstance(document, dict) or not isinstance(document.get("video_prompt_ir"), dict):
        return [issue("prompt_ir_root_missing", "Prompt IR must contain a video_prompt_ir mapping.")]
    prompt_ir = document["video_prompt_ir"]
    for key in PROMPT_IR_REQUIRED:
        if key not in prompt_ir:
            errors.append(issue("prompt_ir_key_missing", "Required Prompt IR key is missing.", key=key))

    registry, registry_errors = load_adapter_registry()
    errors.extend(registry_errors)
    targets = registry.get("registered_targets", {}) if isinstance(registry, dict) else {}
    target = prompt_ir.get("target_model")
    if not isinstance(target, str) or target not in targets:
        errors.append(issue("prompt_ir_target_unregistered", "Prompt IR target must resolve to one registered adapter.", target_model=target))
    if prompt_ir.get("adapter_input_status") != "approved":
        errors.append(issue("prompt_ir_not_approved", "Adapter input status must be approved before serialization."))
    unresolved = prompt_ir.get("unresolved_material_decisions")
    if not isinstance(unresolved, list):
        errors.append(issue("prompt_ir_unresolved_invalid", "Unresolved material decisions must be a list."))
    elif unresolved:
        errors.append(issue("prompt_ir_unresolved_material", "Approved Prompt IR cannot contain unresolved material decisions."))
    if not prompt_ir.get("generation_unit"):
        errors.append(issue("prompt_ir_generation_unit_missing", "Prompt IR requires one active generation unit."))

    scopes: dict[str, set[Any]] = {}
    for key in ("completed_beats", "current_beats", "reserved_future_beats"):
        values = prompt_ir.get(key)
        if not isinstance(values, list):
            errors.append(issue("prompt_ir_beat_scope_invalid", "Each Prompt IR beat scope must be a list.", key=key))
            scopes[key] = set()
        else:
            scopes[key] = set(values)
    overlap = (
        (scopes["completed_beats"] & scopes["current_beats"])
        | (scopes["completed_beats"] & scopes["reserved_future_beats"])
        | (scopes["current_beats"] & scopes["reserved_future_beats"])
    )
    if overlap:
        errors.append(issue("prompt_ir_beat_scope_overlap", "Prompt IR completed, current, and future beat scopes must be disjoint.", beats=sorted(overlap)))

    for forbidden_key in ("serialization_owner", "adapter_id", "native_ref", "ui_mode", "route", "prompt_headings"):
        if forbidden_key in prompt_ir:
            errors.append(issue("adapter_dialect_in_prompt_ir", "Model-neutral Prompt IR contains an adapter-owned field.", key=forbidden_key))
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

    selected_takes = state.get("selected_generated_takes", []) or []
    if not isinstance(selected_takes, list):
        errors.append(issue("selected_takes_invalid", "Selected generated takes must be a list."))
        selected_takes = []
    canon_by_id: dict[str, dict[str, Any]] = {}
    for index, take in enumerate(selected_takes):
        if not isinstance(take, dict):
            errors.append(issue("selected_take_invalid", "Selected generated take must be a mapping.", index=index))
            continue
        if take.get("director_selected") is not True:
            errors.append(issue("take_not_director_selected", "Only a director-selected generated take may become continuity truth."))
        take_id = take.get("take_id")
        source_unit = take.get("source_generation_unit")
        if not isinstance(take_id, str) or not take_id or not isinstance(source_unit, str) or not source_unit:
            errors.append(issue("selected_take_identity_missing", "Continuity-canon take requires take ID and source generation unit.", index=index))
        if take.get("continuity_status") != "accepted":
            errors.append(issue("selected_take_not_accepted", "Continuity-canon take must have accepted continuity status.", take_id=take_id))
        provenance = take.get("observation_provenance")
        confidence = take.get("observation_confidence")
        confirmation = take.get("requires_confirmation")
        if provenance not in OBSERVATION_PROVENANCE or confidence not in OBSERVATION_CONFIDENCE or not isinstance(confirmation, bool):
            errors.append(issue("take_observation_contract_invalid", "Selected take requires valid provenance, confidence, and confirmation fields.", take_id=take_id))
        if provenance == "reported" and (confidence != "low" or confirmation is not True):
            errors.append(issue("reported_take_overclaimed", "Reported, uninspected take state must remain low-confidence and require confirmation.", take_id=take_id))
        actual_end_state = take.get("accepted_actual_end_state")
        if not isinstance(actual_end_state, dict) or not actual_end_state:
            errors.append(issue("accepted_end_state_missing", "Selected take requires a non-empty accepted actual end state.", take_id=take_id))
        completed = set(take.get("completed_beats", []) or [])
        reserved = set(take.get("reserved_future_beats", []) or [])
        if completed & reserved:
            errors.append(issue("selected_take_beat_overlap", "Selected take cannot complete and reserve the same beat.", take_id=take_id, beats=sorted(completed & reserved)))
        if isinstance(take_id, str) and take_id:
            canon_by_id[take_id] = take

    beat_scope = state.get("beat_scope")
    if not isinstance(beat_scope, dict):
        errors.append(issue("beat_scope_invalid", "Beat scope must be a mapping."))
    else:
        scopes: dict[str, set[Any]] = {}
        for key in ("completed", "current_unit", "reserved_future"):
            values = beat_scope.get(key)
            if not isinstance(values, list):
                errors.append(issue("beat_scope_invalid", "Each beat scope must be a list.", key=key))
                scopes[key] = set()
            else:
                scopes[key] = set(values)
        overlaps = (scopes["completed"] & scopes["current_unit"]) | (scopes["completed"] & scopes["reserved_future"]) | (scopes["current_unit"] & scopes["reserved_future"])
        if overlaps:
            errors.append(issue("beat_scope_overlap", "Completed, current-unit, and reserved-future beat scopes must be disjoint.", beats=sorted(overlaps)))

    continuations = state.get("continuation_contracts", []) or []
    if not isinstance(continuations, list):
        errors.append(issue("continuation_contracts_invalid", "Continuation contracts must be a list."))
        continuations = []
    for index, contract in enumerate(continuations):
        if not isinstance(contract, dict):
            errors.append(issue("continuation_contract_invalid", "Continuation contract must be a mapping.", index=index))
            continue
        contract_id = contract.get("continuation_id")
        continuation_type = contract.get("continuation_type")
        if not isinstance(contract_id, str) or not contract_id or continuation_type not in CONTINUATION_TYPES:
            errors.append(issue("continuation_identity_invalid", "Continuation requires an ID and supported type.", index=index))
        source_take_id = contract.get("source_take_id")
        source_take = canon_by_id.get(str(source_take_id))
        if source_take is None or source_take.get("director_selected") is not True or source_take.get("continuity_status") != "accepted":
            errors.append(issue("continuation_source_not_canon", "Continuation source must be the selected accepted continuity take.", source_take_id=source_take_id))
        elif contract.get("source_state") != source_take.get("accepted_actual_end_state"):
            errors.append(issue("continuation_source_state_mismatch", "Continuation source state must match the selected take's accepted actual end state.", source_take_id=source_take_id))
        if not isinstance(contract.get("planned_start_state"), dict) or contract.get("start_state_reconciled") is not True:
            errors.append(issue("continuation_start_unreconciled", "Continuation requires a planned start state reconciled to canon.", continuation_id=contract_id))
        if continuation_type == "seamless_extension":
            if contract.get("open_motion_state") is not True:
                errors.append(issue("seamless_open_motion_missing", "Seamless extension requires an open motion state.", continuation_id=contract_id))
            if contract.get("explicit_cut") is True or contract.get("camera_reset") is True:
                errors.append(issue("seamless_reset_forbidden", "Seamless extension forbids cuts and camera resets.", continuation_id=contract_id))
        if continuation_type == "next_shot" and contract.get("camera_reset") is True and contract.get("explicit_cut") is not True:
            errors.append(issue("next_shot_reset_requires_cut", "Next-shot camera reset requires an explicit cut.", continuation_id=contract_id))
    return errors


def validate_seedance25(data: Any, prompt: str) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    if not isinstance(data, dict):
        return [issue("seedance_contract_invalid", "Seedance 2.5 qualification data must be a mapping.")]

    route = data.get("route")
    if route not in SEEDANCE_ROUTES:
        errors.append(issue("seedance_route_invalid", "Seedance 2.5 route is missing or unsupported.", route=route))

    parameters = data.get("parameter_contract")
    if route in SEEDANCE_ROUTES and not isinstance(parameters, dict):
        errors.append(issue("parameter_contract_missing", "Seedance 2.5 route qualification requires parameter provenance."))
    if isinstance(parameters, dict) and route in SEEDANCE_ROUTES:
        duration = parameters.get("duration", {})
        aspect = parameters.get("aspect_ratio", {})
        expected: dict[str, tuple[set[str], set[str]]] = {
            "omni_reference": ({"user_settable"}, {"user_settable"}),
            "long_video": ({"user_settable"}, {"user_settable"}),
            "smart_edit": ({"platform_locked", "inherited_from_source"}, {"locked_to_source_video"}),
            "first_last_frames": ({"user_settable"}, {"locked_to_first_image"}),
            "extend": ({"user_settable"}, {"locked_to_source_video"}),
        }
        duration_allowed, aspect_allowed = expected[route]
        if not isinstance(duration, dict) or duration.get("provenance") not in duration_allowed:
            errors.append(issue("duration_provenance_invalid", "Duration provenance does not match the selected route.", route=route))
        if not isinstance(aspect, dict) or aspect.get("provenance") not in aspect_allowed:
            errors.append(issue("aspect_provenance_invalid", "Aspect-ratio provenance does not match the selected route.", route=route))
        if route == "smart_edit":
            if duration.get("surface_value") != -1:
                errors.append(issue("smart_edit_duration_lock_invalid", "Smart Edit surface duration must be locked with -1."))
            if aspect.get("surface_value") != "adaptive":
                errors.append(issue("source_aspect_lock_invalid", "Smart Edit aspect ratio must be locked to the source with adaptive."))
        if route in {"first_last_frames", "extend"} and aspect.get("surface_value") != "adaptive":
            errors.append(issue("source_aspect_lock_invalid", "The selected locked-aspect route requires adaptive."))
        if route == "first_last_frames" and data.get("endpoint_aspect_compatible") is not True:
            errors.append(issue("endpoint_aspect_mismatch", "First and last frame images must use the same aspect ratio."))

    materials = data.get("materials")
    if isinstance(materials, dict):
        images = int(materials.get("image_count", 0) or 0)
        videos = int(materials.get("video_count", 0) or 0)
        audio = int(materials.get("audio_count", 0) or 0)
        video_seconds = float(materials.get("video_combined_seconds", 0) or 0)
        audio_seconds = float(materials.get("audio_combined_seconds", 0) or 0)
        if images + videos + audio > 50 or images > 30 or videos > 10 or audio > 10 or video_seconds > 30 or audio_seconds > 30:
            errors.append(issue("material_hard_limit_exceeded", "Seedance 2.5 material count or combined duration exceeds a platform hard limit."))
        stable_exceeded = any(
            (
                int(materials.get("subject_image_count", 0) or 0) > 8,
                int(materials.get("subject_av_count", 0) or 0) > 5,
                float(materials.get("motion_reference_seconds", 0) or 0) > 10,
                float(materials.get("edit_source_seconds", 0) or 0) > 20,
                int(materials.get("edit_reference_image_count", 0) or 0) > 5,
                int(materials.get("storyboard_panel_count", 0) or 0) > 15,
            )
        )
        if stable_exceeded and data.get("stable_range_warning_present") is not True:
            errors.append(issue("stable_range_warning_missing", "A recommendation was exceeded without an assistant-facing stability warning."))
        if images + videos + audio > 0 and data.get("active_subset_mapped") is not True:
            errors.append(issue("active_subset_mapping_missing", "Admitted materials require an explicit active-subset mapping."))

    if route == "smart_edit":
        smart_edit = data.get("smart_edit")
        if not isinstance(smart_edit, dict) or smart_edit.get("sole_source_master") is not True or not smart_edit.get("edit_scope") or not smart_edit.get("content_to_preserve"):
            errors.append(issue("smart_edit_contract_incomplete", "Smart Edit requires one source master, bounded scope, and preservation contract."))
    if route == "long_video":
        stages = data.get("stages")
        if not isinstance(stages, list) or not stages or any(
            not isinstance(stage, dict) or not stage.get("entry_state") or not stage.get("end_state") or not stage.get("principal_change")
            for stage in stages
        ):
            errors.append(issue("long_video_stage_contract_incomplete", "Every Long Video stage requires entry state, one principal change, and end state."))
    if route == "first_last_frames":
        endpoints = data.get("endpoints")
        if not isinstance(endpoints, dict) or not endpoints.get("first_frame") or (
            endpoints.get("last_frame") and not endpoints.get("middle_motion_and_state_change")
        ):
            errors.append(issue("endpoint_authority_incomplete", "First/last route requires explicit endpoint authority and middle motion when both endpoints exist."))
    if route == "extend" and not isinstance(data.get("extension"), dict):
        errors.append(issue("extension_contract_missing", "Extend route requires direction, boundary owner, and trigger."))

    extension = data.get("extension")
    if isinstance(extension, dict):
        direction = extension.get("direction")
        if direction not in {"forward", "backward"}:
            errors.append(issue("extension_direction_invalid", "Extend requires forward or backward direction."))
        expected_boundary = "source_end" if direction == "forward" else "source_start"
        if extension.get("boundary_owner") != expected_boundary:
            errors.append(issue("extension_boundary_invalid", "Extension direction uses the wrong source boundary.", direction=direction))
        trigger = str(extension.get("trigger", "")).lower()
        if not any(token in trigger for token in ("extend", "continue")):
            errors.append(issue("extension_trigger_missing", "Extend requires an explicit extension trigger."))

    controls = data.get("controls", {})
    if isinstance(controls, dict):
        keyframes = controls.get("multi_keyframe")
        if isinstance(keyframes, dict):
            anchors = keyframes.get("ordered_anchors", [])
            if not isinstance(anchors, list) or len(anchors) < 2 or any(
                not isinstance(anchor, dict) or not anchor.get("native_ref") or not anchor.get("state") for anchor in anchors
            ):
                errors.append(issue("keyframe_order_or_state_missing", "Multi-keyframe control requires ordered anchors with state mappings."))
            if keyframes.get("cuts_implied") is not False:
                errors.append(issue("keyframe_cut_inferred", "Keyframe order must not imply cuts automatically."))
        coarse = controls.get("blockout_coarse")
        if isinstance(coarse, dict):
            allowed = set(coarse.get("allowed_authority", []) or [])
            denied = set(coarse.get("denied_authority", []) or [])
            if not {"action_paths", "blocking", "camera_path"}.issubset(allowed) or not {"identity", "final_surface", "final_style"}.issubset(denied):
                errors.append(issue("coarse_blockout_authority_invalid", "Coarse blockout authority is incomplete or leaks final appearance."))
        fine = controls.get("blockout_fine")
        if isinstance(fine, dict):
            allowed = set(fine.get("allowed_authority", []) or [])
            denied = set(fine.get("denied_authority", []) or [])
            if not {"structure", "blocking", "motion", "camera"}.issubset(allowed) or not {"identity", "temporary_material", "final_style"}.issubset(denied):
                errors.append(issue("fine_blockout_authority_invalid", "Fine blockout authority is incomplete or leaks temporary appearance."))
        transition = controls.get("seamless_transition")
        if isinstance(transition, dict):
            for key in ("before_material", "after_material", "trigger", "camera_path", "transformation_or_transition", "arrival_state", "audio_bridge"):
                if not transition.get(key):
                    errors.append(issue("seamless_transition_incomplete", "Seamless transition is missing an execution field.", key=key))
            if transition.get("pixel_identical_preservation_promised") is not False:
                errors.append(issue("pixel_identical_promise", "Seamless transition must not promise pixel-identical preservation."))

    timing = data.get("numeric_timing")
    if isinstance(timing, dict) and timing.get("active") is True:
        if timing.get("trigger_reason") not in {"long_video", "critical_moment", "synchronization", "technique_required"}:
            errors.append(issue("numeric_timing_unqualified", "Numeric timing lacks an approved trigger condition."))
        duration = float(timing.get("resolved_duration", 0) or 0)
        ranges = timing.get("ranges", [])
        previous_end = 0.0
        for index, item in enumerate(ranges if isinstance(ranges, list) else []):
            start = float(item.get("start", -1)) if isinstance(item, dict) else -1
            end = float(item.get("end", -1)) if isinstance(item, dict) else -1
            if start != previous_end or end <= start or end > duration:
                errors.append(issue("numeric_timing_range_invalid", "Numeric timing ranges must be consecutive, non-overlapping, and within duration.", index=index))
                break
            if item.get("critical") is True and not item.get("trigger"):
                errors.append(issue("critical_timing_trigger_missing", "A critical timed event requires a trigger.", index=index))
            if item.get("camera_critical") is True and not item.get("camera_instruction"):
                errors.append(issue("critical_camera_instruction_missing", "A production-critical timed camera event requires camera instruction.", index=index))
            if item.get("state_must_continue") is True and not item.get("continued_state"):
                errors.append(issue("continued_state_missing", "A timed event fails to preserve the state that must continue.", index=index))
            previous_end = end
        if previous_end != duration:
            errors.append(issue("numeric_timing_range_invalid", "Numeric timing ranges do not cover the resolved duration."))

    audio = data.get("audio")
    if isinstance(audio, dict):
        if audio.get("music_requested") is not True and audio.get("music") not in {None, "no_music", "preserve", "remove"}:
            errors.append(issue("unrequested_music", "Seedance syntax activated music without an explicit request."))
        if audio.get("dialogue_requested") is not True and re.search(r"\{[^{}]+\}", prompt):
            errors.append(issue("unrequested_dialogue_syntax", "Dialogue syntax appeared without an approved dialogue scope."))
        if audio.get("visible_text_requested") is not True and "■■" in prompt:
            errors.append(issue("unrequested_visible_text_syntax", "Visible-text syntax appeared without an approved scope."))
        if audio.get("syntax_evidence_grade") not in {None, "current_online", "snapshot_qualified"}:
            errors.append(issue("audio_syntax_evidence_invalid", "Special syntax has no valid evidence grade."))

    typography = data.get("typography_or_frame_accuracy")
    if isinstance(typography, dict) and typography.get("critical") is True:
        if typography.get("assistant_limitation_present") is not True or typography.get("recommended_route") not in {"prepared_asset", "locked_reference", "post_production"}:
            errors.append(issue("typography_limitation_missing", "Critical text or frame accuracy needs an assistant-facing limitation and reliable route."))

    compactness = data.get("compactness")
    if isinstance(compactness, dict):
        if compactness.get("character_count") != len(prompt):
            errors.append(issue("compactness_count_mismatch", "Recorded character count does not match the clean Prompt."))
        if not compactness.get("semantic_anchors"):
            errors.append(issue("compactness_anchors_missing", "Compactness qualification must preserve semantic anchors."))
        if compactness.get("assistant_facing_leakage") is True or compactness.get("inactive_blocks"):
            errors.append(issue("compactness_not_qualified", "Compactness qualification found leakage or inactive blocks."))
    return errors


def validate_minimax_h3(data: Any, prompt: str) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    if not isinstance(data, dict):
        return [issue("h3_contract_invalid", "MiniMax H3 qualification data must be a mapping.")]

    if data.get("explicit_target_selection") is not True:
        errors.append(issue("h3_target_not_explicit", "MiniMax H3 adapter requires explicit target-model selection."))

    route = data.get("route")
    if route not in H3_ROUTES:
        errors.append(issue("h3_route_invalid", "MiniMax H3 route is missing or unsupported.", route=route))

    if len(prompt) > 7000:
        errors.append(issue("h3_prompt_limit_exceeded", "MiniMax H3 prompt exceeds 7,000 characters.", actual=len(prompt)))

    parameters = data.get("parameter_contract")
    if not isinstance(parameters, dict):
        errors.append(issue("h3_parameter_contract_missing", "MiniMax H3 requires duration, resolution, and aspect-ratio provenance."))
    else:
        duration = parameters.get("duration_seconds", {})
        resolution = parameters.get("resolution", {})
        aspect = parameters.get("aspect_ratio", {})
        duration_value = duration.get("resolved_value") if isinstance(duration, dict) else None
        if not isinstance(duration_value, int) or not 4 <= duration_value <= 15:
            errors.append(issue("h3_duration_invalid", "MiniMax H3 duration must be an integer from 4 through 15."))
        if not isinstance(resolution, dict) or resolution.get("resolved_value") not in {"768P", "2K"}:
            errors.append(issue("h3_resolution_invalid", "MiniMax H3 resolution must be 768P or 2K."))
        aspect_value = aspect.get("resolved_value") if isinstance(aspect, dict) else None
        concrete_ratios = {"21:9", "16:9", "4:3", "1:1", "3:4", "9:16"}
        if route == "t2va" and aspect_value not in concrete_ratios:
            errors.append(issue("h3_t2v_ratio_invalid", "H3 T2VA requires a concrete non-adaptive aspect ratio."))
        if route in {"i2va", "fl2va", "l2va"}:
            if not isinstance(aspect, dict) or aspect.get("provenance") != "locked_to_endpoint_image" or aspect_value != "adaptive":
                errors.append(issue("h3_endpoint_ratio_invalid", "H3 endpoint-image routes require an image-locked adaptive ratio."))
        if route == "ref2va" and aspect_value not in concrete_ratios | {"adaptive"}:
            errors.append(issue("h3_reference_ratio_invalid", "H3 Ref2VA ratio is unsupported."))

    bindings = data.get("input_bindings", []) or []
    if not isinstance(bindings, list):
        errors.append(issue("h3_bindings_invalid", "H3 input bindings must be a list."))
        bindings = []
    roles: list[str] = []
    labels: list[str] = []
    for index, binding in enumerate(bindings):
        if not isinstance(binding, dict):
            errors.append(issue("h3_binding_invalid", "H3 input binding must be a mapping.", index=index))
            continue
        role = binding.get("api_role")
        if role not in H3_API_ROLES:
            errors.append(issue("h3_api_role_invalid", "H3 input binding uses an unsupported API role.", index=index, role=role))
        else:
            roles.append(role)
        if not binding.get("material_key") or not binding.get("allowed_authority") or not binding.get("denied_authority"):
            errors.append(issue("h3_binding_authority_missing", "H3 input binding requires stable identity and limited authority.", index=index))
        for label in binding.get("model_labels", []) or []:
            if not H3_LABEL_RE.fullmatch(str(label)):
                errors.append(issue("h3_label_invalid", "H3 model label has invalid syntax.", index=index, label=label))
            else:
                labels.append(str(label))

    endpoint_roles = {"first_frame", "last_frame"} & set(roles)
    reference_roles = {"reference_image", "reference_video", "reference_audio"} & set(roles)
    if endpoint_roles and reference_roles:
        errors.append(issue("h3_role_family_conflict", "H3 endpoint roles and reference roles are mutually exclusive."))
    if route == "t2va" and roles:
        errors.append(issue("h3_t2v_material_present", "H3 T2VA must not contain media bindings."))
    if route == "i2va" and roles != ["first_frame"]:
        errors.append(issue("h3_i2v_role_invalid", "H3 I2VA requires exactly one first-frame binding."))
    if route == "l2va" and roles != ["last_frame"]:
        errors.append(issue("h3_l2v_role_invalid", "H3 L2VA requires exactly one last-frame binding."))
    if route == "fl2va" and sorted(roles) != ["first_frame", "last_frame"]:
        errors.append(issue("h3_fl2v_role_invalid", "H3 FL2VA requires exactly one first-frame and one last-frame binding."))
    if route == "fl2va" and data.get("endpoint_aspect_compatible") is not True:
        errors.append(issue("h3_endpoint_aspect_mismatch", "H3 FL2VA endpoint images must have compatible aspect ratios."))
    if route == "ref2va" and (not roles or any(role not in {"reference_image", "reference_video", "reference_audio"} for role in roles)):
        errors.append(issue("h3_ref_roles_invalid", "H3 Ref2VA requires one or more reference-role bindings only."))

    media = data.get("media_limits", {})
    if isinstance(media, dict):
        images = int(media.get("reference_image_count", 0) or 0)
        videos = int(media.get("reference_video_count", 0) or 0)
        audio = int(media.get("reference_audio_count", 0) or 0)
        video_seconds = float(media.get("reference_video_combined_seconds", 0) or 0)
        audio_seconds = float(media.get("reference_audio_combined_seconds", 0) or 0)
        request_mb = float(media.get("request_body_mb", 0) or 0)
        if images > 9 or videos > 3 or audio > 3 or images + videos + audio > 12 or video_seconds > 15 or audio_seconds > 15 or request_mb > 64:
            errors.append(issue("h3_material_hard_limit_exceeded", "MiniMax H3 reference count, duration, or request size exceeds a hard limit."))

    used_labels = sorted(set(match.group(0) for match in H3_LABEL_RE.finditer(prompt)))
    declared_labels = sorted(set(labels))
    if sorted(set(used_labels) - set(declared_labels)):
        errors.append(issue("h3_label_unmapped", "An H3 prompt label has no declared material binding.", values=sorted(set(used_labels) - set(declared_labels))))
    if sorted(set(declared_labels) - set(used_labels)):
        errors.append(issue("h3_binding_unused", "A declared H3 label is unused in the prompt.", values=sorted(set(declared_labels) - set(used_labels))))

    if route in {"t2va", "i2va", "fl2va", "l2va"}:
        required = ["integrated_multimodal_description:", "overall_soundscape:", "non_diegetic_music:"]
    else:
        required = ["subject_definitions:", "summary:", "retention_analysis:", "detailed_description:", "overall_soundscape:", "non_diegetic_music:"]
    positions = [prompt.find(field) for field in required]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append(issue("h3_schema_invalid", "H3 prompt fields are missing or out of order.", route=route))

    relationships = data.get("relationships", {})
    if isinstance(relationships, dict):
        for value in relationships.get("visible", []) or []:
            if value not in H3_VISIBLE_RELATIONSHIPS:
                errors.append(issue("h3_visible_relationship_invalid", "H3 visible relationship marker is invalid.", value=value))
        for value in relationships.get("audio", []) or []:
            if value not in H3_AUDIO_RELATIONSHIPS:
                errors.append(issue("h3_audio_relationship_invalid", "H3 audio relationship marker is invalid.", value=value))

    timeline_field = "detailed_description:" if route == "ref2va" else "integrated_multimodal_description:"
    timeline_start = prompt.find(timeline_field)
    timeline_end = prompt.find("overall_soundscape:", timeline_start + len(timeline_field)) if timeline_start >= 0 else -1
    timeline_text = prompt[timeline_start:timeline_end] if timeline_start >= 0 and timeline_end > timeline_start else ""
    shot_matches = list(re.finditer(r"\[Shot\s+(\d+)\](?:\s+At\s+(\d{2}):(\d{2})\.(\d{3}),)?", timeline_text))
    if shot_matches:
        shot_numbers = [int(match.group(1)) for match in shot_matches]
        if shot_numbers != list(range(1, len(shot_numbers) + 1)):
            errors.append(issue("h3_shot_sequence_invalid", "H3 shot numbers must be consecutive from Shot 1."))
        if shot_matches[0].group(2) is not None:
            errors.append(issue("h3_shot1_timestamped", "H3 Shot 1 must not have a timestamp."))
        duration_limit = 15.0
        if isinstance(parameters, dict) and isinstance(parameters.get("duration_seconds"), dict):
            duration_limit = float(parameters["duration_seconds"].get("resolved_value", 15) or 15)
        previous = 0.0
        for match in shot_matches[1:]:
            if match.group(2) is None:
                errors.append(issue("h3_cut_timestamp_missing", "Every H3 shot after Shot 1 requires a cut timestamp."))
                break
            value = int(match.group(2)) * 60 + int(match.group(3)) + int(match.group(4)) / 1000
            if value <= previous or value >= duration_limit:
                errors.append(issue("h3_cut_timestamp_invalid", "H3 cut timestamps must increase and remain inside the duration."))
                break
            previous = value

    music_requested = data.get("music_requested") is True
    music_match = re.search(r"non_diegetic_music:\s*([^\n]*)", prompt)
    if not music_requested and (music_match is None or music_match.group(1).strip() != "N/A"):
        errors.append(issue("h3_default_no_music_missing", "H3 prompt must serialize non_diegetic_music: N/A unless music was explicitly requested."))

    enhancement = data.get("prompt_enhancement", "framewright_compile")
    if enhancement not in {"framewright_compile", "context_ir_opt_in"}:
        errors.append(issue("h3_prompt_enhancement_invalid", "H3 prompt-enhancement mode is unsupported."))
    if enhancement == "context_ir_opt_in" and data.get("context_ir_authorized") is not True:
        errors.append(issue("h3_context_ir_unauthorized", "H3 Context-IR requires separate explicit authorization."))
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

    if ownership_validation_required(data):
        errors.extend(validate_serialization_ownership(data, prompt if isinstance(prompt, str) else ""))
    for field, code in (
        ("active_stages", "active_stage_count"),
        ("director_modes", "director_mode_count"),
        ("production_spines", "production_spine_count"),
        ("material_registries", "material_registry_count"),
    ):
        values = data.get(field)
        if values is not None and (not isinstance(values, list) or len(values) != 1):
            errors.append(issue(code, f"{field} must contain exactly one active owner."))
    director_modes = data.get("director_modes")
    if not isinstance(director_modes, list) or len(director_modes) != 1:
        errors.append(issue("director_mode_count", "Exactly one internal Director Mode must be resolved."))
    if data.get("conversation_mode_declared") is not True:
        errors.append(issue("director_mode_undeclared", "The resolved Director Mode must be declared to the user outside the clean Prompt."))

    seedance = data.get("seedance25")
    if seedance is not None:
        errors.extend(validate_seedance25(seedance, prompt if isinstance(prompt, str) else ""))

    minimax_h3 = data.get("minimax_h3")
    if minimax_h3 is not None:
        errors.extend(validate_minimax_h3(minimax_h3, prompt if isinstance(prompt, str) else ""))

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

    direction = data.get("directing_intention_contract")
    if direction is not None:
        if not isinstance(direction, dict) or not direction.get("statement") or not direction.get("source"):
            errors.append(issue("directing_intention_invalid", "Directing intention requires one functional statement and source."))
        else:
            lenses = direction.get("dramatic_lenses", []) or []
            if not isinstance(lenses, list) or any(value not in DRAMATIC_LENSES for value in lenses):
                errors.append(issue("dramatic_lens_invalid", "Dramatic lenses must be selective registered lenses."))
            if direction.get("non_narrative") is True and direction.get("psychology_forced") is True:
                errors.append(issue("non_narrative_psychology_forced", "Non-narrative work may not be forced into psychological story logic."))
            instruments = direction.get("instrument_coherence", {})
            if not isinstance(instruments, dict) or not instruments:
                errors.append(issue("instrument_coherence_missing", "Material directing intention requires an instrument-coherence review."))
            else:
                for instrument, record in instruments.items():
                    if not isinstance(record, dict) or record.get("relationship") not in INSTRUMENT_RELATIONSHIPS:
                        errors.append(issue("instrument_relationship_invalid", "Each active instrument must support, counterpoint, or remain neutral.", instrument=instrument))
                    elif record.get("relationship") == "counterpoint" and not record.get("function"):
                        errors.append(issue("instrument_counterpoint_unmotivated", "A counterpoint instrument requires a stated function.", instrument=instrument))

    for review in data.get("default_solution_review", []) or []:
        if not isinstance(review, dict) or any(
            not review.get(key)
            for key in ("tempting_default", "why_it_weakens_this_specific_scene", "chosen_replacement", "replacement_carrier")
        ):
            errors.append(issue("default_solution_review_incomplete", "A default review requires a scene-specific weakness and executable replacement."))
            continue
        if review.get("director_locked") is True and review.get("rejected") is True:
            errors.append(issue("auteur_locked_default_rejected", "A director-locked conventional choice may not be rejected merely as a default."))

    voice = data.get("directorial_voice_contract")
    if voice is not None:
        if not isinstance(voice, dict):
            errors.append(issue("directorial_voice_invalid", "Directorial voice must be a functional mapping."))
        else:
            dimensions = voice.get("functional_dimensions")
            if not isinstance(dimensions, dict) or not any(dimensions.values()):
                errors.append(issue("directorial_voice_empty", "Directorial voice requires at least one functional decision tendency."))
            if voice.get("preset_label_is_authority") is True:
                errors.append(issue("directorial_voice_preset_authority", "A descriptive preset label cannot own directorial voice."))
            if voice.get("named_living_director_imitation") is True:
                errors.append(issue("living_director_imitation_forbidden", "Directorial voice may not imitate a named living director."))

    expressive_arc = data.get("cross_generation_expressive_arc")
    if expressive_arc is not None:
        if not isinstance(expressive_arc, dict) or not isinstance(expressive_arc.get("generation_units"), list):
            errors.append(issue("expressive_arc_invalid", "Cross-generation expressive arc requires an ordered generation-unit list."))
        else:
            for deviation in expressive_arc.get("pattern_breaks", []) or []:
                if not isinstance(deviation, dict):
                    errors.append(issue("pattern_break_invalid", "Pattern break must be a mapping."))
                    continue
                if deviation.get("pattern_established") is not True or not deviation.get("function"):
                    errors.append(issue("pattern_break_unmotivated", "A pattern break requires an established pattern and material function."))
                if deviation.get("future_beat_leak") is True:
                    errors.append(issue("expressive_arc_future_leak", "Global expressive planning may not leak future beats into a local compile."))

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


def validate_generation_evidence(document: Any) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    if not isinstance(document, dict) or not isinstance(document.get("generation_evidence"), dict):
        return [issue("generation_evidence_invalid", "Generation evidence must contain a generation_evidence mapping.")]
    evidence = document["generation_evidence"]

    disposition = evidence.get("take_disposition")
    if disposition not in TAKE_DISPOSITIONS:
        errors.append(issue("take_disposition_invalid", "Generation evidence requires one supported take disposition.", value=disposition))
    root_cause = evidence.get("root_cause_classification")
    if root_cause not in ROOT_CAUSE_CLASSES:
        errors.append(issue("root_cause_classification_invalid", "Generation evidence requires one supported root-cause class.", value=root_cause))

    budget = evidence.get("attempt_budget")
    remaining: int | None = None
    if not isinstance(budget, dict):
        errors.append(issue("attempt_budget_invalid", "Generation evidence requires an explicit finite attempt budget."))
    else:
        values: dict[str, int] = {}
        for key in ("authorized_attempts", "attempts_used", "attempts_remaining"):
            value = budget.get(key)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                errors.append(issue("attempt_budget_unbounded", "Attempt counts must be finite non-negative integers.", key=key, value=value))
            else:
                values[key] = value
        if len(values) == 3 and values["attempts_remaining"] != values["authorized_attempts"] - values["attempts_used"]:
            errors.append(issue("attempt_budget_inconsistent", "Remaining attempts must equal authorized attempts minus used attempts."))
        if not isinstance(budget.get("budget_unit"), str) or not budget.get("budget_unit"):
            errors.append(issue("attempt_budget_unit_missing", "Attempt budget must name its counting unit."))
        if not isinstance(budget.get("cost_known"), bool):
            errors.append(issue("cost_known_not_explicit", "Attempt budget must explicitly state whether cost is known."))
        remaining = values.get("attempts_remaining")

    exit_condition = evidence.get("exit_condition")
    if not isinstance(exit_condition, str) or not exit_condition.strip():
        errors.append(issue("exit_condition_missing", "Every take disposition requires a non-empty exit condition."))
    next_authorized = evidence.get("next_attempt_authorized")
    if not isinstance(next_authorized, bool):
        errors.append(issue("next_attempt_authorization_invalid", "Generation evidence must explicitly state whether another attempt is authorized."))
    unaffected_preserved = evidence.get("unaffected_contracts_preserved")
    if not isinstance(unaffected_preserved, bool):
        errors.append(issue("unaffected_contracts_invalid", "Generation evidence must explicitly state whether unaffected contracts were preserved."))

    if disposition == "retry":
        if next_authorized is not True:
            errors.append(issue("retry_not_authorized", "Retry disposition requires explicit next-attempt authorization."))
        if remaining is None or remaining <= 0:
            errors.append(issue("retry_budget_exhausted", "Retry disposition requires positive remaining attempt budget."))
        changed_variable = evidence.get("changed_variable")
        if not isinstance(changed_variable, str) or not changed_variable.strip():
            errors.append(issue("retry_changed_variable_invalid", "Retry must name exactly one changed variable."))
        if unaffected_preserved is not True:
            errors.append(issue("retry_contract_preservation_missing", "Retry must preserve every unaffected contract."))

    if disposition == "rewrite_or_split" and evidence.get("boundary_change_requested") is True:
        if evidence.get("director_boundary_change_approved") is not True:
            errors.append(issue("unapproved_boundary_change", "A rewrite or split may not change generation-unit boundaries without director approval."))
    if disposition == "do_not_generate" and (not isinstance(exit_condition, str) or not exit_condition.strip()):
        errors.append(issue("do_not_generate_exit_missing", "Do-not-generate disposition must explain why the generation loop ends."))
    return errors


def validate_fixture(path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        return [issue("fixture_invalid", "Fixture must be a mapping.")], {}
    kind = data.get("kind")
    if kind == "compile_trace":
        errors = validate_compile_trace(data)
    elif kind == "prompt_ir":
        errors = validate_prompt_ir_data(data.get("document"))
    elif kind == "state":
        errors = validate_state_data(data.get("document"), check_locators=False)
    elif kind == "generation_evidence":
        errors = validate_generation_evidence(data.get("document"))
    elif kind == "prompt":
        errors = validate_prompt_text(
            str(data.get("prompt", "")),
            int(data.get("character_limit", 10_000)),
            data.get("native_bindings"),
        )
    else:
        errors = [issue("fixture_kind_invalid", "Fixture kind is not supported.", kind=kind)]
    return errors, data


def validate_core(
    core: Path,
    skill: Path,
    profiles: list[Path],
    manifest: Path,
    registry: Path = DEFAULT_REGISTRY,
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    try:
        core_meta, core_text = frontmatter(core)
        skill_meta, skill_text = frontmatter(skill)
        loaded_profiles = [frontmatter(profile) for profile in profiles]
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [issue("frontmatter_invalid", str(exc))]

    if core_meta.get("version") != "3.5.4-merge.6-local":
        errors.append(issue("candidate_version_mismatch", "Merge candidate must identify as 3.5.4-merge.6-local.", actual=core_meta.get("version")))
    if skill_meta.get("name") != "framewright-merge" or not skill_meta.get("description"):
        errors.append(issue("skill_frontmatter_invalid", "Skill frontmatter name or description is invalid."))
    for profile, (profile_meta, _) in zip(profiles, loaded_profiles):
        if not profile_meta.get("profile_version") or profile_meta.get("profile_role") != "subordinate_video_prompt_adapter":
            errors.append(issue("profile_frontmatter_invalid", "Runtime profile version or role is missing.", profile=str(profile)))

    documents = [("core", core_text), ("skill", skill_text)] + [
        (f"profile:{profile.name}", profile_text)
        for profile, (_, profile_text) in zip(profiles, loaded_profiles)
    ]
    for name, text in documents:
        if len(re.findall(r"^```", text, re.MULTILINE)) % 2:
            errors.append(issue("markdown_fence_unbalanced", "Markdown fences are unbalanced.", file=name))

    manifest_data = load_yaml(manifest)
    anchors = manifest_data.get("protected_anchors", []) if isinstance(manifest_data, dict) else []
    for anchor in anchors:
        if str(anchor) not in core_text and str(anchor) not in skill_text and not any(
            str(anchor) in profile_text for _, profile_text in loaded_profiles
        ):
            errors.append(issue("protected_anchor_missing", "A protected semantic anchor is missing.", anchor=anchor))
    registry_data, registry_errors = load_adapter_registry(registry)
    errors.extend(registry_errors)
    registered_profiles = {
        str(record.get("profile"))
        for record in registry_data.get("registered_targets", {}).values()
        if isinstance(record, dict) and record.get("profile")
    }
    supplied_profiles = {profile.name for profile in profiles}
    if supplied_profiles != registered_profiles:
        errors.append(
            issue(
                "registered_profile_set_mismatch",
                "Core validation must load exactly the adapter profiles declared by the registry.",
                registered=sorted(registered_profiles),
                supplied=sorted(supplied_profiles),
            )
        )
    return errors


def validate_video_prompt_path(
    path: Path,
    target_model: str,
    serialization_owner: str,
    adapter_id: str | None,
    profile_contract: str | None,
    compiler_sources: list[str] | None,
    registry: Path = DEFAULT_REGISTRY,
    character_limit: int = 10_000,
) -> list[dict[str, Any]]:
    registry_data, registry_errors = load_adapter_registry(registry)
    errors = list(registry_errors)
    if errors:
        return errors
    targets = registry_data.get("registered_targets", {})
    record = targets.get(target_model) if isinstance(targets, dict) else None
    sources = compiler_sources
    if sources is None:
        sources = list(registry_data.get("compiler_instruction_sources", []) or [])
        if isinstance(record, dict) and isinstance(record.get("profile"), str):
            sources.append(registered_profile_source(record["profile"]))
    data: dict[str, Any] = {
        "artifact_stage": "video_prompt",
        "target_model": target_model,
        "serialization_owner": serialization_owner,
        "adapter_id": adapter_id,
        "adapter_profile_contract": profile_contract,
        "compiler_instruction_sources": sources,
    }
    text = path.read_text(encoding="utf-8")
    errors.extend(validate_prompt_text(text, character_limit))
    errors.extend(validate_serialization_ownership(data, text, registry))
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

    video_prompt_parser = subparsers.add_parser("video-prompt")
    video_prompt_parser.add_argument("path", type=Path)
    video_prompt_parser.add_argument("--target-model", required=True)
    video_prompt_parser.add_argument("--serialization-owner", required=True)
    video_prompt_parser.add_argument("--adapter-id")
    video_prompt_parser.add_argument("--profile-contract")
    video_prompt_parser.add_argument("--compiler-source", action="append")
    video_prompt_parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    video_prompt_parser.add_argument("--character-limit", type=int, default=10_000)

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
    core_parser.add_argument("--profile", type=Path, required=True, action="append")
    core_parser.add_argument("--manifest", type=Path, required=True)
    core_parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)

    args = parser.parse_args()
    if args.command == "prompt":
        return emit(str(args.path), validate_prompt_text(args.path.read_text(encoding="utf-8"), args.character_limit), args.json)
    if args.command == "video-prompt":
        return emit(
            str(args.path),
            validate_video_prompt_path(
                args.path,
                args.target_model,
                args.serialization_owner,
                args.adapter_id,
                args.profile_contract,
                args.compiler_source,
                args.registry,
                args.character_limit,
            ),
            args.json,
        )
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
            validate_core(args.core, args.skill, args.profile, args.manifest, args.registry),
            args.json,
        )
    return 2


if __name__ == "__main__":
    sys.exit(main())
