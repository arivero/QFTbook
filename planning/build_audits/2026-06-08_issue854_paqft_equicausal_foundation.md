# Issue #854 pAQFT functional-space foundation repair

Date: 2026-06-08.

Scope:

- Targeted Volume XII Chapter 10, the Volume XII claim-control spine, and the
  downstream semiclassical backreaction inheritance point.
- Replaced the implicit use of unrestricted microcausal functionals as the
  pAQFT algebra domain with an explicit local/equicausal closure contract.

Primary source checked:

- Hawkins--Rejzner--Visser, `arXiv:2312.15203v2`, which proves that the
  traditional microcausal class is not closed under the Peierls bracket, that
  the microcausal complex is not closed under the time-slice homotopy, and
  that equicausal functionals contain local functionals and Wick polynomials
  while closing under Peierls/star products and satisfying the time-slice
  axiom.

Before:

- The chapter defined `F_muc(M)` and immediately used it as the star-product
  domain.
- The text correctly explained why individual Hadamard contractions are
  wavefront-set admissible, but did not separate that pointwise pairing fact
  from smoothness and closure of the resulting functional.
- The claim-control matrix and backreaction chapter could therefore be read as
  inheriting a stronger unrestricted-microcausal theorem than the current
  literature supplies.

After:

- Chapter 10 now distinguishes:
  - microcausal functionals as the pointwise wavefront-set pairing test;
  - equicausal functionals as the local normal-topology/equicontinuity class
    on which Peierls bracket, Hadamard star product, and time-slice closure
    are asserted;
  - local/multilocal/Wick-polynomial subalgebras as the concrete domains used
    by the chapter's physical examples and Epstein--Glaser time-ordering maps.
- The star product now has domain `F_ec(M)[[hbar]]`.
- Time-ordered products now map local inputs into the equicausal lane, and the
  text marks arbitrary time ordering on general equicausal inputs as an open
  extension question.
- The Volume XII claim-control row and Ch11 backreaction opening now state
  that pAQFT source/stress claims require the local/equicausal closure package,
  not bare microcausal admissibility.

Negative controls added:

- A finite margin-budget check rejects the shortcut from positive pointwise
  microcausal margins to a closed star/Peierls algebra.
- The same check accepts a uniform equicausal margin and the local/Wick
  polynomial finite subalgebra.

Boundary:

- This is a foundation correction for the perturbative algebraic lane.  It is
  not a new nonperturbative interacting curved-spacetime QFT, not a proof of
  the full Hawkins--Rejzner--Visser theorem inside the monograph, and not an
  extension of Epstein--Glaser time-ordering to arbitrary equicausal
  functionals.

Verification:

- `python3 calculation-checks/paqft_algebra_checks.py`
- `python3 tools/audit_negative_scope_prose.py --root ch01 --root ch10 --root ch11 --fail`
- `python3 tools/audit_theorem_form.py --root ch01 --root ch10 --root ch11`
- `tools/audit_monograph_text.sh ch01 ch10 ch11`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_xii`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii --fail --limit 40`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

Build-log repair:

- The first full build after the text insertion produced a single overfull
  `\vbox` in the Volume XII claim-control matrix.  The repair tightened the
  pAQFT row wording and that matrix's row spacing; the final full build and
  log scan are clean.
