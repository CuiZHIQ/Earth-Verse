from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .core import ToolRegistry


PACKAGE_INSPECTION_TOOLS = [
    "inspect_package_file",
    "list_archive_contents",
    "summarize_archive_member",
]


def _dedupe(names: list[str]) -> list[str]:
    out = []
    seen = set()
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        out.append(name)
    return out


MINIMUM_10 = [
    "list_event_package_files",
    "read_event_metadata",
    "read_text_or_html",
    "read_pdf_text",
    "summarize_table_or_json",
    "load_table_schema",
    "compute_time_window_stats",
    "get_event_aoi",
    "read_image_rgb_summary",
    "assemble_structured_answer_fields",
]

MINIMAL_ANALYTICS_12 = [
    "list_event_package_files",
    "read_event_metadata",
    "read_text_or_html",
    "read_pdf_text",
    "extract_report_snippets",
    "summarize_table_or_json",
    "compute_time_window_stats",
    "compute_rolling_sum",
    "detect_consecutive_exceedance",
    "compute_unit_conversion_or_ratio",
    "compute_precip_accumulation",
    "infer_task_reasoning_axes",
]

MINIMUM_REAL_17 = MINIMAL_ANALYTICS_12 + [
    "compute_heatwave_duration_intensity",
    "compute_apparent_temperature_stats",
    "compute_hot_dry_vpd_metrics",
    "compute_urban_pluvial_diagnostics",
    "compute_cold_spell_metrics",
]

CORE_37 = [
    "list_event_package_files",
    "read_event_metadata",
    "inspect_package_file",
    "list_archive_contents",
    "summarize_archive_member",
    "get_event_aoi",
    "find_files_by_layer",
    "summarize_event_inventory",
    "read_text_or_html",
    "extract_report_snippets",
    "extract_impact_claims",
    "extract_hazard_magnitude_claims",
    "load_table_schema",
    "filter_table_rows",
    "compute_time_window_stats",
    "compute_rolling_sum",
    "detect_consecutive_exceedance",
    "load_vector_summary",
    "clip_vector_to_aoi",
    "calculate_line_length_in_polygon",
    "calculate_polygon_area",
    "estimate_population_exposure",
    "load_raster_summary",
    "compute_zonal_raster_stats",
    "compare_pre_post_rasters",
    "compute_raster_threshold_area",
    "read_image_rgb_summary",
    "compute_wet_bulb_temperature",
    "compute_precip_accumulation",
    "compute_flood_impact_metrics",
    "compute_fire_hotspot_metrics",
    "compute_cyclone_track_metrics",
    "compute_earthquake_sequence_metrics",
    "compute_enso_phase_metrics",
    "build_hazard_metric_matrix",
    "assemble_structured_answer_fields",
    "summarize_key_findings_table",
]

DEEP_REASONING_12 = [
    "infer_task_reasoning_axes",
    "build_mechanism_competition_table",
    "reconstruct_event_process_stages",
    "evaluate_physical_consistency",
    "synthesize_compound_hazard_chain",
    "compare_visual_numeric_evidence",
    "calibrate_event_severity_profile",
    "derive_response_priority_rationale",
    "test_option_hypothesis_consistency",
    "extract_required_computation_targets",
    "map_task_to_required_tools",
    "build_metric_dependency_graph",
]

CORE_DEEP_48 = [
    "list_event_package_files",
    "read_event_metadata",
    "inspect_package_file",
    "list_archive_contents",
    "summarize_archive_member",
    "find_files_by_layer",
    "summarize_event_inventory",
    "read_text_or_html",
    "read_pdf_text",
    "extract_report_snippets",
    "extract_event_time_claims",
    "extract_impact_claims",
    "extract_hazard_magnitude_claims",
    "load_table_schema",
    "filter_table_rows",
    "compute_time_window_stats",
    "compute_rolling_sum",
    "detect_consecutive_exceedance",
    "compute_lagged_peak",
    "compute_precip_accumulation",
    "compute_precip_intensity_duration",
    "compute_heatwave_duration_intensity",
    "compute_warm_night_count",
    "compute_apparent_temperature_stats",
    "compute_cold_spell_metrics",
    "compute_wet_bulb_temperature",
    "get_event_aoi",
    "compute_heat_index",
    "estimate_population_exposure",
    "count_facilities_exposed",
    "load_raster_summary",
    "compute_zonal_raster_stats",
    "compare_pre_post_rasters",
    "read_image_rgb_summary",
    "summarize_image_rgb_statistics",
    "compare_image_rgb_summaries",
    "estimate_image_obscuration_proxy",
    "read_alphaearth_embedding_stats",
    "compute_nbr",
    "compute_marine_heatwave_metrics",
    "compute_flood_impact_metrics",
    "compute_landslide_trigger_index",
    "compute_air_quality_exceedance",
    "infer_task_reasoning_axes",
    "build_mechanism_competition_table",
    "reconstruct_event_process_stages",
    "evaluate_physical_consistency",
    "synthesize_compound_hazard_chain",
    "compare_visual_numeric_evidence",
    "calibrate_event_severity_profile",
    "derive_response_priority_rationale",
    "compute_fire_weather_index_proxy",
    "assemble_structured_answer_fields",
    "summarize_key_findings_table",
]

TRAJECTORY_DERIVED_6 = [
    "summarize_table_or_json",
    "compute_unit_conversion_or_ratio",
    "compute_hot_dry_vpd_metrics",
    "compute_urban_pluvial_diagnostics",
    "reconcile_point_grid_regional_scale",
    "parse_mcq_options_and_select",
]

CORE_DEEP_54 = CORE_DEEP_48 + TRAJECTORY_DERIVED_6

WORKFLOW_PROFILES = {
    "heat_health_persistence": [
        "list_event_package_files", "read_event_metadata", "read_text_or_html",
        "extract_report_snippets", "load_table_schema", "compute_time_window_stats",
        "detect_consecutive_exceedance", "compute_heat_index", "compute_wet_bulb_temperature",
        "compute_apparent_temperature_stats", "compute_warm_night_count",
        "compute_heatwave_duration_intensity", "estimate_population_exposure",
        "compute_hospital_exposure_priority", "read_image_rgb_summary",
        "calibrate_event_severity_profile", "evaluate_physical_consistency",
        "build_hazard_metric_matrix", "summarize_key_findings_table", "assemble_structured_answer_fields",
    ],
    "flood_hazard_impact_chain": [
        "list_event_package_files", "read_event_metadata", "get_event_aoi",
        "read_text_or_html", "extract_report_snippets", "load_table_schema",
        "compute_precip_accumulation", "compute_rolling_sum",
        "compare_event_to_baseline_percentile", "load_raster_summary",
        "compare_pre_post_rasters", "compute_raster_threshold_area",
        "compute_flood_impact_metrics", "estimate_population_exposure",
        "calculate_line_length_in_polygon", "summarize_311_complaints",
        "compute_lagged_peak", "synthesize_compound_hazard_chain",
        "derive_response_priority_rationale", "make_overview_map", "assemble_structured_answer_fields",
        "summarize_key_findings_table",
    ],
    "cyclone_compound_wind_rain_surge": [
        "list_event_package_files", "read_event_metadata", "get_event_aoi",
        "load_table_schema", "compute_cyclone_track_metrics",
        "compute_precip_accumulation", "compute_distance_to_track_or_epicenter",
        "compute_wind_exposure_metrics", "compute_storm_surge_proxy",
        "compute_tide_surge_compound_index", "estimate_population_exposure",
        "compute_port_airport_exposure", "build_mechanism_competition_table",
        "calibrate_event_severity_profile", "summarize_key_findings_table",
    ],
    "wildfire_smoke_health": [
        "list_event_package_files", "read_event_metadata", "read_text_or_html",
        "extract_report_snippets", "load_table_schema", "compute_fire_hotspot_metrics",
        "compute_burned_area_metrics", "compute_nbr", "estimate_image_burn_proxy",
        "estimate_image_obscuration_proxy", "compute_smoke_pm_lag_metrics",
        "compute_air_quality_exceedance", "interpolate_station_pollution",
        "estimate_population_exposure", "compare_visual_numeric_evidence",
        "synthesize_compound_hazard_chain", "summarize_key_findings_table",
    ],
    "drought_agricultural_stress": [
        "list_event_package_files", "read_event_metadata", "read_text_or_html",
        "extract_report_snippets", "load_table_schema", "compute_anomaly_from_climatology",
        "compute_spei_spi", "compute_soil_moisture_percentile", "compute_ndvi",
        "compute_rolling_mean", "compare_event_to_baseline_percentile",
        "synthesize_multisource_evidence", "calibrate_event_severity_profile",
        "evaluate_physical_consistency", "summarize_key_findings_table",
    ],
    "enso_teleconnection": [
        "list_event_package_files", "read_event_metadata", "read_text_or_html",
        "extract_report_snippets", "load_table_schema", "compute_enso_phase_metrics",
        "compute_teleconnection_lag_correlation", "compute_anomaly_from_climatology",
        "compute_percentile_rank", "synthesize_multisource_evidence",
        "calibrate_event_severity_profile", "evaluate_physical_consistency",
        "summarize_key_findings_table",
    ],
    "marine_heatwave_coral": [
        "list_event_package_files", "read_event_metadata", "read_text_or_html",
        "extract_report_snippets", "load_table_schema", "load_raster_summary",
        "extract_raster_timeseries", "compute_marine_heatwave_metrics",
        "compute_ocean_heat_content_proxy", "compute_coral_bleaching_alert",
        "compute_raster_histogram", "compare_visual_numeric_evidence",
        "calibrate_event_severity_profile", "build_hazard_metric_matrix",
        "summarize_key_findings_table",
    ],
    "earthquake_lifeline_response": [
        "list_event_package_files", "read_event_metadata", "read_text_or_html",
        "extract_report_snippets", "load_table_schema", "compute_earthquake_sequence_metrics",
        "compute_shakemap_exposure", "estimate_ground_failure_susceptibility",
        "count_facilities_exposed", "compute_road_disruption_proxy",
        "reconstruct_event_process_stages", "derive_response_priority_rationale",
        "rank_response_priorities", "summarize_key_findings_table",
    ],
    "volcano_ash_airspace": [
        "list_event_package_files", "read_event_metadata", "read_text_or_html",
        "extract_report_snippets", "compute_volcano_ash_extent", "compute_so2_anomaly",
        "estimate_image_obscuration_proxy", "compute_port_airport_exposure",
        "extract_response_action_claims", "compare_visual_numeric_evidence",
        "build_hazard_metric_matrix", "summarize_key_findings_table",
    ],
    "landslide_trigger_exposure": [
        "list_event_package_files", "read_event_metadata", "get_event_aoi",
        "read_text_or_html", "extract_report_snippets", "load_table_schema",
        "compute_landslide_trigger_index", "estimate_runoff_proxy",
        "compute_precip_intensity_duration", "calculate_line_length_in_polygon",
        "estimate_population_exposure", "reconstruct_event_process_stages",
        "make_overview_map", "summarize_key_findings_table",
    ],
    "urban_feedback_infrastructure": [
        "list_event_package_files", "read_event_metadata", "get_event_aoi",
        "read_text_or_html", "extract_report_snippets", "load_table_schema",
        "summarize_311_complaints", "compute_lagged_peak", "compute_road_disruption_proxy",
        "count_facilities_exposed", "rank_admin_units_by_response_need",
        "derive_response_priority_rationale", "extract_report_causal_chains",
        "summarize_key_findings_table",
    ],
    "remote_sensing_change_diagnosis": [
        "list_event_package_files", "read_event_metadata", "get_event_aoi",
        "load_raster_summary", "compute_zonal_raster_stats", "compare_pre_post_rasters",
        "read_image_rgb_summary", "summarize_image_rgb_statistics", "compare_image_rgb_summaries",
        "compute_ndvi", "compute_ndwi", "compute_nbr",
        "estimate_image_flood_proxy", "estimate_image_burn_proxy",
        "read_alphaearth_embedding_stats", "compare_alphaearth_embedding_stats",
        "compare_image_proxy_to_hazard_signature", "read_image_file_metadata",
        "build_image_change_summary",
        "compare_visual_numeric_evidence", "build_hazard_metric_matrix",
        "summarize_key_findings_table",
    ],
    "compound_physical_process_diagnosis": [
        "list_event_package_files", "read_event_metadata", "get_event_aoi",
        "read_text_or_html", "extract_report_snippets", "load_table_schema",
        "compute_time_window_stats", "compute_rolling_sum",
        "compute_zonal_raster_stats", "read_image_rgb_summary",
        "infer_task_reasoning_axes", "build_mechanism_competition_table",
        "reconstruct_event_process_stages", "evaluate_physical_consistency",
        "compare_visual_numeric_evidence", "calibrate_event_severity_profile",
        "synthesize_compound_hazard_chain", "derive_response_priority_rationale",
        "assemble_structured_answer_fields", "summarize_key_findings_table",
    ],
}


HAZARD_TO_WORKFLOW = {
    "heat": "heat_health_persistence",
    "heat_wave": "heat_health_persistence",
    "flood": "flood_hazard_impact_chain",
    "precip": "flood_hazard_impact_chain",
    "rain": "flood_hazard_impact_chain",
    "cyclone": "cyclone_compound_wind_rain_surge",
    "hurricane": "cyclone_compound_wind_rain_surge",
    "typhoon": "cyclone_compound_wind_rain_surge",
    "wildfire": "wildfire_smoke_health",
    "smoke": "wildfire_smoke_health",
    "fire": "wildfire_smoke_health",
    "drought": "drought_agricultural_stress",
    "enso": "enso_teleconnection",
    "marine": "marine_heatwave_coral",
    "coral": "marine_heatwave_coral",
    "earthquake": "earthquake_lifeline_response",
    "quake": "earthquake_lifeline_response",
    "volcano": "volcano_ash_airspace",
    "ash": "volcano_ash_airspace",
    "landslide": "landslide_trigger_exposure",
    "urban": "urban_feedback_infrastructure",
    "311": "urban_feedback_infrastructure",
    "remote": "remote_sensing_change_diagnosis",
    "sentinel": "remote_sensing_change_diagnosis",
    "image": "remote_sensing_change_diagnosis",
    "process": "compound_physical_process_diagnosis",
    "mechanism": "compound_physical_process_diagnosis",
    "consistency": "compound_physical_process_diagnosis",
    "stage": "compound_physical_process_diagnosis",
    "diagnosis": "compound_physical_process_diagnosis",
}


@dataclass
class ToolProfile:
    name: str
    level: str
    description: str
    tools: list[str]


class ToolProfileManager:
    """Manage layered tool packages for EarthVerse agents."""

    def __init__(self, registry: ToolRegistry | None = None):
        self.registry = registry or ToolRegistry()
        self._all = [t["name"] for t in self.registry.list_tools()]
        self._by_kit: dict[str, list[str]] = {}
        for spec in self.registry.list_tools():
            self._by_kit.setdefault(spec["kit"], []).append(spec["name"])

    def list_profiles(self) -> list[dict[str, Any]]:
        return [p.__dict__ for p in self._build_profiles()]

    def get_profile(self, name: str) -> dict[str, Any]:
        for profile in self._build_profiles():
            if profile.name == name:
                return profile.__dict__
        raise KeyError(name)

    def tools_for_profile(self, name: str) -> list[dict[str, Any]]:
        names = set(self.get_profile(name)["tools"])
        return [self.registry.describe(n) for n in self._all if n in names]

    def route_profile(self, question: str = "", metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        text = " ".join(str(x) for x in [question, metadata or {}]).lower()
        scores: dict[str, int] = {}
        for keyword, workflow in HAZARD_TO_WORKFLOW.items():
            if keyword in text:
                scores[workflow] = scores.get(workflow, 0) + 1
        if not scores:
            return self.get_profile("core_deep_54")
        workflow = sorted(scores.items(), key=lambda x: (-x[1], x[0]))[0][0]
        return self.get_profile(f"workflow:{workflow}")

    def _build_profiles(self) -> list[ToolProfile]:
        profiles = [
            ToolProfile("minimum_10", "minimum", "Smallest reasoning runner set: package discovery, report/PDF reading, table/JSON summary, basic time-window stats, image RGB summary, and structured answer composition.", [t for t in MINIMUM_10 if t in self._all]),
            ToolProfile(
                "minimal_analytics_12",
                "minimum",
                "Compact analytical set for reports, PDFs, tables, event windows, threshold runs, unit and ratio normalization, precipitation accumulation, and task routing.",
                [t for t in MINIMAL_ANALYTICS_12 if t in self._all],
            ),
            ToolProfile(
                "minimum_real_17",
                "minimum",
                "Practical set for core analytics plus heat-wave, apparent-temperature, hot-dry/VPD, urban-pluvial, and cold-spell diagnostics.",
                [t for t in MINIMUM_REAL_17 if t in self._all],
            ),
            ToolProfile("core_37", "stable", "First practical implementation set for most benchmark questions without arbitrary Python execution, including package-file and archive inspection fallbacks.", [t for t in CORE_37 if t in self._all]),
            ToolProfile(
                "core_deep_48",
                "advanced",
                "Updated deep-reasoning set for mechanism competition, process reconstruction, visual-numeric synthesis, and severity calibration.",
                [t for t in CORE_DEEP_48 if t in self._all],
            ),
            ToolProfile(
                "core_deep_54",
                "advanced",
                "Deep runner with JSON and table summaries, unit and ratio normalization, hot-dry/VPD and urban-pluvial diagnostics, scale reconciliation, and MCQ checks.",
                [t for t in CORE_DEEP_54 if t in self._all],
            ),
            ToolProfile("full_170", "full", "Complete registry; should be filtered by router before exposure to an LLM.", self._all),
        ]
        for kit, names in sorted(self._by_kit.items()):
            profiles.append(ToolProfile(f"kit:{kit}", "kit", f"All tools in {kit}.", names))
        for workflow, names in sorted(WORKFLOW_PROFILES.items()):
            profiles.append(ToolProfile(f"workflow:{workflow}", "workflow", f"Workflow-specific package for {workflow}, with package-file and archive inspection fallbacks.", [t for t in _dedupe(PACKAGE_INSPECTION_TOOLS + names) if t in self._all]))
        return profiles
