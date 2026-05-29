# QFT Cluster Workflow Templates

These files are reproducible wrappers for running the reader-facing finite
regulator scripts on a SLURM cluster.  They are deliberately small: the
mathematical content remains in the monograph and in `qft_scripts/`, while
this directory records the remote-execution protocol, checkpoint locations,
and the exact shell commands submitted to SLURM.

The templates do not store passwords or authentication tokens.  For Harvard
RC, copy `rc_env.example` to `rc_env.sh`, edit the user-specific paths, and
open one Duo-approved SSH master connection:

```bash
cp qft_scripts/cluster/rc_env.example qft_scripts/cluster/rc_env.sh
${EDITOR:-vi} qft_scripts/cluster/rc_env.sh
qft_scripts/cluster/rc_open_master.sh
```

The remaining wrappers reuse the authenticated control socket:

```bash
qft_scripts/cluster/rc_sync_push.sh
qft_scripts/cluster/rc_exec.sh sbatch qft_scripts/cluster/slurm/su3_small_pipeline.sbatch
qft_scripts/cluster/rc_sync_pull_results.sh
qft_scripts/cluster/rc_close_master.sh
```

The first SLURM vertical slice is `slurm/su3_small_pipeline.sbatch`.  It runs
a small pure-gauge SU(3) HDF5 sampler, Wilson flow on the saved checkpoint,
and static-potential extraction from the correlated Wilson-loop samples.  The
job is a cluster smoke run, not a production continuum extrapolation.

The first parameter-sweep wrapper is `slurm/su3_parameter_sweep_array.sbatch`.
It uses `su3_sweep_grid.py` to resolve each `SLURM_ARRAY_TASK_ID` into a
finite pair `(beta, seed)`, then runs the same sampler/flow/static-potential
pipeline in a task-local results directory with a JSON manifest.  Override the
default grid with comma-separated environment variables:

```bash
QFT_SWEEP_BETAS=5.7,5.85,6.0 \
QFT_SWEEP_SEEDS=101,102,103,104 \
sbatch --array=0-11 qft_scripts/cluster/slurm/su3_parameter_sweep_array.sbatch
```

The array wrapper is a reproducibility and bookkeeping layer.  It does not
assert Markov-chain mixing, continuum scaling, or independence among nearby
couplings; those are separate analysis claims.
