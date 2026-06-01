# Charged Coulomb-Tail Wrapper Demoted

Related issue: GitHub #691, in the charged-sector Haag--Ruelle/LSZ lane
tracked by #527 and #528.

The finite-dimensional comparison calculation
\[
  V(t)=\kappa/\sqrt{a^2+|b+ut|^2}
\]
is useful because it fixes the \((\kappa/|u|)\log t\) normalization of a
Dollard comparison phase.  It is not, however, a theorem about QFT.  Its proof
is completed-square algebra plus the elementary asymptotic expansion of
\(\operatorname{arsinh}\).

This pass demotes the former proposition/proof wrapper in Volume IV Chapter 5
to a paragraph-level worked calculation.  The exact primitive, logarithmic
asymptotic, calculation-check companion, and charged-scattering interpretation
are retained.  The theorem-family burden remains on the genuinely open QFT
problem: deriving the long-range coefficient and the \(L^1\) remainder from
Wilson-line or Coulomb-dressed charged creators.

The old title is added to `tools/audit_theorem_form.py` so this elementary
comparison calculation cannot return as a theorem, proposition, lemma, or
corollary.
