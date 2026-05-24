# 2026-05-24 Issue #345 Vafa--Witten Measure Hypotheses Audit

## Issue

GitHub issue #345 flagged that the Vafa--Witten positivity discussion
presupposed the existence of the underlying four-dimensional Yang--Mills/QCD
Euclidean measure and did not sharply state the needed lattice reflection
positivity hypothesis.

## Edits

- Strengthened `hyp:vafa-witten-measure-data` in the global-anomalies,
  spontaneous-symmetry-breaking, and pion chapter.
- Distinguished finite-regulator measures \(\dd\nu_{m,\Lambda}\) from a
  continuum limiting functional or measure \(\dd\nu_m\).
- Stated that a continuum Vafa--Witten conclusion requires convergence of the
  relevant gauge-invariant Schwinger functions and order-parameter source
  functionals.
- Required reflection positivity for the full regulator measure, including
  gauge action and vectorlike fermion regulator or determinant, with positivity
  preserved by the limiting Schwinger functions.
- Generalized determinant positivity to the chosen fermion regulator: continuum
  anti-Hermitian eigenvalue pairing is one realization; lattice formulations
  require the corresponding vectorlike positivity condition.
- Added text that Wilson plaquette reflection positivity is a special
  finite-lattice property and that arbitrary regulators or gauge-fixed
  formulae do not automatically inherit it.
- Reiterated that the finite-lattice positivity argument is not itself a
  construction of continuum QCD; the continuum measure/scaling-limit problem is
  part of the four-dimensional Yang--Mills/QCD construction problem.
- Updated the chapter dossier with the new symbols and issue #345 boundary.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 754 pages.
