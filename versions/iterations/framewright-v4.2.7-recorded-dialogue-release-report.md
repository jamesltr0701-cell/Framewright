# Framewright v4.2.7 — recorded dialogue and body performance

When the director selects a recording to drive dialogue, the recording owns the words, delivery, pauses, timing, and character voices. Shot planning uses the approved recording without letting the written script compete for control of speech. For a voice that begins off-screen and continues after a cut, the prompt names the same turn and assigns lip sync where the mouth is visible. Each generation uses the relevant excerpt of the approved recording. Text-driven dialogue uses the approved script.

During initial shot planning, choose a body action or held posture that fits the character's response. Relate the action to an audible or visible cue. Check that the shot can show it. A held posture can carry a beat in a restrained scene.

The recorded-dialogue workflow is qualified for one in-scene excerpt per generation on Seedance 2.5 Omni Reference, with Chinese or English prompt prose. The Run Card identifies the approved clip and its native audio reference. Productions requiring the exact recorded performance in the final mix can retain the original as the post-production audio master.

## Validation

The package and 140 existing regression fixtures passed, along with 39 existing focused tests, 13 new focused tests, and three command-line smoke checks. The new tests cover audio binding, script leakage, speaker order, a turn continuing across cuts, scoped silence, and whether a planned gesture survives into final prompt text.

Actual voice fidelity, lip sync, and body performance require reviewing generated footage. This release was validated at the prompt level. The [v4.2.6 snapshot](../releases/framewright-v4.2.6.md) remains available for comparison.
