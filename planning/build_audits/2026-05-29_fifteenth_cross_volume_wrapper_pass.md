# Fifteenth Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue issue #691 by reading short theorem-family statements and
demoting proof blocks whose content is finite algebra, direct quotient
functoriality, first-order Green-kernel inversion, Neumann-series expansion,
or one-line symmetry selection.

Demoted theorem-family environments:

- `volume_i/chapter14_cross_sections_partial_waves_and_unitarity.tex`
  - `Invariant two-particle flux`: converted from proposition/proof to a
    worked normalization paragraph.
- `volume_i/chapter18_maxwell_theory_constraints_and_gauge_fixing.tex`
  - `Gupta--Bleuler quotient as the two-helicity photon Fock space`: converted
    from proposition/proof to the functorial Fock-quotient paragraph.
- `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
  - `Center selection for reduced open words`: converted from lemma/proof to
    the reduced-model center-selection paragraph.
  - `Static propagator as a Wilson line`: converted from proposition/proof to
    the first-order HQET Green-kernel calculation.
- `volume_xi/chapter03_lattice_reflection_positivity.tex`
  - `Wilson plaquette action`: converted from corollary/proof to the
    character-expansion paragraph following the Osterwalder--Seiler criterion.
- `volume_xi/chapter06_monte_carlo_and_sign_problems.tex`
  - `Leapfrog reversibility and volume preservation`: converted from
    proposition/proof to the finite-dimensional HMC algebra paragraph.
- `volume_xi/chapter08_lattice_to_continuum_local_qft.tex`
  - `Dense-test convergence plus uniform seminorm control`: converted from
    proposition/proof to the countability/extension paragraph, explicitly
    identifying the uniform seminorm bound as the hard input.
  - `Finite-graph random-walk resolvent`: converted from proposition/proof to
    the positive-operator/Neumann-series calculation paragraph.

Retained after reading:

- `Finite Grassmann reflection-positivity criterion`, `Largest-time identity
  for a scalar graph`, `Fredholm expansion and canonical coefficients`,
  `Unitary implementation of an invariant state`, Chern--Weil transgression,
  the causal-propagator kernel lemma, and the light-ray gauge-covariance
  proposition remain theorem-family statements or lemmas because each supplies
  a structural positivity, graph-combinatoric, functional-analytic, GNS,
  descent, support, or gauge-covariance mechanism used downstream.

Status after edit, before build:

- Removed labels have no remaining references in `monograph`, `planning`, or
  `tools`.
- Theorem-family environments in `monograph/tex/volumes`: 654.
- Proof environments in `monograph/tex/volumes`: 649.

Verification before full build:

- `python3 tools/audit_theorem_form.py` — clean.
- `tools/audit_negative_scope_prose.py` — clean.
- `tools/audit_monograph_text.sh` — clean.
- `python3 tools/audit_unnumbered_display_labels.py` — clean.
- `git diff --check` — clean.
- `tools/build_monograph.sh` — clean.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` — `Pages: 2583`.
