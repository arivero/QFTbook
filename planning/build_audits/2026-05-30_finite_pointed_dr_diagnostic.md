# Finite Pointed DR Diagnostic Pass

Date: 2026-05-30

## Scope

- Advanced the Doplicher--Roberts part of #695.
- Added a concrete finite diagnostic for the categorical compact-group output
  rather than leaving the reconstruction discussion entirely abstract.

## Manuscript Changes

- Inserted a finite pointed \(C^*\)-tensor category with simples
  \(X_q\), \(q\in\mathbb Z/N\mathbb Z\), fusion
  \(X_q\otimes X_r\simeq X_{q+r}\), and one-dimensional fiber functor.
- Derived the tensor-automorphism constraint
  \(u_{q+r}=u_q u_r\), hence \(u_q=u_1^q\) and \(u_1^N=1\).
- Identified the reconstructed compact group as
  \(\mu_N=\{\zeta\in U(1):\zeta^N=1\}\).
- Added the finite charged grading
  \(\mathcal F_{\rm alg}=\bigoplus_q\mathcal F_q\) and showed that group
  averaging projects to \(\mathcal F_0\).

## Calculation Check

- Added `calculation-checks/dhr_dr_reconstruction_checks.py`, which verifies
  by exact modular arithmetic that tensor automorphisms obey the character
  law and that the fixed-degree projection keeps exactly the neutral degree
  for \(2\le N\le 12\).

## Verification

- `python3 calculation-checks/dhr_dr_reconstruction_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
