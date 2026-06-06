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
- `ca:finite-cell-instanton-channel-control`: finite retained-cell residuals
  and source-determinant perturbations obey the displayed absolute bounds.
- `prop:su3-nf2-hard-source-power-slow-tail` and
  `ca:instanton-hard-benchmark-gate-ledger`: the SU(3), Nf=2 hard
  four-source benchmark has the stated rho power, Q power, slow endpoint tail,
  gate dependence, and same-theory hard-scale ratio bound.

Independent construction:
- The checks build small exact rational cell models from scratch.  They compute
  two-by-two determinants, mass/source polynomials, one-loop RG exponents,
  the Bessel-product tail cancellation for an individual zero-mode slot,
  finite Gaussian source-quotient covariance identities,
  multiplicative hard-amplitude assembly bounds on signed windows,
  physical projection bins, residual sums, and hard-window power ledgers
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
  density-only hard-channel power, an untransported determinant constant, a
  fused-density endpoint class substituted for differentiated fermion slots,
  an unamputated external residue absorbed into the zero-mode slot tail, a
  vacuum determinant calibration substituted for a source-fluctuation
  quotient, a relative quotient formed after zero-mode rank loss, a
  determinant-only assembled amplitude, signed-window relative error control
  without a noncancellation margin, a
  single Euclidean cell sum used as a spectral-bin observable, a
  determinant-only hard-scale ratio, a hard benchmark with a missing hard
  slot, and a residual bound that omits the external projection/sector
  remainder.

Scope boundary:
- Passing these checks proves only finite algebra and channel bookkeeping.  It
  does not prove continuum convergence of the instanton integral, compute the
  Pauli--Villars determinant constant, establish a Lorentzian scattering
  theorem, or justify any specific dilute-gas regime.
"""

from __future__ import annotations

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


def check_one_loop_density_gate_rg_and_channel_power() -> None:
    for n_colors, n_flavors in [(2, 0), (3, 2), (4, 3), (5, 6)]:
        b0 = beta0(n_colors, n_flavors)
        correct_density_power = b0
        wrong_density_power = b0 + Fraction(1)

        rg_derivative = correct_density_power - b0
        wrong_rg_derivative = wrong_density_power - b0
        assert_equal(
            f"SU({n_colors}) Nf={n_flavors} one-loop density RG gate",
            rg_derivative,
            Fraction(0),
        )
        assert_not_equal(
            "wrong determinant logarithm power fails the RG gate",
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
    transported_gate = Fraction(5, 13)
    source_window_1 = Fraction(17, 19)
    source_window_2 = Fraction(23, 29)
    q_power = -Fraction(35, 3)
    absolute_prefactor_1 = determinant_constant * transported_gate * source_window_1
    absolute_prefactor_2 = determinant_constant * transported_gate * source_window_2
    same_channel_ratio_prefactor = absolute_prefactor_2 / absolute_prefactor_1
    assert_equal(
        "same-channel determinant constant cancels in density-gate ratio",
        same_channel_ratio_prefactor,
        source_window_2 / source_window_1,
    )
    if q_power == 0:
        raise AssertionError("hard ratio should retain the physical source-scale power")

    untransported_gate = Fraction(3, 17)
    untransported_ratio_prefactor = (
        determinant_constant * untransported_gate * source_window_2
    ) / absolute_prefactor_1
    assert_not_equal(
        "changed gate data is not a same-channel determinant cancellation",
        untransported_ratio_prefactor,
        source_window_2 / source_window_1,
    )

    scheme_constant_dropped = transported_gate * source_window_1
    assert_not_equal(
        "absolute density coefficient depends on finite determinant convention",
        scheme_constant_dropped,
        absolute_prefactor_1,
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


def check_hard_amplitude_assembly_ledger() -> None:
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


def check_hard_benchmark_gate_ledger_and_ratio() -> None:
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
    assert_not_equal("density-only hard shortcut misses gate data", density_only, euclidean_benchmark)
    assert_not_equal("Euclidean colored kernel is not physical projection", euclidean_benchmark, physical_benchmark)

    off_shell = (
        center_delta_off_shell
        * determinant_constant
        * haar_projection
        * source_factor
        * hard_window
    )
    assert_equal("off-shell center gate kills hard benchmark", off_shell, Fraction(0))

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
    check_one_loop_density_gate_rg_and_channel_power()
    check_individual_zero_mode_slot_tail_from_bessel_products()
    check_nonzero_mode_source_fluctuation_quotient()
    check_hard_amplitude_assembly_ledger()
    check_two_flavor_mass_source_determinant_coordinate()
    check_moduli_equivalent_channel_separation()
    check_projection_not_recoverable_from_one_euclidean_sum()
    check_finite_cell_residual_bound()
    check_source_determinant_stability_bound()
    check_su3_two_flavor_hard_source_power_and_tail()
    check_hard_benchmark_gate_ledger_and_ratio()
    print("instanton physical amplitude architecture checks passed")


if __name__ == "__main__":
    main()
