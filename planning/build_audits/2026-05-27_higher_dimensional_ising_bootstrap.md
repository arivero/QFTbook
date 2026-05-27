# Build Audit: Higher-Dimensional Ising Bootstrap Datum

## Scope

- Branch: `codex/higher-dimensional-cft`
- Base after rebase: `origin/main` at `9ce8e9e6`.
- Issue context: #606 broad depth/rigor audit, applied here to
  higher-dimensional CFT and the three-dimensional Ising bootstrap interface.
- Files touched:
  - `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`
  - `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`
  - `calculation-checks/conformal_block_companion.py`
  - `calculation-checks/ising_mixed_bootstrap_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`
  - `planning/chapter_dossiers/volume_ii/chapter15_wilson_fisher_fixed_point_scaling_operators.md`
  - `planning/build_audits/2026-05-27_higher_dimensional_ising_bootstrap.md`

## Content

This pass adds a self-contained higher-dimensional mixed-correlator bootstrap
datum for the scalar pair used in the three-dimensional Ising CFT.  Volume III,
Chapter 9 now states the \(\mathbb Z_2\)-graded hypotheses on
\(\sigma,\varepsilon\), derives the spin-\(\ell\) exchange sign, defines the
\(\mathsf F_\pm^{ij,kl}\) crossing kernels, proves the five scalar crossing
equations, packages them as the standard five-vector semidefinite-programming
system, and proves the finite-functional exclusion certificate from reflection
positivity.

The same section states the status boundary for the numerical Ising island:
the crossing and positivity system is monograph-derived, while derivative
truncations, spectral gaps, block approximation, and high-precision SDP
islands remain external or certification-boundary input.  Volume II's
Wilson--Fisher comparison table now points to this derived system while
continuing to treat the displayed \(d=3\) dimensions as external numerical
bootstrap data.

The calculation companion checks the convention-sensitive algebra exactly:
the scalar four-point prefactor ratios, \(F_\pm\) symmetry signs, spin exchange
sign, even-sector positive-semidefinite OPE matrices, and five-vector packing
of the crossing equations.

A follow-up companion script, `conformal_block_companion.py`, provides the
same normalization layer for actual global-block evaluation.  Its automatic
evaluator uses the Dolan--Osborn hypergeometric closed forms in \(D=2\) and
\(D=4\), and the Dolan--Osborn/Hogervorst--Rychkov Casimir recursion for
\(D=3\) or generic \(D>2\) Euclidean radial checks.  The script also exposes
the universal leading radial Gegenbauer/harmonic term and the mixed-correlator
\(F_\pm\) helper.  Two-dimensional Virasoro blocks are noted as a separate
Zamolodchikov-recursion companion task, and production bootstrap runs should
continue to compare against established packages such as PyCFTBoot/SDPB.

## Verification

- `python3 calculation-checks/ising_mixed_bootstrap_checks.py`
- `python3 -m py_compile calculation-checks/ising_mixed_bootstrap_checks.py`
- `python3 calculation-checks/conformal_block_companion.py`
- `python3 -m py_compile calculation-checks/conformal_block_companion.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `9ce8e9e6`, the full calculation harness,
audits, whitespace check, and TeX build/log scan completed cleanly.  The final
PDF has 1974 pages.
