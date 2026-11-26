# Data and output layout

| Directory | Role |
| --- | --- |
| [`data/raw/`](../data/raw/) | Immutable inputs. The CLI only checks the directory's existence. |
| [`data/processed/`](../data/processed/) | Reserved for derived files. The stub creates the directory and leaves its contents alone. |
| [`results/`](../results/) | Reserved for downstream reports and figures. |
| [`logs/`](../logs/) | Append-mode CLI records, including failures. |
| [`notebooks/`](../notebooks/) | Optional exploration workspace. |

The repository tracks placeholders in these directories. Ignored local files
may already exist and should be preserved. Keep raw inputs separate from
logs and derived outputs. The [smoke workflow](development.md#smoke-workflow)
creates its own temporary directories.
