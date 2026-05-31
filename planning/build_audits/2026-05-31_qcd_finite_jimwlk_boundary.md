# QCD Finite JIMWLK Boundary Pass

Date: 2026-05-31

Scope:
- GitHub issue: #630, QCD rigor uplift.
- Volume II, Chapter 19, small-\(x\) Wilson-line section.

Change:
- Added a finite compact Wilson-line rapidity-evolution datum on
  \(SU(N_c)^{\Lambda_\perp}\), with left-invariant vector fields, a smooth
  positive coefficient matrix, and a divergence-form finite generator.
- Wrote the weak observable equation and the strong density equation and
  derived their equivalence by Haar integration by parts.
- Recorded probability conservation from \(\mathcal H_Y1=0\), and identified
  the dipole observable as the first Balitsky-hierarchy coordinate before any
  large-\(N_c\) or mean-field BK closure.
- Stated the continuum JIMWLK problem as a theorem boundary: one must remove
  the transverse and rapidity regulators while controlling Wilson-line
  observables, the coefficient kernel, and the factorization map to measured
  processes.

Companion check:
- Extended `calculation-checks/qcd_bfkl_small_x_checks.py` with a finite
  torus diffusion model verifying constant preservation, zero integral of the
  divergence-form generator, dissipative Fourier eigenvalues, and weak/strong
  duality for a positive coefficient matrix.

Verification:
- `python3 calculation-checks/qcd_bfkl_small_x_checks.py`
- `python3 -m py_compile calculation-checks/qcd_bfkl_small_x_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The full build/log scan completed cleanly; `main.pdf` rebuilt at 2752 pages.
