# AGENTS.md — `template_bioinformatics_project/scripts`

Production scripts for the scaffold. Contains `01_process_data.py`:
example entrypoint demonstrating the scaffold's conventions — YAML config
loading (`--config config/default.yaml`), `logging` setup writing
`logs/01_process_data.log`, reading `data/raw/` and writing
`data/processed/`. Executed 2026-10-26 from the repo root (Python 3.15,
pyyaml only): exit 0, wrote `logs/01_process_data.log`; the only
non-stdlib import is `yaml`.
Convention: numbered scripts (`NN_name.py`) run in order. Local-only under
`projects/ongoing/` — never commit; see
`/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md`.
