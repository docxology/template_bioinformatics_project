# Bioinformatics Project Template

This repository serves as a standard template for organizing bioinformatics projects.
It ensures reproducibility, clear separation of data and code, and organized outputs.

## Directory Structure

- `data/`
  - `raw/`: Immutable raw data. Treat everything in this folder as read-only.
  - `processed/`: Cleaned and processed data ready for analysis.
- `scripts/`: Source code for data processing and analysis.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and visualization.
- `results/`: Output from scripts and notebooks (e.g., final tables, figures).
- `logs/`: Execution logs and pipeline output logs.
- `config/`: Configuration files (YAML, JSON).

## Reproducibility

1.  **Environment**: Define requirements in a `requirements.txt` or `conda.yaml` file natively in the root directory.
2.  **Configuration**: Store variables in `config/` rather than hardcoding them in scripts.
3.  **Logs**: Always write logging outputs to the `logs/` directory for debugging.
