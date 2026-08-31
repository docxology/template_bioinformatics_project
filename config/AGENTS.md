# AGENTS.md — `template_bioinformatics_project/config`

Pipeline configuration for the bioinformatics scaffold. Contains
`default.yaml` only: `import_path` (path routing for raw/processed data,
results, logs), `processing` (threads: 4, filtering_threshold: 10.0,
normalize: true), `logging` (level INFO, standard format string).
Verified 2026-08-29. Local-only path under `projects/ongoing/` — never
commit; see `/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md`.
Gotcha: scripts read this file by relative path
(`--config config/default.yaml`), so run from the repo root.
