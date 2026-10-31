# Bioinformatics Project Template

This repository serves as a **standard template** for organizing bioinformatics projects.
It provides conventions for reproducibility, separation of data and code, and tracking outputs and execution parameters. The shipped processing function is a **stub**, not a biological analysis pipeline.

## Architecture and support boundary

This is an independently authored scaffold, **not one of the canonical
`docxology/template` SDK exemplars**. It has no SDK dependency or version
contract; the root template's 4.5.0 release does not version this repository.
There is no package API, `pyproject.toml`, test suite, or manuscript renderer.
Compose it with other tools through its CLI, YAML settings, and filesystem
directories; any SDK or scientific workflow integration must be implemented
and validated in the downstream project.

## Quickstart

The shipped CLI demonstrates configuration and logging, not scientific processing.

1. **Environment Setup** (use Python 3.11 or newer)
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install 'pyyaml>=6.0.1'
    ```
   This is the minimal environment for the shipped script. Optionally run
   `python -m pip install -r requirements.txt` for the downstream analysis and
   workflow starter stack. Its open-ended dependency floors are not a lockfile
   or a promise of compatibility across every Python version.

2. **Configuration**
   Open `config/default.yaml` to set directory routing and logging. All relative
   paths resolve against the working directory, not the config file's location.
   The threshold is logged only; threads, normalization, results routing, and
   `import_path.config` are reserved settings, not implemented processing.

3. **Execution**
   Run the standard entrypoint from the repository root (`--config` is resolved relative to the current directory):
    ```bash
    python scripts/01_process_data.py --config config/default.yaml
    ```
   The script requires the configured raw directory to exist, creates the
   processed directory, and appends its run log to `logs/01_process_data.log`.
   The processing step is a stub to replace; no **data** files are read or
   written. Missing raw input returns a nonzero status without creating it.

   No `Snakefile` ships with the scaffold — `snakemake` is declared in `requirements.txt` for pipelines you add. There is no automated test suite; the entrypoint script is the smoke check.

## Harmless smoke workflow

With the minimal environment active, run this from the repository root. It
copies the default config into a temporary working directory, exercises the
real CLI on a synthetic fixture, and verifies that raw bytes are unchanged
and no processed data is produced. Temporary artifacts are removed on exit;
repository data and logs are untouched. In a GitVault-managed checkout, run
this command inside the official repository lease described in `AGENTS.md`.

```bash
python - <<'PY'
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

repository = Path.cwd()
with tempfile.TemporaryDirectory(prefix="bioinformatics-smoke-") as temporary:
    workspace = Path(temporary)
    raw = workspace / "data/raw"
    raw.mkdir(parents=True)
    fixture = raw / "fixture.tsv"
    original = b"sample\tvalue\nsmoke\t1\n"
    fixture.write_bytes(original)
    shutil.copyfile(repository / "config/default.yaml", workspace / "config.yaml")
    subprocess.run(
        [sys.executable, str(repository / "scripts/01_process_data.py"),
         "--config", "config.yaml"], cwd=workspace, check=True,
    )
    assert fixture.read_bytes() == original
    assert sorted(entry.name for entry in raw.iterdir()) == ["fixture.tsv"]
    assert list((workspace / "data/processed").iterdir()) == []
    assert "no data files were read or processed" in (
        workspace / "logs/01_process_data.log"
    ).read_text()
    assert not (workspace / "results").exists()
print("PASS: scaffold plumbing only; raw fixture preserved; no scientific output")
PY
```

## Directory Structure

Strict adherence to the directory structure preserves project integrity:

- `data/`
  - `raw/`: **Immutable raw data.** Treat everything in this folder as absolutely read-only.
  - `processed/`: Intermediate cleansed and processed data.
- `scripts/`: Example entrypoint; add and validate downstream processing here.
- `notebooks/`: Jupyter notebooks (`.ipynb`) restricted purely to exploratory data analysis and visualization.
- `results/`: Formatted outputs (e.g., final TSV tables, figures) from scripts and notebooks.
- `logs/`: High-resolution execution logs generated directly by scripts to track state over time.
- `config/`: Pipeline configuration files (YAML, JSON) specifying hyper-parameters and path routing.

## Principles of Reproducibility

1. **No Hardcoding**: All paths and thresholds should route dynamically through `config/` files.
2. **Immutability**: Anything inside `data/raw` must never be modified by a script. Generate altered states into `data/processed`.
3. **Traceability**: All scripts should utilize the standard Python `logging` library mapping `.log` files securely into `logs/`.
