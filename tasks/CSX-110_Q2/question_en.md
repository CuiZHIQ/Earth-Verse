# Cyclone Freddy Scenario Sensitivity Ranking

A tropical-cyclone verification team is stress-testing the Cyclone Freddy diagnosis for Madagascar, Mozambique, and Malawi during February-March 2023. The baseline diagnosis is `long_duration_delayed_rain_flood_lag_event_not_wind_only`. Your task is to rank plausible scenario perturbations by how much each one could change that duration-wind-rain-lag diagnosis.

Use only the local CSX-110 event package evidence. Prioritize storm/event catalog data, event-report text, hourly wind/rain/pressure observations, daily point rainfall, and gridded rainfall summaries.

Return one compact JSON object with this top-level structure:

```json
{
  "answer": "scenario_name",
  "target_family": "freddy_duration_wind_rain_lag_sensitivity_ranking",
  "computed_values": {},
  "scenario_scores": {},
  "ranked_scenarios": [],
  "top_sensitivity": {},
  "rejected_sensitivity": {},
  "reasoning_path": []
}
```

Rank these candidate perturbations, using the names exactly as written:

- `rainfall_duration_shortened`
- `rainfall_load_reduced`
- `peak_wind_reinterpreted_as_primary`
- `pressure_signal_weakened`
- `flood_lag_removed`
- `gridded_rainfall_context_weakened`

Compute the baseline evidence first:

- WMO record-duration anchor and catalog tropical-cyclone duration.
- Catalog alert level and peak wind, plus the local hourly peak gust and gust-to-catalog-wind ratio.
- Hourly rainfall total, wet-hour count, wet-hour share, wet-day count, longest wet run, wettest 72 h and 168 h rainfall shares, and pressure range.
- Daily point rainfall total and daily exceedance counts.
- GPM and CHIRPS event precipitation means and maxima, their max-to-mean ratios, and the CHIRPS-to-GPM mean ratio.
- The time lag from the catalog cyclone end to the Malawi flood start.

Use this deterministic sensitivity rule: for each candidate, compute the fractional perturbation needed to cross the competing-diagnosis threshold, then score it as `max(0, 100 * (1 - fractional_change_needed))`. Higher score means the diagnosis is more sensitive to that perturbation. Round scores to three decimals.

Candidate threshold rules:

- `rainfall_duration_shortened`: the smaller fractional count removal needed either to push wet hours below `400` or wet days below `30`.
- `rainfall_load_reduced`: the smaller fractional uniform rainfall reduction needed for either hourly or daily point event precipitation to fall below `300 mm`.
- `peak_wind_reinterpreted_as_primary`: the fractional increase in the local gust-to-catalog-peak ratio needed to reach `0.50`.
- `pressure_signal_weakened`: the fractional weakening of the hourly pressure range needed for the range to fall below `5 hPa`.
- `flood_lag_removed`: the fraction of the `72 h` short-lag cutoff needed to move the flood start from the observed lag to the cutoff.
- `gridded_rainfall_context_weakened`: the smaller fractional weakening needed for either the GPM or CHIRPS max-to-mean rainfall ratio to fall below `2.0`.

The final ranking should identify the top sensitivity and the perturbation that remains least plausible as a diagnosis-changing alternative.
