# Greece Wildfire Smoke-Chain Score Ledger

A wildfire science team is checking a compact score ledger for the July-August 2023 Greece wildfires. The test is whether the technical record supports a regional smoke-transport chain more strongly than a local Athens fire-context reading or a burn-surface mapping reading.

Compute these scores from the record:

- `regional_smoke_chain = 2*(alexandroupolis_source) + 1*(southwest_transport) + 1*(receptor_count >= 3) + 1*(weather_terms_count == 3) + 1*(late_august_fires_min >= 24) + 1*(timing_hours <= 24) + 1*(viirs_date == "2023-08-22")`
- `athens_local_fire_context = 1*(athens_cue_count >= 4) + 1*(weather_terms_count == 3) + 1*(late_august_fires_min >= 24)`
- `burn_surface_mapping = 1*(dnbr_max >= 0.75) + 1*(dnbr_mean >= 0.10) + 1*(alphaearth_mean >= 0.10) + 1*(post_pre_scene_ratio >= 1.20)`. Treat these as available surface-comparison metrics, not as a strict event-window burn-perimeter proof.

Treat "dozens" as a minimum count of 24. Use `1` for a true text or numeric gate and `0` otherwise. The lead label is valid only if the top score is at least 7 and the top score minus the second score is at least 4.

Return compact JSON:

```json
{
  "target_family": "candidate_explanation_score_ledger",
  "metrics": {
    "late_august_fires_min": 0,
    "timing_hours": 0,
    "receptor_count": 0,
    "weather_terms_count": 0,
    "viirs_date": "YYYY-MM-DD",
    "dnbr_mean": 0,
    "dnbr_max": 0,
    "alphaearth_mean": 0,
    "post_pre_scene_ratio": 0
  },
  "text_gates": {
    "alexandroupolis_source": false,
    "southwest_transport": false,
    "athens_local_cues": false
  },
  "scores": {
    "regional_smoke_chain": 0,
    "athens_local_fire_context": 0,
    "burn_surface_mapping": 0
  },
  "score_comparison": {
    "lead_signal": "",
    "second_signal": "",
    "low_score_signal": ""
  },
  "margin": 0,
  "answer": "short_label",
  "computed_consequence": "one sentence tied only to the ledger"
}
```
