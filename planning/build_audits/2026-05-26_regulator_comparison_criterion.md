# 2026-05-26 Regulator Comparison Criterion Audit

## Scope

This pass makes the regulator-comparison obligation in Volume XI, Chapter 9 theorem-level precise.

## Mathematical Content

- Added Proposition `prop:spde-regulator-comparison-os-criterion`.
- It considers two cutoff families `mu_N^F` and `mu_N^L` on a Hausdorff locally convex field space with continuous time reflection.
- If `mu_N^F` converges weakly to `mu`, `mu_N^L` is OS-positive at finite cutoff, and bounded cylinder expectations agree between the two regulator families after matching local coordinates, then `mu` is OS-positive.
- The proof applies the comparison to `Q_F = overline{F(Theta phi)} F(phi)`, combines it with weak convergence of the Fourier family and finite-cutoff lattice positivity, and passes to the limit.
- The polynomial part uses bounded truncations `P_R`, uniform integrability of `|P|^2` for both cutoff families, and dominated convergence under `mu` to identify polynomial Schwinger-function limits and polynomial OS inequalities.
- Updated the `Phi^4_2` assembly theorem to point to this criterion.
- Added calculation-check error-budget arithmetic for truncation, comparison, and tail terms.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1539 pages.
- Final log scan found no LaTeX warnings, errors, overfull boxes, or underfull boxes.
