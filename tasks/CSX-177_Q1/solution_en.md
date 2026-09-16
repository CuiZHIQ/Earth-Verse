# Final Answer

The computed answer is `20.40`, with severity class `high`.

```json
{
  "reported_wind_dry_burn_forcing_index": 20.4,
  "units": "thousand-hectare anchor-fraction index",
  "inputs": {
    "A_report_anchor_count": 3,
    "E_early_active_days": 4,
    "N_event_days": 10,
    "early_active_fraction": 0.4,
    "H_burned_area_kha": 17.0,
    "anchors": {
      "strong_winds_text": true,
      "dry_weather_text": true,
      "westerly_smoke_transport_text": true
    }
  },
  "severity_class": "high",
  "interpretation": "The 20.40 reported wind-dry-burn index crosses the high threshold because all three report anchors are present, early fire activity spans 4 of 10 event days, and the report gives about 17.0 kha burned."
}
```

# Key Computations

Input files read by `compute_gt.py`:

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_2022_Uljin-Samcheok_wildfire_in_South_Korea.json`
- `data/event_reports/event_reports_004_Locked_anchor_report_NASA_Earth_Observatory.html`

Event window: 2022-03-04 through 2022-03-13, so `N = 10` inclusive days.

Report text anchors:

- strong winds: present
- dry weather: present
- westerly smoke transport toward southern Japan: present

Therefore `A = 3`.

The report states that fire activity was still detected by March 7 after the March 4 event-window start, so the early active interval is March 4 through March 7 inclusive: `E = 4` days and `E / N = 0.4`.

The report states that nearly 17,000 hectares were charred, so `Hkha = 17.0`.

Formula:

`RWDBFI = A * (E / N) * Hkha`

`RWDBFI = 3 * (4 / 10) * 17.0 = 20.40`

Threshold comparison: `20.40 >= 20`, so the severity class is `high`.

# Reasoning Path

The index is a report-grounded screening measure. It counts whether the report itself contains the wind, dry-weather, and smoke-transport anchors needed for smoke-spread concern, then scales that evidence by early active-fire persistence and reported burned area.

For the Uljin-Samcheok wildfire, all three report anchors are present. The fire activity persisted through the early part of the event window, and the reported burned area is large enough that the product crosses the high threshold. The result should be interpreted as a screening index, not as a measured PM2.5 concentration, smoke dose, health outcome estimate, ignition cause, or exact spread path.

# Computed Interpretation

The computed value supports a high screening-level smoke-transport concern because the report links dry weather, strong wind, westerly smoke movement, early fire persistence, and about 17.0 thousand hectares burned.

# Scoring Rubric

Total: 20 points.

- 4 points: Reports the reported wind-dry-burn forcing index as `20.40`, or an equivalent value within +/-0.05, in the requested numeric field. Partial credit for a value within +/-1.0 caused by rounding or minor arithmetic error.
- 4 points: Finds all three report anchors: strong winds, dry weather, and westerly smoke transport toward southern Japan. Partial credit of 1 point for each correct anchor and 1 point for correctly counting the anchors.
- 3 points: Uses March 4-13 as a 10-day inclusive event window and March 4-7 as a 4-day early active fire interval. Partial credit for identifying the dates but missing one inclusive-day calculation.
- 3 points: Extracts nearly 17,000 hectares and converts it to `17.0` thousand hectares. Partial credit if the hectare value is found but conversion or rounding is wrong.
- 3 points: Applies `RWDBFI = A * (E / N) * Hkha` and classifies the result as `high` because it is at least `20`. Partial credit for using the right variables but misapplying the threshold or fraction.
- 2 points: Provides a bounded computed interpretation linking the report anchors, early fire activity, and burned area to smoke-transport concern. Partial credit for a mostly bounded interpretation with one minor overstatement.
- 1 point: Returns compact JSON with the requested top-level fields. No credit if the answer is unstructured prose only.
