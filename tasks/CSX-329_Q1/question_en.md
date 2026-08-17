# Northwest Pacific Reef Heat-Stress Dominance Check

A technical analyst is checking the CSX-329 2020 Northwest Pacific reef event against a deterministic dominance rule for an Alert Level 2 bleaching heat-stress classification. Use the CSX-329 package data to compute the coverage fractions, score ledger, margin, and pass state.

Return JSON only.

```json
{
  "answer": {
    "region_fraction": 0.0,
    "term_fraction": 0.0,
    "scores": {
      "heat": 0,
      "rain": 0,
      "land": 0,
      "later": 0,
      "ceiling": 0
    },
    "margin": 0,
    "precip_ratio": 0.0,
    "land_values": {
      "alpha_mean": 0.0,
      "dnbr_mean": 0.0,
      "dnbr_max": 0.0
    },
    "passes": false,
    "label": "<short computed label>"
  },
  "interpretation": "<one calculation-tied sentence>"
}
```

Use these rules:

- `region_fraction = present(Taiwan, Japan/Ryukyu, South China Sea) / 3`.
- `term_fraction = present(HotSpot, Degree Heating Week, Bleaching Alert Area, 7-day maximum) / 4`.
- `heat = hazard_match + Alert_Level_2 + severity_definition + region_count + term_count`.
- `rain = I(GPM_mean_mm >= 100) + I(CHIRPS_mean_mm >= 100)`.
- `land = I(alpha_mean >= 0.1) + I(dnbr_mean >= 0.2) + I(dnbr_max >= 0.5)`.
- `later = I(Guam_CNMI_warning_current) + I(Guam_Alert_Level_2_later)`.
- `ceiling = max(rain, land, later)` and `margin = heat - ceiling`.
- The check passes only if `region_fraction = 1.0`, `term_fraction = 1.0`, and `margin >= 5`.
- Use `precip_ratio = GPM_mean_mm / CHIRPS_mean_mm`.
