from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'A Package Discovery'
__all__ = [
    'list_event_package_files',
    'read_event_metadata',
    'get_event_aoi',
    'find_files_by_layer',
    'find_files_by_keyword',
    'find_files_by_extension',
    'summarize_event_inventory',
    'check_required_layers_present',
    'resolve_relative_package_path',
    'inspect_package_file',
    'list_archive_contents',
    'summarize_archive_member',
    'infer_data_layer_from_filename',
    'build_task_file_manifest',
    'select_candidate_files_for_question',
]

def list_event_package_files(**kwargs: Any) -> dict[str, Any]:
    """list_event_package_files

Kit: A Package Discovery
Purpose: List files in one event package with size, type and relative path.
Inputs: event_id, recursive, layer_filter?
Output: file inventory JSON
Used by: all tasks
"""
    return dispatch('list_event_package_files', **kwargs)

def read_event_metadata(**kwargs: Any) -> dict[str, Any]:
    """read_event_metadata

Kit: A Package Discovery
Purpose: Read event anchor metadata: hazard family, date window, AOI and source summary.
Inputs: event_id
Output: metadata JSON
Used by: all tasks
"""
    return dispatch('read_event_metadata', **kwargs)

def get_event_aoi(**kwargs: Any) -> dict[str, Any]:
    """get_event_aoi

Kit: A Package Discovery
Purpose: Return the event AOI as bbox or GeoJSON for spatial operations.
Inputs: event_id, format
Output: bbox/GeoJSON
Used by: spatial tasks
"""
    return dispatch('get_event_aoi', **kwargs)

def find_files_by_layer(**kwargs: Any) -> dict[str, Any]:
    """find_files_by_layer

Kit: A Package Discovery
Purpose: Find files belonging to a semantic layer such as reports, hazard, exposure or imagery.
Inputs: event_id, layer
Output: matched file list
Used by: tool routing
"""
    return dispatch('find_files_by_layer', **kwargs)

def find_files_by_keyword(**kwargs: Any) -> dict[str, Any]:
    """find_files_by_keyword

Kit: A Package Discovery
Purpose: Find package files by data-source or variable keywords.
Inputs: event_id, keywords
Output: matched file list
Used by: tool routing
"""
    return dispatch('find_files_by_keyword', **kwargs)

def find_files_by_extension(**kwargs: Any) -> dict[str, Any]:
    """find_files_by_extension

Kit: A Package Discovery
Purpose: Find files by extensions such as tif, csv, geojson, png, pdf or html.
Inputs: event_id, extensions
Output: matched file list
Used by: tool routing
"""
    return dispatch('find_files_by_extension', **kwargs)

def summarize_event_inventory(**kwargs: Any) -> dict[str, Any]:
    """summarize_event_inventory

Kit: A Package Discovery
Purpose: Summarize package layers, representative files and missing data classes.
Inputs: event_id
Output: inventory summary
Used by: first pass triage
"""
    return dispatch('summarize_event_inventory', **kwargs)

def check_required_layers_present(**kwargs: Any) -> dict[str, Any]:
    """check_required_layers_present

Kit: A Package Discovery
Purpose: Check whether a question-required evidence set exists or has substitutes.
Inputs: event_id, required_layers
Output: presence report
Used by: task feasibility
"""
    return dispatch('check_required_layers_present', **kwargs)

def resolve_relative_package_path(**kwargs: Any) -> dict[str, Any]:
    """resolve_relative_package_path

Kit: A Package Discovery
Purpose: Resolve safe relative paths inside the benchmark package.
Inputs: event_id, relative_path
Output: absolute path or error
Used by: runner safety
"""
    return dispatch('resolve_relative_package_path', **kwargs)

def inspect_package_file(**kwargs: Any) -> dict[str, Any]:
    """inspect_package_file

Kit: A Package Discovery
Purpose: Inspect any local package file and return the best available summary for archives, text, JSON, tables, rasters, images, vectors, PDFs or binary files.
Inputs: path, max_chars?, max_rows?, max_members?
Output: typed file summary JSON
Used by: universal evidence inspection
"""
    return dispatch('inspect_package_file', **kwargs)

def list_archive_contents(**kwargs: Any) -> dict[str, Any]:
    """list_archive_contents

Kit: A Package Discovery
Purpose: List members inside a ZIP evidence artifact without extracting files to disk.
Inputs: path, max_members?
Output: archive member inventory
Used by: masked exposure and downloaded source packages
"""
    return dispatch('list_archive_contents', **kwargs)

def summarize_archive_member(**kwargs: Any) -> dict[str, Any]:
    """summarize_archive_member

Kit: A Package Discovery
Purpose: Read or summarize one ZIP member as text, JSON, CSV/TSV, nested archive metadata or binary metadata.
Inputs: path, member?, max_chars?, max_rows?
Output: archive member summary
Used by: masked exposure and downloaded source packages
"""
    return dispatch('summarize_archive_member', **kwargs)

def infer_data_layer_from_filename(**kwargs: Any) -> dict[str, Any]:
    """infer_data_layer_from_filename

Kit: A Package Discovery
Purpose: Infer probable layer and source from filename patterns.
Inputs: path
Output: layer/source guess
Used by: messy packages
"""
    return dispatch('infer_data_layer_from_filename', **kwargs)

def build_task_file_manifest(**kwargs: Any) -> dict[str, Any]:
    """build_task_file_manifest

Kit: A Package Discovery
Purpose: Create the exact file manifest an agent should see for one task.
Inputs: task_id
Output: manifest JSON
Used by: trajectory logging
"""
    return dispatch('build_task_file_manifest', **kwargs)

def select_candidate_files_for_question(**kwargs: Any) -> dict[str, Any]:
    """select_candidate_files_for_question

Kit: A Package Discovery
Purpose: Rank candidate files by question terms without reading answers.
Inputs: task_text, file_manifest
Output: ranked file list
Used by: routing
"""
    return dispatch('select_candidate_files_for_question', **kwargs)
