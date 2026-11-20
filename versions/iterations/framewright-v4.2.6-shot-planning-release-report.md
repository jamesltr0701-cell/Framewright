# Framewright v4.2.6 — shot planning, timing, and prompt language

The first textual shot proposal now uses Framewright's scene and shot rules. Plan a continuous scene as one unit when the action fits the route and its required references can coexist. When separate units are needed, review the cut between the footage intended for the edit. A removable opening anchor still grounds the generation and is accounted for separately.

- Estimate unit length from playable actions, dialogue, reactions, and cut room. Count concurrent beats once. Keep planning estimates out of final prompt timestamps unless the director requests numeric timing or the approved synchronization needs it.
- When an entrance or exit is required for the edit, specify the frame edge, the completed action, and enough material to cut. Maintain the state of causally relevant people when the sequence leaves them offscreen.
- Default prompt prose to Chinese. Preserve explicit language choices, native adapter syntax, and exact spoken and visible text. Use verified limits for the actual surface and report unknown limits separately from Framewright's validation budget.
- The optional Ran profile records preferences for cross-unit cuts, short reactions and inserts in high-energy sequences, and complete entrances and exits.

## Validation

The release passed package validation, all 140 regression fixtures, 39 focused tests, and three command-line smoke checks. Text review covered one-space sequences, state-card transitions, and retained-shot handoffs. A bilingual wording check exercised the prompt validator with exact dialogue and reference markers, a character budget, and shot-local evidence for a complete exit.

The shot-plan review and text checks validate the workflow and protected prompt clauses. They do not establish how a video model will execute the timing or edit. Platform-specific text caps require evidence for the selected entry.

The v4.2.5 snapshot remains available alongside this release.
