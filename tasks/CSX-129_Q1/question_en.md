# Hurricane Ian Point-and-Box Consistency Ledger

During Hurricane Ian's September 23-30, 2022 Florida landfall period, a tropical-cyclone analytics team is checking whether a severe point weather signal can be reconciled with a compact mapped box that is far from Florida. Compute a five-row proof ledger that keeps the Florida point intensity calculation separate from the remote mapped context.

Return only JSON. Each ledger row must include a formula or boolean test, computed values with units or unit-implied field names, the threshold or test used, a pass or reject result, and a compact interpretation. The answer must not convert remote-box population, feature, image, or surge-layer checks into Ian-wide loss counts or observed surge impacts.

```json
{
  "target_family": "ian_landfall_point_signal_remote_box_consistency_ledger",
  "consistency_ledger": [
    {"row_id": "florida_point_landfall_signal", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": "", "interpretation": ""},
    {"row_id": "daily_power_crosscheck", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": "", "interpretation": ""},
    {"row_id": "mapped_box_distance_check", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": "", "interpretation": ""},
    {"row_id": "bounded_precip_ratio_check", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": "", "interpretation": ""},
    {"row_id": "image_exposure_transfer_check", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": "", "interpretation": ""}
  ],
  "failed_transfers": [
    {"transfer_id": "", "calculation_or_test": "", "decision": ""}
  ],
  "final_consistency_label": ""
}
```
