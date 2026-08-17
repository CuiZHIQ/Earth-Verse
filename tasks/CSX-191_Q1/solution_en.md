# Final Answer

```json
{
  "psi_excess_ratio": 5.714,
  "co_anomaly_ratio": 13.0,
  "resp_cases_per_exposed_million": 11627.907,
  "service_markers_per_100k": 9.937,
  "threshold_pass_count": 4,
  "final_label": "smoke_threshold_confirmed"
}
```

# Key Computations

The incident window is 2015-08-01 to 2015-11-30 for the 2015 Southeast Asia haze linked to Indonesian fires. The ledger uses four deterministic threshold tests.

1. PSI excess: the report says PSI rose above 2000 in parts of southern Sumatra and Borneo, and that any score above 350 is hazardous. Using 2000 and 350 as benchmark anchors gives `2000 / 350 = 5.714285714`, rounded to `5.714`, so the PSI test passes the `>= 5.0` rule.
2. Carbon monoxide anomaly: the report gives a usual average of about 100 ppb and a Borneo surface value up to nearly 1300 ppb in 2015. Using 100 and 1300 as benchmark anchors gives `1300 / 100 = 13.0`, so the carbon monoxide test passes the `>= 10.0` rule.
3. Respiratory-case rate: the report gives about 500000 respiratory-problem cases and says more than 43000000 people were exposed to unusually high smoke levels. Using 43 million as the lower-bound exposure anchor gives `500000 / (43000000 / 1000000) = 11627.9069767` cases per exposed million, rounded to `11627.907`, so the benchmark rate test passes the `>= 10000` rule.
4. Local service-marker density: the local mapped context contains 26 schools, 5 hospitals, 6 police amenities, 1 fire station, and 19 shelters. The service-marker count is `26 + 5 + 6 + 1 + 19 = 57`. With a local population sum of `573590.9458804413`, the rate is `57 / 573590.9458804413 * 100000 = 9.937395353`, rounded to `9.937`, so the package-derived receptor-context density test passes the `>= 8.0` rule. This is not an event-time facility-impact count.

# Reasoning Path

The first two tests check whether the smoke record clears severity thresholds rather than relying on a single descriptive phrase. The PSI ratio is more than five times the hazardous threshold, and the carbon monoxide ratio is thirteen times the usual average. Those two pass flags establish that the smoke indicators are numerically extreme.

The third test converts reported respiratory-problem cases and reported high-smoke exposure into a rate. Using exposed people in millions prevents the case count from being interpreted without a denominator. The computed rate, `11627.907` cases per exposed million, clears the stated threshold.

The fourth test converts package-derived local receptor-context counts into a population-normalized service-marker density. The calculation uses only the specified service categories and the local population sum. The resulting `9.937` markers per 100000 residents clears the stated threshold, but it remains a receptor-density measure rather than an event-time service status or a count of harmed facilities.

All four threshold tests pass. Because the final rule requires at least three passes, the final label is `smoke_threshold_confirmed`.

# Computed Interpretation

The ledger supports a severe regional smoke-loading diagnosis with high pollutant ratios, a high reported respiratory-case rate per exposed million, and dense local service receptors; it does not require adding any broader casualty or facility-damage inference.

# Scoring Rubric

Total: 20 points

- 4 points: Final JSON and label. Full credit returns the six requested fields and the final label `smoke_threshold_confirmed` with `threshold_pass_count` equal to 4. Partial credit: 2 points for the correct label with missing or malformed fields; 1 point for a plausible threshold result with the wrong pass count.
- 4 points: PSI and carbon monoxide ratios. Full credit computes benchmark-anchor ratios `2000 / 350 = 5.714` and `1300 / 100 = 13.0`, with correct rounding and pass states. Partial credit: 2 points for one correct ratio and pass state; 3 points for both ratios with minor rounding or unit wording errors.
- 3 points: Respiratory-case rate. Full credit computes the benchmark rate `500000 / 43 = 11627.907` cases per exposed million from the report's case anchor and exposed-population lower-bound anchor, then marks the test as passed. Partial credit: 1-2 points for using the correct inputs but dividing by total people rather than millions, rounding poorly, or omitting the pass comparison.
- 3 points: Local service-marker density. Full credit sums the package-derived service-context markers to 57, divides by `573590.9458804413`, multiplies by 100000, obtains `9.937`, and marks the context-density test as passed without treating markers as event-time facility impacts. Partial credit: 1 point for the correct marker sum only; 2 points for the correct rate with a minor category or rounding error.
- 3 points: Threshold arithmetic. Full credit applies the four thresholds exactly and derives the final rule from at least three passing tests. Partial credit: 1-2 points for correct arithmetic with one threshold comparison or final-rule mistake.
- 2 points: Computed interpretation. Full credit gives a concise interpretation tied to the four computed values and avoids turning the local service counts into confirmed facility harm. Partial credit: 1 point for a mostly numeric answer with a vague or overstated interpretation.
- 1 point: Concise answer format. Full credit keeps the answer compact and uses the requested field names. Partial credit: 0.5 points for a correct answer embedded in unnecessary prose.
