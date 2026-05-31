# Fermat LG Wilsonian Spurion Pass

Date: 2026-05-31

## Trigger

The stringbook Appendix K discussion of two-dimensional
Landau-Ginzburg models includes a concise nonrenormalization footnote for
`W=X^k`.  The QFT monograph needs the same idea in a self-contained form:
as a statement about a declared Wilsonian chiral coordinate, with all
spurion assumptions and proof boundaries visible.

## Edits

- Added a `Wilsonian superpotential coordinate for Fermat LG models`
  paragraph to Volume VII, Chapter 09.
- Stated the exact assumptions used by the selection argument:
  chiral Wilsonian regularity, nonnegative powers of background chiral
  couplings `g_i`, flavor spurion symmetries, and `R(W)=1`.
- Derived explicitly that a candidate monomial
  `prod_i g_i^{m_i} (Phi^i)^{a_i}` obeys
  `a_i=d_i m_i` and `sum_i a_i/d_i=1`, hence `sum_i m_i=1`; therefore the
  only regular holomorphic Wilsonian superpotential monomials are the
  original `g_i (Phi^i)^{d_i}` terms.
- Kept the statement at Wilsonian-coordinate level, separating it from the
  existence of the infrared fixed point and from uncontrolled
  nonperturbative sectors.
- Updated the chapter dossier and stringbook crosswalk.
- Added exact finite coverage in `calculation-checks/susy_2d_lg_glsm_checks.py`.

## Verification Plan

- Run the dedicated Python calculation check for the 2D SUSY LG/GLSM chapter.
- Run the text/proof-form audits and the monograph build before committing.

