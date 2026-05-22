# Lorentzian Boundary-Value Dictionary Pass

Date: 2026-05-22

## Scope

This pass strengthened `monograph/tex/volumes/volume_i/chapter11_lorentzian_green_functions_and_analytic_continuation.tex`, the chapter that later LSZ, perturbative Green-function rules, and analytic continuation arguments depend on.

## Improvements

- Added the local framework for the chapter:
  - Lorentzian spacetime \(M=\mathbb R^{1,D-1}\) with mostly-plus metric.
  - A scalar Wightman field presentation in a vacuum sector.
  - Translation generators \(P^\mu\) with joint spectrum in \(\overline V_+\).
  - Point-field notation as kernel notation for smeared operator-valued distributions.
- Defined the Wightman \(n\)-point distribution \(W_n\in\mathcal S'(M^n)\).
- Defined strict time-ordering regions \(M_\pi^n\) for \(\pi\in S_n\).
- Defined a vacuum time-ordered Green function \(G_n\in\mathcal S'(M^n)\) by its restrictions to the regions \(M_\pi^n\).
- Clarified that local commutativity makes the noncoincident ordered restrictions compatible across spacelike equal-time boundaries, while extension across partial diagonals is local distributional time-ordered-product data.
- Added a boundary-value dictionary:
  - Ordered imaginary shifts \(\epsilon_1>\cdots>\epsilon_n>0\) give the time-ordered Lorentzian boundary value of the holomorphic Wightman continuation.
  - Ordered Euclidean times give Schwinger functions as imaginary-time restrictions of the same holomorphic functions under Wightman tube analyticity.
  - OS-admissible Schwinger hierarchies provide the converse route to Wightman boundary values through OS reconstruction.
- Rephrased the two-point \(i\epsilon\) prescription as the momentum-space encoding of the ordered tube boundary value.
- Updated the Chapter 15 dossier with the new symbols and claim ledger entries.

## Verification

- Ran `tools/build_monograph.sh`; the strict text audit, LaTeX build, and log scan were clean.
- Rendered the affected Chapter 15 pages from `monograph/tex/main.pdf` with `pdftoppm`.
- Visually inspected the pages containing:
  - the Wightman/time-ordered distribution definitions;
  - the tube analyticity section;
  - the new boundary-value dictionary;
  - the Lorentzian Feynman-rule display and tadpole contour material.

## Next Dependency

This pass makes the Green-function analytic-continuation layer more explicit. The next natural development target is the transition from these time-ordered boundary values to Haag--Ruelle scattering and LSZ, checking that every LSZ use refers back to nonperturbative asymptotic states and to the distributional boundary-value hypotheses established here.
