# Final Answer

Correct answer: `rapid_runoff_load_pass`.

```json
{
  "target_family": "western_europe_rainfall_runoff_process_chain",
  "process_chain": [
    {
      "stage": "regional_rainfall_input",
      "computed_values": {"area_48h_rain_mm": 104},
      "process_role": "A 48-hour basin-scale rainfall load supplies the regional hydrologic input."
    },
    {
      "stage": "rapid_runoff_conversion",
      "computed_values": {"runoff_fraction_range": [0.20, 0.25], "runoff_depth_range_mm": [20.8, 26.0]},
      "process_role": "The documented rapid-runoff fraction converts the rainfall field into at least 20.8 mm of fast runoff depth."
    },
    {
      "stage": "station_scale_amplification",
      "computed_values": {"station_to_area_ratios": {"jalhay": 2.61, "spa": 2.09, "german_min": 1.44}},
      "process_role": "Two Belgian station totals exceed twice the area rainfall, showing local amplification on top of the regional input."
    },
    {
      "stage": "flood_process_label",
      "computed_values": {"runoff_load_pass": true, "station_amplification_pass": true},
      "process_role": "The combined rainfall-runoff and station-amplification evidence supports the rapid runoff-load process label."
    }
  ],
  "area_48h_rain_mm": 104,
  "runoff_depth_range_mm": [20.8, 26.0],
  "station_to_area_ratios": {
    "jalhay": 2.61,
    "spa": 2.09,
    "german_min": 1.44
  },
  "gate_results": {
    "runoff_load_pass": true,
    "station_amplification_pass": true
  },
  "answer": "rapid_runoff_load_pass"
}
```

# Key Computations

The 48-hour area rainfall is `104 mm`. Applying the documented rapid-runoff fraction gives:

```text
104 * 0.20 = 20.8 mm
104 * 0.25 = 26.0 mm
```

Station-to-area ratios are:

```text
Jalhay: 271 / 104 = 2.61
Spa: 217 / 104 = 2.09
German lower bound: 150 / 104 = 1.44
```

# Reasoning Path

The process chain starts with regional rainfall, converts it to fast runoff depth, then checks whether station totals show local amplification. The lower runoff-equivalent depth is already at least `20 mm`, and exactly two station ratios exceed `2.0`. Both gates pass, so the answer is `rapid_runoff_load_pass`.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested JSON shape with target family, four process-chain stages, gate results, and final answer. Partial credit for the right answer with one missing stage.
- 4 points: Extracts the correct input values and 48-hour context: `104 mm`, 20-25 percent runoff fraction, `271 mm` Jalhay, `217 mm` Spa, and at least `150 mm` German station total. Partial credit for three or four correct inputs.
- 4 points: Computes `[20.8, 26.0] mm` runoff depth correctly and compares the lower bound to the 20 mm rule. Partial credit for the correct formula with minor rounding error.
- 3 points: Computes station ratios `2.61`, `2.09`, and `1.44`, and counts two ratios above `2.0`. Partial credit for two correct ratios.
- 3 points: Explains the ordered rainfall input -> rapid runoff -> station amplification process rather than giving only a final label. Partial credit for correct gates without process ordering.
- 2 points: Rejects a ponding-only or image-led interpretation by grounding the answer in rainfall conversion and station amplification. Partial credit for one bounded rejection.
- 1 point: Keeps the answer concise and does not add uncomputed loss or response claims.
