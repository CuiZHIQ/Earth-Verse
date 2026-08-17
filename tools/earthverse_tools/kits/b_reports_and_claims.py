from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'B Reports and Claims'
__all__ = [
    'read_text_or_html',
    'read_pdf_text',
    'extract_report_snippets',
    'extract_event_time_claims',
    'extract_location_claims',
    'extract_impact_claims',
    'extract_hazard_magnitude_claims',
    'extract_response_action_claims',
    'parse_report_source_metadata',
    'build_report_event_timeline',
    'deduplicate_report_claims',
    'classify_claim_type',
    'extract_report_causal_chains',
    'extract_report_numeric_observations',
]

def read_text_or_html(**kwargs: Any) -> dict[str, Any]:
    """read_text_or_html

Kit: B Reports and Claims
Purpose: Read plain text, markdown, saved webpages or HTML reports.
Inputs: path, max_chars?
Output: clean text with title
Used by: report tasks
"""
    return dispatch('read_text_or_html', **kwargs)

def read_pdf_text(**kwargs: Any) -> dict[str, Any]:
    """read_pdf_text

Kit: B Reports and Claims
Purpose: Extract text from a PDF report by page range.
Inputs: path, pages?
Output: page text JSON
Used by: institutional reports
"""
    return dispatch('read_pdf_text', **kwargs)

def extract_report_snippets(**kwargs: Any) -> dict[str, Any]:
    """extract_report_snippets

Kit: B Reports and Claims
Purpose: Extract keyword-centered snippets with source provenance.
Inputs: paths, keywords, window
Output: snippet list
Used by: evidence retrieval
"""
    return dispatch('extract_report_snippets', **kwargs)

def extract_event_time_claims(**kwargs: Any) -> dict[str, Any]:
    """extract_event_time_claims

Kit: B Reports and Claims
Purpose: Extract dates, windows and temporal qualifiers from reports.
Inputs: paths
Output: time claims
Used by: event anchoring
"""
    return dispatch('extract_event_time_claims', **kwargs)

def extract_location_claims(**kwargs: Any) -> dict[str, Any]:
    """extract_location_claims

Kit: B Reports and Claims
Purpose: Extract place names, admin units and coordinates from reports.
Inputs: paths
Output: location claims
Used by: event anchoring
"""
    return dispatch('extract_location_claims', **kwargs)

def extract_impact_claims(**kwargs: Any) -> dict[str, Any]:
    """extract_impact_claims

Kit: B Reports and Claims
Purpose: Extract deaths, displaced people, damage, disruption and response impacts.
Inputs: paths
Output: impact claims
Used by: impact reasoning
"""
    return dispatch('extract_impact_claims', **kwargs)

def extract_hazard_magnitude_claims(**kwargs: Any) -> dict[str, Any]:
    """extract_hazard_magnitude_claims

Kit: B Reports and Claims
Purpose: Extract rainfall, wind, temperature, magnitude, AQI or other hazard intensity claims.
Inputs: paths
Output: magnitude claims
Used by: physical context
"""
    return dispatch('extract_hazard_magnitude_claims', **kwargs)

def extract_response_action_claims(**kwargs: Any) -> dict[str, Any]:
    """extract_response_action_claims

Kit: B Reports and Claims
Purpose: Extract warnings, evacuations, closures and response actions.
Inputs: paths
Output: response claims
Used by: priority tasks
"""
    return dispatch('extract_response_action_claims', **kwargs)

def parse_report_source_metadata(**kwargs: Any) -> dict[str, Any]:
    """parse_report_source_metadata

Kit: B Reports and Claims
Purpose: Extract concrete source metadata such as organization, publication date, URL, title and document type from report files.
Inputs: paths, metadata_patterns?
Output: source metadata table JSON
Used by: report parsing tasks
"""
    return dispatch('parse_report_source_metadata', **kwargs)

def build_report_event_timeline(**kwargs: Any) -> dict[str, Any]:
    """build_report_event_timeline

Kit: B Reports and Claims
Purpose: Convert extracted time, hazard, impact and response claims into an ordered event timeline.
Inputs: time_claims, hazard_claims?, impact_claims?, response_claims?
Output: event timeline rows JSON
Used by: process reconstruction tasks
"""
    return dispatch('build_report_event_timeline', **kwargs)

def deduplicate_report_claims(**kwargs: Any) -> dict[str, Any]:
    """deduplicate_report_claims

Kit: B Reports and Claims
Purpose: Merge duplicate claims repeated across reports and news pages.
Inputs: claims
Output: deduplicated claims
Used by: report synthesis
"""
    return dispatch('deduplicate_report_claims', **kwargs)

def classify_claim_type(**kwargs: Any) -> dict[str, Any]:
    """classify_claim_type

Kit: B Reports and Claims
Purpose: Classify a text claim as hazard, exposure, impact, response or uncertainty.
Inputs: claim_text
Output: claim class
Used by: scoring
"""
    return dispatch('classify_claim_type', **kwargs)

def extract_report_causal_chains(**kwargs: Any) -> dict[str, Any]:
    """extract_report_causal_chains

Kit: B Reports and Claims
Purpose: Extract reported causal links such as rainfall-to-flooding, heat-to-health stress or fire-to-smoke impacts.
Inputs: paths, hazard_keywords?, impact_keywords?
Output: causal chain claim list JSON
Used by: mechanism and impact-chain tasks
"""
    return dispatch('extract_report_causal_chains', **kwargs)

def extract_report_numeric_observations(**kwargs: Any) -> dict[str, Any]:
    """extract_report_numeric_observations

Kit: B Reports and Claims
Purpose: Extract numeric observations and their units from reports, including casualties, rainfall, wind, temperature, discharge, area and exposure counts.
Inputs: paths, target_variables?, unit_patterns?
Output: numeric observation table JSON
Used by: numeric report reasoning tasks
"""
    return dispatch('extract_report_numeric_observations', **kwargs)
