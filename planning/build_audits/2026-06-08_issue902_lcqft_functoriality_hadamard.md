# 2026-06-08 Issue #902 LCQFT Functoriality And Hadamard Audit

## Scope

Addressed #902 in Volume XII Chapter 1:

- causal-propagator functoriality under causally convex embeddings;
- injectivity of the free Klein--Gordon CCR functor;
- global smoothness of differences of Hadamard two-point functions.

This pass repairs the foundation used by point splitting, pAQFT, Hawking and
Unruh states, cosmological particle creation, and semiclassical
backreaction.  The mathematics appears only where it protects the physical
claim: which observables are functorial under spacetime restriction, and when
Hadamard subtraction is globally state independent.

## Substance

- Replaced the false global identity \(E_N\chi_*f=\chi_*E_Mf\) by
  \[
    \chi^*E_N^{\rm ret/adv}\chi_*f=E_M^{\rm ret/adv}f,\qquad
    \chi^*E_N\chi_*f=E_Mf .
  \]
- Stated explicitly that \(E_N^{\rm ret/adv}\chi_*f\) may propagate outside
  the open image \(\chi(M)\), and that zero-extending \(E_M^{\rm ret/adv}f\)
  is generally not smooth at the boundary.
- Reworked symplectic preservation and quotient injectivity using the
  restriction identity.
- Upgraded the Hadamard smooth-difference statement to a proposition with a
  proof boundary: local parametrix cancellation gives smoothness near the
  diagonal, while global smoothness uses the local-to-global Hadamard theorem
  and propagation of singularities for bisolutions.
- Added finite negative controls in `locally_covariant_kg_checks.py` for the
  false zero-extension identity, retarded propagation outside a Minkowski
  diamond, and the failure of diagonal \(U\times U\) charts to cover
  far-separated pairs.

## Re-Audit

- Physics depth: the repair changes the validity of the free-field functor
  and the state-independent subtraction used by composite observables.  It is
  not an adjacent lemma cell.
- Coherence: the same restriction convention is now present in the TeX proof,
  finite checks, calculation README, evidence contract, and dossier.
- Scope restraint: no directive/planning prose was added to monograph TeX.
- Boundary: the analytic Green-operator and propagation-of-singularities
  theorems are invoked as theorem boundaries; the finite companion verifies
  the exact logical shape but does not claim to prove those analytic results.

## Verification

- `python3 calculation-checks/locally_covariant_kg_checks.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii/chapter01_locally_covariant_qft_and_hadamard_states.tex --fail`
- `bash tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xii/chapter01_locally_covariant_qft_and_hadamard_states.tex`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

The full build initially caught an overfull symplectic-pairing display in the
new functoriality proof; the final version breaks that calculation across
aligned lines, and the subsequent build/log scan is clean.
