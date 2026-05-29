# Issue #519 Back-To-Back EEC Sudakov Pass

Date: 2026-05-29.

Scope:

- Advanced GitHub issue #519 in
  `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`.
- Strengthened the back-to-back endpoint discussion of the QCD
  energy-energy correlator.

Manuscript content:

- Added the impact-parameter convention
  `b_F = 2 exp(-gamma_E)`, `mu_b = b_F / b`, and
  `L_b = log(Q^2 b^2 / b_F^2)`.
- Stated the one-loop quark cusp anomalous dimension in the monograph
  trace-delta convention,
  `Gamma_cusp^q = g^2 C_F / (4 pi^2) + O(g^4)`.
- Added Proposition `Leading Sudakov factor in the back-to-back EEC`.
- Derived the fixed-coupling leading-logarithmic factor
  `exp[- Gamma_cusp^q L_b^2 / 2]` from the cusp-evolution integral
  between `mu_b` and `Q`.
- Added a scope remark separating this universal double logarithm from the
  full endpoint theorem, which still requires rapidity-regulator data,
  finite hard/jet/soft functions, running-coupling improvement, matching to
  fixed separated-angle distributions, and power corrections.

Companion checks:

- Added `calculation-checks/energy_correlator_sudakov_checks.py`, verifying
  `int_0^L u du = L^2/2`, the fixed-coupling differential equation for
  `exp[-Gamma L^2/2]`, and trace-delta/half-trace invariance of the
  one-loop cusp product `g^2 C_F`.
- Updated `calculation-checks/README.md`.
- Updated the Volume II QCD chapter dossier and `claude_review.md`.

Verification:

- `python3 calculation-checks/energy_correlator_sudakov_checks.py` passed.
- `python3 -m py_compile
  calculation-checks/energy_correlator_sudakov_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `python3 tools/audit_theorem_form.py` passed.
- `python3 tools/audit_negative_scope_prose.py` passed.
- `tools/build_monograph.sh` passed with a clean log scan; the resulting PDF
  was `monograph/tex/main.pdf` at 2545 pages.

Backlog impact:

- This pass advances #519 by replacing the previous naming of Sudakov
  resummation with a concrete derivation of the universal leading double
  logarithm.
- Issue #519 remains open because the full modern energy-correlator program
  still requires the renormalized light-ray OPE/mixing theorem, complete
  endpoint matching, high-loop analytic frontier discussion, and further
  CFT/QCD bridge development.
