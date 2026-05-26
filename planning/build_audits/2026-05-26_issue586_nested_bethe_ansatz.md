# Build Audit: Issue #586 Nested Bethe Ansatz

## Scope

- Added `monograph/tex/volumes/volume_vi/chapter04a_algebraic_bethe_ansatz_transfer_matrices.tex`.
- Added `monograph/tex/volumes/volume_vi/chapter04b_nested_bethe_ansatz_matrix_bethe_yang.tex`.
- Added `monograph/tex/volumes/volume_vi/chapter05b_nested_tba_tq_relations_and_separation_variables.tex`.
- Inserted the chapters into `monograph/tex/volumes/volume_vi/volume_vi_current.tex`.
- Added `calculation-checks/nested_bethe_ansatz_checks.py`.
- Updated calculation-check README, Volume VI chapter dossiers, and the
  stringbook crosswalk.

## Mathematical Content

- RTT relation derived from Yang--Baxter by site-by-site commutation.
- Transfer-matrix commutativity proved by auxiliary trace cyclicity.
- \(XXX_{1/2}\) algebraic Bethe ansatz developed through the unwanted-term
  cancellation proof of the Bethe equations.
- Matrix Bethe--Yang states defined with internal transfer-matrix eigenvalues.
- \(SU(N)\) nested equations stated with level-by-level pole-cancellation
  proof and an explicit \(SU(3)\) nested-root solution.
- Nested TBA variational equations derived for physical and auxiliary
  densities.
- Baxter \(TQ\) pole-cancellation equivalence proved for simple roots.

## Verification

- `python3 calculation-checks/nested_bethe_ansatz_checks.py`

Full manuscript audits and build are recorded in the commit workflow that
closes issue #586.
