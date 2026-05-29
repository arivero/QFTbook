# 2026-05-27 Volume I Haag--Ruelle Introductory Formalization

## Scope

This pass continues issue #615 by upgrading Volume I, Chapter 12 from an
introductory Cook-estimate narrative toward labeled propositions with proof
blocks.  The theorem-level vacuum-net Haag--Ruelle proof remains in Volume IV,
Chapter 5; this pass strengthens the Volume I point-field layer that feeds
that theorem.

## Manuscript Changes

- Added the mass-shell spectral calculation proving that the phase in \(h_t\)
  cancels the translation phase and gives \(P_1B_t(h)\Omega=W_1(bh)\).
- Added Proposition `prop:hr-velocity-tube-separation`, proving rapid
  off-tube decay by nonstationary integration by parts and linear spacelike
  separation for disjoint velocity-support tubes.
- Rewrote Proposition `prop:haag-ruelle-cook-limits` as an explicit
  conditional Cook theorem with integrable derivative bounds and recursive
  scalar-product contraction estimates among its hypotheses.
- Corrected the surrounding prose from "preceding theorem" to "preceding
  proposition" and removed vague dependence on unstated assumptions.

## Companion Checks

- Added `calculation-checks/haag_ruelle_velocity_checks.py`.
- The script checks the finite convention algebra behind the new Chapter 12
  propositions: positive-energy phase cancellation, subluminal massive group
  velocity, velocity-tube separation arithmetic, and the nonstationary
  phase-gradient lower bound.
- Updated the calculation-check README and the Chapter 12 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/haag_ruelle_velocity_checks.py`
- `python3 -m py_compile calculation-checks/haag_ruelle_velocity_checks.py`
- weak-language scan on the edited chapter, dossier, audit note, check script,
  and calculation-check README
- long-line scan on the edited chapter, dossier, audit note, check script, and
  calculation-check README
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2110 pages
