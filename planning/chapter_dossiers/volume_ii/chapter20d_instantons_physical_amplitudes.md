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
- Opening order-of-calculation paragraph: the chapter flow now moves from
  the finite-regulator source functional, through one-loop density and
  determinant normalization, channel/source data, the hard \(SU(3)\),
  \(N_f=2\) benchmark and Wilsonian size split, to normal-fluctuation
  response, cluster corrections, and observable maps.

## Definitions And Results

- `ch:instantons-physical-amplitudes`: dedicated chapter for instantons as
  physical amplitudes.
- `sec:instanton-source-functional-route`: front-loaded finite-regulator
  source-functional route, making the order from zero-mode source
  differentiation through normal-fluctuation source response, collective
  integration, and final physical projection explicit before the density or
  hard benchmark is interpreted.
- `eq:instanton-source-functional-route`: retained one-instanton source
  functional with collective density, zero-mode-deleted determinant
  normalization, size-window factor, zero-mode Grassmann determinant,
  normal-fluctuation source insertion, and non-Gaussian fluctuation remainder
  in one formula.
- `eq:instanton-source-functional-observable-extraction`: physical observable
  extraction by applying a declared source differential and projection to the
  finite source functional, with regulator, continuation, sector, endpoint,
  and matching residuals kept outside the source functional itself.
- `ca:instanton-source-functional-route`: route-to-amplitude block rejecting
  the three main shortcut reorderings: source differentiation replaced by mass
  saturation, determinant normalization substituted for source response, and
  a raw Euclidean source kernel read as a physical observable before
  projection.
- `sec:instanton-density-gate`: one-loop density normalization separating the
  collective-coordinate Jacobian, bosonic zero-mode normalization, running
  BPST action, zero-mode-deleted fluctuation determinant logarithm, and finite
  scheme constant before the density is inserted into a physical channel.
- `ca:instanton-one-loop-density-gate-channel`: checks that the universal
  density power is fixed by the one-loop RG cancellation, while the channel
  size power also depends on zero-mode/source data such as mass saturation or
  hard external source differentiation.
- `ca:instanton-collective-jacobian-gauge-slice`: gauge-sliced
  collective-coordinate Jacobian block; the bosonic measure is the square root
  of the horizontal zero-mode Gram determinant, divided by the residual
  stabilizer quotient, with a finite metric-stability bound before the source
  channel is interpreted.
- `ca:instanton-proper-time-determinant-channel`: derives the
  zero-mode-deleted proper-time determinant logarithm inside a source channel,
  with boson inverse-square-root, ghost determinant, Dirac fermion determinant,
  and local
  counterterm weights, then turns the determinant remainder into an absolute
  source-window bound.
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
- `prop:instanton-chirality-source-selection-gate`: finite zero-mode Berezin
  selection rule for the hard instanton vertex; in the \(Q=1\) convention the
  massless hard coefficient is supported on the anomalous
  \((n_L,n_R,\bar n_L,\bar n_R)=(N_f,0,0,N_f)\) source coordinate, with the
  \(Q=-1\) sector carrying the conjugate chirality coordinate.
- `prop:instanton-axial-ward-source-transport`: finite source-determinant
  Ward-transport statement for the \(Q=1\), \(N_f=2\) zero-mode block.  The
  source matrix \(C_{\rm zm}=S+iP\) varies as
  `V_A C_zm = -2 i C_zm`, the instanton phase varies by
  `delta theta = 4 alpha`, and
  `(4 partial_theta + V_A^src)(e^{i theta} det C_zm)=0`.  This connects the
  chirality-selection rule to the parent Ch20 anomalous source-Ward ledger
  before the hard benchmark is projected to a physical observable.
- `sec:instanton-hard-four-fermion-benchmark`: hard two-flavor four-source
  benchmark, organized as center, Haar, zero-mode-rank, amputation,
  size-window, and physical-projection data.
- `prop:instanton-hard-haar-orientation-tensor`: derives the charge-one
  color-orientation average as the antisymmetric two-frame projector
  `2/(N_c(N_c-1)) (delta_ac delta_bd - delta_ad delta_bc)` and turns the
  hard-channel Haar factor into a source projection rather than an
  orientation-volume constant.
- `prop:instanton-hard-individual-zero-mode-slot`: derives the individual
  singular-gauge BPST zero-mode slot profile used by the hard four-source
  amplitude, including `F_zm(0)=1`, the `6 (rho |p|)^(-3)` tail, and the
  four-slot product `6^4 prod c_l^(-3) s^(-12)`.
- `ca:instanton-thooft-four-point-amputated-assembly`: packages the
  't Hooft-style hard four-source calculation as an amputated Green-function
  assembly: density, Haar tensor, chiral source determinants, individual
  zero-mode slots, nonzero-mode source quotient, external-leg amputation,
  physical projection, endpoint tail, and sector isolation all sit in one
  residual budget.
- `prop:su3-nf2-hard-source-power-slow-tail`: derives the SU(3), `N_f=2`
  hard four-source powers `rho^(32/3) d rho`,
  `(8 pi^2/g_ht^2(Q))^6 Lambda_ht^(29/3) Q^(-35/3)`, and the slow
  `R^(-1/3)` large-size tail.
- `ca:instanton-hard-window-tail-subtraction`: evaluates the hard size window
  as a finite core plus leading `R^(-1/3)` and subleading `R^(-7/3)` analytic
  endpoint tails from the two-term zero-mode-slot expansion.
- `ca:instanton-hard-benchmark-gate-ledger`: same-theory hard-scale ratio and
  residual multiplier bound after the channel data and source-window shape have
  been transported.
- `sec:instanton-hard-wilsonian-ope-datum`: Wilsonian OPE-input
  interpretation of the hard four-source kernel as a short-distance local
  four-fermion coefficient,
  with the dimensionless size split \(R\), boundary-flux flow, operator
  matching, physical matrix element, and long-size remainder kept separate.
- `ca:instanton-wilsonian-matching-covariance`: finite Wilsonian matching
  covariance for the instanton vertex.  The short instanton coefficient is a
  row vector in a renormalized operator basis, while the physical contribution
  is the paired coefficient/matrix-element coordinate plus the long-size shell
  and bridge residuals.  The block shows finite scheme covariance and the
  cancellation between boundary flux, anomalous-dimension transport, and the
  long-size remainder.
- `sec:instanton-normal-fluctuation-source-data`: local amplitude-facing block
  separating the determinant normalization of nonzero modes from the
  fluctuation average of the selected source insertion.
- `ca:instanton-nonzero-mode-source-quotient`: finite Gaussian source quotient
  and covariance identity, including the quadratic source trace correction
  `1/2 Tr(QC)` and the absolute bound
  `epsilon_U + M_U M_V / d_0`.
- `ca:instanton-first-source-cumulant-normal-modes`: first explicit
  normal-mode source cumulant; a linear source deformation has zero Gaussian
  mean but contributes through Wick covariance with the cubic fluctuation
  action, so it is not a source-independent determinant constant.
- `sec:instanton-hard-amplitude-assembly`: recombines the hard source kernel,
  finite determinant normalization, nonzero-mode source quotient,
  zero-mode/source stability, and physical projection into one regulated
  amplitude coordinate.
- `ca:instanton-hard-amplitude-assembly-ledger`: assembled hard-amplitude
  absolute error bound, with noncancellation margin required before relative
  scale-law claims are allowed.
- `ca:instanton-hard-reference-channel-calibration`: reference-channel
  determinant calibration for the assembled hard amplitude; one physical
  reference channel fixes only the same-frame finite determinant constant, with
  reference residuals amplified by the target/reference integral ratio.
- `sec:instanton-source-kernel-physical-projection`: projection bridge from an
  assembled Euclidean instanton source kernel to a physical pole, spectral,
  OPE, or inclusive observable coordinate.
- `ca:instanton-source-kernel-physical-projection`: physical bridge residual
  bound separating regulator transport, analytic continuation, pole/bin
  isolation, infrared completion, unitarity-cut normalization, matching, and
  endpoint control.
- `ca:instanton-pole-normalized-four-source-extraction`: mixed-source pole
  extraction block showing that a Euclidean four-source instanton window
  becomes a matrix element only after full overlap-matrix amputation and a
  pole-leakage residual bound.
- `ca:instanton-inclusive-cut-quadratic-projection`: inclusive-cut block
  showing that a pole- or OPE-projected one-instanton amplitude feeds a
  positive cut/rate only through conjugate-sector pairing, the physical
  measurement matrix, source amputation, and quadratic residual propagation.
- `sec:instanton-first-cluster-amplitude-correction`: source-amplitude bridge
  from the assembled one-instanton coefficient to the first connected
  instanton-pair correction.
- `ca:instanton-first-cluster-amplitude-correction`: first cluster correction
  for a source amplitude, including disconnected one-body subtraction,
  neutral-pair source visibility, same-charge theta harmonic data, pair-kernel
  residual control, and the sector-isolation consequence.
- `ca:instanton-neutral-pair-valley-prescription`: neutral
  instanton--anti-instanton valley prescription block; it separates the
  attractive quasi-zero-mode lateral ambiguity from an ordinary positive
  molecule integral and cancels it against the perturbative lateral ambiguity
  only in the same source/projection coordinate.
- `sec:instanton-observable-handoffs`: physical observable-map block distinguishing a
  hard source coefficient, theta curvature, \(U(1)_A\)-odd susceptibility
  kernel, and real-time axial relaxation rate.
- `ca:instanton-observable-handoff-ledger`: finite-regulator observable-map
  statement: the one-instanton amplitude density must be projected to a named
  observable before its physical meaning is fixed.
- `ca:finite-cell-instanton-channel-control`: finite retained-cell model
  proving the absolute residual bound and the two-by-two determinant stability
  estimate.

## Claim Ledger

- The new chapter advances issue #597 at the architecture level: it starts a
  dedicated instanton chapter and makes the physical channel, rather than the
  moduli space, the organizing object.
- The source-functional route block repairs the chapter-level flow after many
  local insertions.  It tells the reader what is computed first at finite
  regulator and why the later density, zero-mode, normal-fluctuation,
  size-window, and projection blocks are parts of one amplitude extraction
  rather than adjacent facts about the BPST saddle.
- The first substantive result is not an ADHM refinement.  It proves that the
  same collective-coordinate measure and nonzero-mode determinant convention
  can give different physical amplitudes once zero-mode source rank and
  projection are changed.
- The density-normalization block prevents the hard benchmark from treating
  `rho^(b0-5)` as a moduli-space fact.  It records the fluctuation/RG origin
  of `(mu rho)^b0`, the finite determinant constant, and the added
  zero-mode/source power `beta_C` that turns a density into a channel
  integrand.
- The collective-coordinate Jacobian block opens the path-integral measure
  step behind the BPST density.  It derives the bosonic measure from
  horizontal zero-mode representatives and the square root of their Gram
  determinant, keeps the residual stabilizer quotient visible, and gives a
  perturbative stability bound.  This blocks dimension-only zero-mode
  counting, raw gauge-vertical tangents, and using `det G` where the
  functional measure supplies `sqrt(det G)`.
- The proper-time determinant-channel block opens the compressed fluctuation
  step behind that density: the zero-mode-deleted boson, ghost, fermion, and
  counterterm logarithms must assemble to `b0`, and the leftover determinant
  error is a pointwise multiplicative source-window residual.  A signed
  heat-kernel cancellation or a nonzero determinant density cannot replace a
  vanished zero-mode source determinant or physical projection.
- The two-flavor determinant calculation is the local algebra behind the
  distinction between a mass-saturated vacuum activity and a differentiated
  four-source 't Hooft amplitude.
- The chirality-source selection rule turns that determinant into an anomalous
  amplitude selection rule.  A nonzero determinant in the conjugate source
  block, a chirality-balanced four-source selection, or a mass-assisted
  coordinate cannot be relabelled as the \(Q=1\) hard 't Hooft vertex before
  the size integral.  This keeps axial charge flow, source differentiation,
  and topological sector in the same finite zero-mode calculation.
- The axial Ward transport proposition connects the zero-mode selection to the
  anomaly/source-Ward machinery of Ch20.  The \(Q=1\) phase and the source
  determinant are one Ward-transported coordinate; rotating only the
  determinant, shifting only theta, or changing the source frame without
  transporting the physical projection changes the amplitude claim.
- The hard benchmark section moves beyond the local determinant to a physical
  four-source channel: center conservation, shared Haar projection, two
  zero-mode source determinants, amputation, hard form factors, and endpoint
  tails must all be part of the coefficient before a scale law is quoted.
- The hard-channel Haar tensor exposes the color-orientation part of the
  amplitude.  A symmetric color-pair source is killed by the antisymmetric
  two-frame projector even when the density, determinant, zero-mode flavor
  determinants, and size window are all nonzero.
- The individual-slot form-factor block opens one of the hard channel's
  previously compressed inputs: the endpoint tail comes from the cancellation
  of the apparent `t^(-1)` terms in the BPST zero-mode Bessel products, giving
  the differentiated-slot power tail rather than the fused-density exponential
  source class.
- The normal-fluctuation source quotient opens the next compressed input:
  even after the Gaussian determinant is normalized, the selected hard source
  has a mean and a covariance with nonzero-mode interactions.  A vacuum
  determinant constant alone cannot control a four-source amplitude.
- The first source-cumulant block makes that statement constructive: the
  linear normal-mode deformation of the source has zero Gaussian mean, but the
  cubic fluctuation action produces a Wick-paired contribution
  `-1/2 l_i T_abc C_ia C_bc`.  This is exactly the kind of fluctuation
  response that is invisible in moduli-space or determinant-only
  presentations.
- The assembled hard-channel formula prevents the chapter from becoming a list
  of adjacent checkpoints.  It places the determinant scheme constant, hard
  zero-mode slots, nonzero-mode source quotient, source-frame stability, and
  projection mismatch in a single amplitude formula, with absolute
  signed-window control and an explicit noncancellation hypothesis for
  relative statements.
- The reference-channel calibration block gives the finite determinant
  constant an amplitude-facing use without overclaiming it.  A reference
  physical channel fixes one same-frame normalization; source-fluctuation
  quotients, zero-mode rank, endpoint tails, and pole/spectral/OPE projection
  data remain either inside the transported \(B_\alpha\) integral or in the
  residual.
- The physical projection bridge opens the last compressed step between a
  Euclidean instanton source coefficient and a physical claim.  It separates
  stable-particle pole extraction, spectral-bin/discontinuity functionals,
  OPE matching, colored auxiliary kernels, and bridge residuals, so a
  Euclidean source number cannot be relabelled as a scattering amplitude or
  spectral observable.
- The pole-normalized four-source extraction block makes the stable-particle
  projection more concrete: in a mixed source basis the physical instanton
  matrix element is \(Z_f^{-1}\widetilde C^I(Z_i^\dagger)^{-1}\), not a raw
  Euclidean kernel or a diagonal residue division.  Excited-state and
  continuum leakage are amplified by the inverse overlap matrices, so pole
  isolation is a physical part of the amplitude calculation.
- The inclusive-cut quadratic-projection block prevents the \(Q=1\)
  source-amplitude coefficient from being overread as a positive rate.  A
  physical cut uses the conjugate sector, the final-state measurement matrix,
  and the same amputated physical amplitude basis; signed linear sums,
  unamputated source vectors, and locally inclusive replacement of the
  declared measurement are rejected.
- The observable-map block connects the dedicated instanton-amplitude
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
- The neutral-pair valley prescription block opens the attractive
  instanton--anti-instanton quasi-zero-mode direction as a lateral
  prescription problem rather than a positive molecule count.  The ambiguous
  valley residue must carry zero-mode overlap, nonzero-mode determinant,
  source insertion, endpoint window, and physical projection data before it can
  cancel the perturbative lateral ambiguity.  This prevents transporting a
  vacuum-residue cancellation into a hard, pole, spectral, or inclusive
  amplitude without the source/projection maps.
- The `Q^(-35/3)` hard-scale behavior is the power-counting part tied to
  `b0=29/3` and four individual hard zero-mode form factors; the full
  one-loop hard coefficient also retains the running collective-coordinate
  factor `(8 pi^2/g_ht^2(Q))^6`.  The large-size endpoint is convergent but
  slow, with a retained-tail majorant of order `R^(-1/3)`, so a
  window/stability budget is load-bearing.
- The Wilsonian OPE bridge makes the hard benchmark usable as a local QFT
  input only after a size split.  The short coefficient has a nonzero boundary
  flow, the long-size tail cancels that flow in the completed split, and the
  physical observable still needs the renormalized four-fermion matrix element
  plus matching, infrared, projection, and sector residuals.
- The Wilsonian matching covariance block keeps the instanton vertex from
  being overread as a scheme-independent number.  Coefficients, operator
  matrix elements, anomalous-dimension transport, boundary flux, and long-size
  shell form one finite matching coordinate; changing only the coefficient or
  moving the size boundary without the long shell changes the physical claim.
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
- The check verifies the source-functional route order by separating source
  differentiation, normal-fluctuation response, and physical projection before
  any hard benchmark is interpreted; it rejects the corresponding mass
  saturation, determinant-only source-response, and raw Euclidean-kernel
  shortcuts.  It also verifies the exact `det(M+B)` polynomial, rejects the
  wrong off-diagonal sign, separates mass-saturated and four-source coordinates,
  verifies the one-loop density RG cancellation and the distinction between
  density-only, mass-saturated, and hard four-source size powers,
  verifies the gauge-sliced zero-mode Gram determinant, square-root collective
  Jacobian, stabilizer quotient, action-normalization scaling, raw-gauge
  negative control, and finite Gram-perturbation stability bound,
  verifies the proper-time determinant-log channel window, including the
  boson/ghost/fermion weights, counterterm conversion to `b0`, absolute
  determinant residual bound, and rank-killed source negative control,
  verifies the hard-channel color-orientation Haar tensor and rejects
  symmetric color-pair sources or orientation-volume constants as substitutes
  for the antisymmetric two-frame source projection,
  derives the individual zero-mode slot tail coefficient from the Bessel
  product cancellation and rejects fused-density endpoint substitution or
  hidden unamputated residues,
  verifies the amputated 't Hooft four-point assembly and rejects density-only
  shortcuts, rank-lost chiral source determinants, symmetric Haar sources,
  omitted nonzero-mode source quotients, unamputated source overlaps, and
  underbudgeted physical-projection residuals,
  verifies the finite Gaussian nonzero-mode source quotient covariance
  identity, the quadratic trace correction, absolute window propagation, and
  rank-loss rejection,
  verifies the first Wick-paired source cumulant from a linear normal-mode
  source deformation and cubic fluctuation action, rejecting zero-cubic,
  determinant-only, and signed-remainder shortcuts,
  verifies the assembled hard-amplitude product bound and rejects
  determinant-only assembly or signed-window relative control without a
  noncancellation margin,
  verifies hard reference-channel determinant calibration, including residual
  amplification by the target/reference ratio and negative controls for
  omitted source-fluctuation transport, omitted physical-projection transport,
  rank-lost references, and nearly canceled references,
  verifies the observable-map distinction between hard source coefficients,
  dilute theta curvature, \(U(1)_A\)-odd zero-mode-zone kernels, real-time
  axial rates, and Witten--Veneziano curvature comparison budgets,
  verifies the physical projection bridge from Euclidean source kernels to
  pole-window and spectral-bin coordinates, including contact-polynomial
  separation, one-Euclidean-value inversion failure, bridge residual control,
  and colored-kernel LSZ rejection,
  verifies the mixed-source pole amputation formula and rejects raw-kernel
  and diagonal-overlap shortcuts, rank-lost source bases, and determinant
  constants used to absorb pole leakage,
  verifies the inclusive-cut quadratic projection from physical instanton
  amplitude vectors and rejects linear signed amplitude sums, unamputated
  source vectors, measurement omission, and unbudgeted quadratic residual
  propagation,
  verifies the first connected instanton-pair source correction, including
  disconnected subtraction, ordered-pair/Mayer symmetry-factor counting,
  neutral-pair source visibility despite zero theta curvature, same-charge
  second-harmonic data, zero-mode overlap survival, and pair residual control,
  verifies the neutral-pair valley prescription with exact rational
  `(PV, ambiguity)` lateral coordinates, a source-projected residue, its
  perturbative lateral partner, same-coordinate ambiguity cancellation,
  residual-bound propagation, and negative controls for pair-only,
  principal-value-only, wrong-frame, and source-projection-omitted
  cancellations,
  verifies the chirality-source selection rule with exact two-by-two
  determinant blocks, axial-weight counts, wrong-chirality and
  chirality-balanced negative controls, sector-mixing rejection, and a
  mass-assisted coordinate check,
  verifies axial Ward transport of the \(Q=1\) theta phase with the complex
  two-flavor source determinant and rejects source-only, theta-only, and
  wrong-sign theta rotations,
  builds moduli-equivalent finite cell channels with different or vanishing
  amplitudes, constructs a same-Euclidean-sum/different-projection ambiguity,
  checks the SU(3), `N_f=2` hard four-source scale and tail powers, verifies
  the two-term hard-window endpoint subtraction, validates the hard channel
  comparison and same-theory ratio residual bound, verifies the
  hard-kernel Wilsonian OPE boundary flow, finite matching scheme covariance,
  anomalous-dimension/boundary-flux cancellation, and long-size tail budget,
  and checks the finite residual and determinant-stability bounds.
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
  amplitude comparison, the `(8 pi^2/g_ht^2(Q))^6 Lambda_ht^(29/3)
  Q^(-35/3)` one-loop hard scaling, slow `R^(-1/3)` tail, and same-theory
  ratio bound into the chapter so the reader sees a concrete `t Hooft-style
  amplitude mechanism rather than only the abstract channel package.
- 2026-06-06 one-loop density-normalization pass: inserted the determinant/RG
  checkpoint before the channel definition, so the dedicated chapter now
  explains why the density contains fluctuation data and why the hard
  four-source channel still needs zero-mode/source powers, endpoint windows,
  and scheme transport before the amplitude is defined.
- 2026-06-06 proper-time determinant-channel pass: inserted the
  zero-mode-deleted determinant-log calculation between density normalization
  and channel packaging, with the companion exact check guarding the
  boson/ghost/Dirac-fermion determinant signs, counterterm conversion,
  absolute residual window, and the failure of determinant density alone to
  produce an amplitude.
- 2026-06-06 running collective-factor repair: restored the
  `(8 pi^2/g_ht^2(Q))^6` bosonic zero-mode normalization in the Ch20D hard
  coefficient, OPE split, assembled amplitude, same-theory ratio, and
  logarithmic slope statement.  The companion check now rejects coefficients
  or ratios that retain only the pure `Q^(-35/3)` power.
- 2026-06-06 cross-chapter normalization and pair-counting repair: propagated
  the same running collective factor into the parent Ch20 hard-scale benchmark,
  added a cross-file regression comparing the duplicate benchmark equations,
  and made the first cluster correction use an ordered two-body measure with a
  displayed Mayer \(1/2\).  The companion check now rejects both the old
  pure-power-only duplicate and an ordered pair sum that omits the symmetry
  factor.
- 2026-06-06 hard color-orientation projection pass: added
  `prop:instanton-hard-haar-orientation-tensor` before the individual
  zero-mode-slot calculation.  The pass derives the two-frame Haar projector
  in the embedded color plane and makes the antisymmetric color source
  projection part of the hard amplitude.  The companion finite check rejects
  replacing this tensor by an orientation-volume constant and verifies that a
  symmetric color-pair source kills the hard benchmark even with nonzero
  determinant, flavor-zero-mode, and size-window factors.
- 2026-06-06 individual-slot form-factor pass: expanded the hard benchmark by
  deriving the BPST zero-mode slot tail in the physical-amplitude chapter and
  pairing it with a focused companion check.  This is amplitude/source
  machinery, not a moduli-space refinement.
- 2026-06-06 normal-fluctuation source quotient pass: added the finite Gaussian
  source-fluctuation quotient to the physical-amplitude chapter, with companion
  checks rejecting replacement by a vacuum determinant constant.  This targets
  the fluctuation/source side of the instanton amplitude.
- 2026-06-06 hard amplitude assembly pass: added the assembled hard-channel
  formula and absolute error bound, so the chapter now recombines the
  determinant, zero-mode/source, nonzero-mode source quotient, and physical
  projection data before quoting the hard coefficient.
- 2026-06-06 hard reference-channel calibration pass: added a physical
  amplitude calibration block after the assembled hard-channel bound.  The new
  block uses one reference channel only to fix the same-frame determinant
  constant and keeps source fluctuation, zero-mode rank, endpoint, and physical
  projection data as transported integral data or residuals.  The companion
  check rejects calibrations that try to absorb those channel-dependent
  factors.
- 2026-06-06 observable-map pass: added a physics bridge from the assembled
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
  correction to the dedicated physical-amplitude chapter.  This is a
  sector-isolation and source-observable improvement, not a moduli-space
  expansion.
- 2026-06-06 neutral-pair valley prescription pass: added
  `ca:instanton-neutral-pair-valley-prescription` after the connected
  first-cluster block.  The pass treats the attractive neutral pair direction
  as a same-source-coordinate lateral-prescription issue and rejects
  pair-only, principal-value-only, wrong-frame, and source-projection-omitted
  ambiguity cancellations.
- 2026-06-06 chirality-source selection pass: added
  `prop:instanton-chirality-source-selection-gate` after the two-flavor
  mass/source determinant coordinate.  The pass makes the hard \(Q=1\)
  't Hooft vertex an anomalous zero-mode source-selection statement, rejecting
  wrong-chirality determinants, chirality-balanced four-source selections,
  sector-mixed unlabeled determinants, and mass-assisted coordinates as
  substitutes for the massless hard vertex.
- 2026-06-06 axial Ward transport pass: added
  `prop:instanton-axial-ward-source-transport` after the chirality-source
  selection proposition.  The pass ties the zero-mode source determinant to
  the parent anomalous source-Ward convention: the source determinant and the
  instanton theta phase are transported together before a hard, pole, OPE, or
  susceptibility observable is projected.  The companion check rejects
  source-only, theta-only, and wrong-sign theta transports.
- 2026-06-06 hard Wilsonian OPE pass: added
  `sec:instanton-hard-wilsonian-ope-datum`, which turns the hard four-source
  benchmark into a short-distance operator coefficient only after the
  dimensionless size split, boundary flux, long-size remainder, operator
  matching, and physical matrix element are named.  This prevents using the
  hard source coefficient as a direct hadronic amplitude.
- 2026-06-06 Wilsonian matching covariance pass: added
  `ca:instanton-wilsonian-matching-covariance` inside the hard Wilsonian OPE
  section.  The pass makes the instanton vertex a renormalized
  coefficient/operator/matrix-element coordinate: finite operator-basis
  mixing transforms \(C^{<}\) and \(\langle O\rangle\) inversely, while the
  moving size boundary cancels only after the long-size shell and
  anomalous-dimension transport are included.  The companion check rejects
  coefficient-only scheme changes and omitted long-shell residuals.  This is a
  physical-amplitude matching pass, not a moduli-space or ADHM expansion.
- 2026-06-06 hard-window tail-subtraction pass: added
  `ca:instanton-hard-window-tail-subtraction` after the hard-source slow-tail
  proposition.  The pass opens the endpoint control inside the hard
  four-source amplitude by deriving the two-term differentiated-slot tail,
  the induced integrand coefficients \(A_0,A_1\), and the core-plus-tail
  evaluation \(H(R)+3A_0R^{-1/3}+(3/7)A_1R^{-7/3}+E_{\rm tail}\).  The
  companion check verifies the exact rational tail coefficients and rejects
  leading-tail-only and fused-density endpoint shortcuts.
- 2026-06-06 issue #597 amputated four-point assembly pass: added
  `ca:instanton-thooft-four-point-amputated-assembly` inside the hard
  benchmark.  This pass explicitly treats the original-style hard instanton
  calculation as an amputated Green-function assembly, with the density,
  color-orientation tensor, chiral source determinants, individual zero-mode
  slots, nonzero-mode source quotient, amputation, projection, endpoint, and
  sector terms normalized in one regulator and one residual budget.  It is a
  physics-amplitude consolidation, not an ADHM or moduli-space expansion.
- 2026-06-06 issue #844 instanton amplitude surface pass: re-audited the
  dedicated physical-amplitude chapter for architecture vocabulary.  The
  reader-facing text now presents density normalization, channel data, hard
  channel comparison, hard amplitude assembly, and observable maps
  rather than gate/ledger language.  Cross-reference labels were kept stable;
  the physics equations and companion checks are unchanged in substance.  This
  is a coherence and physical-output pass, not another instanton cell.
- 2026-06-06 issue #597 chapter-flow pass: added a front-loaded
  order-of-calculation paragraph and replaced the remaining reader-facing
  observable-handoff wording in the monograph with observable-map language.
  The edit keeps the hard instanton chapter oriented toward the physical
  calculation from fluctuation density through source channels to measured
  QFT observables, without adding another local instanton cell.
- 2026-06-06 issue #597 coherence follow-up: re-audited the heavily edited
  chapter surface after the later source, fluctuation, valley, and chirality
  insertions.  The visible theorem/control titles now say source-functional
  route to a physical amplitude, zero-mode Jacobian from a gauge slice, and
  chirality-source selection rather than process-facing gate/discipline
  language.  Stable labels were kept unchanged; the equations and evidence
  checks are unchanged in substance.
- 2026-06-06 source-functional route pass: inserted
  `sec:instanton-source-functional-route` at the chapter entrance.  The pass
  makes the finite-regulator source functional the first object and derives the
  observable only after source differentiation, source-dependent normal
  fluctuation averaging, collective integration, and physical projection.  The
  companion check rejects the corresponding shortcut routes in finite
  arithmetic.
- 2026-06-06 mixed-source pole extraction pass: added
  `ca:instanton-pole-normalized-four-source-extraction` inside the physical
  projection bridge.  The pass turns the stable-particle projection into an
  explicit overlap-matrix amputation problem, so the hard instanton
  four-source window becomes a physical matrix element only after source
  mixing, pole residues, and excited-state leakage are controlled.
- 2026-06-06 issue #597 chapter-order re-audit: corrected the opening
  calculation-order paragraph so the source functional, not the one-loop
  density, is the first object.  The visible section/control titles now say
  Wilsonian OPE input and hard amplitude assembly control while stable labels
  are preserved.  No formula, physics claim, or calculation companion changed;
  this is a coherence repair enforcing the amplitude-first architecture after
  the many later source, fluctuation, projection, and cluster insertions.
