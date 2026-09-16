# July 2023 Northern Italy Severe Hailstorms

A severe-storm climatology team is preparing a technical note on the July 2023 northern Italy hail outbreak, centered on the late-evening Azzano Decimo hail report. Compute a threshold and context ledger that checks whether the reported hail size, timing, location, precipitation context, population context, and image timing are mutually consistent with one compact event record.

Return only a compact JSON object with these fields:

- `answer`: the final consistency label.
- `hail_thresholds`: confirmed hailstone size in cm, severe-hail threshold ratio, giant-hail threshold ratio, previous European record ratio, and gap to the cited world-record comparison in cm.
- `event_match`: reported place, local hit time normalized to date plus about-23:00, and boolean checks for date-in-window and Italy match.
- `context_metrics`: GPM maximum accumulated precipitation in mm, ERA5-Land maximum precipitation sum in mm, and rounded 2020 WorldPop population.
- `remote_sensing_check`: AlphaEarth annual mean and maximum change, RGB mean absolute difference between the two true-color images, the event-image lead time in days relative to the reported hit, and whether the event image is post-hit.
- `final_score`: passed checks, total checks, percent score, and the same final label as `answer`.

Use numeric values with units implied by the field names and round ratios to three decimals, precipitation to three decimals, AlphaEarth values to six decimals, RGB mean absolute difference to three decimals, and percent score to one decimal.
