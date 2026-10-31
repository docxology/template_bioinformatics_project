# data

Data tree for the bioinformatics scaffold: `raw/` (immutable inputs) and
`processed/` (reserved for downstream intermediates). Both ship `.gitkeep`
placeholders; ignored local data may exist. The shipped stub checks raw's
existence and creates processed, but reads and writes no data files.
Routing comes from `config/default.yaml`. Use the root README's temporary
fixture for smoke checks. Part of `template_bioinformatics_project`.
