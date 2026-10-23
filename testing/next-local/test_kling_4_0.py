"""Kling entry, shared media quota, ownership and real final-file checks."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("fw_validator", ROOT / "skill/framewright/scripts/validate_framewright.py")
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def runtime(**changes):
    return dict(explicit_target_selection=True, entry="omni_reference", task="generate",
                duration_seconds=12, resolution="1080p", aspect_ratio="9:16", input_bindings=[], **changes)


def binding(kind, index=1, role="reference", **extra):
    label = {"image": "Image", "video": "Video", "image_element": "Element", "video_element": "Element", "voice_profile": "Voice"}[kind]
    return dict(material_key=f"{kind}_{index}", kind=kind, role=role,
                native_mention=f"@{label}{index}", allowed_authority=["approved role"],
                denied_authority=["unapproved scene changes"], **extra)


def trace(prompt, contract):
    return dict(core_version=V.frontmatter(ROOT / "skill/framewright/references/framewright.md")[0]["version"],
                director_modes=["auteur"], conversation_mode_declared=True,
                artifact_stage="video_prompt", target_model="kling_4_0",
                serialization_owner="framewright_adapter_kling_4_0", adapter_id="kling_4_0",
                adapter_profile_contract="kling_4_0",
                compiler_instruction_sources=["skill/framewright/SKILL.md", "skill/framewright/references/framewright.md",
                    "skill/framewright/references/runtime_profiles/kling_4_0.md"],
                prompt=prompt, kling40=contract)


class KlingTests(unittest.TestCase):
    def codes(self, data, prompt=None):
        if prompt is None:
            prompt = " ".join(b["native_mention"] for b in data.get("input_bindings", []) if isinstance(b, dict)) + " A hand releases one key onto a table."
        return {e["code"] for e in V.validate_kling40(data, prompt)}

    def test_text_only_and_duration_edges(self):
        for n in [3, 12, 30]:
            d = runtime(); d["duration_seconds"] = n
            self.assertEqual(self.codes(d), set())
        for n in [2, 31, 3.5, True, "12"]:
            d = runtime(); d["duration_seconds"] = n
            self.assertIn("kling_duration_invalid", self.codes(d))

    def test_shared_video_count_includes_elements_and_edit_base(self):
        d = runtime(); d["task"] = "edit"
        d["input_bindings"] = [binding("video", i, "edit_base" if i == 1 else "reference", duration_seconds=3) for i in range(1, 5)]
        d["input_bindings"] += [binding("video_element", i, duration_seconds=3) for i in [1, 2]]
        self.assertIn("kling_video_pool_limit", self.codes(d))
        d["input_bindings"].pop()
        self.assertEqual(self.codes(d), set())

    def test_shared_video_duration(self):
        d = runtime(); d["input_bindings"] = [binding("video", duration_seconds=26), binding("video_element", duration_seconds=4)]
        self.assertEqual(self.codes(d), set())
        d["input_bindings"][0]["duration_seconds"] = 27
        self.assertIn("kling_video_pool_limit", self.codes(d))

    def test_individual_and_combined_limits(self):
        groups = [([binding("image", i) for i in range(1, 12)]),
                  ([binding("voice_profile", i, "voice") for i in range(1, 5)]),
                  ([binding("image_element", i) for i in range(1, 9)]),
                  ([binding("image", i) for i in range(1, 11)] + [binding("voice_profile", i, "voice") for i in range(1, 4)] + [binding("image_element", i) for i in range(1, 4)]),
                  ([binding("video_element", i, duration_seconds=3) for i in range(1, 5)])]
        for inputs in groups:
            with self.subTest(inputs=len(inputs)):
                d = runtime(); d["input_bindings"] = inputs
                self.assertIn("kling_asset_limit", self.codes(d))

    def test_keyframes_are_image_only_and_inherit_ratio(self):
        d = runtime(); d.update(entry="keyframes", aspect_ratio="inherited",
            input_bindings=[binding("image", 1, "first_frame", time_seconds=0), binding("image", 2, "last_frame", time_seconds=12)])
        self.assertEqual(self.codes(d), set())
        d["input_bindings"].append(binding("voice_profile", role="voice"))
        self.assertIn("kling_entry_role_conflict", self.codes(d))
        d["input_bindings"].pop(); d["aspect_ratio"] = "9:16"
        self.assertIn("kling_aspect_invalid", self.codes(d))

    def test_keyframe_times(self):
        d = runtime(); d.update(entry="keyframes", aspect_ratio="inherited",
            input_bindings=[binding("image", 1, "first_frame", time_seconds=0), binding("image", 2, "middle_frame", time_seconds=0)])
        self.assertIn("kling_keyframe_time_conflict", self.codes(d))
        self.assertIn("kling_keyframe_role_time", self.codes(d))
        d["input_bindings"][1]["time_seconds"] = 13
        self.assertIn("kling_keyframe_time", self.codes(d))

    def test_omni_cannot_claim_dedicated_slots(self):
        d = runtime(); d["input_bindings"] = [binding("image", role="first_frame", time_seconds=0)]
        self.assertIn("kling_entry_role_conflict", self.codes(d))

    def test_edit_primary(self):
        d = runtime(); d["task"] = "edit"
        self.assertIn("kling_edit_base_count", self.codes(d))
        d["input_bindings"] = [binding("video", role="edit_base", duration_seconds=12)]
        self.assertEqual(self.codes(d), set())
        d["task"] = "generate"
        self.assertIn("kling_edit_base_count", self.codes(d))

    def test_measured_properties_and_malformed_values(self):
        for prop, value, code in [("duration_seconds", 31, "media_duration"), ("duration_seconds", "unknown", "media_duration"),
                                  ("size_mb", 301, "media_size"), ("aspect_ratio", 0.3, "media_aspect"), ("size_mb", float("nan"), "media_size")]:
            d = runtime(); d["input_bindings"] = [binding("video", **{prop: value})]
            self.assertIn("kling_" + code, self.codes(d))
        d = runtime(); d["input_bindings"] = [binding("video_element", duration_seconds=9)]
        self.assertIn("kling_media_duration", self.codes(d))

    def test_voice_is_profile_not_arbitrary_audio(self):
        d = runtime(); d["input_bindings"] = [binding("voice_profile", role="voice", duration_seconds=5, size_mb=50)]
        self.assertEqual(self.codes(d), set())
        d["input_bindings"][0]["kind"] = "audio"
        self.assertIn("kling_input_kind_invalid", self.codes(d))

    def test_malformed_enums_return_errors(self):
        for field in ["entry", "task", "resolution", "aspect_ratio"]:
            d = runtime(); d[field] = []
            self.assertTrue(self.codes(d))
        for field in ["kind", "role"]:
            d = runtime(); d["input_bindings"] = [binding("image")]
            d["input_bindings"][0][field] = []
            self.assertTrue(self.codes(d))

    def test_mentions_match_uploads(self):
        d = runtime(); d["input_bindings"] = [binding("image")]
        self.assertIn("kling_mention_unmapped", self.codes(d, "@Image1 and @Video2"))
        self.assertIn("kling_binding_unused", self.codes(d, "A door opens."))
        d["input_bindings"].append(copy.deepcopy(d["input_bindings"][0]))
        self.assertIn("kling_mention_duplicate", self.codes(d))

    def test_token_count_is_optional_and_not_character_count(self):
        d = runtime(); d["prompt_token_count"] = 8001
        self.assertIn("kling_token_limit", self.codes(d))
        d.pop("prompt_token_count")
        self.assertEqual(self.codes(d, "a " * 6000), set())

    def validate_file(self, prompt, data=None, **changes):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "prompt.txt"; p.write_text(prompt)
            t = None
            if data is not None:
                t = Path(tmp) / "trace.yaml"; t.write_text(yaml.safe_dump(data))
            kwargs = dict(path=p, target_model="kling_4_0", serialization_owner="framewright_adapter_kling_4_0",
                          adapter_id="kling_4_0", profile_contract="kling_4_0", compiler_sources=None, trace_path=t)
            kwargs.update(changes)
            return {e["code"] for e in V.validate_video_prompt_path(**kwargs)}

    def test_final_file_and_runtime_cannot_be_skipped(self):
        p = "A hand releases one key onto a table. Quiet room tone; no speech or music."
        self.assertIn("kling_contract_missing", self.validate_file(p))
        self.assertEqual(self.validate_file(p, trace(p, runtime())), set())
        t = trace(p, runtime()); t.pop("kling40")
        self.assertIn("kling_contract_missing", self.validate_file(p, t))

    def test_final_file_rejects_foreign_and_stale_trace(self):
        p = "One key rests on a table."
        t = trace(p, runtime()); t["adapter_id"] = "seedance_2_5"
        self.assertIn("kling_trace_owner_mismatch", self.validate_file(p, t))
        t = trace(p, runtime()); t["minimax_h3"] = {}
        self.assertIn("adapter_profile_contract_mismatch", self.validate_file(p, t))
        self.assertIn("video_trace_mismatch", self.validate_file(p, trace(p + " Changed.", runtime())))

    def test_final_file_does_not_impose_unrelated_character_limit(self):
        p = "a " * 6000
        self.assertEqual(self.validate_file(p, trace(p, runtime())), set())
        self.assertIn("character_limit_exceeded", self.validate_file(p, trace(p, runtime()), character_limit=10000))

    def test_owner_and_native_binding_boundary(self):
        p = "A table."
        self.assertIn("target_owner_mismatch", self.validate_file(p, trace(p, runtime()), serialization_owner="framewright_adapter_seedance_2_5"))
        p = "REFS\n{{HANDLE}}\nA table."
        self.assertIn("generic_handle_forbidden", self.validate_file(p, trace(p, runtime())))


if __name__ == "__main__":
    unittest.main()
