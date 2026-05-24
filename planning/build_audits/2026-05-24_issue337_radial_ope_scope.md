# 2026-05-24 Issue #337 Radial OPE Scope Audit

## Issue

GitHub issue #337 asked for the OPE convergence theorem to be tied explicitly
to Chapter 4's radial reconstruction hypotheses, rather than relying on an
implicit phrase such as reflection-positive CFT.

## Edits

- Added `def:radial-ope-convergence-hypotheses` to Volume III, Chapter 9.
- The definition lists the Euclidean ingredients used by the radial OPE
  theorem: Schwinger distributions with contact prescriptions, radial
  reflection positivity, the null quotient and Hilbert completion,
  nonnegative self-adjoint \(D_{\rm rad}\) with discrete finite-multiplicity
  spectrum, and radial local completeness.
- The definition also states that Lorentzian OPE statements additionally use
  the tube-domain analytic continuation, spectrum condition, and local
  commutativity part of `hyp:radial-reconstruction-data`.
- Updated the Chapter 9 dossier accordingly.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; rebuilt
  `monograph/tex/main.pdf` at 745 pages.
