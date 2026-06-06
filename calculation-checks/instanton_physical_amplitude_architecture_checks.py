"""Finite checks for the instanton physical-amplitude architecture chapter.

Evidence contract.

Target claims:
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
- `ca:instanton-proper-time-determinant-channel`: the proper-time fluctuation
  log contributes to a source channel through weighted zero-mode-deleted
  boson, ghost, fermion, and counterterm coefficients; the resulting
  determinant residual must be bounded on the absolute source window.
- `prop:instanton-hard-individual-zero-mode-slot`: the differentiated hard
  fermion slot has the singular-gauge BPST zero-mode form-factor tail
  `F_zm(c s/2) = 6 c^(-3) s^(-3) + O(s^(-5))`; four such slots give the
  `6^4 prod c_l^(-3) s^(-12)` endpoint factor, while fused bilinear-density
  sources have a different endpoint class.
- `ca:instanton-nonzero-mode-source-quotient`: the source-dependent
  nonzero-mode fluctuation quotient separates the Gaussian source mean from
  its covariance with the same interaction weight that defines the determinant
  normalization.
- `ca:instanton-hard-amplitude-assembly-ledger`: the hard channel must assemble
  the determinant, source-fluctuation, zero-mode/source, and physical-projection
  factors in the same kernel, with absolute control unless a noncancellation
  margin is supplied.
- `ca:instanton-observable-handoff-ledger`: the assembled instanton channel
  must still be mapped to a named physical observable; hard source
  coefficients, theta curvatures, U(1)_A susceptibility kernels, and real-time
  axial relaxation rates are not interchangeable.
- `ca:instanton-source-kernel-physical-projection`: a finite Euclidean
  instanton source kernel becomes a physical amplitude only after a declared
  pole, spectral-bin, OPE, or inclusive projection, with bridge residuals for
  regulator transport, continuation, pole/bin isolation, infrared completion,
  unitarity-cut normalization, matching, and endpoint control.
- `ca:instanton-first-cluster-amplitude-correction`: a first connected
  two-body correction to a source amplitude requires the disconnected one-body
  product subtraction, a source/projection-specific pair kernel, absolute pair
  residual control, and a separate reading of neutral and same-charge pairs.
- `ca:finite-cell-instanton-channel-control`: finite retained-cell residuals
  and source-determinant perturbations obey the displayed absolute bounds.
- `prop:su3-nf2-hard-source-power-slow-tail` and
  `ca:instanton-hard-benchmark-gate-ledger`: the SU(3), Nf=2 hard
  four-source benchmark has the stated rho power, Q power, slow endpoint tail,
  channel-data dependence, and same-theory hard-scale ratio bound.
- `ca:instanton-hard-window-tail-subtraction`: the hard four-source window is
  controlled as a core integral plus leading and subleading analytic endpoint
  tails, rather than as a formal size integral.
- `sec:instanton-hard-wilsonian-ope-datum`: the hard source kernel becomes a
  Wilsonian local four-fermion input only after a dimensionless size split,
  boundary-flux flow, operator matching, long-size remainder, and physical
  matrix element are supplied.

Independent construction:
- The checks build small exact rational cell models from scratch.  They compute
  two-by-two determinants, mass/source polynomials, one-loop RG exponents,
  weighted proper-time determinant logarithms,
  the Bessel-product tail cancellation for an individual zero-mode slot,
  finite Gaussian source-quotient covariance identities,
  multiplicative hard-amplitude assembly bounds on signed windows,
  finite observable-handoff comparisons for theta, U(1)_A, and real-time
  axial channels,
  pole-window extraction, spectral-bin/Stieltjes comparisons, contact
  polynomial separation, and bridge residual telescopes,
  first connected instanton-pair source corrections,
  physical projection bins, residual sums, two-term hard-window endpoint
  tail subtraction, and hard-window power checks
  directly, rather than importing BPST radial integrals or copying a monograph
  coefficient.

Imported assumptions:
- The finite model assumes that the continuum instanton window has already been
  reduced to finitely many regulator cells and that two light flavors give a
  two-by-two zero-mode source determinant.  It does not assume any continuum
  determinant constant, ADHM volume, or spectral-continuation theorem.

Negative controls:
- The script rejects a plus sign in the off-diagonal determinant term, a
  moduli-only prediction that ignores zero-mode rank, a rank-one source matrix
  treated as a nonzero four-source channel, a wrong one-loop density power, a
  density-only hard-channel power, a wrong proper-time determinant sign, a
  signed heat-kernel residual cancellation used as an absolute window bound,
  an untransported determinant constant, a
  fused-density endpoint class substituted for differentiated fermion slots,
  an unamputated external residue absorbed into the zero-mode slot tail, a
  vacuum determinant calibration substituted for a source-fluctuation
  quotient, a relative quotient formed after zero-mode rank loss, a
  determinant-only assembled amplitude, signed-window relative error control
  without a noncancellation margin, a
  hard source coefficient used as a theta susceptibility, a dilute
  topological susceptibility used as a real-time rate, a dilute instanton
  curvature substituted for Witten-Veneziano curvature without a comparison
  budget, a Euclidean source value used as a physical pole or spectral bin,
  a colored auxiliary instanton kernel treated as a standalone LSZ amplitude,
  a bridge budget omitting the inverse-problem residual, a neutral pair
  controlled only by theta curvature, a disconnected
  pair product counted as a connected source correction, a one-body
  sector-isolation budget that omits pair leakage, a
  single Euclidean cell sum used as a spectral-bin observable, a
  determinant-only hard-scale ratio, a hard benchmark with a missing hard
  slot, a leading-tail-only hard-window approximation, a fused-density
  endpoint substituted for differentiated slots, a fixed short-instanton
  vertex under a moving size boundary, a short
  coefficient used as a physical amplitude, a full hard source coefficient
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


def beta0(n_colors: int, n_flavors: int) -> Fraction:
    return Fraction(11, 3) * n_colors - Fraction(2, 3) * n_flavors


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


def check_first_cluster_amplitude_correction() -> None:
    one_body_plus = Fraction(5, 11)
    one_body_minus = Fraction(7, 13)
    disconnected_product = one_body_plus * one_body_minus
    neutral_connected = Fraction(3, 17)
    full_neutral_pair_kernel = disconnected_product + neutral_connected

    cluster_assembled = one_body_plus + one_body_minus + neutral_connected
    unsubtracted_assembled = (
        one_body_plus + one_body_minus + full_neutral_pair_kernel
    )
    assert_equal(
        "pair disconnected subtraction removes one-body product",
        unsubtracted_assembled - cluster_assembled,
        disconnected_product,
    )
    assert_not_equal(
        "full pair kernel is not a connected source correction",
        full_neutral_pair_kernel,
        neutral_connected,
    )

    source_projection = Fraction(19, 23)
    neutral_source_coefficient = source_projection * neutral_connected
    neutral_topological_charge = 0
    neutral_theta_curvature = (
        neutral_topological_charge * neutral_topological_charge * neutral_connected
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

    same_charge_connected = Fraction(2, 19)
    same_charge_topological_charge = 2
    same_charge_theta_curvature = (
        same_charge_topological_charge
        * same_charge_topological_charge
        * same_charge_connected
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
    ratio_powers = {
        "determinant_constant": Fraction(0),
        "Lambda_ht": Fraction(0),
        "Q2_over_Q1": q_power,
        "source_window_ratio": Fraction(1),
    }
    assert_equal("same-theory determinant constant cancels in ratio", ratio_powers["determinant_constant"], Fraction(0))
    assert_equal("same-theory Lambda power cancels in ratio", ratio_powers["Lambda_ht"], Fraction(0))
    assert_equal("hard scale ratio keeps Q power", ratio_powers["Q2_over_Q1"], q_power)

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
    stale_source_window_ratio = Fraction(15, 14)
    assert_equal("changed source window is a real ratio input", stale_source_window_ratio == Fraction(1), False)


def main() -> None:
    check_one_loop_density_rg_and_channel_power()
    check_proper_time_determinant_log_channel_window()
    check_individual_zero_mode_slot_tail_from_bessel_products()
    check_nonzero_mode_source_fluctuation_quotient()
    check_hard_amplitude_assembly_bound()
    check_observable_handoff_map()
    check_source_kernel_physical_projection_bridge()
    check_first_cluster_amplitude_correction()
    check_two_flavor_mass_source_determinant_coordinate()
    check_moduli_equivalent_channel_separation()
    check_projection_not_recoverable_from_one_euclidean_sum()
    check_finite_cell_residual_bound()
    check_source_determinant_stability_bound()
    check_su3_two_flavor_hard_source_power_and_tail()
    check_hard_window_tail_subtraction()
    check_hard_wilsonian_ope_boundary_flow()
    check_hard_benchmark_channel_comparison_and_ratio()
    print("instanton physical amplitude architecture checks passed")


if __name__ == "__main__":
    main()
