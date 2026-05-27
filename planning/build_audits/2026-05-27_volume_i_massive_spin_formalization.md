# 2026-05-27 Volume I Massive Spin Formalization

## Scope

Issue #615 asks for the substantial Volume I chapters to be upgraded from
flowing derivations to labeled theorem/proof structure.  This pass targets
Volume I, Chapter 15, because massive Wigner rotations, spin-frame covariance,
covariant field intertwiners, and spinor projectors set the normalization and
sign conventions used by spinorial LSZ and later gauge-theory chapters.

## Manuscript Changes

- Added a definition of the massive one-particle spin datum, including
  \(\Hilb_1\), the mass shell \(\Sigma_m^+\), covariantly normalized
  generalized states, and the finite spin label space.
- Added definitions for the standard rest momentum, standard boost section,
  delta-normalized half-density factor, and Wigner rotation.
- Proved the massive Wigner transformation law in covariant and
  delta-normalized conventions, including the mass-shell Jacobian.
- Proved the \(SU(2)\) covering-group spin-label statement, including the
  \(2\pi\)/\(4\pi\) central-sign distinction.
- Added a definition of a massive spin frame over the mass shell.
- Proved the Wigner cocycle identity and the spin-frame change law
  \(W'=Q(\Lambda p)^{-1}WQ(p)\), with inner-product and amplitude
  invariance under simultaneous component transformations.
- Proved the vacuum-to-particle intertwiner equivariance condition and the
  rest little-group intertwiner criterion for nonzero particle overlap.
- Proved the massive Dirac eigenspace, projector, \(\beta\)-pairing, and
  spin-sum identities in the chapter's mostly-plus conventions.

## Companion Checks

- Added `calculation-checks/massive_spin_checks.py`.
- The script checks exact rational Lorentz algebra for the on-shell boost
  Jacobian and Wigner cocycle, finite \(SU(2)\) central signs, spin-frame
  conjugation and inner-product invariance, the displayed Clifford basis,
  beta-pairing signs, \(\gamma_5\), and the rest-frame spin sums.
- Updated the calculation-check README and the Chapter 15 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/massive_spin_checks.py`
- `python3 -m py_compile calculation-checks/massive_spin_checks.py`
- weak-language scan on the edited chapter, dossier, audit note, check script,
  and calculation-check README
- long-line scan on the edited chapter, dossier, audit note, check script, and
  calculation-check README
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2118 pages
