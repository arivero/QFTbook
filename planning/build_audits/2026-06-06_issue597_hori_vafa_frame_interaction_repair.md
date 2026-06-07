Issue: #597
Date: 2026-06-06
Area: Volume VII, Chapter 9 GLSM/Hori--Vafa vortex amplitude

Scope
- Repaired the one-vortex Hori--Vafa lane so the original GLSM finite source
  functional carries a numerical FI-theta vortex weight, while `exp(-Y_i)` is
  used only after the abelian dual operator map.
- Added the interacting normal-mode expectation/cumulant factor to the
  single-vortex coefficient, source-functional extraction, component cell, and
  noncancellation integrand.
- Extended `susy_2d_lg_glsm_checks.py` with a finite frame/normal-interaction
  check and new determinant-only/source-frame negative controls.

Quality audit
- This is a physics-depth repair, not a wrapper.  It changes the typed
  amplitude statement: a dual mirror operator is no longer treated as the
  scalar sector weight of the original path integral.
- The Gaussian determinant is no longer advertised as the full regulated
  coefficient unless the normal-mode interaction factor is proved trivial or
  bounded.
- The repair follows the instanton standard requested for the monograph:
  measure, determinant, zero modes, source insertions, normal fluctuations, and
  operator matching are separate inputs.
- Directives and issue-tracking language remain in planning files only.

Verification plan
- Run the focused GLSM companion and wrapper.
- Run Chapter 9 theorem/display/prose/style audits.
- Run dossier/text, inventory/evidence, full Python, and full monograph build
  checks before posting the issue update.
