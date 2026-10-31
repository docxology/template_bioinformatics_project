# AGENTS.md — `template_bioinformatics_project/config`

Follow the repository-root `AGENTS.md`. `default.yaml` defines path routing,
processing placeholders, and active logging settings. All relative paths,
including `--config`, resolve against the working directory, not the YAML
file's directory. The raw directory must already exist; configure output
and log paths outside raw data.

The stub logs `filtering_threshold` but does not apply it. `threads`,
`normalize`, `results`, and `import_path.config` are reserved, unused fields.
Do not claim processing behavior from their presence. Validate configuration
changes using the root README's temporary-fixture smoke workflow.
