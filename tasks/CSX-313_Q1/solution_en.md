# Correct Answer

```json
{
  "source_paths": {
    "event_report": [
      "data/event_reports/event_reports_001_Locked_package_evidence_report.html",
      "data/event_reports/event_reports_004_Locked_event_anchor_Taan_Fiord_glacier-adjacent_landslide_tsunami.json"
    ],
    "metadata_or_catalog_context": [
      "metadata/event.json",
      "metadata/files.csv",
      "data/event_catalogs/event_catalogs_002_GLIMS_glacier_database_and_RGI_outlines.html"
    ]
  },
  "process_model": {
    "event_window": "2015-10-17 to 2015-10-17",
    "location": "Taan Fiord / Tyndall Glacier, Alaska, United States",
    "mechanism_chain": [
      "recent glacier retreat exposed unstable slopes",
      "deep fjord water extended beneath slope margins",
      "a 180 million ton rockslide entered Taan Fiord",
      "impulsive displacement generated a tsunami with 193 m maximum runup",
      "the source mechanics dominate the monitoring priority"
    ],
    "classification": "source_dominated_landslide_tsunami_report_confirmed"
  },
  "computed_metrics": {
    "mass_million_tons": 180.0,
    "runup_m": 193.0,
    "source_runup_load_million_ton_m": 34740.0,
    "source_power_norm": 0.869,
    "report_mechanism_completeness": 1.0,
    "glacier_retreat_context_flag": 1,
    "process_dominance_index": 91.45
  },
  "scenario_analysis": {
    "runup_increase_percent": 15.0,
    "scenario_runup_m": 221.95,
    "scenario_source_power_norm": 0.999,
    "scenario_process_dominance_index": 99.92,
    "scenario_delta_index": 8.47
  },
  "scientific_use_notes": {
    "decisive_evidence": "The event report supplies the source mechanism, mass, runup, timing, and retreat/deep-water fjord context.",
    "weak_context": "Auxiliary precipitation, remote-sensing, exposure, and geocoding slices are not used for this source-dominance score; the report mechanics are sufficient.",
    "interpretive_consequence": "The model emphasizes impulsive landslide-tsunami generation and monitoring sensitivity in deglaciating fjords rather than a rainfall-driven, image-product, or population-exposure-dominated disaster process."
  },
  "final_interpretation": "A very large rockslide entering a recently deglaciated deep-water fjord is the dominant process; the report-confirmed source mass and runup support a source-driven monitoring priority, and a modest runup-coupling increase would materially raise the index."
}
```

# Computation Path

The strongest event report states that the 17 October 2015 slope failure at Tyndall Glacier sent 180 million tons of rock into Taan Fiord and produced tsunami runup as high as 193 m.

`source_runup_load_million_ton_m = 180 * 193 = 34740.0`.

`source_power_norm = 34740 / 40000 = 0.8685`, rounded to `0.869`.

All five report mechanism terms are supported: fjord landslide source, reported rock mass, reported tsunami runup, glacier-retreat/unstable-slope context, and deep-water context. Therefore `report_mechanism_completeness = 1.000` and `glacier_retreat_context_flag = 1`.

`process_dominance_index = 100 * (0.65 * 0.8685 + 0.25 * 1.000 + 0.10 * 1) = 91.45`.

The 15 percent fjord-sensitivity scenario uses only changed runup:

`scenario_runup_m = 193 * 1.15 = 221.95`.

`scenario_source_power_norm = (180 * 221.95) / 40000 = 0.998775`, rounded to `0.999`.

`scenario_process_dominance_index = 99.92`.

`scenario_delta_index = 99.92 - 91.45 = 8.47`.

The classification is `source_dominated_landslide_tsunami_report_confirmed` because `source_power_norm >= 0.75`, `report_mechanism_completeness >= 0.80`, and `glacier_retreat_context_flag == 1`.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "A weather, exposure, or generic remote-sensing explanation fails because the source mass and extreme runup already establish the landslide-tsunami mechanism.",
    "evidence_weighting": "The report-confirmed rockslide mass, runup, fjord source setting, glacier-retreat context, and deep-water context are decisive; auxiliary products are not needed for the source-dominance label.",
    "uncertainty_or_scale_caveat": "The 15 percent runup scenario is a sensitivity test, not a prediction of a second observed event."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

Award 20 points total:

- **Self-directed package discovery and citations (3 points):** Finds the relevant event report, event anchor or metadata, and optional catalog context without being given filenames, and cites package-relative paths. Partial credit: 1-2 points for incomplete but relevant citations.
- **Event mechanism reconstruction (4 points):** Correctly identifies the Taan Fiord/Tyndall Glacier location, the 17 October 2015 window, glacier-retreat/deep-water slope conditioning, rockslide entry into the fjord, and tsunami runup process.
- **Source load calculations (4 points):** Extracts 180 million tons and 193 m, computes `34740.0` and `source_power_norm = 0.869` within tolerance.
- **Report mechanism support (3 points):** Correctly evaluates the five report mechanism terms, reports `report_mechanism_completeness = 1.000`, and sets `glacier_retreat_context_flag = 1`.
- **Process index and classification (3 points):** Computes `process_dominance_index = 91.45` and returns `source_dominated_landslide_tsunami_report_confirmed` using all rule conditions.
- **Scenario reasoning (2 points):** Applies the 15 percent runup-only perturbation, reports `221.95 m`, `0.999`, `99.92`, and `8.47` within tolerance, and explains the fjord-sensitivity meaning.
- **Structured scientific answer quality (1 point):** Returns exactly the requested top-level JSON keys, keeps the interpretation concise, and avoids unsupported casualty, damage, auxiliary-product, or outside-source claims.
