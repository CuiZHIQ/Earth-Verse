# Final Answer

```json
{
  "classification": "peat_smoke_co_signal",
  "co_signal": {
    "usual_surface_ppb": 100,
    "peak_surface_borneo_ppb_nearly": 1300,
    "peak_to_usual_multiplier": 13.0
  },
  "vertical_transport": {
    "calipso_plume_km": 2,
    "airs_co_km": 5,
    "mls_co_km": 9,
    "mls_to_calipso_ratio": 4.5
  },
  "context_checks": {
    "rainfall_totals_secondary": true,
    "burn_perimeter_from_dnbr": "not_established"
  },
  "image_reading": "The 2015-09-30 true-color view is consistent with a broad gray haze layer compared with the 2015-07-02 pre-event view.",
  "computed_interpretation": "The decisive ledger is peat-smoke gas loading: near-surface CO rose to about thirteen times the usual value and was also detected several kilometers above the surface."
}
```

# Key Computations

Hidden inputs used by `compute_gt.py`:

- `data/event_reports/event_reports_004_Locked_anchor_report_NASA_Earth_Observatory.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_2015_Southeast_Asia_haze_from_Indonesian_fires.json`
- `data/remote_sensing/remote_sensing_001_pre.jpg`
- `data/remote_sensing/remote_sensing_002_event.jpg`
- `data/physical_hazard/physical_hazard_009_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_daily_weather_fill.json`
- `metadata/files.csv`

Core values:

- Event window: 2015-08-01 to 2015-11-30.
- Usual carbon monoxide over Indonesia: about 100 ppb.
- Peak surface carbon monoxide in parts of Borneo: nearly 1,300 ppb.
- Peak-to-usual multiplier: `1300 / 100 = 13.0`.
- CALIPSO plume height over central Kalimantan on 2015-10-04: 2 km.
- AIRS carbon monoxide height: about 5 km above the surface.
- MLS elevated carbon monoxide height in late October: upwards of 9 km.
- MLS-to-CALIPSO height ratio: `9 / 2 = 4.5`.
- Sentinel-2 dNBR scene counts: 0 pre-event scenes and 0 post-event scenes, so a burn-perimeter answer is not established by that product.
- Rainfall context values are secondary diagnostics, not the full event explanation: GPM mean 178.993 mm, CHIRPS mean 262.833 mm, ERA5-Land mean 292.612 mm, and the available Open-Meteo point total is 170.9 mm for 2015-08-01 to 2015-09-15.
- True-color views: 2015-07-02 pre-event and 2015-09-30 during-event MODIS Terra scenes.

# Reasoning Path

The strongest classification is `peat_smoke_co_signal` because the carbon monoxide increase is large and directly tied to peat-fire smoke. The surface CO peak of nearly 1,300 ppb is about thirteen times the usual 100 ppb value over Indonesia.

The vertical values reinforce the same ledger rather than creating a separate broad mechanism task. CALIPSO reported a 2 km smoke plume, AIRS saw CO about 5 km above the surface, and MLS detected elevated CO near 9 km. The 4.5 ratio between the MLS and CALIPSO heights shows that the gas signal extended well above the near-surface plume layer.

The two weaker readings fail as primary classifications. Rainfall totals provide weather context, but they do not outscore the CO and height ledger. The dNBR product has zero usable pre-event and post-event scenes, so it does not establish the requested burn-perimeter reading.

The true-color image pair gives a compact visual cross-check: the during-event view aligns with widespread gray haze compared with the pre-event scene, while the numeric CO ledger supplies the decisive classification.

# Computed Interpretation

The event should be scored as a peat-smoke carbon monoxide signal, with rainfall and dNBR treated as secondary checks rather than the primary ledger.

# Scoring Rubric

Total: 20 points.

- Classification and JSON shape (3 points): Gives `peat_smoke_co_signal` and returns the requested compact JSON fields. Partial credit: 1-2 points for the right classification with missing fields, or a parseable ledger with a weaker but related label.
- Carbon monoxide arithmetic (4 points): Reports about 100 ppb usual CO, nearly 1,300 ppb peak surface CO, and the 13.0x multiplier. Partial credit: 1-3 points for two correct values, a correct formula with a rounding issue, or correct units with one missing CO anchor.
- Vertical transport ledger (4 points): Reports 2 km, 5 km, 9 km, and the 4.5 MLS-to-CALIPSO ratio. Partial credit: 1-3 points for most heights with a missing ratio or one swapped/misrounded value.
- Context checks (3 points): Marks available package rainfall diagnostics as secondary and marks the dNBR burn-perimeter test as `not_established` because pre and post counts are both zero. Partial credit: 1-2 points for getting one check right or giving the right conclusion without the scene-count reason.
- Image-to-number synthesis (3 points): Connects the 2015-09-30 true-color haze view to the CO ledger while keeping the 2015-07-02 image as the pre-event comparison. Partial credit: 1-2 points for mentioning haze imagery without dates or without linking it to the CO values.
- Compact computed interpretation (3 points): Keeps the final sentence tied to peat-smoke gas loading and avoids realized-loss counts, action steps, and broad policy claims. Partial credit: 1-2 points for a mostly ledger-based interpretation with minor extra narrative.
