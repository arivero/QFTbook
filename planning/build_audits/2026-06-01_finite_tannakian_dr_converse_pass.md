# Finite Tannakian DR Converse Pass

Date: 2026-06-01.

Issue context: GitHub #695.

Scope:
- Strengthened the Doplicher--Roberts theorem-boundary discussion in
  `monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`.
- Added `Finite Tannakian converse through the regular algebra` after the
  finite \(S_3\) charged-coordinate core.
- Proved the finite Peter--Weyl converse: for a finite group \(G\), every
  left-equivariant unital \(*\)-automorphism of
  \(\operatorname{Fun}(G)\) permutes point idempotents by
  \(\delta_x\mapsto\delta_{xh}\) for a unique \(h\in G\).
- Derived the induced action on matrix coefficients
  \(f^W_{\alpha i}(g)=D_W(g)_{\alpha i}\), giving the tensor natural
  automorphism \(u_W=D_W(h^{-1})\).
- Identified the compact-group Doplicher--Roberts theorem as the analytic
  completion of this Peter--Weyl mechanism plus the local-QFT construction of
  the DHR category and field algebra.

Calculation check:
- Extended `calculation-checks/dhr_dr_reconstruction_checks.py` with an exact
  \(S_3\) enumeration of all left-equivariant automorphisms of
  \(\operatorname{Fun}(S_3)\), verifying that precisely the six right
  translations occur, and checked the corresponding matrix-coefficient action
  \(T_h f(g)=f(g h^{-1})\).

Verification commands for this pass:
- `python3 calculation-checks/dhr_dr_reconstruction_checks.py`
- `python3 -m py_compile calculation-checks/dhr_dr_reconstruction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only dhr_dr_reconstruction`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

Status:
- This closes a concrete finite Tannakian-converse gap inside the DR
  reconstruction discussion.
- It does not close #695.  The remaining issue still includes compact
  analytic completion, local-QFT field-algebra reconstruction, and substantial
  model-level AQFT examples.
