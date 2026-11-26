# Setup and verification

Use Python 3.11 or newer. From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install 'PyYAML>=6.0.1'
```

PyYAML is the shipped CLI's only third-party dependency. The optional
[starter requirements](../requirements.txt) declare dependency floors for
downstream work. The scaffold ships a single script and no workflow runner
configuration or automated test suite.

For normal use, review [the YAML settings](configuration.md) and run
`python scripts/01_process_data.py --config config/default.yaml` from the
repository root. The command writes a log and creates the configured processed
directory. The temporary check below avoids project data and logs.

## Smoke workflow

Run this from the repository root with PyYAML available. The fixture is an
invented table of meadow plot observations. The check verifies the bytes are
unchanged, successful logs append, the processed directory remains empty,
and a missing raw directory causes exit code 1.

```bash
python - <<'PY'
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

repository = Path.cwd()
entrypoint = repository / "scripts/01_process_data.py"
config = repository / "config/default.yaml"
message = "Scaffold smoke complete; no data files were read or processed."

with tempfile.TemporaryDirectory(prefix="scaffold-smoke-") as temporary:
    workspace = Path(temporary)
    ready = workspace / "ready"
    missing = workspace / "missing"

    for case in (ready, missing):
        (case / "nested").mkdir(parents=True)
        shutil.copyfile(config, case / "nested/settings.yaml")

    raw = ready / "data/raw"
    raw.mkdir(parents=True)
    fixture = raw / "meadow_plots.tsv"
    original = b"plot_id\tnative_cover_percent\nmeadow-a\t12\nmeadow-b\t35\n"
    fixture.write_bytes(original)

    command = [sys.executable, str(entrypoint), "--config", "nested/settings.yaml"]
    subprocess.run(command, cwd=ready, check=True)
    subprocess.run(command, cwd=ready, check=True)

    assert fixture.read_bytes() == original
    assert list(raw.iterdir()) == [fixture]
    assert list((ready / "data/processed").iterdir()) == []
    assert (ready / "logs/01_process_data.log").read_text().count(message) == 2
    assert not (ready / "results").exists()

    failure = subprocess.run(command, cwd=missing, capture_output=True, text=True)
    assert failure.returncode == 1
    assert "Raw data directory does not exist" in failure.stdout
    assert not (missing / "data/raw").exists()
    assert not (missing / "data/processed").exists()
    assert "Raw data directory does not exist" in (
        missing / "logs/01_process_data.log"
    ).read_text()

print("PASS: raw fixture preserved, logs appended, missing input refused")
PY
```

This checks configuration, directory handling, and logging. The CLI performs
no scientific transformation during the smoke run.
