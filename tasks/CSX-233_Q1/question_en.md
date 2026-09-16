# 2024 Noto Peninsula Earthquake Consistency Ledger

Compute a compact numeric ledger for the 2024 Noto Peninsula earthquake that tests whether the recorded source, shaking, coastal, exposure, weather, and surface-change signals are mutually consistent with a high seismic-coastal event signal.

Return a concise JSON object with these fields:

- `event_time_utc`
- `source_intensity_score`
- `coastal_ground_score`
- `context_score`
- `countercheck_penalty`
- `final_score`
- `consistency_class`

Use these rules:

- `source_intensity_score`: add 2 if moment magnitude is at least 7.0, add 2 if maximum MMI is at least 8.0, add 1 if source depth is at most 20 km, and add 1 if the event alert is red.
- `coastal_ground_score`: add 2 if the tsunami flag equals 1, add 2 if liquefaction population exposure is at least 100,000 people, and add 1 if the liquefaction-to-landslide population exposure ratio is at least 100.
- `context_score`: add 1 if the exposed-area population is at least 1,000,000 people, add 1 if finite-fault length is at least 100 km, and add 1 if maximum slip is at least 5 m.
- `countercheck_penalty`: subtract 2 if the larger of the GPM and CHIRPS mean event precipitation values is at least 25 mm, subtract 1 if the absolute mean Sentinel-1 VV change is at least 5 dB, and subtract 1 if the mean annual embedding change is at least 0.10.
- `final_score` equals the three positive scores minus the penalty.
- `consistency_class` is `high_seismic_coastal` for scores of 11 or higher, `mixed_seismic_context` for scores from 7 through 10, and `weak_seismic_context` for scores of 6 or lower.
