# Issue #597 Charge-One ADHM Chart Pass

Date: 2026-05-29.

Scope:

- Advanced GitHub issue #597 in
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Filled in the finite-dimensional ADHM construction behind the
  charge-one instanton size and orientation coordinates.

Manuscript content:

- Added Proposition `prop:k-one-adhm-chart-orientation-orbit`.
- Derived the centered `k=1` ADHM equations from the vector spaces
  `K = C` and `W = C^{N_c}`:
  `IJ=0` and `II^\dagger-J^\dagger J=0`, modulo the ADHM `U(1)`.
- Identified the positive-size data with orthogonal equal-norm vectors
  `(u,v)` in `W`, and the fixed-size quotient with
  `U(N_c)/(U(N_c-2) x U(1))`.
- Treated the `N_c=2` specialization separately as the usual
  `SU(2)/Z_2` orientation orbit, avoiding the meaningless `SU(0)` notation.
- Added the cone-structure calculation, later demoted from corollary form while
  retaining the radial cone volume factor
  `rho^{4N_c-5} d rho d Omega_{N_c}` and identifying `rho=0` as the
  small-instanton boundary where the two-frame collapses.

Companion checks:

- Extended `calculation-checks/bpst_instanton_normalization_checks.py` with
  exact integer checks for:
  - full `k=1` ADHM dimension `4N_c`,
  - centered cone dimension `4N_c-4`,
  - orientation dimension `4N_c-5`,
  - homogeneous-orbit dimension,
  - cone radial volume power.
- Updated `calculation-checks/README.md`.
- Updated the anomaly chapter dossier and `claude_review.md`.

Verification:

- `python3 calculation-checks/bpst_instanton_normalization_checks.py` passed.
- `python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py`
  passed.
- `git diff --check` passed.
- `python3 tools/audit_theorem_form.py` passed.
- `python3 tools/audit_negative_scope_prose.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed with a clean log scan.  The built
  monograph PDF had 2548 pages at this checkpoint.

Backlog impact:

- This pass removes one structural gap in the instanton-measure foundation:
  the size and orientation variables are now constructed from ADHM data rather
  than stated by orbit dimension alone.
- Issue #597 remains open.  The remaining work includes determinant constants
  in specified schemes, multi-instanton ADHM geometry, compactification and
  boundary-stratum analysis beyond `k=1`, and additional soliton
  quantization examples.
