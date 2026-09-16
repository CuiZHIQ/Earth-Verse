# Super Typhoon Yagi Rainfall-Impact Ratio Ledger

During 7-18 September 2024, Super Typhoon Yagi produced flooding and landslides across northern Viet Nam, Laos, Thailand, and Myanmar. A technical review team needs a compact ratio ledger to test whether the storm-window rainfall signal, timing, reported regional impacts, local denominator checks, and surface-change metrics support a rainfall-dominant regional flood/landslide classification.

Return compact JSON with this shape:

```json
{
  "target_family": "yagi_rainfall_impact_ratio_ledger",
  "row_results": {
    "rainfall_load": "",
    "rainfall_concentration": "",
    "wind_context": "",
    "regional_impact_ratios": "",
    "local_denominator_test": "",
    "surface_change_metric_role": ""
  },
  "core_values": {},
  "rejected_scaling": [],
  "final_label": "",
  "interpretation": ""
}
```

Use formulas or inequalities for each row. Include the main numeric values with units or unit-implied field names, mark each row as `pass`, `context_only`, or `reject_scaling`, and keep the interpretation to one sentence tied directly to the computed values.
