# AGENTS.md — `template_bioinformatics_project/scripts`

Follow the repository-root `AGENTS.md`. `01_process_data.py` is the only
entrypoint; PyYAML is its only non-stdlib import. It loads YAML, checks an
existing raw directory, creates the processed directory, and appends a log.
It does not read or write data files or implement biological processing.

Relative config and data paths resolve against the working directory.
Use the root README's temporary-fixture smoke workflow; verify raw bytes
are unchanged and no processed data is produced. Keep success messages
explicit about the stub boundary. Number downstream scripts `NN_name.py`;
their scientific methods require separate validation.
