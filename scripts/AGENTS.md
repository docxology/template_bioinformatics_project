# AGENTS.md — `template_bioinformatics_project/scripts`

Production scripts for the scaffold. Contains `01_process_data.py`:
example entrypoint demonstrating the scaffold's conventions — YAML config
loading (`--config config/default.yaml`), `logging` setup writing
`logs/01_process_data.log`, reading `data/raw/` and writing
`data/processed/`. Verified by inspection 2026-08-29 (not executed).
Convention: numbered scripts (`NN_name.py`) run in order. Local-only under
`projects/ongoing/` — never commit; see
`/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md`.
