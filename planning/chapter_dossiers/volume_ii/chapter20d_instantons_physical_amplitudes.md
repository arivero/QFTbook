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
- `prop:su3-nf2-hard-source-power-slow-tail`: derives the SU(3), `N_f=2`
  hard four-source powers `rho^(32/3) d rho`,
  `Lambda_ht^(29/3) Q^(-35/3)`, and the slow `R^(-1/3)` large-size tail.
- `ca:instanton-hard-benchmark-gate-ledger`: same-theory hard-scale ratio and
  residual multiplier bound after the gate data and source-window shape have
  been transported.
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
- The `Q^(-35/3)` hard-scale behavior is tied to `b0=29/3` and four individual
  hard zero-mode form factors.  The large-size endpoint is convergent but slow,
  with a retained-tail majorant of order `R^(-1/3)`, so a window/stability
  budget is load-bearing.
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
  builds moduli-equivalent finite cell channels with different or vanishing
  amplitudes, constructs a same-Euclidean-sum/different-projection ambiguity,
  checks the SU(3), `N_f=2` hard four-source scale and tail powers, validates
  the hard gate ledger and same-theory ratio residual bound, and checks the
  finite residual and determinant-stability bounds.
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
