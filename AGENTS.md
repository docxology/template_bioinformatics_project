# AGENTS.md — `template_bioinformatics_project`

## Scope and architecture

This public repository is an independently authored organizational scaffold,
not a scientific pipeline or one of the canonical `docxology/template` SDK
exemplars. It has no SDK dependency, SDK version contract, `pyproject.toml`,
package API, automated test suite, or manuscript-rendering integration. Do
not impose the root template's 4.5.0 version or replace this scaffold with
an exemplar. See `README.md` for installation and the executable smoke check.

## Source map

- `scripts/01_process_data.py`: YAML loading, directory checks, and logging;
  `process_data` is a stub. It does not scan, read, transform, or write data.
- `config/default.yaml`: paths resolve against the process working directory,
  not the YAML file's directory. Logging settings are active;
  `filtering_threshold` is logged only. `threads`, `normalize`, `results`, and
  `import_path.config` are reserved settings, not implemented behavior.
- `data/raw/`: immutable inputs; the script requires an existing directory.
- `data/processed/`: output directory created by the stub, without data files.
- `logs/`: append-mode run logging; `results/` and `notebooks/` are placeholders.
- `docs/manuscript/`: explains why this scaffold has no research manuscript.
- `requirements.txt`: optional downstream analysis/workflow starter stack;
  only PyYAML is required for the shipped script. No Snakefile ships here.

## Change and verification contract

- Preserve all raw inputs and local/ignored data, logs, and results. Never
  infer cleanup permission from a clean Git status or placeholder directories.
- Keep paths configurable. Use temporary working directories and harmless
  fixtures for validation, as shown in the README's smoke workflow.
- Smoke success proves CLI/config/path/logging plumbing only, not biological
  processing, statistical validity, SDK integration, or full-stack support.
- There is no test framework to invoke or introduce for scaffold-only changes.
- These are public repository files, not a local-only `projects/ongoing/`
  checkout. Do not use historical external-drive paths as policy dependencies.
- In a GitVault-managed checkout, follow ancestor custody rules and use the
  official `with-repo --cwd <checkout> docxology/template_bioinformatics_project`
  lease for writes, gates, and authorized publication. Never force-push.
