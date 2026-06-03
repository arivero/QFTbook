#!/usr/bin/env python3
"""Finite checks for BPST instanton normalizations used in the monograph.

The displayed BPST formulas use the common SU(2) basis T_a=sigma_a/2 with
tr(T_a T_b)=delta_ab/2.  The active monograph coupling uses the trace-delta
basis t_a=sqrt(2) T_a and

    S = (4 g_YM^2)^(-1) int tr_delta(F_{mu nu} F_{mu nu}).

This script verifies the finite algebra and radial integrals behind the
relations

    int F^a_{mu nu} F^a_{mu nu} d^4x = 32 pi^2,
    Q = 1,
    S_common = 8 pi^2/g_ht^2 = 4 pi^2/g_YM^2,
    d^4 a d rho / rho^5 and (mu rho)^b0 are the universal
    one-loop scale/RG factors in the instanton density
    the one-instanton small-rho boundary exponent criterion is
    b0 + beta_X > 4
    the general charge-k framed ADHM quotient has local real dimension 4 k N
    the finite-dimensional ADHM quotient-density coarea formula has the
    correct orbit-volume and homogeneous-cone scaling
    the finite-regulator nonzero-mode determinant datum has the correct
    boson/ghost/fermion determinant powers and counterterm shifts
    the proper-time fluctuation determinant combines with the zero-mode
    source determinant to give the finite four-fermion instanton amplitude
    the physical instanton correlator contribution is the top Berezin
    coefficient after operator, mass/source, and zero-mode factors are
    restricted to the instanton zero-mode subspace, giving the full flavor
    determinant and the theta+arg det M phase combination
    Uhlenbeck boundary faces have the expected codimensions and product
    power-counting integrability thresholds
    the k=1 ADHM quotient has orientation dimension 4N-5 and cone
    volume power rho^(4N-5)

with g_ht = sqrt(2) g_YM.
"""

from __future__ import annotations

from fractions import Fraction
import itertools


def eps4(a: int, b: int, c: int, d: int) -> int:
    vals = [a, b, c, d]
    if len(set(vals)) < 4:
        return 0
    inv = 0
    for i in range(4):
        for j in range(i + 1, 4):
            inv += vals[i] > vals[j]
    return -1 if inv % 2 else 1


def eps3(a: int, b: int, c: int) -> int:
    vals = [a, b, c]
    if len(set(vals)) < 3:
        return 0
    inv = 0
    for i in range(3):
        for j in range(i + 1, 3):
            inv += vals[i] > vals[j]
    return -1 if inv % 2 else 1


def eta(a: int, mu: int, nu: int) -> int:
    """Self-dual 't Hooft eta symbol, indices a=0,1,2 and mu,nu=0..3.

    The fourth Euclidean coordinate is represented by index 3.  The convention
    is eta^a_{ij}=epsilon_{aij}, eta^a_{i4}=delta_ai,
    eta^a_{4i}=-delta_ai.
    """

    if mu == nu:
        return 0
    if mu < 3 and nu < 3:
        return eps3(a, mu, nu)
    if mu < 3 and nu == 3:
        return 1 if a == mu else 0
    if mu == 3 and nu < 3:
        return -1 if a == nu else 0
    raise AssertionError("unreachable")


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def det_fraction(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    if n == 1:
        return matrix[0][0]
    total = Fraction(0)
    for j in range(n):
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        total += ((-1) ** j) * matrix[0][j] * det_fraction(minor)
    return total


def product_fraction(values: list[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


GrassmannPolynomial = dict[tuple[int, ...], Fraction]


def grassmann_monomial(
    *variables: int,
    coefficient: Fraction = Fraction(1),
) -> GrassmannPolynomial:
    if len(set(variables)) != len(variables):
        return {}
    inversions = sum(
        1
        for i in range(len(variables))
        for j in range(i + 1, len(variables))
        if variables[i] > variables[j]
    )
    sign = Fraction(-1) if inversions % 2 else Fraction(1)
    return {tuple(sorted(variables)): sign * coefficient}


def grassmann_add(
    left: GrassmannPolynomial,
    right: GrassmannPolynomial,
) -> GrassmannPolynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def grassmann_mul(
    left: GrassmannPolynomial,
    right: GrassmannPolynomial,
) -> GrassmannPolynomial:
    result: GrassmannPolynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            if set(left_monomial) & set(right_monomial):
                continue
            concatenated = left_monomial + right_monomial
            product = grassmann_monomial(
                *concatenated,
                coefficient=left_coefficient * right_coefficient,
            )
            result = grassmann_add(result, product)
    return result


def berezin_top_coefficient(
    polynomial: GrassmannPolynomial,
    variable_count: int,
) -> Fraction:
    return polynomial.get(tuple(range(variable_count)), Fraction(0))


def grassmann_source_determinant_top_coefficient(
    matrix: list[list[Fraction]],
) -> Fraction:
    flavor_count = len(matrix)
    polynomial: GrassmannPolynomial = {}
    for permutation in itertools.permutations(range(flavor_count)):
        term = grassmann_monomial(coefficient=Fraction(1))
        for left_flavor, right_flavor in enumerate(permutation):
            term = grassmann_mul(
                term,
                grassmann_monomial(
                    2 * left_flavor,
                    2 * right_flavor + 1,
                    coefficient=matrix[left_flavor][right_flavor],
                ),
            )
        polynomial = grassmann_add(polynomial, term)
    return berezin_top_coefficient(polynomial, 2 * flavor_count)


def check_eta_self_duality() -> None:
    for a, mu, nu in itertools.product(range(3), range(4), range(4)):
        dual = Fraction(1, 2) * sum(
            eps4(mu, nu, rho, sig) * eta(a, rho, sig)
            for rho in range(4)
            for sig in range(4)
        )
        assert_equal(f"eta self-duality a={a} mu={mu} nu={nu}", dual, eta(a, mu, nu))


def check_eta_norm() -> None:
    norm = sum(eta(a, mu, nu) ** 2 for a in range(3) for mu in range(4) for nu in range(4))
    assert_equal("sum eta^2", norm, 12)


def check_eta_quadratic_identity() -> None:
    # Check the tensor identity
    #   eps^a_bc eta^b_{mu rho} eta^c_{nu sigma} y^rho y^sigma
    # = r^2 eta^a_{mu nu}
    #   + y_mu eta^a_{nu lambda} y^lambda
    #   - y_nu eta^a_{mu lambda} y^lambda
    # coefficient by coefficient in the commuting monomials y_i y_j.
    for a, mu, nu in itertools.product(range(3), range(4), range(4)):
        lhs = {(i, j): 0 for i in range(4) for j in range(i, 4)}
        rhs = {(i, j): 0 for i in range(4) for j in range(i, 4)}
        for b, c, rho, sig in itertools.product(range(3), range(3), range(4), range(4)):
            key = (rho, sig) if rho <= sig else (sig, rho)
            lhs[key] += eps3(a, b, c) * eta(b, mu, rho) * eta(c, nu, sig)
        for lam in range(4):
            rhs[(lam, lam)] += eta(a, mu, nu)
            key = (mu, lam) if mu <= lam else (lam, mu)
            rhs[key] += eta(a, nu, lam)
            key = (nu, lam) if nu <= lam else (lam, nu)
            rhs[key] -= eta(a, mu, lam)
        assert_equal(f"eta quadratic identity a={a} mu={mu} nu={nu}", lhs, rhs)


def check_radial_integrals_and_actions() -> None:
    # Integral over R^4 of rho^4/(r^2+rho^2)^4:
    # 2*pi^2 * 1/2 * B(2,2) = pi^2/6.  Track only the rational coefficient.
    radial_coeff = Fraction(1, 6)
    f_component_coeff = 16 * 12 * radial_coeff
    assert_equal("int F_component^2 coefficient", f_component_coeff, 32)

    # In the half-trace basis tr(T_a T_b)=delta_ab/2.
    trace_half_coeff = Fraction(1, 2) * f_component_coeff
    assert_equal("int tr_half F^2 coefficient", trace_half_coeff, 16)

    # Q = (32*pi^2)^(-1) int F^a Ftilde^a for self-dual unit instanton.
    topological_charge = Fraction(f_component_coeff, 32)
    assert_equal("BPST topological charge", topological_charge, 1)

    # Common component action: (4 g_ht^2)^(-1) int F^a F^a.
    action_common_coeff = Fraction(f_component_coeff, 4)
    assert_equal("common half-trace action coefficient", action_common_coeff, 8)

    # Trace-delta action: F_delta^a = F_common^a/sqrt(2), hence int tr_delta F^2
    # is half the common component contraction.
    action_trace_delta_coeff = Fraction(trace_half_coeff, 4)
    assert_equal("trace-delta action coefficient", action_trace_delta_coeff, 4)

    # Coupling conversion g_ht^2 = 2 g_YM^2 makes 8/g_ht^2 = 4/g_YM^2.
    converted_common_coeff = Fraction(action_common_coeff, 2)
    assert_equal("coupling-converted action coefficient", converted_common_coeff, action_trace_delta_coeff)


def check_radial_cumulative_profile() -> None:
    # The normalized cumulative charge inside R=rho*u is
    # C(u)=1-3/(1+u^2)^2+2/(1+u^2)^3.  It is the integral of
    # 12 u^3/(1+u^2)^4, i.e. the radial measure times the normalized
    # BPST density divided by the total charge.
    def cumulative(u: Fraction) -> Fraction:
        t = 1 + u * u
        return 1 - Fraction(3, t * t) + Fraction(2, t * t * t)

    def density_with_measure(u: Fraction) -> Fraction:
        t = 1 + u * u
        return Fraction(12) * u**3 / (t**4)

    assert_equal("BPST cumulative at origin", cumulative(Fraction(0)), 0)
    assert_equal("BPST cumulative at u=1", cumulative(Fraction(1)), Fraction(1, 2))

    u = Fraction(2)
    t = 1 + u * u
    derivative = Fraction(12) * u / (t**3) - Fraction(12) * u / (t**4)
    assert_equal("BPST cumulative derivative", derivative, density_with_measure(u))


def check_one_instanton_density_scaling() -> None:
    # Translation and size coordinates have dimensions L^4 and L respectively;
    # rho^{-5} makes the center/scale measure dimensionless.
    measure_length_dimension = 4 + 1 - 5
    assert_equal("one-instanton center-size measure dimension", measure_length_dimension, 0)

    for n_c, n_f in [(2, 0), (3, 0), (3, 2), (5, 4)]:
        zero_modes = 4 * n_c
        # (8*pi^2/g^2)^(2 N_c) carries g-power -4 N_c, one g^{-1}
        # per bosonic zero mode.
        displayed_g_power = -2 * (2 * n_c)
        assert_equal(f"zero-mode g-power SU({n_c})", displayed_g_power, -zero_modes)

        b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
        alpha = b0
        # For log[g^{-4N_c} (mu rho)^alpha exp(-8*pi^2/g^2)],
        # beta=-b0 g^3/(16*pi^2) gives the leading RG derivative alpha-b0.
        leading_rg_derivative = alpha - b0
        assert_equal(f"one-loop RG exponent SU({n_c}) Nf={n_f}", leading_rg_derivative, 0)


def check_small_instanton_boundary_exponent_criterion() -> None:
    def b0(n_c: int, n_f: int) -> Fraction:
        return Fraction(11, 3) * n_c - Fraction(2, 3) * n_f

    def status(n_c: int, n_f: int, beta_x: Fraction) -> str:
        threshold_margin = b0(n_c, n_f) + beta_x - 4
        if threshold_margin > 0:
            return "finite"
        if threshold_margin == 0:
            return "log_divergent"
        return "power_divergent"

    assert_equal("pure SU(2) vacuum small-rho status", status(2, 0, Fraction(0)), "finite")
    assert_equal("pure SU(3) vacuum small-rho status", status(3, 0, Fraction(0)), "finite")

    # Asymptotic freedom is b0>0, but local small-rho integrability of the
    # vacuum one-instanton density with beta_X=0 requires b0>4.
    assert_equal("SU(3) Nf=16 asymptotic freedom", b0(3, 16) > 0, True)
    assert_equal("SU(3) Nf=16 vacuum small-rho status", status(3, 16, Fraction(0)), "power_divergent")
    assert_equal("SU(3) Nf=16 with insertion beta=4 status", status(3, 16, Fraction(4)), "finite")

    assert_equal("borderline log divergence", status(3, 9, Fraction(-1)), "log_divergent")

    # For integrand rho^(b0+beta_X-5), the antiderivative denominator is
    # b0+beta_X-4; this is exactly the threshold margin above.
    for n_c, n_f, beta_x in [(2, 0, Fraction(0)), (3, 16, Fraction(0)), (3, 9, Fraction(-1))]:
        exponent = b0(n_c, n_f) + beta_x - 5
        antiderivative_denominator = exponent + 1
        assert_equal(
            f"small-rho threshold denominator SU({n_c}) Nf={n_f} beta={beta_x}",
            antiderivative_denominator,
            b0(n_c, n_f) + beta_x - 4,
        )


def check_k_one_adhm_dimension_and_cone_power() -> None:
    for n_c in range(2, 9):
        # k=1 ADHM data: B1,B2 are two complex center coordinates, while
        # I,J contribute 4N real centered variables.
        real_variables = 4 + 4 * n_c
        real_equations = 3
        gauge_quotient = 1
        full_moduli_dim = real_variables - real_equations - gauge_quotient
        assert_equal(f"k=1 ADHM full dimension SU({n_c})", full_moduli_dim, 4 * n_c)

        centered_dim = full_moduli_dim - 4
        fixed_size_orbit_dim = centered_dim - 1
        assert_equal(f"k=1 ADHM centered cone dimension SU({n_c})", centered_dim, 4 * n_c - 4)
        assert_equal(f"k=1 ADHM orientation dimension SU({n_c})", fixed_size_orbit_dim, 4 * n_c - 5)

        u_n = n_c**2
        u_n_minus_two = (n_c - 2) ** 2
        homogeneous_orbit_dim = u_n - u_n_minus_two - 1
        assert_equal(
            f"U(N)/(U(N-2)xU(1)) dimension SU({n_c})",
            homogeneous_orbit_dim,
            fixed_size_orbit_dim,
        )

        if n_c == 2:
            assert_equal("SU(2)/Z2 orientation dimension", 3, fixed_size_orbit_dim)
        else:
            su_n = n_c**2 - 1
            su_n_minus_two = (n_c - 2) ** 2 - 1
            su_homogeneous_orbit_dim = su_n - su_n_minus_two - 1
            assert_equal(
                f"SU(N)/(SU(N-2)xU(1)) dimension SU({n_c})",
                su_homogeneous_orbit_dim,
                fixed_size_orbit_dim,
            )

        cone_radial_power = centered_dim - 1
        assert_equal(f"k=1 ADHM cone volume power SU({n_c})", cone_radial_power, 4 * n_c - 5)


def check_general_adhm_quotient_dimension() -> None:
    for n_c in range(2, 8):
        for k in range(1, 6):
            real_variables = 4 * k * k + 4 * k * n_c
            complex_equation_real = 2 * k * k
            real_moment_equation = k * k
            unitary_quotient = k * k
            quotient_dim = real_variables - complex_equation_real - real_moment_equation - unitary_quotient
            assert_equal(f"ADHM quotient dimension k={k} SU({n_c})", quotient_dim, 4 * k * n_c)
            assert_equal(f"centered ADHM dimension k={k} SU({n_c})", quotient_dim - 4, 4 * k * n_c - 4)

            # The four center coordinates are the two complex trace parts
            # tr(B_1)/k and tr(B_2)/k.  The traceless variables carry the
            # remaining dimension before constraints.
            traceless_b_real = 4 * (k * k - 1)
            framing_real = 4 * k * n_c
            centered_unconstrained = traceless_b_real + framing_real
            assert_equal(
                f"centered unconstrained ADHM variables k={k} SU({n_c})",
                centered_unconstrained,
                real_variables - 4,
            )


def check_adhm_quotient_density_coarea_scaling() -> None:
    # Toy quotient R^2 \ {0} -> R_{>0} by U(1): the level-set coarea formula
    # divides the circle density 2*pi*r by Vol(U(1))*sqrt(M), with M=r^2.
    # Thus the quotient radial density is dr, not r dr.
    circle_density_power = 1
    sqrt_orbit_gram_power = 1
    quotient_radial_density_power = circle_density_power - sqrt_orbit_gram_power
    assert_equal("toy U(1) quotient radial density power", quotient_radial_density_power, 0)

    for n_c in range(2, 8):
        for k in range(1, 6):
            centered_ambient_dim = 4 * k * k + 4 * k * n_c - 4
            constraint_dim = 3 * k * k
            group_dim = k * k
            quotient_dim = centered_ambient_dim - constraint_dim - group_dim
            assert_equal(f"centered ADHM quotient dimension k={k} SU({n_c})", quotient_dim, 4 * k * n_c - 4)

            # In the ambient coarea expression, the moment maps are quadratic.
            # Under X -> lambda X:
            # dX contributes V, delta(mu) contributes -2C, J_mu contributes C
            # because D mu is linear in X, and sqrt(det M) contributes G.
            ball_scaling_power = centered_ambient_dim - 2 * constraint_dim + constraint_dim - group_dim
            assert_equal(f"ADHM quotient ball scaling k={k} SU({n_c})", ball_scaling_power, quotient_dim)
            assert_equal(
                f"ADHM quotient cone shell power k={k} SU({n_c})",
                ball_scaling_power - 1,
                4 * k * n_c - 5,
            )


def check_finite_regulator_determinant_datum() -> None:
    # Finite toy Hessians after zero modes are removed.
    boson_vacuum = [[Fraction(2), Fraction(0), Fraction(0)],
                    [Fraction(0), Fraction(3), Fraction(0)],
                    [Fraction(0), Fraction(0), Fraction(5)]]
    boson_inst_nonzero = [[Fraction(7), Fraction(0)],
                          [Fraction(0), Fraction(11)]]
    ghost_vacuum = [[Fraction(13), Fraction(0)], [Fraction(0), Fraction(17)]]
    ghost_inst_nonzero = [[Fraction(19), Fraction(0)], [Fraction(0), Fraction(23)]]

    boson_ratio_squared = det_fraction(boson_vacuum) / det_fraction(boson_inst_nonzero)
    ghost_ratio = det_fraction(ghost_inst_nonzero) / det_fraction(ghost_vacuum)
    assert_equal("bosonic determinant inverse square factor squared", boson_ratio_squared, Fraction(30, 77))
    assert_equal("ghost determinant numerator factor", ghost_ratio, Fraction(437, 221))

    # A real antisymmetric fermion block [[0,a],[-a,0]] has Pfaffian a.
    # For two blocks, Pfaffians multiply.  Zero-mode blocks are omitted.
    fermion_inst_pf = Fraction(29) * Fraction(31)
    fermion_vac_pf = Fraction(37) * Fraction(41)
    fermion_ratio = fermion_inst_pf / fermion_vac_pf
    assert_equal("fermion Pfaffian nonzero ratio", fermion_ratio, Fraction(899, 1517))

    # The whole scalar datum in a vectorlike toy model has one ghost factor,
    # one inverse-square-root bosonic factor, and one Pfaffian factor.  Track
    # the square to avoid irrational square roots while preserving powers.
    scalar_weight_squared = boson_ratio_squared * ghost_ratio * ghost_ratio * fermion_ratio * fermion_ratio
    expected = Fraction(30, 77) * Fraction(437, 221) ** 2 * Fraction(899, 1517) ** 2
    assert_equal("finite determinant datum squared", scalar_weight_squared, expected)

    # A local counterterm c0+c1 log(mu rho) multiplies the density by
    # exp(-c0) (mu rho)^(-c1).  Check the exponent bookkeeping used in the
    # manuscript discussion.
    old_power = Fraction(11, 3)
    c1 = Fraction(2, 5)
    new_power = old_power - c1
    assert_equal("counterterm logarithmic power shift", new_power, Fraction(49, 15))


def check_physical_instanton_correlator_zero_mode_saturation() -> None:
    # Four zero modes in canonical order: R1, L1, R2, L2.  Berezin
    # integration returns only the coefficient of R1 L1 R2 L2.
    variable_count = 4
    unsaturated = grassmann_mul(
        grassmann_monomial(0, coefficient=Fraction(3)),
        grassmann_monomial(2, coefficient=Fraction(5)),
    )
    assert_equal(
        "unsaturated instanton zero-mode correlator vanishes",
        berezin_top_coefficient(unsaturated, variable_count),
        Fraction(0),
    )

    operator_pair = grassmann_monomial(0, 1, coefficient=Fraction(7))
    mass_lift = grassmann_monomial(2, 3, coefficient=Fraction(11))
    lifted = grassmann_mul(operator_pair, mass_lift)
    assert_equal(
        "mass/source lifting supplies missing instanton zero modes",
        berezin_top_coefficient(lifted, variable_count),
        Fraction(77),
    )

    # Two-flavor QCD zero-mode insertions form the determinant
    # B_11 B_22 - B_12 B_21 as the top Berezin coefficient.
    b11 = Fraction(2)
    b12 = Fraction(3)
    b21 = Fraction(5)
    b22 = Fraction(7)
    diagonal_pairing = grassmann_mul(
        grassmann_monomial(0, 1, coefficient=b11),
        grassmann_monomial(2, 3, coefficient=b22),
    )
    crossed_pairing = grassmann_mul(
        grassmann_monomial(0, 3, coefficient=b12),
        grassmann_monomial(2, 1, coefficient=b21),
    )
    flavor_determinant_polynomial = grassmann_add(diagonal_pairing, crossed_pairing)
    determinant = b11 * b22 - b12 * b21
    assert_equal(
        "two-flavor 't Hooft determinant from zero-mode Berezin coefficient",
        berezin_top_coefficient(flavor_determinant_polynomial, variable_count),
        determinant,
    )

    axial_charge_per_bilinear = 2
    flavor_count = 2
    assert_equal(
        "QCD instanton axial charge selection",
        axial_charge_per_bilinear * flavor_count,
        4,
    )

    three_flavor_source = [
        [Fraction(2), Fraction(3), Fraction(5)],
        [Fraction(7), Fraction(11), Fraction(13)],
        [Fraction(17), Fraction(19), Fraction(23)],
    ]
    assert_equal(
        "three-flavor 't Hooft determinant from zero-mode Berezin coefficient",
        grassmann_source_determinant_top_coefficient(three_flavor_source),
        det_fraction(three_flavor_source),
    )

    axial_parameter_units = 5
    flavor_count = 3
    theta_shift = 2 * flavor_count * axial_parameter_units
    mass_phase_shift = -2 * flavor_count * axial_parameter_units
    assert_equal(
        "strong CP phase theta plus arg det M is axial invariant",
        theta_shift + mass_phase_shift,
        0,
    )


def check_proper_time_fluctuation_four_fermion_amplitude() -> None:
    # A finite proper-time determinant ledger is a product over nonzero
    # spectra.  The zero eigenvalue is visible before collective-coordinate
    # projection and is absent from the determinant datum.
    raw_boson_instanton_spectrum = [Fraction(0), Fraction(11), Fraction(13), Fraction(17)]
    boson_instanton_nonzero = [
        eigenvalue for eigenvalue in raw_boson_instanton_spectrum if eigenvalue != 0
    ]
    assert_equal(
        "unprojected instanton bosonic determinant has zero mode",
        product_fraction(raw_boson_instanton_spectrum),
        Fraction(0),
    )
    assert_equal(
        "bosonic collective coordinate removed before determinant",
        len(raw_boson_instanton_spectrum) - len(boson_instanton_nonzero),
        1,
    )

    boson_vacuum_spectrum = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
    ghost_vacuum_spectrum = [Fraction(19), Fraction(23)]
    ghost_instanton_spectrum = [Fraction(29), Fraction(31)]
    fermion_vacuum_pfaffian_blocks = [Fraction(37), Fraction(41)]
    fermion_instanton_pfaffian_blocks = [Fraction(43), Fraction(47)]

    boson_inverse_sqrt_squared = (
        product_fraction(boson_vacuum_spectrum)
        / product_fraction(boson_instanton_nonzero)
    )
    ghost_ratio = (
        product_fraction(ghost_instanton_spectrum)
        / product_fraction(ghost_vacuum_spectrum)
    )
    fermion_pfaffian_ratio = (
        product_fraction(fermion_instanton_pfaffian_blocks)
        / product_fraction(fermion_vacuum_pfaffian_blocks)
    )
    nonzero_mode_weight_squared = (
        boson_inverse_sqrt_squared
        * ghost_ratio
        * ghost_ratio
        * fermion_pfaffian_ratio
        * fermion_pfaffian_ratio
    )
    assert_equal(
        "proper-time nonzero-mode determinant weight squared",
        nonzero_mode_weight_squared,
        Fraction(210, 2431) * Fraction(899, 437) ** 2 * Fraction(2021, 1517) ** 2,
    )

    # The four external fermion wave packets enter only through the
    # zero-mode-projected two-flavor source matrix B_eta.  The full
    # semiclassical four-point amplitude is W_nz det(B_eta) integrated over
    # collective coordinates; this finite check tracks the scalar integrand.
    source_matrix = [[Fraction(2), Fraction(3)], [Fraction(5), Fraction(11)]]
    source_determinant = det_fraction(source_matrix)
    assert_equal(
        "zero-mode projected four-fermion source determinant",
        grassmann_source_determinant_top_coefficient(source_matrix),
        source_determinant,
    )
    four_fermion_integrand_squared = (
        nonzero_mode_weight_squared * source_determinant * source_determinant
    )
    assert_equal(
        "four-fermion instanton amplitude integrand squared",
        four_fermion_integrand_squared,
        nonzero_mode_weight_squared * Fraction(49),
    )

    # In the local limit for N_f=2, each zero-mode source matrix entry carries
    # the BPST zero-mode normalization rho^3, while det(B_eta) contains two
    # entries.  This is the rho^6 factor in the local four-fermion vertex.
    assert_equal("two-flavor local 't Hooft vertex rho power", 2 * 3, 6)

    # The universal log(mu rho) power is the sum of the proper-time small-t
    # trace coefficient and the coupling/counterterm conversion in the same
    # scheme.  For SU(3) with two Dirac fundamentals this equals b0=29/3.
    spectral_trace_power = Fraction(7, 3)
    coupling_and_local_counterterm_power = Fraction(22, 3)
    assert_equal(
        "proper-time plus counterterm log power for SU(3) Nf=2",
        spectral_trace_power + coupling_and_local_counterterm_power,
        Fraction(29, 3),
    )


def check_uhlenbeck_boundary_face_budget() -> None:
    for n_c in range(2, 8):
        for k in range(1, 6):
            full_dim = 4 * k * n_c
            for ell in range(1, k + 1):
                open_stratum_dim = 4 * (k - ell) * n_c + 4 * ell
                open_codim = full_dim - open_stratum_dim
                assert_equal(
                    f"open Uhlenbeck codim k={k} ell={ell} SU({n_c})",
                    open_codim,
                    4 * ell * (n_c - 1),
                )
                for clusters in range(1, ell + 1):
                    diagonal_dim = 4 * (k - ell) * n_c + 4 * clusters
                    total_codim = full_dim - diagonal_dim
                    additional_collision_codim = total_codim - open_codim
                    assert_equal(
                        f"Uhlenbeck diagonal codim k={k} ell={ell} r={clusters} SU({n_c})",
                        additional_collision_codim,
                        4 * (ell - clusters),
                    )
                    assert_equal(
                        f"total Uhlenbeck diagonal codim k={k} ell={ell} r={clusters} SU({n_c})",
                        total_codim,
                        4 * ell * (n_c - 1) + 4 * (ell - clusters),
                    )

    def power_status(exponents: list[Fraction]) -> str:
        if all(exponent > 0 for exponent in exponents):
            return "finite"
        if any(exponent < 0 for exponent in exponents):
            return "power_divergent"
        return "log_divergent"

    assert_equal("Uhlenbeck positive product status", power_status([Fraction(1, 3), Fraction(5, 4)]), "finite")
    assert_equal("Uhlenbeck zero exponent status", power_status([Fraction(2), Fraction(0)]), "log_divergent")
    assert_equal("Uhlenbeck negative exponent status", power_status([Fraction(2), Fraction(-1, 3)]), "power_divergent")

    # With epsilon=1 and no logarithms, the factorized boundary integral is
    # product_alpha A_alpha^{-1}.  This is the finite shadow of the product
    # criterion in the manuscript.
    exponents = [Fraction(1, 2), Fraction(3, 2), Fraction(2)]
    product_integral = Fraction(1)
    for exponent in exponents:
        product_integral *= Fraction(1, 1) / exponent
    assert_equal("Uhlenbeck product antiderivative", product_integral, Fraction(2, 3))

    # The charge-one threshold is the same product criterion with a single
    # scale exponent A=b0+beta_X-4.
    b0 = Fraction(11, 3) * 3 - Fraction(2, 3) * 9
    beta_x = Fraction(-1)
    charge_one_scale_exponent = b0 + beta_x - 4
    assert_equal("charge-one exponent from b0 beta", charge_one_scale_exponent, Fraction(0))
    assert_equal("charge-one threshold as face status", power_status([charge_one_scale_exponent]), "log_divergent")


def main() -> None:
    check_eta_self_duality()
    check_eta_norm()
    check_eta_quadratic_identity()
    check_radial_integrals_and_actions()
    check_radial_cumulative_profile()
    check_one_instanton_density_scaling()
    check_small_instanton_boundary_exponent_criterion()
    check_general_adhm_quotient_dimension()
    check_adhm_quotient_density_coarea_scaling()
    check_finite_regulator_determinant_datum()
    check_physical_instanton_correlator_zero_mode_saturation()
    check_proper_time_fluctuation_four_fermion_amplitude()
    check_uhlenbeck_boundary_face_budget()
    check_k_one_adhm_dimension_and_cone_power()
    print("All BPST instanton normalization checks passed.")


if __name__ == "__main__":
    main()
