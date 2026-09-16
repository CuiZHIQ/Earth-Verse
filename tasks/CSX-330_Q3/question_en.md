# Coral Bleaching Rescue Clock Under Degree-Heating Stress

You are advising a coral-response team during the 2023 Florida Keys marine heatwave. The package contains a NOAA-style event report, event metadata, population and road/bridge context, and remote-sensing summaries.

Build a thermal-clock and rescue-priority model. Convert the sea-surface-temperature exceedance above the bleaching threshold into Degree Heating Week timing, compare that clock with the threshold-to-peak interval, and connect the result to coral rescue logistics.

Use only package-local files and cite package-relative paths. Return JSON with exactly these top-level fields:

```json
{
  "answer": "<short snake_case label>",
  "source_files_used": ["<package-relative path>", "..."],
  "thermal_threshold_clock": {},
  "dhw_escalation": {},
  "ecological_and_rescue_context": {},
  "coastal_logistics_context": {},
  "priority_model": {},
  "recommended_reasoning_path": ["..."]
}
```

The final reasoning must explain why the crisis is governed by accumulated heat stress and rescue timing, not only by a peak SST value.
