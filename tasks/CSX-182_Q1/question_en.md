# Black Summer Numeric Fingerprint Ledger

A climate-risk analytics team is auditing a compact numerical fingerprint for the 2019-2020 Australian Black Summer bushfire period in southeastern Australia. The goal is to test whether the local technical record is best summarized by a compound smoke-burn-exposure signal, a burn-only surface-change signal, or a population-only context signal.

Using the incident technical record and quantitative diagnostics, compute these metrics. The weather-overlap metrics are the package daily-weather rows that fall inside the incident window; do not treat that overlap as complete weather coverage for all 182 event days.

- inclusive event days
- event-window weather-overlap days, dry/windy day count, and dry/windy share
- local dNBR mean, minimum, maximum, and standard deviation
- annual embedding-change mean
- rounded population count
- text flags for stratospheric smoke transport and hazardous or severe air-quality wording

Apply this deterministic ledger:

- `burn_mean_gate = 1` if dNBR mean is at least 0.10, else `0`
- `burn_peak_gate = 1` if dNBR maximum is at least 0.66, else `0`
- `heterogeneous_gate = 1` if dNBR minimum is below 0 and annual embedding-change mean is below 0.05, else `0`
- `dry_windy_gate = 1` if dry/windy day count is at least 8 and dry/windy share is at least 0.15, else `0`
- `smoke_transport_gate = 1` if the text record contains stratospheric smoke transport, else `0`
- `air_quality_gate = 1` if the text record contains hazardous or severe air-quality wording, else `0`
- `population_gate = 1` if rounded population is at least 300000, else `0`
- `uniform_burn_gate = 1` if dNBR minimum is at least 0 and dNBR standard deviation is at most 0.05, else `0`
- `annual_change_high_gate = 1` if annual embedding-change mean is at least 0.10, else `0`

Score the three labels as:

- `compound_smoke_burn_exposure = burn_mean_gate + burn_peak_gate + heterogeneous_gate + dry_windy_gate + smoke_transport_gate + air_quality_gate + population_gate`
- `burn_only_surface_change = burn_mean_gate + burn_peak_gate + uniform_burn_gate + annual_change_high_gate`
- `population_only_context = population_gate`
- `score_margin = compound_smoke_burn_exposure - max(burn_only_surface_change, population_only_context)`

Return a compact JSON object with exactly these fields: `target_family`, `metrics`, `gates`, `scores`, `score_margin`, `answer`, and `computed_interpretation`.
