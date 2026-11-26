# Directory and configuration contract {#sec:layout}

Reproducible project organization keeps original inputs separate from
derived files and records the parameters used in a run
[@wilson2017good; @sandve2013rules]. This scaffold defines separate raw,
processed, and log directories. The process working directory supplies the
base for relative paths in the YAML file.

![YAML configures the CLI, which checks the raw directory, creates the processed directory, and appends a run log.](../../output/figures/architecture-overview.png){#fig:scaffold-layout width=100%}

Figure [@fig:scaffold-layout] shows the active paths. The raw directory must
exist already. The script logs the configured filtering threshold as a
parameter. Other processing fields remain reserved for downstream work.
