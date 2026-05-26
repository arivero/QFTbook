# 2026-05-26 Volume VI Finite-Volume Form-Factors Depth Pass

Scope: comprehensive depth pass on Volume VI, Chapter 11, which was flagged
as a remaining thin integrable-QFT chapter.  The pass focuses on deriving the
finite-volume normalization and spectral-expansion formulas used by form
factor/TFFSA methods.

## Manuscript Changes

- Rewrote the chapter around finite-volume Hilbert-space normalization.
- Proved Bethe-Yang quantization by moving one particle around the circle and
  collecting diagonal scattering phases.
- Defined the Gaudin matrix and density, including the explicit two-particle
  determinant.
- Proved the Bethe-state counting measure from the Jacobian of the
  Bethe-Yang map.
- Proved the off-diagonal finite-volume form-factor formula under explicit
  regularity and no-coincident-rapidity hypotheses.
- Proved cancellation of the Gaudin determinant in the infinite-volume
  two-point sum.
- Defined connected diagonal form factors through kinematic-pole subtraction.
- Proved the finite-volume diagonal subset formula using principal Gaudin
  minors.
- Displayed the one- and two-particle diagonal formulas explicitly.
- Derived the zero-temperature spectral expansion and stated a sufficient
  Euclidean convergence criterion.
- Added the free-Majorana energy-density two-particle example, including the
  center/relative rapidity transformation and Bessel-kernel prefactor.
- Restated the Leclair-Mussardo type thermal series with its TBA and
  connected-diagonal dependencies explicit.

## Calculation Checks

Added `calculation-checks/finite_volume_form_factor_checks.py`, which checks:

- the two-particle Gaudin determinant against the displayed formula;
- cancellation of the Gaudin density between finite-volume matrix elements
  and the state-counting measure;
- connected diagonal subset expansion through three particles;
- the \(2^n\) subset count used in diagonal disconnected-contraction
  bookkeeping;
- the free-Majorana two-particle Bessel-reduction prefactor.

The calculation-check README and Volume VI chapter dossier were updated.

## Verification

Completed before commit:

- `python3 calculation-checks/finite_volume_form_factor_checks.py`
- `python3 -m py_compile calculation-checks/finite_volume_form_factor_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The build completed with a clean log scan and produced
`monograph/tex/main.pdf` with 1786 pages.
