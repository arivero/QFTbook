# Volume VI Factorized-Scattering Formalization Audit

## Scope

- Strengthened `monograph/tex/volumes/volume_vi/chapter01_factorized_scattering_and_integrability.tex`.
- Added the rapidity chart and ordered-chamber definition, with the
  mostly-plus invariant \(s_{ab}=-(p_a+p_b)^2\).
- Promoted the chamber-transition logic to a proposition: unitarity and the
  Yang--Baxter equation are exactly the local relations needed for
  path-independent chamber continuation.
- Promoted the Zamolodchikov--Faddeev associativity statement and Watson
  exchange statement to propositions with proofs.
- Added \(S\)-symmetric finite-particle wavefunctions and a well-defined
  extension proposition.
- Corrected the adjacent Chapter 2 rapidity-kinematics sign display from
  \((p_a+p_b)^2\) to \(-\bigl(p_a+p_b\bigr)^2\) in mostly-plus signature.
- Added `calculation-checks/factorized_scattering_algebra_checks.py`.

## Verification

Run on 2026-05-28:

```sh
python3 calculation-checks/factorized_scattering_algebra_checks.py
python3 -m py_compile calculation-checks/factorized_scattering_algebra_checks.py
git diff --check -- monograph/tex/volumes/volume_vi/chapter01_factorized_scattering_and_integrability.tex monograph/tex/volumes/volume_vi/chapter02_two_dimensional_scattering_analyticity_bootstrap.tex calculation-checks/factorized_scattering_algebra_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_vi/chapter01_factorized_scattering_and_integrability.md planning/chapter_dossiers/volume_vi/chapter02_two_dimensional_scattering_analyticity_bootstrap.md planning/build_audits/2026-05-28_volume_vi_factorized_scattering_formalization.md
tools/build_monograph.sh
pdfinfo monograph/tex/main.pdf | rg '^Pages:'
```
