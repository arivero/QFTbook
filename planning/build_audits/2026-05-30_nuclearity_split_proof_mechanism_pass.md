# 2026-05-30 Nuclearity/Split Proof-Mechanism Pass

## Scope

This pass addresses the nuclearity/split portion of the foundational AQFT
quoted-theorem proof debt in Volume IV, Chapter 4.  The theorem remains a
quoted theorem.  The manuscript now explains the operator-algebraic bridge
between the energy-damped nuclear map and the split inclusion, instead of
leaving the theorem as a compressed structural statement.

## Manuscript Change

- Added the split criterion for an inclusion
  `M_1 subset M_2`: the multiplication representation of
  `M_1 odot M_2'` extends normally to `M_1 \bar\otimes M_2'`.
- Displayed the corresponding spatial tensor-product representation and the
  type-I interpolating factor.
- Explained how a nuclear decomposition of
  `Theta_{\beta,O}(A)=e^{-\beta H}A Omega` controls the local energy-damped
  unit ball by a summable family.
- Explained why the collar `O_1 \Subset O_2` is the geometric input that
  permits analytic imaginary-time translation without crossing the spacelike
  complement.
- Separated one-scale nuclearity from the uniform small-`\beta` phase-space
  bound used in continuum applications.
- Clarified that type `III_1` sharp-local-algebra status requires additional
  relativistic regularity/scaling hypotheses and is not a formal consequence
  of split inclusions alone.

## Issue Alignment

- #695: improves the nuclearity/split part of the foundational quoted-theorem
  proof-debt cluster.
- #691: keeps a genuinely substantive quoted theorem while exposing where the
  proof substance lies.

## Remaining Proof Debt

This pass does not close #695.  Remaining pieces include OS boundary-value
infrastructure, Borchers--Wiesbrock half-sided modular inclusions, and
substantial interacting examples of AQFT objects.
