# Build Audit: Pure SYM Instanton Condensate Logic

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issues: #562 and #606, with a partial instanton-method cross-link to #597.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Companion files:
  - `calculation-checks/susy_n1_pure_sym_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph source:
  Section~`sec:bpst-instanton-thooft-vertex` for the BPST instanton and
  fermion-zero-mode normalization.
- The pass follows the user's requested convention discipline for
  supersymmetric field theory and does not use superstring compactification,
  D-brane, or holographic input.

## Substantive Changes

- Added a pure-SYM one-instanton zero-mode proposition in the gaugino
  condensation section.
- Proved that the charge-one \(SU(N_c)\) instanton has \(2N_c\) adjoint
  gaugino zero modes and that separated correlators with fewer than \(N_c\)
  insertions of \(S\) vanish at the Berezin-integral level.
- Identified the first possible saturated chiral instanton test as the
  \(N_c\)-point \(S\)-correlator, whose dimension and anomalous-charge ledger
  match \(S^{N_c}\sim\Lambda_h^{3N_c}\).
- Added an explicit hypothesis for the analytic controls absent from the
  zero-mode count alone: instanton-size integration, nonzero-mode
  determinant, collision singularities, and boundary strata.
- Proved the cluster-extraction step separately: if a massive pure phase
  exists and the \(N_c\)-point chiral correlator clusters, the instanton input
  gives only the root equation for the condensate; branch selection and
  existence of pure phases require the anomaly, index, and massive-branch
  inputs already stated in the chapter.
- Extended the pure-SYM calculation check to cover zero-mode saturation,
  \(S^{N_c}\) dimension/charge matching, and branch independence of the
  clustered \(N_c\)-point power.

## Verification

- `python3 calculation-checks/susy_n1_pure_sym_checks.py` passed.
- `python3 -m py_compile calculation-checks/susy_n1_pure_sym_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram Language
  gamma-trace backend.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; final `main.pdf` has 1800 pages and
  size 7182981 bytes.

## Status

This pass converts a common folklore step in the gaugino-condensate story
into a precise logical ledger.  It does not claim a fully regularized
instanton-measure theorem for pure SYM and does not close #597.
