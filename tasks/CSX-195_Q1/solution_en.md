# Final Answer

```json
{
  "event_days": 13,
  "image_to_height_lag_days": 2,
  "altitude_margin_km": 3,
  "transport_signal_count": 6,
  "transport_score": 4,
  "surface_score": 1,
  "score_gap": 3,
  "final_label": "upper_air_smoke_transport_pass"
}
```

# Key Computations

The incident window is 2019-12-29 through 2020-01-10. Inclusive duration is:

`2020-01-10 - 2019-12-29 + 1 = 13 days`

The natural-color image anchor is January 4, 2020. The smoke-height anchor is January 6, 2020, so:

`image_to_height_lag_days = 2020-01-06 - 2020-01-04 = 2`

The companion report gives smoke height as 15 to 19 km on January 6. Against a 12 km upper-air threshold:

`altitude_margin_km = 15 - 12 = 3`

The six transport signals all evaluate true:

- January 4 image context is present.
- The report distinguishes tan smoke.
- The report uses pyrocumulonimbus wording.
- December 29 and January 4 fire-cloud dates are both present.
- Pacific transport and New Zealand wording are both present.
- Snow-darkening and more-than-halfway global travel wording are both present.

Therefore `transport_signal_count = 6`.

Transport score:

- duration between 10 and 16 days: pass.
- image-to-height lag no more than 2 days: pass.
- altitude margin at least 0 km: pass.
- at least 5 transport signals: pass.

`transport_score = 4`

Surface comparison score:

- mean burn-index proxy is 0.236, below the 0.27 threshold: fail.
- mean annual feature-change proxy is 0.026, below the 0.05 threshold: fail.
- the event-dated image date, 2020-01-04, falls within 2019-12-29 through 2020-01-10: pass.

`surface_score = 1`, so `score_gap = 4 - 1 = 3`.

# Reasoning Path

The ledger first fixes the time base. The event lasts 13 inclusive days, which satisfies the 10-16 day duration test. The January 4 image and January 6 height report are only 2 days apart, so the image-to-height bridge also satisfies the timing test.

The height test is decisive in numeric form: the lower end of the reported smoke range is 15 km, which is 3 km above the 12 km upper-air threshold. The report text then contributes six of six transport signals, clearing the minimum count of five.

The comparison ledger does not keep pace: the mean burn-index proxy is below 0.27, the mean annual feature-change proxy is below 0.05, and only the event image date test passes. These surface proxy layers are only a comparison score against the upper-air transport ledger, not proof of an event burn perimeter. The resulting 4 versus 1 score split gives a gap of 3, meeting the rule for `upper_air_smoke_transport_pass`.

# Computed Interpretation

The computed ledger passes all four upper-air smoke transport tests while the local surface-change comparison passes only one of three, so the compact classification is `upper_air_smoke_transport_pass`.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns exactly the requested eight-key compact JSON ledger with integer counts and the final label. Partial credit: 1-2 points for a mostly correct structure with one or two missing or renamed fields; 0 points for prose-only output.
- 4 points: Computes the time-window values correctly: 13 inclusive event days and 2 image-to-height lag days. Partial credit: 2 points for one correct value; 1 point for exclusive-date arithmetic that is otherwise traceable.
- 3 points: Computes the altitude threshold test correctly: minimum height 15 km, 12 km threshold, and 3 km margin. Partial credit: 1-2 points for using the right altitude range but the wrong margin or threshold comparison.
- 3 points: Counts the six transport signals correctly and applies the at-least-5 rule. Partial credit: 1-2 points for recognizing most signals but missing a paired wording test.
- 3 points: Computes `transport_score = 4` from the four pass/fail tests. Partial credit: 1-2 points for correct tests with an arithmetic or threshold error.
- 2 points: Computes `surface_score = 1` from the two failed surface proxy thresholds and the event-image date pass, while treating surface proxies as comparison evidence rather than burn-perimeter proof. Partial credit: 1 point for using the right proxy values but the wrong threshold outcome.
- 2 points: Computes `score_gap = 3` and assigns `upper_air_smoke_transport_pass`. Partial credit: 1 point for the right label with a wrong gap, or the right gap with an incorrect label.
