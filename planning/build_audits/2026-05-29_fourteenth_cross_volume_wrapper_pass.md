# Fourteenth Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue the issue #691 proof-status audit by demoting formula
packages and local algebraic identities whose proof content is a direct
variation, pole-equation substitution, implicit-function application, or
matrix/projector normalization calculation.

Demoted theorem-family environments:

- `volume_i/chapter07_symmetries_noether_theorem_and_stress_tensors.tex`
  - `Localized-parameter form of Noether's theorem`: converted from
    proposition/proof to the local parameter-variation paragraph.
- `volume_iii/chapter06_primary_operators_and_finite_transformations.tex`
  - `Spinful local conformal-current Ward identity`: converted from
    proposition/proof to a Ward-identity paragraph with the contact-sign
    derivation kept inline.
- `volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`
  - `Leading N=1 scaling data`: converted from proposition/proof to a scaling
    data paragraph.
  - `Two-loop N=1 Wilson--Fisher epsilon data`: converted from
    proposition/proof to a two-loop pole-equation calculation paragraph.
  - `O(N) Wilson--Fisher data through two loops`: converted from
    proposition/proof to the corresponding tensor-combinatoric data paragraph.
- `volume_vii/chapter05_nonrenormalization_holomorphy.tex`
  - `Tree-level elimination of a massive chiral block`: converted from
    proposition/proof to a holomorphic implicit-function paragraph.
- `volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`
  - `Chiral F-term data and quadratic masses`: converted from
    proposition/proof to the quadratic-expansion paragraph.
- `volume_vi/chapter09_on_gross_neveu_sigma_model_families.tex`
  - `Projector form of the kinetic term and charge`: converted from
    proposition/proof to a projector-identity paragraph.
  - `CP^1 as the O(3) sigma model`: converted from proposition/proof to a
    Pauli-matrix normalization paragraph.

Status after edit, before build:

- Removed labels have no remaining references in `monograph`, `planning`, or
  `tools`.
- Theorem-family environments in `monograph/tex/volumes`: 662.
- Proof environments in `monograph/tex/volumes`: 657.

Verification:

- `python3 tools/audit_theorem_form.py` — clean.
- `tools/audit_negative_scope_prose.py` — clean.
- `tools/audit_monograph_text.sh` — clean.
- `python3 tools/audit_unnumbered_display_labels.py` — clean.
- `git diff --check` — clean.
- `tools/build_monograph.sh` — clean after shortening the chiral-elimination
  paragraph heading that produced an overfull hbox in the first build attempt.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` — `Pages: 2583`.
