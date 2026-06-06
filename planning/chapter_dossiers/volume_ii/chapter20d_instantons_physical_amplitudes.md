# Volume II, Instantons as Physical Amplitudes Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Compiled in the gauge/anomaly part through
  `monograph/tex/volumes/volume_iv/volume_iv_current.tex`, immediately after
  `chapter20_chiral_axial_anomalies.tex`.
- Role in the monograph: begin the dedicated instanton-physics chapter
  requested by the soliton/monopole/instanton depth lane.  It treats the
  BPST/ADHM measure data of Ch20 as input to physical amplitudes rather than
  as the endpoint of the calculation.
- Relation to Ch20: Ch20 remains the anomaly and BPST derivation home.  This
  chapter reorganizes the instanton material around physical channels:
  fluctuation determinants, zero-mode saturation, source typing, size windows,
  observable projection, and residual budgets.

## Definitions And Results

- `ch:instantons-physical-amplitudes`: dedicated chapter for instantons as
  physical amplitudes.
- `sec:instanton-density-gate`: one-loop density gate separating the
  collective-coordinate Jacobian, bosonic zero-mode normalization, running
  BPST action, zero-mode-deleted fluctuation determinant logarithm, and finite
  scheme constant before the density is inserted into a physical channel.
- `ca:instanton-one-loop-density-gate-channel`: checks that the universal
  density power is fixed by the one-loop RG cancellation, while the channel
  size power also depends on zero-mode/source data such as mass saturation or
  hard external source differentiation.
- `def:instanton-physical-amplitude-channel`: finite-regulator channel datum
  consisting of a retained window, collective density, nonzero-mode determinant,
  zero-mode Berezin coefficient, source/matching map, endpoint factor, and
  physical projection.
- `eq:instanton-physical-channel-functional`: the channel coefficient after the
  determinant, zero-mode, source, endpoint, and projection data are assembled.
- `eq:instanton-physical-channel-residual-budget`: reusable residual budget
  separating determinant/fluctuation, zero-mode/source, endpoint, sector,
  continuation, spectral, infrared, cut, and scheme errors.
- `prop:instanton-moduli-equivalent-channel-separation`: moduli-equivalent
  channels can have different, or zero, amplitudes because the two-flavor
  zero-mode source determinant may vanish or differ.
- `prop:two-flavor-source-mass-determinant-coordinate`: exact expansion of
  `det(M+B)` into vacuum, mass-assisted source, and four-source coordinates.
- `sec:instanton-hard-four-fermion-benchmark`: hard two-flavor four-source
  benchmark, organized as center, Haar, zero-mode-rank, amputation,
  size-window, and physical-projection gates.
- `prop:instanton-hard-individual-zero-mode-slot`: derives the individual
  singular-gauge BPST zero-mode slot profile used by the hard four-source
  amplitude, including `F_zm(0)=1`, the `6 (rho |p|)^(-3)` tail, and the
  four-slot product `6^4 prod c_l^(-3) s^(-12)`.
- `prop:su3-nf2-hard-source-power-slow-tail`: derives the SU(3), `N_f=2`
  hard four-source powers `rho^(32/3) d rho`,
  `Lambda_ht^(29/3) Q^(-35/3)`, and the slow `R^(-1/3)` large-size tail.
- `ca:instanton-hard-benchmark-gate-ledger`: same-theory hard-scale ratio and
  residual multiplier bound after the gate data and source-window shape have
  been transported.
- `sec:instanton-hard-wilsonian-ope-datum`: Wilsonian interpretation of the
  hard four-source kernel as a short-distance local four-fermion coefficient,
  with the dimensionless size split \(R\), boundary-flux flow, operator
  matching, physical matrix element, and long-size remainder kept separate.
- `sec:instanton-normal-fluctuation-source-data`: local amplitude-facing block
  separating the determinant normalization of nonzero modes from the
  fluctuation average of the selected source insertion.
- `ca:instanton-nonzero-mode-source-quotient`: finite Gaussian source quotient
  and covariance identity, including the quadratic source trace correction
  `1/2 Tr(QC)` and the absolute bound
  `epsilon_U + M_U M_V / d_0`.
- `sec:instanton-hard-amplitude-assembly`: recombines the hard source kernel,
  finite determinant normalization, nonzero-mode source quotient,
  zero-mode/source stability, and physical projection into one regulated
  amplitude coordinate.
- `ca:instanton-hard-amplitude-assembly-ledger`: assembled hard-amplitude
  absolute error bound, with noncancellation margin required before relative
  scale-law claims are allowed.
- `sec:instanton-source-kernel-physical-projection`: projection bridge from an
  assembled Euclidean instanton source kernel to a physical pole, spectral,
  OPE, or inclusive observable coordinate.
- `ca:instanton-source-kernel-physical-projection`: physical bridge residual
  bound separating regulator transport, analytic continuation, pole/bin
  isolation, infrared completion, unitarity-cut normalization, matching, and
  endpoint control.
- `sec:instanton-first-cluster-amplitude-correction`: source-amplitude bridge
  from the assembled one-instanton coefficient to the first connected
  instanton-pair correction.
- `ca:instanton-first-cluster-amplitude-correction`: first cluster correction
  ledger for a source amplitude, including disconnected one-body subtraction,
  neutral-pair source visibility, same-charge theta harmonic data, pair-kernel
  residual control, and the sector-isolation consequence.
- `sec:instanton-observable-handoffs`: physics handoff block distinguishing a
  hard source coefficient, theta curvature, \(U(1)_A\)-odd susceptibility
  kernel, and real-time axial relaxation rate.
- `ca:instanton-observable-handoff-ledger`: finite-regulator observable map
  discipline: the one-instanton amplitude density must be projected to a named
  observable before its physical meaning is fixed.
- `ca:finite-cell-instanton-channel-control`: finite retained-cell model
  proving the absolute residual bound and the two-by-two determinant stability
  estimate.

## Claim Ledger

- The new chapter advances issue #597 at the architecture level: it starts a
  dedicated instanton chapter and makes the physical channel, rather than the
  moduli space, the organizing object.
- The first substantive result is not an ADHM refinement.  It proves that the
  same collective-coordinate measure and nonzero-mode determinant convention
  can give different physical amplitudes once zero-mode source rank and
  projection are changed.
- The density-gate block prevents the hard benchmark from treating
  `rho^(b0-5)` as a moduli-space fact.  It records the fluctuation/RG origin
  of `(mu rho)^b0`, the finite determinant constant, and the added
  zero-mode/source power `beta_C` that turns a density into a channel
  integrand.
- The two-flavor determinant calculation is the local algebra behind the
  distinction between a mass-saturated vacuum activity and a differentiated
  four-source 't Hooft amplitude.
- The hard benchmark section moves beyond the local determinant to a physical
  four-source channel: center conservation, shared Haar projection, two
  zero-mode source determinants, amputation, hard form factors, and endpoint
  tails must all be part of the coefficient before a scale law is quoted.
- The individual-slot form-factor block opens one of the hard channel's
  previously compressed inputs: the endpoint tail comes from the cancellation
  of the apparent `t^(-1)` terms in the BPST zero-mode Bessel products, giving
  the differentiated-slot power tail rather than the fused-density exponential
  source class.
- The normal-fluctuation source quotient opens the next compressed input:
  even after the Gaussian determinant is normalized, the selected hard source
  has a mean and a covariance with nonzero-mode interactions.  A vacuum
  determinant constant alone cannot control a four-source amplitude.
- The assembled hard-channel ledger prevents the chapter from becoming a list
  of adjacent gates.  It places the determinant scheme constant, hard
  zero-mode slots, nonzero-mode source quotient, source-frame stability, and
  projection mismatch in a single amplitude formula, with absolute
  signed-window control and an explicit noncancellation hypothesis for
  relative statements.
- The physical projection bridge opens the last compressed step between a
  Euclidean instanton source coefficient and a physical claim.  It separates
  stable-particle pole extraction, spectral-bin/discontinuity functionals,
  OPE matching, colored auxiliary kernels, and bridge residuals, so a
  Euclidean source number cannot be relabelled as a scattering amplitude or
  spectral observable.
- The observable-handoff block connects the dedicated instanton-amplitude
  chapter back to the QCD theta and \(U(1)_A\) material without duplicating it:
  a hard four-source coefficient, a dilute theta curvature, a zero-mode-zone
  \(U(1)_A\)-odd kernel, and a real-time Chern--Simons diffusion rate are
  separate final maps from the instanton-side data.
- The first cluster correction block addresses the next amplitude obstruction
  after the one-instanton hard coefficient.  It treats the neutral
  instanton--anti-instanton and same-charge pair sectors as source/projection
  data: the disconnected product must be subtracted, the neutral pair can
  affect source correlators without theta curvature, and the same-charge pair
  carries the first second-harmonic theta correction.
- The `Q^(-35/3)` hard-scale behavior is tied to `b0=29/3` and four individual
  hard zero-mode form factors.  The large-size endpoint is convergent but slow,
  with a retained-tail majorant of order `R^(-1/3)`, so a window/stability
  budget is load-bearing.
- The Wilsonian OPE bridge makes the hard benchmark usable as a local QFT
  input only after a size split.  The short coefficient has a nonzero boundary
  flow, the long-size tail cancels that flow in the completed split, and the
  physical observable still needs the renormalized four-fermion matrix element
  plus matching, infrared, projection, and sector residuals.
- The finite-cell control model records why residuals such as source rank,
  endpoint, spectral projection, cut, infrared, and scheme transport are
  load-bearing.  Dropping them changes the physical claim.

## Figure Ledger

- No new figure in this pass.  The chapter is equation/proposition driven.
- If the chapter is expanded, likely figure candidates are an amplitude-channel
  flow diagram and a finite-cell projection diagram, but neither is required
  for the current derivations.

## Calculation Checks

- `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  carries the companion evidence contract.
- The check verifies the exact `det(M+B)` polynomial, rejects the wrong
  off-diagonal sign, separates mass-saturated and four-source coordinates,
  verifies the one-loop density RG gate and the distinction between
  density-only, mass-saturated, and hard four-source size powers,
  derives the individual zero-mode slot tail coefficient from the Bessel
  product cancellation and rejects fused-density endpoint substitution or
  hidden unamputated residues,
  verifies the finite Gaussian nonzero-mode source quotient covariance
  identity, the quadratic trace correction, absolute window propagation, and
  rank-loss rejection,
  verifies the assembled hard-amplitude product bound and rejects
  determinant-only assembly or signed-window relative control without a
  noncancellation margin,
  verifies the observable-handoff distinction between hard source coefficients,
  dilute theta curvature, \(U(1)_A\)-odd zero-mode-zone kernels, real-time
  axial rates, and Witten--Veneziano curvature comparison budgets,
  verifies the physical projection bridge from Euclidean source kernels to
  pole-window and spectral-bin coordinates, including contact-polynomial
  separation, one-Euclidean-value inversion failure, bridge residual control,
  and colored-kernel LSZ rejection,
  verifies the first connected instanton-pair source correction, including
  disconnected subtraction, neutral-pair source visibility despite zero theta
  curvature, same-charge second-harmonic data, zero-mode overlap survival, and
  pair residual control,
  builds moduli-equivalent finite cell channels with different or vanishing
  amplitudes, constructs a same-Euclidean-sum/different-projection ambiguity,
  checks the SU(3), `N_f=2` hard four-source scale and tail powers, validates
  the hard gate ledger and same-theory ratio residual bound, verifies the
  hard-kernel Wilsonian OPE boundary flow and long-size tail budget, and checks
  the finite residual and determinant-stability bounds.
- `calculation-checks/bpst_instanton_normalization_checks.py` remains the
  larger companion for the full BPST normalization, determinant, hard-window,
  tail-subtraction, Wilsonian, dilute-gas, and thermal instanton machinery.

## Audit Notes

- 2026-06-06 issue #597 dedicated-chapter start: added the compiled chapter
  `chapter20d_instantons_and_physical_amplitudes.tex` after Ch20.  This is an
  architecture and physical-amplitude pass, not a moduli-space expansion.
- The frontmatter source map was updated so later listed chapter numbers shift
  after the new compiled chapter.
- No directives, GitHub issue text, or process-monitoring language was inserted
  into monograph TeX.
- 2026-06-06 hard four-fermion benchmark pass: lifted the hard-source
  amplitude gate ledger, `Q^(-35/3)` scale law, slow `R^(-1/3)` tail, and
  same-theory ratio bound into the chapter so the reader sees a concrete
  `t Hooft-style amplitude mechanism rather than only the abstract channel
  package.
- 2026-06-06 one-loop density-gate pass: inserted the determinant/RG
  checkpoint before the channel definition, so the dedicated chapter now
  explains why the density contains fluctuation data and why the hard
  four-source channel still needs zero-mode/source powers, endpoint windows,
  and scheme transport before the amplitude is defined.
- 2026-06-06 individual-slot form-factor pass: expanded the hard benchmark by
  deriving the BPST zero-mode slot tail in the physical-amplitude chapter and
  pairing it with a focused companion check.  This is amplitude/source
  machinery, not a moduli-space refinement.
- 2026-06-06 normal-fluctuation source quotient pass: added the finite Gaussian
  source-fluctuation quotient to the physical-amplitude chapter, with companion
  checks rejecting replacement by a vacuum determinant constant.  This targets
  the fluctuation/source side of the instanton amplitude.
- 2026-06-06 hard amplitude assembly pass: added the assembled hard-channel
  formula and absolute error ledger, so the chapter now recombines the
  determinant, zero-mode/source, nonzero-mode source quotient, and physical
  projection data before quoting the hard coefficient.
- 2026-06-06 observable-handoff pass: added a physics bridge from the assembled
  instanton amplitude to QCD observables, explicitly separating hard source
  coefficients, theta curvature, \(U(1)_A\)-odd susceptibility kernels, and
  real-time axial relaxation rates.
- 2026-06-06 physical-projection bridge pass: added
  `sec:instanton-source-kernel-physical-projection` after the hard amplitude
  assembly.  The pass promotes the old residual entry "physical projection"
  into an explicit pole/spectral/OPE/inclusive projection bridge with finite
  checks for pole-window extraction, contact-free spectral bins, one-value
  inversion failure, bridge budgets, and colored-kernel LSZ rejection.  This
  targets physical amplitude extraction, not moduli-space structure.
- 2026-06-06 first cluster amplitude pass: added the connected instanton-pair
  correction ledger to the dedicated physical-amplitude chapter.  This is a
  sector-isolation and source-observable improvement, not a moduli-space
  expansion.
- 2026-06-06 hard Wilsonian OPE pass: added
  `sec:instanton-hard-wilsonian-ope-datum`, which turns the hard four-source
  benchmark into a short-distance operator coefficient only after the
  dimensionless size split, boundary flux, long-size remainder, operator
  matching, and physical matrix element are named.  This prevents using the
  hard source coefficient as a direct hadronic amplitude.
