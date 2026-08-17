# Uljin-Samcheok Reported Wind-Dry-Burn Forcing Index

A wildfire-smoke analyst is preparing a short technical note on the March 2022 Uljin-Samcheok wildfire along South Korea's east coast. The decision question is whether the local report record contains enough combined wind, dry-weather, early fire-activity, and burn-extent evidence to classify the screening-level smoke-spread forcing as high rather than moderate.

Compute the reported wind-dry-burn forcing index:

`RWDBFI = A * (E / N) * Hkha`

where:

- `A` is the count of report text anchors among: strong winds, dry weather, and westerly smoke transport toward southern Japan.
- `E` is the inclusive number of early active fire days from the event-window start through the report date when satellites still detected fire activity after winds slackened.
- `N` is the inclusive number of days in the March 4-13, 2022 event window.
- `Hkha` is the reported charred area in thousand hectares.

Classify the result with these thresholds: high if `RWDBFI >= 20`, moderate if `10 <= RWDBFI < 20`, and lower if `RWDBFI < 10`.

Return one compact JSON object with exactly these top-level fields:

- `reported_wind_dry_burn_forcing_index`
- `units`
- `inputs`
- `severity_class`
- `interpretation`

Round the final index to two decimals, keep the burned-area input in thousand hectares, and make the interpretation one sentence linking the numeric result to screening-level wildfire-smoke transport concern.
