# Free State Severe-Storm Impact Ledger

During the 6 December 2023 severe thunderstorms and hail event in South Africa's Free State Province, a climate-risk analyst needs a compact ledger that compares residential and public-building harm with storm-linked electrical infrastructure disruption. Reconstruct the ledger from the technical record and decide whether the shelter-utility threshold is met.

Use these definitions:

- `reported_houses` = damaged or roof-loss houses reported for Bloemfontein, Dewetsdorp, Madikgetla, and Bohlokong.
- `residential_structures` = `reported_houses` + affected residential shacks.
- `public_cbd_assets` = damaged stadiums + damaged church + damaged school + Mangaung CBD building with roof loss.
- `utility_substations` = electrical power supply substations or feeders struck by lightning.
- `qualitative_pathways` = the count of present but unquantified pathways among street or road flooding, residential flooding, crop damage, and vegetation or tree damage.
- `shelter_index = 100*fatalities + 25*hospital_admissions + residential_structures + 10*public_cbd_assets`.
- `utility_index = 15*utility_substations + 20` when the same storm record links storm or lightning damage to power-supply loss or affected electrical infrastructure; otherwise omit the `+20`.
- The threshold is met only when `shelter_index >= 4*utility_index`, `residential_structures >= 300`, and `public_cbd_assets >= 5`.

Return compact JSON with this shape and no narrative outside the JSON:

```json
{
  "counts": {
    "fatalities": 0,
    "hospital_admissions": 0,
    "reported_houses": 0,
    "residential_structures": 0,
    "public_cbd_assets": 0,
    "utility_substations": 0,
    "qualitative_pathways": 0
  },
  "indices": {
    "shelter_index": 0,
    "utility_index": 0,
    "shelter_utility_ratio": 0.0,
    "threshold_margin": 0
  },
  "threshold_met": false,
  "class_label": ""
}
```
