# Issue 479: Generalized-Free Scalar Four-Point Example

GitHub issue #479 flagged that the OPE/crossing chapter stated the
identical-scalar crossing equation without displaying the canonical
generalized-free or free-scalar four-point example.

## Manuscript Additions

- Added `sec:gff-four-point-crossing` to
  `volume_iii/chapter09_operator_product_expansion.tex`.
- Defined the separated-point generalized-free scalar datum by Wick pairings
  and identified the radial Hilbert-space sector as the symmetric Fock space
  over the scalar lowest-weight module after null-vector quotienting.
- Derived
  \[
    \mathcal G_{\rm GFF}(u,v)
    =
    1+u^{\Delta_\phi}+(u/v)^{\Delta_\phi}.
  \]
- Displayed the direct prefactor crossing check
  \[
    v^{\Delta_\phi}\mathcal G_{\rm GFF}(u,v)
    =
    u^{\Delta_\phi}\mathcal G_{\rm GFF}(v,u).
  \]
- Constructed the bilinear primary tower from the finite two-particle radial
  Hilbert-space projection with
  \(\Delta_{n,\ell}=2\Delta_\phi+2n+\ell\), even spin, and positive OPE
  coefficients.
- Computed the leading scalar coefficient
  \(a^{\rm GFF}_{0,0}=2\) for
  \(\mathcal O_{0,0}=:\phi^2:/\sqrt2\).
- Displayed both the \(12\to34\) and \(14\to23\) block expansions with their
  channel domains.

## Calculation Check

Added `calculation-checks/free_scalar_four_point_checks.py`, which verifies:

- the monomial equality in the crossing identity;
- the three Wick pairings in the four-point function;
- the Wick counts giving \(a^{\rm GFF}_{0,0}=2\);
- the even-spin bilinear dimensions and twists in the free four-dimensional
  scalar specialization.
