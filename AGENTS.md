# AGENTS.md — `template_bioinformatics_project`

> Verified against disk 2026-10-26. Agent notes for the bioinformatics
> project-scaffold repo. Repo-wide policy: see
> `/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md`.

## What this repo is

A **standard organizational template** for bioinformatics data-processing
projects (not a research project with its own findings): reproducibility
conventions, immutable raw data, config-driven processing, and log
traceability. See root `README.md` for the human-facing quickstart.

## Layout map (verified 2026-10-26)

- `config/` — `default.yaml`: path routing (`data/raw/`, `data/processed/`,
  `results/`, `logs/`), processing params (threads, filtering_threshold,
  normalize), logging level/format.
- `data/raw/` — **immutable raw data. Currently empty** in this checkout.
- `data/processed/` — cleansed intermediate data. Currently empty.
- `scripts/` — `01_process_data.py`: example entrypoint reading
  `data/raw/` -> writing `data/processed/`, YAML-config-driven, logging to
  `logs/01_process_data.log`.
- `notebooks/` — EDA/visualization notebooks. Currently `.gitkeep` only.
- `results/` — final formatted outputs (tables, figures). Currently empty.
- `logs/` — execution logs. Currently empty.
- `docs/manuscript/` — `MANUSCRIPT_STATUS.md`: documents why this repo has
  no publication manuscript (scaffold, not research).
- `README.md`, `requirements.txt` (pandas/numpy/matplotlib/seaborn/scipy/
  snakemake/pyyaml/click/tqdm). **No `src/`, no `tests/`, no
  `pyproject.toml`** — this repo intentionally deviates from the docxology
  exemplar layout because it is a scaffold, not a pipeline-rendered project.

## Invariants

- Never modify anything in `data/raw/`.
- No hardcoding: all paths/thresholds route through `config/`.
- Logs go through Python `logging` into `logs/`.
- Local-only under `projects/ongoing/` — never commit (root `.gitignore`
  `projects/*`; guarded by `scripts/audit/check_tracked_all.py`).
- This is a symlinked view of the public docxology mirror
  (`../docxology/template_bioinformatics_project`) — writes here become
  public on push.

## Gotchas

- Snakemake is in `requirements.txt` (`>=8.0.0`) but **no Snakefile exists**
  in this checkout — the dep is a starter for pipelines added downstream,
  not a wired-up workflow.
- Entry point: `python scripts/01_process_data.py --config config/default.yaml`
  run from the repo root — **executed 2026-10-26**: exit 0, wrote
  `logs/01_process_data.log` (needs only `pyyaml`).

## Verify

- `ls data/raw data/processed results logs` — confirm emptiness/contents.
- `head scripts/01_process_data.py` — confirm config-driven pattern.
