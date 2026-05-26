# 2026-05-26 Volume XII Locally Covariant KG Deepening

## Scope

- Rewrote Volume XII, Chapter 1 from a short overview into a foundational
  construction of locally covariant QFT on globally hyperbolic backgrounds.
- Added the free Klein--Gordon CCR functor as the chapter's main example,
  including the quotient by the equation of motion, the causal-propagator
  symplectic form, functoriality under causally convex embeddings, and the
  time-slice property for Cauchy morphisms.
- Added a finite exact calculation check for the quotient/symplectic algebra
  used by the free scalar construction.

## Mathematical Content Added

- Definitions of globally hyperbolic spacetime, causally convex subset,
  background category `Loc`, Cauchy morphism, locally covariant QFT, kinematic
  local algebra, locally covariant field, and locally covariant state space.
- Proof that a locally covariant theory induces an isotone Einstein-causal
  kinematic net on each fixed background.
- Construction of the Klein--Gordon operator
  \(P_M=-\nabla^\mu\nabla_\mu+m^2+\xi R\), retarded/advanced Green
  operators, causal propagator, equation-of-motion quotient, nondegenerate
  symplectic form, and CCR algebra.
- Proof of \(\ker E_M=P_MC_c^\infty(M)\), using retarded/advanced support
  and global hyperbolicity.
- Proof of causal-embedding functoriality from compatibility of Green
  operators with causally convex isometric embeddings.
- Proof of the time-slice axiom by cutting off a solution between Cauchy
  surfaces inside the Cauchy image.
- Definitions of quasifree states, Hadamard local form, Synge world function,
  \(i\epsilon\) boundary prescription, \(U=\Delta^{1/2}\), and the smooth
  state-dependent Hadamard remainder.
- Proof that two Hadamard two-point functions for the same Klein--Gordon
  operator differ by a smooth function.
- Connection to Wick square subtraction and finite local curvature freedom
  of the stress tensor.

## Verification

- `python3 calculation-checks/locally_covariant_kg_checks.py`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1372`.
- `rg -n "undefined|Warning|Error" monograph/tex/main.log` returned no
  matches after the cross-reference label was corrected.
