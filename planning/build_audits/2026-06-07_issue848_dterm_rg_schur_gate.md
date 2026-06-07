# 2026-06-07 Issue #848 D-term RG Schur-Complement Audit

## Scope

- Target issue: #848, full Hori--Vafa/mirror QFT data beyond protected
  superpotential coordinates.
- Added `ca:glsm-mirror-dterm-rg-schur-gate` in Vol VII Ch09 after the
  admissible mirror-datum definition.
- Added `check_full_mirror_dterm_rg_schur_gate()` to the GLSM companion and
  registered it in the main check runner.

## Substance

- The new cell treats mirror `D`-term universality as a Wilsonian comparison:
  split the cutoff Hilbert space into retained and eliminated subspaces, then
  compare the Feshbach--Schur effective Hamiltonian and effective source row.
- The finite example uses the same protected low block but different high-mode
  couplings.  It shows that a Hamiltonian counterterm can match the retained
  Hamiltonian while still leaving the low source-resolvent observable wrong
  unless source renormalization is also supplied.
- This targets physics/QFT data: fluctuation/measure effects, counterterms, and
  source-normalized correlators.  It is not another protected residue identity
  or an authority-based Hori--Vafa derivation.

## Quality Boundary

- The pass does not prove Hori--Vafa mirror equivalence, classify all mirror
  `D`-terms, or construct the continuum RG flow.  It supplies a finite
  adversarial gate that any claimed `D`-term universality argument must pass.
- The TeX receives only mathematical/QFT content.  Issue, review, directive,
  and process notes remain confined to planning and companion metadata.
- The scope is intentionally aligned with the user's instanton warning: the
  useful depth lies in fluctuation/measure/source transport, not in adding
  tangential protected-sector algebra.

## Verification Plan

- Focused Python compile and GLSM checks.
- Focused Vol VII Ch09 theorem/display/text/negative-scope/style/leakage
  audits.
- Evidence-contract, inventory, dossier, JSON, and diff-whitespace audits.
- Full calculation-check suite and full monograph build.
