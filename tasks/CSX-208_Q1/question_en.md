# Australian Bushfire Air-Smoke-Fire Consistency Ledger

A technical review is checking whether the 2019-2020 Australian bushfire smoke and hazardous air-quality episode is numerically consistent with a compound fire-smoke-air hazard label.

Build a calculation-led threshold ledger with these row IDs:

- `hot_dry_fire_weather`
- `rainfall_suppression`
- `wind_smoke_transport`
- `smoke_report_anchor`
- `burn_fire_context`
- `direct_loss_guardrail`

Use these tests:

- `hot_dry_fire_weather`: `heat_load_c_days = sum(max(Tmax - 35 C, 0))` over the available early-season daily diagnostic segment since 2019-09-01; the row passes if `max_temperature_c >= 40` and `heat_load_c_days >= 25`.
- `rainfall_suppression`: the row passes if both local daily precipitation totals are `<= 1 mm` and both gridded event-mean precipitation values are `< 5 mm`.
- `wind_smoke_transport`: convert any wind speed in m/s to km/h before comparing; the row passes if the maximum available 10 m wind speed is `>= 25 km/h`.
- `smoke_report_anchor`: count the required air-quality text anchors `fires`, `smoke`, and `southeastern australia`; the row passes if all three are present.
- `burn_fire_context`: compute `fire_context_score = I(dNBR_max >= 0.4) + I(dNBR_mean >= 0.03) + I(annual_embedding_change_mean >= 0.02) + I(report_fire_smoke_context_count >= 5)`; the row passes if `fire_context_score >= 3`.
- `direct_loss_guardrail`: compute `direct_loss_support_flag = I(local humanitarian report count > 0)`; the guardrail passes when the flag is `0`, meaning receptor layers are context rather than observed-loss measurements.

Score one point for each passing row. If the total score is at least 5, return `compound_fire_smoke_air_hazard_consistent`; otherwise return `insufficient_fire_smoke_air_consistency`. Keep the final interpretation to the computed hazard label.

Return valid JSON in this shape:

```json
{
  "target_family": "australia_bushfire_air_smoke_fire_consistency_ledger",
  "ledger": [
    {
      "row_id": "hot_dry_fire_weather",
      "formula": "",
      "computed_values": {},
      "threshold_or_test": "",
      "result": ""
    },
    {
      "row_id": "rainfall_suppression",
      "formula": "",
      "computed_values": {},
      "threshold_or_test": "",
      "result": ""
    },
    {
      "row_id": "wind_smoke_transport",
      "formula": "",
      "computed_values": {},
      "threshold_or_test": "",
      "result": ""
    },
    {
      "row_id": "smoke_report_anchor",
      "formula": "",
      "computed_values": {},
      "threshold_or_test": "",
      "result": ""
    },
    {
      "row_id": "burn_fire_context",
      "formula": "",
      "computed_values": {},
      "threshold_or_test": "",
      "result": ""
    },
    {
      "row_id": "direct_loss_guardrail",
      "formula": "",
      "computed_values": {},
      "threshold_or_test": "",
      "result": ""
    }
  ],
  "score": 0,
  "final_label": "",
  "rejected_alternatives": []
}
```
