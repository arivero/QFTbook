#!/usr/bin/env bash
#SBATCH --job-name=qft-su3-small-pipeline
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=slurm-%x-%j.out
#SBATCH --error=slurm-%x-%j.err

set -euo pipefail

repo_root="${SLURM_SUBMIT_DIR:-$(pwd)}"
cd "$repo_root"

results_root="${QFT_CLUSTER_RESULTS:-results/cluster}"
run_id="${SLURM_JOB_ID:-local}"
run_dir="$results_root/su3_small_pipeline/$run_id"
mkdir -p "$run_dir"

python_bin="${PYTHON:-python3}"

"$python_bin" - <<'PY'
try:
    import h5py  # noqa: F401
except ModuleNotFoundError as exc:
    raise SystemExit(
        "su3_small_pipeline.sbatch requires h5py because the sampler, flow, "
        "and static-potential bridge exchange HDF5 checkpoints.  Load a "
        "Python environment with h5py, or set PYTHON=/path/to/python."
    ) from exc
PY

"$python_bin" qft_scripts/su3_gauge_4d_metropolis_hdf5.py \
  --L 2 \
  --beta 6.0 \
  --proposal-width 0.05 \
  --therm 2 \
  --sweeps 8 \
  --measure-every 1 \
  --max-r 1 \
  --max-t 2 \
  --seed 6312026 \
  --start cold \
  --output-hdf5 "$run_dir/su3_samples.h5" \
  --samples-csv "$run_dir/wilson_samples.csv"

"$python_bin" qft_scripts/su3_wilson_flow_hdf5.py \
  --input-hdf5 "$run_dir/su3_samples.h5" \
  --steps 8 \
  --step-size 0.01 \
  --measure-every 1 \
  --output-hdf5 "$run_dir/su3_flow.h5"

"$python_bin" qft_scripts/static_potential_from_wilson_loops.py \
  --samples-hdf5 "$run_dir/su3_samples.h5" \
  --block-size 2 \
  --bootstrap-samples 32 \
  --seed 6312027 \
  --output "$run_dir/static_potential.csv"

cat > "$run_dir/manifest.json" <<MANIFEST
{
  "job_id": "$run_id",
  "script": "qft_scripts/cluster/slurm/su3_small_pipeline.sbatch",
  "sampler_hdf5": "su3_samples.h5",
  "flow_hdf5": "su3_flow.h5",
  "static_potential_csv": "static_potential.csv",
  "status": "finished"
}
MANIFEST
