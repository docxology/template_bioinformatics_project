# Harmless verification {#sec:verification}

The smoke workflow runs in temporary working directories. It copies the
YAML configuration into a nested directory and places an invented table
of meadow plot observations under the raw path. Successful runs preserve
the raw table byte for byte, create the processed directory with no data
files, and append a completion record to the run log. A separate run with
no raw directory exits with an error, records the failure, and leaves both
the raw and processed paths absent.

The invented observations are sentinels for input preservation. The
scaffold does not open or analyze their values.
