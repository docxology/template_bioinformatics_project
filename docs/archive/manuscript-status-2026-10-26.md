# Manuscript status — Bioinformatics Project Template

**Repo type:** tool/boilerplate project template (a standard organizational
scaffold for bioinformatics data-processing projects — see root
`README.md`).

**Historical evidence checked (2026-10-26):** root `README.md` (Quickstart, directory
structure, reproducibility principles), `requirements.txt` (dependency
floors refreshed 2026-10-26), `config/`, `scripts/` (entry point executed),
`results/`, `logs/`. No analysis outputs, figures, or
publication-target research content exist in this checkout; no
`manuscript/` directory exists at repo top level.

**Why no publication-target manuscript applies today:** this repository is
a reusable scaffold instantiated per bioinformatics project, not a
research project with its own findings. Any manuscript produced from a
project *using* this scaffold belongs in the instantiated project, not in
the template itself. This repository does not install or integrate the
docxology/template SDK or its manuscript renderer.

**What would trigger creating one:** instantiating this scaffold into a
concrete research project that generates analysis outputs (figures,
processed result tables) with publication intent. In that downstream project,
one optional layout is a `manuscript/` directory following the
docxology/template exemplar standard (SECTION files `00_abstract.md`..`99_references.md`, `config.yaml`,
`config.yaml.example`, `preamble.md`, `references.bib`, `README.md`,
`AGENTS.md`).
