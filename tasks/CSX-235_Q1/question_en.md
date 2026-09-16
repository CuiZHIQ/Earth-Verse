# Palu Coupled Hazard-Chain Score

A technical review team is checking the 28 September 2018 Sulawesi earthquake and tsunami near Palu, Central Sulawesi. The task is to prove numerically whether the incident record fits a coupled geophysical hazard-chain pattern rather than a rainfall-led, image-only, or single-driver reading.

Compute the normalized terms below from the incident record:

- `S`: mean of capped magnitude, shaking intensity, and peak-ground-acceleration terms: `mean(min(M/7.5,1), min(MMI/8,1), min(PGA/0.8,1))`.
- `L`: liquefaction population alert term: `min(liquefaction_alert_population/140000,1)`.
- `W`: coastal wave term: `min(wave_height_m/7,1)`.
- `P`: mapped population term: `min(population/500000,1)`.
- `F`: mapped facility term: `min((schools+hospitals+healthcare+bridges)/40,1)`.
- `H`: reported human-impact term: `min(((killed/2000)+(displaced/200000))/2,1)`.
- `C`: surface-change context term: `min(mean_embedding_change/0.10,1)`.
- `R`: rainfall context deduction term: `min(mean(GPM_mean_mm,CHIRPS_mean_mm)/25,1)`.

Use:

`score = 100 * (0.20*S + 0.18*L + 0.14*W + 0.14*P + 0.12*F + 0.15*H + 0.07*C - 0.05*R)`

Threshold rules:

- The seven positive terms pass at `S>=0.95`, `L>=0.95`, `W>=0.95`, `P>=0.75`, `F>=0.75`, `H>=0.95`, and `C>=0.50`.
- The rainfall context term passes as non-dominant when `R<0.25`.
- Set `final_label` to `coupled_geophysical_high_consistency` only when `score>=85`, at least six positive terms pass, and `R<0.25`; otherwise use `not_high_consistency_by_this_score`.

Return JSON only:

```json
{
  "component_ledger": [
    {"term": "S", "value": 0, "threshold_result": ""},
    {"term": "L", "value": 0, "threshold_result": ""},
    {"term": "W", "value": 0, "threshold_result": ""},
    {"term": "P", "value": 0, "threshold_result": ""},
    {"term": "F", "value": 0, "threshold_result": ""},
    {"term": "H", "value": 0, "threshold_result": ""},
    {"term": "C", "value": 0, "threshold_result": ""},
    {"term": "R", "value": 0, "threshold_result": ""}
  ],
  "score": 0,
  "positive_terms_passing": 0,
  "final_label": "",
  "rejected_readings": []
}
```
