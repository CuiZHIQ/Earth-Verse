# Final Answer

```json
{
  "target_family": "ian_landfall_core_timing_rainfall_concentration_ledger",
  "checks": [
    {
      "id": "catalog_window",
      "test": "alert_level == 'Red' and affected_has_us_cuba and mentions_florida and mentions_carolinas and mentions_cuba",
      "values": {
        "catalog_alert_level": "Red",
        "catalog_wind_severity_kmh": 249.9984,
        "affected_has_united_states": true,
        "affected_has_cuba": true,
        "report_text_source_role": "local_event_summary_report_text",
        "mentions_florida": true,
        "mentions_carolinas": true,
        "mentions_cuba": true
      },
      "pass": true,
      "reason": "The catalog and report flags all match the Ian verification window."
    },
    {
      "id": "wind_pressure_lock",
      "test": "peak_gust_time == min_pressure_time and pressure_drop_hpa > 40",
      "values": {
        "shared_time": "2022-09-28T19:00",
        "peak_gust_kmh": 185.4,
        "peak_wind_kmh": 105.7,
        "pressure_baseline_time": "2022-09-23T00:00",
        "pressure_baseline_hpa": 1010.3,
        "min_pressure_hpa": 966.9,
        "pressure_drop_hpa": 43.4,
        "gust_pressure_lag_hours": 0.0
      },
      "pass": true,
      "reason": "The gust maximum and pressure minimum are simultaneous, and the first-hour to minimum-pressure drop is 43.4 hPa."
    },
    {
      "id": "rainfall_concentration",
      "test": "total_precip_mm > 200 and max24_to_total_fraction > 0.65 and peak_rain_pressure_lag_hours <= 6",
      "values": {
        "total_precip_mm": 211.5,
        "max_24h_precip_mm": 149.9,
        "max24_to_total_fraction": 0.709,
        "peak_rain_time": "2022-09-28T22:00",
        "min_pressure_time": "2022-09-28T19:00",
        "peak_rain_pressure_lag_hours": 3.0
      },
      "pass": true,
      "reason": "The point rainfall total clears 200 mm, the wettest 24 hours contain 70.9 percent of it, and peak-hour rain is 3 hours from the pressure minimum."
    },
    {
      "id": "duration_balance",
      "test": "max72_to_total_fraction > 0.90 and max6_to_max24_fraction < 0.50",
      "values": {
        "total_precip_mm": 211.5,
        "max_6h_precip_mm": 67.0,
        "max_24h_precip_mm": 149.9,
        "max_72h_precip_mm": 202.9,
        "max72_to_total_fraction": 0.959,
        "max6_to_max24_fraction": 0.447
      },
      "pass": true,
      "reason": "Nearly all rainfall sits inside the wettest 72 hours, while the wettest 6 hours are less than half of the wettest 24-hour total."
    },
    {
      "id": "gridded_peak_contrast",
      "test": "max_grid_precip_mm / point_max_24h_precip_mm < 0.50",
      "values": {
        "grid_precip_maxima_mm": [46.63, 53.225, 73.144],
        "max_grid_precip_mm": 73.144,
        "point_max_24h_precip_mm": 149.9,
        "max_grid_to_point_24h_fraction": 0.488
      },
      "pass": true,
      "reason": "The largest gridded maximum is 0.488 of the point wettest-24-hour amount, which is below the 0.50 cutoff."
    }
  ],
  "final_classification": "Ian passes all five checks as a locked wind-pressure event with concentrated multi-day rainfall around the landfall-core hour.",
  "score_summary": "passes_all_five_checks; 5 of 5 checks pass."
}
```

# Key Computations

The catalog alert for IAN-22 is `Red`, catalog wind severity is `249.9984 km/h`, affected countries include the United States and Cuba, and the local event-summary report text mentions Florida, the Carolinas, and Cuba.

From the hourly point weather record, the peak gust is `185.4 km/h`, peak wind is `105.7 km/h`, and the minimum pressure is `966.9 hPa`. The pressure-drop baseline is the first hourly sea-level pressure value in the event-window point series: `1010.3 hPa` at `2022-09-23T00:00`, so the pressure drop is `1010.3 - 966.9 = 43.4 hPa`. The peak gust and minimum pressure both occur at `2022-09-28T19:00`, giving a `0.0 h` lag.

Hourly precipitation totals `211.5 mm`. Rolling sums give `67.0 mm` for 6 hours, `149.9 mm` for 24 hours, and `202.9 mm` for 72 hours. The wettest-24-hour share is `149.9 / 211.5 = 0.709`, the wettest-72-hour share is `202.9 / 211.5 = 0.959`, and the wettest-6-hour to wettest-24-hour fraction is `67.0 / 149.9 = 0.447`. The peak hourly rain time is `2022-09-28T22:00`, which is `3.0 h` after the pressure minimum.

The three gridded precipitation maxima are `46.63 mm`, `53.225 mm`, and `73.144 mm`. The largest divided by the point wettest-24-hour amount is `73.144 / 149.9 = 0.488`.

# Reasoning Path

First, the catalog and report text place Ian in the correct verification window because the alert is Red, the affected-country test includes the United States and Cuba, and all three place-name flags are true.

Second, the wind-pressure check passes because the largest gust and minimum pressure are co-timed at `2022-09-28T19:00`, and the pressure drop exceeds the `40 hPa` threshold by `3.4 hPa`.

Third, the rainfall concentration check passes because the event total is above `200 mm`, more than `0.65` of the total falls in the wettest 24 hours, and peak-hour rain is only `3 h` from the minimum-pressure hour.

Fourth, the duration balance check prevents a single-burst reading: the wettest 72 hours contain `0.959` of total point rainfall, while the wettest 6 hours are only `0.447` of the wettest 24-hour amount.

Fifth, the gridded contrast check passes because the largest gridded maximum is below half the point wettest-24-hour amount. All five checks therefore support the answer label `passes_all_five_checks`.

# Computed Interpretation

The computed record is a synchronized wind-pressure and rainfall-timing ledger: the strongest gust, deepest pressure, concentrated 24-hour rainfall, and broader 72-hour accumulation form one coherent landfall-core timing pattern.

# Scoring Rubric

- 3 points: Gives the correct final answer label and classification: `passes_all_five_checks`, five of five checks passing, and a concise sentence matching the wind-pressure plus concentrated multi-day rainfall result. Partial credit: award 1-2 points for the right pass count without the exact label or with a vague classification.
- 3 points: Returns the requested JSON shape with the target family, exactly five checks in order, and the required `test`, `values`, `pass`, and `reason` fields. Partial credit: award 1-2 points for a mostly correct structure with one missing check or minor field omissions.
- 5 points: Reports the key numeric anchors accurately: `249.9984 km/h`, `185.4 km/h`, `105.7 km/h`, the pressure baseline `1010.3 hPa` at `2022-09-23T00:00`, the pressure minimum `966.9 hPa`, `43.4 hPa`, `211.5 mm`, `67.0 mm`, `149.9 mm`, `202.9 mm`, `0.709`, `0.959`, `0.447`, `73.144 mm`, and `0.488`. Partial credit: award 3-4 points for mostly correct wind-pressure and rainfall values; award 1-2 points for copied values with missing ratios or timing.
- 4 points: Applies all threshold and timing tests correctly: Red catalog window, zero gust-pressure lag, pressure drop greater than `40 hPa`, total precipitation greater than `200 mm`, wettest-24-hour share greater than `0.65`, rain-pressure lag at most `6 h`, wettest-72-hour share greater than `0.90`, wettest-6-hour fraction below `0.50`, and grid fraction below `0.50`. Partial credit: award 2-3 points for correct decisions with one or two arithmetic or threshold mistakes; award 1 point for qualitative pass/fail statements without inequalities.
- 3 points: Explains why the duration and grid checks refine the ledger rather than duplicating the rainfall total, especially the difference between a 24-hour concentration, a 72-hour accumulation, and lower gridded maxima. Partial credit: award 1-2 points for explanations that mention these checks but do not connect them to the computed ratios.
- 2 points: Keeps the answer compact and calculation-led, without adding casualty totals, damage estimates, or instructions outside the requested ledger. Partial credit: award 1 point for a correct ledger with extra prose that does not change the answer.
