# Split Product-State Independence Pass

Date: 2026-05-31

GitHub issue: #695, foundational reconstruction/AQFT proof debt.

## Scope

Volume IV, Chapter 4 introduces the split property before the quoted
nuclearity-to-split theorem.  The surrounding text stated that the type-I
interpolant gives an approximate tensor-product separation, but the operational
normal-state consequence needed to be visible at the point of definition.

## Change

Added the explicit construction: if
\(\mathcal M_1=\mathcal R(\mathcal O_1)\),
\(\mathcal M_2=\mathcal R(\mathcal O_2)\), and
\(\mathcal M_1\subset\mathcal N\subset\mathcal M_2\) is split, choose
\[
  U\mathcal N U^*=\mathcal B(\mathcal K)\otimes 1,
  \qquad
  U\mathcal N'U^*=1\otimes\mathcal B(\mathcal L).
\]
Then \(\mathcal M_1\) and \(\mathcal M_2'\) act on the two tensor factors, so
normal states on the two commuting algebras extend to a normal product state
\[
  \Phi(AB')=\varphi_1(A)\varphi_2(B').
\]

This is a construction, not a theorem wrapper.  It explains the continuum
meaning of split independence at positive separation while keeping the
nuclearity-to-split implication as the deeper quoted operator-algebra input.
