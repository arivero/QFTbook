Issue: #597
Date: 2026-06-07
Area: Volume VII, Chapter 9 GLSM/Hori--Vafa vortex amplitude

Scope
- Re-audited the one-vortex Hori--Vafa frame repair after review found that the
  numerical FI-theta sector weight had been folded into `c_i` and then counted
  again in `exp(t) prod_i c_i`.
- Split the original charge-one amplitude into the explicit original-theory
  sector weight `q_vort` times the reduced determinant/operator normalization
  `chat_orig`; the mirror coefficient `c_i` is now `Z_map chat_orig`.
- Replaced the source-independent interaction scalar in the source functional
  by the effective insertion `<exp(-V_int) P_bare>`, with scalar
  factorization allowed only as an additional theorem.
- Updated the noncancellation bound so the original reduced target is `C_R`,
  while the dual target is `Z_map C_R` with a separate map residual.

Quality audit
- This is a physics-depth repair, not a notation wrapper: it changes which
  object is a path-integral amplitude and which object is a mirror-coordinate
  normalization.
- The repair removes two overclaims: FI-theta double counting and universal
  vacuum-factor source factorization.
- The companion now includes negative controls for FI double counting,
  scalar-vacuum source factorization, omitted `Z_map`, and frame-crossed
  noncancellation targets.
- Directives and issue-tracking language remain in planning files only.

Verification plan
- Run the focused GLSM companion and wrapper.
- Run Chapter 9 theorem/display/prose/style audits.
- Run dossier/text, inventory/evidence, full Python, and full monograph build
  checks before posting the issue update.
