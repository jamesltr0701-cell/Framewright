"""Mutation tests for source-to-shot evidence, including the real video-prompt boundary."""

import copy
import importlib.util
import shutil
from pathlib import Path
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("framewright_validator", ROOT / "skill/framewright/scripts/validate_framewright.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def trace(treatment="visible_transition"):
    blocks = {
        "s1": "She retains a smile. She recognizes the room; her mouth relaxes.",
        "s2": "Cut to her profile, already unsmiling. She stays seated.",
    }
    return {
        "core_version": VALIDATOR.frontmatter(ROOT / "skill/framewright/references/framewright.md")[0]["version"],
        "director_modes": ["auteur"],
        "conversation_mode_declared": True,
        "source_review_required": True,
        "prompt": "\n".join(blocks.values()),
        "prompt_shots": blocks,
        "semantic_trace": [{
            "intent_id": "realization",
            "source_locator": "director request / opening",
            "source_excerpt": "Show pleasure survive briefly as she recognizes reality. In the later shot she is already unsmiling.",
            "source_scope": ["s1", "s2"],
            "affected_shots_or_phases": ["s1", "s2"],
            "requirement_type": "performance_transition",
            "treatment": treatment,
            "rationale": "Show the established realization before the cut; the later shot starts after it.",
            "preservation_status": "preserved",
            "model_facing_carrier": [
                {"shot_id": "s1", "role": "baseline", "span": "She retains a smile."},
                {"shot_id": "s1", "role": "transition", "span": "She recognizes the room; her mouth relaxes."},
                {"shot_id": "s2", "role": "result", "span": "already unsmiling"},
            ],
        }],
    }


def camera_trace(treatment="continue"):
    result = trace()
    result["prompt_shots"] = {
        "s1": "Lin starts chest-up and lands shoulders-up.",
        "s2": "Mei holds a fixed waist-up frame.",
        "s3": "Back to Lin at the prior shoulders-up frame, then closer while keeping her chin and forehead.",
        "s4": "Return to Mei at the same fixed waist-up frame, without a push.",
    }
    result["prompt"] = "\n".join(result["prompt_shots"].values())
    entry = result["semantic_trace"][0]
    entry.update({
        "intent_id": "lin_approach",
        "source_excerpt": "Return to Lin from the previous landing and continue closer; Mei stays at the same waist-up distance.",
        "source_scope": ["s1", "s3"],
        "affected_shots_or_phases": ["s1", "s3"],
        "requirement_type": "camera_return",
        "treatment": treatment,
        "rationale": "Lin accumulates distance changes; Mei's separate framing holds.",
        "model_facing_carrier": [
            {"shot_id": "s1", "role": "previous_frame", "span": "lands shoulders-up"},
            {"shot_id": "s3", "role": "return_start", "span": "Back to Lin at the prior shoulders-up frame"},
            {"shot_id": "s3", "role": "return_end", "span": "then closer while keeping her chin and forehead"},
        ],
    })
    held = copy.deepcopy(entry)
    held.update({
        "intent_id": "mei_hold", "treatment": "hold",
        "source_scope": ["s2", "s4"], "affected_shots_or_phases": ["s2", "s4"],
        "model_facing_carrier": [
            {"shot_id": "s2", "role": "previous_frame", "span": "fixed waist-up frame"},
            {"shot_id": "s4", "role": "return_start", "span": "same fixed waist-up frame, without a push"},
        ],
    })
    result["semantic_trace"].append(held)
    return result


class SourceReviewTests(unittest.TestCase):
    def codes(self, data):
        return {error["code"] for error in VALIDATOR.validate_compile_trace(data)}

    def voice_trace(self, placement="voiceover", sync="forbidden"):
        block = 'Mara stays visible with closed lips. Her voiceover says, without lip sync: "I remember."'
        return {
            "core_version": "4.2.1", "director_modes": ["auteur"], "conversation_mode_declared": True,
            "prompt": block, "prompt_shots": {"s1": block},
            "vocal_events": [{
                "event_id": "memory", "speaker": "Mara", "beat": "s1", "allowed_count": 1,
                "exact_text": "I remember.", "language": "en", "prompt_evidence": block,
                "presentation": {"placement": placement, "lip_sync": sync, "shot_id": "s1", "span": block},
            }],
        }

    def test_voiceover_preserves_visible_silent_face(self):
        self.assertEqual(self.codes(self.voice_trace()), set())
        self.assertIn("vocal_presentation_conflict", self.codes(self.voice_trace(sync="required")))

    def test_voice_evidence_must_be_in_its_own_shot(self):
        data = self.voice_trace()
        data["prompt_shots"]["s2"] = "Another person opens the door."
        data["prompt"] += "\n" + data["prompt_shots"]["s2"]
        data["vocal_events"][0]["presentation"]["shot_id"] = "s2"
        self.assertIn("vocal_presentation_evidence_missing", self.codes(data))

    def test_offscreen_and_onscreen_sync_rules(self):
        for placement, sync, block in (
            ("off_screen", "not_visible", 'Mara replies off-screen: "I remember." Keep the listener in frame.'),
            ("on_screen", "required", 'Mara says "I remember." on-screen, with synchronized lips.'),
        ):
            with self.subTest(placement=placement):
                data = self.voice_trace(placement, sync)
                data["prompt"] = data["prompt_shots"]["s1"] = block
                data["vocal_events"][0]["prompt_evidence"] = block
                data["vocal_events"][0]["presentation"]["span"] = block
                self.assertEqual(self.codes(data), set())
        self.assertIn("vocal_presentation_conflict", self.codes(self.voice_trace("off_screen", "required")))

    def test_repeated_voice_needs_each_occurrence_located(self):
        data = self.voice_trace()
        second = 'Mara now says "I remember." in-scene with synchronized lips.'
        data["prompt_shots"]["s2"] = second
        data["prompt"] += "\n" + second
        event = data["vocal_events"][0]
        event["allowed_count"] = 2
        self.assertIn("vocal_presentation_count_mismatch", self.codes(data))
        event["presentation"] = [event["presentation"], {"placement": "on_screen", "lip_sync": "required", "shot_id": "s2", "span": second}]
        self.assertEqual(self.codes(data), set())

    def test_standalone_install_resolves_registered_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / "installed-skills/framewright"
            shutil.copytree(ROOT / "skill/framewright", package, ignore=shutil.ignore_patterns("__pycache__"))
            registry = package / "references/runtime_profiles/adapter_registry.yaml"
            document = yaml.safe_load(registry.read_text())
            self.assertEqual(VALIDATOR.validate_registry_data(document, registry), [])
            document["compiler_instruction_sources"].append("skill/framewright/../../outside.md")
            errors = VALIDATOR.validate_registry_data(document, registry)
            self.assertIn("compiler_source_registry_path_invalid", {e["code"] for e in errors})

    def test_visible_process_and_asymmetric_camera_pass(self):
        self.assertEqual(self.codes(trace()), set())
        self.assertEqual(self.codes(camera_trace()), set())

    def test_ellipsis_and_withheld_response_do_not_require_transition(self):
        for treatment in ("ellipsis", "withheld"):
            with self.subTest(treatment=treatment):
                data = trace(treatment)
                data["prompt_shots"]["s1"] = "She retains a smile."
                data["prompt"] = "\n".join(data["prompt_shots"].values())
                entry = data["semantic_trace"][0]
                entry["source_excerpt"] = "Omit the change across the cut; show the later neutral state only."
                entry["rationale"] = "Preserve the directed omission or withheld response."
                entry["model_facing_carrier"].pop(1)
                self.assertEqual(self.codes(data), set())

    def test_missing_transition_detected_without_performance_beat(self):
        data = trace()
        data["semantic_trace"][0]["model_facing_carrier"].pop(1)
        self.assertNotIn("performance_beats", data)
        self.assertIn("source_review_relation_missing", self.codes(data))

    def test_compression_cannot_delete_transition_or_camera_landing(self):
        for data, shot_id, removed in (
            (trace(), "s1", " She recognizes the room; her mouth relaxes."),
            (camera_trace(), "s3", ", then closer while keeping her chin and forehead"),
        ):
            with self.subTest(removed=removed):
                data["prompt_shots"][shot_id] = data["prompt_shots"][shot_id].replace(removed, "")
                data["prompt"] = "\n".join(data["prompt_shots"].values())
                self.assertIn("source_review_span_missing", self.codes(data))

    def test_evidence_elsewhere_in_prompt_is_not_current_shot_evidence(self):
        data = camera_trace()
        data["semantic_trace"][0]["model_facing_carrier"][1]["span"] = "fixed waist-up frame"
        self.assertIn("source_review_span_missing", self.codes(data))

    def test_later_constraint_cannot_expand_to_earlier_shot(self):
        data = trace()
        entry = data["semantic_trace"][0]
        entry.update({
            "source_scope": ["s2"], "affected_shots_or_phases": ["s2"],
            "source_excerpt": "In the side view she is already no longer smiling.",
            "requirement_type": "scoped_constraint", "treatment": "preserve",
            "model_facing_carrier": [{"shot_id": "s2", "role": "constraint", "span": "already unsmiling"}],
        })
        self.assertEqual(self.codes(data), set())
        entry["affected_shots_or_phases"].append("s1")
        self.assertIn("source_review_scope_invalid", self.codes(data))

    def test_reference_state_preserves_directed_start(self):
        data = trace()
        data["prompt_shots"] = {"s1": "She starts seated, rises, then leans as in the end-pose reference."}
        data["prompt"] = data["prompt_shots"]["s1"]
        data["semantic_trace"][0].update({
            "source_scope": ["s1"], "affected_shots_or_phases": ["s1"],
            "source_excerpt": "Start seated, then stand; image supplies the final lean only.",
            "requirement_type": "reference_state", "treatment": "preserve",
            "model_facing_carrier": [{"shot_id": "s1", "role": "constraint", "span": data["prompt"]}],
        })
        self.assertEqual(self.codes(data), set())
        data["prompt_shots"]["s1"] = "She starts leaning as in the reference."
        data["prompt"] = data["prompt_shots"]["s1"]
        self.assertIn("source_review_span_missing", self.codes(data))

    def test_one_constraint_can_have_evidence_in_multiple_affected_shots(self):
        data = trace()
        entry = data["semantic_trace"][0]
        entry.update({
            "requirement_type": "scoped_constraint", "treatment": "preserve",
            "source_excerpt": "Show these two distinct states in their respective shots.",
            "model_facing_carrier": [
                {"shot_id": "s1", "role": "constraint", "span": "She retains a smile."},
                {"shot_id": "s2", "role": "constraint", "span": "already unsmiling"},
            ],
        })
        self.assertEqual(self.codes(data), set())
        entry["model_facing_carrier"].pop()
        self.assertIn("source_review_affected_uncovered", self.codes(data))

    def test_collapsed_or_reordered_relations_fail(self):
        for mutation in ("collapse", "reorder"):
            with self.subTest(mutation=mutation):
                data = trace()
                carriers = data["semantic_trace"][0]["model_facing_carrier"]
                if mutation == "collapse":
                    carriers[1]["span"] = carriers[0]["span"]
                else:
                    carriers[0]["span"], carriers[1]["span"] = carriers[1]["span"], carriers[0]["span"]
                self.assertIn("source_review_order_changed", self.codes(data))

    def test_malformed_or_unresolved_reviews_fail_cleanly(self):
        mutations = {
            "source_review_missing": lambda d: d.update(semantic_trace=[]),
            "source_review_provenance_missing": lambda d: d["semantic_trace"][0].pop("source_excerpt"),
            "source_review_unresolved": lambda d: d["semantic_trace"][0].update(preservation_status="unresolved"),
            "source_review_scope_invalid": lambda d: d["semantic_trace"][0].update(source_scope=[{}]),
            "source_review_treatment_invalid": lambda d: d["semantic_trace"][0].update(treatment={}),
            "source_review_shot_invalid": lambda d: d["prompt_shots"].update(s1="not in the prompt"),
        }
        for expected, mutate in mutations.items():
            with self.subTest(expected=expected):
                data = trace()
                mutate(data)
                self.assertIn(expected, self.codes(data))

    def test_overlapping_or_duplicate_shot_blocks_fail(self):
        for block in ("She retains a smile.", trace()["prompt_shots"]["s1"]):
            data = trace()
            data["prompt_shots"]["extra"] = block
            self.assertIn("source_review_shot_overlap", self.codes(data))

    def test_legacy_trace_stays_compatible(self):
        data = trace()
        data.pop("source_review_required")
        data["semantic_trace"] = [{"intent_id": "legacy", "model_facing_carrier": "existing description"}]
        self.assertEqual(self.codes(data), set())
        data["source_review_required"] = True
        self.assertIn("source_review_missing", self.codes(data))

    def test_video_prompt_flag_requires_trace_and_checks_exact_saved_text(self):
        with tempfile.TemporaryDirectory() as directory:
            prompt_path, trace_path = Path(directory) / "prompt.txt", Path(directory) / "trace.yaml"
            data = trace()
            prompt_path.write_text(data["prompt"], encoding="utf-8")
            kwargs = dict(path=prompt_path, target_model="seedance_2_5", serialization_owner="framewright_adapter_seedance_2_5", adapter_id="seedance_2_5", profile_contract="seedance_2_5", compiler_sources=None, source_review=True)
            codes = lambda: {e["code"] for e in VALIDATOR.validate_video_prompt_path(**kwargs)}
            self.assertIn("source_review_missing", codes())
            kwargs["trace_path"] = trace_path
            data.pop("source_review_required")  # The command flag must enforce it itself.
            trace_path.write_text(yaml.safe_dump(data), encoding="utf-8")
            self.assertEqual(codes(), set())
            data["semantic_trace"] = []
            trace_path.write_text(yaml.safe_dump(data), encoding="utf-8")
            self.assertIn("source_review_missing", codes())
            prompt_path.write_text("A different prompt.", encoding="utf-8")
            self.assertIn("video_trace_mismatch", codes())


if __name__ == "__main__":
    unittest.main()
