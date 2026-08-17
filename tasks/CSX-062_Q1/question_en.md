# Western Europe Flood Rainfall-Runoff Process Chain

You are a basin flood-process analyst reconstructing the July 2021 Western Europe floods in western Germany and eastern Belgium. The task is to build a process chain from 48-hour area rainfall to rapid runoff and then to station-scale amplification.

Use only the local CSX-062 event package. Select package-relative evidence for area rainfall, runoff fraction, and station-total comparisons.

Compute:

- `area_48h_rain_mm`;
- `runoff_depth_range_mm` from the documented rapid-runoff fraction;
- `station_to_area_ratios` for Jalhay, Spa, and the German minimum station total.

Then express the result as an ordered chain:

1. regional 48-hour rainfall input;
2. rapid-runoff conversion;
3. local station amplification;
4. final hydrologic process label.

Return compact JSON with exactly these fields:

```json
{
  "target_family": "western_europe_rainfall_runoff_process_chain",
  "process_chain": [
    {"stage": "regional_rainfall_input", "computed_values": {}, "process_role": ""},
    {"stage": "rapid_runoff_conversion", "computed_values": {}, "process_role": ""},
    {"stage": "station_scale_amplification", "computed_values": {}, "process_role": ""},
    {"stage": "flood_process_label", "computed_values": {}, "process_role": ""}
  ],
  "area_48h_rain_mm": 0,
  "runoff_depth_range_mm": [0, 0],
  "station_to_area_ratios": {
    "jalhay": 0,
    "spa": 0,
    "german_min": 0
  },
  "gate_results": {
    "runoff_load_pass": false,
    "station_amplification_pass": false
  },
  "answer": "..."
}
```

Use `rapid_runoff_load_pass` only when the lower runoff-equivalent depth is at least 20 mm and at least two station totals are at least twice the area-rain total. Round depths and ratios to two decimals and add the process meaning inside the chain rather than as a broad narrative.
