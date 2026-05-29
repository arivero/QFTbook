# Volume VI Ising Form-Factor Reconstruction Pass

Date: 2026-05-29.

GitHub issues advanced:

- #562, assertion-passing-as-derivation.
- #564, promised examples and computations.

Manuscript scope:

- Strengthened `monograph/tex/volumes/volume_vi/chapter04_form_factor_bootstrap_local_operators.tex`.
- Added Proposition `prop:ising-spin-separated-euclidean-series`, a
  separated-point Euclidean reconstruction theorem for the free Majorana
  Ising branch-field form-factor families.
- The new result starts from the explicit even spin family
  `F_{2k}^{sigma_+} = bar sigma i^k P_{2k}` and the odd twist/order family
  `F_{2k+1}^{Sigma} = v i^k P_{2k+1}`.
- It defines the one-particle Euclidean majorant
  `I_m(r)=int dtheta/(2 pi) exp(-m r cosh theta)=K_0(m r)/pi`.
- It proves absolute convergence of the even and odd finite-particle
  spectral series for every `r>0`, with majorants
  `|bar sigma|^2 cosh I_m(r)` and `|v|^2 sinh I_m(r)`.
- It proves uniform convergence of all `r`-derivatives on compact subsets of
  `r>0` by controlling polynomial `cosh(theta)` factors with a smaller
  exponential.
- The scope boundary is stated constructively: this is a separated-point
  reconstruction theorem for this free model; collision-diagonal extensions
  and general factorizing-S-matrix local reconstruction remain the open
  problem stated in the chapter.

Companion checks:

- Extended `calculation-checks/ising_form_factor_checks.py` with exact
  rational checks for the even/odd exponential majorant coefficient split,
  plus numerical checks of the real-rapidity `|tanh(delta/2)| <= 1` product
  input.
- Updated `calculation-checks/README.md`.
- Updated the Volume VI Chapter 4 dossier.

Verification:

- `python3 calculation-checks/ising_form_factor_checks.py`: passed.
- `python3 -m py_compile calculation-checks/ising_form_factor_checks.py`:
  passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `python3 tools/audit_negative_scope_prose.py`: passed.
- `git diff --check`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; `monograph/tex/main.pdf` rebuilt cleanly
  at 2540 pages.

Backlog impact:

- This removes one concrete Vol VI promised-example gap: the Ising
  spin/twist form-factor families are now carried beyond algebraic axioms to
  a separated Euclidean spectral convergence theorem.
- Issues #562 and #564 remain open because they are cross-volume audit
  issues with other unresolved chapters and examples.
