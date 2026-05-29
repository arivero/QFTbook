# Thirteenth Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue issue #691's proof-status audit by reading short theorem-family
proofs and assumption/hypothesis-adjacent statements in context, then demoting
claims whose proof content is elementary algebra, a square completion, a finite
analyticity observation, or a direct bookkeeping expansion.

Demoted theorem-family environments:

- `volume_ii/chapter20c_large_n_two_dimensional_qcd_light_front.tex`
  - `Finite-regulator Gauss-law reduction`: converted from proposition/proof
    to a square-completion paragraph; retained the zero-mode caveat.
  - `Positive form of the subtracted kernel`: converted from proposition/proof
    to a quadratic-form identity paragraph; references now point to the
    numbered identity.
- `volume_ix/chapter04_confinement_screening_oblique_confinement.tex`
  - `Pairing on the screened topological quotient`: converted from
    proposition/proof to an orthogonal-quotient bookkeeping paragraph.
- `volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
  - `Finite-regulator analyticity`: converted from proposition/proof to a
    finite-dimensional analyticity paragraph, with the thermodynamic-limit
    input kept separate.
  - `Hard-dense-loop Debye mass at zero temperature`: converted from
    proposition/proof to the HDL susceptibility calculation paragraph.
- `volume_xi/chapter05_wilson_lattice_gauge_theory.tex`
  - `Finite surface expansion and area estimate`: converted from
    proposition/proof to a finite surface-counting paragraph.
  - `Compact-group spin-foam expansion at finite cutoff`: converted from
    proposition/proof to a Peter--Weyl link-integration paragraph.
- `volume_xii/chapter04_unruh_effect_modular_theory.tex`
  - `Imaginary part of a complex boost`: converted from lemma/proof to the
    complex-boost geometry paragraph used in the KMS strip proof.

Assumption/hypothesis checks read in context:

- `volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex` already
  treats the local \(P\)-\(Q\) bridge as an assumption followed by explicit
  algebraic paragraphs rather than a theorem-family wrapper.
- `volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex` keeps the
  large-spin BES scaling regime as an explicit assumption; the nearby
  Zhukovsky Fourier-transform proposition is an independent contour
  calculation, not merely a restatement of the assumption.
- `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
  keeps the leading-log dipole/BFKL setup as a hypothesis; the Mellin
  eigenvalue proposition is a separate beta-integral computation.

Status after edit, before build:

- The removed labels have no remaining references in `monograph`, `planning`,
  or `tools`.
- Theorem-family environments in `monograph/tex/volumes`: 671.
- Proof environments in `monograph/tex/volumes`: 666.

Verification:

- `python3 tools/audit_theorem_form.py` — clean.
- `tools/audit_negative_scope_prose.py` — clean.
- `tools/audit_monograph_text.sh` — clean.
- `python3 tools/audit_unnumbered_display_labels.py` — clean.
- `git diff --check` — clean.
- `tools/build_monograph.sh` — clean.
- `pdfinfo monograph/tex/main.pdf` — 2583 pages.
