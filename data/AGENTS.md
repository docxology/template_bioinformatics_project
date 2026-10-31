# AGENTS.md — `template_bioinformatics_project/data`

Follow the repository-root `AGENTS.md`. `raw/` holds immutable inputs:
never create, modify, or remove user data during scaffold validation.
`processed/` is reserved for downstream derived data; the current stub
creates the directory but writes no data files. Both directories ship only
tracked `.gitkeep` placeholders; ignored local data may still be present.
Use temporary fixtures as described in the root README, not repository raw
data. Do not treat ignored or regenerable files as authorized cleanup.
