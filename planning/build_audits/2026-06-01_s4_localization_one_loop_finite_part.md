# 2026-06-01 S4 Localization One-Loop Finite-Part Pass

## Scope

This pass advances the Volume VII supersymmetric-localization depth lane.  The
chapter already proved the \(H\)-function product and stated the \(S^4\)
vector/hypermultiplet determinant.  The missing local bridge was the
finite-part operation that turns the regulated mode product into the displayed
\(H\)-powers.

## Manuscript Changes

- Added the finite-cutoff raw determinant
  \(D_{\kappa,N}^{\rm raw}(x)=\prod_{n\le N}(n^2+x^2)^{\kappa n}\).
- Separated the \(x\)-independent determinant normalization from the
  Coulomb/mass-dependent finite part.
- Made the logarithmic subtraction
  \(\kappa x^2\sum_{n\le N}1/n\) explicit as a quadratic local counterterm in
  the rigid vector or flavor background.
- Identified the determinant-sector ledger: vector root pairs carry
  \(\kappa=2\); full hypermultiplet weights carry \(\kappa=-1\).
- Kept the full field-theoretic equality to the localized path integral at the
  compact supersymmetric localization datum / regulator boundary.

## Calculation Check

`calculation-checks/susy_localization_matrix_checks.py` now checks the
finite-part determinant identity at finite cutoff and the finite-cutoff
\(\mathcal N=4\) root-pair cancellation of \(H\)-factors.

## Verification

Clean in this pass:

- `python3 calculation-checks/susy_localization_matrix_checks.py`
- `python3 -m py_compile calculation-checks/susy_localization_matrix_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/build_monograph.sh`

The rebuilt manuscript is `monograph/tex/main.pdf`.
