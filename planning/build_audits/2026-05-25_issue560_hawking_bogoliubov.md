# 2026-05-25 Issue 560: Hawking Bogoliubov Coefficients

## Scope

Issue #560 flagged that Volume XII Chapter 5 described Hawking mode mixing
but did not display the Bogoliubov coefficient calculation.

## Edits

- Replaced the short Bogoliubov-mechanism section by a collapse mode-tracing
  derivation using \(v_0-v=C e^{-\kappa u}\).
- Defined the in/out null modes and the Klein-Gordon product on null
  infinity.
- Displayed the Fourier transforms of \(x^{i\omega/\kappa}\) against
  positive and negative frequencies.
- Derived the explicit singular coefficients, their thermal ratio, the
  \(|\Gamma(i a)|^2=\pi/(a\sinh\pi a)\) identity, and the Planck factor in
  \(|\beta_{\omega\omega'}|^2\).
- Clarified that the continuous coefficient has a \(1/\omega'\)
  normalization density and that finite particle numbers require wave
  packets.
- Added the trans-Planckian precursor-frequency estimate and the moving
  mirror analogue.
- Added `calculation-checks/hawking_bogoliubov_checks.py` to verify the
  Gamma-function and normalization identities used in the displayed
  derivation.
- Updated the Volume XII Chapter 5 dossier and calculation-check README.

## Targeted Verification

- `python3 calculation-checks/hawking_bogoliubov_checks.py`

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The first build pass caught use of `\mathscr` in the new null-infinity
notation; the chapter was corrected to use `\mathcal I^\pm`, consistent with
the current preamble.  The rerun completed cleanly, and the rebuilt PDF has
1285 pages.
