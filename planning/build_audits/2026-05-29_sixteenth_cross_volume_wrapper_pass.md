# Sixteenth Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue issue #691 by demoting theorem-family statements whose
proof blocks were convention algebra, residue bookkeeping, direct
Ward-identity substitution, Gaussian determinant normalization, or
finite-dimensional mode/representation calculations.

Demoted theorem-family environments:

- `volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex`
  - `One-loop determinant from a quadratic fluctuation`: converted from
    proposition/proof to the Gaussian determinant paragraph.
- `volume_i/chapter13_lsz_reduction_and_the_s_matrix.tex`
  - `Large-time pole selector`: converted from proposition/proof to the
    contour-residue paragraph.
- `volume_i/chapter16a_spinor_conventions.tex`
  - `Basic Clifford, adjoint, and current identities`: converted from
    proposition/proof to the convention-check paragraph.
- `volume_i/chapter18_maxwell_theory_constraints_and_gauge_fixing.tex`
  - `Axial gauge leaves two canonical degrees of freedom`: converted from
    proposition/proof to the gauge-slice algebra paragraph.
- `volume_ii/chapter03_bound_states_from_exchange_amplitudes.tex`
  - `Spin from the angular residue`: converted from proposition/proof to the
    spherical-harmonic addition-theorem paragraph.
- `volume_iii/chapter03_stress_tensor_weyl_structure_and_improvement.tex`
  - `Flat-space trace condition from Weyl invariance`: converted from
    theorem/proof to the metric-source Ward paragraph, since the key
    assumption is the Weyl-invariant renormalized functional.
- `volume_iii/chapter06_primary_operators_and_finite_transformations.tex`
  - `Elementary generator actions`: converted from corollary/proof to the
    explicit generator-action paragraph.
- `volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`
  - `Scalar two-point selection rule`: converted from theorem/proof to the
    separated-point Ward-identity paragraph.
- `volume_v/chapter15_two_dimensional_superconformal_algebras.tex`
  - `Mode algebra for N=2`: converted from proposition/proof to the OPE-mode
    residue calculation paragraph; spectral flow now cites the displayed mode
    equations rather than a proposition wrapper.

Retained after reading:

- The Witten-index positive-energy pairing, transfer-matrix commutativity,
  Dijkgraaf--Witten triangulation independence, McKean--Singer identity,
  cocharacter criterion for an 't Hooft singularity, and two-dimensional axial
  contact term remain theorem-family statements or propositions because each
  supplies a structural pairing, commuting-family theorem, topological
  invariance mechanism, index bridge, singular-defect criterion, or anomaly
  computation used downstream.

Status after edit, before build:

- Removed labels have no remaining references in `monograph`, `planning`, or
  `tools`.
- Theorem-family environments in `monograph/tex/volumes`: 645.
- Proof environments in `monograph/tex/volumes`: 640.

Verification before full build:

- `python3 tools/audit_theorem_form.py` — clean.
- `tools/audit_negative_scope_prose.py` — clean.
- `tools/audit_monograph_text.sh` — clean.
- `python3 tools/audit_unnumbered_display_labels.py` — clean.
- `git diff --check` — clean.
- `tools/build_monograph.sh` — clean.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` — `Pages: 2583`.
