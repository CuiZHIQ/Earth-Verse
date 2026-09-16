# Expert Error Attribution: Compound Heat Diagnosis Stress Test

A benchmark auditor proposes this CSX-003 diagnosis:

> "Classify the 2022 China heat wave and drought as dominated by moist-heat stress because the package heat archive reaches an estimated 30 C wet-bulb threshold."

Audit the proposed diagnosis and attribute the error. Use only CSX-003 package-local evidence. Do not use web search, hidden answers, or invented values. All paths in the answer must be package-relative.

Required method:

1. Use the locked event window from the package anchor.
2. From the Open-Meteo archive, compute inside that window:
   - the longest consecutive run where `temperature_2m_max >= 35 C`, `temperature_2m_min >= 28 C`, and `apparent_temperature_max >= 40 C`;
   - the peak daily `apparent_temperature_max`, rounded to 0.1 C;
   - the number of hourly records whose Stull-estimated wet-bulb temperature is `>= 30 C`, using hourly `temperature_2m` and `relative_humidity_2m`.
3. Treat a moist-heat-only diagnosis as insufficient unless the count of hourly records with wet-bulb `>= 30 C` reaches at least 24 hours inside the locked window.
4. Use the strongest package report evidence for Poyang Lake or related water-system stress.
5. Reject at least one insufficient alternative source basis with a package-relative path and a numeric or source-path reason.

Return only compact JSON with this schema:

```json
{
  "answer_type": "expert_error_attribution",
  "corrected_classification": "short_label",
  "error_attribution": {
    "error_class": "short_error_label",
    "rejected_counterfactual": "short_label",
    "wrong_operation": "short statement",
    "correct_operation": "short statement"
  },
  "evidence_basis": {
    "event_window": {
      "path": "package-relative/path",
      "start": "YYYY-MM-DD",
      "end": "YYYY-MM-DD",
      "daily_records": 0,
      "hourly_records": 0
    },
    "heat_source": {
      "path": "package-relative/path",
      "compound_run_days": 0,
      "compound_run_start": "YYYY-MM-DD",
      "compound_run_end": "YYYY-MM-DD",
      "peak_apparent_temp_c": 0.0,
      "peak_apparent_temp_date": "YYYY-MM-DD"
    },
    "humidity_check": {
      "path": "package-relative/path",
      "wet_bulb_ge_30_hours": 0,
      "max_wet_bulb_c": 0.0,
      "max_wet_bulb_time": "YYYY-MM-DDTHH:MM",
      "humid_heat_duration_threshold_hours": 24
    },
    "water_stress_report": {
      "path": "package-relative/path",
      "role": "direct_event_context",
      "matched_terms": ["term"]
    }
  },
  "calculation_check": {
    "compound_heat_rule": "short rule",
    "wet_bulb_formula": "short formula label",
    "humid_heat_shortfall_hours": 0,
    "apparent_minus_wet_bulb_peak_c": 0.0
  },
  "insufficient_alternatives": [
    {
      "basis": "short rejected basis",
      "paths": ["package-relative/path"],
      "reason_code": "insufficient_duration|weak_context|wrong_measurement_type",
      "numeric_or_path_reason": "short reason"
    }
  ],
  "minimal_required_paths": ["package-relative/path"],
  "final_assessment": "one sentence"
}
```
