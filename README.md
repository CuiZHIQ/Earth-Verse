# EarthVerse

Anonymous review release: evaluation code, 405 tasks, reference answers, structured ground truth, and scientific tools for 199 events across 19 hazard families.

## Setup

Use Python 3.10 or newer. From the extracted repository directory:

```bash
python -m pip install -r requirements.txt
```

Event evidence is distributed separately and is not included in this code release. To execute investigations, place the event packages under `event_packages/standard_event_packages/packages/<event_id>/`. Task questions, reference answers, and ground truth can be inspected without these files.

Set `OPENAI_API_KEY` and, if needed, `OPENAI_BASE_URL`. Set the model name in `configs/evaluation.json`.

## Evaluation

```bash
python scripts/run_agent.py --config configs/evaluation.json --task-file task_sets/orig405.txt
python scripts/validate_submission.py --submission-dir outputs/agent/your-model --task-file task_sets/orig405.txt --strict
python scripts/judge.py --submission-dir outputs/agent/your-model --out-dir reports/judge --task-file task_sets/orig405.txt
python scripts/report.py --judge-csv reports/judge/per_task_judge_scores.csv --out-dir reports/final
```

Each task output contains `answer.md`, `trajectory.json`, `tool_trace.md`, and `run_notes.md`. Replace `your-model` with the configured model name.

The main score is the mean of answer correctness and process rubric scores. Strict Accuracy@95 measures the share of tasks with answer-unit scores of at least 95. Runtime and cost are reported separately.

## Files

- `tasks/`: questions, reference solutions, and structured ground truth.
- `task_sets/`: task IDs and capability labels.
- `configs/`: evaluation configuration and dimension schema.
- `scripts/`: agent and direct runners, validation, judging, and reporting.
- `tools/`: scientific tools and specialist environments.
- `integrations/earthverse_mcp_server.py`: tool access for external agents.

Agents may read only the question and its event package; reference solutions and ground truth are reserved for evaluation. `MANIFEST.json` identifies the prompt locations and entry points.

For GIS, raster, PDF, meteorological, or MCP support:

```bash
python -m pip install -r requirements-tools.txt
python -m tools.earthverse_tools.cli --list
```

See `LICENSE.md` for software, annotation, and third-party evidence terms.
