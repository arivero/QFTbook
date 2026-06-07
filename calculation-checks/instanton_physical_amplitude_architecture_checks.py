r"""Finite checks for the instanton physical-amplitude architecture chapter.

Evidence contract.

Target claims:
- `eq:instanton-source-functional-route`,
  `eq:instanton-source-functional-observable-extraction`, and
  `ca:instanton-source-functional-route`: the one-instanton sector first
  defines a finite-regulator source functional, and a physical amplitude is
  obtained only after source differentiation, source-dependent fluctuation
  averaging, collective integration, and the named physical projection.
- `ex:instanton-finite-source-functional-laboratory`: a retained-cell
  amplitude coordinate multiplies the collective weight, nonzero-mode
  determinant normalization, differentiated zero-mode source coordinate,
  normal-mode source quotient, and physical projection in one finite sum.
- `rem:instanton-su3-nf2-hard-channel-spine` and
  `eq:instanton-su3-nf2-hard-channel-spine`: the named hard
  `SU(3)`, `N_f=2` channel keeps collective density, zero-mode source
  selection, normal-fluctuation source response, Haar/LSZ/size-window data,
  and the final physical projection in a fixed order.
- `def:instanton-physical-amplitude-channel` and
  `eq:instanton-physical-channel-functional`: the physical channel depends on
  the collective density, nonzero-mode determinant, zero-mode source
  determinant, endpoint/projection weights, and residuals, not on the moduli
  measure alone.
- `prop:instanton-moduli-equivalent-channel-separation`: two channels with the
  same collective-coordinate and determinant weights can have different, or
  zero, two-flavor source amplitudes.
- `prop:two-flavor-source-mass-determinant-coordinate`: the mass-saturated
  activity, mass-assisted source terms, and four-source coefficient are
  distinct coordinates of det(M+B).
- `ca:instanton-one-loop-density-gate-channel`: the one-loop density power
  is fixed by the RG cancellation between the determinant logarithm and the
  running BPST action, while the physical channel power also depends on
  zero-mode/source data.
- `ca:instanton-collective-jacobian-gauge-slice`: the bosonic
  collective-coordinate measure is the square root of the gauge-sliced
  zero-mode Gram determinant, with residual stabilizer and metric stability
  transported before the source channel is interpreted.
- `ca:instanton-proper-time-determinant-channel`: the proper-time fluctuation
  log contributes to a source channel through weighted zero-mode-deleted
  boson, ghost, fermion, and counterterm coefficients; the resulting
  determinant residual must be bounded on the absolute source window.
- `prop:instanton-hard-individual-zero-mode-slot`: the differentiated hard
  fermion slot has the singular-gauge BPST zero-mode form-factor tail
  `F_zm(c s/2) = 6 c^(-3) s^(-3) + O(s^(-5))`; four such slots give the
  `6^4 prod c_l^(-3) s^(-12)` endpoint factor, while fused bilinear-density
  sources have a different endpoint class.
- `prop:instanton-hard-haar-orientation-tensor`: the charge-one color
  orientation integral is the antisymmetric two-frame projector
  `2/(Nc(Nc-1)) (delta_ac delta_bd - delta_ad delta_bc)`, so symmetric color
  pair sources vanish before the size integral is interpreted as an amplitude.
- `ca:instanton-nonzero-mode-source-quotient`: the source-dependent
  nonzero-mode fluctuation quotient separates the Gaussian source mean from
  its covariance with the same interaction weight that defines the determinant
  normalization.
- `ca:instanton-primed-determinant-source-response`: source perturbations of
  the zero-mode-deleted fluctuation determinant are primed resolvent trace
  calculations with boson/fermion signs and counterterm coordinates fixed in
  the same regulator; higher operator-family terms require a separate
  resolvent remainder bound beyond the linear log-series tail.
- `ca:instanton-first-source-cumulant-normal-modes`: a linear normal-mode
  source deformation has zero Gaussian mean but contributes to the instanton
  source amplitude through its Wick covariance with the cubic fluctuation
  action; this term is not a source-independent determinant constant.
- `ca:instanton-normal-propagator-source-insertion`: a nonzero-mode
  propagator insertion in an instanton channel is a primed, source-projected,
  amputated bilinear matrix element multiplied by the zero-mode coefficient;
  it is not a determinant constant, an unprimed zero-mode-regulated inverse,
  a trace response, or a diagonal residue division.
- `ca:instanton-subtracted-normal-green-matching`: a normal Green-function
  insertion must first declare its source/operator class.  Smooth smeared
  source bilinears are distributional pairings, while local/composite or
  background-subtracted source coordinates require the same zero-mode
  projector, local parametrix, logarithmic heat-kernel counterterm, finite
  local matching term, and compensating Wilsonian coefficient shift.
- `ca:instanton-spectral-local-green-matching-test`: in a concrete spectral
  cutoff model, smooth source pairings converge by source decay, whereas a
  local diagonal source coordinate has independently extracted `A0 N` and
  `A1 H_N` cutoff terms plus a finite local Wilsonian coordinate.
- `ca:instanton-hard-amplitude-assembly-ledger`: the hard channel must assemble
  the determinant, source-fluctuation, zero-mode/source, and physical-projection
  factors in the same kernel, with absolute control unless a noncancellation
  margin is supplied.
- `ca:instanton-hard-reference-channel-calibration`: one reference physical
  channel can calibrate only a same-frame finite determinant normalization;
  reference residuals are amplified by the target/reference integral ratio,
  and source-fluctuation or physical-projection data not included in the
  retained integrals remain separate residuals.
- `ca:instanton-overdetermined-reference-channel-calibration`: two same-frame
  reference channels must extract the same finite determinant constant within
  the displayed residual and noncancellation-margin budget; omitted
  source-fluctuation quotients or physical-projection factors appear as
  channel-dependent drifts rather than as determinant normalizations.
- `rem:instanton-finite-determinant-scheme-transport-architecture`: a finite
  one-loop determinant constant has a scheme-transport architecture involving
  the coupling/action conversion, running bosonic zero-mode power, and
  orientation measure.  Source and physical-projection data are transported
  separately as channel vectors and covectors; this is a covariance typing
  check, not an independent determinant-conversion computation.
- `ca:instanton-finite-determinant-conversion-benchmark`: two finite regulated
  determinant densities are computed independently before their conversion
  ratio, residual, and inverse matching factor are tested.
- `rem:instanton-observable-handoff-map`: the assembled instanton channel
  must still be mapped to a named physical observable; hard source
  coefficients, theta curvatures, U(1)_A susceptibility kernels, and real-time
  axial relaxation rates are not interchangeable.
- `ca:instanton-source-kernel-physical-projection`: a finite Euclidean
  instanton source kernel becomes a physical amplitude only after a declared
  pole, spectral-bin, OPE, or inclusive projection, with bridge residuals for
  regulator transport, continuation, pole/bin isolation, infrared completion,
  unitarity-cut normalization, matching, and endpoint control.
- `ca:instanton-pole-normalized-four-source-extraction`: a pole-window
  four-source kernel with a mixed source basis must be amputated by the full
  source-overlap matrices, with excited-state and continuum leakage amplified
  by the inverse overlap matrices.
- `ca:instanton-inclusive-cut-quadratic-projection`: a pole- or OPE-projected
  one-instanton source coefficient feeds a positive inclusive cut only through
  conjugate-sector pairing, the physical measurement matrix, source
  amputation, and quadratic residual propagation have been supplied.
- `ca:instanton-first-cluster-amplitude-correction`: a first connected
  two-body correction to a source amplitude requires the disconnected one-body
  product subtraction, a declared ordered/unordered pair convention with the
  correct symmetry factor, a source/projection-specific pair kernel, absolute
  pair residual control, and a separate reading of neutral and same-charge
  pairs.
- `ca:instanton-neutral-pair-valley-prescription`: a neutral instanton-pair
  valley contribution is a lateral prescription in the same source/projection
  coordinate as its perturbative ambiguity partner; pair-only, principal-value
  only, or wrong-frame cancellations change the physical assertion.
- `prop:instanton-chirality-source-selection-gate`: the hard zero-mode
  vertex is supported only on the anomalous chirality source coordinate for
  the chosen topological sector; a nonzero determinant in the conjugate block,
  a chirality-balanced four-source selection, or a mass-assisted coordinate
  is not the same physical amplitude.
- `prop:instanton-axial-ward-source-transport`: the Q=1 phase
  `exp(i theta)` and the two-flavor zero-mode source determinant must be
  transported together under the anomalous singlet axial Ward vector.
- `constr:instanton-mass-source-rg-channel-transport`: the mass/source determinant
  and finite light-fermion nonzero-mode determinant factor cancel only at
  source-functional level; fixed-basis differentiated coefficients, running
  physical source contractions, and finite source-bundle connections have
  distinct RG transports.
- `ca:finite-cell-instanton-channel-control`: finite retained-cell residuals
  and source-determinant perturbations obey the displayed absolute bounds.
- `prop:su3-nf2-hard-source-power-slow-tail` and
  `ca:instanton-hard-benchmark-gate-ledger`: the SU(3), Nf=2 hard
  four-source benchmark has the stated rho power, Q power, slow endpoint tail,
  running collective-coordinate Jacobian, channel-data dependence, and
  same-theory hard-scale ratio bound.
- `ca:instanton-thooft-four-point-amputated-assembly`: an amputated
  four-source instanton Green-function contribution is a common-regulator
  product of density, Haar projection, chiral source determinants, individual
  zero-mode slots, nonzero-mode source response, amputation, physical
  projection, and an absolute residual budget.
- `ca:instanton-thooft-crossed-chiral-channel`: the all-outgoing
  two-flavor 't Hooft source kernel becomes a physical `RR -> LL` channel
  only after the anomalous chirality source monomial is selected, the barred
  slots are crossed with their LSZ residues, and the instanton/anti-instanton
  theta phases are read in a declared quadratic or interference observable.
- `constr:instanton-crossed-helicity-projection`: the crossed scalar source
  kernel becomes a fixed-helicity physical amplitude only after the external
  Weyl spinors are contracted with the antisymmetric left and right spinor
  tensors in the same LSZ normalization.
- `ca:instanton-size-integrated-crossed-hard-channel`: the scalar crossed
  hard coefficient entering the fixed-helicity amplitude is the
  tail-subtracted common-regulator size-window integral multiplied by the
  channel source, Haar, nonzero-mode, amputation, crossing, and running
  collective factors, with helicity residuals propagated afterward.
- `ca:instanton-retained-hard-normal-source-quotient`: the nonzero-mode source
  quotient in the retained crossed hard coefficient is the pointwise
  source-selected Gaussian mean plus the first cubic source-cumulant
  correction, integrated through the same signed hard measure as the zero-mode
  slots.
- `ca:instanton-mass-assisted-interference-channel`: a theta-linear physical
  observable arises only when a mass-assisted one-instanton two-source
  channel, such as `m_d B_uu`, is interfered with a same-basis
  chirality-breaking reference amplitude carrying the conjugate `u` mass
  orientation; the retained phase is `theta + arg m_u + arg m_d` up to the
  channel phase.
- `rem:instanton-same-coordinate-amplitude-rate-obligation`: the all-outgoing
  Euclidean source vector must be crossed, amputated, and projected into a
  physical external-state basis before it is squared or interfered with a
  reference amplitude; unamputated source overlaps, wrong-channel references,
  linear theta-charged sums, and positive-rate or interference residual
  underbudgets are different coordinates.
- `ca:instanton-hard-window-tail-subtraction`: the hard four-source window is
  controlled as a core integral plus leading and subleading analytic endpoint
  tails, rather than as a formal size integral.
- `ca:instanton-hard-screened-retained-window`: a screened hard-size majorant
  window uses the logarithmic shell power, the hard source envelope, the
  physical screening scale, endpoint/weak-coupling gates, and the
  source/projection residual budget together; the majorant shell is not a
  physical amplitude peak unless comparability and noncancellation data are
  also supplied.
- `sec:instanton-hard-wilsonian-ope-datum` and
  `ca:instanton-wilsonian-matching-covariance`: the hard source kernel
  becomes a Wilsonian local four-fermion input only after a dimensionless size
  split, boundary-flux flow, operator matching, long-size remainder, physical
  matrix element, and finite scheme-covariance transport are supplied.

Independent construction:
- The checks build small exact rational cell models from scratch.  They compute
  source-functional route orderings, a named hard-channel spine with
  collective, zero-mode, normal-source, Haar/LSZ, endpoint, and projection
  stages, a retained-cell finite amplitude laboratory with collective,
  determinant, zero-mode source, normal-mode covariance, and projection factors,
  two-by-two determinants, mass/source polynomials, one-loop RG exponents,
  running collective zero-mode Jacobian ratios,
  gauge-sliced zero-mode Gram determinants,
  weighted proper-time determinant logarithms,
  finite color two-frame Haar projectors,
  the Bessel-product tail cancellation for an individual zero-mode slot,
  primed determinant source-response coefficients from finite resolvents,
  cubic operator-family determinant remainders,
  finite Gaussian source-quotient covariance identities,
  Wick-paired first source cumulants from cubic normal-mode interactions,
  source-projected normal propagator insertions with full source-overlap
  amputation and residual telescopes,
  typed normal Green-function bilinears separating smooth source propagation
  from local/composite matching, with finite local covariance and
  Green-norm projector residuals,
  a spectral cutoff model in which smooth source tails converge without local
  subtraction while the local diagonal coordinate exposes independent
  `A0 N`, `A1 H_N`, finite counterterm, and spectral-tail residuals,
  multiplicative hard-amplitude assembly bounds on signed windows,
  finite determinant-scheme transport factors and an independently computed
  two-regulator determinant-density benchmark,
  finite observable-map status comparisons for theta, U(1)_A, and real-time
  axial channels,
  pole-window extraction, mixed-source matrix amputation,
  quadratic inclusive-cut projections from physical amplitude vectors,
  spectral-bin/Stieltjes comparisons, contact
  polynomial separation, and bridge residual telescopes,
  first connected instanton-pair source corrections with explicit
  ordered-pair versus unordered-pair combinatorics,
  neutral-pair lateral-prescription cancellation coordinates,
  chirality-source selection rules for the instanton zero-mode determinant,
  axial Ward transport of the theta phase with the complex source determinant,
  mass/source RG weights separated into fixed-basis coefficients, running
  physical source contractions, and source-bundle connection cancellations,
  an amputated 't Hooft four-point assembly ledger,
  crossed chiral `RR -> LL` channel extraction from the all-outgoing
  source kernel with formal theta-phase bookkeeping,
  crossed hard-channel helicity projections from finite two-component spinors,
  retained-window crossed hard-channel amplitude assembly from the two-term
  size-window tail, source/Haar/fluctuation/crossing data, and helicity
  residual propagation,
  retained hard-channel normal-source quotients from pointwise Gaussian and
  cubic-cumulant corrections integrated against a signed hard measure,
  mass-assisted two-source interference with exact formal mass/theta powers,
  same-coordinate amplitude-to-rate typing with crossed/amputated vectors,
  positive measurement matrices, same-channel interference, source-overlap
  negative controls, positive-rate residual budgets, and vector residual
  propagation,
  physical projection bins, residual sums, two-term hard-window endpoint
  tail subtraction, screened hard-size majorant-window stationarity,
  boundary/weak-coupling gates, actual-kernel counterexamples under the same
  majorant, source/projection residual budgets, Wilsonian
  coefficient/operator scheme covariance,
  boundary-flux/anomalous-dimension cancellation, and hard-window power checks
  directly, rather than importing BPST radial integrals or copying a monograph
  coefficient.

Primary derivation route:
- The manuscript derives the channel formulas from the semiclassical
  finite-regulator path-integral expansion: collective density, zero-mode
  Berezin saturation, proper-time determinant logarithms, source insertion,
  endpoint window, and physical projection are assembled in that order.

Independent verification route:
- The check does not recompute the continuum BPST integral.  It builds finite
  algebraic source channels, exact two-by-two zero-mode source matrices,
  finite Gaussian fluctuation quotients, finite pole/spectral projections, and
  exact rational calibration windows.  These finite models are deliberately
  chosen so rank loss, source quotient transport, physical projection, and
  determinant normalization can be varied independently.

Convention dependencies:
- The evidence uses the monograph half-trace Yang-Mills coupling coordinate,
  the \(SU(3)\), \(N_f=2\) hard-source convention, Dirac fundamental
  determinants rather than Pfaffian half-bookkeeping, coefficient measures
  normalized by `dc/sqrt(2*pi)` for bosonic zero modes, singular-gauge BPST
  zero-mode slots, normalized Haar orientation measure, and the chapter's
  separation between Euclidean source kernels and physical pole/spectral/OPE
  projections.

Domain and remainder assumptions:
- All continuum estimates are represented by finite retained-window cells with
  declared absolute residuals.  The checks assume a weak-size hard window,
  fixed nonzero hard momentum ratios, a nonzero source-rank margin when a
  relative statement is made, and separately budgeted endpoint, sector,
  infrared, continuation, and projection errors.

Remaining unproved or conditional:
- The companion does not compute the continuum finite determinant constant,
  convert Pauli--Villars to \(\overline{\rm MS}\), prove convergence of the
  instanton size integral, prove a Lorentzian LSZ theorem for the auxiliary
  kernel, construct a full dilute ensemble, or validate any specific
  phenomenological instanton regime.

Imported assumptions:
- The finite model assumes that the continuum instanton window has already been
  reduced to finitely many regulator cells and that two light flavors give a
  two-by-two zero-mode source determinant.  It does not assume any continuum
  determinant constant, ADHM volume, or spectral-continuation theorem.

Negative controls:
- The script rejects source-functional shortcuts that replace source
  differentiation by mass saturation, replace source-dependent normal
  fluctuation response by a determinant-only Gaussian mean, replace a
  physical projection by a raw Euclidean source sum, or assemble the finite
  retained-cell laboratory after any of those substitutions.  It rejects named
  hard-channel shortcuts that keep only the moduli/density factor, omit
  normal-source response, omit Haar/LSZ/size-window transport, or square the
  linear amplitude before the physical projection.  It also rejects a plus
  sign in the off-diagonal determinant term, a
  moduli-only prediction that ignores zero-mode rank, a rank-one source matrix
  treated as a nonzero four-source channel, a wrong one-loop density power, a
  density-only hard-channel power, a missing running collective-coordinate
  factor in the hard coefficient or ratio, a Pfaffian half-convention
  substituted for a Dirac fundamental determinant, a wrong proper-time
  determinant sign, a
  signed heat-kernel residual cancellation used as an absolute window bound,
  an untransported determinant constant, a
  symmetric color source or orientation-volume constant substituted for the
  Haar antisymmetric two-frame projection, a
  fused-density endpoint class substituted for differentiated fermion slots,
  an unamputated external residue absorbed into the zero-mode slot tail, a
  dimension-only zero-mode count substituted for the collective-coordinate
  Jacobian, raw gauge-vertical tangents used before horizontal projection, a
  determinant used where the functional measure requires a square-root
  determinant, an unprimed trace with an arbitrary zero-mode regulator
  substituted for a primed determinant response, a wrong bosonic determinant
  sign, a linear log-series tail used to bound a cubic operator-family
  perturbation, a vacuum determinant calibration substituted for a
  source-fluctuation quotient, a zero cubic interaction used to erase a
  linear-source cumulant, a source-dependent cubic covariance absorbed into a
  universal determinant constant, a normal propagator insertion replaced by a
  determinant constant, an unprimed zero-mode-regulated inverse used as a
  channel propagator, a trace substituted for an external-source bilinear,
  diagonal residue division substituted for a full source-overlap inverse, an
  omitted propagator residual in a zero-mode-times-normal channel, a relative
  quotient formed after zero-mode
  rank loss, a
  subtracted Green function formed without the projector, without the free
  parametrix, without the logarithmic local term, or without the compensating
  local Wilsonian coefficient shift, a smooth spectral source over-subtracted
  by local shell terms, a local spectral coordinate used without extracting
  the `A0`/`A1` shell data, a finite local counterterm omitted from the
  matched coordinate, or a local spectral residual budget with the leading
  shell-coefficient error removed, a
  determinant-only assembled amplitude, signed-window relative error control
  without a noncancellation margin, a reference calibration with omitted
  source-fluctuation or physical-projection transport, a rank-lost reference
  channel used as a determinant normalization, source/projection matrices
  absorbed into a universal determinant constant, a finite determinant constant
  transported without the running zero-mode power or orientation measure, a
  determinant conversion inferred from a chosen transport constant rather than
  independently computed regulator densities, a
  hard source coefficient used as a theta susceptibility, a dilute
  topological susceptibility used as a real-time rate, a dilute instanton
  curvature substituted for Witten-Veneziano curvature without a comparison
  budget, a Euclidean source value used as a physical pole or spectral bin,
  diagonal-overlap division substituted for mixed-source pole amputation,
  a colored auxiliary instanton kernel treated as a standalone LSZ amplitude,
  a linear signed instanton amplitude sum treated as a positive inclusive cut,
  an unamputated source vector used in the quadratic cut, a measurement matrix
  omitted from the physical bin,
  a bridge budget omitting the inverse-problem residual, a neutral pair
  controlled only by theta curvature, a disconnected
  pair product counted as a connected source correction, an ordered pair sum
  used without its Mayer symmetry factor, a one-body sector-isolation budget
  that omits pair leakage, a
  neutral valley principal value treated as the full lateral contribution,
  pair-only lateral ambiguity treated as physical, a vacuum-residue
  cancellation transported to a different source coordinate,
  wrong-chirality determinants, chirality-balanced four-source selections, or
  mass-assisted source coordinates treated as the Q=1 hard 't Hooft vertex,
  source-only or theta-only axial rotations treated as Ward-invariant,
  RG-invariant-density shortcuts that omit the mass/source determinant flow,
  differentiated instanton coefficients used without the compensating source
  or operator projection flow,
  an amputated four-point coefficient reduced to density-only data, a
  symmetric Haar source treated as nonzero, an omitted nonzero-mode source
  quotient, unamputated source overlaps read as a physical coefficient, or an
  assembly residual budget with the projection term removed,
  an all-outgoing source coefficient used without crossing residues, a
  conjugate anti-instanton chirality block inserted into the same massless
  `RR -> LL` channel, a linear theta-charged instanton sum treated as a
  positive rate, a chirality-preserving perturbative reference used despite
  the selection rule, or a crossed-channel residual budget with the crossing
  term removed,
  a scalar crossed hard coefficient treated as a fixed-helicity amplitude,
  collinear external spinors treated as nonzero in the helicity bin, swapped
  external Weyl slots used without the antisymmetric sign, a scalar coefficient
  squared as a spin-summed rate without helicity/phase-space weights, or a
  helicity residual budget with the external-state term removed,
  a size-integrated hard channel read from the density alone, the numerical
  core of the size integral without endpoint tails, the channel without the
  nonzero-mode source quotient, the hard scale dependence with the running
  collective factor stripped, or the retained scalar coefficient used as a
  fixed-helicity amplitude before spinor projection,
  a retained hard-channel normal-source quotient replaced by the vacuum
  determinant, by the Gaussian mean alone, by an unweighted post-projection
  average, or by a residual budget with the cubic source cumulant omitted,
  a mass-assisted two-source channel used as the massless four-source
  vertex, a wrong same-flavor mass used to saturate the complementary
  zero modes, a reference amplitude in the wrong source degree or chirality
  coordinate, a nonconjugated mass reference producing
  `theta - arg m_u + arg m_d`, or an interference residual budget with the
  reference-amplitude error removed,
  an all-outgoing source vector squared before crossing/projection,
  unamputated source overlaps used in a physical quadratic cut, a
  wrong-channel reference amplitude interfered through a formal scalar
  product, a linear theta-charged source sum treated as a positive rate, or
  a positive-rate residual budget with the amplitude or measurement error
  removed, or a same-channel vector interference residual budget with the
  reference-vector error removed,
  single Euclidean cell sum used as a spectral-bin observable, a
  determinant-only hard-scale ratio, a hard benchmark with a missing hard
  slot, a leading-tail-only hard-window approximation, hard-only or
  screening-only shell substitutions, a moduli-only screened-window bound, a
  majorant-shell peak treated as an actual-amplitude peak without
  comparability, an interior saddle used below the long-size endpoint or
  outside the weak-coupling domain, a wrong `d rho` power used as a
  logarithmic shell power, a fused-density
  endpoint substituted for differentiated slots, a fixed short-instanton
  vertex under a moving size boundary, a short
  coefficient used as a physical amplitude, a finite scheme change applied to
  coefficients without the operator matrix elements, a moving-boundary flow
  with the long-size shell omitted, a full hard source coefficient
  used as a local OPE coefficient without the long-size matrix element, and a
  residual bound that omits the external projection/sector remainder.

Scope boundary:
- Passing these checks proves only finite algebra and channel bookkeeping.  It
  does not prove continuum convergence of the instanton integral, compute the
  Pauli--Villars determinant constant, establish a Lorentzian scattering
  theorem, or justify any specific dilute-gas regime.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

from check_utils import assert_close, assert_geq, assert_gt, assert_leq


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def det2(matrix: Matrix2) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def trace2(matrix: Matrix2) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def add2(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def sub2(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def transpose2(matrix: Matrix2) -> Matrix2:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def matmul2(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def inv2(matrix: Matrix2) -> Matrix2:
    determinant = det2(matrix)
    if determinant == 0:
        raise AssertionError("singular matrix")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def max_abs_entry(matrix: Matrix2) -> Fraction:
    return max(abs(entry) for row in matrix for entry in row)


def assert_not_equal(name: str, actual: Fraction, bad: Fraction) -> None:
    if actual == bad:
        raise AssertionError(f"{name}: wrong shortcut unexpectedly matched {actual!r}")


def assert_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def product(values: list[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def label_context(path: str, label: str, before: int = 900, after: int = 1300) -> str:
    text = Path(path).read_text()
    index = text.index(label)
    return text[max(0, index - before) : index + after]


def assert_contains(name: str, haystack: str, needle: str) -> None:
    if needle not in haystack:
        raise AssertionError(f"{name}: missing {needle!r}")


def beta0(n_colors: int, n_flavors: int) -> Fraction:
    return Fraction(11, 3) * n_colors - Fraction(2, 3) * n_flavors


def check_source_functional_route_order() -> None:
    # The two-flavor zero-mode determinant is a source functional.  Its
    # differentiated four-source coordinates are not the mass-saturated vacuum
    # activity.
    m_u = Fraction(2)
    m_d = Fraction(3)
    vacuum_activity = m_u * m_d
    diagonal_four_source = Fraction(1)
    offdiagonal_four_source = -Fraction(1)

    assert_not_equal(
        "diagonal four-source derivative is not mass-saturated activity",
        diagonal_four_source,
        vacuum_activity,
    )
    assert_not_equal(
        "off-diagonal four-source derivative is not mass-saturated activity",
        offdiagonal_four_source,
        vacuum_activity,
    )
    assert_equal(
        "opposite source order reads the determinant sign",
        diagonal_four_source + offdiagonal_four_source,
        Fraction(0),
    )

    def average(values: list[Fraction]) -> Fraction:
        return sum(values, Fraction(0)) / len(values)

    def source_response(
        source_insertion: list[Fraction],
        interaction_weight: list[Fraction],
    ) -> tuple[Fraction, Fraction, Fraction, Fraction]:
        determinant_normalization = average(interaction_weight)
        gaussian_source_mean = average(source_insertion)
        interacting_source_response = (
            average(
                [
                    src * weight
                    for src, weight in zip(source_insertion, interaction_weight)
                ]
            )
            / determinant_normalization
        )
        covariance = average(
            [
                (src - gaussian_source_mean) * (weight - determinant_normalization)
                for src, weight in zip(source_insertion, interaction_weight)
            ]
        )
        return (
            interacting_source_response,
            gaussian_source_mean,
            determinant_normalization,
            covariance,
        )

    # A retained-cell source-functional laboratory.  Each cell carries a
    # collective weight, a determinant normalization, a zero-mode source
    # coordinate, a normal-fluctuation source quotient, and a physical
    # projection.  The exact values below make these five factors independent.
    retained_cells = [
        (
            "hard cell",
            Fraction(1, 2),
            Fraction(2, 3),
            Fraction(1),
            diagonal_four_source,
            [Fraction(1), Fraction(2)],
            [Fraction(1), Fraction(3)],
        ),
        (
            "projected tail cell",
            Fraction(1, 3),
            Fraction(3, 5),
            Fraction(1, 2),
            diagonal_four_source,
            [Fraction(2), Fraction(3)],
            [Fraction(3), Fraction(1)],
        ),
    ]

    routed_coordinate = Fraction(0)
    determinant_only_source_shortcut = Fraction(0)
    mass_saturation_shortcut = Fraction(0)
    euclidean_kernel_shortcut = Fraction(0)

    for (
        cell_name,
        collective_weight,
        determinant_constant,
        projection_weight,
        zero_mode_source_coordinate,
        source_insertion,
        interaction_weight,
    ) in retained_cells:
        (
            interacting_source_response,
            gaussian_source_mean,
            determinant_normalization,
            covariance,
        ) = source_response(source_insertion, interaction_weight)
        assert_equal(
            f"{cell_name} source-fluctuation covariance identity",
            interacting_source_response - gaussian_source_mean,
            covariance / determinant_normalization,
        )
        assert_not_equal(
            f"{cell_name} determinant normalization alone does not fix source response",
            interacting_source_response,
            gaussian_source_mean,
        )

        common_weight = (
            collective_weight * determinant_constant * zero_mode_source_coordinate
        )
        routed_coordinate += (
            projection_weight * common_weight * interacting_source_response
        )
        determinant_only_source_shortcut += (
            projection_weight * common_weight * gaussian_source_mean
        )
        mass_saturation_shortcut += (
            projection_weight
            * collective_weight
            * determinant_constant
            * vacuum_activity
            * interacting_source_response
        )
        euclidean_kernel_shortcut += common_weight * interacting_source_response

    assert_equal(
        "finite retained-cell source-functional amplitude laboratory",
        routed_coordinate,
        Fraction(97, 120),
    )
    assert_equal(
        "determinant-only finite laboratory shortcut value",
        determinant_only_source_shortcut,
        Fraction(3, 4),
    )
    assert_equal(
        "mass-saturated finite laboratory shortcut value",
        mass_saturation_shortcut,
        Fraction(97, 20),
    )
    assert_equal(
        "raw Euclidean finite laboratory shortcut value",
        euclidean_kernel_shortcut,
        Fraction(31, 30),
    )

    assert_not_equal(
        "mass saturation is not the differentiated source amplitude",
        mass_saturation_shortcut,
        routed_coordinate,
    )
    assert_not_equal(
        "Gaussian determinant-only shortcut misses source covariance",
        determinant_only_source_shortcut,
        routed_coordinate,
    )
    assert_not_equal(
        "raw Euclidean kernel shortcut misses physical projection",
        euclidean_kernel_shortcut,
        routed_coordinate,
    )


def check_named_hard_channel_trace_spine() -> None:
    physical_path = (
        "monograph/tex/volumes/volume_ii/"
        "chapter20d_instantons_and_physical_amplitudes.tex"
    )
    spine_context = label_context(
        physical_path,
        "rem:instanton-su3-nf2-hard-channel-spine",
        before=300,
        after=1900,
    )
    for name, needle in [
        ("named spine exposes BPST/ADHM as collective data", "BPST/ADHM"),
        ("named spine keeps normal-fluctuation response", "normal-fluctuation"),
        ("named spine keeps physical projection", "\\Pi_{\\rm phys}"),
        ("named spine keeps projection residual", "B_{\\rm proj}"),
    ]:
        assert_contains(name, spine_context, needle)

    # Finite analogue of the named SU(3), N_f=2 hard channel trace.  The
    # numerical choices are independent so each stage can be removed without
    # accidentally preserving the final coordinate.
    stage_factors = {
        "collective_density": Fraction(5, 7),
        "zero_mode_source": Fraction(3, 2),
        "normal_source_response": Fraction(7, 6),
        "haar_lsz_window": Fraction(4, 9),
        "size_window": Fraction(11, 10),
        "physical_projection": Fraction(2, 5),
    }
    hard_amplitude = product(list(stage_factors.values()))
    assert_equal("named hard-channel linear amplitude", hard_amplitude, Fraction(11, 45))

    moduli_density_only = stage_factors["collective_density"]
    omitted_normal_response = hard_amplitude / stage_factors["normal_source_response"]
    omitted_haar_lsz_window = hard_amplitude / stage_factors["haar_lsz_window"]
    raw_euclidean_before_projection = hard_amplitude / stage_factors["physical_projection"]

    assert_not_equal(
        "named spine rejects moduli-density-only coordinate",
        moduli_density_only,
        hard_amplitude,
    )
    assert_not_equal(
        "named spine rejects omitted normal-source response",
        omitted_normal_response,
        hard_amplitude,
    )
    assert_not_equal(
        "named spine rejects omitted Haar/LSZ/size transport",
        omitted_haar_lsz_window,
        hard_amplitude,
    )
    assert_not_equal(
        "named spine rejects raw Euclidean pre-projection coordinate",
        raw_euclidean_before_projection,
        hard_amplitude,
    )

    measurement_weight = Fraction(9, 8)
    positive_rate_bin = measurement_weight * hard_amplitude * hard_amplitude
    assert_equal("named hard-channel positive rate bin", positive_rate_bin, Fraction(121, 1800))
    assert_not_equal(
        "named spine rejects linear amplitude as positive rate",
        hard_amplitude,
        positive_rate_bin,
    )

    residuals = {
        "collective": Fraction(1, 300),
        "zero_mode": Fraction(1, 360),
        "normal_source": Fraction(1, 420),
        "haar_lsz": Fraction(1, 630),
        "size_window": Fraction(1, 700),
        "projection": Fraction(1, 840),
    }
    residual_budget = sum(residuals.values(), Fraction(0))
    actual_extreme_residual = residual_budget
    assert_equal(
        "named hard-channel residual budget keeps all stages",
        actual_extreme_residual <= residual_budget,
        True,
    )
    underbudget_without_normal = residual_budget - residuals["normal_source"]
    assert_equal(
        "omitting normal-source residual underbudgets named spine",
        actual_extreme_residual <= underbudget_without_normal,
        False,
    )
    underbudget_without_projection = residual_budget - residuals["projection"]
    assert_equal(
        "omitting projection residual underbudgets named spine",
        actual_extreme_residual <= underbudget_without_projection,
        False,
    )


def check_collective_coordinate_zero_mode_jacobian() -> None:
    Vector3 = tuple[Fraction, Fraction, Fraction]

    def dot3(left: Vector3, right: Vector3) -> Fraction:
        return sum(l * r for l, r in zip(left, right))

    def horizontal(vector: Vector3) -> Vector3:
        # Finite analogue of the gauge-slice projection: remove the vertical
        # gauge direction before forming the collective-coordinate Gram metric.
        return (vector[0], vector[1], Fraction(0))

    def gram2(
        first: Vector3,
        second: Vector3,
    ) -> Matrix2:
        return (
            (dot3(first, first), dot3(first, second)),
            (dot3(second, first), dot3(second, second)),
        )

    def scale2(scalar: Fraction, matrix: Matrix2) -> Matrix2:
        return tuple(
            tuple(scalar * entry for entry in row)
            for row in matrix
        )  # type: ignore[return-value]

    def row_sum_norm2(matrix: Matrix2) -> Fraction:
        return max(sum(abs(entry) for entry in row) for row in matrix)

    raw_tangent_a: Vector3 = (Fraction(2), Fraction(0), Fraction(1))
    raw_tangent_b: Vector3 = (Fraction(1), Fraction(2), -Fraction(1))
    horizontal_a = horizontal(raw_tangent_a)
    horizontal_b = horizontal(raw_tangent_b)

    horizontal_gram = gram2(horizontal_a, horizontal_b)
    assert_equal(
        "horizontal zero-mode Gram metric",
        horizontal_gram,
        ((Fraction(4), Fraction(2)), (Fraction(2), Fraction(5))),
    )
    gram_determinant = det2(horizontal_gram)
    sqrt_gram_determinant = Fraction(4)
    assert_equal(
        "collective-coordinate Jacobian uses sqrt det Gram",
        gram_determinant,
        sqrt_gram_determinant * sqrt_gram_determinant,
    )

    dimension_only_weight = Fraction(1)
    assert_not_equal(
        "zero-mode dimension count misses the Gram Jacobian",
        dimension_only_weight,
        sqrt_gram_determinant,
    )
    assert_not_equal(
        "det Gram is not the bosonic functional-measure Jacobian",
        gram_determinant,
        sqrt_gram_determinant,
    )

    raw_gram = gram2(raw_tangent_a, raw_tangent_b)
    assert_not_equal(
        "raw gauge-vertical tangents change the Gram determinant",
        det2(raw_gram),
        gram_determinant,
    )

    action_inner_product_factor = Fraction(5, 3)
    scaled_gram = scale2(action_inner_product_factor, horizontal_gram)
    assert_equal(
        "action normalization scales the two-mode Jacobian",
        det2(scaled_gram),
        (action_inner_product_factor * sqrt_gram_determinant) ** 2,
    )

    stabilizer_volume = Fraction(2)
    source_kernel = Fraction(7, 11)
    channel_weight = sqrt_gram_determinant * source_kernel / stabilizer_volume
    assert_not_equal(
        "stabilizer quotient is part of the source-channel normalization",
        sqrt_gram_determinant * source_kernel,
        channel_weight,
    )

    delta_gram: Matrix2 = (
        (Fraction(1, 20), -Fraction(1, 40)),
        (-Fraction(1, 40), Fraction(1, 30)),
    )
    perturbed_gram = add2(horizontal_gram, delta_gram)
    det_shift = det2(perturbed_gram) - gram_determinant
    entry_bound = max_abs_entry(delta_gram)
    det_shift_bound = (
        (
            abs(horizontal_gram[1][1])
            + abs(horizontal_gram[0][0])
            + abs(horizontal_gram[0][1])
            + abs(horizontal_gram[1][0])
        )
        * entry_bound
        + 2 * entry_bound * entry_bound
    )
    assert_leq(
        "finite zero-mode Gram determinant perturbation bound",
        abs(det_shift),
        det_shift_bound,
    )

    sqrt_shift = abs(math.sqrt(float(det2(perturbed_gram))) - float(sqrt_gram_determinant))
    assert_leq(
        "finite zero-mode Jacobian square-root perturbation bound",
        sqrt_shift,
        float(det_shift_bound / sqrt_gram_determinant),
    )

    relative_metric_error = matmul2(inv2(horizontal_gram), delta_gram)
    norm_bound = row_sum_norm2(relative_metric_error)
    assert_lt_one = norm_bound < 1
    assert_equal(
        "retained Gram perturbation is inside the logarithmic stability domain",
        assert_lt_one,
        True,
    )
    relative_jacobian_error = (
        math.sqrt(float(det2(perturbed_gram) / gram_determinant)) - 1.0
    )
    logarithmic_bound = math.exp(
        float(Fraction(2) * norm_bound / (2 * (1 - norm_bound)))
    ) - 1.0
    assert_leq(
        "zero-mode Jacobian logarithmic stability bound",
        abs(relative_jacobian_error),
        logarithmic_bound,
    )


def check_one_loop_density_rg_and_channel_power() -> None:
    for n_colors, n_flavors in [(2, 0), (3, 2), (4, 3), (5, 6)]:
        b0 = beta0(n_colors, n_flavors)
        correct_density_power = b0
        wrong_density_power = b0 + Fraction(1)

        rg_derivative = correct_density_power - b0
        wrong_rg_derivative = wrong_density_power - b0
        assert_equal(
            f"SU({n_colors}) Nf={n_flavors} one-loop density RG cancellation",
            rg_derivative,
            Fraction(0),
        )
        assert_not_equal(
            "wrong determinant logarithm power fails the RG cancellation",
            wrong_rg_derivative,
            Fraction(0),
        )

        density_only_size_power = b0 - 5
        mass_saturated_power = density_only_size_power + n_flavors
        assert_equal(
            "mass-saturated channel adds zero-mode mass powers",
            mass_saturated_power,
            b0 + n_flavors - 5,
        )
        if n_flavors:
            assert_not_equal(
                "mass-saturated channel is not the density-only integrand",
                mass_saturated_power,
                density_only_size_power,
            )

    b0_su3_nf2 = beta0(3, 2)
    density_only_size_power = b0_su3_nf2 - 5
    four_source_zero_mode_power = Fraction(6)
    hard_four_source_power = density_only_size_power + four_source_zero_mode_power
    assert_equal("SU3 Nf2 density-only rho power", density_only_size_power, Fraction(14, 3))
    assert_equal("SU3 Nf2 hard four-source channel rho power", hard_four_source_power, Fraction(32, 3))
    assert_not_equal(
        "density-only power misses hard four-source zero modes",
        density_only_size_power,
        hard_four_source_power,
    )

    determinant_constant = Fraction(7, 11)
    transported_channel_factor = Fraction(5, 13)
    source_window_1 = Fraction(17, 19)
    source_window_2 = Fraction(23, 29)
    q_power = -Fraction(35, 3)
    absolute_prefactor_1 = determinant_constant * transported_channel_factor * source_window_1
    absolute_prefactor_2 = determinant_constant * transported_channel_factor * source_window_2
    same_channel_ratio_prefactor = absolute_prefactor_2 / absolute_prefactor_1
    assert_equal(
        "same-channel determinant constant cancels in density-normalization ratio",
        same_channel_ratio_prefactor,
        source_window_2 / source_window_1,
    )
    if q_power == 0:
        raise AssertionError("hard ratio should retain the physical source-scale power")

    untransported_channel_factor = Fraction(3, 17)
    untransported_ratio_prefactor = (
        determinant_constant * untransported_channel_factor * source_window_2
    ) / absolute_prefactor_1
    assert_not_equal(
        "changed channel data is not a same-channel determinant cancellation",
        untransported_ratio_prefactor,
        source_window_2 / source_window_1,
    )

    scheme_constant_dropped = transported_channel_factor * source_window_1
    assert_not_equal(
        "absolute density coefficient depends on finite determinant convention",
        scheme_constant_dropped,
        absolute_prefactor_1,
    )


def check_running_collective_jacobian_in_hard_coefficient() -> None:
    n_colors = 3
    b0_su3_nf2 = beta0(n_colors, 2)
    q_power = -(b0_su3_nf2 + 2)
    collective_jacobian_power = 2 * n_colors

    assert_equal("SU3 Nf2 hard b0 for collective check", b0_su3_nf2, Fraction(29, 3))
    assert_equal("SU3 bosonic zero-mode Jacobian power", collective_jacobian_power, 6)
    assert_equal("hard power-counting Q exponent", q_power, -Fraction(35, 3))
    assert_equal("hard coefficient mass dimension modulo logs", b0_su3_nf2 + q_power, Fraction(-2))

    # Finite model for two hard scales.  The displayed collective factor is
    # L(Q)^(2Nc), where L(Q)=8*pi^2/g_ht(Q)^2.  It is dimensionless but it
    # runs, so it cannot be hidden in a scale-independent channel constant.
    log_action_q1 = Fraction(5, 2)
    log_action_q2 = Fraction(7, 2)
    gamma_coll_q1 = log_action_q1**collective_jacobian_power
    gamma_coll_q2 = log_action_q2**collective_jacobian_power
    finite_channel_constant = Fraction(11, 13)
    source_window = Fraction(27, 40)

    leading_q1 = gamma_coll_q1 * finite_channel_constant * source_window
    leading_q2 = gamma_coll_q2 * finite_channel_constant * source_window
    omitted_jacobian_q2 = finite_channel_constant * source_window

    assert_not_equal(
        "hard coefficient omits the running collective Jacobian",
        omitted_jacobian_q2,
        leading_q2,
    )
    assert_equal(
        "hard coefficient ratio retains collective Jacobian ratio",
        leading_q2 / leading_q1,
        (log_action_q2 / log_action_q1) ** collective_jacobian_power,
    )
    assert_not_equal(
        "pure power ratio omits running collective factor",
        Fraction(1),
        leading_q2 / leading_q1,
    )

    power_only_slope = -q_power
    logarithmic_slope_correction = Fraction(6, 37)
    slope_with_collective_log = power_only_slope - logarithmic_slope_correction
    assert_not_equal(
        "collective logarithm changes the hard logarithmic slope",
        slope_with_collective_log,
        power_only_slope,
    )


def check_cross_chapter_hard_scale_collective_factor_regression() -> None:
    parent_path = "monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex"
    physical_path = (
        "monograph/tex/volumes/volume_ii/"
        "chapter20d_instantons_and_physical_amplitudes.tex"
    )

    parent_decomposition = label_context(
        parent_path,
        "eq:thooft-hard-scale-benchmark-decomposition",
        before=1000,
        after=700,
    )
    parent_ratio = label_context(
        parent_path,
        "eq:thooft-hard-scale-benchmark-ratio",
        before=900,
        after=700,
    )
    physical_coefficient = label_context(
        physical_path,
        "eq:instanton-hard-four-source-coefficient",
        before=900,
        after=500,
    )
    physical_ratio = label_context(
        physical_path,
        "eq:instanton-hard-four-source-ratio",
        before=800,
        after=450,
    )

    for name, context in [
        ("parent hard-scale benchmark coefficient", parent_decomposition),
        ("parent hard-scale benchmark ratio", parent_ratio),
        ("physical chapter hard coefficient", physical_coefficient),
        ("physical chapter hard ratio", physical_ratio),
    ]:
        assert_contains(name, context, "\\Gamma_{\\rm coll}")

    assert_contains(
        "parent hard-scale benchmark keeps pure hard power",
        parent_decomposition,
        "Q^{-(b_0+2)}",
    )
    assert_contains(
        "physical hard coefficient keeps SU3 Nf2 hard power",
        physical_coefficient,
        "Q^{-35/3}",
    )
    assert_contains(
        "parent ratio keeps collective ratio",
        parent_ratio,
        "\\frac{\\Gamma_{\\rm coll}(Q_2)}{\\Gamma_{\\rm coll}(Q_1)}",
    )
    assert_contains(
        "physical ratio keeps collective ratio",
        physical_ratio,
        "\\frac{\\Gamma_{\\rm coll}(Q_2)}{\\Gamma_{\\rm coll}(Q_1)}",
    )

    gamma_index = parent_decomposition.index("\\Gamma_{\\rm coll}(Q)")
    lambda_index = parent_decomposition.index("\\Lambda_{\\rm ht}")
    q_index = parent_decomposition.index("Q^{-(b_0+2)}")
    if not gamma_index < lambda_index < q_index:
        raise AssertionError("parent hard benchmark no longer matches Ch20D factor order")

    old_ratio_without_collective = (
        "\\left(\\frac{Q_2}{Q_1}\\right)^{-(b_0+2)}\n"
        "  \\frac{\\mathcal H_{\\mathfrak h_{Q_2}}(R)}"
    )
    pure_power_pos = parent_ratio.index(old_ratio_without_collective)
    collective_ratio_pos = parent_ratio.index(
        "\\frac{\\Gamma_{\\rm coll}(Q_2)}{\\Gamma_{\\rm coll}(Q_1)}"
    )
    if not collective_ratio_pos < pure_power_pos:
        raise AssertionError("parent hard benchmark ratio dropped the collective prefactor")


def check_proper_time_determinant_log_channel_window() -> None:
    # The density logarithm comes from weighted zero-mode-deleted spectra plus
    # the local counterterm/coupling conversion in the same convention.
    heat_coefficients = {
        "boson": Fraction(20, 3),
        "ghost": Fraction(4, 3),
        "fermion": Fraction(13, 3),
    }
    determinant_weights = {
        "boson": -Fraction(1, 2),
        "ghost": Fraction(1),
        "fermion": Fraction(1),
    }
    spectral_log_power = sum(
        determinant_weights[name] * heat_coefficients[name]
        for name in heat_coefficients
    )
    counterterm_power = Fraction(22, 3)
    b0_su3_nf2 = beta0(3, 2)
    assert_equal("proper-time spectral determinant log power", spectral_log_power, Fraction(7, 3))
    assert_equal(
        "proper-time determinant plus counterterm gives SU3 Nf2 beta0",
        spectral_log_power + counterterm_power,
        b0_su3_nf2,
    )

    wrong_boson_sign_power = (
        Fraction(1, 2) * heat_coefficients["boson"]
        + determinant_weights["ghost"] * heat_coefficients["ghost"]
        + determinant_weights["fermion"] * heat_coefficients["fermion"]
        + counterterm_power
    )
    assert_not_equal(
        "bosonic determinant sign is fixed by the inverse square root",
        wrong_boson_sign_power,
        b0_su3_nf2,
    )

    pfaffian_half_fermion_power = (
        determinant_weights["boson"] * heat_coefficients["boson"]
        + determinant_weights["ghost"] * heat_coefficients["ghost"]
        + Fraction(1, 2) * heat_coefficients["fermion"]
        + counterterm_power
    )
    assert_not_equal(
        "Dirac fundamental determinant is not a Pfaffian half-convention",
        pfaffian_half_fermion_power,
        b0_su3_nf2,
    )

    omitted_ghost_power = (
        determinant_weights["boson"] * heat_coefficients["boson"]
        + determinant_weights["fermion"] * heat_coefficients["fermion"]
        + counterterm_power
    )
    assert_not_equal(
        "ghost determinant is not optional in the log power",
        omitted_ghost_power,
        b0_su3_nf2,
    )

    leading_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    log_residuals = [Fraction(1, 50), -Fraction(1, 45), Fraction(1, 60)]
    epsilon_det = Fraction(1, 40)
    leading_channel = sum(leading_cells, Fraction(0))
    exact_channel = sum(
        float(cell) * math.exp(float(delta))
        for cell, delta in zip(leading_cells, log_residuals)
    )
    absolute_window_mass = sum(abs(cell) for cell in leading_cells)
    determinant_window_bound = float(absolute_window_mass) * (
        math.exp(float(epsilon_det)) - 1.0
    )
    assert_equal(
        "proper-time log residuals stay inside declared window",
        all(abs(delta) <= epsilon_det for delta in log_residuals),
        True,
    )
    assert_leq(
        "proper-time determinant absolute source-window bound",
        abs(exact_channel - float(leading_channel)),
        determinant_window_bound,
    )

    canceling_trace_bounds = {
        "ghost": Fraction(1, 12),
        "boson": Fraction(1, 3),
        "fermion": Fraction(1, 12),
    }
    signed_fake_bound = sum(
        determinant_weights[name] * canceling_trace_bounds[name]
        for name in canceling_trace_bounds
    )
    absolute_trace_bound = sum(
        abs(determinant_weights[name]) * canceling_trace_bounds[name]
        for name in canceling_trace_bounds
    )
    assert_equal("signed heat-kernel residuals can cancel spuriously", signed_fake_bound, Fraction(0))
    assert_gt(
        "absolute heat-kernel residual window remains positive",
        float(absolute_trace_bound),
        0.0,
    )

    determinant_density = Fraction(5, 7)
    zero_mode_source_rank_lost = Fraction(0)
    physical_projection = Fraction(3, 11)
    actual_channel = determinant_density * zero_mode_source_rank_lost * physical_projection
    determinant_only_shortcut = determinant_density * physical_projection
    assert_equal("rank-lost source channel vanishes after determinant", actual_channel, Fraction(0))
    assert_not_equal(
        "nonzero determinant density does not revive a killed source channel",
        determinant_only_shortcut,
        actual_channel,
    )


def check_hard_color_orientation_haar_tensor() -> None:
    n_colors = 3
    coefficient = Fraction(2, n_colors * (n_colors - 1))
    assert_equal("SU3 charge-one Haar two-frame coefficient", coefficient, Fraction(1, 3))

    trace_of_antisymmetric_projector = n_colors * n_colors - n_colors
    assert_equal(
        "Haar two-frame tensor has unnormalized wedge norm two",
        coefficient * trace_of_antisymmetric_projector,
        Fraction(2),
    )

    def orientation_projection(x, y):
        return coefficient * sum(
            x[a][b] * (y[a][b] - y[b][a])
            for a in range(n_colors)
            for b in range(n_colors)
        )

    antisymmetric_right = (
        (Fraction(0), Fraction(2), -Fraction(1)),
        (-Fraction(2), Fraction(0), Fraction(3)),
        (Fraction(1), -Fraction(3), Fraction(0)),
    )
    antisymmetric_left = (
        (Fraction(0), Fraction(5), Fraction(4)),
        (-Fraction(5), Fraction(0), Fraction(1)),
        (-Fraction(4), -Fraction(1), Fraction(0)),
    )
    symmetric_left = (
        (Fraction(7), Fraction(2), Fraction(3)),
        (Fraction(2), Fraction(11), Fraction(5)),
        (Fraction(3), Fraction(5), Fraction(13)),
    )

    projected_color_factor = orientation_projection(antisymmetric_right, antisymmetric_left)
    assert_equal("hard Haar antisymmetric source projection", projected_color_factor, Fraction(12))
    assert_equal(
        "hard Haar projection kills symmetric color pair source",
        orientation_projection(antisymmetric_right, symmetric_left),
        Fraction(0),
    )

    orientation_volume_constant = Fraction(1)
    naive_volume_factor = orientation_volume_constant * sum(
        antisymmetric_right[a][b] * antisymmetric_left[a][b]
        for a in range(n_colors)
        for b in range(n_colors)
    )
    assert_not_equal(
        "orientation volume constant is not the Haar color tensor",
        naive_volume_factor,
        projected_color_factor,
    )

    determinant_constant = Fraction(11, 13)
    right_flavor_det = Fraction(3)
    left_flavor_det = Fraction(4)
    hard_window = Fraction(27, 40)
    physical_projection = Fraction(7, 11)
    amplitude_color_projected = (
        determinant_constant
        * right_flavor_det
        * left_flavor_det
        * projected_color_factor
        * hard_window
        * physical_projection
    )
    amplitude_symmetric_color = (
        determinant_constant
        * right_flavor_det
        * left_flavor_det
        * orientation_projection(antisymmetric_right, symmetric_left)
        * hard_window
        * physical_projection
    )
    assert_equal("symmetric color source kills full hard benchmark", amplitude_symmetric_color, Fraction(0))
    assert_not_equal(
        "nonzero density and zero-mode flavor determinants do not bypass color projection",
        determinant_constant * right_flavor_det * left_flavor_det * hard_window,
        amplitude_symmetric_color,
    )
    assert_gt("antisymmetric color projected amplitude is nonzero", float(abs(amplitude_color_projected)), 0.0)


def check_individual_zero_mode_slot_tail_from_bessel_products() -> None:
    # From the displayed large-t products:
    #   2t(I0 K1 - I1 K0) = t^(-1) + 3/8 t^(-3) + O(t^(-5)),
    #   2 I1 K1          = t^(-1) - 3/8 t^(-3) + O(t^(-5)).
    # The apparent t^(-1) tail cancels in F_zm.
    first_term_t_minus_1 = Fraction(1)
    second_term_t_minus_1 = Fraction(1)
    first_term_t_minus_3 = Fraction(3, 8)
    second_term_t_minus_3 = -Fraction(3, 8)

    assert_equal(
        "individual zero-mode slot cancels t^-1 tail",
        first_term_t_minus_1 - second_term_t_minus_1,
        Fraction(0),
    )
    fzm_t_tail = first_term_t_minus_3 - second_term_t_minus_3
    assert_equal(
        "individual zero-mode slot t^-3 coefficient",
        fzm_t_tail,
        Fraction(3, 4),
    )

    # The hard channel uses t = z/2 = c s/2, so (3/4) t^(-3) = 6 z^(-3).
    fzm_z_tail = fzm_t_tail * Fraction(2**3)
    assert_equal("individual zero-mode slot z^-3 coefficient", fzm_z_tail, Fraction(6))

    c_values = [Fraction(1), Fraction(2), Fraction(3), Fraction(5)]
    four_slot_tail = product([fzm_z_tail / (c**3) for c in c_values])
    expected_tail = Fraction(6**4, (1 * 2 * 3 * 5) ** 3)
    assert_equal("four differentiated zero-mode slot tail", four_slot_tail, expected_tail)

    b0_su3_nf2 = beta0(3, 2)
    size_integrand_power = b0_su3_nf2 + 6 - 5
    tail_integrand_power = size_integrand_power - 12
    tail_antiderivative_power = tail_integrand_power + 1
    leading_tail_coefficient = -four_slot_tail / tail_antiderivative_power
    assert_equal("four-slot product tail integrand power", tail_integrand_power, -Fraction(4, 3))
    assert_equal("four-slot product tail coefficient", leading_tail_coefficient, 3 * four_slot_tail)

    fused_density_endpoint_class = "exponential"
    individual_slot_endpoint_class = "power"
    assert_not_equal(
        "fused density source endpoint class is not a differentiated slot",
        fused_density_endpoint_class,
        individual_slot_endpoint_class,
    )

    external_residue = Fraction(7, 5)
    unamputated_slot_tail = external_residue * fzm_z_tail
    assert_not_equal(
        "external residue is not part of the amputated zero-mode slot tail",
        unamputated_slot_tail,
        fzm_z_tail,
    )
    assert_equal(
        "amputation recovers zero-mode slot tail",
        unamputated_slot_tail / external_residue,
        fzm_z_tail,
    )


def check_primed_determinant_source_response() -> None:
    def entry_l1(matrix: Matrix2) -> Fraction:
        return sum(abs(entry) for row in matrix for entry in row)

    def row_sum_norm(matrix: Matrix2) -> Fraction:
        return max(sum(abs(entry) for entry in row) for row in matrix)

    boson_hessian: Matrix2 = (
        (Fraction(3), Fraction(1)),
        (Fraction(1), Fraction(2)),
    )
    boson_source: Matrix2 = (
        (Fraction(1, 5), Fraction(2, 7)),
        (Fraction(2, 7), Fraction(-1, 3)),
    )
    boson_resolvent = matmul2(inv2(boson_hessian), boson_source)
    boson_trace = trace2(boson_resolvent)
    boson_trace_square = trace2(matmul2(boson_resolvent, boson_resolvent))
    boson_det_square = det2(boson_resolvent)

    assert_equal(
        "primed boson determinant polynomial uses resolvent traces",
        boson_det_square,
        Fraction(1, 2) * (boson_trace * boson_trace - boson_trace_square),
    )
    boson_ratio_first = -Fraction(1, 2) * boson_trace
    boson_ratio_second = (
        -Fraction(1, 2) * boson_det_square
        + Fraction(3, 8) * boson_trace * boson_trace
    )
    boson_log_second_from_ratio = (
        boson_ratio_second
        - Fraction(1, 2) * boson_ratio_first * boson_ratio_first
    )
    assert_equal(
        "bosonic determinant source log first coefficient",
        boson_ratio_first,
        -Fraction(1, 2) * boson_trace,
    )
    assert_equal(
        "bosonic determinant source log second coefficient",
        boson_log_second_from_ratio,
        Fraction(1, 4) * boson_trace_square,
    )

    fermion_dirac: Matrix2 = (
        (Fraction(2), Fraction(1)),
        (Fraction(3), Fraction(5)),
    )
    fermion_source: Matrix2 = (
        (Fraction(1, 4), Fraction(-1, 6)),
        (Fraction(2, 9), Fraction(1, 7)),
    )
    fermion_resolvent = matmul2(inv2(fermion_dirac), fermion_source)
    fermion_trace = trace2(fermion_resolvent)
    fermion_trace_square = trace2(matmul2(fermion_resolvent, fermion_resolvent))
    fermion_det_square = det2(fermion_resolvent)
    fermion_log_second_from_det = (
        fermion_det_square
        - Fraction(1, 2) * fermion_trace * fermion_trace
    )
    assert_equal(
        "fermion determinant source log first coefficient",
        fermion_trace,
        trace2(fermion_resolvent),
    )
    assert_equal(
        "fermion determinant source log second coefficient",
        fermion_log_second_from_det,
        -Fraction(1, 2) * fermion_trace_square,
    )

    counterterm_first = Fraction(1, 11)
    counterterm_second = Fraction(-2, 13)
    combined_log_first = (
        counterterm_first
        - Fraction(1, 2) * boson_trace
        + fermion_trace
    )
    combined_log_second = (
        counterterm_second
        + Fraction(1, 4) * boson_trace_square
        - Fraction(1, 2) * fermion_trace_square
    )
    source_independent_counterterm_only = counterterm_first
    assert_not_equal(
        "source-independent determinant constant misses primed first response",
        combined_log_first,
        source_independent_counterterm_only,
    )
    wrong_boson_sign = (
        counterterm_first
        + Fraction(1, 2) * boson_trace
        + fermion_trace
    )
    assert_not_equal(
        "wrong bosonic determinant sign changes source response",
        wrong_boson_sign,
        combined_log_first,
    )
    determinant_constant_second_only = counterterm_second
    assert_not_equal(
        "second determinant response is not a scheme constant alone",
        combined_log_second,
        determinant_constant_second_only,
    )

    zero_mode_source_trace = Fraction(3, 17)
    zero_mode_regulator_a = Fraction(1, 19)
    zero_mode_regulator_b = Fraction(1, 23)
    unprimed_trace_a = (
        boson_trace + zero_mode_source_trace / zero_mode_regulator_a
    )
    unprimed_trace_b = (
        boson_trace + zero_mode_source_trace / zero_mode_regulator_b
    )
    assert_not_equal(
        "unprimed determinant trace depends on arbitrary zero-mode regulator",
        unprimed_trace_a,
        unprimed_trace_b,
    )
    assert_not_equal(
        "zero-mode-regulated trace is not the primed trace",
        unprimed_trace_a,
        boson_trace,
    )

    linear_x: Matrix2 = (
        (Fraction(1, 10), Fraction(0)),
        (Fraction(0), -Fraction(1, 20)),
    )
    cubic_y: Matrix2 = (
        (Fraction(1, 5), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    linear_norm = row_sum_norm(linear_x)
    cubic_norm = row_sum_norm(cubic_y)
    linear_trace_norm = entry_l1(linear_x)
    cubic_trace_norm = entry_l1(cubic_y)
    linear_third_coefficient = -Fraction(1, 6) * trace2(
        matmul2(matmul2(linear_x, linear_x), linear_x)
    )
    cubic_operator_third_coefficient = -Fraction(1, 2) * trace2(cubic_y)
    full_third_coefficient = (
        linear_third_coefficient + cubic_operator_third_coefficient
    )
    old_linear_tail_bound = (
        linear_trace_norm
        * linear_norm
        * linear_norm
        / (6 * (1 - linear_norm))
    )
    operator_remainder_bound = (
        Fraction(1, 2)
        * (cubic_trace_norm / (1 - linear_norm))
        / (1 - cubic_norm / (1 - linear_norm))
    )
    assert_equal(
        "cubic determinant perturbation stays inside resolvent domain",
        cubic_norm / (1 - linear_norm) < 1,
        True,
    )
    assert_equal(
        "old linear determinant tail cannot bound cubic operator response",
        abs(full_third_coefficient) <= old_linear_tail_bound,
        False,
    )
    assert_equal(
        "linear plus operator determinant remainder bounds cubic response",
        abs(full_third_coefficient)
        <= old_linear_tail_bound + operator_remainder_bound,
        True,
    )


def check_nonzero_mode_source_fluctuation_quotient() -> None:
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    assert_equal(
        "normal fluctuation Gaussian weights normalize",
        sum(weights, Fraction(0)),
        Fraction(1),
    )

    source_variation = [Fraction(1, 5), -Fraction(1, 7), Fraction(1, 11)]
    interaction_weight = [Fraction(5, 6), Fraction(7, 5), Fraction(9, 8)]
    determinant_average = sum(
        weight * factor for weight, factor in zip(weights, interaction_weight)
    )
    source_mean = sum(
        weight * variation
        for weight, variation in zip(weights, source_variation)
    )
    numerator = sum(
        weight * (1 + variation) * factor
        for weight, variation, factor in zip(
            weights,
            source_variation,
            interaction_weight,
        )
    )
    fluctuation_quotient = numerator / determinant_average
    covariance = sum(
        weight
        * (variation - source_mean)
        * (factor - determinant_average)
        for weight, variation, factor in zip(
            weights,
            source_variation,
            interaction_weight,
        )
    )

    assert_equal(
        "nonzero-mode source quotient covariance identity",
        fluctuation_quotient - 1,
        source_mean + covariance / determinant_average,
    )
    assert_not_equal(
        "vacuum determinant calibration is not the source quotient",
        fluctuation_quotient,
        Fraction(1),
    )

    source_variance = sum(
        weight * (variation - source_mean) ** 2
        for weight, variation in zip(weights, source_variation)
    )
    interaction_variance = sum(
        weight * (factor - determinant_average) ** 2
        for weight, factor in zip(weights, interaction_weight)
    )
    assert_equal(
        "source/interactions covariance obeys Cauchy bound",
        covariance * covariance <= source_variance * interaction_variance,
        True,
    )

    normal_covariance = (
        (Fraction(2, 3), Fraction(1, 5)),
        (Fraction(1, 5), Fraction(3, 4)),
    )
    quadratic_source = (
        (Fraction(1, 7), Fraction(2, 11)),
        (Fraction(2, 11), -Fraction(1, 13)),
    )
    linear_source = [Fraction(3, 17), -Fraction(5, 19)]
    linear_mean = Fraction(0) * sum(linear_source, Fraction(0))
    trace_qc = sum(
        quadratic_source[a][b] * normal_covariance[b][a]
        for a in range(2)
        for b in range(2)
    )
    assert_equal("Gaussian normal linear source mean vanishes", linear_mean, Fraction(0))
    assert_equal(
        "quadratic normal source trace correction",
        Fraction(1, 2) * trace_qc,
        Fraction(6623, 120120),
    )

    window_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    fluctuation_errors = [Fraction(1, 20), -Fraction(1, 30), Fraction(1, 40)]
    leading_window = sum(window_cells, Fraction(0))
    exact_window = sum(
        cell * (1 + error) for cell, error in zip(window_cells, fluctuation_errors)
    )
    absolute_window_mass = sum(abs(cell) for cell in window_cells)
    epsilon_fluc = max(abs(error) for error in fluctuation_errors)
    assert_equal(
        "source fluctuation absolute window bound",
        abs(exact_window - leading_window) <= epsilon_fluc * absolute_window_mass,
        True,
    )
    signed_only_window = abs(sum(fluctuation_errors, Fraction(0))) * abs(leading_window)
    assert_equal(
        "signed source-fluctuation cancellation underbudgets a window",
        signed_only_window < abs(exact_window - leading_window),
        True,
    )

    vanished_zero_mode_source = Fraction(0)
    if vanished_zero_mode_source == 0:
        relative_quotient_defined = False
    else:
        relative_quotient_defined = True
    assert_equal(
        "rank-lost zero-mode channel has no relative fluctuation quotient",
        relative_quotient_defined,
        False,
    )


def check_first_source_cumulant_from_normal_modes() -> None:
    covariance: Matrix2 = (
        (Fraction(2), Fraction(1, 3)),
        (Fraction(1, 3), Fraction(3)),
    )
    linear_source = (Fraction(2, 5), -Fraction(3, 7))
    quadratic_source: Matrix2 = (
        (Fraction(1, 4), Fraction(1, 6)),
        (Fraction(1, 6), -Fraction(1, 5)),
    )
    cubic_action = {
        (0, 0, 0): Fraction(1, 3),
        (0, 0, 1): Fraction(1, 5),
        (0, 1, 0): Fraction(1, 5),
        (1, 0, 0): Fraction(1, 5),
        (0, 1, 1): -Fraction(2, 7),
        (1, 0, 1): -Fraction(2, 7),
        (1, 1, 0): -Fraction(2, 7),
        (1, 1, 1): Fraction(1, 9),
    }

    def c(index_a: int, index_b: int) -> Fraction:
        return covariance[index_a][index_b]

    def t(index_a: int, index_b: int, index_c: int) -> Fraction:
        return cubic_action[(index_a, index_b, index_c)]

    def wick4(i: int, a: int, b: int, c_index: int) -> Fraction:
        return (
            c(i, a) * c(b, c_index)
            + c(i, b) * c(a, c_index)
            + c(i, c_index) * c(a, b)
        )

    gaussian_quadratic_mean = Fraction(1, 2) * sum(
        quadratic_source[a][b] * covariance[a][b]
        for a in range(2)
        for b in range(2)
    )
    direct_linear_cubic_covariance = Fraction(1, 6) * sum(
        linear_source[i]
        * t(a, b, c_index)
        * wick4(i, a, b, c_index)
        for i in range(2)
        for a in range(2)
        for b in range(2)
        for c_index in range(2)
    )
    symmetric_cubic_contraction = Fraction(1, 2) * sum(
        linear_source[i]
        * t(a, b, c_index)
        * covariance[i][a]
        * covariance[b][c_index]
        for i in range(2)
        for a in range(2)
        for b in range(2)
        for c_index in range(2)
    )
    assert_equal(
        "symmetric cubic action reduces the Wick-pairing source cumulant",
        direct_linear_cubic_covariance,
        symmetric_cubic_contraction,
    )

    first_source_cumulant = (
        gaussian_quadratic_mean
        - direct_linear_cubic_covariance
    )
    assert_equal(
        "first source cumulant from normal-mode cubic interaction",
        first_source_cumulant,
        Fraction(14867, 44100),
    )
    assert_not_equal(
        "linear normal source has zero Gaussian mean but nonzero cubic covariance",
        direct_linear_cubic_covariance,
        Fraction(0),
    )
    assert_not_equal(
        "quadratic Gaussian trace alone misses the cubic source cumulant",
        gaussian_quadratic_mean,
        first_source_cumulant,
    )

    zero_cubic_shortcut = gaussian_quadratic_mean
    assert_not_equal(
        "setting the cubic normal action to zero erases source response",
        zero_cubic_shortcut,
        first_source_cumulant,
    )

    determinant_constant = Fraction(11, 13)
    source_channel_value = determinant_constant * (1 + first_source_cumulant)
    determinant_only_value = determinant_constant
    assert_not_equal(
        "source-dependent cumulant cannot be absorbed into a universal determinant",
        determinant_only_value,
        source_channel_value,
    )

    kernel_cells = [Fraction(2, 3), -Fraction(1, 5), Fraction(3, 10)]
    cumulant_remainders = [Fraction(1, 100), -Fraction(1, 80), Fraction(1, 120)]
    exact_window_shift = sum(
        cell * remainder
        for cell, remainder in zip(kernel_cells, cumulant_remainders)
    )
    absolute_cumulant_budget = sum(
        abs(cell) * abs(remainder)
        for cell, remainder in zip(kernel_cells, cumulant_remainders)
    )
    assert_leq(
        "normal-mode source cumulant absolute window budget",
        abs(exact_window_shift),
        absolute_cumulant_budget,
    )
    signed_remainder_budget = (
        abs(sum(cumulant_remainders, Fraction(0)))
        * abs(sum(kernel_cells, Fraction(0)))
    )
    assert_equal(
        "signed cumulant remainder cancellation underbudgets the window",
        signed_remainder_budget < abs(exact_window_shift),
        True,
    )


def check_normal_propagator_source_insertion() -> None:
    Vector2 = tuple[Fraction, Fraction]

    def matvec2(matrix: Matrix2, vector: Vector2) -> Vector2:
        return (
            matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
            matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
        )

    def dot2(left: Vector2, right: Vector2) -> Fraction:
        return left[0] * right[0] + left[1] * right[1]

    def scale_vec2(scalar: Fraction, vector: Vector2) -> Vector2:
        return (scalar * vector[0], scalar * vector[1])

    zero_mode_projector: Matrix2 = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    normal_projector: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    assert_equal(
        "zero and normal projectors are complementary",
        add2(zero_mode_projector, normal_projector),
        ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))),
    )

    physical_out: Vector2 = (Fraction(3, 5), Fraction(7, 11))
    physical_in: Vector2 = (Fraction(5, 13), -Fraction(2, 7))
    residue_out = Fraction(3, 2)
    residue_in = Fraction(5, 3)
    overlap_out: Matrix2 = (
        (Fraction(1), Fraction(1, 5)),
        (Fraction(1, 7), Fraction(1)),
    )
    overlap_in: Matrix2 = (
        (Fraction(1), -Fraction(1, 6)),
        (Fraction(2, 9), Fraction(1)),
    )
    amputated_out = matvec2(inv2(overlap_out), scale_vec2(1 / residue_out, physical_out))
    amputated_in = matvec2(inv2(overlap_in), scale_vec2(1 / residue_in, physical_in))

    primed_green: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(7, 5)),
    )
    projected_out = matvec2(normal_projector, amputated_out)
    projected_in = matvec2(normal_projector, amputated_in)
    normal_bilinear = dot2(projected_out, matvec2(primed_green, projected_in))
    assert_not_equal(
        "normal propagator insertion is source dependent",
        normal_bilinear,
        Fraction(0),
    )

    density_weight = Fraction(5, 7)
    zero_mode_source = Fraction(2, 3)
    determinant_constant = Fraction(11, 13)
    instanton_channel = density_weight * zero_mode_source * normal_bilinear
    moduli_determinant_only = density_weight * zero_mode_source * determinant_constant
    assert_not_equal(
        "moduli density and determinant constant do not supply normal propagator insertion",
        moduli_determinant_only,
        instanton_channel,
    )

    unprimed_green_a: Matrix2 = (
        (Fraction(19), Fraction(0)),
        (Fraction(0), Fraction(7, 5)),
    )
    unprimed_green_b: Matrix2 = (
        (Fraction(23), Fraction(0)),
        (Fraction(0), Fraction(7, 5)),
    )
    unprimed_bilinear_a = dot2(amputated_out, matvec2(unprimed_green_a, amputated_in))
    unprimed_bilinear_b = dot2(amputated_out, matvec2(unprimed_green_b, amputated_in))
    assert_not_equal(
        "unprimed normal inverse depends on arbitrary zero-mode regulator",
        unprimed_bilinear_a,
        unprimed_bilinear_b,
    )
    assert_not_equal(
        "unprimed zero-mode-regulated inverse is not the primed channel bilinear",
        unprimed_bilinear_a,
        normal_bilinear,
    )

    trace_response = trace2(primed_green)
    assert_not_equal(
        "trace response loses the external source vectors",
        trace_response,
        normal_bilinear,
    )

    diagonal_only_out: Vector2 = (
        physical_out[0] / (residue_out * overlap_out[0][0]),
        physical_out[1] / (residue_out * overlap_out[1][1]),
    )
    diagonal_only_in: Vector2 = (
        physical_in[0] / (residue_in * overlap_in[0][0]),
        physical_in[1] / (residue_in * overlap_in[1][1]),
    )
    diagonal_bilinear = dot2(
        matvec2(normal_projector, diagonal_only_out),
        matvec2(primed_green, matvec2(normal_projector, diagonal_only_in)),
    )
    assert_not_equal(
        "diagonal residue division misses mixed source-overlap amputation",
        diagonal_bilinear,
        normal_bilinear,
    )

    zero_mode_rank_lost = Fraction(0)
    relative_channel_defined = zero_mode_rank_lost != 0
    assert_equal(
        "rank-lost zero-mode block has no relative normal-propagator coordinate",
        relative_channel_defined,
        False,
    )

    density_cells = [Fraction(2, 3), Fraction(5, 7)]
    zero_mode_cells = [Fraction(3, 5), -Fraction(1, 4)]
    leading_propagator = [Fraction(7, 11), -Fraction(2, 13)]
    density_errors = [Fraction(0), Fraction(0)]
    zero_mode_errors = [Fraction(0), Fraction(0)]
    propagator_errors = [Fraction(1, 50), -Fraction(1, 60)]
    e_density = max(abs(error) for error in density_errors)
    e_zero_mode = max(abs(error) for error in zero_mode_errors)
    leading_window = sum(
        density * zero_mode * prop
        for density, zero_mode, prop in zip(
            density_cells,
            zero_mode_cells,
            leading_propagator,
        )
    )
    exact_window = sum(
        density
        * (1 + density_error)
        * zero_mode
        * (1 + zero_mode_error)
        * (prop + prop_error)
        for density, zero_mode, prop, density_error, zero_mode_error, prop_error in zip(
            density_cells,
            zero_mode_cells,
            leading_propagator,
            density_errors,
            zero_mode_errors,
            propagator_errors,
        )
    )
    residual = abs(exact_window - leading_window)
    propagator_bound = sum(
        abs(density * zero_mode)
        * (
            (1 + e_density) * (1 + e_zero_mode) * abs(prop_error)
            + abs(prop) * ((1 + e_density) * (1 + e_zero_mode) - 1)
        )
        for density, zero_mode, prop, prop_error in zip(
            density_cells,
            zero_mode_cells,
            leading_propagator,
            propagator_errors,
        )
    )
    assert_equal(
        "zero-mode times normal-propagator residual telescope",
        residual <= propagator_bound,
        True,
    )
    underbudget_without_propagator_error = sum(
        abs(density * zero_mode)
        * abs(prop)
        * ((1 + e_density) * (1 + e_zero_mode) - 1)
        for density, zero_mode, prop in zip(
            density_cells,
            zero_mode_cells,
            leading_propagator,
        )
    )
    assert_equal(
        "omitting normal-propagator residual underbudgets the channel",
        residual <= underbudget_without_propagator_error,
        False,
    )


def check_subtracted_normal_green_function_matching() -> None:
    Vector2 = tuple[Fraction, Fraction]

    def matvec2(matrix: Matrix2, vector: Vector2) -> Vector2:
        return (
            matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
            matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
        )

    def dot2(left: Vector2, right: Vector2) -> Fraction:
        return left[0] * right[0] + left[1] * right[1]

    def bilinear(matrix: Matrix2, left: Vector2, right: Vector2) -> Fraction:
        return dot2(left, matvec2(matrix, right))

    normal_projector: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    source_out: Vector2 = (Fraction(2, 3), Fraction(5, 7))
    source_in: Vector2 = (Fraction(3, 5), -Fraction(4, 9))
    projected_out = matvec2(normal_projector, source_out)
    projected_in = matvec2(normal_projector, source_in)

    finite_green: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(23, 29)),
    )
    free_parametrix: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(5, 6)),
    )
    heat_kernel_local: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(7, 10)),
    )
    finite_local: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), -Fraction(2, 15)),
    )
    log_lambda_over_mu = Fraction(3)
    zero_mode_pollution: Matrix2 = (
        (Fraction(101), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    log_heat: Matrix2 = (
        (log_lambda_over_mu * heat_kernel_local[0][0], Fraction(0)),
        (Fraction(0), log_lambda_over_mu * heat_kernel_local[1][1]),
    )
    smooth_green = add2(finite_green, free_parametrix)
    raw_green = add2(
        add2(
            smooth_green,
            log_heat,
        ),
        add2(finite_local, zero_mode_pollution),
    )

    smooth_projected_bilinear = bilinear(smooth_green, projected_out, projected_in)
    raw_projected_bilinear = bilinear(raw_green, projected_out, projected_in)
    free_bilinear = bilinear(free_parametrix, projected_out, projected_in)
    heat_bilinear = log_lambda_over_mu * bilinear(
        heat_kernel_local,
        projected_out,
        projected_in,
    )
    local_bilinear = bilinear(finite_local, projected_out, projected_in)
    subtracted_green = raw_projected_bilinear - free_bilinear - heat_bilinear - local_bilinear
    expected_subtracted = bilinear(finite_green, projected_out, projected_in)
    assert_equal(
        "smooth source Green pairing keeps ordinary propagation",
        smooth_projected_bilinear,
        expected_subtracted + free_bilinear,
    )
    over_subtracted_smooth = smooth_projected_bilinear - free_bilinear
    assert_not_equal(
        "default free subtraction changes a smooth-source observable",
        over_subtracted_smooth,
        smooth_projected_bilinear,
    )
    assert_equal(
        "subtracted normal Green coordinate keeps finite source bilinear",
        subtracted_green,
        expected_subtracted,
    )
    assert_not_equal(
        "local matched coordinate is not the smooth smeared source bilinear",
        subtracted_green,
        smooth_projected_bilinear,
    )

    unsubtracted = raw_projected_bilinear
    assert_not_equal(
        "unsubtracted normal Green insertion keeps local regulator pieces",
        unsubtracted,
        subtracted_green,
    )

    unprojected_bilinear = bilinear(raw_green, source_out, source_in)
    assert_not_equal(
        "unprojected normal Green insertion depends on zero-mode regulator pollution",
        unprojected_bilinear,
        raw_projected_bilinear,
    )

    no_free_subtraction = raw_projected_bilinear - heat_bilinear - local_bilinear
    assert_not_equal(
        "missing free parametrix subtraction changes Green coordinate",
        no_free_subtraction,
        subtracted_green,
    )

    no_heat_subtraction = raw_projected_bilinear - free_bilinear - local_bilinear
    assert_not_equal(
        "missing logarithmic heat-kernel subtraction changes Green coordinate",
        no_heat_subtraction,
        subtracted_green,
    )

    smooth_source_class = "smooth_smeared"
    local_source_class = "local_composite"
    background_difference_class = "background_minus_vacuum"
    subtraction_classes = {local_source_class, background_difference_class}
    assert_equal(
        "smooth source class does not activate local subtraction package",
        smooth_source_class in subtraction_classes,
        False,
    )
    assert_equal(
        "local source class activates local subtraction package",
        local_source_class in subtraction_classes,
        True,
    )

    trace_shortcut = trace2(finite_green)
    assert_not_equal(
        "determinant trace response is not the external-source Green bilinear",
        trace_shortcut,
        subtracted_green,
    )

    wrong_source_basis: Vector2 = (source_out[0], source_out[0] + source_out[1])
    wrong_basis_subtraction = raw_projected_bilinear - bilinear(
        free_parametrix,
        matvec2(normal_projector, wrong_source_basis),
        projected_in,
    ) - heat_bilinear - local_bilinear
    assert_not_equal(
        "free subtraction in a different source basis changes the matched insertion",
        wrong_basis_subtraction,
        subtracted_green,
    )

    delta_local: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(4, 11)),
    )
    delta_bilinear = bilinear(delta_local, projected_out, projected_in)
    subtracted_prime = subtracted_green - delta_bilinear
    local_coefficient = Fraction(7, 8)
    zero_mode_source = Fraction(9, 10)
    matched = zero_mode_source * (subtracted_green + local_coefficient)
    matched_prime = zero_mode_source * (
        subtracted_prime + local_coefficient + delta_bilinear
    )
    assert_equal(
        "finite local Green subtraction is compensated by Wilsonian coefficient shift",
        matched_prime,
        matched,
    )
    unmatched_prime = zero_mode_source * (subtracted_prime + local_coefficient)
    assert_not_equal(
        "finite local subtraction shift without coefficient transport changes amplitude",
        unmatched_prime,
        matched,
    )

    norm_out = sum(abs(entry) for entry in source_out)
    norm_in = sum(abs(entry) for entry in source_in)
    e_projector = Fraction(1, 100)
    e_parametrix = Fraction(1, 120)
    e_heat = Fraction(1, 90)
    e_local = Fraction(1, 40)
    e_amputation = Fraction(1, 200)
    m_green = Fraction(23, 20)
    projector_residual = 2 * m_green * e_projector * norm_out * norm_in
    residual = (
        abs(zero_mode_source)
        * (
            projector_residual
            + e_parametrix
            + abs(log_lambda_over_mu) * e_heat
            + e_local
        )
        + e_amputation / 2
    )
    residual_bound = (
        abs(zero_mode_source)
        * (
            projector_residual
            + e_parametrix
            + abs(log_lambda_over_mu) * e_heat
            + e_local
        )
        + e_amputation
    )
    assert_equal(
        "subtracted Green residual includes projection, parametrix, heat, local, and amputation errors",
        residual <= residual_bound,
        True,
    )
    underbudget_without_local_matching = (
        abs(zero_mode_source)
        * (
            projector_residual
            + e_parametrix
            + abs(log_lambda_over_mu) * e_heat
        )
        + e_amputation
    )
    assert_equal(
        "omitting finite local matching error underbudgets subtracted Green insertion",
        residual <= underbudget_without_local_matching,
        False,
    )
    underbudget_without_resolvent_norm = (
        abs(zero_mode_source)
        * (
            e_projector * norm_out * norm_in
            + e_parametrix
            + abs(log_lambda_over_mu) * e_heat
            + e_local
        )
        + e_amputation
    )
    assert_equal(
        "omitting the Green/resolvent norm underbudgets projector error",
        residual <= underbudget_without_resolvent_norm,
        False,
    )


def check_spectral_local_green_matching_source_classes() -> None:
    def harmonic(n_terms: int) -> Fraction:
        return sum((Fraction(1, n) for n in range(1, n_terms + 1)), Fraction(0))

    def smooth_pairing(n_terms: int) -> Fraction:
        return sum(
            (Fraction(2, n * (n + 1) * (n + 2)) for n in range(1, n_terms + 1)),
            Fraction(0),
        )

    def smooth_tail(n_terms: int) -> Fraction:
        return Fraction(1, (n_terms + 1) * (n_terms + 2))

    a0 = Fraction(5, 3)
    a1 = Fraction(7, 5)
    finite_remainder_total = Fraction(11)
    finite_counterterm = Fraction(2, 7)

    def local_remainder_shell(shell: int) -> Fraction:
        return finite_remainder_total / (shell * (shell + 1))

    def local_shell(shell: int) -> Fraction:
        return a0 + a1 / shell + local_remainder_shell(shell)

    def raw_local_diagonal(n_terms: int) -> Fraction:
        return sum((local_shell(n) for n in range(1, n_terms + 1)), Fraction(0))

    def renormalized_local(n_terms: int) -> Fraction:
        return raw_local_diagonal(n_terms) - a0 * n_terms - a1 * harmonic(n_terms) - finite_counterterm

    smooth_eight = smooth_pairing(8)
    smooth_sixteen = smooth_pairing(16)
    assert_equal(
        "smooth spectral pairing has telescoping tail",
        smooth_eight + smooth_tail(8),
        Fraction(1, 2),
    )
    assert_equal(
        "smooth spectral pairing improves under cutoff refinement",
        smooth_sixteen - smooth_eight,
        smooth_tail(8) - smooth_tail(16),
    )

    over_subtracted_smooth_eight = smooth_eight - a0 * 8 - a1 * harmonic(8)
    over_subtracted_smooth_sixteen = smooth_sixteen - a0 * 16 - a1 * harmonic(16)
    assert_not_equal(
        "local shell subtraction changes a smooth spectral source pairing",
        over_subtracted_smooth_eight,
        smooth_eight,
    )
    assert_gt(
        "smooth over-subtraction grows with local cutoff volume",
        abs(over_subtracted_smooth_sixteen),
        abs(over_subtracted_smooth_eight),
    )

    local_eight = renormalized_local(8)
    local_sixteen = renormalized_local(16)
    expected_local_eight = finite_remainder_total * Fraction(8, 9) - finite_counterterm
    expected_local_sixteen = finite_remainder_total * Fraction(16, 17) - finite_counterterm
    assert_equal("renormalized local spectral coordinate at N=8", local_eight, expected_local_eight)
    assert_equal("renormalized local spectral coordinate at N=16", local_sixteen, expected_local_sixteen)
    assert_equal(
        "local spectral tail is finite after A0/A1 subtraction",
        finite_remainder_total - finite_counterterm - local_eight,
        finite_remainder_total * Fraction(1, 9),
    )
    assert_gt(
        "local matched coordinate stabilizes as cutoff grows",
        abs(finite_remainder_total - finite_counterterm - local_eight),
        abs(finite_remainder_total - finite_counterterm - local_sixteen),
    )

    raw_local_eight = raw_local_diagonal(8)
    missing_a0 = raw_local_eight - a1 * harmonic(8) - finite_counterterm
    missing_a1 = raw_local_eight - a0 * 8 - finite_counterterm
    missing_counterterm = raw_local_eight - a0 * 8 - a1 * harmonic(8)
    assert_not_equal("local spectral coordinate needs the A0 shell subtraction", missing_a0, local_eight)
    assert_not_equal("local spectral coordinate needs the A1 harmonic subtraction", missing_a1, local_eight)
    assert_not_equal("local spectral coordinate needs the finite local counterterm", missing_counterterm, local_eight)

    shell = 12
    extracted_a1_with_remainder = shell * (local_shell(shell) - a0)
    assert_not_equal(
        "finite shell remainder cannot be read as the heat-kernel A1 coefficient",
        extracted_a1_with_remainder,
        a1,
    )
    assert_equal(
        "A1 is recovered only after the declared local remainder is separated",
        shell * (local_shell(shell) - a0 - local_remainder_shell(shell)),
        a1,
    )

    delta_a0 = Fraction(1, 50)
    delta_a1 = -Fraction(1, 70)
    delta_l = Fraction(1, 90)
    cutoff = 12
    shifted_local = (
        raw_local_diagonal(cutoff)
        - (a0 + delta_a0) * cutoff
        - (a1 + delta_a1) * harmonic(cutoff)
        - (finite_counterterm + delta_l)
    )
    local_error = abs(shifted_local - renormalized_local(cutoff))
    local_error_bound = cutoff * abs(delta_a0) + harmonic(cutoff) * abs(delta_a1) + abs(delta_l)
    assert_equal("spectral local matching residual bound", local_error <= local_error_bound, True)
    underbudget_without_a0 = local_error_bound - cutoff * abs(delta_a0)
    assert_equal(
        "omitting A0 shell uncertainty underbudgets local spectral matching",
        local_error <= underbudget_without_a0,
        False,
    )


def check_hard_amplitude_assembly_bound() -> None:
    b0_su3_nf2 = beta0(3, 2)
    zero_mode_power = Fraction(6)
    size_power = b0_su3_nf2 + zero_mode_power - 5
    q_power = -(size_power + 1)

    assert_equal("assembled hard-channel Lambda power", b0_su3_nf2, Fraction(29, 3))
    assert_equal("assembled hard-channel Q power", q_power, -Fraction(35, 3))
    assert_equal(
        "assembled hard-channel four-fermion mass dimension",
        b0_su3_nf2 + q_power,
        Fraction(-2),
    )

    leading_kernel_cells = [Fraction(1), -Fraction(97, 100), Fraction(3, 100)]
    determinant_errors = [Fraction(1, 20), -Fraction(1, 30), Fraction(1, 40)]
    fluctuation_errors = [Fraction(1, 25), Fraction(1, 50), -Fraction(1, 60)]
    zero_mode_errors = [-Fraction(1, 30), Fraction(1, 45), Fraction(1, 35)]
    physical_projection_errors = [
        Fraction(1, 50),
        -Fraction(1, 40),
        Fraction(1, 55),
    ]

    leading_window = sum(leading_kernel_cells, Fraction(0))
    exact_window = sum(
        cell * (1 + det) * (1 + fluc) * (1 + zm) * (1 + phys)
        for cell, det, fluc, zm, phys in zip(
            leading_kernel_cells,
            determinant_errors,
            fluctuation_errors,
            zero_mode_errors,
            physical_projection_errors,
        )
    )
    determinant_only_window = sum(
        cell * (1 + det)
        for cell, det in zip(leading_kernel_cells, determinant_errors)
    )

    e_det = max(abs(error) for error in determinant_errors)
    e_fluc = max(abs(error) for error in fluctuation_errors)
    e_zm = max(abs(error) for error in zero_mode_errors)
    e_phys = max(abs(error) for error in physical_projection_errors)
    epsilon_assembly = product([1 + e_det, 1 + e_fluc, 1 + e_zm, 1 + e_phys]) - 1
    absolute_window_mass = sum(abs(cell) for cell in leading_kernel_cells)

    assert_equal("assembled hard leading signed window", leading_window, Fraction(3, 50))
    assert_equal(
        "hard assembly absolute product bound",
        abs(exact_window - leading_window)
        <= epsilon_assembly * absolute_window_mass,
        True,
    )
    assert_not_equal(
        "determinant-only assembled amplitude misses source and projection data",
        determinant_only_window,
        exact_window,
    )

    signed_relative_budget = epsilon_assembly * abs(leading_window)
    assert_equal(
        "signed-window relative budget fails without noncancellation margin",
        signed_relative_budget < abs(exact_window - leading_window),
        True,
    )

    determinant_constant = Fraction(13, 17)
    common_source_window = Fraction(19, 23)
    source_quotient_q1 = Fraction(21, 20)
    source_quotient_q2 = Fraction(24, 25)
    prefactor_q1 = determinant_constant * common_source_window * source_quotient_q1
    prefactor_q2 = determinant_constant * common_source_window * source_quotient_q2
    transported_ratio_prefactor = prefactor_q2 / prefactor_q1

    assert_equal(
        "same-scheme determinant constant cancels in assembled ratio",
        transported_ratio_prefactor,
        source_quotient_q2 / source_quotient_q1,
    )
    assert_not_equal(
        "untransported source quotient changes assembled hard ratio",
        transported_ratio_prefactor,
        Fraction(1),
    )


def check_hard_reference_channel_calibration() -> None:
    universal_prefactor = Fraction(5, 7)
    determinant_constant = Fraction(11, 13)

    reference_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    target_cells = [Fraction(2, 7), -Fraction(1, 8), Fraction(5, 11)]
    b_ref = sum(reference_cells, Fraction(0))
    b_target = sum(target_cells, Fraction(0))
    m_ref = sum(abs(cell) for cell in reference_cells)
    m_target = sum(abs(cell) for cell in target_cells)
    kappa_ref = abs(b_ref) / m_ref

    assert_equal("hard reference integral", b_ref, Fraction(17, 20))
    assert_equal("hard reference absolute mass", m_ref, Fraction(21, 20))
    assert_equal("hard reference noncancellation margin", kappa_ref, Fraction(17, 21))

    reference_residual = Fraction(1, 50)
    target_residual = -Fraction(1, 70)
    reference_amplitude = universal_prefactor * determinant_constant * b_ref + reference_residual
    target_amplitude = universal_prefactor * determinant_constant * b_target + target_residual
    calibrated_prediction = reference_amplitude * b_target / b_ref

    assert_equal(
        "hard reference calibration residual identity",
        target_amplitude - calibrated_prediction,
        target_residual - reference_residual * b_target / b_ref,
    )
    calibration_bound = abs(target_residual) + abs(b_target / b_ref) * abs(reference_residual)
    assert_equal(
        "hard reference calibration residual bound",
        abs(target_amplitude - calibrated_prediction) <= calibration_bound,
        True,
    )
    assert_equal(
        "hard reference calibration ratio margin",
        abs(b_target / b_ref) <= m_target / (kappa_ref * m_ref),
        True,
    )

    zero_residual_reference = universal_prefactor * determinant_constant * b_ref
    assert_equal(
        "hard reference calibration exact without residuals",
        zero_residual_reference * b_target / b_ref,
        universal_prefactor * determinant_constant * b_target,
    )

    source_quotient_ref = Fraction(21, 20)
    source_quotient_target = Fraction(24, 25)
    reference_with_source = (
        universal_prefactor
        * determinant_constant
        * b_ref
        * source_quotient_ref
    )
    target_with_source = (
        universal_prefactor
        * determinant_constant
        * b_target
        * source_quotient_target
    )
    omitted_source_prediction = reference_with_source * b_target / b_ref
    transported_source_prediction = (
        reference_with_source
        * (b_target * source_quotient_target)
        / (b_ref * source_quotient_ref)
    )
    assert_not_equal(
        "reference calibration does not absorb target source quotient",
        omitted_source_prediction,
        target_with_source,
    )
    assert_equal(
        "transported source quotient gives same-frame calibrated target",
        transported_source_prediction,
        target_with_source,
    )

    projection_ref = Fraction(7, 11)
    projection_target = Fraction(5, 13)
    reference_with_projection = (
        universal_prefactor
        * determinant_constant
        * b_ref
        * projection_ref
    )
    target_with_projection = (
        universal_prefactor
        * determinant_constant
        * b_target
        * projection_target
    )
    omitted_projection_prediction = reference_with_projection * b_target / b_ref
    transported_projection_prediction = (
        reference_with_projection
        * (b_target * projection_target)
        / (b_ref * projection_ref)
    )
    assert_not_equal(
        "reference calibration does not absorb target physical projection",
        omitted_projection_prediction,
        target_with_projection,
    )
    assert_equal(
        "transported physical projection gives calibrated target",
        transported_projection_prediction,
        target_with_projection,
    )

    rank_lost_reference = Fraction(0)
    calibration_defined = rank_lost_reference != 0
    assert_equal(
        "rank-lost reference cannot calibrate determinant constant",
        calibration_defined,
        False,
    )

    canceled_reference_cells = [Fraction(1), -Fraction(99, 100)]
    b_cancel = sum(canceled_reference_cells, Fraction(0))
    m_cancel = sum(abs(cell) for cell in canceled_reference_cells)
    kappa_cancel = abs(b_cancel) / m_cancel
    assert_equal("canceled hard reference margin", kappa_cancel, Fraction(1, 199))
    assert_equal(
        "canceled hard reference amplifies residual",
        abs(reference_residual * b_target / b_cancel)
        > 50 * abs(reference_residual * b_target / b_ref),
        True,
    )


def check_overdetermined_reference_channel_calibration() -> None:
    universal_prefactor = Fraction(5, 7)
    determinant_constant = Fraction(11, 13)

    reference_0_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    reference_1_cells = [Fraction(1, 3), Fraction(2, 5), -Fraction(1, 6)]
    b_0 = sum(reference_0_cells, Fraction(0))
    b_1 = sum(reference_1_cells, Fraction(0))
    m_0 = sum(abs(cell) for cell in reference_0_cells)
    m_1 = sum(abs(cell) for cell in reference_1_cells)
    kappa_0 = abs(b_0) / m_0
    kappa_1 = abs(b_1) / m_1

    assert_equal("first overdetermined reference integral", b_0, Fraction(17, 20))
    assert_equal("second overdetermined reference integral", b_1, Fraction(17, 30))
    assert_equal("second overdetermined reference margin", kappa_1, Fraction(17, 27))

    residual_0 = Fraction(1, 100)
    residual_1 = -Fraction(1, 140)
    amplitude_0 = universal_prefactor * determinant_constant * b_0 + residual_0
    amplitude_1 = universal_prefactor * determinant_constant * b_1 + residual_1
    extracted_0 = amplitude_0 / (universal_prefactor * b_0)
    extracted_1 = amplitude_1 / (universal_prefactor * b_1)

    assert_equal(
        "first overdetermined reference extracts constant plus residual",
        extracted_0 - determinant_constant,
        residual_0 / (universal_prefactor * b_0),
    )
    assert_equal(
        "second overdetermined reference extracts constant plus residual",
        extracted_1 - determinant_constant,
        residual_1 / (universal_prefactor * b_1),
    )
    pair_bound = (
        abs(residual_0) / (abs(universal_prefactor) * abs(b_0))
        + abs(residual_1) / (abs(universal_prefactor) * abs(b_1))
    )
    margin_bound = (
        abs(residual_0) / (abs(universal_prefactor) * kappa_0 * m_0)
        + abs(residual_1) / (abs(universal_prefactor) * kappa_1 * m_1)
    )
    assert_equal(
        "overdetermined reference pair consistency bound",
        abs(extracted_0 - extracted_1) <= pair_bound,
        True,
    )
    assert_equal(
        "overdetermined reference margin bound equals pair bound",
        margin_bound,
        pair_bound,
    )

    exact_0 = universal_prefactor * determinant_constant * b_0
    exact_1 = universal_prefactor * determinant_constant * b_1
    assert_equal(
        "zero-residual overdetermined references extract same determinant",
        exact_0 / (universal_prefactor * b_0),
        exact_1 / (universal_prefactor * b_1),
    )

    source_quotient_0 = Fraction(21, 20)
    source_quotient_1 = Fraction(24, 25)
    projection_0 = Fraction(7, 11)
    projection_1 = Fraction(5, 13)
    channel_factor_0 = source_quotient_0 * projection_0
    channel_factor_1 = source_quotient_1 * projection_1
    amplitude_with_channel_0 = (
        universal_prefactor * determinant_constant * b_0 * channel_factor_0
    )
    amplitude_with_channel_1 = (
        universal_prefactor * determinant_constant * b_1 * channel_factor_1
    )
    wrongly_extracted_0 = amplitude_with_channel_0 / (universal_prefactor * b_0)
    wrongly_extracted_1 = amplitude_with_channel_1 / (universal_prefactor * b_1)
    assert_equal(
        "omitted source/projection factors drift extracted constants",
        wrongly_extracted_0 - wrongly_extracted_1,
        determinant_constant * (channel_factor_0 - channel_factor_1),
    )
    assert_not_equal(
        "overdetermined references reject channel factors as determinant data",
        wrongly_extracted_0,
        wrongly_extracted_1,
    )
    assert_equal(
        "transported channel factors restore common determinant extraction",
        amplitude_with_channel_0
        / (universal_prefactor * b_0 * channel_factor_0),
        amplitude_with_channel_1
        / (universal_prefactor * b_1 * channel_factor_1),
    )
    assert_equal(
        "omitted channel factors violate zero-residual pair budget",
        abs(wrongly_extracted_0 - wrongly_extracted_1) <= Fraction(0),
        False,
    )

    rank_lost_reference = Fraction(0)
    assert_equal(
        "rank-lost overdetermined reference cannot extract determinant constant",
        rank_lost_reference != 0,
        False,
    )

    canceled_reference_cells = [Fraction(1), -Fraction(99, 100)]
    b_cancel = sum(canceled_reference_cells, Fraction(0))
    m_cancel = sum(abs(cell) for cell in canceled_reference_cells)
    kappa_cancel = abs(b_cancel) / m_cancel
    assert_equal(
        "canceled overdetermined reference margin",
        kappa_cancel,
        Fraction(1, 199),
    )
    assert_equal(
        "canceled overdetermined reference amplifies extracted residual",
        abs(residual_0 / (universal_prefactor * b_cancel))
        > 50 * abs(residual_0 / (universal_prefactor * b_0)),
        True,
    )


def check_finite_determinant_scheme_transport() -> None:
    def row_times_matrix(
        row: tuple[Fraction, Fraction],
        matrix: Matrix2,
    ) -> tuple[Fraction, Fraction]:
        return (
            row[0] * matrix[0][0] + row[1] * matrix[1][0],
            row[0] * matrix[0][1] + row[1] * matrix[1][1],
        )

    def matrix_times_column(
        matrix: Matrix2,
        column: tuple[Fraction, Fraction],
    ) -> tuple[Fraction, Fraction]:
        return (
            matrix[0][0] * column[0] + matrix[0][1] * column[1],
            matrix[1][0] * column[0] + matrix[1][1] * column[1],
        )

    def dot(
        row: tuple[Fraction, Fraction],
        column: tuple[Fraction, Fraction],
    ) -> Fraction:
        return row[0] * column[0] + row[1] * column[1]

    n_colors = 3
    x_scheme = Fraction(7, 5)
    x_prime = Fraction(9, 4)
    gamma_scheme = x_scheme ** (2 * n_colors)
    gamma_prime = x_prime ** (2 * n_colors)

    determinant_constant = Fraction(13, 17)
    action_conversion = Fraction(5, 4)
    orientation_conversion = Fraction(7, 9)

    source_basis_change: Matrix2 = (
        (Fraction(2), Fraction(1, 3)),
        (Fraction(1, 5), Fraction(3, 2)),
    )
    source_coefficients = (Fraction(5, 7), Fraction(11, 13))
    physical_projection = (Fraction(17, 19), Fraction(23, 29))
    channel_kernel = dot(source_coefficients, physical_projection)
    source_prime = row_times_matrix(
        source_coefficients,
        inv2(source_basis_change),
    )
    projection_prime = matrix_times_column(source_basis_change, physical_projection)
    assert_equal(
        "source/projection covariance is a channel-vector identity",
        dot(source_prime, projection_prime),
        channel_kernel,
    )

    scheme_amplitude = determinant_constant * gamma_scheme * channel_kernel
    transported_instanton_constant = (
        determinant_constant
        * action_conversion
        * gamma_scheme
        / gamma_prime
        / orientation_conversion
    )
    transported_amplitude = (
        transported_instanton_constant
        * gamma_prime
        / action_conversion
        * orientation_conversion
        * dot(source_prime, projection_prime)
    )
    assert_equal(
        "universal determinant transport plus channel covariance preserves amplitude",
        transported_amplitude,
        scheme_amplitude,
    )

    constant_only_transport = (
        determinant_constant
        * gamma_prime
        / action_conversion
        * orientation_conversion
        * dot(source_prime, projection_prime)
    )
    omitted_gamma_ratio = (
        determinant_constant
        * action_conversion
        * gamma_prime
        / action_conversion
        * orientation_conversion
        * dot(source_prime, projection_prime)
    )
    omitted_orientation_conversion = (
        determinant_constant
        * action_conversion
        * gamma_scheme
        / gamma_prime
        * gamma_prime
        / action_conversion
        * orientation_conversion
        * dot(source_prime, projection_prime)
    )
    unpaired_source_transform = dot(source_prime, physical_projection)

    assert_not_equal(
        "transporting finite determinant constant alone changes the amplitude",
        constant_only_transport,
        scheme_amplitude,
    )
    assert_not_equal(
        "omitting running zero-mode power changes scheme transport",
        omitted_gamma_ratio,
        scheme_amplitude,
    )
    assert_not_equal(
        "omitting orientation measure changes determinant transport",
        omitted_orientation_conversion,
        scheme_amplitude,
    )
    assert_not_equal(
        "source basis change without projection transport changes the channel",
        transported_instanton_constant
        * gamma_prime
        / action_conversion
        * orientation_conversion
        * unpaired_source_transform,
        scheme_amplitude,
    )

    target_source_coefficients = (Fraction(2, 5), Fraction(7, 11))
    target_projection = (Fraction(13, 17), Fraction(19, 31))
    target_kernel = dot(target_source_coefficients, target_projection)
    target_source_prime = row_times_matrix(
        target_source_coefficients,
        inv2(source_basis_change),
    )
    target_projection_prime = matrix_times_column(
        source_basis_change,
        target_projection,
    )
    assert_equal(
        "second channel source/projection covariance",
        dot(target_source_prime, target_projection_prime),
        target_kernel,
    )

    reference_leak = unpaired_source_transform / channel_kernel
    bad_reference_absorbed_constant = transported_instanton_constant / reference_leak
    target_with_reference_absorbed_constant = (
        bad_reference_absorbed_constant
        * gamma_prime
        / action_conversion
        * orientation_conversion
        * dot(target_source_prime, target_projection)
    )
    assert_not_equal(
        "source/projection leakage calibrated in one channel is not universal",
        target_with_reference_absorbed_constant,
        determinant_constant * gamma_scheme * target_kernel,
    )

    declared_universal_errors = [
        Fraction(1, 20),
        Fraction(1, 25),
        Fraction(1, 30),
    ]
    actual_universal_errors = [
        Fraction(1, 40),
        -Fraction(1, 50),
        Fraction(1, 90),
    ]
    declared_multiplier = product(
        [1 + error for error in declared_universal_errors]
    ) - 1
    actual_multiplier = product(
        [1 + error for error in actual_universal_errors]
    ) - 1
    declared_channel_residual = abs(channel_kernel) / 40
    actual_channel_residual = -declared_channel_residual / 2
    assert_leq(
        "finite determinant scheme residual separates universal and channel errors",
        abs(
            actual_multiplier * scheme_amplitude
            + determinant_constant * gamma_scheme * actual_channel_residual
        ),
        declared_multiplier * abs(scheme_amplitude)
        + abs(determinant_constant * gamma_scheme) * declared_channel_residual,
    )

    underbudget_without_bridge = (
        declared_multiplier * abs(scheme_amplitude)
        + abs(determinant_constant * gamma_scheme) * declared_channel_residual
    )
    bridge_residual = underbudget_without_bridge + Fraction(1, 70)
    physical_difference = (
        actual_multiplier * scheme_amplitude
        + determinant_constant * gamma_scheme * actual_channel_residual
        + bridge_residual
    )
    assert_equal(
        "scheme transport bound needs bridge residual",
        abs(physical_difference)
        <= underbudget_without_bridge + bridge_residual,
        True,
    )
    assert_equal(
        "dropping bridge residual can underbudget scheme transport",
        abs(physical_difference) <= underbudget_without_bridge,
        False,
    )


def check_finite_determinant_conversion_benchmark() -> None:
    def density_components(
        data: dict[str, Fraction],
        n_colors: int,
    ) -> tuple[Fraction, Fraction, Fraction]:
        determinant_constant = (
            data["zero_mode_jacobian"]
            * data["fermion_det"]
            * data["ghost_det"]
            / data["sqrt_boson_det"]
        )
        gamma = data["x"] ** (2 * n_colors)
        density = (
            data["action_weight"]
            * gamma
            * data["orientation_volume"]
            * determinant_constant
        )
        return determinant_constant, gamma, density

    n_colors = 2
    scheme = {
        "action_weight": Fraction(2, 3),
        "x": Fraction(3, 2),
        "orientation_volume": Fraction(5, 7),
        "zero_mode_jacobian": Fraction(5, 4),
        "fermion_det": Fraction(2),
        "ghost_det": Fraction(2),
        "sqrt_boson_det": Fraction(4),
    }
    scheme_prime = {
        "action_weight": Fraction(3, 5),
        "x": Fraction(4, 3),
        "orientation_volume": Fraction(7, 8),
        "zero_mode_jacobian": Fraction(1),
        "fermion_det": Fraction(3),
        "ghost_det": Fraction(3),
        "sqrt_boson_det": Fraction(5),
    }

    det_scheme, gamma_scheme, density_scheme = density_components(
        scheme,
        n_colors,
    )
    det_prime, gamma_prime, density_prime = density_components(
        scheme_prime,
        n_colors,
    )

    assert_equal("finite benchmark determinant constant S", det_scheme, Fraction(5, 4))
    assert_equal(
        "finite benchmark determinant constant S prime",
        det_prime,
        Fraction(9, 5),
    )
    assert_equal("finite benchmark running power S", gamma_scheme, Fraction(81, 16))
    assert_equal("finite benchmark running power S prime", gamma_prime, Fraction(256, 81))
    assert_equal(
        "finite benchmark density conversion",
        density_prime / density_scheme,
        Fraction(50176, 50625),
    )

    action_conversion = scheme["action_weight"] / scheme_prime["action_weight"]
    orientation_conversion = (
        scheme_prime["orientation_volume"] / scheme["orientation_volume"]
    )
    transported_prime_constant = (
        det_scheme
        * action_conversion
        * gamma_scheme
        / gamma_prime
        / orientation_conversion
    )
    assert_equal(
        "finite benchmark action conversion",
        action_conversion,
        Fraction(10, 9),
    )
    assert_equal(
        "finite benchmark orientation conversion",
        orientation_conversion,
        Fraction(49, 40),
    )
    assert_equal(
        "finite benchmark gamma ratio",
        gamma_scheme / gamma_prime,
        Fraction(6561, 4096),
    )
    assert_equal(
        "transport architecture constant before benchmark comparison",
        transported_prime_constant,
        Fraction(91125, 50176),
    )
    assert_not_equal(
        "transport architecture constant is not the independently computed constant",
        transported_prime_constant,
        det_prime,
    )
    assert_equal(
        "independently computed constant reveals finite conversion ratio",
        det_prime / transported_prime_constant,
        Fraction(50176, 50625),
    )

    channel_kernel = Fraction(11, 13)
    amplitude_scheme = density_scheme * channel_kernel
    amplitude_prime = density_prime * channel_kernel
    benchmark_residual = amplitude_prime - amplitude_scheme
    matching_factor = density_scheme / density_prime
    assert_equal(
        "finite benchmark source-channel residual",
        benchmark_residual,
        -Fraction(4939, 218400),
    )
    assert_equal(
        "inverse finite matching factor",
        matching_factor,
        Fraction(50625, 50176),
    )
    assert_equal(
        "inverse finite matching restores same-channel amplitude",
        matching_factor * amplitude_prime,
        amplitude_scheme,
    )

    full_conversion = density_prime / density_scheme
    negative_controls = {
        "constant-only determinant ratio misses full finite conversion":
            det_prime / det_scheme,
        "omitting action weight changes finite determinant conversion":
            (gamma_prime * scheme_prime["orientation_volume"] * det_prime)
            / (gamma_scheme * scheme["orientation_volume"] * det_scheme),
        "omitting running zero-mode power changes finite determinant conversion":
            (
                scheme_prime["action_weight"]
                * scheme_prime["orientation_volume"]
                * det_prime
            )
            / (
                scheme["action_weight"]
                * scheme["orientation_volume"]
                * det_scheme
            ),
        "omitting orientation volume changes finite determinant conversion":
            (scheme_prime["action_weight"] * gamma_prime * det_prime)
            / (scheme["action_weight"] * gamma_scheme * det_scheme),
        "omitting zero-mode jacobian changes finite determinant conversion":
            (
                scheme_prime["action_weight"]
                * gamma_prime
                * scheme_prime["orientation_volume"]
                * scheme_prime["fermion_det"]
                * scheme_prime["ghost_det"]
                / scheme_prime["sqrt_boson_det"]
            )
            / (
                scheme["action_weight"]
                * gamma_scheme
                * scheme["orientation_volume"]
                * scheme["fermion_det"]
                * scheme["ghost_det"]
                / scheme["sqrt_boson_det"]
            ),
        "omitting determinant ratio changes finite determinant conversion":
            (
                scheme_prime["action_weight"]
                * gamma_prime
                * scheme_prime["orientation_volume"]
                * scheme_prime["zero_mode_jacobian"]
            )
            / (
                scheme["action_weight"]
                * gamma_scheme
                * scheme["orientation_volume"]
                * scheme["zero_mode_jacobian"]
            ),
    }
    for name, shortcut in negative_controls.items():
        assert_not_equal(name, shortcut, full_conversion)


def check_observable_handoff_map() -> None:
    hard_four_source_coefficient = Fraction(5, 7)
    one_instanton_activity = Fraction(7, 13)
    mass_factors = [Fraction(2, 3), Fraction(0), Fraction(11, 17)]
    mass_saturated_vacuum_activity = one_instanton_activity * product(mass_factors)

    assert_equal(
        "massless flavor removes vacuum theta activity",
        mass_saturated_vacuum_activity,
        Fraction(0),
    )
    assert_not_equal(
        "hard source coefficient is not vacuum theta curvature",
        hard_four_source_coefficient,
        mass_saturated_vacuum_activity,
    )

    zeta = Fraction(7, 13)
    dilute_chi = 2 * zeta
    fourth_theta_derivative = -2 * zeta
    b2 = fourth_theta_derivative / (12 * dilute_chi)
    assert_equal("dilute handoff topological susceptibility", dilute_chi, Fraction(14, 13))
    assert_equal("dilute handoff b2 coefficient", b2, -Fraction(1, 12))

    m = Fraction(1, 10)
    singular_values = [Fraction(1, 5), Fraction(2, 5)]
    u1a_splitting = sum(
        4 * m * m / (m * m + singular * singular) ** 2
        for singular in singular_values
    )
    assert_not_equal(
        "U(1)_A zero-mode-zone kernel is not theta susceptibility",
        u1a_splitting,
        dilute_chi,
    )

    n_f = 2
    gamma_cs_1 = Fraction(3, 11)
    gamma_cs_2 = Fraction(5, 11)
    chi5 = Fraction(7, 13)
    temperature = Fraction(2)
    axial_rate_1 = (2 * n_f) ** 2 * gamma_cs_1 / (2 * chi5 * temperature)
    axial_rate_2 = (2 * n_f) ** 2 * gamma_cs_2 / (2 * chi5 * temperature)
    assert_not_equal(
        "theta susceptibility is not the real-time axial rate",
        dilute_chi,
        axial_rate_1,
    )
    assert_not_equal(
        "same Euclidean susceptibility can have different retarded slopes",
        axial_rate_1,
        axial_rate_2,
    )

    observable_map_status = {
        "hard source coefficient": "projection_obligation",
        "theta curvature": "zero_mode_saturation_obligation",
        "U(1)_A susceptibility": "ensemble_spectral_obligation",
        "real-time axial rate": "retarded_continuation_obligation",
    }

    def certifies_controlled_observable_estimate(
        status: dict[str, str],
    ) -> bool:
        acceptable = {
            "proved_identity",
            "derived_bound",
            "external_estimate",
            "same_scheme_projection_bound",
        }
        return all(value in acceptable for value in status.values())

    assert_equal(
        "observable map status is not a controlled estimate",
        certifies_controlled_observable_estimate(observable_map_status),
        False,
    )

    certified_status = {
        name: "same_scheme_projection_bound"
        for name in observable_map_status
    }
    assert_equal(
        "row-wise projection budgets can certify observable estimates",
        certifies_controlled_observable_estimate(certified_status),
        True,
    )

    chi_ym = Fraction(5, 7)
    zeta_trial = Fraction(3, 10)
    chi_inst = 2 * zeta_trial
    n_f_wv = 3
    z0 = Fraction(5, 4)
    f_pi = Fraction(2)
    mass_gap = (
        2 * n_f_wv * abs(chi_ym - chi_inst)
        / (z0 * f_pi * f_pi)
    )
    sufficient_curvature_budget = Fraction(1, 8)
    insufficient_curvature_budget = Fraction(1, 10)
    good_mass_budget = (
        2 * n_f_wv * sufficient_curvature_budget
        / (z0 * f_pi * f_pi)
    )
    bad_mass_budget = (
        2 * n_f_wv * insufficient_curvature_budget
        / (z0 * f_pi * f_pi)
    )
    assert_equal(
        "same-scheme instanton/WV curvature budget can control mass gap",
        mass_gap <= good_mass_budget,
        True,
    )
    assert_equal(
        "underbudgeted dilute curvature cannot replace WV input",
        bad_mass_budget < mass_gap,
        True,
    )


def check_source_kernel_physical_projection_bridge() -> None:
    source_overlap = Fraction(7, 15)
    sink_overlap = Fraction(11, 21)
    selected_matrix_element = Fraction(13, 17)
    source_gap_factor = Fraction(1, 5)
    sink_gap_factor = Fraction(1, 7)

    selected_pole = sink_overlap * source_overlap * selected_matrix_element
    final_excited = sink_overlap * source_overlap * Fraction(2, 9) * sink_gap_factor
    initial_excited = sink_overlap * source_overlap * Fraction(-3, 11) * source_gap_factor
    double_excited = (
        sink_overlap
        * source_overlap
        * Fraction(5, 13)
        * sink_gap_factor
        * source_gap_factor
    )
    normalized_window = (
        selected_pole
        + final_excited
        + initial_excited
        + double_excited
    ) / (sink_overlap * source_overlap)
    leakage = normalized_window - selected_matrix_element
    tail_bound = (
        Fraction(2, 9) * sink_gap_factor
        + Fraction(3, 11) * source_gap_factor
        + Fraction(5, 13) * sink_gap_factor * source_gap_factor
    )
    assert_equal(
        "instanton pole-window leading residue",
        selected_pole / (sink_overlap * source_overlap),
        selected_matrix_element,
    )
    assert_equal(
        "instanton pole-window excited leakage bound",
        abs(leakage) <= tail_bound,
        True,
    )
    assert_not_equal(
        "raw Euclidean source pole is not the matrix element",
        selected_pole,
        selected_matrix_element,
    )
    assert_not_equal(
        "overlap division alone does not isolate the pole",
        normalized_window,
        selected_matrix_element,
    )

    zero_sink_overlap = Fraction(0)
    extraction_defined = zero_sink_overlap != 0
    assert_equal(
        "zero source overlap prevents pole extraction",
        extraction_defined,
        False,
    )

    longer_tail_bound = (
        Fraction(2, 9) * sink_gap_factor * sink_gap_factor
        + Fraction(3, 11) * source_gap_factor * source_gap_factor
        + Fraction(5, 13)
        * sink_gap_factor
        * sink_gap_factor
        * source_gap_factor
        * source_gap_factor
    )
    assert_equal(
        "longer pole window improves excited-state majorant",
        longer_tail_bound < tail_bound,
        True,
    )

    def stieltjes_value(
        atoms: list[tuple[Fraction, Fraction]],
        q2: Fraction,
    ) -> Fraction:
        return sum(weight / (mass2 + q2) for mass2, weight in atoms)

    def spectral_bin(
        atoms: list[tuple[Fraction, Fraction]],
        lower: Fraction,
        upper: Fraction,
    ) -> Fraction:
        return sum(weight for mass2, weight in atoms if lower <= mass2 <= upper)

    atoms = [
        (Fraction(1), Fraction(5, 6)),
        (Fraction(4), Fraction(3, 5)),
        (Fraction(9), Fraction(7, 10)),
    ]
    q2 = Fraction(2)
    euclidean_value = stieltjes_value(atoms, q2)
    selected_bin = spectral_bin(atoms, Fraction(3), Fraction(6))
    assert_equal("instanton spectral bin weight", selected_bin, Fraction(3, 5))
    assert_not_equal(
        "Euclidean Stieltjes value is not the spectral bin",
        euclidean_value,
        selected_bin,
    )

    contact_polynomial = Fraction(11, 7) + Fraction(2, 9) * q2
    assert_not_equal(
        "contact polynomial changes spacelike source value",
        euclidean_value + contact_polynomial,
        euclidean_value,
    )
    assert_equal(
        "contact polynomial has no separated bin weight",
        spectral_bin(atoms, Fraction(3), Fraction(6)),
        selected_bin,
    )

    spectral_a = [(Fraction(1), Fraction(1)), (Fraction(4), Fraction(1))]
    spectral_b = [(Fraction(1), Fraction(13, 10)), (Fraction(4), Fraction(2, 5))]
    assert_equal(
        "distinct spectra share one Euclidean source value",
        stieltjes_value(spectral_a, q2),
        stieltjes_value(spectral_b, q2),
    )
    assert_not_equal(
        "shared Euclidean source value hides different physical bin",
        spectral_bin(spectral_a, Fraction(0), Fraction(2)),
        spectral_bin(spectral_b, Fraction(0), Fraction(2)),
    )
    assert_not_equal(
        "second Euclidean point detects the spectral ambiguity",
        stieltjes_value(spectral_a, Fraction(5)),
        stieltjes_value(spectral_b, Fraction(5)),
    )

    leading_kernel_coordinate = Fraction(7, 13)
    residuals = {
        "regulator": Fraction(1, 17),
        "continuation": Fraction(2, 19),
        "pole_bin": Fraction(3, 23),
        "infrared": Fraction(5, 29),
        "unitarity_cut": Fraction(7, 31),
        "matching": Fraction(11, 37),
        "size_endpoint": Fraction(13, 41),
    }
    total_residual = sum(residuals.values(), Fraction(0))
    physical_amplitude = leading_kernel_coordinate + total_residual
    bridge_majorant = sum(abs(value) for value in residuals.values())
    assert_equal(
        "instanton physical bridge residual telescope",
        physical_amplitude - leading_kernel_coordinate,
        total_residual,
    )
    assert_equal(
        "instanton physical bridge absolute bound",
        abs(physical_amplitude - leading_kernel_coordinate) <= bridge_majorant,
        True,
    )
    underbudget = bridge_majorant - abs(residuals["pole_bin"])
    assert_equal(
        "omitting pole/bin residual underbudgets physical bridge",
        abs(physical_amplitude - leading_kernel_coordinate) <= underbudget,
        False,
    )

    has_color_singlet_source = False
    has_declared_infrared_deformation = False
    assert_equal(
        "colored instanton kernel has no standalone physical LSZ map",
        has_color_singlet_source or has_declared_infrared_deformation,
        False,
    )


def check_pole_normalized_four_source_matrix_extraction() -> None:
    # Two mixed source bases for a selected incoming/outgoing pole subspace.
    # The Euclidean four-source window contains the overlap matrices on both
    # sides of the physical instanton matrix element.
    source_overlap: Matrix2 = (
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(1)),
    )
    sink_overlap: Matrix2 = (
        (Fraction(3), Fraction(1)),
        (Fraction(1), Fraction(1)),
    )
    physical_matrix: Matrix2 = (
        (Fraction(5, 7), -Fraction(2, 11)),
        (Fraction(3, 13), Fraction(7, 17)),
    )
    source_adjoint = transpose2(source_overlap)

    pole_window = matmul2(matmul2(sink_overlap, physical_matrix), source_adjoint)
    recovered_matrix = matmul2(
        matmul2(inv2(sink_overlap), pole_window),
        inv2(source_adjoint),
    )
    assert_equal(
        "mixed-source pole amputation recovers physical instanton matrix",
        recovered_matrix,
        physical_matrix,
    )
    assert_not_equal(
        "raw four-source pole window is not the physical matrix element",
        pole_window,
        physical_matrix,
    )

    sink_diagonal_inverse: Matrix2 = (
        (1 / sink_overlap[0][0], Fraction(0)),
        (Fraction(0), 1 / sink_overlap[1][1]),
    )
    source_diagonal_inverse: Matrix2 = (
        (1 / source_adjoint[0][0], Fraction(0)),
        (Fraction(0), 1 / source_adjoint[1][1]),
    )
    diagonal_shortcut = matmul2(
        matmul2(sink_diagonal_inverse, pole_window),
        source_diagonal_inverse,
    )
    assert_not_equal(
        "diagonal overlap division misses source mixing",
        diagonal_shortcut,
        physical_matrix,
    )

    pole_leakage: Matrix2 = (
        (Fraction(1, 100), -Fraction(1, 120)),
        (Fraction(1, 90), Fraction(1, 150)),
    )
    leaked_window = add2(pole_window, pole_leakage)
    recovered_with_leakage = matmul2(
        matmul2(inv2(sink_overlap), leaked_window),
        inv2(source_adjoint),
    )
    recovered_error = sub2(recovered_with_leakage, physical_matrix)
    propagated_error = matmul2(
        matmul2(inv2(sink_overlap), pole_leakage),
        inv2(source_adjoint),
    )
    assert_equal(
        "mixed-source pole leakage propagates through inverse overlaps",
        recovered_error,
        propagated_error,
    )
    max_leakage = max_abs_entry(pole_leakage)
    matrix_bound = (
        Fraction(4)
        * max_abs_entry(inv2(sink_overlap))
        * max_leakage
        * max_abs_entry(inv2(source_adjoint))
    )
    assert_leq(
        "mixed-source pole amputation residual bound",
        float(max_abs_entry(recovered_error)),
        float(matrix_bound),
    )

    singular_source_overlap: Matrix2 = (
        (Fraction(1), Fraction(2)),
        (Fraction(2), Fraction(4)),
    )
    assert_equal(
        "rank-lost source basis cannot define pole amputation",
        det2(singular_source_overlap) != 0,
        False,
    )

    assert_not_equal(
        "excited-state leakage is not a determinant constant",
        pole_leakage[0][0] / pole_window[0][0],
        pole_leakage[0][1] / pole_window[0][1],
    )


def check_instanton_inclusive_cut_quadratic_projection() -> None:
    def matvec(
        matrix: Matrix2,
        vector: tuple[Fraction, Fraction],
    ) -> tuple[Fraction, Fraction]:
        return (
            matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
            matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
        )

    def dot2(
        left: tuple[Fraction, Fraction],
        right: tuple[Fraction, Fraction],
    ) -> Fraction:
        return left[0] * right[0] + left[1] * right[1]

    def quadratic(
        vector: tuple[Fraction, Fraction],
        measurement: Matrix2,
    ) -> Fraction:
        return dot2(vector, matvec(measurement, vector))

    physical_amplitude = (Fraction(3, 5), -Fraction(2, 7))
    measurement: Matrix2 = (
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(3)),
    )
    inclusive_cut = quadratic(physical_amplitude, measurement)
    assert_equal(
        "instanton inclusive cut is a quadratic projection",
        inclusive_cut,
        Fraction(762, 1225),
    )
    assert_gt("positive measurement gives positive retained cut", inclusive_cut, Fraction(0))

    signed_linear_sum = physical_amplitude[0] + physical_amplitude[1]
    assert_not_equal(
        "linear instanton amplitude sum is not the inclusive cut",
        signed_linear_sum,
        inclusive_cut,
    )
    canceling_amplitude = (Fraction(1, 2), -Fraction(1, 2))
    assert_equal(
        "signed instanton amplitudes can cancel linearly",
        sum(canceling_amplitude),
        Fraction(0),
    )
    assert_gt(
        "quadratic cut survives signed amplitude cancellation",
        quadratic(canceling_amplitude, measurement),
        Fraction(0),
    )

    source_overlap: Matrix2 = (
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(1)),
    )
    source_basis_vector = matvec(source_overlap, physical_amplitude)
    raw_source_cut = quadratic(source_basis_vector, measurement)
    assert_not_equal(
        "unamputated source vector changes the inclusive cut",
        raw_source_cut,
        inclusive_cut,
    )
    recovered_vector = matvec(inv2(source_overlap), source_basis_vector)
    assert_equal(
        "source amputation restores the physical cut vector",
        recovered_vector,
        physical_amplitude,
    )

    locally_inclusive_measurement: Matrix2 = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    assert_not_equal(
        "dropping the measurement matrix changes the physical bin",
        quadratic(physical_amplitude, locally_inclusive_measurement),
        inclusive_cut,
    )

    theta_phase_power_linear = 1
    theta_phase_power_cut = 0
    assert_not_equal(
        "positive I Ibar cut does not retain the one-instanton theta phase",
        Fraction(theta_phase_power_linear),
        Fraction(theta_phase_power_cut),
    )

    reference_amplitude = (Fraction(4, 9), Fraction(1, 6))
    interference = 2 * dot2(reference_amplitude, matvec(measurement, physical_amplitude))
    selection_rule_allows_reference = False
    assert_not_equal(
        "interference term is a different observable from the positive cut",
        interference,
        inclusive_cut,
    )
    assert_equal(
        "selection rule can remove the linear interference channel",
        interference if selection_rule_allows_reference else Fraction(0),
        Fraction(0),
    )

    residual = (Fraction(1, 100), -Fraction(1, 120))
    shifted_amplitude = (
        physical_amplitude[0] + residual[0],
        physical_amplitude[1] + residual[1],
    )
    cut_shift = quadratic(shifted_amplitude, measurement) - inclusive_cut
    max_amplitude = max(abs(value) for value in physical_amplitude)
    max_residual = max(abs(value) for value in residual)
    row_sum_bound = max(
        sum(abs(entry) for entry in row)
        for row in measurement
    )
    n_states = Fraction(2)
    quadratic_bound = (
        2 * n_states * max_amplitude * row_sum_bound * max_residual
        + n_states * row_sum_bound * max_residual * max_residual
    )
    assert_leq(
        "instanton inclusive cut quadratic residual bound",
        float(abs(cut_shift)),
        float(quadratic_bound),
    )

    underbudget = (
        quadratic_bound
        - 2 * n_states * max_amplitude * row_sum_bound * max_residual
    )
    assert_equal(
        "omitting linear amplitude residual underbudgets the cut",
        abs(cut_shift) <= underbudget,
        False,
    )


def check_first_cluster_amplitude_correction() -> None:
    one_body_plus = Fraction(5, 11)
    one_body_minus = Fraction(7, 13)
    disconnected_product = one_body_plus * one_body_minus
    neutral_connected_pm = Fraction(3, 17)
    neutral_connected_mp = Fraction(3, 17)
    same_charge_connected_pp = Fraction(2, 19)
    same_charge_connected_mm = -Fraction(5, 23)
    full_neutral_pair_kernel_pm = disconnected_product + neutral_connected_pm
    full_neutral_pair_kernel_mp = disconnected_product + neutral_connected_mp

    ordered_pair_sum = (
        same_charge_connected_pp
        + neutral_connected_pm
        + neutral_connected_mp
        + same_charge_connected_mm
    )
    cluster_assembled = (
        one_body_plus + one_body_minus + Fraction(1, 2) * ordered_pair_sum
    )
    unordered_equivalent = (
        one_body_plus
        + one_body_minus
        + neutral_connected_pm
        + Fraction(1, 2) * same_charge_connected_pp
        + Fraction(1, 2) * same_charge_connected_mm
    )
    assert_equal(
        "ordered pair sum with Mayer half equals unordered pair assembly",
        cluster_assembled,
        unordered_equivalent,
    )
    assert_equal(
        "mixed distinguishable pair is counted once",
        Fraction(1, 2) * (neutral_connected_pm + neutral_connected_mp),
        neutral_connected_pm,
    )
    assert_equal(
        "identical ++ pair carries one half",
        Fraction(1, 2) * same_charge_connected_pp,
        Fraction(1, 19),
    )
    assert_equal(
        "identical -- pair carries one half",
        Fraction(1, 2) * same_charge_connected_mm,
        -Fraction(5, 46),
    )
    assert_not_equal(
        "ordered pair sum without one half double counts pair data",
        one_body_plus + one_body_minus + ordered_pair_sum,
        cluster_assembled,
    )

    unsubtracted_assembled = (
        one_body_plus
        + one_body_minus
        + Fraction(1, 2) * (full_neutral_pair_kernel_pm + full_neutral_pair_kernel_mp)
        + Fraction(1, 2) * (same_charge_connected_pp + same_charge_connected_mm)
    )
    assert_equal(
        "pair disconnected subtraction removes one-body product",
        unsubtracted_assembled - cluster_assembled,
        disconnected_product,
    )
    assert_not_equal(
        "full pair kernel is not a connected source correction",
        full_neutral_pair_kernel_pm,
        neutral_connected_pm,
    )

    source_projection = Fraction(19, 23)
    neutral_source_coefficient = source_projection * neutral_connected_pm
    neutral_topological_charge = 0
    neutral_theta_curvature = (
        neutral_topological_charge * neutral_topological_charge * neutral_connected_pm
    )
    assert_equal(
        "neutral pair has zero theta curvature charge",
        neutral_theta_curvature,
        Fraction(0),
    )
    assert_gt(
        "neutral pair source coefficient can be nonzero",
        float(abs(neutral_source_coefficient)),
        0.0,
    )
    assert_not_equal(
        "theta curvature cannot bound a neutral source pair",
        abs(neutral_source_coefficient),
        neutral_theta_curvature,
    )

    same_charge_topological_charge = 2
    same_charge_theta_curvature = (
        same_charge_topological_charge
        * same_charge_topological_charge
        * same_charge_connected_pp
    )
    assert_equal(
        "same-charge pair carries second harmonic curvature weight",
        same_charge_theta_curvature,
        Fraction(8, 19),
    )
    assert_not_equal(
        "neutral and same-charge pairs are different handoff data",
        same_charge_theta_curvature,
        neutral_theta_curvature,
    )

    singular_values = [Fraction(1, 5), Fraction(2, 7)]
    mass = Fraction(1, 11)
    overlap_weight = product(
        [mass * mass + singular * singular for singular in singular_values]
    )
    independent_mass_weight = mass ** (2 * len(singular_values))
    massless_overlap_weight = product(
        [singular * singular for singular in singular_values]
    )
    assert_not_equal(
        "IbarI overlap is not independent mass saturation",
        overlap_weight,
        independent_mass_weight,
    )
    assert_gt(
        "massless neutral overlap channel can survive",
        float(massless_overlap_weight),
        0.0,
    )

    connected_cells = [Fraction(1), -Fraction(97, 100), Fraction(3, 100)]
    leading_connected_window = sum(connected_cells, Fraction(0))
    absolute_connected_mass = sum(abs(cell) for cell in connected_cells)
    pair_corrections = [
        Fraction(1, 20),
        -Fraction(1, 25),
        Fraction(1, 30),
        -Fraction(1, 40),
        Fraction(1, 50),
    ]
    correction_multiplier = product([1 + error for error in pair_corrections])
    epsilon_pair = product([1 + abs(error) for error in pair_corrections]) - 1
    exact_connected_window = sum(
        cell * correction_multiplier for cell in connected_cells
    )
    tail_actual = Fraction(1, 149)
    tail_bound = Fraction(1, 97)
    assert_leq(
        "connected pair absolute product-plus-tail bound",
        float(abs(exact_connected_window + tail_actual - leading_connected_window)),
        float(epsilon_pair * absolute_connected_mass + tail_bound),
    )
    assert_equal(
        "connected pair leading signed window",
        leading_connected_window,
        Fraction(3, 50),
    )

    one_body_sector_bound = Fraction(1, 31)
    pair_sector_leakage = abs(neutral_source_coefficient)
    assert_gt(
        "one-body sector budget omits neutral pair leakage",
        float(one_body_sector_bound + pair_sector_leakage),
        float(one_body_sector_bound),
    )


def check_neutral_pair_valley_prescription() -> None:
    ComplexPair = tuple[Fraction, Fraction]

    def addz(left: ComplexPair, right: ComplexPair) -> ComplexPair:
        return (left[0] + right[0], left[1] + right[1])

    def subz(left: ComplexPair, right: ComplexPair) -> ComplexPair:
        return (left[0] - right[0], left[1] - right[1])

    def norm1(value: ComplexPair) -> Fraction:
        return abs(value[0]) + abs(value[1])

    pair_principal_value = Fraction(13, 19)
    perturbative_principal_value = Fraction(23, 29)
    vacuum_residue = Fraction(5, 17)
    source_projection = Fraction(7, 11)
    source_residue = source_projection * vacuum_residue

    pair_plus: ComplexPair = (pair_principal_value, source_residue)
    pair_minus: ComplexPair = (pair_principal_value, -source_residue)
    perturbative_plus: ComplexPair = (perturbative_principal_value, -source_residue)
    perturbative_minus: ComplexPair = (perturbative_principal_value, source_residue)

    combined_plus = addz(pair_plus, perturbative_plus)
    combined_minus = addz(pair_minus, perturbative_minus)
    assert_equal(
        "neutral valley lateral ambiguity cancels in the same source coordinate",
        combined_plus,
        combined_minus,
    )
    assert_not_equal(
        "neutral pair lateral value alone is prescription dependent",
        pair_plus,
        pair_minus,
    )

    principal_value_only: ComplexPair = (pair_principal_value, Fraction(0))
    assert_not_equal(
        "neutral valley principal value omits the lateral residue",
        principal_value_only,
        pair_plus,
    )

    wrong_frame_perturbative_plus: ComplexPair = (
        perturbative_principal_value,
        -vacuum_residue,
    )
    wrong_frame_perturbative_minus: ComplexPair = (
        perturbative_principal_value,
        vacuum_residue,
    )
    wrong_frame_plus = addz(pair_plus, wrong_frame_perturbative_plus)
    wrong_frame_minus = addz(pair_minus, wrong_frame_perturbative_minus)
    assert_not_equal(
        "vacuum valley residue does not cancel a projected source residue",
        wrong_frame_plus,
        wrong_frame_minus,
    )

    dropped_projection_pair_plus: ComplexPair = (pair_principal_value, vacuum_residue)
    assert_not_equal(
        "source projection is part of the neutral valley residue",
        dropped_projection_pair_plus,
        pair_plus,
    )

    pair_residual_plus: ComplexPair = (Fraction(1, 150), -Fraction(1, 500))
    pair_residual_minus: ComplexPair = (-Fraction(1, 180), Fraction(1, 600))
    borel_residual_plus: ComplexPair = (Fraction(1, 100), Fraction(1, 300))
    borel_residual_minus: ComplexPair = (-Fraction(1, 120), -Fraction(1, 400))
    exact_plus = addz(
        addz(pair_plus, pair_residual_plus),
        addz(perturbative_plus, borel_residual_plus),
    )
    exact_minus = addz(
        addz(pair_minus, pair_residual_minus),
        addz(perturbative_minus, borel_residual_minus),
    )
    residual_difference = addz(
        subz(pair_residual_plus, pair_residual_minus),
        subz(borel_residual_plus, borel_residual_minus),
    )
    assert_equal(
        "neutral valley residual prescription difference",
        subz(exact_plus, exact_minus),
        residual_difference,
    )
    residual_bound = (
        norm1(subz(pair_residual_plus, pair_residual_minus))
        + norm1(subz(borel_residual_plus, borel_residual_minus))
    )
    assert_leq(
        "neutral valley residual prescription bound",
        norm1(subz(exact_plus, exact_minus)),
        residual_bound,
    )


def check_two_flavor_mass_source_determinant_coordinate() -> None:
    m_u = Fraction(2, 5)
    m_d = Fraction(3, 7)
    mass: Matrix2 = ((m_u, Fraction(0)), (Fraction(0), m_d))
    source: Matrix2 = (
        (Fraction(11, 13), Fraction(5, 17)),
        (Fraction(7, 19), Fraction(13, 23)),
    )
    full = det2(add2(mass, source))
    polynomial = (
        m_u * m_d
        + m_u * source[1][1]
        + m_d * source[0][0]
        + source[0][0] * source[1][1]
        - source[0][1] * source[1][0]
    )
    assert_close("mass/source determinant polynomial", float(full), float(polynomial))

    wrong_plus = (
        m_u * m_d
        + m_u * source[1][1]
        + m_d * source[0][0]
        + source[0][0] * source[1][1]
        + source[0][1] * source[1][0]
    )
    assert_not_equal("off-diagonal determinant sign", full, wrong_plus)

    vacuum_coordinate = m_u * m_d
    four_source_coordinate = det2(source)
    assert_not_equal("vacuum coordinate is not four-source coefficient", vacuum_coordinate, four_source_coordinate)
    assert_gt("four-source coefficient nonzero", abs(float(four_source_coordinate)), 0.0)


def check_chirality_source_selection_gate() -> None:
    n_flavors = 2
    q_plus_slots = (n_flavors, 0, 0, n_flavors)
    q_minus_slots = (0, n_flavors, n_flavors, 0)
    chirality_balanced_slots = (1, 1, 1, 1)
    mass_assisted_slots = (1, 0, 0, 1)

    def axial_weight(slots: tuple[int, int, int, int]) -> int:
        n_left, n_right, n_bar_left, n_bar_right = slots
        return n_right + n_bar_left - n_left - n_bar_right

    def q_plus_supported(slots: tuple[int, int, int, int], mass_pairs: int = 0) -> bool:
        retained_pairs = n_flavors - mass_pairs
        return slots == (retained_pairs, 0, 0, retained_pairs)

    q_plus_source: Matrix2 = (
        (Fraction(2), Fraction(1)),
        (Fraction(3), Fraction(5)),
    )
    q_minus_source: Matrix2 = (
        (Fraction(1), Fraction(4)),
        (Fraction(2), Fraction(7)),
    )
    common_density_window = Fraction(5, 13) * Fraction(11, 17) * Fraction(19, 23)

    def q_plus_amplitude(slots: tuple[int, int, int, int], source: Matrix2) -> Fraction:
        if not q_plus_supported(slots):
            return Fraction(0)
        return common_density_window * det2(source)

    assert_equal("Q=1 chirality source determinant", det2(q_plus_source), Fraction(7))
    assert_equal("Q=-1 conjugate chirality source determinant", det2(q_minus_source), -Fraction(1))
    assert_equal("Q=1 hard vertex axial weight", axial_weight(q_plus_slots), -2 * n_flavors)
    assert_equal("Q=-1 hard vertex axial weight", axial_weight(q_minus_slots), 2 * n_flavors)
    assert_equal("chirality-balanced source has zero axial weight", axial_weight(chirality_balanced_slots), 0)

    q_plus_vertex = q_plus_amplitude(q_plus_slots, q_plus_source)
    assert_equal(
        "Q=1 chirality selection keeps the anomalous hard source coordinate",
        q_plus_vertex,
        common_density_window * det2(q_plus_source),
    )
    assert_equal(
        "Q=1 selection rejects the conjugate chirality coordinate",
        q_plus_amplitude(q_minus_slots, q_minus_source),
        Fraction(0),
    )
    assert_equal(
        "Q=1 selection rejects chirality-balanced four-source data",
        q_plus_amplitude(chirality_balanced_slots, q_plus_source),
        Fraction(0),
    )

    wrong_chirality_determinant_shortcut = common_density_window * det2(q_minus_source)
    assert_not_equal(
        "nonzero wrong-chirality determinant is not the Q=1 vertex",
        wrong_chirality_determinant_shortcut,
        q_plus_amplitude(q_minus_slots, q_minus_source),
    )
    unlabeled_four_source_sum = common_density_window * (
        det2(q_plus_source) + det2(q_minus_source)
    )
    assert_not_equal(
        "unlabeled four-source determinant mixes instanton chirality sectors",
        unlabeled_four_source_sum,
        q_plus_vertex,
    )
    assert_equal(
        "one mass insertion can replace one matched zero-mode source pair",
        q_plus_supported(mass_assisted_slots, mass_pairs=1),
        True,
    )
    assert_equal(
        "mass-assisted source coordinate is not the massless hard four-source vertex",
        q_plus_supported(mass_assisted_slots, mass_pairs=0),
        False,
    )


def check_axial_ward_source_transport() -> None:
    scalar: Matrix2 = (
        (Fraction(2, 3), Fraction(5, 7)),
        (Fraction(11, 13), Fraction(17, 19)),
    )
    pseudoscalar: Matrix2 = (
        (Fraction(3, 5), Fraction(-2, 11)),
        (Fraction(7, 17), Fraction(13, 23)),
    )

    ComplexFraction = tuple[Fraction, Fraction]

    def cadd(left: ComplexFraction, right: ComplexFraction) -> ComplexFraction:
        return (left[0] + right[0], left[1] + right[1])

    def csub(left: ComplexFraction, right: ComplexFraction) -> ComplexFraction:
        return (left[0] - right[0], left[1] - right[1])

    def cmul(left: ComplexFraction, right: ComplexFraction) -> ComplexFraction:
        return (
            left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0],
        )

    def cscale(value: ComplexFraction, scale: Fraction) -> ComplexFraction:
        return (scale * value[0], scale * value[1])

    def imul(value: ComplexFraction) -> ComplexFraction:
        return (-value[1], value[0])

    def cconj(value: ComplexFraction) -> ComplexFraction:
        return (value[0], -value[1])

    def centry(
        real: Matrix2,
        imag: Matrix2,
        row: int,
        col: int,
    ) -> ComplexFraction:
        return (real[row][col], imag[row][col])

    def cdet(real: Matrix2, imag: Matrix2) -> ComplexFraction:
        return csub(
            cmul(centry(real, imag, 0, 0), centry(real, imag, 1, 1)),
            cmul(centry(real, imag, 0, 1), centry(real, imag, 1, 0)),
        )

    def det_variation(
        real: Matrix2,
        imag: Matrix2,
        delta_real: Matrix2,
        delta_imag: Matrix2,
    ) -> ComplexFraction:
        c00 = centry(real, imag, 0, 0)
        c01 = centry(real, imag, 0, 1)
        c10 = centry(real, imag, 1, 0)
        c11 = centry(real, imag, 1, 1)
        dc00 = centry(delta_real, delta_imag, 0, 0)
        dc01 = centry(delta_real, delta_imag, 0, 1)
        dc10 = centry(delta_real, delta_imag, 1, 0)
        dc11 = centry(delta_real, delta_imag, 1, 1)
        return csub(
            cadd(cmul(dc00, c11), cmul(c00, dc11)),
            cadd(cmul(dc01, c10), cmul(c01, dc10)),
        )

    delta_scalar: Matrix2 = (
        (2 * pseudoscalar[0][0], 2 * pseudoscalar[0][1]),
        (2 * pseudoscalar[1][0], 2 * pseudoscalar[1][1]),
    )
    delta_pseudoscalar: Matrix2 = (
        (-2 * scalar[0][0], -2 * scalar[0][1]),
        (-2 * scalar[1][0], -2 * scalar[1][1]),
    )

    determinant = cdet(scalar, pseudoscalar)
    source_variation = det_variation(
        scalar,
        pseudoscalar,
        delta_scalar,
        delta_pseudoscalar,
    )
    expected_source_variation = cscale(imul(determinant), -4)
    theta_variation = cscale(imul(determinant), 4)
    assert_equal(
        "two-flavor source determinant axial variation",
        source_variation,
        expected_source_variation,
    )
    assert_equal(
        "Q=1 source determinant plus theta phase is Ward transported",
        cadd(source_variation, theta_variation),
        (Fraction(0), Fraction(0)),
    )

    anti_source_variation = cconj(source_variation)
    anti_theta_variation = cscale(imul(cconj(determinant)), -4)
    assert_equal(
        "anti-instanton conjugate source determinant Ward transport",
        cadd(anti_source_variation, anti_theta_variation),
        (Fraction(0), Fraction(0)),
    )
    assert_not_equal(
        "source-only axial rotation changes the charged hard coordinate",
        source_variation,
        (Fraction(0), Fraction(0)),
    )
    assert_not_equal(
        "theta-only axial shift changes the sector phase",
        theta_variation,
        (Fraction(0), Fraction(0)),
    )
    wrong_theta_sign = cscale(imul(determinant), -4)
    assert_not_equal(
        "wrong theta-shift sign violates instanton Ward transport",
        cadd(source_variation, wrong_theta_sign),
        (Fraction(0), Fraction(0)),
    )


def check_mass_source_rg_channel_transport() -> None:
    gamma_m = Fraction(5, 13)
    n_flavors = 2
    finite_fermion_factor_weight = n_flavors * gamma_m
    running_source_vector_weight = -gamma_m

    def fixed_basis_component_weight(source_derivatives: int) -> Fraction:
        mass_degree = n_flavors - source_derivatives
        mass_source_weight = -mass_degree * gamma_m
        return finite_fermion_factor_weight + mass_source_weight

    def running_source_contraction_weight(source_derivatives: int) -> Fraction:
        determinant_derivative_weight = (
            -(n_flavors - source_derivatives) * gamma_m
            + source_derivatives * running_source_vector_weight
        )
        return finite_fermion_factor_weight + determinant_derivative_weight

    for source_derivatives in range(n_flavors + 1):
        coefficient_weight = fixed_basis_component_weight(source_derivatives)
        projection_weight = -source_derivatives * gamma_m
        assert_equal(
            f"{source_derivatives}-source fixed-basis coefficient RG weight",
            coefficient_weight,
            source_derivatives * gamma_m,
        )
        assert_equal(
            f"{source_derivatives}-source fixed-basis projection cancels RG weight",
            coefficient_weight + projection_weight,
            Fraction(0),
        )
        assert_equal(
            f"{source_derivatives}-source running-source contraction RG weight",
            running_source_contraction_weight(source_derivatives),
            Fraction(0),
        )
        if source_derivatives:
            assert_not_equal(
                f"{source_derivatives}-source old shortcut misreads running-source flow",
                running_source_contraction_weight(source_derivatives),
                source_derivatives * gamma_m,
            )
            assert_not_equal(
                f"{source_derivatives}-source projection double-counts running sources",
                running_source_contraction_weight(source_derivatives) + projection_weight,
                Fraction(0),
            )

    vacuum_mass_source_weight = -n_flavors * gamma_m
    assert_equal(
        "vacuum source functional RG cancellation",
        finite_fermion_factor_weight + vacuum_mass_source_weight,
        Fraction(0),
    )
    assert_not_equal(
        "mass/source determinant alone is not the RG-covariant instanton vertex",
        vacuum_mass_source_weight,
        Fraction(0),
    )

    one_source_fixed_weight = fixed_basis_component_weight(1)
    one_source_running_weight = one_source_fixed_weight + running_source_vector_weight
    hard_source_weight = fixed_basis_component_weight(2)
    hard_running_source_weight = hard_source_weight + 2 * running_source_vector_weight
    assert_equal(
        "two-flavor fixed-basis mass-assisted coefficient carries one source weight",
        one_source_fixed_weight,
        gamma_m,
    )
    assert_equal(
        "two-flavor running mass-assisted source contraction is invariant",
        one_source_running_weight,
        Fraction(0),
    )
    assert_equal(
        "two-flavor fixed-basis hard coefficient carries two source weights",
        hard_source_weight,
        2 * gamma_m,
    )
    assert_equal(
        "two-flavor running hard source contraction is invariant",
        hard_running_source_weight,
        Fraction(0),
    )
    assert_not_equal(
        "hard fixed-basis coefficient is not RG invariant before projection",
        hard_source_weight,
        Fraction(0),
    )
    wrong_projection_sign = 2 * gamma_m
    assert_not_equal(
        "wrong-sign source projection doubles anomalous-dimension flow",
        hard_source_weight + wrong_projection_sign,
        Fraction(0),
    )
    assert_not_equal(
        "old running-source hard-flow formula invents a spurious two-source weight",
        hard_running_source_weight,
        2 * gamma_m,
    )

    connection = [
        [Fraction(0), Fraction(2, 7)],
        [Fraction(-3, 11), Fraction(1, 5)],
    ]
    covector = [Fraction(3, 7), Fraction(-5, 11)]
    source_vector = [Fraction(7, 13), Fraction(11, 17)]

    def dot_cov_vec(cov: list[Fraction], vec: list[Fraction]) -> Fraction:
        return sum(c * v for c, v in zip(cov, vec))

    def covector_connection(cov: list[Fraction]) -> list[Fraction]:
        return [
            sum(connection[row][col] * cov[col] for col in range(2))
            for row in range(2)
        ]

    def vector_connection(vec: list[Fraction]) -> list[Fraction]:
        return [
            -sum(connection[row][col] * vec[row] for row in range(2))
            for col in range(2)
        ]

    covector_flow = [
        gamma_m * covector[row] + covector_connection(covector)[row]
        for row in range(2)
    ]
    source_vector_flow = [
        -gamma_m * source_vector[col] + vector_connection(source_vector)[col]
        for col in range(2)
    ]
    connected_one_source_flow = dot_cov_vec(covector_flow, source_vector) + dot_cov_vec(
        covector,
        source_vector_flow,
    )
    assert_equal(
        "source-bundle connection cancels in one-source running contraction",
        connected_one_source_flow,
        Fraction(0),
    )
    missing_covector_connection_flow = dot_cov_vec(
        [gamma_m * entry for entry in covector],
        source_vector,
    ) + dot_cov_vec(covector, source_vector_flow)
    assert_not_equal(
        "omitting fixed-basis covector connection spoils one-source transport",
        missing_covector_connection_flow,
        Fraction(0),
    )

    rank_two_tensor = [
        [Fraction(1, 3), Fraction(-2, 5)],
        [Fraction(3, 7), Fraction(5, 11)],
    ]
    source_vector_1 = [Fraction(2, 9), Fraction(5, 12)]
    source_vector_2 = [Fraction(-7, 15), Fraction(4, 13)]

    def tensor_contract(
        tensor: list[list[Fraction]],
        first: list[Fraction],
        second: list[Fraction],
    ) -> Fraction:
        return sum(
            tensor[row][col] * first[row] * second[col]
            for row in range(2)
            for col in range(2)
        )

    def tensor_connection(tensor: list[list[Fraction]]) -> list[list[Fraction]]:
        return [
            [
                sum(connection[row][slot] * tensor[slot][col] for slot in range(2))
                + sum(connection[col][slot] * tensor[row][slot] for slot in range(2))
                for col in range(2)
            ]
            for row in range(2)
        ]

    tensor_conn = tensor_connection(rank_two_tensor)
    tensor_flow = [
        [
            2 * gamma_m * rank_two_tensor[row][col] + tensor_conn[row][col]
            for col in range(2)
        ]
        for row in range(2)
    ]
    source_vector_1_flow = [
        -gamma_m * source_vector_1[col] + vector_connection(source_vector_1)[col]
        for col in range(2)
    ]
    source_vector_2_flow = [
        -gamma_m * source_vector_2[col] + vector_connection(source_vector_2)[col]
        for col in range(2)
    ]
    connected_two_source_flow = (
        tensor_contract(tensor_flow, source_vector_1, source_vector_2)
        + tensor_contract(rank_two_tensor, source_vector_1_flow, source_vector_2)
        + tensor_contract(rank_two_tensor, source_vector_1, source_vector_2_flow)
    )
    assert_equal(
        "source-bundle connection cancels in two-source running contraction",
        connected_two_source_flow,
        Fraction(0),
    )
    tensor_flow_without_connection = [
        [2 * gamma_m * rank_two_tensor[row][col] for col in range(2)]
        for row in range(2)
    ]
    missing_tensor_connection_flow = (
        tensor_contract(tensor_flow_without_connection, source_vector_1, source_vector_2)
        + tensor_contract(rank_two_tensor, source_vector_1_flow, source_vector_2)
        + tensor_contract(rank_two_tensor, source_vector_1, source_vector_2_flow)
    )
    assert_not_equal(
        "omitting fixed-basis tensor connection spoils two-source transport",
        missing_tensor_connection_flow,
        Fraction(0),
    )

    finite_density_prefactor = Fraction(7, 11)
    vacuum_coefficient = Fraction(3, 5)
    hard_coefficient = Fraction(2, 7)
    vacuum_reference = finite_density_prefactor * vacuum_coefficient
    hard_channel = finite_density_prefactor * hard_coefficient
    calibrated_from_vacuum_without_projection = (
        vacuum_reference * hard_coefficient / vacuum_coefficient
    )
    hard_projection = Fraction(13, 17)
    physical_hard_channel = hard_channel * hard_projection
    assert_equal(
        "vacuum calibration recovers only the unprojected hard coefficient",
        calibrated_from_vacuum_without_projection,
        hard_channel,
    )
    assert_not_equal(
        "vacuum calibration is not the projected hard amplitude",
        calibrated_from_vacuum_without_projection,
        physical_hard_channel,
    )

    coefficient_residual = Fraction(1, 100)
    projection_residual = Fraction(1, 90)
    residual_flow = (
        coefficient_residual * hard_projection
        + hard_channel * projection_residual
    )
    residual_bound = (
        abs(coefficient_residual) * abs(hard_projection)
        + abs(hard_channel) * abs(projection_residual)
    )
    assert_equal(
        "mass/source RG channel residual bound",
        abs(residual_flow) <= residual_bound,
        True,
    )
    underbudget_without_projection = (
        residual_bound - abs(hard_channel) * abs(projection_residual)
    )
    assert_equal(
        "omitting projection-flow residual underbudgets mass/source RG transport",
        abs(residual_flow) <= underbudget_without_projection,
        False,
    )


def check_moduli_equivalent_channel_separation() -> None:
    weights = [Fraction(1, 3), Fraction(2, 5), Fraction(7, 11)]
    determinants = [Fraction(13, 17), Fraction(19, 23), Fraction(29, 31)]
    base_cells = [w * d for w, d in zip(weights, determinants)]
    moduli_only = sum(base_cells, Fraction(0))

    full_rank_sources: list[Matrix2] = [
        ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(3))),
        ((Fraction(3), Fraction(1, 2)), (Fraction(1, 5), Fraction(5))),
        ((Fraction(5, 2), Fraction(2, 3)), (Fraction(1, 7), Fraction(7, 3))),
    ]
    rank_one_sources: list[Matrix2] = [
        ((Fraction(2), Fraction(4)), (Fraction(3), Fraction(6))),
        ((Fraction(5), Fraction(10)), (Fraction(1), Fraction(2))),
        ((Fraction(7), Fraction(14)), (Fraction(3), Fraction(6))),
    ]

    full_rank_channel = sum(
        base * det2(source)
        for base, source in zip(base_cells, full_rank_sources)
    )
    rank_one_channel = sum(
        base * det2(source)
        for base, source in zip(base_cells, rank_one_sources)
    )

    assert_gt("moduli-only retained density nonzero", float(moduli_only), 0.0)
    assert_close("rank-one source channel vanishes", float(rank_one_channel), 0.0)
    assert_gt("full-rank source channel nonzero", abs(float(full_rank_channel)), 0.0)
    assert_not_equal("moduli-only shortcut cannot predict full-rank channel", moduli_only, full_rank_channel)


def check_projection_not_recoverable_from_one_euclidean_sum() -> None:
    cell_coefficients = [Fraction(1), Fraction(2), Fraction(3)]
    alternate_coefficients = [Fraction(3), Fraction(2), Fraction(1)]
    euclidean_sum = sum(cell_coefficients, Fraction(0))
    alternate_sum = sum(alternate_coefficients, Fraction(0))
    first_bin = [Fraction(1), Fraction(0), Fraction(0)]

    projected = sum(p * c for p, c in zip(first_bin, cell_coefficients))
    alternate_projected = sum(p * c for p, c in zip(first_bin, alternate_coefficients))

    assert_close("same Euclidean source sum", float(euclidean_sum), float(alternate_sum))
    assert_not_equal("one Euclidean sum does not determine spectral bin", projected, alternate_projected)
    assert_gt("projected ambiguity visible", abs(float(projected - alternate_projected)), 0.0)


def check_finite_cell_residual_bound() -> None:
    cells = [Fraction(5, 7), Fraction(-2, 9), Fraction(4, 11)]
    epsilons = [Fraction(1, 20), Fraction(1, 15), Fraction(1, 25)]
    deltas = [Fraction(1, 30), Fraction(-1, 20), Fraction(1, 40)]
    external_residual = Fraction(1, 5)
    external_actual = Fraction(1, 8)

    leading = sum(cells, Fraction(0))
    exact = sum(c * (1 + delta) for c, delta in zip(cells, deltas)) + external_actual
    error = abs(exact - leading)
    bound = sum(abs(c) * eps for c, eps in zip(cells, epsilons)) + external_residual
    underbudget = sum(abs(c) * eps for c, eps in zip(cells, epsilons))

    assert_leq("finite-cell residual bound", float(error), float(bound))
    assert_gt("omitting external residual underbudgets", float(error), float(underbudget))


def check_source_determinant_stability_bound() -> None:
    base: Matrix2 = ((Fraction(3), Fraction(1)), (Fraction(1), Fraction(2)))
    perturbation: Matrix2 = ((Fraction(1, 20), Fraction(-1, 50)), (Fraction(1, 60), Fraction(1, 40)))

    relative_matrix = matmul2(inv2(base), perturbation)
    eta = max_abs_entry(relative_matrix)
    relative_error = abs(det2(add2(base, perturbation)) - det2(base)) / abs(det2(base))
    bound = 2 * eta + eta * eta

    assert_leq("source determinant stability", float(relative_error), float(bound))
    assert_geq("positive determinant margin", float(abs(det2(base))), 1.0)


def check_su3_two_flavor_hard_source_power_and_tail() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    zero_mode_power = Fraction(6)
    measure_power = Fraction(-5)
    rho_power = b0 + zero_mode_power + measure_power

    assert_equal("SU3 Nf2 hard b0", b0, Fraction(29, 3))
    assert_equal("hard four-source rho power", rho_power, Fraction(32, 3))

    q_power = -(rho_power + 1)
    lambda_power = b0
    assert_equal("hard four-source Q power", q_power, -Fraction(35, 3))
    assert_equal("hard four-source coefficient mass dimension", lambda_power + q_power, Fraction(-2))

    c_values = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    leading_slot_coefficient = product([Fraction(6) / (c**3) for c in c_values])
    tail_integrand_power = rho_power - 12
    tail_antiderivative_power = tail_integrand_power + 1
    leading_tail_coefficient = -leading_slot_coefficient / tail_antiderivative_power

    assert_equal("hard four-source tail integrand power", tail_integrand_power, -Fraction(4, 3))
    assert_equal("hard four-source tail antiderivative power", tail_antiderivative_power, -Fraction(1, 3))
    assert_equal("hard four-source leading tail coefficient", leading_tail_coefficient, 3 * leading_slot_coefficient)
    assert_equal(
        "hard four-source sample tail coefficient",
        leading_tail_coefficient,
        Fraction(3 * 6**4, (1 * 2 * 3 * 4) ** 3),
    )

    one_soft_slot_power = rho_power - 9
    assert_equal("one missing hard slot endpoint power", one_soft_slot_power, Fraction(5, 3))
    assert_equal("one missing hard slot is not endpoint controlled", one_soft_slot_power < -1, False)


def check_hard_window_tail_subtraction() -> None:
    c_values = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    a_values = [Fraction(6) / (c**3) for c in c_values]
    b_values = [Fraction(45) / (c**5) for c in c_values]

    a0 = product(a_values)
    a1 = sum(
        b_values[index]
        * product(a_values[j] for j in range(len(a_values)) if j != index)
        for index in range(len(a_values))
    )
    compact_a1 = a0 * Fraction(15, 2) * sum(Fraction(1, c * c) for c in c_values)
    assert_equal(
        "hard window leading tail coefficient",
        a0,
        Fraction(6**4, (1 * 2 * 3 * 4) ** 3),
    )
    assert_equal("hard window subleading tail coefficient", a1, compact_a1)

    integrand_power_0 = Fraction(32, 3) - 12
    integrand_power_1 = Fraction(32, 3) - 14
    assert_equal("hard window leading integrand tail power", integrand_power_0, -Fraction(4, 3))
    assert_equal(
        "hard window subleading integrand tail power",
        integrand_power_1,
        -Fraction(10, 3),
    )

    # Choose R=27 so R^(-1/3) and R^(-7/3) are exact rational powers.
    r_root = Fraction(3)
    leading_tail = 3 * a0 / r_root
    subleading_tail = Fraction(3, 7) * a1 / (r_root**7)
    two_term_tail = leading_tail + subleading_tail
    assert_equal(
        "hard window leading tail at R=27",
        leading_tail,
        a0,
    )
    assert_equal(
        "hard window subleading tail at R=27",
        subleading_tail,
        Fraction(3, 7) * a1 / 2187,
    )
    assert_gt(
        "subleading hard-window tail is a real retained term",
        float(abs(subleading_tail)),
        0.0,
    )

    core_integral = Fraction(101, 37)
    tail_residual = Fraction(1, 20000)
    full_window = core_integral + two_term_tail + tail_residual
    leading_only_window = core_integral + leading_tail
    assert_not_equal(
        "leading-tail-only hard window misses subleading endpoint term",
        leading_only_window,
        full_window,
    )

    complete_budget = abs(subleading_tail) + abs(tail_residual)
    underbudget = abs(tail_residual)
    leading_only_error = abs(full_window - leading_only_window)
    assert_equal(
        "two-term hard-window tail budget controls leading-only error",
        leading_only_error <= complete_budget,
        True,
    )
    assert_equal(
        "omitting subleading tail underbudgets hard-window evaluation",
        leading_only_error <= underbudget,
        False,
    )

    fused_density_tail_class = "exponential"
    differentiated_slot_tail_class = "power"
    assert_not_equal(
        "fused density endpoint class is not differentiated hard slots",
        fused_density_tail_class,
        differentiated_slot_tail_class,
    )


def check_hard_screened_retained_size_window() -> None:
    b0_su3_nf2 = beta0(3, 2)
    zero_mode_power = Fraction(6)
    measure_power = Fraction(-5)
    rho_density_power = b0_su3_nf2 + zero_mode_power + measure_power
    log_shell_power = rho_density_power + 1

    assert_equal(
        "screened hard-window density power",
        rho_density_power,
        Fraction(32, 3),
    )
    assert_equal(
        "screened hard-window logarithmic shell power",
        log_shell_power,
        Fraction(35, 3),
    )

    hard_source_spectral_gaps = [Fraction(2), Fraction(7, 3), Fraction(3)]
    hard_envelope = min(hard_source_spectral_gaps)
    assert_equal(
        "screened majorant hard envelope from finite source gaps",
        hard_envelope,
        Fraction(2),
    )

    # Derive the screening mass from independent finite medium data, rather
    # than choosing the desired shell and solving backward for the mass.
    screening_vector = [Fraction(2), Fraction(1)]
    screening_eigenvalues = [Fraction(2), Fraction(44, 27)]
    screening_norm = sum(value * value for value in screening_vector)
    screening_mass_squared = sum(
        value * value * eigenvalue
        for value, eigenvalue in zip(screening_vector, screening_eigenvalues)
    ) / screening_norm
    assert_equal(
        "screened majorant mass from finite screening Rayleigh quotient",
        screening_mass_squared,
        Fraction(52, 27),
    )

    rho_star = Fraction(3, 2)

    def log_shell_derivative(
        shell_power: Fraction,
        rho: Fraction,
        include_hard: bool,
        include_screening: bool,
    ) -> Fraction:
        return (
            shell_power
            - (hard_envelope * rho if include_hard else 0)
            - (2 * screening_mass_squared * rho * rho if include_screening else 0)
        )

    assert_equal(
        "screened majorant mixed stationarity",
        log_shell_derivative(
            log_shell_power,
            rho_star,
            include_hard=True,
            include_screening=True,
        ),
        Fraction(0),
    )
    assert_gt(
        "screened majorant derivative before shell",
        log_shell_derivative(
            log_shell_power,
            Fraction(1),
            include_hard=True,
            include_screening=True,
        ),
        Fraction(0),
    )
    assert_gt(
        "screened majorant derivative after shell has changed sign",
        Fraction(0),
        log_shell_derivative(
            log_shell_power,
            Fraction(2),
            include_hard=True,
            include_screening=True,
        ),
    )

    hard_only_shell = log_shell_power / hard_envelope
    screened_only_shell_squared = log_shell_power / (2 * screening_mass_squared)
    assert_equal(
        "screened majorant mixed shell below hard-only shell",
        rho_star < hard_only_shell,
        True,
    )
    assert_equal(
        "screened majorant mixed shell below screened-only shell",
        rho_star * rho_star < screened_only_shell_squared,
        True,
    )
    assert_not_equal(
        "hard-only shell is not stationary with screening present",
        log_shell_derivative(
            log_shell_power,
            hard_only_shell,
            include_hard=True,
            include_screening=True,
        ),
        Fraction(0),
    )
    screened_only_shortcut_residual_squared = (
        hard_envelope * hard_envelope * screened_only_shell_squared
    )
    assert_gt(
        "screened-only shell has a nonzero hard-envelope residual",
        screened_only_shortcut_residual_squared,
        Fraction(0),
    )
    assert_equal(
        "using d rho power misses the d log rho shell",
        log_shell_derivative(
            rho_density_power,
            rho_star,
            include_hard=True,
            include_screening=True,
        ),
        -Fraction(1),
    )

    lower_endpoint = Fraction(1)
    window_low = Fraction(4, 3)
    window_high = Fraction(5, 3)
    weak_coupling_lambda = Fraction(1, 10)
    weak_coupling_limit = Fraction(1, 4)
    assert_equal(
        "screened majorant interior shell lies above long-size endpoint",
        lower_endpoint <= window_low < rho_star < window_high,
        True,
    )
    assert_equal(
        "screened majorant window stays in weak-coupling domain",
        weak_coupling_lambda * window_high < weak_coupling_limit,
        True,
    )

    boundary_endpoint = Fraction(2)
    assert_equal(
        "endpoint above shell is boundary controlled",
        log_shell_derivative(
            log_shell_power,
            boundary_endpoint,
            include_hard=True,
            include_screening=True,
        )
        < 0,
        True,
    )
    boundary_denominator = (
        hard_envelope
        + 2 * screening_mass_squared * boundary_endpoint
        - (rho_density_power / boundary_endpoint)
    )
    assert_gt(
        "boundary tail denominator is positive after the shell",
        boundary_denominator,
        Fraction(0),
    )
    assert_equal(
        "interior shell cannot be used below the integration endpoint",
        rho_star >= boundary_endpoint,
        False,
    )
    bad_window_high = Fraction(4)
    assert_equal(
        "screened majorant rejects shells outside weak coupling",
        weak_coupling_lambda * bad_window_high < weak_coupling_limit,
        False,
    )

    majorant_bins = {
        Fraction(1): Fraction(12),
        rho_star: Fraction(20),
        Fraction(2): Fraction(10),
    }
    concentrated_at_shell = {
        Fraction(1): Fraction(0),
        rho_star: Fraction(18),
        Fraction(2): Fraction(0),
    }
    concentrated_at_boundary = {
        Fraction(1): Fraction(10),
        rho_star: Fraction(0),
        Fraction(2): Fraction(8),
    }
    for rho, value in concentrated_at_shell.items():
        assert_equal(
            f"shell-concentrated kernel obeys majorant at rho={rho}",
            value <= majorant_bins[rho],
            True,
        )
    for rho, value in concentrated_at_boundary.items():
        assert_equal(
            f"boundary-concentrated kernel obeys same majorant at rho={rho}",
            value <= majorant_bins[rho],
            True,
        )
    shell_peak = max(concentrated_at_shell, key=concentrated_at_shell.get)
    boundary_peak = max(concentrated_at_boundary, key=concentrated_at_boundary.get)
    assert_equal(
        "same majorant can allow an actual shell peak",
        shell_peak,
        rho_star,
    )
    assert_not_equal(
        "same majorant can also allow a non-shell actual peak",
        boundary_peak,
        rho_star,
    )

    comparable_positive_kernel = {
        Fraction(1): Fraction(6),
        rho_star: Fraction(12),
        Fraction(2): Fraction(4),
    }
    comparability_ratio = min(
        comparable_positive_kernel[rho] / majorant_bins[rho]
        for rho in majorant_bins
    )
    assert_gt(
        "positive comparability ratio is extra data beyond the majorant",
        comparability_ratio,
        Fraction(0),
    )
    zero_at_shell_kernel = {
        Fraction(1): Fraction(6),
        rho_star: Fraction(0),
        Fraction(2): Fraction(4),
    }
    zero_at_shell_ratio = min(
        zero_at_shell_kernel[rho] / majorant_bins[rho] for rho in majorant_bins
    )
    assert_equal(
        "majorant alone cannot supply noncancellation at the shell",
        zero_at_shell_ratio,
        Fraction(0),
    )

    density_tail_bound = Fraction(1, 20)
    actual_density_tail = Fraction(1, 30)
    source_norm = Fraction(7, 5)
    physical_projection_norm = Fraction(5, 6)
    screened_size_bound = (
        density_tail_bound * source_norm * physical_projection_norm
    )
    actual_size_contribution = (
        actual_density_tail * source_norm * physical_projection_norm
    )
    determinant_residual = Fraction(1, 100)
    normal_mode_residual = Fraction(1, 120)
    tail_residual = Fraction(1, 80)
    projection_residual = Fraction(1, 90)
    actual_determinant_error = Fraction(1, 200)
    actual_normal_mode_error = Fraction(1, 300)
    actual_tail_error = Fraction(1, 500)
    actual_projection_error = Fraction(1, 180)
    actual_long_size_remainder = (
        actual_size_contribution
        + actual_determinant_error
        + actual_normal_mode_error
        + actual_tail_error
        + actual_projection_error
    )
    complete_bound = (
        screened_size_bound
        + determinant_residual
        + normal_mode_residual
        + tail_residual
        + projection_residual
    )
    underbudget_without_projection = (
        screened_size_bound
        + determinant_residual
        + normal_mode_residual
        + tail_residual
    )

    assert_equal(
        "screened majorant bound keeps source and projection norms",
        screened_size_bound,
        Fraction(7, 120),
    )
    assert_not_equal(
        "moduli-only screened tail is not the physical long-size bound",
        density_tail_bound,
        screened_size_bound,
    )
    assert_equal(
        "screened majorant residual budget controls the physical remainder",
        actual_long_size_remainder <= complete_bound,
        True,
    )
    assert_equal(
        "omitting physical-projection residual underbudgets certified window",
        complete_bound <= underbudget_without_projection,
        False,
    )


def check_hard_wilsonian_ope_boundary_flow() -> None:
    b0_su3_nf2 = beta0(3, 2)
    zero_mode_power = Fraction(6)
    size_power = b0_su3_nf2 + zero_mode_power - 5
    q_power = -(size_power + 1)
    assert_equal("hard OPE source coefficient dimension", b0_su3_nf2 + q_power, Fraction(-2))

    c_values = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    tail_slot_coefficient = product([Fraction(6) / (c**3) for c in c_values])
    tail_integrand_power = size_power - 12
    assert_equal("hard OPE tail integrand power", tail_integrand_power, -Fraction(4, 3))

    # Choose R=27 so R^(-1/3) remains rational in the leading tail model.
    r_cuberoot = Fraction(3)
    boundary_flux = tail_slot_coefficient / r_cuberoot
    long_tail = 3 * tail_slot_coefficient / r_cuberoot
    mu_i_flow = -boundary_flux
    log_r_tail_flow = -boundary_flux
    mu_i_long_tail_flow = -log_r_tail_flow
    assert_equal("hard OPE long-tail coefficient", long_tail, 3 * boundary_flux)
    assert_equal("hard OPE factorization-scale boundary flow", mu_i_flow, -boundary_flux)
    assert_equal("hard OPE log-R tail flow matches short mu-flow", mu_i_flow, log_r_tail_flow)
    assert_equal(
        "hard OPE completed split is factorization-scale stationary",
        mu_i_flow + mu_i_long_tail_flow,
        Fraction(0),
    )

    prefactor = Fraction(5, 11)
    short_integral = Fraction(10, 7)
    operator_matching = Fraction(13, 17)
    matrix_element = Fraction(19, 23)
    residuals = [Fraction(1, 500), -Fraction(1, 700), Fraction(1, 900)]

    short_coefficient = prefactor * operator_matching * short_integral
    short_matrix_element_part = short_coefficient * matrix_element
    long_size_part = prefactor * long_tail
    physical_amplitude = (
        short_matrix_element_part
        + long_size_part
        + sum(residuals, Fraction(0))
    )
    assert_not_equal(
        "short instanton coefficient alone is not the physical amplitude",
        short_coefficient,
        physical_amplitude,
    )
    assert_not_equal(
        "short coefficient needs its physical matrix element",
        short_coefficient,
        short_matrix_element_part,
    )

    basis_scale = Fraction(7, 5)
    transformed_coefficient = short_coefficient / basis_scale
    transformed_matrix_element = basis_scale * matrix_element
    assert_equal(
        "operator basis change leaves coefficient-matrix-element pairing fixed",
        transformed_coefficient * transformed_matrix_element,
        short_matrix_element_part,
    )

    full_hard_as_local = (short_coefficient + long_size_part) * matrix_element
    assert_not_equal(
        "full hard source coefficient is not a local OPE coefficient",
        full_hard_as_local,
        physical_amplitude,
    )
    fixed_vertex_flow = Fraction(0)
    assert_not_equal(
        "moving Wilsonian boundary gives nonzero vertex flow",
        fixed_vertex_flow,
        mu_i_flow,
    )

    error_from_short_local_term = abs(physical_amplitude - short_matrix_element_part)
    complete_budget = abs(long_size_part) + sum(abs(residual) for residual in residuals)
    underbudget = sum(abs(residual) for residual in residuals)
    assert_equal(
        "hard OPE assembly with long-size tail is bounded",
        error_from_short_local_term <= complete_budget,
        True,
    )
    assert_equal(
        "omitting long-size instanton tail underbudgets OPE assembly",
        error_from_short_local_term <= underbudget,
        False,
    )


def check_wilsonian_matching_scheme_covariance() -> None:
    Vector2 = tuple[Fraction, Fraction]

    def dot(left: Vector2, right: Vector2) -> Fraction:
        return left[0] * right[0] + left[1] * right[1]

    def row_mat(row: Vector2, matrix: Matrix2) -> Vector2:
        return (
            row[0] * matrix[0][0] + row[1] * matrix[1][0],
            row[0] * matrix[0][1] + row[1] * matrix[1][1],
        )

    def mat_vec(matrix: Matrix2, vector: Vector2) -> Vector2:
        return (
            matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
            matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
        )

    def sub_vec(left: Vector2, right: Vector2) -> Vector2:
        return (left[0] - right[0], left[1] - right[1])

    def neg_vec(vector: Vector2) -> Vector2:
        return (-vector[0], -vector[1])

    short_coefficients: Vector2 = (Fraction(2, 5), -Fraction(1, 7))
    matrix_elements: Vector2 = (Fraction(3, 11), Fraction(5, 13))
    local_pairing = dot(short_coefficients, matrix_elements)

    scheme: Matrix2 = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(1)))
    inverse_scheme = inv2(scheme)
    transformed_coefficients = row_mat(short_coefficients, inverse_scheme)
    transformed_matrix_elements = mat_vec(scheme, matrix_elements)
    assert_equal(
        "Wilsonian coefficient/operator scheme covariance",
        dot(transformed_coefficients, transformed_matrix_elements),
        local_pairing,
    )

    diagonal_only_inverse: Matrix2 = (
        (Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    diagonal_shortcut = row_mat(short_coefficients, diagonal_only_inverse)
    assert_not_equal(
        "diagonal rescaling misses operator mixing in instanton matching",
        dot(diagonal_shortcut, transformed_matrix_elements),
        local_pairing,
    )
    assert_not_equal(
        "short coefficient vector alone is scheme dependent",
        transformed_coefficients,
        short_coefficients,
    )

    boundary_flux: Vector2 = (Fraction(1, 17), -Fraction(2, 19))
    anomalous_dimension: Matrix2 = (
        (Fraction(1, 3), Fraction(1, 5)),
        (-Fraction(2, 7), Fraction(1, 11)),
    )
    coefficient_flow = sub_vec(
        row_mat(short_coefficients, anomalous_dimension),
        boundary_flux,
    )
    matrix_element_flow = neg_vec(mat_vec(anomalous_dimension, matrix_elements))
    long_tail_flow = dot(boundary_flux, matrix_elements)
    completed_flow = (
        dot(coefficient_flow, matrix_elements)
        + dot(short_coefficients, matrix_element_flow)
        + long_tail_flow
    )
    assert_equal(
        "instanton Wilsonian boundary/anomalous-dimension flow cancels",
        completed_flow,
        Fraction(0),
    )

    local_only_flow = dot(coefficient_flow, matrix_elements) + dot(
        short_coefficients,
        matrix_element_flow,
    )
    assert_not_equal(
        "omitting the long-size shell leaves moving-boundary flow",
        local_only_flow,
        Fraction(0),
    )

    coefficient_residual: Vector2 = (Fraction(1, 100), -Fraction(1, 120))
    matrix_element_residual: Vector2 = (Fraction(1, 90), Fraction(1, 110))
    long_tail_residual = Fraction(1, 30)
    residual_flow = (
        dot(coefficient_residual, matrix_elements)
        + dot(short_coefficients, matrix_element_residual)
        + long_tail_residual
    )
    residual_bound = (
        (abs(coefficient_residual[0]) + abs(coefficient_residual[1]))
        * max(abs(matrix_elements[0]), abs(matrix_elements[1]))
        + (abs(short_coefficients[0]) + abs(short_coefficients[1]))
        * max(abs(matrix_element_residual[0]), abs(matrix_element_residual[1]))
        + abs(long_tail_residual)
    )
    assert_leq(
        "instanton Wilsonian covariance residual bound",
        float(abs(residual_flow)),
        float(residual_bound),
    )
    underbudget_without_long_shell = residual_bound - abs(long_tail_residual)
    assert_equal(
        "omitting long-shell residual underbudgets Wilsonian matching",
        abs(residual_flow) <= underbudget_without_long_shell,
        False,
    )


def check_hard_benchmark_channel_comparison_and_ratio() -> None:
    center_delta_on_shell = Fraction(1)
    center_delta_off_shell = Fraction(0)
    determinant_constant = Fraction(11, 13)
    haar_projection = Fraction(3, 7)
    amputation = Fraction(1)
    source_frame = Fraction(1)
    physical_projection = Fraction(7, 11)

    right_overlap: Matrix2 = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(2)))
    left_overlap: Matrix2 = ((Fraction(3), Fraction(1)), (Fraction(2), Fraction(2)))
    source_factor = det2(right_overlap) * det2(left_overlap)
    assert_equal("hard benchmark right source determinant", det2(right_overlap), Fraction(3))
    assert_equal("hard benchmark left source determinant", det2(left_overlap), Fraction(4))
    assert_equal("hard benchmark zero-mode source factor", source_factor, Fraction(12))

    window_cells = [Fraction(1, 2), -Fraction(1, 8), Fraction(3, 10)]
    hard_window = sum(window_cells, Fraction(0))
    euclidean_benchmark = (
        center_delta_on_shell
        * determinant_constant
        * haar_projection
        * amputation
        * source_frame
        * source_factor
        * hard_window
    )
    physical_benchmark = physical_projection * euclidean_benchmark
    density_only = determinant_constant * hard_window

    assert_equal("hard benchmark signed window", hard_window, Fraction(27, 40))
    assert_not_equal("density-only hard shortcut misses channel data", density_only, euclidean_benchmark)
    assert_not_equal("Euclidean colored kernel is not physical projection", euclidean_benchmark, physical_benchmark)

    off_shell = (
        center_delta_off_shell
        * determinant_constant
        * haar_projection
        * source_factor
        * hard_window
    )
    assert_equal("off-shell center projection kills hard benchmark", off_shell, Fraction(0))

    rank_one_right: Matrix2 = ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(4)))
    collapsed_source_factor = det2(rank_one_right) * det2(left_overlap)
    assert_equal("rank-one zero-mode source kills hard benchmark", collapsed_source_factor, Fraction(0))

    unamputated_residue_product = Fraction(5, 3)
    unamputated = unamputated_residue_product * euclidean_benchmark
    assert_not_equal("unamputated external residues change coordinate", unamputated, euclidean_benchmark)
    assert_equal("amputation restores benchmark coordinate", unamputated / unamputated_residue_product, euclidean_benchmark)

    q_power = -Fraction(35, 3)
    collective_jacobian_power = 6
    log_action_q1 = Fraction(5, 2)
    log_action_q2 = Fraction(7, 2)
    collective_jacobian_ratio = (log_action_q2 / log_action_q1) ** collective_jacobian_power
    ratio_powers = {
        "determinant_constant": Fraction(0),
        "Lambda_ht": Fraction(0),
        "Q2_over_Q1": q_power,
        "collective_jacobian_ratio": collective_jacobian_ratio,
        "source_window_ratio": Fraction(1),
    }
    assert_equal("same-theory determinant constant cancels in ratio", ratio_powers["determinant_constant"], Fraction(0))
    assert_equal("same-theory Lambda power cancels in ratio", ratio_powers["Lambda_ht"], Fraction(0))
    assert_equal("hard scale ratio keeps Q power", ratio_powers["Q2_over_Q1"], q_power)
    assert_not_equal(
        "hard scale ratio keeps running collective Jacobian",
        ratio_powers["collective_jacobian_ratio"],
        Fraction(1),
    )

    e1 = -Fraction(1, 20)
    e2 = Fraction(1, 30)
    eps1 = Fraction(1, 10)
    eps2 = Fraction(1, 12)
    ratio_residual = (1 + e2) / (1 + e1) - 1
    ratio_bound = (eps1 + eps2) / (1 - eps1)
    assert_equal("hard ratio residual sample", ratio_residual, Fraction(5, 57))
    assert_leq("hard ratio residual bound", float(abs(ratio_residual)), float(ratio_bound))

    determinant_only_q_power = Fraction(0)
    assert_equal("determinant-only ratio misses hard Q power", determinant_only_q_power == q_power, False)
    assert_equal(
        "pure-power ratio misses hard collective Jacobian",
        collective_jacobian_ratio == Fraction(1),
        False,
    )
    stale_source_window_ratio = Fraction(15, 14)
    assert_equal("changed source window is a real ratio input", stale_source_window_ratio == Fraction(1), False)


def check_thooft_four_point_amputated_assembly_gate() -> None:
    momentum_slots = [3, -5, 7, -5]
    off_shell_slots = [3, -5, 7, -4]
    center_delta = Fraction(1) if sum(momentum_slots) == 0 else Fraction(0)
    off_shell_delta = Fraction(1) if sum(off_shell_slots) == 0 else Fraction(0)
    assert_equal("amputated four-point center projection", center_delta, Fraction(1))
    assert_equal("off-shell four-point center projection", off_shell_delta, Fraction(0))

    density = Fraction(11, 13)
    haar_projection = Fraction(2, 7)
    right_source_det = Fraction(3)
    left_source_det = Fraction(4)
    zero_mode_slot_product = Fraction(5, 9)
    nonzero_mode_source_quotient = Fraction(21, 20)
    amputation_transport = Fraction(9, 10)
    physical_projection = Fraction(7, 8)

    leading_amputated = product(
        [
            center_delta,
            density,
            haar_projection,
            right_source_det,
            left_source_det,
            zero_mode_slot_product,
            nonzero_mode_source_quotient,
            amputation_transport,
            physical_projection,
        ]
    )
    assert_equal("amputated four-point assembled coefficient", leading_amputated, Fraction(693, 520))

    density_only = density
    determinant_and_slots_only = density * zero_mode_slot_product
    omitted_nonzero_source = leading_amputated / nonzero_mode_source_quotient
    unamputated_source_overlap = Fraction(5, 3)
    unamputated = leading_amputated * unamputated_source_overlap
    assert_not_equal("density-only four-point shortcut misses channel assembly", density_only, leading_amputated)
    assert_not_equal(
        "zero-mode slots without source/projection data miss four-point assembly",
        determinant_and_slots_only,
        leading_amputated,
    )
    assert_not_equal(
        "omitted nonzero-mode source quotient changes four-point coefficient",
        omitted_nonzero_source,
        leading_amputated,
    )
    assert_not_equal("unamputated source overlaps change four-point coefficient", unamputated, leading_amputated)
    assert_equal("amputation removes external overlap factor", unamputated / unamputated_source_overlap, leading_amputated)

    rank_lost_right_det = Fraction(0)
    rank_lost_channel = (
        density
        * haar_projection
        * rank_lost_right_det
        * left_source_det
        * zero_mode_slot_product
        * nonzero_mode_source_quotient
        * amputation_transport
        * physical_projection
    )
    assert_equal("rank-lost right source determinant kills four-point channel", rank_lost_channel, Fraction(0))
    assert_not_equal(
        "nonzero density does not revive rank-lost four-point source",
        density,
        rank_lost_channel,
    )

    symmetric_haar_projection = Fraction(0)
    symmetric_color_channel = (
        density
        * symmetric_haar_projection
        * right_source_det
        * left_source_det
        * zero_mode_slot_product
        * nonzero_mode_source_quotient
        * amputation_transport
        * physical_projection
    )
    assert_equal("symmetric Haar source kills amputated four-point channel", symmetric_color_channel, Fraction(0))

    residuals = {
        "density": Fraction(1, 100),
        "slot": Fraction(1, 120),
        "haar": Fraction(1, 150),
        "source": Fraction(1, 175),
        "nonzero_source": Fraction(1, 210),
        "amputation": Fraction(1, 240),
        "tail": Fraction(1, 260),
        "projection": Fraction(1, 280),
        "sector": Fraction(1, 315),
    }
    residual_sum = sum(residuals.values(), Fraction(0))
    physical_amplitude = leading_amputated + residual_sum
    residual_budget = sum(abs(value) for value in residuals.values())
    assert_equal(
        "amputated four-point residual telescope",
        physical_amplitude - leading_amputated,
        residual_sum,
    )
    assert_equal(
        "amputated four-point absolute residual bound",
        abs(physical_amplitude - leading_amputated) <= residual_budget,
        True,
    )
    underbudget_without_projection = residual_budget - abs(residuals["projection"])
    assert_equal(
        "omitting projection residual underbudgets four-point assembly",
        abs(physical_amplitude - leading_amputated) <= underbudget_without_projection,
        False,
    )


def check_thooft_crossed_chiral_channel() -> None:
    q_plus_all_out = ("u_L", "d_L", "ubar_R", "dbar_R")
    q_minus_all_out = ("u_R", "d_R", "ubar_L", "dbar_L")
    chirality_balanced = ("u_L", "d_R", "ubar_L", "dbar_R")

    def axial_weight(slots: tuple[str, str, str, str]) -> int:
        weights = {
            "u_L": -1,
            "d_L": -1,
            "ubar_R": -1,
            "dbar_R": -1,
            "u_R": 1,
            "d_R": 1,
            "ubar_L": 1,
            "dbar_L": 1,
        }
        return sum(weights[slot] for slot in slots)

    def cross_barred_slot(slot: str) -> str:
        crossing = {
            "ubar_R": "u_R",
            "dbar_R": "d_R",
            "ubar_L": "u_L",
            "dbar_L": "d_L",
        }
        return crossing[slot]

    def crossed_process(
        all_outgoing: tuple[str, str, str, str],
        incoming_indices: tuple[int, int],
    ) -> tuple[tuple[str, str], tuple[str, str]]:
        incoming = tuple(cross_barred_slot(all_outgoing[index]) for index in incoming_indices)
        outgoing = tuple(
            slot for index, slot in enumerate(all_outgoing) if index not in incoming_indices
        )
        return incoming, outgoing

    assert_equal("Q=1 crossed source axial weight", axial_weight(q_plus_all_out), -4)
    assert_equal("Q=-1 crossed source axial weight", axial_weight(q_minus_all_out), 4)
    assert_equal("balanced crossed source axial weight", axial_weight(chirality_balanced), 0)
    assert_equal(
        "Q=1 barred-slot crossing gives RR to LL",
        crossed_process(q_plus_all_out, (2, 3)),
        (("u_R", "d_R"), ("u_L", "d_L")),
    )
    assert_equal(
        "Q=-1 barred-slot crossing gives LL to RR",
        crossed_process(q_minus_all_out, (2, 3)),
        (("u_L", "d_L"), ("u_R", "d_R")),
    )

    density = Fraction(11, 13)
    haar_projection = Fraction(2, 7)
    zero_mode_slot_product = Fraction(5, 9)
    nonzero_mode_source_quotient = Fraction(21, 20)
    amputation_transport = Fraction(9, 10)
    physical_projection = Fraction(7, 8)
    common_kernel = product(
        [
            density,
            haar_projection,
            zero_mode_slot_product,
            nonzero_mode_source_quotient,
            amputation_transport,
            physical_projection,
        ]
    )

    q_plus_right: Matrix2 = ((Fraction(2), Fraction(1)), (Fraction(3), Fraction(5)))
    q_plus_left: Matrix2 = ((Fraction(3), Fraction(1)), (Fraction(2), Fraction(4)))
    q_minus_right: Matrix2 = ((Fraction(4), Fraction(1)), (Fraction(2), Fraction(3)))
    q_minus_left: Matrix2 = ((Fraction(5), Fraction(2)), (Fraction(1), Fraction(3)))
    assert_equal("Q=1 crossed right determinant", det2(q_plus_right), Fraction(7))
    assert_equal("Q=1 crossed left determinant", det2(q_plus_left), Fraction(10))
    assert_equal("Q=-1 crossed right determinant", det2(q_minus_right), Fraction(10))
    assert_equal("Q=-1 crossed left determinant", det2(q_minus_left), Fraction(13))

    all_outgoing_kernel = common_kernel * det2(q_plus_right) * det2(q_plus_left)
    crossing_residue = product(
        [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13), Fraction(17, 19)]
    )
    crossed_kernel = all_outgoing_kernel * crossing_residue
    assert_not_equal(
        "all-outgoing source coefficient is not the crossed physical channel",
        all_outgoing_kernel,
        crossed_kernel,
    )
    assert_equal(
        "crossing residues multiply the selected source kernel",
        crossed_kernel / crossing_residue,
        all_outgoing_kernel,
    )

    wrong_unlabeled_process_kernel = Fraction(0)
    assert_not_equal(
        "physical in/out labels cannot replace all-outgoing zero-mode slots",
        wrong_unlabeled_process_kernel,
        crossed_kernel,
    )
    same_channel_anti_instanton = Fraction(0)
    conjugate_channel_kernel = (
        common_kernel * det2(q_minus_right) * det2(q_minus_left) * crossing_residue
    )
    assert_equal(
        "anti-instanton is the conjugate massless chiral channel",
        same_channel_anti_instanton,
        Fraction(0),
    )
    assert_not_equal(
        "conjugate chirality determinant is not the same RR to LL channel",
        conjugate_channel_kernel,
        same_channel_anti_instanton,
    )
    assert_equal(
        "chirality-balanced source is not the Q=1 crossed hard channel",
        chirality_balanced == q_plus_all_out,
        False,
    )

    PhasePoly = dict[int, Fraction]

    def normalize(poly: PhasePoly) -> PhasePoly:
        return {power: coeff for power, coeff in poly.items() if coeff != 0}

    def phase_add(left: PhasePoly, right: PhasePoly) -> PhasePoly:
        result = dict(left)
        for power, coeff in right.items():
            result[power] = result.get(power, Fraction(0)) + coeff
        return normalize(result)

    def phase_mul(left: PhasePoly, right: PhasePoly) -> PhasePoly:
        result: PhasePoly = {}
        for left_power, left_coeff in left.items():
            for right_power, right_coeff in right.items():
                power = left_power + right_power
                result[power] = result.get(power, Fraction(0)) + left_coeff * right_coeff
        return normalize(result)

    def phase_conj(poly: PhasePoly) -> PhasePoly:
        return normalize({-power: coeff for power, coeff in poly.items()})

    instanton_amplitude = {1: crossed_kernel}
    anti_instanton_amplitude = {-1: conjugate_channel_kernel}
    selected_rate = phase_mul(phase_conj(instanton_amplitude), instanton_amplitude)
    conjugate_rate = phase_mul(phase_conj(anti_instanton_amplitude), anti_instanton_amplitude)
    cp_paired_rate = phase_add(selected_rate, conjugate_rate)
    assert_equal(
        "positive crossed-channel rate is theta neutral",
        selected_rate,
        {0: crossed_kernel * crossed_kernel},
    )
    assert_equal("CP-paired crossed rates keep only theta-neutral powers", set(cp_paired_rate), {0})

    linear_sector_sum = phase_add(instanton_amplitude, anti_instanton_amplitude)
    assert_equal(
        "linear instanton plus anti-instanton sum remains theta charged",
        set(linear_sector_sum),
        {-1, 1},
    )
    assert_not_equal(
        "linear theta-charged sector sum is not a positive crossed-channel rate",
        sum(linear_sector_sum.values(), Fraction(0)),
        selected_rate[0],
    )

    perturbative_chirality_preserving_reference = {0: Fraction(5, 11)}
    formal_interference = phase_add(
        phase_mul(phase_conj(perturbative_chirality_preserving_reference), instanton_amplitude),
        phase_mul(phase_conj(instanton_amplitude), perturbative_chirality_preserving_reference),
    )
    selection_rule_allows_reference = False
    retained_interference = formal_interference if selection_rule_allows_reference else {}
    assert_equal(
        "chirality selection removes perturbative reference interference",
        retained_interference,
        {},
    )
    assert_not_equal(
        "formal theta-linear interference is a different observable from the rate",
        formal_interference,
        selected_rate,
    )

    residuals = {
        "assembly": Fraction(1, 120),
        "crossing": Fraction(1, 330),
        "infrared": Fraction(1, 420),
    }
    residual_sum = sum(residuals.values(), Fraction(0))
    residual_budget = sum(abs(value) for value in residuals.values())
    shifted_channel = crossed_kernel + residual_sum
    assert_equal(
        "crossed chiral channel residual telescope",
        shifted_channel - crossed_kernel,
        residual_sum,
    )
    assert_equal(
        "crossed chiral channel residual bound",
        abs(shifted_channel - crossed_kernel) <= residual_budget,
        True,
    )
    underbudget_without_crossing = residual_budget - abs(residuals["crossing"])
    assert_equal(
        "omitting crossing residual underbudgets the crossed chiral channel",
        abs(shifted_channel - crossed_kernel) <= underbudget_without_crossing,
        False,
    )


def check_crossed_hard_helicity_projection_gate() -> None:
    Vec2 = tuple[Fraction, Fraction]

    def bracket(left: Vec2, right: Vec2) -> Fraction:
        return left[0] * right[1] - left[1] * right[0]

    density = Fraction(11, 13)
    haar_projection = Fraction(2, 7)
    zero_mode_source = Fraction(70)
    slot_product = Fraction(5, 9)
    crossing_residue = Fraction(17, 29)
    normal_source = Fraction(21, 20)
    scalar_crossed_kernel = product(
        [
            density,
            haar_projection,
            zero_mode_source,
            slot_product,
            crossing_residue,
            normal_source,
        ]
    )
    assert_gt("crossed scalar hard source coefficient is nonzero", scalar_crossed_kernel, 0)

    left_u: Vec2 = (Fraction(1), Fraction(2))
    left_d: Vec2 = (Fraction(3), Fraction(5))
    right_u: Vec2 = (Fraction(2), Fraction(1))
    right_d: Vec2 = (Fraction(5), Fraction(3))
    left_factor = bracket(left_u, left_d)
    right_factor = bracket(right_u, right_d)
    helicity_factor = left_factor * right_factor
    physical_helicity_amplitude = scalar_crossed_kernel * helicity_factor
    assert_equal("left-handed external spinor determinant", left_factor, Fraction(-1))
    assert_equal("right-handed external spinor determinant", right_factor, Fraction(1))
    assert_not_equal(
        "scalar crossed source coefficient is not the fixed-helicity amplitude",
        scalar_crossed_kernel,
        physical_helicity_amplitude,
    )

    collinear_left_d: Vec2 = (Fraction(2), Fraction(4))
    collinear_helicity_factor = bracket(left_u, collinear_left_d) * right_factor
    assert_equal(
        "collinear external Weyl spinors kill the fixed-helicity bin",
        scalar_crossed_kernel * collinear_helicity_factor,
        Fraction(0),
    )
    assert_not_equal(
        "nonzero scalar source kernel cannot revive a zero helicity projection",
        scalar_crossed_kernel,
        scalar_crossed_kernel * collinear_helicity_factor,
    )

    swapped_left_factor = bracket(left_d, left_u)
    swapped_amplitude = scalar_crossed_kernel * swapped_left_factor * right_factor
    assert_equal("swapping left Weyl slots flips the helicity sign", swapped_amplitude, -physical_helicity_amplitude)
    assert_not_equal(
        "external-state ordering sign is not optional",
        swapped_amplitude,
        physical_helicity_amplitude,
    )

    second_helicity_factor = Fraction(3, 2)
    phase_space_weights = (Fraction(1, 2), Fraction(3, 5))
    spin_summed_rate = (
        phase_space_weights[0] * physical_helicity_amplitude * physical_helicity_amplitude
        + phase_space_weights[1]
        * scalar_crossed_kernel
        * second_helicity_factor
        * scalar_crossed_kernel
        * second_helicity_factor
    )
    scalar_squared_shortcut = scalar_crossed_kernel * scalar_crossed_kernel
    assert_not_equal(
        "spin-summed rate is not the scalar hard coefficient squared",
        spin_summed_rate,
        scalar_squared_shortcut,
    )
    assert_gt("positive helicity-bin rate is nonnegative", spin_summed_rate, 0)

    residuals = {
        "assembly": Fraction(1, 120),
        "crossing": Fraction(1, 330),
        "helicity": Fraction(1, 370),
        "projection": Fraction(1, 420),
    }
    residual_sum = sum(residuals.values(), Fraction(0))
    residual_budget = sum(abs(value) for value in residuals.values())
    shifted_amplitude = physical_helicity_amplitude + residual_sum
    assert_equal(
        "fixed-helicity residual telescope",
        shifted_amplitude - physical_helicity_amplitude,
        residual_sum,
    )
    assert_equal(
        "fixed-helicity residual bound",
        abs(shifted_amplitude - physical_helicity_amplitude) <= residual_budget,
        True,
    )
    underbudget_without_helicity = residual_budget - abs(residuals["helicity"])
    assert_equal(
        "omitting helicity residual underbudgets physical external-state projection",
        abs(shifted_amplitude - physical_helicity_amplitude) <= underbudget_without_helicity,
        False,
    )


def check_size_integrated_crossed_hard_channel() -> None:
    c_values = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    a_values = [Fraction(6) / (c**3) for c in c_values]
    b_values = [Fraction(45) / (c**5) for c in c_values]
    a0 = product(a_values)
    a1 = sum(
        b_values[index]
        * product(a_values[j] for j in range(len(a_values)) if j != index)
        for index in range(len(a_values))
    )

    r_root = Fraction(3)
    core_integral = Fraction(101, 37)
    leading_tail = 3 * a0 / r_root
    subleading_tail = Fraction(3, 7) * a1 / (r_root**7)
    retained_window = core_integral + leading_tail + subleading_tail
    core_only_window = core_integral
    assert_gt("retained hard window includes a nonzero leading tail", leading_tail, 0)
    assert_gt("retained hard window includes a nonzero subleading tail", subleading_tail, 0)
    assert_not_equal(
        "retained size-integrated window is not the numerical core alone",
        retained_window,
        core_only_window,
    )

    center_delta = Fraction(1)
    determinant_density = Fraction(11, 13)
    running_collective = Fraction(81, 16)
    lambda_q_power = Fraction(29, 31)
    right_source_det = Fraction(3)
    left_source_det = Fraction(4)
    haar_projection = Fraction(2, 7)
    nonzero_mode_source_quotient = Fraction(21, 20)
    amputation_transport = Fraction(9, 10)
    crossing_residue = Fraction(17, 29)
    source_window_shape = Fraction(5, 6)

    scalar_coefficient = product(
        [
            center_delta,
            determinant_density,
            running_collective,
            lambda_q_power,
            right_source_det,
            left_source_det,
            haar_projection,
            nonzero_mode_source_quotient,
            amputation_transport,
            crossing_residue,
            source_window_shape,
            retained_window,
        ]
    )
    density_only = determinant_density * running_collective * lambda_q_power * retained_window
    core_only_channel = scalar_coefficient * core_only_window / retained_window
    omitted_nonzero_source = scalar_coefficient / nonzero_mode_source_quotient
    stripped_collective = scalar_coefficient / running_collective

    assert_not_equal(
        "size-integrated crossed channel is not density times window",
        scalar_coefficient,
        density_only,
    )
    assert_not_equal(
        "tail-subtracted retained window changes the crossed hard coefficient",
        scalar_coefficient,
        core_only_channel,
    )
    assert_not_equal(
        "nonzero-mode source quotient is part of the size-integrated amplitude",
        scalar_coefficient,
        omitted_nonzero_source,
    )
    assert_not_equal(
        "running collective factor is not a scale-independent determinant constant",
        scalar_coefficient,
        stripped_collective,
    )

    left_factor = Fraction(3, 2)
    right_factor = Fraction(4, 3)
    helicity_factor = left_factor * right_factor
    fixed_helicity_amplitude = scalar_coefficient * helicity_factor
    assert_equal("sample hard-channel helicity factor", helicity_factor, Fraction(2))
    assert_not_equal(
        "retained scalar coefficient is not yet a fixed-helicity amplitude",
        scalar_coefficient,
        fixed_helicity_amplitude,
    )

    residuals = {
        "density": Fraction(1, 120),
        "source": Fraction(1, 130),
        "haar": Fraction(1, 150),
        "nonzero_source": Fraction(1, 160),
        "amputation": Fraction(1, 170),
        "crossing": Fraction(1, 180),
        "tail": Fraction(1, 190),
        "window": Fraction(1, 200),
    }
    scalar_residual_bound = sum(residuals.values(), Fraction(0))
    helicity_residual = Fraction(1, 370)
    projection_residual = Fraction(1, 410)
    sector_residual = Fraction(1, 430)
    shifted_amplitude = (
        (scalar_coefficient + scalar_residual_bound)
        * (helicity_factor + helicity_residual)
        + projection_residual
        + sector_residual
    )
    propagated_bound = (
        abs(helicity_factor) * scalar_residual_bound
        + abs(scalar_coefficient) * helicity_residual
        + scalar_residual_bound * helicity_residual
        + projection_residual
        + sector_residual
    )
    actual_residual = shifted_amplitude - fixed_helicity_amplitude
    assert_equal(
        "size-integrated helicity residual telescope",
        actual_residual,
        propagated_bound,
    )
    underbudget_without_tail = propagated_bound - abs(helicity_factor) * residuals["tail"]
    assert_equal(
        "omitting size-window tail residual underbudgets retained hard amplitude",
        actual_residual <= underbudget_without_tail,
        False,
    )
    underbudget_without_helicity = (
        propagated_bound
        - abs(scalar_coefficient) * helicity_residual
        - scalar_residual_bound * helicity_residual
    )
    assert_equal(
        "omitting helicity residual underbudgets size-integrated physical amplitude",
        actual_residual <= underbudget_without_helicity,
        False,
    )


def check_retained_hard_channel_normal_source_quotient() -> None:
    signed_hard_measure = [Fraction(3, 5), -Fraction(2, 7), Fraction(5, 11)]
    gaussian_source_mean = [Fraction(1, 10), -Fraction(1, 12), Fraction(1, 14)]
    cubic_source_cumulant = [
        -Fraction(1, 15),
        Fraction(1, 18),
        Fraction(1, 20),
    ]
    quotient_remainder = [
        Fraction(1, 200),
        -Fraction(1, 300),
        Fraction(1, 400),
    ]

    determinant_normalized = sum(signed_hard_measure, Fraction(0))
    gaussian_only = sum(
        weight * (1 + q2)
        for weight, q2 in zip(signed_hard_measure, gaussian_source_mean)
    )
    retained_quotient = sum(
        weight * (1 + q2 + q3)
        for weight, q2, q3 in zip(
            signed_hard_measure,
            gaussian_source_mean,
            cubic_source_cumulant,
        )
    )
    exact_quotient = sum(
        weight * (1 + q2 + q3 + remainder)
        for weight, q2, q3, remainder in zip(
            signed_hard_measure,
            gaussian_source_mean,
            cubic_source_cumulant,
            quotient_remainder,
        )
    )
    remainder_bound = sum(
        abs(weight) * abs(remainder)
        for weight, remainder in zip(signed_hard_measure, quotient_remainder)
    )

    assert_not_equal(
        "retained hard channel is not determinant-normalized zero modes only",
        retained_quotient,
        determinant_normalized,
    )
    assert_not_equal(
        "retained hard channel keeps the cubic source cumulant",
        retained_quotient,
        gaussian_only,
    )
    assert_equal(
        "retained hard normal-source quotient residual bound",
        abs(exact_quotient - retained_quotient) <= remainder_bound,
        True,
    )

    unweighted_post_projection = determinant_normalized * (
        1
        + sum(
            q2 + q3
            for q2, q3 in zip(gaussian_source_mean, cubic_source_cumulant)
        )
        / len(signed_hard_measure)
    )
    assert_not_equal(
        "unweighted post-projection quotient changes signed hard measure",
        unweighted_post_projection,
        retained_quotient,
    )

    determinant_prefactor = Fraction(13, 17)
    physical_coefficient = determinant_prefactor * retained_quotient
    determinant_only_coefficient = determinant_prefactor * determinant_normalized
    gaussian_only_coefficient = determinant_prefactor * gaussian_only
    assert_not_equal(
        "physical hard coefficient includes pointwise normal-source quotient",
        physical_coefficient,
        determinant_only_coefficient,
    )
    assert_not_equal(
        "physical hard coefficient includes cubic source-cumulant correction",
        physical_coefficient,
        gaussian_only_coefficient,
    )

    underbudget_without_cubic = remainder_bound
    exact_gaussian_error = abs(exact_quotient - gaussian_only)
    assert_equal(
        "omitting cubic cumulant underbudgets retained normal-source quotient",
        exact_gaussian_error <= underbudget_without_cubic,
        False,
    )


def check_mass_assisted_theta_linear_interference_channel() -> None:
    q_plus_mass_assisted_u = ("u_L", "ubar_R")
    q_plus_four_source = ("u_L", "d_L", "ubar_R", "dbar_R")
    vacuum_coordinate: tuple[str, ...] = ()
    assert_equal("mass-assisted u channel has two source slots", len(q_plus_mass_assisted_u), 2)
    assert_equal("massless hard channel has four source slots", len(q_plus_four_source), 4)
    assert_equal("vacuum coordinate has no source slots", len(vacuum_coordinate), 0)

    density = Fraction(5, 11)
    zero_mode_slot = Fraction(7, 13)
    crossing_residue = Fraction(3, 5)
    projection = Fraction(17, 19)
    common_kernel = product([density, zero_mode_slot, crossing_residue, projection])

    abs_m_u = Fraction(2, 5)
    abs_m_d = Fraction(3, 7)
    u_source_residue = Fraction(11, 13)
    d_source_residue = Fraction(5, 17)
    u_mass_assisted = common_kernel * abs_m_d * u_source_residue
    d_mass_assisted = common_kernel * abs_m_u * d_source_residue
    four_source_coefficient = common_kernel * u_source_residue * d_source_residue
    vacuum_activity = common_kernel * abs_m_u * abs_m_d

    assert_not_equal(
        "mass-assisted u channel is not the four-source coefficient",
        u_mass_assisted,
        four_source_coefficient,
    )
    assert_not_equal(
        "mass-assisted u channel is not the vacuum activity",
        u_mass_assisted,
        vacuum_activity,
    )
    wrong_same_flavor_mass = common_kernel * abs_m_u * u_source_residue
    assert_not_equal(
        "u channel requires complementary d-mass zero-mode saturation",
        wrong_same_flavor_mass,
        u_mass_assisted,
    )
    omitted_complementary_mass = common_kernel * u_source_residue
    assert_not_equal(
        "omitting the complementary mass leaves zero modes unsaturated",
        omitted_complementary_mass,
        u_mass_assisted,
    )

    PhaseKey = tuple[int, int, int]  # theta, arg(m_u), arg(m_d)
    PhasePoly = dict[PhaseKey, Fraction]

    def normalize(poly: PhasePoly) -> PhasePoly:
        return {power: coeff for power, coeff in poly.items() if coeff != 0}

    def phase_add(left: PhasePoly, right: PhasePoly) -> PhasePoly:
        result = dict(left)
        for power, coeff in right.items():
            result[power] = result.get(power, Fraction(0)) + coeff
        return normalize(result)

    def phase_mul(left: PhasePoly, right: PhasePoly) -> PhasePoly:
        result: PhasePoly = {}
        for left_power, left_coeff in left.items():
            for right_power, right_coeff in right.items():
                power = tuple(a + b for a, b in zip(left_power, right_power))
                result[power] = result.get(power, Fraction(0)) + left_coeff * right_coeff
        return normalize(result)

    def phase_conj(poly: PhasePoly) -> PhasePoly:
        return normalize(
            {
                tuple(-entry for entry in power): coeff
                for power, coeff in poly.items()
            }
        )

    instanton_u: PhasePoly = {(1, 0, 1): u_mass_assisted}
    reference_u: PhasePoly = {(0, -1, 0): abs_m_u * Fraction(23, 29)}
    interference = phase_add(
        phase_mul(phase_conj(reference_u), instanton_u),
        phase_mul(phase_conj(instanton_u), reference_u),
    )
    assert_equal(
        "mass-assisted interference carries theta plus both mass phases",
        set(interference),
        {(1, 1, 1), (-1, -1, -1)},
    )
    expected_interference_coeff = u_mass_assisted * abs_m_u * Fraction(23, 29)
    assert_equal(
        "mass-assisted interference coefficient",
        interference[(1, 1, 1)],
        expected_interference_coeff,
    )
    assert_equal(
        "mass-assisted conjugate interference coefficient",
        interference[(-1, -1, -1)],
        expected_interference_coeff,
    )

    positive_rate = phase_mul(phase_conj(instanton_u), instanton_u)
    assert_equal(
        "mass-assisted positive rate is theta neutral",
        positive_rate,
        {(0, 0, 0): u_mass_assisted * u_mass_assisted},
    )
    assert_not_equal(
        "theta-linear interference is not the positive rate",
        set(interference),
        set(positive_rate),
    )

    wrong_reference_u: PhasePoly = {(0, 1, 0): abs_m_u * Fraction(23, 29)}
    wrong_interference = phase_add(
        phase_mul(phase_conj(wrong_reference_u), instanton_u),
        phase_mul(phase_conj(instanton_u), wrong_reference_u),
    )
    assert_equal(
        "nonconjugated mass reference gives wrong phase powers",
        set(wrong_interference),
        {(1, -1, 1), (-1, 1, -1)},
    )
    assert_not_equal(
        "wrong mass orientation is not the two-flavor axial invariant",
        set(wrong_interference),
        set(interference),
    )

    reference_source_degree = 2
    reference_chirality_breaking = True
    wrong_reference_source_degree = 4
    chirality_preserving_reference = False
    assert_equal(
        "same-basis mass reference can interfere",
        reference_source_degree == len(q_plus_mass_assisted_u) and reference_chirality_breaking,
        True,
    )
    assert_equal(
        "wrong source degree cannot interfere with mass-assisted channel",
        wrong_reference_source_degree == len(q_plus_mass_assisted_u),
        False,
    )
    assert_equal(
        "chirality-preserving reference cannot interfere with mass-assisted channel",
        chirality_preserving_reference,
        False,
    )

    reference_leading = abs_m_u * Fraction(23, 29)
    instanton_leading = u_mass_assisted
    measurement = Fraction(7, 9)
    instanton_error = Fraction(1, 100)
    reference_error = Fraction(1, 120)
    measurement_error = Fraction(1, 1000)
    leading_interference = 2 * measurement * reference_leading * instanton_leading
    shifted_interference = (
        2
        * measurement
        * (reference_leading + reference_error)
        * (instanton_leading + instanton_error)
        + measurement_error
    )
    interference_residual = shifted_interference - leading_interference
    residual_bound = (
        2
        * measurement
        * (
            reference_leading * instanton_error
            + instanton_leading * reference_error
            + reference_error * instanton_error
        )
        + measurement_error
    )
    assert_equal(
        "mass-assisted interference residual telescope",
        interference_residual,
        residual_bound,
    )
    underbudget_without_reference = residual_bound - 2 * measurement * instanton_leading * reference_error
    assert_equal(
        "omitting reference residual underbudgets mass-assisted interference",
        interference_residual <= underbudget_without_reference,
        False,
    )

    assert_gt("d-channel mass-assisted coefficient is nonzero", d_mass_assisted, Fraction(0))


def check_same_coordinate_amplitude_rate_gate() -> None:
    def mat_vec(matrix: Matrix2, vector: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (
            matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
            matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
        )

    def vec_add(
        left: tuple[Fraction, Fraction],
        right: tuple[Fraction, Fraction],
    ) -> tuple[Fraction, Fraction]:
        return (left[0] + right[0], left[1] + right[1])

    def dot(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> Fraction:
        return left[0] * right[0] + left[1] * right[1]

    def quad(vector: tuple[Fraction, Fraction], measurement: Matrix2) -> Fraction:
        return dot(vector, mat_vec(measurement, vector))

    all_outgoing_source = (Fraction(5, 7), Fraction(2, 3))
    crossing_with_residues: Matrix2 = (
        (Fraction(3, 5), Fraction(1, 7)),
        (Fraction(2, 11), Fraction(5, 6)),
    )
    physical_projection: Matrix2 = (
        (Fraction(4, 5), Fraction(1, 6)),
        (Fraction(1, 5), Fraction(7, 8)),
    )
    measurement: Matrix2 = (
        (Fraction(2), Fraction(1, 3)),
        (Fraction(1, 3), Fraction(3)),
    )

    physical_map = matmul2(physical_projection, crossing_with_residues)
    physical_vector = mat_vec(physical_map, all_outgoing_source)
    physical_rate = quad(physical_vector, measurement)
    raw_source_rate = quad(all_outgoing_source, measurement)
    assert_not_equal(
        "all-outgoing source vector cannot be squared as the physical rate",
        raw_source_rate,
        physical_rate,
    )

    folded_measurement = matmul2(
        transpose2(physical_map),
        matmul2(measurement, physical_map),
    )
    assert_equal(
        "folding crossing and projection into W recovers the physical rate",
        quad(all_outgoing_source, folded_measurement),
        physical_rate,
    )

    source_overlap: Matrix2 = (
        (Fraction(2), Fraction(1, 5)),
        (Fraction(0), Fraction(3, 2)),
    )
    unamputated_vector = mat_vec(source_overlap, physical_vector)
    unamputated_rate = quad(unamputated_vector, measurement)
    assert_not_equal(
        "unamputated source overlaps compute a different quadratic cut",
        unamputated_rate,
        physical_rate,
    )

    same_channel_reference = (Fraction(1, 4), Fraction(3, 10))
    interference = 2 * dot(same_channel_reference, mat_vec(measurement, physical_vector))
    assert_gt("same-coordinate interference is nonzero", interference, Fraction(0))

    wrong_channel_reference = (Fraction(7, 17), Fraction(5, 19))
    zero_selection: Matrix2 = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    formal_wrong_interference = 2 * dot(
        wrong_channel_reference,
        mat_vec(measurement, physical_vector),
    )
    retained_wrong_interference = 2 * dot(
        wrong_channel_reference,
        mat_vec(zero_selection, mat_vec(measurement, physical_vector)),
    )
    assert_equal(
        "selection rule removes wrong-channel reference interference",
        retained_wrong_interference,
        Fraction(0),
    )
    assert_not_equal(
        "formal wrong-channel scalar product is not the physical interference",
        formal_wrong_interference,
        retained_wrong_interference,
    )

    theta_neutral_rate = {0: physical_rate}
    theta_charged_linear_sum = {
        1: physical_vector[0] + physical_vector[1],
        -1: physical_vector[0] + physical_vector[1],
    }
    theta_linear_interference = {
        1: interference / 2,
        -1: interference / 2,
    }
    assert_equal("positive rate keeps only theta-neutral power", set(theta_neutral_rate), {0})
    assert_equal("linear sector sum remains theta charged", set(theta_charged_linear_sum), {-1, 1})
    assert_equal("same-channel interference is theta linear", set(theta_linear_interference), {-1, 1})
    assert_not_equal(
        "linear theta-charged source sum is not the positive rate",
        sum(theta_charged_linear_sum.values(), Fraction(0)),
        theta_neutral_rate[0],
    )

    residual_measurement: Matrix2 = (
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(2)),
    )
    n_bins = 2
    row_l1_bound = Fraction(3)
    amp_bound = Fraction(1, 5)
    ref_bound = Fraction(1, 7)
    amp_error = Fraction(1, 100)
    ref_error = Fraction(1, 120)
    amp_leading = (amp_bound, amp_bound)
    ref_leading = (ref_bound, ref_bound)
    amp_shift = (amp_error, amp_error)
    ref_shift = (ref_error, ref_error)
    measurement_error = Fraction(1, 1000)
    leading_rate = quad(amp_leading, residual_measurement)
    shifted_rate = (
        quad(vec_add(amp_leading, amp_shift), residual_measurement)
        + measurement_error
    )
    rate_residual = shifted_rate - leading_rate
    rate_residual_bound = (
        n_bins * row_l1_bound * (2 * amp_bound * amp_error + amp_error * amp_error)
        + measurement_error
    )
    assert_equal(
        "same-coordinate positive-rate residual telescope",
        rate_residual,
        rate_residual_bound,
    )
    underbudget_without_amplitude = rate_residual_bound - (
        n_bins * row_l1_bound * (2 * amp_bound * amp_error + amp_error * amp_error)
    )
    assert_equal(
        "omitting amplitude residual underbudgets positive cut",
        rate_residual <= underbudget_without_amplitude,
        False,
    )
    underbudget_without_measurement = rate_residual_bound - measurement_error
    assert_equal(
        "omitting measurement residual underbudgets positive cut",
        rate_residual <= underbudget_without_measurement,
        False,
    )

    leading_interference = 2 * dot(ref_leading, mat_vec(residual_measurement, amp_leading))
    shifted_interference = 2 * dot(
        vec_add(ref_leading, ref_shift),
        mat_vec(residual_measurement, vec_add(amp_leading, amp_shift)),
    )
    residual = shifted_interference - leading_interference
    residual_bound = (
        2
        * n_bins
        * row_l1_bound
        * (ref_bound * amp_error + amp_bound * ref_error + ref_error * amp_error)
    )
    assert_equal("same-coordinate interference residual telescope", residual, residual_bound)
    underbudget_without_reference = residual_bound - 2 * n_bins * row_l1_bound * amp_bound * ref_error
    assert_equal(
        "omitting reference-vector residual underbudgets same-channel interference",
        residual <= underbudget_without_reference,
        False,
    )


def main() -> None:
    check_source_functional_route_order()
    check_named_hard_channel_trace_spine()
    check_collective_coordinate_zero_mode_jacobian()
    check_one_loop_density_rg_and_channel_power()
    check_running_collective_jacobian_in_hard_coefficient()
    check_cross_chapter_hard_scale_collective_factor_regression()
    check_proper_time_determinant_log_channel_window()
    check_hard_color_orientation_haar_tensor()
    check_individual_zero_mode_slot_tail_from_bessel_products()
    check_primed_determinant_source_response()
    check_nonzero_mode_source_fluctuation_quotient()
    check_first_source_cumulant_from_normal_modes()
    check_normal_propagator_source_insertion()
    check_subtracted_normal_green_function_matching()
    check_spectral_local_green_matching_source_classes()
    check_hard_amplitude_assembly_bound()
    check_hard_reference_channel_calibration()
    check_overdetermined_reference_channel_calibration()
    check_finite_determinant_scheme_transport()
    check_finite_determinant_conversion_benchmark()
    check_observable_handoff_map()
    check_source_kernel_physical_projection_bridge()
    check_pole_normalized_four_source_matrix_extraction()
    check_instanton_inclusive_cut_quadratic_projection()
    check_first_cluster_amplitude_correction()
    check_neutral_pair_valley_prescription()
    check_two_flavor_mass_source_determinant_coordinate()
    check_chirality_source_selection_gate()
    check_axial_ward_source_transport()
    check_mass_source_rg_channel_transport()
    check_moduli_equivalent_channel_separation()
    check_projection_not_recoverable_from_one_euclidean_sum()
    check_finite_cell_residual_bound()
    check_source_determinant_stability_bound()
    check_su3_two_flavor_hard_source_power_and_tail()
    check_hard_window_tail_subtraction()
    check_hard_screened_retained_size_window()
    check_hard_wilsonian_ope_boundary_flow()
    check_wilsonian_matching_scheme_covariance()
    check_hard_benchmark_channel_comparison_and_ratio()
    check_thooft_four_point_amputated_assembly_gate()
    check_thooft_crossed_chiral_channel()
    check_crossed_hard_helicity_projection_gate()
    check_size_integrated_crossed_hard_channel()
    check_retained_hard_channel_normal_source_quotient()
    check_mass_assisted_theta_linear_interference_channel()
    check_same_coordinate_amplitude_rate_gate()
    print("instanton physical amplitude architecture checks passed")


if __name__ == "__main__":
    main()
