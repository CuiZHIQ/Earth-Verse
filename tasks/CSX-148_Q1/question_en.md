# Free State Storm Damage Ledger

On 6 December 2023, severe thunderstorms and hail affected Free State Province, South Africa. A technical analyst is reconciling the incident counts with same-day rainfall and wind diagnostics to decide what the compact damage ledger should say.

Using the local incident record and quantitative diagnostics, compute the reported residential-damage totals and explain how the weather values support the storm-day diagnosis without replacing the reported damage counts.

Return a compact JSON object with these keys:

- `label`
- `house_total`
- `residential_total_including_shacks`
- `human_impacts`
- `substations_struck`
- `gpm_max_mm`
- `gpm_to_openmeteo_precip_ratio`
- `conclusion`

After the JSON, add no more than three short bullets showing the arithmetic and the rainfall-diagnostic comparison. Do not use web search or outside datasets.
