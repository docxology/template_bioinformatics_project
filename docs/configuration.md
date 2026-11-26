# Configuration

The [default YAML](../config/default.yaml) routes the scaffold's directories.
The working directory is the base for all relative paths, including the
`--config` argument. Keep output and log destinations outside the raw input
directory.

| Setting | Current behavior |
| --- | --- |
| `import_path.data_raw` | Must name an existing directory. |
| `import_path.data_processed` | Created on a successful run. |
| `import_path.logs` | Receives `01_process_data.log` in append mode. |
| `logging.level`, `logging.format` | Configure the file and stdout log handlers. |
| `processing.filtering_threshold` | Included in the log. |
| `processing.threads`, `processing.normalize`, `import_path.results`, `import_path.config` | Reserved for downstream work. |

After changing paths or logging, run the [smoke workflow](development.md#smoke-workflow)
with temporary data.
