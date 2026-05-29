# Issue #505 RG Gauge And Reconstruction Layer

Date: 2026-05-29.

Scope:

- Strengthened `volume_xi/chapter07_rigorous_renormalization_group.tex` beyond fixed-point coordinate language.
- Added a taxonomy of RG maps distinguishing exact Wilsonian Gaussian pushforward, Wilson-Polchinski differential flow, Wetterich/effective-average-action flow, constructive polymer RG, and tensor RG.
- Added a comparison datum for two RG descriptions requiring an intertwining map and explicit observable-error estimates in declared seminorms.
- Added a critical-surface and continuum-tuning section:
  - defined the intrinsic tuning map `tau` from a local stable graph;
  - proved the local critical surface is finite-codimensional under a stated `C^1` stable-graph hypothesis;
  - derived the exact finite-depth tuning precision `rho L^{-N y_a}` for diagonal linear relevant directions.
- Added a gauge-compatible Wilsonian RG datum with two theorem-level realizations:
  - gauge-invariant lattice pushforward data with blocking kernels, Wilson-line observables, polymer norms, and reflection-positivity control;
  - regularized BV pushforward data preserving the quantum master equation and the observable cochain map.
- Added an RG reconstruction estimate in the strong dual topology of Schwartz distributions.
- Proved that the reconstruction estimates produce distributional limits and pass symmetry, covariance, and reflection positivity through closed limiting inequalities.
- Added a source-extended RG section:
  - defined source-extended RG data and the exact finite-regulator source identity;
  - defined scaling sources and scaling fields through eigen-directions of the linearized source RG map, with gauge-invariant and BV-cohomological qualifications;
  - defined contact terms as distributions supported on collision diagonals;
  - proved separated-point scaling from source-extended RG estimates and showed that any scaling failure of a full-space extension is a contact term.
- Clarified the status distinction between constructive massive/superrenormalizable scalar Wightman theories and the still-open short-range critical Wilson-Fisher fixed-point reconstruction theorem.
- Clarified that four-dimensional scalar `phi^4` perturbation theory is a formal coordinate system; the UV-complete nonperturbative completion question remains outside the theorem-level results currently established here.

Backlog impact:

- Issue #505 is advanced but remains open. The remaining work is model-specific: ordinary short-range scalar critical reconstruction, gauge-theory constructive examples in lattice or BV form, and a deeper state-of-the-art synthesis of rigorous RG results.
- `claude_review.md` was updated after closing audit-meta issue #579; the open-issue count is now 21.

Verification run:

- `python3 tools/audit_theorem_form.py` passed.
- `python3 tools/audit_negative_scope_prose.py` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed after the source-extended RG insertion; `main.pdf` rebuilt cleanly at 2539 pages.
