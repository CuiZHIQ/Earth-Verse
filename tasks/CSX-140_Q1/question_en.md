# Atacama Desert Rainfall-Pulse Ledger

During 24-26 March 2015, a rare storm affected northern Chile's Atacama Desert, with severe flooding reported around Chanaral and Copiapo. A hydrometeorology review team is checking whether the event passes a compact rainfall-pulse test.

Using the incident record and quantitative diagnostics, compute this ledger:

- `annual_equiv_ratio = Antofagasta one-day rainfall / Antofagasta typical annual rainfall`
- `peak_accumulation_mm = max(package gridded event-window precipitation peak summaries)`
- `product_peak_support_count = count of package gridded event-window precipitation peak summaries at or above 30 mm`
- `homes_affected_at_least = homes swept away + homes severely damaged`

Apply this rule: classify the event as `arid_pulse_confirmed` only if `annual_equiv_ratio >= 10`, `peak_accumulation_mm >= 30`, and `product_peak_support_count >= 2`.

Return compact JSON:

```json
{
  "classification": "<arid_pulse_confirmed|not_confirmed>",
  "annual_equiv_ratio": <number>,
  "reported_one_day_mm": <number>,
  "peak_accumulation_mm": <number>,
  "product_peak_support_count": <integer>,
  "threshold_passes": {
    "annual_ratio": <true|false>,
    "peak_accumulation": <true|false>,
    "product_support": <true|false>
  },
  "impact_anchor": {
    "killed_at_least": <integer>,
    "missing": <integer>,
    "homes_affected_at_least": <integer>
  },
  "check_sentence": "<one sentence tying the numeric tests to the classification>"
}
```
