#!/usr/bin/env bash
#SBATCH --job-name=qft-su3-sweep
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=01:00:00
#SBATCH --array=0-8
#SBATCH --output=slurm-%x-%A_%a.out
#SBATCH --error=slurm-%x-%A_%a.err

set -euo pipefail

repo_root="${SLURM_SUBMIT_DIR:-$(pwd)}"
cd "$repo_root"

python_bin="${PYTHON:-python3}"
betas="${QFT_SWEEP_BETAS:-5.7,5.9,6.1}"
seeds="${QFT_SWEEP_SEEDS:-631101,631102,631103}"
task_id="${SLURM_ARRAY_TASK_ID:-0}"

eval "$("$python_bin" qft_scripts/cluster/su3_sweep_grid.py \
  --betas "$betas" \
  --seeds "$seeds" \
  --task-id "$task_id" \
  --format env)"

results_root="${QFT_CLUSTER_RESULTS:-results/cluster}"
array_id="${SLURM_ARRAY_JOB_ID:-local-array}"
run_dir="$results_root/su3_parameter_sweep/$array_id/task_${QFT_SWEEP_TASK_ID}"
mkdir -p "$run_dir"

"$python_bin" - <<'PY'
try:
    import h5py  # noqa: F401
except ModuleNotFoundError as exc:
    raise SystemExit(
        "su3_parameter_sweep_array.sbatch requires h5py for checkpointed "
        "HDF5 data exchange. Load a Python environment with h5py, or set "
        "PYTHON=/path/to/python."
    ) from exc
PY

"$python_bin" qft_scripts/su3_gauge_4d_metropolis_hdf5.py \
  --L "${QFT_SWEEP_L:-2}" \
  --beta "$QFT_SWEEP_BETA" \
  --proposal-width "${QFT_SWEEP_PROPOSAL_WIDTH:-0.05}" \
  --therm "${QFT_SWEEP_THERM:-4}" \
  --sweeps "${QFT_SWEEP_SWEEPS:-16}" \
  --measure-every "${QFT_SWEEP_MEASURE_EVERY:-1}" \
  --max-r "${QFT_SWEEP_MAX_R:-1}" \
  --max-t "${QFT_SWEEP_MAX_T:-2}" \
  --seed "$QFT_SWEEP_SEED" \
  --start "${QFT_SWEEP_START:-cold}" \
  --output-hdf5 "$run_dir/su3_samples.h5" \
  --samples-csv "$run_dir/wilson_samples.csv"

"$python_bin" qft_scripts/su3_wilson_flow_hdf5.py \
  --input-hdf5 "$run_dir/su3_samples.h5" \
  --steps "${QFT_SWEEP_FLOW_STEPS:-8}" \
  --step-size "${QFT_SWEEP_FLOW_STEP_SIZE:-0.01}" \
  --measure-every "${QFT_SWEEP_FLOW_MEASURE_EVERY:-1}" \
  --output-hdf5 "$run_dir/su3_flow.h5"

"$python_bin" qft_scripts/static_potential_from_wilson_loops.py \
  --samples-hdf5 "$run_dir/su3_samples.h5" \
  --block-size "${QFT_SWEEP_BLOCK_SIZE:-2}" \
  --bootstrap-samples "${QFT_SWEEP_BOOTSTRAP_SAMPLES:-32}" \
  --seed "$((QFT_SWEEP_SEED + 1))" \
  --output "$run_dir/static_potential.csv"

cat > "$run_dir/manifest.json" <<MANIFEST
{
  "array_job_id": "${SLURM_ARRAY_JOB_ID:-local-array}",
  "array_task_id": "$QFT_SWEEP_TASK_ID",
  "grid_size": "$QFT_SWEEP_GRID_SIZE",
  "beta": "$QFT_SWEEP_BETA",
  "seed": "$QFT_SWEEP_SEED",
  "beta_index": "$QFT_SWEEP_BETA_INDEX",
  "seed_index": "$QFT_SWEEP_SEED_INDEX",
  "script": "qft_scripts/cluster/slurm/su3_parameter_sweep_array.sbatch",
  "sampler_hdf5": "su3_samples.h5",
  "flow_hdf5": "su3_flow.h5",
  "static_potential_csv": "static_potential.csv",
  "status": "finished"
}
MANIFEST
