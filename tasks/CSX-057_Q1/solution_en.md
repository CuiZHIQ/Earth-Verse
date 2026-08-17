# Final Answer

```json
{
  "label": "persistent_extreme_rainfall_accumulation",
  "causal_graph": {
    "nodes": [
      {"id": "peak_extreme_rainfall", "role": "trigger", "evidence": "peak_to_20in_ratio=2.41"},
      {"id": "multi_day_accumulation", "role": "trigger", "evidence": "hobby_4day_mean=8.90 in/day; hobby_total_to_20in_ratio=1.78"},
      {"id": "monthly_record_context", "role": "amplifier", "evidence": "houston_month_record_ratio=2.04"},
      {"id": "large_area_water_volume", "role": "amplifier", "evidence": "min_20in_area_volume=10.08 trillion gal"},
      {"id": "heavy_rain_footprint_receptors", "role": "receptor", "evidence": "exposed_density=231.03 people/sq mi"},
      {"id": "short_isolated_downpour", "role": "rejected_alternative", "evidence": "four-day and monthly ratios also exceed the relevant scales"}
    ],
    "edges": [
      {"from": "peak_extreme_rainfall", "to": "multi_day_accumulation", "relationship": "peak rainfall is embedded in a sustained multi-day load"},
      {"from": "multi_day_accumulation", "to": "large_area_water_volume", "relationship": "persistent rainfall over a broad footprint creates large water volume"},
      {"from": "monthly_record_context", "to": "multi_day_accumulation", "relationship": "monthly record ratio confirms persistence beyond one storm hour"},
      {"from": "large_area_water_volume", "to": "heavy_rain_footprint_receptors", "relationship": "large water volume intersects populated heavy-rain area"},
      {"from": "multi_day_accumulation", "to": "short_isolated_downpour", "relationship": "multi-day and monthly accumulation contradict a short isolated downpour framing"}
    ]
  },
  "key_values": {
    "peak_to_20in_ratio": 2.41,
    "hobby_4day_mean_in_per_day": 8.9,
    "hobby_total_to_20in_ratio": 1.78,
    "houston_month_record_ratio": 2.04,
    "exposed_density_per_sq_mi": 231.03,
    "min_20in_area_volume_trillion_gal": 10.08
  },
  "causal_discriminators": {
    "persistent_accumulation": true,
    "large_area_water_volume": true,
    "exposure_density_context": true,
    "short_isolated_downpour_rejected": true
  },
  "interpretation": "Harvey is best represented as persistent extreme rainfall accumulation because the peak, four-day, monthly-record, large-area water-volume, and exposed-footprint metrics reinforce the same flood pathway."
}
```

# Key Computations

The package report provides the rainfall and footprint anchors: peak storm rainfall `48.20 in`, Houston Hobby August 26-29 rainfall `35.6 in`, Houston August rainfall `39.11 in`, previous wettest Houston month `19.21 in`, `6.7 million` people receiving at least 20 inches, and `29,000 sq mi` receiving at least 20 inches.

Derived values:

- `peak_to_20in_ratio = 48.20 / 20 = 2.41`
- `hobby_4day_mean_in_per_day = 35.6 / 4 = 8.90`
- `hobby_total_to_20in_ratio = 35.6 / 20 = 1.78`
- `houston_month_record_ratio = 39.11 / 19.21 = 2.04`
- `exposed_density_per_sq_mi = 6,700,000 / 29,000 = 231.03`
- `min_20in_area_volume_trillion_gal = 20 * 29,000 * 17,378,742.857 / 1e12 = 10.08`

# Reasoning Path

The graph starts with rainfall forcing, not impacts. The peak rainfall node shows extreme intensity, but the four-day Hobby total and monthly-record ratio show persistence. The 20-inch footprint converts that persistence into a minimum water-volume node, and the population-density node is a receptor context inside the heavy-rain footprint. The short isolated downpour alternative fails because the four-day, monthly, and area-volume metrics all remain large.

# Scoring Rubric

- 3 points: Returns the requested JSON with `label`, `causal_graph`, `key_values`, `causal_discriminators`, and `interpretation`.
- 4 points: Computes all six required numeric values within rounding tolerance.
- 4 points: Builds a directed graph that separates trigger, amplifier, receptor, and rejected-alternative nodes.
- 3 points: Correctly explains why persistent accumulation and area volume defeat the isolated-downpour framing.
- 3 points: Uses the exposed-density value as receptor context rather than as the physical rainfall trigger.
- 2 points: Gives `persistent_extreme_rainfall_accumulation` as the final label.
- 1 point: Keeps the answer bounded to computed rainfall, volume, and receptor evidence.
