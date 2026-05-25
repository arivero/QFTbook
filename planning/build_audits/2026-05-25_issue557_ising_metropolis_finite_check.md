# 2026-05-25 Issue 557: Ising Metropolis Companion Verification

## Scope

Issue #557 flagged that the Monte Carlo chapter lacked a worked numerical
example and Python companions.  The chapter and `qft_scripts/` already contain
the finite two-dimensional Ising Metropolis example.  This pass adds the
missing deterministic finite-volume calculation check for that companion
script.

## Edits

- Added `calculation-checks/ising_metropolis_finite_checks.py`.
- The check imports `qft_scripts/ising2d_metropolis.py`, enumerates all
  \(2^4\) configurations of the \(2\times2\) periodic Ising model, verifies
  that the local energy difference equals the total-energy difference, and
  verifies detailed balance for the full one-spin Metropolis transition
  matrix.
- Updated the Monte Carlo chapter, chapter dossier, and calculation-check
  README to record the finite verification.

## Targeted Verification

```text
python3 calculation-checks/ising_metropolis_finite_checks.py
All finite Ising Metropolis checks passed.

python3 qft_scripts/ising2d_metropolis.py --smoke
{"L": 8, "abs_magnetization_mean": 0.815625, "acceptance": 0.17119140625, "beta": 0.44068679350977147, "energy_per_site_mean": -1.5151041666666667, "energy_per_site_stderr_naive": 0.024194795444574615, "seed": 314159, "sweeps": 160, "tau_int_energy_windowed": 1.8461428181724753, "therm": 40}
```

## Full Verification

```text
tools/audit_monograph_text.sh
Strict monograph text audit clean.

tools/audit_chapter_dossiers.sh
Chapter dossier metadata audit clean.

git diff --check

tools/build_monograph.sh
Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf

pdfinfo monograph/tex/main.pdf
Pages:           1281
```
