# Local Cyclone Gonu Numeric Consistency Ledger

A Muscat hydrometeorology analyst is reviewing Cyclone Gonu, which affected Oman and the Arabian Sea during 1-7 June 2007. The local question is whether the Muscat record is consistent with a land-stage coastal-wadi cyclone signal, or whether it should be treated as if the offshore cyclone-core intensity occurred at the local point.

Build a compact JSON ledger from the technical record. Keep the answer numeric and concise, and use these five rows:

- `rainfall_concentration`
- `wind_pressure_signature`
- `official_local_contrast`
- `precip_product_contrast`
- `receptor_density_check`

Return JSON with this structure:

```json
{
  "target_family": "gonu_muscat_land_stage_numeric_consistency_ledger",
  "ledger": [
    {
      "row_id": "rainfall_concentration",
      "formulae": [],
      "values": {},
      "verdict": ""
    }
  ],
  "final_label": "",
  "failed_label": ""
}
```

Use formulas and values in each row. The final label should be a compact classification of the local Muscat signal, and the failed label should name the numerically weaker alternative.
