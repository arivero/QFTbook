# CFT Tauberian Saddle Mechanism Pass

Date: 2026-05-31.

Scope:
- `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
- `calculation-checks/cft_voa_modular_checks.py`
- `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`

Purpose:
The Cardy paragraph previously stated the exponential Tauberian theorem and
then gave only a short saddle check.  This was correct as a theorem boundary
but too opaque for the monograph standard: it did not show which part is the
elementary positive-measure estimate and which part is the genuine Tauberian
inverse step.

Substantive changes:
- Added the Stieltjes-measure convention \(\mu_N([0,E])=N(E)\).
- Proved the elementary Laplace upper bound
  \[
    \log N(E)\le \inf_{\beta>0}\{\beta E+\log Z(\beta)\}.
  \]
- Derived the upper-half coefficient \(2\sqrt A\) from
  \(\log Z(\beta)=A/\beta+o(\beta^{-1})\).
- Isolated the nontrivial lower-bound content of the quoted Tauberian theorem:
  positivity and monotonicity prevent cancellations and force enough spectral
  mass near the saddle window \(E\sim A/\beta^2\).
- Made the formal Legendre relation explicit:
  if \(\log N(E)\sim B\sqrt E\), then the Laplace saddle has value
  \(B^2/(4\beta)\), hence \(B^2=4A\).
- Strengthened the calculation check so it verifies both the Laplace-bound
  coefficient and the Legendre-saddle coefficient in exact rational
  arithmetic after suppressing the common \(\pi^2\) factor.

Remaining boundary:
The full lower-bound step remains a quoted analytic Tauberian theorem.  The
chapter now explains why this is the genuine theorem input rather than a
formal saddle substitution.
