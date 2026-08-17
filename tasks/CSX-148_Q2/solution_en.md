# Final Answer

The correct answer is the threshold-met ledger:

```json
{
  "counts": {
    "fatalities": 1,
    "hospital_admissions": 3,
    "reported_houses": 292,
    "residential_structures": 342,
    "public_cbd_assets": 5,
    "utility_substations": 7,
    "qualitative_pathways": 4
  },
  "indices": {
    "shelter_index": 567,
    "utility_index": 125,
    "shelter_utility_ratio": 4.536,
    "threshold_margin": 67
  },
  "threshold_met": true,
  "class_label": "shelter_utility_threshold_met"
}
```

# Key Computations

The national government storm record for the Free State event reports one fatality and three hospital admissions. The house-damage ledger is built from four place-specific counts: 16 houses with roofs blown off in Bloemfontein, 24 damaged houses in Dewetsdorp, 2 houses with roofs blown off in Madikgetla, and 250 damaged residential houses in Bohlokong. These add to `reported_houses = 16 + 24 + 2 + 250 = 292`.

The same record states that 50 residential shacks were affected, so `residential_structures = 292 + 50 = 342`. Public and CBD assets are counted as two stadiums, one church, one school, and one Mangaung CBD building with roof loss, giving `public_cbd_assets = 2 + 1 + 1 + 1 = 5`.

For the utility side, lightning struck seven electrical power supply substations or feeders. Because the record links those strikes to power-supply loss and affected electrical infrastructure, the `+20` term applies: `utility_index = 15*7 + 20 = 125`.

The four qualitative pathways are present: street or road flooding, residential flooding, crop damage, and vegetation or tree damage. Therefore `qualitative_pathways = 4`.

The shelter index is:

`shelter_index = 100*1 + 25*3 + 342 + 10*5 = 100 + 75 + 342 + 50 = 567`.

The ratio is `567 / 125 = 4.536` when rounded to three decimals. The threshold margin is `567 - 4*125 = 67`.

# Reasoning Path

The task is deterministic because every requested count is either explicitly stated in the storm record or follows from a fixed arithmetic rule. The residential side first separates ordinary houses from shacks, then recombines them for the shelter index. This avoids double-counting Bohlokong shacks as reported houses while still including them in residential structures.

The public and CBD asset count uses only discrete damaged assets: stadiums, church, school, and the Mangaung CBD roof-loss building. The utility count uses the number of lightning-struck electrical substations or feeders and then applies the fixed power-supply bonus because the same storm record directly connects those strikes to power-supply loss.

All three threshold tests pass. First, `shelter_index >= 4*utility_index` because `567 >= 500`. Second, `residential_structures >= 300` because `342 >= 300`. Third, `public_cbd_assets >= 5` because the count is exactly 5. The final class label is therefore `shelter_utility_threshold_met`, not `threshold_not_met`.

# Computed Interpretation

The computed ledger shows that the recorded residential and public-building burden outweighed the electrical-infrastructure disruption under the specified index rule. The margin is not just a ratio effect: the residential-structure and public/CBD minimums also pass, so the threshold result is robust to the three-part definition.

# Scoring Rubric

Total: 20 points.

- Final threshold ledger (3 points): Full credit for reporting `threshold_met = true` with `class_label = shelter_utility_threshold_met` and no contradictory label. Partial credit: 2 points for the correct boolean without the label, or 1 point for a threshold-met conclusion with incomplete JSON.
- Core report counts (4 points): Full credit for extracting 1 fatality, 3 hospital admissions, 7 utility substations, and the four place-specific house counts. Partial credit: 1 point per correctly extracted group, with no credit for values invented outside the record.
- Residential and public asset arithmetic (3 points): Full credit for `reported_houses = 292`, `residential_structures = 342`, and `public_cbd_assets = 5`. Partial credit: 1 point for each correct derived value.
- Utility and qualitative pathway ledger (3 points): Full credit for `utility_index` inputs of 7 substations plus the power-supply bonus and `qualitative_pathways = 4`. Partial credit: 1 point for the substations, 1 point for applying or explaining the bonus, and 1 point for the four-pathway count.
- Index and margin arithmetic (4 points): Full credit for `shelter_index = 567`, `utility_index = 125`, `shelter_utility_ratio = 4.536`, and `threshold_margin = 67`. Partial credit: 1 point for each correct computed value, allowing a ratio tolerance of 0.001.
- Three-part threshold test (2 points): Full credit for checking all three required inequalities: `567 >= 500`, `342 >= 300`, and `5 >= 5`. Partial credit: 1 point for checking only the shelter-utility inequality or for missing one of the two minimum-count tests.
- Compact output discipline (1 point): Full credit for returning only the requested compact JSON. Partial credit: 0.5 points for a correct ledger with extra prose, and no credit for adding exact hail size, wind gust, flood depth, outage duration, or agricultural area values that are not part of the requested ledger.
