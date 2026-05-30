# BV Localization Stratum-Collar Pass

Date: 2026-05-30

## Scope

- Advanced the localization compactness and singular-stratum slice of #698 and
  #629 in Volume VIII, Chapter 10.
- Focused on replacing abstract compactification language with an explicit
  finite-dimensional boundary object.

## Manuscript Changes

- Added a collar/link formula for the stratum boundary functional
  \(\mathcal B_{S_\alpha}(\rho)\).
- Defined the boundary faces \(L_{\alpha,\epsilon}=\{r=\epsilon\}\), the
  inherited boundary orientation, and the ordinary BV Stokes boundary density
  \(V_\rho^{\rm bdry}\).
- Added the asymptotic criterion
  \[
    \int_{L_{\alpha,\epsilon}} V_\rho^{\rm bdry}
    =
    \epsilon^{\eta_\alpha}B_{\alpha,0}
    +
    O(\epsilon^{\eta_\alpha+\delta})
  \]
  distinguishing vanishing boundary terms, finite residues, and divergent
  boundary data.
- Reframed the Uhlenbeck/Gieseker/Nekrasov paragraph so the Gieseker/Nekrasov
  resolution contributes a candidate \(C_\alpha\) whose compatibility with the
  original field-theoretic regulator remains a theorem/hypothesis, not a
  formal consequence of \(Q\)-exactness.

## Calculation Check

- Extended `calculation-checks/bv_localization_checks.py` with exact rational
  checks of the collar-scaling trichotomy: positive exponent, zero exponent,
  and negative exponent.

## Verification

- `python3 calculation-checks/bv_localization_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
