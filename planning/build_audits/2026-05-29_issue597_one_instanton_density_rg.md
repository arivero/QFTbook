# Issue #597 One-Instanton Density Scale And RG Factors

Date: 2026-05-29.

Scope:

- Advanced issue #597 in
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Strengthened the BPST instanton section by deriving the universal
  one-loop scale and running-coupling factors in the one-instanton density.

Manuscript content:

- Added subsection `Scale and Running-Coupling Content of the One-Instanton
  Density`.
- Separated the finite determinant constant from the universal density
  factors fixed by scale covariance, zero-mode normalization, and RG
  invariance.
- Derived the scale-invariant translation-size measure
  `d^4 a d rho / rho^5`.
- Derived the zero-mode coupling power
  `(8 pi^2 / g_ht^2)^(2 N_c)` from the `4 N_c` bosonic zero modes.
- Proved the one-loop RG exponent `(mu rho)^b0` with
  `b0 = 11 N_c/3 - 2 N_f/3`.
- Updated the local QCD 't Hooft vertex coefficient so the coupling power,
  scale power, scheme constant, and higher-loop corrections are logically
  separated.

Companion checks:

- Extended `calculation-checks/bpst_instanton_normalization_checks.py` with
  finite checks for the center-size measure dimension, the zero-mode
  `g`-power, and the one-loop RG exponent.
- Updated `calculation-checks/README.md`.
- Updated the Volume II anomaly chapter dossier and `claude_review.md`.

Verification:

- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
  passed.
- `python3 -m py_compile
  calculation-checks/bpst_instanton_normalization_checks.py` passed.
- `git diff --check` passed before the monograph build.
- `python3 tools/audit_theorem_form.py` passed.
- `python3 tools/audit_negative_scope_prose.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed with a clean log scan; the resulting PDF
  was `monograph/tex/main.pdf` at 2544 pages.

Backlog impact:

- This pass strengthens the instanton-measure component of #597.
- Issue #597 remains open because the dedicated soliton, monopole, and
  instanton chapters still require full ADHM measure development,
  determinant constants in specified schemes, compactification/boundary
  strata, multi-instanton geometry, and soliton quantization examples.
