# Final Answer

```json
{
  "target_family": "candidate_explanation_score_ledger",
  "event_window": {
    "start": "2023-05-01",
    "end": "2023-09-30",
    "days": 153
  },
  "hazard_window": {
    "start": "2023-05-01",
    "end": "2023-06-15",
    "days": 46
  },
  "metrics": {
    "burn_index": 44.91,
    "dnbr_mean": 0.329,
    "dnbr_max": 1.003,
    "alpha_mean_change": 0.02035,
    "gpm_precip_mm": 70.6,
    "chirps_precip_mm": 76.56,
    "era5_precip_mm": 136.35,
    "peak_tmax_c": 19.06,
    "mean_tmax_c": 16.64,
    "worldpop_population": 175.7,
    "fire_station_count": 1,
    "trunk_road_count": 15
  },
  "text_gates": {
    "smoke_air_quality": true,
    "smoke_health": true,
    "out_of_control_fire": true
  },
  "scores": {
    "burn_smoke": 8,
    "rainfall": 0,
    "heat": 0,
    "weak_signal": 0,
    "local_context": 3
  },
  "score_comparison": {
    "dominant_signal": "burn_smoke",
    "secondary_signal": "rainfall_heat_weak_signal_tie",
    "margin": 8,
    "dominance_rule_pass": true
  },
  "severity_bin": "high",
  "answer": "wildfire_burn_smoke_dominant",
  "computed_consequence": "The ledger isolates a high burn-smoke signal while rainfall and heat counters remain below their trigger thresholds."
}
```

# Key Computations

Core event window:

- Event: 2023 Canadian wildfires and smoke.
- Window: 2023-05-01 to 2023-09-30, inclusive duration 153 days.
- Physical-hazard diagnostic window used by precipitation and temperature products: 2023-05-01 to 2023-06-15, inclusive duration 46 days.
- Hazard family in the local metadata: `wildfire_burn_smoke`.

Burn and surface-change metrics:

```text
dNBR_mean = 0.328507
dNBR_max = 1.002855
alpha_mean_change = 0.020350

burn_index = dNBR_mean * 100 + dNBR_max * 10 + alpha_mean_change * 100
burn_index = 0.328507 * 100 + 1.002855 * 10 + 0.020350 * 100
burn_index = 44.914
```

The severity thresholds put `burn_index = 44.91` in the `high` bin.

Text gates from the event report:

- `smoke_air_quality = true`
- `smoke_health = true`
- `out_of_control_fire = true`

Counter metrics:

- GPM mean precipitation: 70.60 mm, below the 100 mm rainfall counter threshold.
- CHIRPS mean precipitation: 76.56 mm, below the 100 mm rainfall counter threshold.
- ERA5 mean precipitation: 136.35 mm, below the 150 mm rainfall counter threshold.
- ERA5 peak Tmax: 19.06 C, below the 30 C heat counter threshold.
- ERA5 mean Tmax: 16.64 C, below the 25 C heat counter threshold.

Local context metrics:

- WorldPop population: 175.659, rounded to 175.7.
- Fire-station count: 1.
- Trunk-road count: 15.

Score arithmetic:

```text
burn_smoke = 2 + 1 + 1 + 1 + 1 + 1 + 1 = 8
rainfall = 0 + 0 + 0 = 0
heat = 0 + 0 = 0
weak_signal = 0 + 0 + 0 + 0 = 0
local_context = 1 + 1 + 1 = 3
margin = 8 - max(0, 0, 0) = 8
```

# Reasoning Path

The burn-and-smoke score receives full support from the burn index, dNBR mean, dNBR maximum, annual embedding-change mean, and three report-text gates. Its score is 8.

The rainfall counter receives no points because all three precipitation means are below their thresholds. The heat counter also receives no points because both temperature metrics are far below their thresholds. The weak-signal counter is zero because the burn index, dNBR mean, and smoke gates all point away from a weak event signal.

The dominance rule is therefore satisfied: `burn_smoke >= 7` and the margin over the strongest counter score is `8`, which is greater than the required margin of 5. The final answer is `wildfire_burn_smoke_dominant`, with `severity_bin = high`.

# Computed Interpretation

The calculation supports a high burn-smoke ledger result: direct burn metrics and smoke text gates dominate, while rainfall and heat counters fail their thresholds. The local context score adds nearby population and asset context, but it does not control the dominance margin.

# Scoring Rubric

Total: 20 points.

- 3 points: Requested JSON structure and final label. Full credit for returning the requested compact JSON fields including event and hazard windows, `severity_bin = high`, and `answer = wildfire_burn_smoke_dominant`. Partial credit for the correct answer with one or two missing fields.
- 4 points: Burn-index formula and burn metrics. Full credit for using `dNBR_mean * 100 + dNBR_max * 10 + alpha_mean_change * 100` and reporting burn index within 1.0 of 44.91, dNBR mean within 0.02 of 0.329, dNBR max within 0.02 of 1.003, and alpha mean change within 0.002 of 0.02035. Partial credit for the right formula with one incorrect or omitted metric.
- 3 points: Report text gates. Full credit for setting smoke air quality, smoke health, and out-of-control fire gates to true. Partial credit for two correct gates or for a correct smoke gate pair with the fire gate omitted.
- 3 points: Counter metrics and threshold states. Full credit for reporting the 2023-05-01 to 2023-06-15 hazard diagnostic window, GPM 70.6 mm, CHIRPS 76.56 mm, ERA5 precipitation 136.35 mm, peak Tmax 19.06 C, mean Tmax 16.64 C, and marking rainfall and heat counters as zero. Partial credit for correct threshold states with one or two missing numeric values.
- 2 points: Local context score. Full credit for reporting WorldPop population near 175.7, fire-station count 1, trunk-road count 15, and `local_context = 3`. Partial credit for two correct local context inputs or a correct score with one missing input.
- 4 points: Score arithmetic and dominance rule. Full credit for scores `burn_smoke = 8`, `rainfall = 0`, `heat = 0`, `weak_signal = 0`, margin 8, and `dominance_rule_pass = true`. Partial credit for one arithmetic error that does not change the final answer.
- 1 point: Computed consequence. Full credit for a one-sentence consequence tied to the ledger, with no added casualty, health-burden, evacuation, or loss totals. Partial credit for a correct but verbose consequence.
