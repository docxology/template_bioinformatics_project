# AGENTS.md — `template_bioinformatics_project/data`

Data root for the bioinformatics scaffold. `raw/` is **immutable** input
data (never modified by scripts); `processed/` holds cleansed intermediates
derived from `raw/`. Both subfolders are **currently empty** in this
checkout (verified 2026-08-29). Invariants: raw is read-only; processed is
regenerable. Local-only under `projects/ongoing/` — never commit; see
`/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md`.
