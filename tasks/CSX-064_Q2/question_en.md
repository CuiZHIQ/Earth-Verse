# Monsoon-Flood Scenario Sensitivity Ranking

A hydrometeorology team is stress-testing the July 2020 South and East Asia monsoon-flood diagnosis. The baseline diagnosis is `persistent_monsoon_rainfall_with_routed_flooding`. Your task is to rank plausible scenario perturbations by how much each one could change that diagnosis.

Use only the local CSX-064 event package evidence. Select package-relative evidence for each physical hazard, timing, precipitation, wind, and process claim you use.

Return one compact JSON object with this top-level structure:

```json
{
  "answer": "scenario_name",
  "target_family": "monsoon_flood_scenario_sensitivity_ranking",
  "computed_values": {},
  "scenario_scores": {},
  "ranked_scenarios": [],
  "top_sensitivity": {},
  "rejected_sensitivity": {},
  "evidence_paths": {},
  "reasoning_path": []
}
```

Rank these candidate perturbations, using the names exactly as written:

- `weaker_three_product_rainfall_load`
- `loss_of_product_coherence`
- `report_anchor_dropout`
- `peak_burst_reinterpretation`
- `shortened_monsoon_window`
- `wind_led_reinterpretation`

Compute the baseline evidence first:

- Inclusive event-window duration in days.
- Three event-total precipitation means and maxima from the available precipitation products.
- Three-product mean precipitation, minimum product mean, event-mean daily rate, product mean spread, spread-to-mean ratio, GPM-to-CHIRPS mean ratio, largest product maximum, and largest-maximum-to-three-product-mean ratio.
- Report anchors for excessive monsoon rains, severe South and East Asia flooding, Assam disruption or displacement, China river and lake swelling with Poyang Lake at 22.6 m on July 13, Japan floods or landslides, Nepal mention, and stationary monsoon systems.
- Wind proxies `sqrt(u10_max^2 + v10_max^2)` and `sqrt(u10_mean^2 + v10_mean^2)`.

Use this deterministic sensitivity rule: for each candidate, compute the fractional perturbation needed to cross the competing-diagnosis threshold, then score it as `max(0, 100 * (1 - fractional_change_needed))`. Higher score means the diagnosis is more sensitive to that perturbation. Round scenario scores and `change_to_threshold` values to three decimals. In `computed_values`, use integers for counts/days, three decimals for millimetre and daily-rate values, three decimals for `spread_ratio`, and two decimals for ratio summaries and wind proxies.

Use `evidence_paths` as an object whose keys are evidence roles and whose values are arrays of package-relative paths. Include at least `event_window`, `report_anchors`, `precipitation_products`, and `wind_proxy`.

Candidate threshold rules:

- `weaker_three_product_rainfall_load`: the fractional uniform rainfall reduction needed for any product event-total mean to fall below `250 mm`.
- `loss_of_product_coherence`: the smaller fractional change needed either to push the GPM-to-CHIRPS mean ratio to `1.25` or to push the spread-to-mean ratio to `0.20`.
- `report_anchor_dropout`: the loss of one required report anchor from the count of required anchors found.
- `peak_burst_reinterpretation`: the fractional increase in the largest product maximum needed for the maximum-to-mean ratio to reach `2.0`.
- `shortened_monsoon_window`: the fraction of event days that must be removed so the remaining duration falls below a `21` day persistence window.
- `wind_led_reinterpretation`: the fractional increase in the maximum wind proxy needed to reach `10 m/s`.

The final ranking should identify the top sensitivity and the perturbation that remains least plausible as a diagnosis-changing alternative.
