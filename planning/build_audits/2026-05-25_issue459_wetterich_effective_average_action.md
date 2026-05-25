# Build Audit: Issue #459 Wetterich Effective Average Action

## Issue

- GitHub issue: #459, oldest open issue at the start of the pass.
- Requested substance: add the effective-average-action form of functional RG,
  parallel to the existing Wilson-Polchinski section.

## Manuscript Edits

- Added `Effective Average Action and the Wetterich Equation` to
  `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`.
- Defined the source convention \(\mathcal J=-J\), the IR regulator
  \(R_{\kappa,N}\), the regulator term \(\Delta S_{\kappa,N}\), the connected
  functional \(W_{\kappa,N}\), the average field \(\varphi\), and the modified
  Legendre transform \(\Gamma_{\kappa,N}\).
- Proved the finite-regulator Hessian identity
  \[
    \Gamma_{\kappa,N}^{(2)}+R_{\kappa,N}
      =(W_{\kappa,N}^{(2)})^{-1}.
  \]
- Proved the finite-regulator Wetterich equation by differentiating the
  modified Legendre transform at fixed \(\varphi\), decomposing the full second
  moment into mean and connected parts, and substituting the Hessian identity.
- Added the continuum-status paragraph separating the formal trace equation
  from the regulator-removal and trace-convergence estimates needed for a
  theorem-level statement.
- Added the constant-field/local-potential projection and the optimized
  regulator formula with the smooth-regulator caveat.
- Added a figure contrasting Wilsonian shell integration with the
  effective-average-action construction.
- Added remarks separating Wilson-Polchinski and Wetterich coordinate systems
  and recording the additional BV/BRST or background-field data needed in
  gauge theories.

## Dossier Edits

- Updated
  `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md`
  to include the new construction, claim ledger entries, figure requirement,
  and audit note.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; generated
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 831 pages.
- Rendered and inspected physical PDF pages 451--452.  Page 451 contains the
  Wilsonian-versus-effective-average-action figure; page 452 contains the
  local-potential projection, relation-to-Polchinski remark, and gauge-theory
  status remark.  The figure labels, arrows, and caption render legibly.
