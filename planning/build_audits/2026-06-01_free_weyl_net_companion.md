# Free Weyl-Net Finite Algebra Companion

Date: 2026-06-01

Scope:
- `monograph/tex/volumes/volume_iv/chapter03_algebraic_qft_local_nets_and_states.tex`
- `calculation-checks/free_weyl_net_checks.py`
- `calculation-checks/README.md`
- `calculation-checks/INDEX.md`
- `planning/chapter_dossiers/volume_iv/chapter03_algebraic_qft_local_nets_and_states.md`

Purpose:
- Support the Volume IV AQFT proof-debt lane by making the finite Weyl
  cocycle algebra behind locality and additivity explicit and reproducible.
- Address the calculation-check coverage gap for the massive scalar Weyl-net
  benchmark without pretending that a finite script proves the continuum
  local-net construction.

Mathematical boundary:
- The script checks exact rational identities in a finite symplectic vector
  space with Weyl relation
  `W(u)W(v)=exp(-i sigma(u,v)/2) W(u+v)`.
- It verifies associativity of the cocycle, the sign in the Weyl
  commutation relation, the group-commutator phase, locality when
  `sigma(u,v)=0`, and the finite partition phase
  `W(sum u_j)=exp(i/2 sum_{j<k} sigma(u_j,u_k)) prod_j W(u_j)`.
- The manuscript continues to carry the continuum analytic content:
  compact-support partition of unity, Green-hyperbolic quotient exactness,
  causal support for locality, and retarded/advanced cutoff for time-slice.

Verification commands:
- `python3 -m py_compile calculation-checks/free_weyl_net_checks.py`
  completed cleanly.
- `python3 calculation-checks/free_weyl_net_checks.py` printed
  `All free Weyl-net finite algebra checks passed.`
- `tools/run_calculation_checks.sh --list` found
  `calculation-checks/free_weyl_net_checks.py` and reported 208 selected
  Python checks plus 2 Wolfram Language checks.
- `git diff --check` completed cleanly.
- `python3 tools/audit_theorem_form.py` reported
  `Theorem-form audit clean.`
- `python3 tools/audit_unnumbered_display_labels.py` reported
  `No labels inside unnumbered display math.`
- `tools/audit_monograph_text.sh` reported
  `Strict monograph text audit clean.`
- `tools/audit_negative_scope_prose.py` reported
  `Negative-scope prose audit clean.`
- `tools/audit_chapter_dossiers.sh` reported
  `Chapter dossier metadata audit clean.`
- `tools/build_monograph.sh` completed cleanly after replacing an initial
  `\over` TeX warning in the new paragraph with `\frac`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported
  `Pages:           2795`.
