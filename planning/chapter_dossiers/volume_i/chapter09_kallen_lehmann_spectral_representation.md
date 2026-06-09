# Volume I, Chapter 9 Dossier: Kallen-Lehmann Spectral Representation
Source-File: monograph/tex/volumes/volume_i/chapter09_kallen_lehmann_spectral_representation_and_particle_content.tex

## Status

Current status: certified against 253a pp. 80--99 on 2026-05-22.  The
2026-05-29 anti-wrapper pass demoted the spacelike \(\Delta_+\) parity check
to a worked paragraph and strengthened the isolated scalar-shell matrix
element proposition by making the selected spin-zero channel and possible
multiplicity-space interpretation explicit.  The 2026-06-09 issue #973 pass
split the invariant mass-shell disintegration at the two-dimensional infrared
endpoint: \(D\ge3\) retains the ordinary scalar zero-mass shell, while
\(D=2\) has two punctured null-ray orbits and a positive locally finite scalar
measure on the full closed cone has \(\rho(\{0\})=0\).

## Logical Role

This chapter is the first full nonperturbative bridge from local fields to
particle content. It uses only Hilbert-space positivity, translation
invariance, the spectrum condition, scalar-field covariance, and the spectral
theorem for the energy-momentum operators. It precedes perturbative
correlation-function diagrams and precedes all scattering theory.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, section "Spectral Representations
  and Particle Content", through the Kallen-Lehmann representation and the
  decomposition into one-particle and continuum spectral support.
- Handwritten visual trace
  `monograph/tex/build/source_visual_trace/253a_trace-080.png` through
  `253a_trace-099.png`.
- `references/253a_notes.tex`, corresponding Kallen-Lehmann and particle
  content sections, used only as a comparison layer.
- `monograph/tex/volumes/volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex`,
  for the definitions of Wightman, time-ordered, and Euclidean Green
  functions.
- `monograph/tex/volumes/volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex`,
  for invariant one-particle normalization.

## Framework

Working framework:

- Hilbert space \(\Hilb\) with unitary representation of the proper
  orthochronous Poincare group;
- invariant vacuum \(\Omega\);
- commuting self-adjoint translation generators \(P^\mu\);
- joint spectrum contained in the closed forward cone;
- scalar operator-valued distribution \(\widehat\phi\) with
  \(\langle\Omega|\widehat\phi|\Omega\rangle=0\) after shifting by a constant
  when necessary;
- matrix elements understood after smearing, with point notation used for the
  corresponding distributions.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(E(\Delta)\) | projection-valued measure | joint spectral measure of \(P^\mu\) |
| \(\nu_\phi\) | positive measure | spectral measure of \(\widehat\phi(0)\Omega\) |
| \(W_2(x)\) | distribution | scalar Wightman two-point function |
| \(G_T(x)\) | distribution | time-ordered two-point function |
| \(G_E(x_E)\) | distribution | Euclidean two-point function |
| \(\Delta_+(x;\mu^2)\) | distribution | positive-frequency free scalar two-point function of mass \(\mu\) |
| \(\Delta_F(x;\mu^2)\) | distribution | Feynman propagator of mass \(\mu\) |
| \(d\rho(\mu^2)\) | positive measure | Kallen-Lehmann spectral measure |
| \(\delta_{a}\) | unit point measure | Borel measure on \([0,\infty)\) with total mass one at \(s=a\) |
| \(\Sigma_s^+\) | homogeneous orbit | positive mass shell \(\{p\in\overline V_+:-p^2=s\}\), \(s>0\) |
| \(\Sigma_0^{+\times}\) | homogeneous orbit for \(D\ge3\) | punctured future light cone |
| \(R_{\mathrm R},R_{\mathrm L}\) | homogeneous orbits for \(D=2\) | right- and left-moving punctured future null rays |
| \(\sigma_s\) | invariant Radon measure | normalized Lorentz-invariant measure on \(\Sigma_s^+\), on \(\Sigma_0^{+\times}\) for \(D\ge3\), or \(dk/(4\pi k)\) on each \(D=2\) punctured null ray before the closed-cone local-finiteness test |
| \(\lambda\) | positive measure | intermediate Mackey--Effros orbit-space measure before absorbing shell normalizations |
| \(Z\) | nonnegative number | atom of \(d\rho\) at an isolated one-particle mass \(m^2\) |
| \(d\rho_{\mathrm c}\) | positive measure | continuum part of the spectral measure |
| \(L(\vec k)\) | Lorentz transformation | standard boost from rest momentum to \(k^\mu=(\omega_{\vec k},\vec k)\) |
| \(W(\Lambda,k)\) | little-group element | Wigner rotation \(L(\Lambda k)^{-1}\Lambda L(k)\) |
| \(N(\vec k)\) | normalization factor | factor relating delta-normalized scalar one-particle states to standard boosts |

## Definition Ledger

- spectral measure associated to a local scalar field acting on the vacuum;
- Lorentz orbit map \(\pi(p)=-p^2\), orbit representatives \(k_s\) and
  \(\ell\), stabilizers \(SO(D-1)\) and \(ISO(D-2)\) for \(D\ge3\), the
  \(D=2\) split into \(R_{\mathrm R}\) and \(R_{\mathrm L}\), and the normalized
  invariant shell measures \(\sigma_s\);
- positive-frequency scalar two-point function \(\Delta_+\);
- Kallen-Lehmann spectral measure \(d\rho\);
- canonical equal-time normalization and the commutator-antisymmetry sign
  converting \([\phi,\pi]=+\ii\delta\) into
  \([\pi,\phi]=-\ii\delta\) in the spectral sum-rule derivative;
- time-ordered and Euclidean Kallen-Lehmann representations;
- \(k^0\)-contour derivation of the Feynman prescription;
- scalar one-particle standard boosts, Wigner little group, and invariant
  normalization;
- isolated one-particle atom and field-strength overlap \(Z\);
- spectral distinction between a nonzero isolated Hilbert-space mass shell and
  a merely continuous Kallen-Lehmann threshold;
- continuum spectral support and threshold assumptions.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The two-point Wightman function is the Fourier transform of a positive measure supported in the forward cone. | Theorem/construction | Joint spectral theorem and spectrum condition |
| Scalar covariance makes the spectral measure a positive measure over invariant masses. | Derived with endpoint split | Lorentz invariance of the vacuum and scalar field; \(D=2\) null-ray coefficients vanish under closed-cone local finiteness |
| \(W_2(x)=\int d\rho(\mu^2)\Delta_+(x;\mu^2)\). | Derived | Mackey--Effros disintegration after explicit verification of the Lorentz-orbit hypotheses; in \(D=2\) the locally finite scalar case has \(\rho(\{0\})=0\) |
| \(\Delta_+(x;\mu^2)=\Delta_+(-x;\mu^2)\) for spacelike \(x\). | Worked calculation | Lorentz frame with \(x^0=0\) and \(\vec p\mapsto-\vec p\); demoted from proposition wrapper on 2026-05-29 |
| \(G_T(x)=\int d\rho(\mu^2)\Delta_F(x;\mu^2)\). | Derived | Definition of time ordering and linearity |
| The \(i\epsilon\) prescription places the positive-energy pole below and the negative-energy pole above the real \(k^0\)-axis. | Derived | Explicit contour closure for \(x^0>0\) and \(x^0<0\) |
| \(G_E(x_E)=\int d\rho(\mu^2)\Delta_E(x_E;\mu^2)\) under analytic continuation. | Framework statement/derived from Chapter 8 conditions | Spectral positivity and Euclidean continuation |
| The canonical sum-rule derivative uses \([\pi_0(\vec r),\phi_0(\vec0)]=-\ii\delta^{(d)}(\vec r)\mathbf1\), obtained from \([\phi_0,\pi_0]=+\ii\delta\mathbf1\) by commutator antisymmetry. | Derived | Explicit sign bridge added in issue #369 pass |
| Delta-normalized scalar one-particle states have \(N(\vec k)=\sqrt{m/\omega_{\vec k}}\). | Derived | Standard boost construction plus Lorentz invariance of the on-shell measure |
| An isolated one-particle mass created by \(\widehat\phi\) is an atom \(Z\,\delta_{m^2}(\dd\mu^2)\) of the spectral measure. | Definition plus derivation | Projection onto the isolated mass shell; issue #379 notation pass |
| For a single stable massive scalar channel with no massless particle, no lighter particles or bound-state atoms, and two-particle continuum onset, \(\operatorname{supp}d\rho_\phi\subset\{m^2\}\cup[4m^2,\infty)\). | Conditional support hypothesis | Issue #382 pass; support remark before Haag--Ruelle/LSZ dependence |
| The existence of a stable one-particle species is the nonzero isolated spectral projection \(E(\Sigma_m^+)\Hilb\ne0\), not a consequence of the Kallen-Lehmann formula itself. | Clarified assumption/status statement | Joint spectral theorem plus atom criterion |
| \(Z\) depends on the local field normalization and is intrinsic once the field and the selected scalar channel or multiplicity-space overlap are fixed. | Definition/consequence | Matrix element normalization; 2026-05-29 multiplicity clarification |

## Figure Ledger

Figures to include:

- \(k^0\)-plane contour figure with the \(+\omega-\ii0\) pole below and
  \(-\omega+\ii0\) pole above;
- positive mass-shell figure showing the standard boost \(L(\vec k)\);
- spectral projection of \(\widehat\phi(f)\Omega\) into vacuum, one-particle,
  and continuum spectral components;
- spectral measure with an isolated atom at \(m\) and continuum support
  beginning at a stated threshold.

## Audit Targets

- Use a positive measure \(d\rho\), not only a smooth function, so delta
  contributions are properly represented.
- Preserve the \(D=2\) endpoint split: two punctured null rays on \(X\), zero
  scalar null-ray coefficient for positive locally finite measures on
  \(\overline V_+\), and separate infrared prescriptions for zero-mode,
  derivative, or chiral massless fields.
- State the assumptions behind the \(2m\) threshold.
- Do not define scattering or asymptotic states in this chapter.
- Keep \(Z\) as a field-overlap datum, not a slogan.

## Certification Notes

- Added the generalized spectral insertion notation while keeping the
  projection-valued measure as the rigorous object.
- Added the spacelike equality of \(\Delta_+\), the \(k^0\)-residue calculation
  for \(\Delta_F\), and the lower-half-plane Euclidean continuation condition.
- Added the scalar one-particle representation construction, including the
  standard boost, Wigner little group, \(N(\vec k)=\sqrt{m/\omega_{\vec k}}\),
  and the delta-normalized and invariant-normalized versions of the \(Z\)
  overlap.
- 2026-05-24 issue #328 pass: added an explicit remark that a
  Kallen-Lehmann measure may have no atom, that \(E(\Sigma_m^+)\Hilb\) may be
  zero or non-isolated, and that Haag--Ruelle/LSZ use of that shell is then
  absent rather than implicit.
- 2026-05-24 issue #369 pass: inserted the commutator-antisymmetry sign step in
  the canonical Kallen--Lehmann sum-rule derivation.
- 2026-05-24 issue #379 pass: standardized \(\delta_{m^2}\) as the unit point
  measure and wrote atomic contributions as \(Z\,\delta_{m^2}(\dd s)\) or
  \(Z\,\delta_{m^2}(\dd\mu^2)\), avoiding density-vs-measure overload.
- 2026-05-24 issue #382 pass: added the single-massive-scalar support
  hypothesis \(\dd\rho_\phi\) has no massless atom, has an isolated atom at
  \(m^2\), and has continuum support beginning at \(4m^2\) under the stated
  two-particle-threshold assumptions.
- 2026-05-24 issue #425 pass: kept \(d\rho\) as the Kallen--Lehmann spectral
  measure notation and moved the unrelated two-body kinematic factor in later
  scattering chapters to \(\beta(s)\).
- 2026-05-24 issue #433 pass: later renormalization chapters denote this
  isolated spectral atom by \(Z_\phi^{\rm pole}\) when it must be compared
  with \(Z[J]\), \(Z_{\rm MOM}(\mu)\), \(Z_\phi^{\rm chart}\), and
  \(Z_\phi^{\rm MS}\).  The Kallen--Lehmann object remains a field-overlap
  datum after the interpolating field normalization is fixed.
- 2026-05-25 issue #507 pass: replaced the black-box "standard
  orbit-disintegration theorem" proof with a Mackey--Effros proof that verifies
  the hypotheses for \(SO^+(1,D-1)\) acting on the forward cone: standard
  Borel orbit space \([0,\infty)\), Borel section \(c(0)=\ell\),
  \(c(s)=k_s\), closed unimodular stabilizers \(SO(D-1)\) and \(ISO(D-2)\),
  measurable normalized shell measures \(\sigma_s\), and absorption of the
  conditional-measure scalar \(c(s)\) into the Kallen--Lehmann measure
  \(d\rho(s)\).
- 2026-06-09 issue #973 pass: corrected the issue #507 low-dimensional
  endpoint by separating \(D\ge3\) from \(D=2\), displaying the two
  \(SO^+(1,1)\) null-ray orbits, deriving the \(dk/(4\pi k)\) ray measure,
  using dyadic annuli as the logarithmic divergence check for test functions
  equal to one near \(p=0\), and propagating \(\rho(\{0\})=0\) to
  \(\Delta_+\), \(\Delta_F\), Euclidean kernels, and Stieltjes endpoint prose.
  Added `calculation-checks/kallen_lehmann_low_dimensional_checks.py` as the
  executable endpoint/orbit regression check.
- 2026-05-30 anti-wrapper audit pass: strengthened the first spectral-measure
  proposition so the measure is characterized by smeared Wightman
  distributions and the Bochner--Schwartz positive-measure representation,
  while the conventional
  \(\langle\vac|\widehat\phi(0)E(\Delta)\widehat\phi(0)|\vac\rangle\)
  notation is explicitly identified as shorthand rather than a literal point
  vector.
- Rendered manuscript pages `kallen_render-090.png` through
  `kallen_render-098.png`; figures are legible and do not use handwritten
  inclusions.
