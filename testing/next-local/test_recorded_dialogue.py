"""Recorded dialogue must stay attached to its original voices and shot timing."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from test_source_review import ROOT, VALIDATOR


SCRIPT_LINE = "我建议我们从里面开门。"
ROLE = "@Audio 1: 所有对白只按这段录音表演，保留原话、语气、节奏、停顿和各角色音色。"
GESTURE = "小林把食指抬到耳边。"


def sync_prompt(trace, role=ROLE, ambience="室内底噪和同步动作声，无音乐。"):
    trace["prompt"] = "\n".join(["MATERIAL ROLES", role, *trace["prompt_shots"].values(), ambience])


def shot_part(shot_id, placement="on_screen", lip_sync="required"):
    return {"shot_id": shot_id, "placement": placement, "lip_sync": lip_sync}


def turn(number, speaker, *parts):
    return {
        "event_id": f"voice_{number}", "source_turn": number, "speaker": speaker,
        "allowed_count": 1, "recording_parts": list(parts),
    }


def recorded_trace():
    data = {
        "core_version": VALIDATOR.frontmatter(ROOT / "skill/framewright/references/framewright.md")[0]["version"],
        "director_modes": ["auteur"],
        "conversation_mode_declared": True,
        "target_model": "seedance_2_5",
        "serialization_owner": "framewright_adapter_seedance_2_5",
        "adapter_id": "seedance_2_5",
        "compiler_instruction_sources": [
            "skill/framewright/SKILL.md",
            "skill/framewright/references/framewright.md",
            "skill/framewright/references/runtime_profiles/seedance_2_5.md",
            "skill/framewright/references/craft/camera-motion.md",
        ],
        "native_bindings": ["@Audio 1"],
        "seedance25": {
            "route": "omni_reference",
            "parameter_contract": {
                "duration": {"provenance": "user_settable", "resolved_value": 12},
                "aspect_ratio": {"provenance": "user_settable", "resolved_value": "16:9"},
            },
            "materials": {"audio_count": 1, "audio_combined_seconds": 10},
            "active_subset_mapped": True,
        },
        "recorded_dialogue": {
            "material_key": "approved_voice_excerpt", "native_ref": "@Audio 1",
            "speaker_order": ["小林", "小孟", "小林"], "prompt_language": "zh",
        },
        "excluded_script_lines": [SCRIPT_LINE],
        "prompt_shots": {
            "s1": f"镜头一。中景。开口前的短停顿里，{GESTURE}\n"
                  "小林在画内开始录音第1轮对白，口型同步。\n开口后把手放回桌面。",
            "s2": "镜头二。小林留在画内，闭嘴听。\n小孟在画外开始录音第2轮对白。",
            "s3": "镜头三。小孟在停顿后重新起音时切到她的正面。\n小孟在画内继续录音第2轮对白，口型同步。",
            "s4": "镜头四。切回小林。\n小林在画内开始录音第3轮对白，口型同步。",
        },
        "vocal_events": [
            turn(1, "小林", shot_part("s1")),
            turn(2, "小孟", shot_part("s2", "off_screen", "not_visible"), shot_part("s3")),
            turn(3, "小林", shot_part("s4")),
        ],
        "silent_reaction_beats": [{"beat_id": "s2", "speaker": "小林", "mode": "strict_no_vocal"}],
        "performance_beats": [{
            "beat_id": "idea", "shot_scale": "medium", "carrier_legible": True,
            "physical_carriers": ["Lift a finger to ear level and return the hand to the desk"],
            "release_or_aftermath": "The hand is back on the desk.",
            "prompt_evidence": {
                "trigger": "开口前的短停顿里",
                "response": GESTURE,
                "aftermath": "开口后把手放回桌面。",
            },
        }],
    }
    sync_prompt(data)
    return data


class RecordedDialogueTests(unittest.TestCase):
    def codes(self, data):
        return {error["code"] for error in VALIDATOR.validate_compile_trace(data)}

    def test_two_distinct_characters_and_a_turn_continuing_through_a_cut(self):
        self.assertEqual(self.codes(recorded_trace()), set())

    def test_one_recorded_speaker_with_english_prompt(self):
        data = recorded_trace()
        data["recorded_dialogue"].update(speaker_order=["Lin"], prompt_language="en")
        data["vocal_events"] = [turn(1, "Lin", shot_part("s1", lip_sync="not_visible"))]
        data["performance_beats"] = []
        data["silent_reaction_beats"] = []
        data["prompt_shots"] = {"s1": "Shot one. Lin looks at the door in profile.\n"
                                       "Lin starts recorded turn 1 on screen with their mouth out of view."}
        sync_prompt(
            data,
            "@Audio 1: Use only this recording for dialogue. Match its words, delivery, pacing, pauses, and each character's voice.",
            "Quiet room tone and synchronized SFX. No music.",
        )
        self.assertEqual(self.codes(data), set())

    def test_audio_role_cannot_revert_to_style_only(self):
        data = recorded_trace()
        sync_prompt(data, "@Audio 1: 只参考说话节奏和语气。")
        self.assertIn("recorded_dialogue_authority_missing", self.codes(data))
        sync_prompt(data, f"{ROLE}\n@Audio 1：实际台词以剧本为准。")
        self.assertIn("recorded_dialogue_authority_missing", self.codes(data))

    def test_wrong_native_mention_or_unsupported_route(self):
        data = recorded_trace()
        data["recorded_dialogue"]["native_ref"] = "@Audio 2"
        self.assertIn("recorded_dialogue_binding_missing", self.codes(data))
        data["recorded_dialogue"]["native_ref"] = "@Audio 1"
        data["seedance25"]["route"] = "long_video"
        self.assertIn("recorded_dialogue_route_unsupported", self.codes(data))

    def test_known_script_and_seedance_spoken_text_are_rejected(self):
        for leaked_line in (f'小林说：“{SCRIPT_LINE}”', "{先去开门。}"):
            with self.subTest(leaked_line=leaked_line):
                data = recorded_trace()
                data["prompt_shots"]["s1"] += f"\n{leaked_line}"
                sync_prompt(data)
                self.assertIn("recorded_dialogue_written_words", self.codes(data))

    def test_a_cut_does_not_restart_the_turn(self):
        data = recorded_trace()
        data["prompt_shots"]["s3"] = data["prompt_shots"]["s3"].replace("继续", "开始")
        sync_prompt(data)
        self.assertIn("recorded_dialogue_shot_evidence", self.codes(data))

    def test_same_turn_can_continue_across_another_on_screen_cut(self):
        data = recorded_trace()
        last = data["prompt_shots"].pop("s4")
        data["prompt_shots"]["s3-detail"] = "镜头四。仍在同一句内切近。\n小孟在画内继续录音第2轮对白，口型同步。"
        data["prompt_shots"]["s4"] = last.replace("镜头四", "镜头五")
        data["vocal_events"][1]["recording_parts"].append(shot_part("s3-detail"))
        sync_prompt(data)
        self.assertEqual(self.codes(data), set())

    def test_pause_is_not_new_turn_and_cue_is_not_new_voice(self):
        data = recorded_trace()
        data["vocal_events"].append({
            "event_id": "extra_filler", "speaker": "小孟", "event_type": "authorized_short_response",
            "authorization_source": "user_preference", "exact_text": "诶", "language": "zh",
            "beat": "s3", "allowed_count": 1,
        })
        self.assertIn("recorded_dialogue_turn_order", self.codes(data))
        data = recorded_trace()
        data["vocal_events"][1]["speaker"] = "小林"
        self.assertIn("recorded_dialogue_turn_order", self.codes(data))

    def test_silence_applies_to_the_correct_character_and_part(self):
        data = recorded_trace()
        data["vocal_events"][1]["recording_parts"][1]["beat"] = "after_cut"
        data["silent_reaction_beats"].append({"beat_id": "after_cut", "speaker": "小孟", "mode": "no_dialogue"})
        self.assertIn("silence_ownership_violation", self.codes(data))
        data["silent_reaction_beats"][-1] = {"beat_id": "s3", "mode": "strict_no_vocal"}
        self.assertIn("silence_ownership_violation", self.codes(data))

    def test_body_cue_survives_into_final_text(self):
        data = recorded_trace()
        data["prompt_shots"]["s1"] = data["prompt_shots"]["s1"].replace(GESTURE, "小林露出恍然大悟的表情。")
        sync_prompt(data)
        self.assertIn("performance_prompt_span_missing", self.codes(data))

    def test_audio_attachment_alone_does_not_activate_recorded_dialogue(self):
        data = recorded_trace()
        del data["recorded_dialogue"]
        line = f"小林在画内说：{{{SCRIPT_LINE}}}，口型同步。"
        data["prompt_shots"] = {"s1": line}
        data["vocal_events"] = [{
            "event_id": "ordinary_ai_voice", "speaker": "小林", "beat": "s1",
            "allowed_count": 1, "exact_text": SCRIPT_LINE, "language": "zh", "prompt_evidence": line,
        }]
        data["performance_beats"] = []
        data["silent_reaction_beats"] = []
        sync_prompt(data, "@Audio 1: 只参考音色。")
        self.assertEqual(self.codes(data), set())

    def test_prompt_ir_validates_recorded_events_before_serialization(self):
        data = recorded_trace()
        fixture = ROOT / "testing/next-local/fixtures/prompt_ir_v42_optional_pass.yaml"
        document = yaml.safe_load(fixture.read_text())["document"]
        ir = document["video_prompt_ir"]
        ir.update(target_model="seedance_2_5", prompt_scope_shots=list(data["prompt_shots"]))
        ir["sound_contract"] = {
            "recorded_dialogue": {"material_key": "approved_voice_excerpt", "speaker_order": ["小林", "小孟", "小林"]},
            "vocal_events": data["vocal_events"],
        }
        self.assertIn(
            "recorded_dialogue_reference_inactive",
            {error["code"] for error in VALIDATOR.validate_prompt_ir_data(document)},
        )
        ir["active_references"] = [{"material_key": "approved_voice_excerpt", "media_type": "audio"}]
        self.assertEqual(VALIDATOR.validate_prompt_ir_data(document), [])
        ir["sound_contract"]["vocal_events"][0]["exact_text"] = SCRIPT_LINE
        self.assertIn(
            "recorded_dialogue_competing_event",
            {error["code"] for error in VALIDATOR.validate_prompt_ir_data(document)},
        )

    def test_video_prompt_cli_requires_matching_recorded_dialogue_trace(self):
        with tempfile.TemporaryDirectory() as directory:
            data = recorded_trace()
            prompt = Path(directory) / "prompt.txt"
            trace = Path(directory) / "trace.yaml"
            prompt.write_text(data["prompt"])
            trace.write_text(yaml.safe_dump(data, allow_unicode=True))
            command = [
                sys.executable, str(ROOT / "skill/framewright/scripts/validate_framewright.py"),
                "video-prompt", str(prompt), "--recorded-dialogue", "--target-model", "seedance_2_5",
                "--serialization-owner", "framewright_adapter_seedance_2_5",
                "--adapter-id", "seedance_2_5", "--profile-contract", "seedance_2_5",
            ]
            result = subprocess.run(command + ["--trace", str(trace)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("recorded_dialogue_missing", result.stdout + result.stderr)
            prompt.write_text(data["prompt"] + "\nChange")
            result = subprocess.run(command + ["--trace", str(trace)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("video_trace_mismatch", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
