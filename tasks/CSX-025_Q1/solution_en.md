# Final Answer

```json
{
  "heat_load_c_day": 11.8,
  "hottest_3day_tmax_mean_c": 33.9,
  "night_recovery_ratio": 0.429,
  "apparent_air_peak_delta_c": -0.2,
  "population_heat_load_proxy_person_c_day": 2072.8,
  "diagnosis": "sustained_heat_load_human_health_pathway"
}
```

These indices support a sustained heat-load diagnosis: the event accumulated 11.8 C-days above 30 C, the hottest three-day air-temperature mean was 33.9 C, and 3 of 7 nights stayed at or above 16 C, while apparent temperature did not exceed air temperature enough to make humid heat the primary mechanism.

# Key Computations

- Cumulative heat load: daily `Tmax` values were 27.3, 30.1, 32.2, 34.0, 35.5, 26.7, and 22.3 C. Applying `sum(max(Tmax - 30, 0))` gives `0.1 + 2.2 + 4.0 + 5.5 = 11.8 C-days`.
- Hottest 3-day mean: the peak window is 2021-06-27 through 2021-06-29, with `(32.2 + 34.0 + 35.5) / 3 = 33.9 C`.
- Night recovery ratio: Tmin reached at least 16 C on 3 of 7 nights, so `3 / 7 = 0.429`.
- Apparent-air peak delta: max apparent temperature was 35.3 C and max air temperature was 35.5 C, so `35.3 - 35.5 = -0.2 C`.
- Local population heat-load proxy: local population sum 175.659 times 11.8 C-days gives 2072.8 person-C-days.

# Reasoning Path

The diagnosis is sustained heat load rather than a single peak-day explanation because the heat-load sum is positive across four consecutive hot days, not only on 2021-06-29. The 33.9 C rolling mean confirms that the peak was embedded in a multi-day hot spell, and the 0.429 warm-night ratio shows incomplete overnight cooling. The apparent-air peak delta is slightly negative, so a moisture-amplified humid-heat interpretation is weaker than the air-temperature heat-load pathway. The population proxy scales the local exposure context by the computed heat burden without converting it into losses.

# Computed Interpretation

The compact event interpretation is a multi-day heat-health stress pathway: sustained daytime exceedance, limited night recovery, and local exposure combine into the strongest computed signal, while drought, fire/smoke, visible-damage, rainfall, and asset-count readings remain secondary.

# Scoring Rubric

- 4 points: Returns the requested compact JSON with all five numeric fields and a sustained heat-load diagnosis label. Partial credit: up to 2 points for the correct diagnosis with missing fields; up to 1 point for valid JSON that omits the diagnosis label.
- 4 points: Computes cumulative heat load correctly as 11.8 C-days above 30 C. Partial credit: up to 3 points for the right formula with a small arithmetic or rounding error; up to 2 points for counting hot days without summing degree exceedances.
- 3 points: Computes the hottest 3-day Tmax mean correctly as 33.9 C for 2021-06-27 through 2021-06-29. Partial credit: up to 2 points for a correct rolling-window method with minor rounding or date imprecision.
- 3 points: Computes the night recovery ratio correctly as 0.429 from 3 warm nights in a 7-day event window. Partial credit: up to 2 points for the correct warm-night count with a denominator or rounding mistake.
- 2 points: Computes the apparent-minus-air peak delta correctly as about -0.2 C and uses it to treat humid heat as weaker than the air-temperature heat-load pathway. Partial credit: 1 point for the correct qualitative comparison without the numeric delta.
- 2 points: Computes or correctly interprets the local population heat-load proxy as about 2072.8 person-C-days while treating it as an exposure-scaled proxy. Partial credit: 1 point for multiplying the correct quantities but overstating what the proxy proves.
- 1 point: Explains the temporal persistence and limited overnight recovery as the key heat-health pathway. Partial credit: this point is earned only when persistence is explicitly tied to heat-health stress.
- 1 point: Rejects peak-day-only, humid-heat, drought, fire/smoke, visible-damage, rainfall, or asset-count shortcuts as secondary. Partial credit: this point is earned only when at least one tempting shortcut is rejected by a computed value.
