# Build Audit: Issue #302 Wilson--Fisher Dimensional-Regularization Status

Date: 2026-05-24

Scope:

- `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`
- `planning/chapter_dossiers/volume_ii/chapter15_wilson_fisher_fixed_point_scaling_operators.md`

Issue addressed:

- GitHub #302 asked that the Wilson--Fisher chapter explicitly classify the
  \(D=4-\epsilon\) integrals as dimensional regularization: formal
  coefficient-by-coefficient analytic continuation of Feynman integrals, not a
  field-configuration-space integral in noninteger dimension.  It also asked
  that the beta functions, anomalous dimensions, and scaling dimensions be
  declared formal perturbative series.

Mathematical changes:

- Added Definition `def:wilson-fisher-dimensional-regularization-status` at
  the start of the Wilson--Fisher chapter.
- The definition states that
  \(\int d^{4-\epsilon}\ell\,F(\ell,p,m)\) denotes meromorphic continuation
  in \(D=4-\epsilon\) of finite-dimensional Euclidean loop-momentum graph
  integrals, with subtractions applied coefficient by coefficient.
- The definition states that no field-configuration-space measure in
  noninteger dimension is being constructed in the chapter.
- The definition records that
  \(\beta^\epsilon(\lambda)\), \(\gamma_\phi(\lambda)\),
  \(\gamma_2(\lambda)\), \(\lambda_*(\epsilon)\), and the resulting scaling
  dimensions are formal perturbative objects.  The fixed point is a formal
  branch \(\lambda_*(\epsilon)\in \epsilon\mathbb R[[\epsilon]]\), and
  convergence or summability requires separate input.
- The chapter dossier now records this status in the construction task, claim
  ledger, and audit notes.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.
