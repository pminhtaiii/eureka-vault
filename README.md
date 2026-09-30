# BBQ local-model results 

This folder contains the curated result artifacts needed for team analysis and reproducibility.

## Use these as the final outputs

For each model under `results/<model>/`:

- `results_final.csv` — row-level predictions for all 58,492 BBQ instances.
- `accuracy_*_CONFIRMED.csv` — final confirmed accuracy summaries.
- `bias_*_PAPER_CORRECTED.csv` — final bias summaries using the BBQ paper definition.
- `POSTPROCESS_CORRECTION_MANIFEST.json` — records that corrected post-processing reused the completed inference output and did not rerun inference.
- `metadata_scoring_audit.json` — audit for metadata used in bias scoring.
- `inference_qc_summary.json` — clean inference-integrity QC.
- `manifest_pre_run.json` — frozen model/protocol metadata.
- `runtime_preflight.json`, `runtime_stats.json` — runtime evidence.

## Shared files

`protocol/` contains the common prompt, parser, grammar, dataset hashes and canonical protocol record.

`summary/model_summary.csv` is the convenient 5-model table for later analysis/plots.
`summary/inference_qc_summary.csv` summarizes full-run integrity.
`summary/results_integrity.csv` verifies each corrected manifest references the exact uploaded `results_final.csv`.

## Do NOT treat old pre-correction bias files as final

Only files ending in `_PAPER_CORRECTED.csv` should be used for final bias analysis.
Only files ending in `_CONFIRMED.csv` should be used for final summarized accuracy.

## Intentionally excluded

This package does not include model GGUFs, `.venv`, llama.cpp runtime binaries, checkpoints,
server logs, old failed metadata diagnostics, or intermediate/pre-correction bias outputs.
Those are not needed for the team repository.

Add the five completed executed notebooks separately under your repository's `notebooks/` folder.
