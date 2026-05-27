# 2026-05-26 Volume VIII Chapter 5 Cohomological Field Theories Depth Pass

Status: completed and pushed-ready.

## Scope

- Rewrote the cohomological field theory chapter from a short template into a
  regulator-level construction.
- Added the full regulated cohomological datum:
  insertion algebra, \(Q_\Lambda\), action/state, cycle, closure
  \(Q_\Lambda^2=B_\Lambda\), invariant subalgebra, and Ward identity.
- Added anomaly and boundary-term decomposition for failed Ward identities.
- Proved metric independence from a full \(Q\)-exact metric-response
  insertion, including contact-term representatives.
- Proved \(Q\)-exact deformation independence for normalized correlators.
- Added a compact finite-dimensional localization theorem with explicit
  normal equivariant Euler factor and proof by finite-dimensional Stokes,
  exponential suppression, and normal Gaussian/Berezin integration.
- Developed the Mathai-Quillen model with the auxiliary Gaussian sign,
  Thom-form interpretation, Euler class, and transverse zero-locus formula.
- Added descent packages and proved integrated descendants are \(Q\)-closed
  and homology-invariant up to \(Q\)-exact shifts.
- Added Cartan equivariant closure and the Hamiltonian \(S^1\) model.
- Added the BV formulation of cohomological gauge theories through the
  quantum master equation and BV Stokes.
- Identified Donaldson-Witten theory as the gauge-equivariant
  Mathai-Quillen model for \(F_A^+\), leaving detailed four-manifold data to
  the later chapter.

## Calculation Check

- Added `calculation-checks/cohomological_field_theory_checks.py`.
- The check verifies \(d_C^2=-u\mathcal L_v\), equivariant closure of
  \(\omega+u\mu\), Mathai-Quillen square completion, and rank-one zero-locus
  orientation.

## Verification

- `python3 calculation-checks/cohomological_field_theory_checks.py`
  passed with
  `All cohomological field-theory algebra checks passed.`
- `python3 -m py_compile calculation-checks/cohomological_field_theory_checks.py`
  passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before the audit update.
- `tools/build_monograph.sh` completed cleanly, including log scan.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1806`.
