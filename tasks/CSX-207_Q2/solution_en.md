# Final Answer

Canonical result ID: `regional_wildfire_smoke_consistency_pass`.

```json
{
  "event_window_days": 52,
  "ledger": [
    {
      "test": "smoke_pm_proxy_load",
      "formula": "150 PM2.5 exceedance days / 52 event days",
      "value": 2.88,
      "threshold_result": "pass: >= 1.00",
      "implication": "The annual reported PM2.5 exceedance burden is a strong smoke/PM proxy when normalized by the event-window duration."
    },
    {
      "test": "burn_event_density",
      "formula": "459 regional wildfire records / 46 catalog days; 44 active days / 46 days",
      "value": {"density_per_day": 9.98, "active_day_fraction": 0.96},
      "threshold_result": "pass: density >= 5 and active fraction >= 0.80",
      "implication": "Many regional burn records support a distributed smoke source field over the available daily catalog slice."
    },
    {
      "test": "fire_weather_support",
      "formula": "sum(max(Tmax - 35, 0)); longest precip <= 0.1 mm/day run; count wind max >= 20 km/h",
      "value": {"heat_load_c_day": 32.7, "dry_run_days": 19, "windy_days": 21},
      "threshold_result": "pass: heat load >= 25, dry run >= 14, windy days >= 15",
      "implication": "The available daily weather slice is hot, dry, and periodically windy enough to support fire activity and smoke movement."
    },
    {
      "test": "precipitation_clearing",
      "formula": "62.4048 mm CHIRPS mean / 46 available CHIRPS days; 39 dry days / 46 weather days",
      "value": {"chirps_mm_day": 1.36, "dry_day_fraction": 0.85},
      "threshold_result": "clearing fails: < 2 mm/day and dry fraction >= 0.75",
      "implication": "Rainfall in the available product slice is too diffuse to reset the fire-smoke classification."
    },
    {
      "test": "satellite_localization",
      "formula": "dNBR max/mean and embedding-change max/mean, with broad conversion ruled out if both means are low",
      "value": {"dnbr_ratio": 8.04, "embedding_ratio": 14.5, "broad_conversion": false},
      "threshold_result": "localized: ratios > 5, dNBR mean 0.112 < 0.20, embedding mean 0.053 < 0.08",
      "implication": "Large maxima but low means indicate localized burn or surface change, not broad regional conversion."
    }
  ],
  "final_classification": "Regional wildfire-smoke loading is numerically consistent with distributed burns, supportive fire weather, incomplete rain clearing, and localized burn scars.",
  "rejected_alternative": "A compact local fire, heat-only event, rainfall-cleared recovery, or basin-wide land-cover conversion fails at least one computed test."
}
```

# Key Computations

The event window is inclusive: 2024-08-01 through 2024-09-21 gives `52` days. The smoke/PM proxy ratio is `150 / 52 = 2.8846`, rounded to `2.88`; the numerator is a reported 2024 PM2.5 exceedance burden proxy, not a direct event-day PM monitor series.

For the available 2024-08-01 to 2024-09-15 catalog slice, the country-title filter gives `459` wildfire records for Brazil, Bolivia, or Paraguay. Over `46` days this is `459 / 46 = 9.98` records/day. At least one matching record appears on `44` of `46` days, so the active-day fraction is `44 / 46 = 0.96`. Daily catalog, weather, and CHIRPS-normalized tests keep this available-slice denominator rather than inferring the uncovered 2024-09-16 to 2024-09-21 tail.

Daily weather over the same 46-day slice gives heat load `sum(max(Tmax - 35, 0)) = 32.7 C-day`, longest precipitation `<= 0.1 mm/day` run of `19` days, and `21` days with maximum 10 m wind speed `>= 20 km/h`.

The precipitation-clearing check uses CHIRPS mean accumulated precipitation: `62.4048 / 46 = 1.36 mm/day`. The weather slice has `39` dry days, so `39 / 46 = 0.85`.

The satellite contrast check gives dNBR `0.90365 / 0.11239 = 8.04` and annual embedding change `0.77023 / 0.05313 = 14.50`. The low means, `0.112` for dNBR and `0.053` for embedding change, keep the result localized rather than basin-wide.

# Reasoning Path

Each row asks whether one numeric family agrees with the final classification. The smoke row passes because the PM2.5 exceedance count is far larger than the inclusive event-window length. The burn row passes because the catalog has both high record density and activity on nearly all days in the slice.

The weather row passes because heat, dry persistence, and wind all clear their thresholds. The rain-clearing row fails as a clearing explanation because the CHIRPS daily mean is below `2 mm/day` while the weather dry-day fraction is high. The satellite row supports localization because peak-to-mean ratios are large while both spatial means stay below the broad-conversion thresholds.

# Computed Interpretation

The ledger supports a regional wildfire-smoke classification with localized burn scars. The weaker alternatives fail for numeric reasons: a compact local fire is too narrow for the catalog density, a heat-only event lacks the burn and smoke rows, rainfall-cleared recovery conflicts with the dry and CHIRPS rows, and broad land-cover conversion conflicts with the low satellite means.

# Scoring Rubric

- 4 points: Returns the requested compact JSON with `event_window_days`, a row-wise `ledger`, `final_classification`, and `rejected_alternative`. Partial credit: 2-3 points for a parseable JSON object with one missing or renamed field; 1 point if the fields are mostly recoverable from prose.
- 5 points: Computes the core numeric anchors correctly: 52 days, annual-proxy PM ratio 2.88, 459/46 = 9.98 burn records/day, active-day fraction 0.96, heat load 32.7 C-day, dry run 19 days, windy days 21, CHIRPS 1.36 mm/day over the available slice, dry fraction 0.85, and satellite ratios 8.04 and 14.50. Partial credit: proportional credit for correct values with units, with reductions for rounding drift or one missed count.
- 4 points: Applies the threshold tests correctly for smoke persistence, burn-event density, fire-weather support, failed precipitation clearing, and localized satellite contrast. Partial credit: 1 point for each correctly applied gate group, capped at 4 points.
- 3 points: Gives row-by-row reasoning that ties each calculation to the consistency proof without replacing it with broad event prose. Partial credit: 1-2 points when most rows connect numbers to threshold results but one implication is vague.
- 2 points: Rejects at least two weaker alternatives using the computed tests, such as compact local fire, heat-only event, rainfall-cleared recovery, or broad regional land-cover conversion. Partial credit: 1 point for one weaker alternative with a correct numeric reason.
- 1 point: Uses a concise final classification label consistent with the calculations. Partial credit: 0.5 points for the right classification stated too verbosely or with minor wording drift.
- 1 point: Avoids uncalculated loss, infrastructure-damage, or basin-wide conversion statements. Partial credit: 0.5 points if there is one small extra assertion that does not alter the numeric conclusion.
