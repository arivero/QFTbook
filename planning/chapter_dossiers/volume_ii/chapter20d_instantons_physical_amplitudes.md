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
- The two-flavor determinant calculation is the local algebra behind the
  distinction between a mass-saturated vacuum activity and a differentiated
  four-source 't Hooft amplitude.
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
  builds moduli-equivalent finite cell channels with different or vanishing
  amplitudes, constructs a same-Euclidean-sum/different-projection ambiguity,
  and checks the finite residual and determinant-stability bounds.

## Audit Notes

- 2026-06-06 issue #597 dedicated-chapter start: added the compiled chapter
  `chapter20d_instantons_and_physical_amplitudes.tex` after Ch20.  This is an
  architecture and physical-amplitude pass, not a moduli-space expansion.
- The frontmatter source map was updated so later listed chapter numbers shift
  after the new compiled chapter.
- No directives, GitHub issue text, or process-monitoring language was inserted
  into monograph TeX.
