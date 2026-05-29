# Issue #597 Monopole Phase Coordinate And Dyonic Tower

Date: 2026-05-29.

Scope:

- Advanced issue #597 in `monograph/tex/volumes/volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`.
- Replaced the previous brief statement that the monopole \(U(1)\) phase
  coordinate produces dyons with a self-contained finite-dimensional
  derivation.

Manuscript content:

- Added subsection `Phase Coordinate, Dyonic Charge, and the Theta Angle`.
- Defined the primitive phase coordinate
  `chi in R / 2 pi Z` and the magnetic charge `n_m` in the matching
  primitive cocharacter normalization.
- Stated the Chern-Weil boundary pairing convention
  `(8 pi^2)^{-1} int tr(F wedge F) = - n_m (2 pi)^{-1} int dot chi dt`
  for a positive phase loop of a positive monopole.
- Derived the phase-sector Lagrangian
  `L_chi = (1/2) I_chi dot chi^2 - theta n_m dot chi/(2 pi)`.
- Proved the Legendre transform and quantization on
  `L^2(S^1, d chi / 2 pi)`.
- Derived the dyonic Hamiltonian
  `H_chi = (2 I_chi)^{-1} (n_e + theta n_m/(2 pi))^2`.
- Identified the shifted electric-field coordinate
  `q_E = n_e + theta n_m/(2 pi)`.
- Proved theta-periodicity by relabelling
  `n_e -> n_e - n_m` under `theta -> theta + 2 pi`.

Companion checks:

- Extended `calculation-checks/soliton_collective_coordinate_checks.py` with
  a symbolic check of the phase-coordinate Legendre transform and the
  theta-periodic charge-lattice relabelling.
- Updated `calculation-checks/README.md`.
- Updated the Volume II Chapter 18 dossier and `claude_review.md`.

Verification:

- `python3 calculation-checks/soliton_collective_coordinate_checks.py`:
  passed.
- `python3 -m py_compile calculation-checks/soliton_collective_coordinate_checks.py`:
  passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `python3 tools/audit_negative_scope_prose.py`: passed.
- `git diff --check`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; `monograph/tex/main.pdf` builds cleanly
  at 2542 pages.

Backlog impact:

- This pass strengthens the monopole/dyonic-sector component of #597.
- Issue #597 remains open because the requested dedicated soliton,
  monopole-moduli, and instanton-measure chapter-level development still
  requires more: full multi-monopole moduli-space geometry, Jackiw-Rebbi and
  DHN soliton quantization, ADHM measure derivation, determinant
  regularization, and instanton compactification/boundary strata.
