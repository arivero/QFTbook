# 2026-05-26 Issue #582 Two-Loop Sector Gaps

## Scope

- Volume XI, Chapter 9 now proves the deterministic two-loop scale estimate
  needed after the one-loop prototype and before the abstract multiscale
  summability theorem.
- The pass separates the non-nested sunset tree from the nested tadpole
  subgraph and proves that the latter is canceled scale by scale by the
  recursive one-loop forest subtraction.

## Mathematical Content

- For kernels of orders \(a,b,c\) in homogeneous dimension \(Q\), with
  \(a+b+c=2Q\), define
  \[
    S_{i,j,\ell}=\int K_i(h)L_j(h)M_\ell(h)\,\dd h,\qquad
    n_*=\max(i,j,\ell).
  \]
- The support intersection is contained in the smallest parabolic ball,
  \(B_{\mathfrak s}(0,A2^{-n_*})\).  Substituting
  \(i=n_*-r_K\), \(j=n_*-r_L\), \(\ell=n_*-r_M\), the equal-scale exponent
  cancels:
  \[
    (Q-a)+(Q-b)+(Q-c)-Q=2Q-(a+b+c)=0.
  \]
- The block estimate is therefore
  \[
    |S_{i,j,\ell}|
    \leq C
    2^{-(Q-a)r_K-(Q-b)r_L-(Q-c)r_M}.
  \]
- The dyadic shell \(\max(i,j,\ell)=N+1\) is covered by the union of the
  three events \(r_K=0\), \(r_L=0\), \(r_M=0\), giving a uniform shell bound.
- In dynamic \(\Phi^4_3\), the orders are heat/covariance/covariance
  \((2,4,4)\) with \(Q=5\), hence the gap exponents are \((3,1,1)\) and the
  shell constant is \(60/7\).
- For the nested tadpole, the fixed-scale local coefficient from
  \(X(z)^2K_iX(w)^3\) is
  \(+6C_{1,\ell}\int K_iG_j\).  The inner one-loop forest subtraction
  \(X(w)^3\mapsto X(w)^3-3C_{1,\ell}X(w)\) contributes
  \(-6C_{1,\ell}\int K_iG_j\), so the nested coefficient is exactly zero at
  each scale triple.

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies:
  - the logarithmic balance \(2Q-(2+4+4)=0\);
  - the dynamic \(\Phi^4_3\) gap exponents \((3,1,1)\);
  - the sunset shell factor \(60/7\);
  - the nested forest cancellation \(2\cdot3-3\cdot2=0\).

## Remaining Issue #582 Obligations

- Convert the concrete sector bounds into the \(\Pi\)- and
  \(\Gamma\)-coordinate charts of the finite dynamic \(\Phi^4_3\) model.
- Verify the coordinate-to-model domination hypotheses for those charts.
- Complete the random-model Cauchy theorem application and then the
  SPDE-to-OS passage.
