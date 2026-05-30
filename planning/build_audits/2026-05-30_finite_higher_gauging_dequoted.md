# Finite Higher-Gauging Proof Pass

Date: 2026-05-30

Issue context:

- Advances #698, the TQFT/generalized-symmetry quoted-theorem proof-debt
  cluster.

Scope:

- `monograph/tex/volumes/volume_ix/chapter11_higher_group_symmetry_symmetry_tft.tex`
- `planning/chapter_dossiers/volume_ix/chapter11_higher_group_symmetry_symmetry_tft.md`
- `calculation-checks/finite_higher_gauging_checks.py`
- `calculation-checks/README.md`

Substantive changes:

- Replaced the finite higher-gauging `quotedtheorem` by a local theorem and
  proof for the finite cochain/topological-defect mechanism.
- Corrected the condensation-defect normalization from a purely cellular
  `|C^1|^{-1}` gauge-volume convention to the finite groupoid normalization
  `|C^0|/|C^1|`, explicitly accounting for degree-zero gauge-for-gauge data.
- Proved the fusion law
  `C(Y)^2 = Z^{(2)}_{Z_N}(Y) C(Y)` with
  `Z^{(2)}_{Z_N}(Y)=|C^0||Z^2|/|C^1|=|H^0||H^2|/|H^1|`.
- Preserved the QFT scope boundary: the theorem assumes anomaly-free
  topological one-form symmetry surfaces and junctions.  Constructing those
  surfaces in a given continuum interacting theory remains a separate QFT
  construction problem.

Verification plan:

- Run the new finite higher-gauging calculation check.
- Run the standard TeX/prose/theorem/dossier audits and rebuild the monograph.
