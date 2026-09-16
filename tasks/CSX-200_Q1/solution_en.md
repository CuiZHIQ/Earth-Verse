# Final Answer

```json
{
  "target_family": "candidate_explanation_score_ledger",
  "metrics": {
    "late_august_fires_min": 24,
    "timing_hours": 24,
    "receptor_count": 3,
    "weather_terms_count": 3,
    "viirs_date": "2023-08-22",
    "dnbr_mean": -0.083037,
    "dnbr_max": 0.859705,
    "alphaearth_mean": 0.061316,
    "post_pre_scene_ratio": 1.64
  },
  "text_gates": {
    "alexandroupolis_source": true,
    "southwest_transport": true,
    "athens_local_cues": true
  },
  "scores": {
    "regional_smoke_chain": 8,
    "athens_local_fire_context": 3,
    "burn_surface_mapping": 2
  },
  "score_comparison": {
    "lead_signal": "regional_smoke_chain",
    "second_signal": "athens_local_fire_context",
    "low_score_signal": "burn_surface_mapping"
  },
  "margin": 5,
  "answer": "regional_smoke_chain_dominant",
  "computed_consequence": "The ledger favors a regional smoke-transport chain; burn-surface metrics are mixed because only the maximum dNBR and scene-count ratio pass."
}
```

The regional smoke-chain score is 8, the Athens local-fire-context score is 3, and the burn-surface-mapping score is 2. The top score clears the dominance rule because 8 is at least 7 and the margin over the second score is 5.

# Key Computations

The reproducible values come from local CSX-200 files:

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_2023_Greece_wildfires.json`
- `data/event_reports/event_reports_004_Locked_anchor_report_NASA_Earth_Observatory.html`
- `data/physical_hazard/physical_hazard_009_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/remote_sensing/remote_sensing_004_Google_Satellite_Embedding_annual_cosine-change_stats.json`

Report-derived inputs:

- `alexandroupolis_source = true`
- `southwest_transport = true`
- `receptor_count = 3` for Italy, the Mediterranean Sea, and northern Africa
- `weather_terms_count = 3` for hot, dry, and windy
- `late_august_fires_min = 24`, interpreting "dozens" as a minimum count of 24
- `timing_hours = 24`
- `viirs_date = "2023-08-22"`
- `athens_cue_count = 4` for Athens, homes, cars, and smoke over the capital city

Remote-sensing inputs are available surface-comparison metrics, not a strict event-window burn-perimeter proof. The Sentinel-2 dNBR post window extends from 2023-07-01 to 2023-09-29, beyond the 2023-08-31 event lock:

- `dnbr_mean = -0.083037`
- `dnbr_max = 0.859705`
- `alphaearth_mean = 0.061316`
- `post_pre_scene_ratio = 82 / 50 = 1.64`

Score arithmetic:

- `regional_smoke_chain = 2*1 + 1 + 1 + 1 + 1 + 1 + 1 = 8`
- `athens_local_fire_context = 1 + 1 + 1 = 3`
- `burn_surface_mapping = 1 + 0 + 0 + 1 = 2`
- `margin = 8 - 3 = 5`

# Reasoning Path

The ledger is designed to compare three bounded readings of the same fire episode. The regional smoke chain receives two points for a named source near Alexandroupolis, then one point each for southwest transport, three named receptors, all three fire-weather terms, a minimum of 24 late-August fires, a 24-hour ignition window, and the August 22 VIIRS date. The Athens local-fire reading is real but narrower: it has the local text cues, the same fire-weather terms, and the same late-August count, for 3 points. The burn-surface reading gets credit for a high maximum dNBR and adequate post/pre scene ratio, but it fails the mean dNBR and AlphaEarth mean-change thresholds. Therefore the regional smoke-chain label is the only one that clears both the score and margin tests.

# Computed Interpretation

The calculation identifies a strong regional smoke-transport chain rather than a burn-surface-mapping lead: the report text supplies a coherent source-to-receptor path, while the surface-change metrics are mixed.

# Scoring Rubric

Total: 20 points

- 3 points: Returns the requested compact JSON with `target_family`, `metrics` including `viirs_date`, `text_gates`, `scores`, `score_comparison`, `margin`, `answer`, and `computed_consequence`; partial credit for minor key-name differences that preserve all scored fields.
- 4 points: Extracts the report metrics correctly: minimum late-August fire count 24, timing window 24 hours, receptor count 3, weather terms count 3, and VIIRS date 2023-08-22; partial credit for correct threshold states with one missing or rounded value.
- 3 points: Sets the text gates correctly: Alexandroupolis source true, southwest transport true, and Athens local cues true with cue count at least 4; partial credit for two correct gates.
- 3 points: Uses the available surface-comparison metrics correctly: dNBR mean -0.083037, dNBR maximum 0.859705, AlphaEarth mean 0.061316, and post/pre scene ratio 1.64, without treating them as strict event-window burn-perimeter proof; partial credit for correct threshold states with weaker rounding.
- 3 points: Applies the formulas exactly, yielding regional smoke chain 8, Athens local-fire context 3, and burn-surface mapping 2; partial credit for one arithmetic error that does not alter the lead label.
- 3 points: Applies the dominance rule correctly, with lead signal `regional_smoke_chain`, second signal `athens_local_fire_context`, low-score signal `burn_surface_mapping`, margin 5, and answer `regional_smoke_chain_dominant`; partial credit for the right answer with incomplete comparison fields.
- 1 point: Keeps the consequence tied to the computed ledger and avoids extra burned-area, casualty, evacuation, hospital, or asset-loss totals not produced by the calculation; partial credit is not awarded for broad narrative additions.
