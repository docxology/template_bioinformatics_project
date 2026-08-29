# AGENTS.md — docs/ (Bioinformatics Project Template)

## Layout

- `README.md` — human entry point (what this repo is, directory map, run/test)
- `AGENTS.md` — this file: conventions for maintaining docs/

## Repo conventions observed

- `data/raw/` is strictly read-only; derived data goes to
  `data/processed/` (from `../README.md`).
- Configuration (input bounds, thresholds, logging) lives in
  `config/default.yaml` — no hardcoding into scripts.
- Scripts log execution state into `logs/` for traceability.
- This checkout is a simplified scaffold (config, data, scripts, results,
  logs, requirements.txt) — it does not carry the monorepo's
  `src/`/`tests/`/`manuscript/` layout.

## Maintaining these docs

Keep both files short (30–80 lines), factual, and derived only from repo
files. Update the directory map when top-level layout changes.
