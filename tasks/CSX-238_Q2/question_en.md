# Christchurch Ground-Failure Numeric Ledger

Use the local CSX-238 package for the 22 February 2011 Christchurch earthquake. Build a calculation-only ledger from the structured earthquake record and its ground-failure product.

Compute these quantities:

1. `pop_ratio = liquefaction_population_alert_value / landslide_population_alert_value`
2. `hazard_ratio = liquefaction_hazard_alert_value / landslide_hazard_alert_value`
3. `bound_floor = min(liquefaction_population_1std_lower / landslide_population_1std_upper, liquefaction_hazard_1std_lower / landslide_hazard_1std_upper)`
4. `alert_gap = rank(liquefaction_alert) - rank(landslide_alert)`, using `green=0`, `yellow=1`, `orange=2`, `red=3`
5. `dominance_score = log10(pop_ratio) + log10(hazard_ratio) + alert_gap`
6. `shaking_index = max(MMI, CDI) / hypocentral_depth_km`

Set `answer` to `liquefaction_led_ground_failure` only when `pop_ratio >= 25`, `hazard_ratio >= 10`, `bound_floor >= 10`, `alert_gap >= 1`, and `dominance_score >= 3.5`; otherwise use `not_liquefaction_led_ground_failure`.

Round all non-integer numeric results to three decimals. Return only compact JSON:

```json
{
  "answer": "",
  "pop_ratio": 0.0,
  "hazard_ratio": 0.0,
  "bound_floor": 0.0,
  "alert_gap": 0,
  "dominance_score": 0.0,
  "shaking_index": 0.0
}
```
