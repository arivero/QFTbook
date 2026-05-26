# 2026-05-26 't Hooft Line Local Model Pass

## Scope

- Deepened
  `monograph/tex/volumes/volume_ix/chapter03_line_surface_domain_wall_operators.tex`.
- Added
  `calculation-checks/thooft_line_local_model_checks.py`.
- Updated the calculation-check index and the Volume IX Chapter 3 dossier.

## Mathematical Content Added

- Added gauge-covariant endpoint bookkeeping for Wilson intervals.
- Constructed the embedded Dirac monopole local model on northern and southern
  patches of a linking two-sphere, including the transition function
  \(g_{NS}(\varphi)=m(e^{i\varphi})\) and flux normalization.
- Proved the cocharacter criterion for a well-defined magnetic singularity and
  the associated integer Dirac phase for Wilson probes.
- Defined dyonic Wilson--'t Hooft lines as a magnetic cocharacter plus a
  representation of the centralizer \(G_m=Z_G(m(U(1)))\).
- Proved the finite linking phase
  \(\exp(2\pi i(\lambda(m')-\lambda'(m)))\) and the mutual-locality
  condition.
- Proved electric screening by adjoint particles and magnetic screening by
  smooth monopole cores.
- Added the theta-angle Witten-effect automorphism with the invariant
  quadratic-form map \(I:X_*(T)\to X^*(T)\), and proved preservation of the
  Dirac pairing.
- Added a Cartan surface-operator local model with \(\alpha\)-holonomy,
  optional \(\eta\)-parameter, and a proof of gauge equivalence under Weyl
  transformations and cocharacter shifts.

## Verification

- Passed: `python3 calculation-checks/thooft_line_local_model_checks.py`.
- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
- Confirmed: `monograph/tex/main.pdf` builds to 1357 pages by `pdfinfo`.
