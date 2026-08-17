# Burn-Index Threshold Ledger for the 2023 Canadian Wildfires

During the 2023 Canadian wildfires and smoke episode, a remote-sensing review team is checking a neighborhood-scale burn-index summary. The specific question is whether the dNBR distribution should be treated as a uniform high-severity burn signal, or as a moderate-average distribution with a severe upper tail.

Reconstruct the threshold ledger from the quantitative dNBR statistics. Use these severity bins for the mean dNBR: below 0.00 = `unburned_or_regrowth`; 0.00 to below 0.27 = `low`; 0.27 to below 0.44 = `moderate`; 0.44 to below 0.66 = `high`; 0.66 and above = `very_high`. Use this patchiness rule: `patchy` requires all three tests to pass: `dnbr_cv = dnbr_stddev / abs(dnbr_mean) >= 0.45`, `dnbr_max >= 0.66`, and `dnbr_min < 0.00`. If only one or two tests pass, use `mixed`; if none pass, use `uniform`.

Return compact JSON with rounded values:

```json
{
  "final_label": "<short_label>",
  "severity_class": "<unburned_or_regrowth|low|moderate|high|very_high>",
  "heterogeneity_class": "<uniform|mixed|patchy>",
  "dnbr_mean": <number>,
  "dnbr_max": <number>,
  "dnbr_min": <number>,
  "dnbr_cv": <number>,
  "patchiness_score": "<passed_tests>/3",
  "computed_interpretation": "<one_sentence_threshold_result>"
}
```
