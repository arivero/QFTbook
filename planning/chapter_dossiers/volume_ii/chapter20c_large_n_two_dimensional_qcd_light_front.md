# Volume II, Large-N Two-Dimensional QCD And Light-Front Bound States Dossier

## Logical Role

- TeX source:
  `monograph/tex/volumes/volume_ii/chapter20c_large_n_two_dimensional_qcd_light_front.tex`.
- Compiled in the gauge-theory volume after the Schwinger model and before the
  Standard Model hybrid-definition chapter.
- Addresses the light-front / two-dimensional large-\(N\) QCD part of GitHub
  issue #596.
- Role in the monograph: give an analytic benchmark where a nonabelian gauge
  constraint, planar color algebra, and color-singlet Hilbert-space sectors
  produce a computable bound-state equation without treating colored quarks as
  physical external particles.

## Definitions And Results

The chapter establishes:

- the \(SU(N_c)\) two-dimensional QCD action in the monograph's trace-delta
  convention, with \(\operatorname{tr}_{\square}(t^at^b)=\delta^{ab}\);
- the fundamental completeness relation
  \[
    (t^a)^i{}_j(t^a)^k{}_\ell
    =\delta^i{}_\ell\delta^k{}_j-N_c^{-1}\delta^i{}_j\delta^k{}_\ell;
  \]
- the dimensionful large-\(N_c\) coupling coordinate
  \(\lambda_2=g_2^2N_c\);
- light-front coordinates \(x^\pm=(x^0\pm x^1)/\sqrt2\), the convention
  \(\dd s^2=-2\dd x^+\dd x^-\), and \(M^2=2P^+P^-\);
- the finite-regulator status of light-front quantization, including the
  zero-mode caveat;
- light-front gauge \(A_-=0\), the nondynamical \(A_+\) action, and the
  Gauss-law constraint;
- a finite-regulator Gauss-law reduction paragraph that performs the
  nonzero-mode Gaussian square completion and isolates the zero-mode caveat;
- the leading large-\(N_c\) color-singlet meson state;
- Definition `def:qcd2-subtracted-thooft-operator`, using the subtracted
  principal-value kernel
  \[
    \operatorname{PV}\int_0^1
    {(\phi(x)-\phi(y))/(x-y)^2}\,\dd y ;
  \]
- Theorem `thm:qcd2-planar-thooft-equation`, deriving the planar light-front
  meson equation under an explicit regulator-convergence hypothesis;
- the normalization \(\gamma_2=\lambda_2/\pi\) for the standard continuum
  principal-value convention;
- a remark separating the subtracted positive-kernel convention from the
  unsubtracted mass-coordinate convention common in the literature;
- a positive-kernel paragraph deriving the quadratic form identity
  \[
    \frac12\int_0^1\dd x\int_0^1\dd y
    {(\phi(x)-\phi(y))^2\over (x-y)^2};
  \]
- the chiral-limit constant zero mode \(M_0^2=0\) at leading planar order;
- the endpoint finite-part coefficient
  \(\pi\beta\cot(\pi\beta)-1\) in the subtracted convention, and the endpoint
  exponent equation
  \(m_i^2/\gamma_2=1-\pi\beta_i\cot(\pi\beta_i)\);
- the closed continuum quadratic form on \(L^2(0,1)\), its form domain with
  endpoint weights, the associated nonnegative self-adjoint mass operator, and
  compact resolvent/discrete spectrum for \(\gamma_2>0\);
- the finite DLCQ matrix and its exact quadratic-form identity;
- a controlled-approximation block stating the data needed before finite DLCQ
  eigenvalues become continuum meson-mass claims;
- controlled approximation
  `ca:qcd2-dlcq-current-correlator-residue-contract`, which upgrades the
  finite DLCQ output from masses alone to current correlators by requiring the
  source vectors, spectral residues, source normalization, and residue
  extrapolation data;
- a positive scope section identifying exactly what the two-dimensional
  large-\(N_c\) construction establishes.

## Claim Ledger

1. The gauge field in \(1+1\) dimensions has no propagating transverse
   polarization, but the nonabelian Gauss law remains a nontrivial constraint.
2. In light-front gauge, the nonzero modes of \(A_+\) are Gaussian constraint
   variables; integrating them out gives an instantaneous current-current
   Hamiltonian.
3. The \(A_+\) zero mode is part of the global Gauss-law datum and cannot be
   silently discarded.
4. The planar color contraction of a normalized color-singlet meson is fixed
   by the trace-delta completeness relation; the trace-subtraction term is
   subleading at fixed \(N_f\).
5. The real instantaneous exchange and self-energy pieces must be regulated
   together.  Their paired finite part is the subtracted 't Hooft kernel.
6. The subtracted kernel is positive as a quadratic form and has an exact
   constant zero mode in the massless equal-flavor case.
7. Endpoint powers are fixed by cancellation of the leading finite-part
   singularity in the same subtracted convention that defines the operator.
8. The continuum spectral problem is the self-adjoint operator associated to
   the closed positive form, not merely the formal principal-value expression.
9. The common unsubtracted presentation is a different mass-coordinate
   convention, not a different physical equation.
10. DLCQ matrix eigenvalues are finite-regulator spectral data until zero-mode,
   endpoint-mass, coefficient-matching, and \(K\to\infty\) convergence data are
   supplied.
11. Current correlators and decay-constant residues require finite source
    vectors and eigenvector overlaps.  Two finite regulators can have the same
    mass eigenvalues but different source residues, so the spectrum alone is
    not the meson observable.

## Calculation Checks

- `calculation-checks/thooft_model_checks.py` verifies, under an extended
  evidence contract, trace-delta color normalization, the finite DLCQ
  quadratic-form identity, positivity in a positive endpoint-mass sample, the
  exact massless constant zero mode of the subtracted finite kernel, the
  endpoint-exponent small-mass expansion, the finite-form monotonicity shadow
  of the closed continuum form, and the current-correlator spectral-measure
  identity.  The companion includes a negative control where fixed finite
  eigenvalues leave current-source residues and Euclidean correlators changed.

## Figure Requirements

- Current chapter contains no figures.  A later light-front constraint-flow
  figure would be acceptable only if it distinguishes finite-regulator
  constraint solving from the continuum bound-state claim.

## Open Development

- Add a numerical spectral comparison between finite DLCQ matrices and the
  continuum integral operator with a controlled extrapolation model.
- Develop the \(1/N_c\) meson-interaction corrections and connect them to the
  general large-\(N_c\) discussion in the four-dimensional QCD chapter.
- Develop the separate 3D Chern--Simons--matter light-front planar solution
  required by issue #596.

## Audit Notes

- 2026-06-06 issue #596/#725 DLCQ current-residue pass: added
  `ca:qcd2-dlcq-current-correlator-residue-contract` so the large-\(N_c\)
  two-dimensional QCD chapter distinguishes finite meson masses from the
  source spectral measure that determines current correlators and residues.
  Promoted `calculation-checks/thooft_model_checks.py` to an extended
  evidence contract with a fixed-spectrum/different-residue negative control.
