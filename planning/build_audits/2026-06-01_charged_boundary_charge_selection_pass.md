# Charged Boundary-Charge Selection Pass

Date: 2026-06-01

Issue: #527

## Scope

This pass tightens the Wilson-line LSZ discussion in
`monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`.
The chapter already contained the endpoint transformation law for abelian and
nonabelian Wilson-line dressed charged operators.  The missing logical link was
the boundary-charge Ward selection rule for the dressed correlators that enter
any LSZ reduction.

## Manuscript Change

Added a structural paragraph after Wilson-line covariance:

- defines the signed charge `epsilon_a q_a` of a dressed insertion and its
  adjoint;
- derives the boundary-gauge transformation of the regulated time-ordered
  vacuum distribution;
- states that a nonzero vacuum dressed correlator requires
  `sum_a epsilon_a q_a = 0`;
- states the corresponding matrix-element rule between charged sectors;
- states the nonabelian version as the requirement that endpoint
  representations contribute through invariant tensors in
  `(R_1 tensor ... tensor R_n)^{G_infty}`;
- separates this exact boundary-charge bookkeeping from the dynamical question
  whether the charged sector has finite-energy asymptotic particles.

The passage was deliberately not promoted to a proposition/proof block.  It is
a necessary Ward-identity synthesis at the point of use, not a new theorem
family; the remaining theorem debt remains the large-time charged
Haag--Ruelle/LSZ construction.

## Calculation Check

Extended `calculation-checks/charged_flux_dressing_checks.py` with exact
finite checks for:

- abelian signed-charge neutrality in dressed vacuum correlators;
- non-neutral dressed charge sums;
- elementary `SU(2)` endpoint singlet-channel bookkeeping using twice-spin
  tensor-product arithmetic.

## Verification

Targeted checks to run for this pass:

```bash
python3 calculation-checks/charged_flux_dressing_checks.py
python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py
tools/run_calculation_checks.sh --python-only --only charged_flux
git diff --check
python3 tools/audit_theorem_form.py
python3 tools/audit_unnumbered_display_labels.py
tools/audit_monograph_text.sh
tools/audit_negative_scope_prose.py
tools/audit_chapter_dossiers.sh
tools/build_monograph.sh
```
