# Render the technical note

The [canonical source](manuscript/README.md) renders with the external
[docxology/template](https://github.com/docxology/template) engine. Install uv,
Python 3.14, librsvg's `rsvg-convert`, Pandoc with a matching
`pandoc-crossref`, and XeLaTeX with its packages.

Use a committed checkout named `template_bioinformatics_project`. From the
repository root, choose an unused path for the engine checkout:

```bash
SCAFFOLD_ROOT="$(pwd -P)"
TEMPLATE_ROOT="$SCAFFOLD_ROOT/../bioinformatics-render-template"
git clone https://github.com/docxology/template.git "$TEMPLATE_ROOT"
git -C "$TEMPLATE_ROOT" switch --detach 87704feae0a4490ef7dad9c931d268e8c30273c2

mkdir -p output/figures
rsvg-convert -o output/figures/architecture-overview.png docs/assets/architecture-overview.svg
cp docs/manuscript/figure_registry.json output/figures/figure_registry.json

cd "$TEMPLATE_ROOT"
uv sync --locked --no-dev --python 3.14
mkdir -p projects/working
ln -s "$SCAFFOLD_ROOT" projects/working/template_bioinformatics_project
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/template_bioinformatics_project --skip-manuscript-hydration
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/template_bioinformatics_project
```

The external engine uses the Git indexes for provenance. The scaffold checkout
receives the combined PDF in `output/pdf/`, the HTML at `output/web/index.html`,
and validation and provenance receipts in `output/reports/`.
