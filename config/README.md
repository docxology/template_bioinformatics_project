# config

YAML configuration for the bioinformatics data-processing scaffold.
`default.yaml` routes paths (`data/raw/`, `data/processed/`, `results/`,
`logs/`) and sets logging plus placeholder processing parameters. Relative
paths use the working directory. The threshold is logged, not applied;
threads, normalization, results, and `import_path.config` are unused by the
stub. Keep outputs and logs outside raw inputs. Edit this file (or add copies) rather
than touching script code. Part of `template_bioinformatics_project`
(see its README for quickstart).
