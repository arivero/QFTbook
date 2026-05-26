# Issue #582 Gaussian Coordinate Estimates Checkpoint

## Manuscript Change

- Added Proposition `prop:spde-gaussian-wick-coordinate-scale-estimates` to
  Volume XI, Chapter 9.
- The proposition proves the scale estimates for the primitive Gaussian
  strict negative-sector coordinates:
  \[
    \Xi,\quad X,\quad X^2,\quad X^3 .
  \]
- For white noise, the proof derives
  \[
    \|\delta^{5/2+\kappa}\xi(\psi_z^\delta)\|_{L^{2m}}
    \lesssim \delta^\kappa .
  \]
- For the stochastic convolution, the proof assumes the covariance
  singularity
  \[
    |C(u,v)|\lesssim \|u-v\|_{\mathfrak s}^{-1}
  \]
  and derives, using Wick covariance and parabolic scaling,
  \[
    \|\delta^{k/2+k\kappa}\langle :X^k:,\psi_z^\delta\rangle\|_{L^{2m}}
    \lesssim \delta^{k\kappa},
    \qquad k=1,2,3 .
  \]
- Same-scale edge estimates are proved with a Holder factor
  \(\eta^\theta\).
- Added Proposition
  `prop:spde-gaussian-wick-dual-norm-coordinate-estimates`.
- This proposition upgrades the primitive Gaussian estimates to the
  \(E_r'\)-dual norm by introducing a parabolic wavelet \(H^{-s}\) majorant,
  with \(Q/2+\theta<s<r\).  The proof shows that white-noise coefficients
  sum as \(\sum_j2^{(Q-2s)j}\), while Wick-power coefficients sum as
  \(\sum_j2^{(k-2s)j}\), and that same-scale edge estimates gain
  \(\eta^\theta\) after splitting the wavelet scale at \(2^{-j}\simeq\eta\).
- Added Proposition
  `prop:spde-heat-integration-reexpansion-coefficient-estimate`.
- This proposition proves the deterministic Schauder/reexpansion transfer:
  if a negative distribution of assigned homogeneity \(\alpha\) has true
  regularity \(\alpha+\sigma\), then heat integration produces an increment
  of regularity \(\beta+\sigma\), where \(\beta=\alpha+2\), and the
  coefficient normalized by \(\|z-z'\|_{\mathfrak s}^{\beta}\) carries scale
  slack \(\sigma\).  For \(Y=\mathcal I(X^3)\), this gives
  \(\alpha=-3/2-3\kappa\), \(\beta=1/2-3\kappa\), and
  \(\sigma=3\kappa\).
- Added Proposition
  `prop:spde-nonlinear-negative-coordinate-wick-decomposition`.
- This proposition gives the exact finite-cutoff Wick decompositions of
  \(XY\) and locally subtracted \(X^2Y\):
  - \(XY\) splits into fourth- and second-chaos pieces with coefficients
    \(1,3\).
  - \(X^2Y\) splits into fifth-, third-, and first-chaos pieces with
    coefficients \(1,6,6\), and the first-chaos piece is locally subtracted
    by \(3C_{2,\epsilon}X_\epsilon\).
  - The local subtraction rewrites the first-chaos term as
    \(6\int K_\epsilon G_\epsilon^2(X_\epsilon(b)-X_\epsilon(a))\,db\),
    identifying the exact Taylor-gain input for the next multiscale estimate.
- Added Proposition
  `prop:spde-nonlinear-negative-coordinate-chaos-kernels`.
- This proposition converts the finite-cutoff Wick identities into tested
  Hilbert-space finite-chaos kernels:
  - \(XY\) gives chaos arities \(4\) and \(2\).
  - locally subtracted \(X^2Y\) gives chaos arities \(5\), \(3\), and \(1\).
  - the first-chaos kernel is explicitly
    \(6\int\chi K_\epsilon G_\epsilon^2
      (p_\epsilon(b)-p_\epsilon(a))\,da\,db\).
- Added Proposition
  `prop:spde-nonlinear-negative-coordinate-kernel-norms`.
- This proposition computes the scalar covariance-integral formulas for the
  Hilbert norms of those tested kernels.  The exact symmetrization weights
  are:
  - \(1/4,3/4\) for the fourth-chaos \(XY\) kernel.
  - \(1/10,3/5,3/10\) for the fifth-chaos \(X^2Y\) kernel.
  - \(1/3,2/3\) for the third-chaos \(X^2Y\) kernel.
  - the first-chaos \(X^2Y\) kernel contains the covariance increment
    \(G_{bb'}-G_{ba'}-G_{ab'}+G_{aa'}\).
- Added Proposition
  `prop:spde-x2y-first-chaos-logarithmic-scale-bound`.
- This proposition proves the first deterministic analytic estimate for the
  locally subtracted \(X^2Y\) first-chaos sector:
  - local \(KG^2\) packets are assumed shell \(L^1\)-bounded, matching the
    already proved two-loop shell estimate.
  - covariance blocks satisfy an explicit dyadic double-increment bound.
  - the resulting first-chaos variance is
    \(O(\delta^{-1}(1+|\log\delta|)^2)\).
  - after normalizing by the assigned homogeneity
    \(-1/2-5\kappa\), the logarithm is absorbed as an arbitrary small loss
    from the \(5\kappa\) slack.
- Added Corollary `cor:spde-local-kg2-shell-lone-bound`.
- This corollary verifies the local shell \(L^1\) hypothesis for the
  \(KG^2\) packets in dynamic \(\Phi^4_3\): heat order \(2\) and covariance
  orders \(4,4\) give relative gaps \(3,1,1\), hence the shell
  \(\max(i,j,\ell)=n\) is uniformly summable.

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  arithmetic for:
  - the white-noise coordinate slack \(\kappa\);
  - the Wick-coordinate slacks \(k\kappa\), \(k=1,2,3\);
  - local integrability condition \(k<5\);
  - a sample Holder edge factor.
  - the wavelet summability and edge-tail inequalities in the dual-norm
    Gaussian-coordinate upgrade.
  - the heat-integration coarse/fine scale arithmetic that transfers the
    \(X^3\) slack to the \(c_n\) coefficient.
  - the nonlinear-coordinate Wick contraction coefficients, \(3C_2\) local
    subtraction normalization, and the target \(XY\), \(X^2Y\) scale slacks.
  - the tested finite-chaos arities \(4,2\) and \(5,3,1\) for the nonlinear
    negative coordinates.
  - the symmetrized kernel-norm weights and the first-chaos increment signs
    used in the covariance-integral formulas.
  - the first-chaos logarithmic physical-scale arithmetic
    \(\delta^{-1}(1+|\log\delta|)^2\) and the resulting normalized slack
    after a sample logarithmic loss.

## Remaining Issue #582 Obligations

- Extend the dual-norm strategy from primitive Gaussian coordinates to the
  concrete finite-cutoff chaos kernels in the displayed \(XY\) and \(X^2Y\)
  decompositions.
- Verify the regulator-specific covariance double-increment hypothesis
  entering the first-chaos bound directly from the chosen cutoff kernels.
- Prove the genuinely nonlinear BPHZ coordinate estimates for the remaining
  explicit scalar covariance kernels: \(XY\)'s fourth and second chaos and
  \(X^2Y\)'s fifth and third chaos.
- Supply the remaining \(X^3\) cutoff-difference and base-increment estimates
  needed to feed the deterministic \(c_n\) transfer into the full
  scale-summed \(\Gamma\)-coordinate theorem.
- Extend from the strict negative sector to the solution sector and complete
  the invariant-law/OS comparison.
