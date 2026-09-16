# Marine Heat-Stress Priority Diagnosis

During the 2023 Florida Keys marine heatwave and coral bleaching emergency, reef managers must decide whether the most defensible response priority is coral rescue and reef-protection triage from accumulated marine heat stress, or whether the event should instead be framed around rainfall-driven terrestrial disruption, broad population displacement, or vegetation/burn-style surface change.

Give a compact structured answer that uses the sea-surface temperature exceedance, the explicit bleaching threshold, the priority exceedance cutoff used for the diagnosis, Degree Heating Week severity thresholds, coral rescue actions, and the main nonpriority checks. Keep the answer bounded to the local package evidence.

Return your answer as:

```json
{
  "answer": "<compact_priority_label>",
  "key_metrics": {
    "peak_sst_c": "<value>",
    "bleaching_threshold_c": "<value>",
    "sst_above_bleaching_threshold_c": "<value>",
    "priority_sst_exceedance_cutoff_c": "<value>",
    "significant_bleaching_dhw_threshold_c_weeks": "<value>",
    "severe_bleaching_dhw_threshold_c_weeks": "<value>",
    "minimum_target_rescue_fragments": "<value>",
    "primary_nonpriority_checks": ["<check>", "<check>"]
  },
  "impact_chain": ["<driver>", "<hazard_index>", "<priority_action>"]
}
```
