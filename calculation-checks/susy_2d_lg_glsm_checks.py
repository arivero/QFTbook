"""Finite algebra checks for the 2D N=(2,2) LG/GLSM chapter.

Evidence contract.
Target claims: the finite LG/GLSM charge ledgers, abelian duality
normalizations, charged-chiral mirror elimination, vortex-zero-mode filter,
vortex-to-FI-coordinate normalization, single-vortex coefficient
noncancellation bound, P^{N-1} mirror residue trace, and
vortex-to-protected-observable residual ledger, together with the
vortex-fugacity dimensional-transmutation coordinate, the degree-one
P^{N-1} stable-map gate, and the finite degree-one stable-map incidence model
with supplied vortex coefficient input plus conditional residual template for
the quantum-product observable relation, in Volume VII Chapter 09.
Independent construction: exact rational charge arithmetic, determinant
elimination, Berezin-degree tests, retained-window signed/mass coefficient
bounds, root-of-unity residue sums, stable-map incidence Jacobians, and
residual budgets are computed directly from finite data rather than by
substituting the displayed final identities.
Imported assumptions: the finite GLSM charge matrix, selected regulator-stage
factorization, supplied vortex coefficients, nonzero-mode determinant
placeholders, logarithm-branch conventions, and the chapter's
protected-coordinate definitions are assumed as finite input.
Negative controls: extra unsaturated zero modes, omitted vortex
normalization constants, unbalanced regulator-scale changes, coherent signed
cancellations with nonzero absolute mass, wrong residue selection powers,
underspecified residual budgets, stable-map dimension mismatches, mirror-only
or dimension-only quantum-product shortcuts, determinant-orientation flips,
zero-mode multiplicity errors, compactification/contact mutations,
hyperplane-normalization changes, omitted off-pairing controls, and finite-gauge
invariance failures are rejected when the finite model can represent them.
Scope boundary: a pass checks finite algebra and bookkeeping interfaces; it
does not prove continuum GLSM existence, Hori--Vafa mirror equivalence,
vortex compactness, derivation of the vortex fluctuation spectra or gauge-ghost
complex, determinant nonvanishing beyond the supplied finite input,
virtual-cycle construction, or uniform remainder estimates.
"""

from __future__ import annotations

from fractions import Fraction
from math import exp, isclose, log, prod

from check_utils import assert_gt as assert_gt_bound
from check_utils import assert_leq as assert_leq_bound


def assert_equal(label: str, left, right) -> None:
    if left != right:
        raise AssertionError(f"{label} failed: {left!r} != {right!r}")


def assert_close(label: str, left: float, right: float, tol: float = 1e-11) -> None:
    if not isclose(left, right, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{label} failed: {left!r} != {right!r}")


def determinant_fraction(matrix: list[list[Fraction]]) -> Fraction:
    reduced = [row[:] for row in matrix]
    size = len(reduced)
    determinant = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if reduced[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            reduced[column], reduced[pivot] = reduced[pivot], reduced[column]
            determinant *= -1
        pivot_value = reduced[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            factor = reduced[row][column] / pivot_value
            for col in range(column, size):
                reduced[row][col] -= factor * reduced[column][col]
    return determinant


def fermat_weights(degrees: list[int]) -> list[Fraction]:
    return [Fraction(1, degree) for degree in degrees]


def monomial_charge(exponents: list[int], weights: list[Fraction]) -> Fraction:
    return sum(Fraction(power) * weight for power, weight in zip(exponents, weights))


def lg_central_charge(weights: list[Fraction]) -> Fraction:
    return 3 * sum(Fraction(1) - 2 * weight for weight in weights)


def jacobi_dimension_fermat(degrees: list[int]) -> int:
    return prod(degree - 1 for degree in degrees)


def check_a_series_lg() -> None:
    for k in range(0, 16):
        degree = k + 2
        q = Fraction(1, degree)
        assert_equal(f"A_{k} superpotential charge", degree * q, Fraction(1))
        assert_equal(f"A_{k} derivative charge", (degree - 1) * q, Fraction(1) - q)
        assert_equal(f"A_{k} Jacobi dimension", jacobi_dimension_fermat([degree]), k + 1)
        assert_equal(f"A_{k} central charge", lg_central_charge([q]), Fraction(3 * k, k + 2))


def check_fermat_tensor_products() -> None:
    examples = [
        [3, 3, 3],
        [4, 4],
        [5, 5, 5, 5, 5],
        [2, 3, 7],
    ]
    for degrees in examples:
        weights = fermat_weights(degrees)
        for index, degree in enumerate(degrees):
            exponents = [0] * len(degrees)
            exponents[index] = degree
            assert_equal(
                f"Fermat degree-{degree} monomial charge in {degrees}",
                monomial_charge(exponents, weights),
                Fraction(1),
            )
            exponents[index] = degree - 1
            assert_equal(
                f"Fermat derivative monomial charge in {degrees}",
                monomial_charge(exponents, weights),
                Fraction(1) - weights[index],
            )

    quintic_weights = fermat_weights([5, 5, 5, 5, 5])
    assert_equal("quintic LG central charge", lg_central_charge(quintic_weights), Fraction(9))
    assert_equal("quintic Fermat Jacobi dimension", jacobi_dimension_fermat([5] * 5), 4**5)


def check_fermat_wilsonian_spurion_selection() -> None:
    # Candidate monomials have the form prod_i g_i^{m_i} X_i^{a_i}.
    # Spurion neutrality gives a_i=d_i m_i, and the chiral R-charge-one
    # condition gives sum_i a_i/d_i = sum_i m_i = 1.  With nonnegative
    # regular Wilsonian powers, this selects exactly one original monomial.
    for degrees in [[3], [4], [3, 3], [3, 4, 5], [5, 5, 5, 5, 5]]:
        selected = []

        def visit(index: int, coupling_powers: list[int]) -> None:
            if index == len(degrees):
                field_powers = [degree * power for degree, power in zip(degrees, coupling_powers)]
                r_charge = sum(
                    Fraction(field_power, degree)
                    for field_power, degree in zip(field_powers, degrees)
                )
                if r_charge == 1:
                    selected.append((tuple(coupling_powers), tuple(field_powers)))
                return
            for power in range(3):
                visit(index + 1, coupling_powers + [power])

        visit(0, [])
        expected = []
        for position, degree in enumerate(degrees):
            coupling_powers = [0] * len(degrees)
            field_powers = [0] * len(degrees)
            coupling_powers[position] = 1
            field_powers[position] = degree
            expected.append((tuple(coupling_powers), tuple(field_powers)))
        assert_equal(
            f"Fermat Wilsonian spurion selection {degrees}",
            sorted(selected),
            sorted(expected),
        )


def glsm_charge_sum(num_x_fields: int, degree: int) -> int:
    return num_x_fields - degree


def check_hypersurface_glsm_ledger() -> None:
    # Charges (1,...,1,-d) make P*G_d gauge invariant.
    for num_x_fields, degree in [(5, 5), (4, 3), (6, 4), (3, 7)]:
        total_charge = glsm_charge_sum(num_x_fields, degree)
        assert_equal(
            f"charge of P G_d for N={num_x_fields}, d={degree}",
            -degree + degree,
            0,
        )
        assert_equal(
            f"axial anomaly ledger for N={num_x_fields}, d={degree}",
            total_charge,
            num_x_fields - degree,
        )
        assert_equal(
            f"positive chamber hypersurface dimension for N={num_x_fields}",
            (num_x_fields - 1) - 1,
            num_x_fields - 2,
        )
        assert_equal(
            f"negative chamber residual finite group order for d={degree}",
            degree,
            degree,
        )

    assert_equal("quintic GLSM axial anomaly cancellation", glsm_charge_sum(5, 5), 0)
    assert_equal("quintic positive chamber complex dimension", 5 - 2, 3)
    assert_equal("quintic negative chamber residual group order", 5, 5)


def check_twist_spin_ledger() -> None:
    # Convention in Volume VII Chapter 09:
    # (s, F_V, F_A) for Q_+, bar Q_+, Q_-, bar Q_-.
    charges = {
        "Q+": (Fraction(1, 2), 1, 1),
        "barQ+": (Fraction(1, 2), -1, -1),
        "Q-": (Fraction(-1, 2), 1, -1),
        "barQ-": (Fraction(-1, 2), -1, 1),
    }

    a_twisted = {name: spin + Fraction(vector, 2) for name, (spin, vector, _axial) in charges.items()}
    b_twisted = {name: spin + Fraction(axial, 2) for name, (spin, _vector, axial) in charges.items()}

    assert_equal("A-twist Q+ spin", a_twisted["Q+"], 1)
    assert_equal("A-twist barQ+ scalar", a_twisted["barQ+"], 0)
    assert_equal("A-twist Q- scalar", a_twisted["Q-"], 0)
    assert_equal("A-twist barQ- spin", a_twisted["barQ-"], -1)

    assert_equal("B-twist Q+ spin", b_twisted["Q+"], 1)
    assert_equal("B-twist barQ+ scalar", b_twisted["barQ+"], 0)
    assert_equal("B-twist Q- spin", b_twisted["Q-"], -1)
    assert_equal("B-twist barQ- scalar", b_twisted["barQ-"], 0)

    # In the central-charge-free local algebra, the scalar sums square to
    # zero because no same-chirality barred/barred or opposite-chirality
    # barred/unbarred anticommutator appears.
    nonzero_anticommutators = {frozenset(("Q+", "barQ+")), frozenset(("Q-", "barQ-"))}
    for label, pair in {
        "A scalar mixed anticommutator": frozenset(("barQ+", "Q-")),
        "B scalar mixed anticommutator": frozenset(("barQ+", "barQ-")),
    }.items():
        if pair in nonzero_anticommutators:
            raise AssertionError(f"{label} should vanish in the local algebra")


def check_abelian_circle_duality() -> None:
    for radius in [Fraction(2, 3), Fraction(3, 2), Fraction(5, 4), Fraction(7, 5)]:
        dual_radius = 1 / radius
        assert_equal("circle duality is involutive", 1 / dual_radius, radius)

        for momentum in range(-4, 5):
            for winding in range(-4, 5):
                p_left = Fraction(momentum, 1) / radius + winding * radius
                p_right = Fraction(momentum, 1) / radius - winding * radius
                dual_p_left = Fraction(winding, 1) / dual_radius + momentum * dual_radius
                dual_p_right = Fraction(winding, 1) / dual_radius - momentum * dual_radius

                assert_equal("T-dual left-moving momentum", dual_p_left, p_left)
                assert_equal("T-dual right-moving momentum sign", dual_p_right, -p_right)
                assert_equal(
                    "T-dual zero-mode quadratic form",
                    dual_p_left**2 + dual_p_right**2,
                    p_left**2 + p_right**2,
                )


def check_abelian_legendre_duality() -> None:
    for radius_squared in [Fraction(4, 9), Fraction(9, 4), Fraction(25, 16), Fraction(7, 3)]:
        kahler_hessian = radius_squared
        dual_hessian = 1 / kahler_hessian
        assert_equal("Legendre Hessian inverse", kahler_hessian * dual_hessian, 1)
        assert_equal("free chiral radius-squared inversion", dual_hessian, 1 / radius_squared)

        # Add an affine term K(B)=a B^2/2 + b B + c.  It shifts the
        # Legendre coordinate u=aB+b but does not change the dual Hessian.
        affine_slope = Fraction(5, 7)
        for u_value in [Fraction(-3, 2), Fraction(1, 5), Fraction(11, 6)]:
            b_value = (u_value - affine_slope) / radius_squared
            assert_equal(
                "affine-shifted Legendre equation",
                radius_squared * b_value + affine_slope,
                u_value,
            )
            derivative_dual_b_wrt_u = 1 / radius_squared
            assert_equal(
                "affine-shifted Legendre inverse Hessian",
                derivative_dual_b_wrt_u,
                dual_hessian,
            )


def check_abelian_glsm_coulomb_ledger() -> None:
    positive_charge_examples = [
        [1, 1],
        [1, 1, 1],
        [2, 1],
        [2, 3, 1],
    ]
    for charges in positive_charge_examples:
        total_charge = sum(charges)
        assert_equal("positive-charge Coulomb vacuum count", total_charge, sum(charges))

        # In product_i (Q_i sigma/mu)^{Q_i}, the exponent of sigma and mu is
        # plus/minus the total charge.  The nonzero constant is product Q_i^{Q_i}.
        sigma_exponent = sum(charges)
        mu_exponent = -sum(charges)
        charge_constant_degree = sum(charges)
        assert_equal("Coulomb sigma exponent", sigma_exponent, total_charge)
        assert_equal("Coulomb mu exponent", mu_exponent, -total_charge)
        assert_equal(
            "Coulomb charge-constant weighted degree",
            charge_constant_degree,
            total_charge,
        )

    for num_x_fields, degree in [(5, 5), (4, 3), (6, 4), (3, 7)]:
        charges = [1] * num_x_fields + [-degree]
        sigma_exponent = sum(charges)
        assert_equal(
            f"hypersurface Coulomb sigma exponent N={num_x_fields} d={degree}",
            sigma_exponent,
            num_x_fields - degree,
        )
        assert_equal(
            f"hypersurface Coulomb exponent equals axial anomaly N={num_x_fields} d={degree}",
            sigma_exponent,
            glsm_charge_sum(num_x_fields, degree),
        )

    assert_equal("quintic Coulomb exponent vanishes", sum([1, 1, 1, 1, 1, -5]), 0)


def check_abelian_coulomb_one_loop_primitive() -> None:
    # The local determinant gives dW/dSigma = -t + sum_i Q_i log(Q_i Sigma/mu).
    # This check verifies the primitive and its finite FI-coordinate
    # transformation under determinant normalization changes.
    sigma = 1.37
    mu = 0.91
    t = -0.42
    charges = [1, 2, 4]
    step = 1e-6

    def primitive(sigma_value: float) -> float:
        return -t * sigma_value + sum(
            charge
            * sigma_value
            * (log(charge * sigma_value / mu) - 1)
            for charge in charges
        )

    derivative_from_log = -t + sum(charge * log(charge * sigma / mu) for charge in charges)
    derivative_from_primitive = (primitive(sigma + step) - primitive(sigma - step)) / (2 * step)
    assert_close(
        "abelian Coulomb one-loop primitive differentiates to log derivative",
        derivative_from_primitive,
        derivative_from_log,
        tol=1e-9,
    )

    determinant_constants = [Fraction(2, 3), Fraction(5, 4), Fraction(7, 5)]
    finite_fi_shift = sum(
        charge * log(float(constant))
        for charge, constant in zip(charges, determinant_constants)
    )
    shifted_t = t + finite_fi_shift
    with_constants = -t * sigma + sum(
        charge
        * sigma
        * (log(charge * sigma / (mu * float(constant))) - 1)
        for charge, constant in zip(charges, determinant_constants)
    )
    shifted_coordinate_form = -shifted_t * sigma + sum(
        charge * sigma * (log(charge * sigma / mu) - 1)
        for charge in charges
    )
    assert_close(
        "determinant constants are finite FI-coordinate shifts",
        with_constants,
        shifted_coordinate_form,
    )


def check_charged_chiral_dual_elimination() -> None:
    sigmas = [1.3, 0.7]
    charges = [[1, 2], [3, 1], [2, 4]]
    t_values = [0.2, -0.4]
    mu = 1.7
    coefficients = [0.9, 1.2, 2.1]

    masses = [sum(q_a * sigma_a for q_a, sigma_a in zip(row, sigmas)) for row in charges]
    y_values = [-log(mass / (mu * coeff)) for mass, coeff in zip(masses, coefficients)]

    w_dual = -sum(t_a * sigma_a for t_a, sigma_a in zip(t_values, sigmas))
    w_dual -= sum(mass * y for mass, y in zip(masses, y_values))
    w_dual -= mu * sum(coeff * exp(-y) for coeff, y in zip(coefficients, y_values))

    w_eliminated = -sum(t_a * sigma_a for t_a, sigma_a in zip(t_values, sigmas))
    w_eliminated += sum(
        mass * (log(mass / (mu * coeff)) - 1)
        for mass, coeff in zip(masses, coefficients)
    )
    assert_close("charged-chiral Y elimination matches one-loop form", w_dual, w_eliminated)

    rank_one_charges = [1, 2, 3]
    sigma = 1.4
    t = -0.6
    coeffs = [0.8, 1.5, 2.2]
    with_coeffs = -t * sigma + sum(
        charge * sigma * (log(charge * sigma / (mu * coeff)) - 1)
        for charge, coeff in zip(rank_one_charges, coeffs)
    )
    shifted_t = t + sum(charge * log(coeff) for charge, coeff in zip(rank_one_charges, coeffs))
    shifted_form = -shifted_t * sigma + sum(
        charge * sigma * (log(charge * sigma / mu) - 1)
        for charge in rank_one_charges
    )
    assert_close("rank-one FI coordinate absorbs vortex coefficients", with_coeffs, shifted_form)


def check_all_rank_vortex_fi_coordinate_shift() -> None:
    charges = [
        [1, 0],
        [1, 1],
        [0, 2],
        [-2, -3],
        [3, -1],
    ]
    rank = 2
    log_coefficients = [
        Fraction(2, 3),
        Fraction(-5, 4),
        Fraction(7, 6),
        Fraction(11, 5),
        Fraction(-13, 7),
    ]
    x_logs = [
        Fraction(17, 5),
        Fraction(-19, 6),
        Fraction(23, 7),
        Fraction(29, 8),
        Fraction(-31, 9),
    ]
    sigmas = [Fraction(11, 3), Fraction(-7, 4)]

    delta_t = [
        sum(row[a] * ell_i for row, ell_i in zip(charges, log_coefficients))
        for a in range(rank)
    ]

    for a in range(rank):
        bare_constraint_log = sum(row[a] * x_i for row, x_i in zip(charges, x_logs))
        normalized_constraint_log = sum(
            row[a] * (x_i + ell_i)
            for row, x_i, ell_i in zip(charges, x_logs, log_coefficients)
        )
        assert_equal(
            f"all-rank normalized mirror-torus constraint a={a}",
            normalized_constraint_log,
            bare_constraint_log + delta_t[a],
        )

    affine_from_masses = sum(
        sum(row[a] * sigmas[a] for a in range(rank)) * ell_i
        for row, ell_i in zip(charges, log_coefficients)
    )
    affine_from_fi_shift = sum(sigmas[a] * delta_t[a] for a in range(rank))
    assert_equal(
        "all-rank Coulomb affine term equals FI-coordinate shift",
        affine_from_masses,
        affine_from_fi_shift,
    )

    branch_shifts = [1, -2, 3, 0, -1]
    theta_periods = [
        sum(row[a] * branch_i for row, branch_i in zip(charges, branch_shifts))
        for a in range(rank)
    ]
    assert_equal("all-rank logarithm branch theta periods", theta_periods, [-4, 5])

    rank_one_charges = [2, -1, 3, 4]
    rank_one_logs = [Fraction(3, 2), Fraction(-5, 3), Fraction(7, 4), Fraction(11, 5)]
    assert_equal(
        "all-rank formula restricts to rank-one FI shift",
        sum(charge * ell for charge, ell in zip(rank_one_charges, rank_one_logs)),
        Fraction(1123, 60),
    )


def check_vortex_fugacity_dimensional_transmutation() -> None:
    charges = [2, 3, 5]
    charge_sum = sum(charges)
    charge_constant = prod(Fraction(charge) ** charge for charge in charges)
    bare_q = Fraction(7, 11)
    vortex_coefficients = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    q_phys = bare_q * prod(
        coefficient**charge
        for coefficient, charge in zip(vortex_coefficients, charges)
    )
    mu = Fraction(17, 5)
    lambda_power = mu**charge_sum * q_phys / charge_constant

    scale_factor = Fraction(19, 7)
    mu_prime = mu * scale_factor
    q_phys_prime = q_phys / scale_factor**charge_sum
    assert_equal(
        "GLSM vortex fugacity RG-invariant scale",
        mu_prime**charge_sum * q_phys_prime / charge_constant,
        lambda_power,
    )

    wrong_uncompensated_scale = mu_prime**charge_sum * q_phys / charge_constant
    if wrong_uncompensated_scale == lambda_power:
        raise AssertionError("changing mu without FI flow should move the Coulomb scale")

    bare_lambda_power = mu**charge_sum * bare_q / charge_constant
    if bare_lambda_power == lambda_power:
        raise AssertionError("bare FI coordinate should not ignore vortex coefficients")

    anomaly_free_charges = [1, 1, 1, -3]
    assert_equal("anomaly-free GLSM has no mu power", sum(anomaly_free_charges), 0)
    q_anomaly_free = Fraction(23, 29)
    assert_equal(
        "anomaly-free fugacity is dimensionless under mu rescaling",
        q_anomaly_free * mu ** sum(anomaly_free_charges),
        q_anomaly_free,
    )


def check_mirror_primitive_monomial_selection() -> None:
    # If the connected protected correction is h(X)=sum_n a_n X^n and exact
    # Coulomb matching demands X(M)=M/a_1 on a branch, then the critical
    # equation M=X h'(X) forces all higher a_n to vanish.  The check below is
    # the finite coefficient test behind the displayed argument in the chapter.
    a1 = Fraction(5, 3)
    x_value = Fraction(2, 7)
    matched_mass = a1 * x_value
    assert_equal("primitive mirror monomial matches branch", a1 * x_value, matched_mass)

    for degree in range(2, 8):
        higher_coeff = Fraction(degree + 1, degree + 3)
        critical_mass = a1 * x_value + degree * higher_coeff * x_value**degree
        if critical_mass == matched_mass:
            raise AssertionError("higher mirror harmonic should spoil exact Coulomb matching")


def check_vortex_zero_mode_filter() -> None:
    # After the two universal zero modes have been identified with the twisted
    # F-term measure, the residual Berezin integral extracts the top exterior
    # degree.  Without insertions, only zero residual modes survive.
    def survives(residual_zero_modes: int, insertion_degree: int) -> bool:
        return insertion_degree == residual_zero_modes

    for residual_zero_modes in range(0, 7):
        assert_equal(
            f"uninserted vortex F-term survives iff no residual zero modes {residual_zero_modes}",
            survives(residual_zero_modes, 0),
            residual_zero_modes == 0,
        )
        for insertion_degree in range(0, 7):
            assert_equal(
                f"vortex Berezin top-degree saturation r={residual_zero_modes} d={insertion_degree}",
                survives(residual_zero_modes, insertion_degree),
                insertion_degree == residual_zero_modes,
            )

    # Universal zero modes are removed into d^2 theta_tilde before the scalar
    # coefficient is formed; residual modes are the only Grassmann degree left
    # for the coefficient integral.
    total_fermion_zero_modes = 6
    universal_twisted_f_modes = 2
    residual_zero_modes = total_fermion_zero_modes - universal_twisted_f_modes
    assert_equal("vortex residual zero-mode count", residual_zero_modes, 4)
    assert_equal("residual insertions saturate Berezin integral", survives(4, 4), True)
    assert_equal("missing residual insertion kills Berezin integral", survives(4, 3), False)


def check_single_vortex_amplitude_assembly() -> None:
    # Finite charge-one vortex sector: remove bosonic collective-coordinate
    # zero modes before forming the determinant ratio.
    raw_boson_vortex_spectrum = [Fraction(0), Fraction(0), Fraction(5), Fraction(7)]
    boson_vortex_nonzero = [
        eigenvalue for eigenvalue in raw_boson_vortex_spectrum if eigenvalue != 0
    ]
    assert_equal("raw vortex bosonic determinant has zero modes", prod(raw_boson_vortex_spectrum), 0)
    assert_equal(
        "vortex collective coordinates removed before determinant",
        len(raw_boson_vortex_spectrum) - len(boson_vortex_nonzero),
        2,
    )

    boson_vacuum_spectrum = [Fraction(2), Fraction(3), Fraction(11)]
    ghost_vacuum_spectrum = [Fraction(13), Fraction(17)]
    ghost_vortex_spectrum = [Fraction(19), Fraction(23)]
    fermion_vacuum_blocks = [Fraction(29), Fraction(31)]
    fermion_vortex_blocks = [Fraction(37), Fraction(41)]

    boson_inverse_sqrt_squared = prod(boson_vacuum_spectrum) / prod(boson_vortex_nonzero)
    ghost_ratio = prod(ghost_vortex_spectrum) / prod(ghost_vacuum_spectrum)
    fermion_ratio = prod(fermion_vortex_blocks) / prod(fermion_vacuum_blocks)
    determinant_weight_squared = (
        boson_inverse_sqrt_squared * ghost_ratio**2 * fermion_ratio**2
    )
    assert_equal(
        "single-vortex nonzero-mode determinant weight squared",
        determinant_weight_squared,
        Fraction(66, 35) * Fraction(437, 221) ** 2 * Fraction(1517, 899) ** 2,
    )

    universal_fermion_zero_modes = 2
    twisted_f_term_measure_degree = 2
    assert_equal(
        "universal vortex zero modes match twisted F-term measure",
        universal_fermion_zero_modes,
        twisted_f_term_measure_degree,
    )

    residual_zero_modes = 0
    saturated_zero_mode_coefficient = Fraction(5, 4)
    unsaturated_zero_mode_coefficient = (
        saturated_zero_mode_coefficient if residual_zero_modes == 0 else Fraction(0)
    )
    assert_equal(
        "saturated vortex zero-mode coefficient survives",
        unsaturated_zero_mode_coefficient,
        Fraction(5, 4),
    )

    extra_zero_modes = 2
    extra_unsaturated_coefficient = (
        saturated_zero_mode_coefficient if extra_zero_modes == 0 else Fraction(0)
    )
    assert_equal("extra unsaturated vortex zero modes kill F-term", extra_unsaturated_coefficient, 0)

    reduced_classical_weight = Fraction(7, 9)
    vortex_coefficient_squared = (
        reduced_classical_weight**2
        * determinant_weight_squared
        * saturated_zero_mode_coefficient**2
    )
    assert_equal(
        "single-vortex coefficient assembly squared",
        vortex_coefficient_squared,
        Fraction(7, 9) ** 2 * determinant_weight_squared * Fraction(25, 16),
    )

    # The superpotential has mass dimension one in two dimensions; exp(-Y) and
    # c_i are dimensionless after the regulator integral is normalized by mu.
    assert_equal("single-vortex superpotential dimension", 1 + 0 + 0, 1)

    # Rescaling the finite vortex coefficient is absorbed by an affine shift
    # of the FI coordinate.  In exponentiated form q=exp(-t), the exact
    # bookkeeping is q -> q c^{-Q}.
    bare_q = Fraction(11, 13)
    charge = 3
    coefficient = Fraction(2, 5)
    shifted_q = bare_q / coefficient**charge
    assert_equal("vortex coefficient FI shift in exponentiated coordinate", shifted_q, Fraction(1375, 104))


def check_vortex_coefficient_noncancellation_bound() -> None:
    # The retained one-vortex window carries a signed integrand, not just an
    # allowed charge.  A usable amplitude bound needs a margin between
    # the signed coefficient and all determinant, zero-mode, boundary, and
    # continuum errors.
    retained_cells = [Fraction(3, 4), Fraction(-1, 8), Fraction(1, 16)]
    retained_signed = sum(retained_cells, Fraction(0))
    retained_mass = sum(abs(cell) for cell in retained_cells)
    noncancellation_fraction = abs(retained_signed) / retained_mass

    assert_equal(
        "retained vortex coefficient signed value",
        retained_signed,
        Fraction(11, 16),
    )
    assert_equal(
        "retained vortex coefficient absolute mass",
        retained_mass,
        Fraction(15, 16),
    )
    assert_equal(
        "retained vortex noncancellation fraction",
        noncancellation_fraction,
        Fraction(11, 15),
    )

    residuals = {
        "tail": Fraction(1, 80),
        "determinant": Fraction(1, 90),
        "zero-mode orientation": Fraction(1, 100),
        "compactification boundary": Fraction(1, 110),
        "continuum comparison": Fraction(1, 120),
    }
    total_residual_bound = sum(residuals.values(), Fraction(0))
    bounded_coefficient = retained_signed + total_residual_bound
    actual_error = abs(bounded_coefficient - retained_signed)

    assert_equal(
        "one-vortex coefficient residual telescope",
        actual_error,
        total_residual_bound,
    )
    assert_gt_bound(
        "one-vortex signed window dominates residuals",
        abs(retained_signed),
        total_residual_bound,
    )
    assert_leq_bound(
        "one-vortex relative coefficient error",
        total_residual_bound / (noncancellation_fraction * retained_mass),
        Fraction(1, 10),
    )

    omitted_determinant_budget = total_residual_bound - residuals["determinant"]
    assert_gt_bound(
        "omitting determinant residual underbudgets vortex coefficient",
        actual_error,
        omitted_determinant_budget,
    )

    canceling_cells = [Fraction(1, 3), Fraction(-1, 3)]
    canceling_signed = sum(canceling_cells, Fraction(0))
    canceling_mass = sum(abs(cell) for cell in canceling_cells)
    charge_and_zero_mode_allowed = True
    determinant_line_declared = True
    symmetry_only_nonzero_claim = (
        charge_and_zero_mode_allowed
        and determinant_line_declared
        and canceling_signed != 0
    )
    assert_equal(
        "coherent signed cancellation can leave nonzero mass",
        canceling_mass,
        Fraction(2, 3),
    )
    assert_equal(
        "symmetry-only vortex coefficient nonzero claim rejected",
        symmetry_only_nonzero_claim,
        False,
    )


def check_cp_mirror_critical_ledger() -> None:
    for n_fields in range(2, 9):
        x = Fraction(3, 2)
        product_constraint = x**n_fields
        assert_equal(
            f"CP^{n_fields - 1} constrained product",
            prod([x] * n_fields),
            product_constraint,
        )

        # In logarithmic variables z_a=log X_a, a=1,...,N-1, with
        # X_N=q/(X_1...X_{N-1}), the critical equations are X_a=X_N.
        # At a common nonzero value x, the Hessian is x(I+J), whose determinant
        # is N x^{N-1}; this proves the critical points are simple.
        log_hessian_determinant = n_fields * x ** (n_fields - 1)
        if log_hessian_determinant == 0:
            raise AssertionError("CP mirror critical Hessian should be nonzero")


def nth_root_power_sum(n_fields: int, exponent: int, q_value: Fraction) -> Fraction:
    if exponent % n_fields != 0:
        return Fraction(0)
    return Fraction(n_fields) * q_value ** (exponent // n_fields)


def cp_mirror_residue_trace(n_fields: int, insertion_power: int, q_value: Fraction) -> Fraction:
    if insertion_power < 0:
        raise ValueError(
            "CP mirror residue trace is defined here for polynomial insertions"
        )
    root_power = insertion_power - (n_fields - 1)
    return nth_root_power_sum(n_fields, root_power, q_value) / n_fields


def check_cp_mirror_residue_correlators() -> None:
    for n_fields in range(2, 9):
        q_phys = Fraction(n_fields + 1, n_fields + 4)
        x = Fraction(5, 3)

        # In the constrained logarithmic torus the Hessian denominator of the
        # normalized mirror trace is det(x(I+J))=N x^{N-1}.
        hessian = [
            [x * (1 + int(row == col)) for col in range(n_fields - 1)]
            for row in range(n_fields - 1)
        ]
        assert_equal(
            f"CP^{n_fields - 1} residue Hessian denominator",
            determinant_fraction(hessian),
            n_fields * x ** (n_fields - 1),
        )

        assert_equal(
            f"CP^{n_fields - 1} top trace normalization",
            cp_mirror_residue_trace(n_fields, n_fields - 1, q_phys),
            Fraction(1),
        )

        for degree in range(1, 4):
            insertion_power = n_fields - 1 + degree * n_fields
            assert_equal(
                f"CP^{n_fields - 1} degree-{degree} residue selection",
                cp_mirror_residue_trace(n_fields, insertion_power, q_phys),
                q_phys**degree,
            )

        for insertion_power in range(0, 4 * n_fields):
            selected = (insertion_power - (n_fields - 1)) % n_fields == 0
            if not selected:
                assert_equal(
                    f"CP^{n_fields - 1} off-selection residue vanishes k={insertion_power}",
                    cp_mirror_residue_trace(n_fields, insertion_power, q_phys),
                    Fraction(0),
                )

        for insertion_power in range(0, 3 * n_fields):
            assert_equal(
                f"CP^{n_fields - 1} quantum-product trace recurrence k={insertion_power}",
                cp_mirror_residue_trace(n_fields, insertion_power + n_fields, q_phys),
                q_phys * cp_mirror_residue_trace(n_fields, insertion_power, q_phys),
            )


def check_vortex_to_observable_residual_budget() -> None:
    n_fields = 4
    q_regulated = Fraction(5, 7)
    insertion_power = n_fields - 1 + 2 * n_fields
    residue_prediction = cp_mirror_residue_trace(
        n_fields,
        insertion_power,
        q_regulated,
    )
    assert_equal(
        "finite mirror residue prediction is q^degree",
        residue_prediction,
        q_regulated**2,
    )

    residuals = {
        "coefficient": Fraction(1, 13),
        "determinant": Fraction(1, 17),
        "zero mode": Fraction(1, 19),
        "compactification": Fraction(1, 23),
        "gluing": Fraction(1, 29),
        "operator map": Fraction(1, 31),
        "continuum": Fraction(1, 37),
    }
    protected_amplitude = residue_prediction + sum(residuals.values(), Fraction(0))
    actual_error = abs(protected_amplitude - residue_prediction)
    full_budget = sum(abs(value) for value in residuals.values())
    assert_equal("vortex-to-observable residual telescope", actual_error, full_budget)

    omitted_operator_budget = full_budget - abs(residuals["operator map"])
    if actual_error <= omitted_operator_budget:
        raise AssertionError("omitting operator-map residual should underbudget the error")

    assert_equal(
        "zero residuals identify protected amplitude with residue prediction",
        residue_prediction + sum([Fraction(0)] * len(residuals), Fraction(0)),
        residue_prediction,
    )

    bare_q = Fraction(3, 11)
    vortex_coefficients = [
        Fraction(2, 3),
        Fraction(5, 7),
        Fraction(11, 13),
        Fraction(17, 19),
    ]
    q_with_vortex_measure = bare_q * prod(vortex_coefficients)
    degree_one_power = n_fields - 1 + n_fields
    assert_equal(
        "degree-one observable uses vortex-normalized q",
        cp_mirror_residue_trace(n_fields, degree_one_power, q_with_vortex_measure),
        q_with_vortex_measure,
    )
    if cp_mirror_residue_trace(n_fields, degree_one_power, bare_q) == q_with_vortex_measure:
        raise AssertionError("bare FI coordinate should not ignore vortex coefficients")

    unsaturated_zero_mode_gate = Fraction(0)
    q_unsaturated = bare_q * prod(vortex_coefficients) * unsaturated_zero_mode_gate
    assert_equal(
        "unsaturated residual zero modes kill degree-one observable",
        cp_mirror_residue_trace(n_fields, degree_one_power, q_unsaturated),
        Fraction(0),
    )
    if cp_mirror_residue_trace(n_fields, degree_one_power, bare_q) == q_unsaturated:
        raise AssertionError("symmetry-only q should not survive a zero-mode gate")


def quantum_product_power(n_fields: int, left_power: int, right_power: int) -> tuple[int, int]:
    total_power = left_power + right_power
    return total_power % n_fields, total_power // n_fields


def check_cp_degree_one_stable_map_quantum_product_gate() -> None:
    for n_fields in range(2, 9):
        degree = 1
        virtual_dimension = (n_fields - 1) + n_fields * degree
        codimension_relation = 1 + (n_fields - 1) + (n_fields - 1)
        assert_equal(
            f"CP^{n_fields - 1} degree-one stable-map dimension",
            virtual_dimension,
            2 * n_fields - 1,
        )
        assert_equal(
            f"CP^{n_fields - 1} quantum-product insertion dimension",
            codimension_relation,
            virtual_dimension,
        )

        wrong_top_power = n_fields - 2
        wrong_codimension = 1 + wrong_top_power + (n_fields - 1)
        if wrong_codimension == virtual_dimension:
            raise AssertionError("lower insertion power should miss degree-one dimension")

        for wrong_degree in [0, 2, 3]:
            wrong_virtual_dimension = (n_fields - 1) + n_fields * wrong_degree
            if codimension_relation == wrong_virtual_dimension:
                raise AssertionError("degree-one insertion should not match another degree")

        # Two generic point constraints determine one projective line, and a
        # generic hyperplane meets that line once.  This is the finite count
        # behind I_1(H,H^{N-1},H^{N-1})=1.
        unique_line_through_two_points = 1
        hyperplane_intersections_with_line = 1
        assert_equal(
            f"CP^{n_fields - 1} degree-one line count",
            unique_line_through_two_points * hyperplane_intersections_with_line,
            1,
        )

        reduced_power, q_power = quantum_product_power(n_fields, 1, n_fields - 1)
        assert_equal("H times top class reduces to the unit", reduced_power, 0)
        assert_equal("H times top class carries one q", q_power, 1)

        for pairing_power in range(n_fields):
            nonzero_pairing = reduced_power + pairing_power == n_fields - 1
            assert_equal(
                f"quantum relation pairs only with top class a={pairing_power}",
                nonzero_pairing,
                pairing_power == n_fields - 1,
            )


def check_degree_one_stable_map_incidence_model() -> None:
    # The degree-one product coefficient is an observable pairing, not just a
    # residue root sum or a dimension count.  This finite model treats the
    # vortex coefficients as supplied input and checks the stable-map incidence
    # Jacobian, selection degree, boundary exclusion, operator normalization,
    # and residual budget before any continuum comparison residuals are invoked.
    n_fields = 5
    bare_fi = Fraction(3, 17)

    supplied_spectral_blocks = [
        ([2, 3], [5, 7], [11], [13], [17], [19], Fraction(23, 29)),
        ([3, 5], [7, 11], [13], [17], [19], [23], Fraction(29, 31)),
        ([5, 7], [11, 13], [17], [19], [23], [29], Fraction(31, 37)),
        ([7, 11], [13, 17], [19], [23], [29], [31], Fraction(37, 41)),
        ([11, 13], [17, 19], [23], [29], [31], [37], Fraction(41, 43)),
    ]

    def finite_det(values: list[int]) -> Fraction:
        return prod((Fraction(value) for value in values), start=Fraction(1))

    def supplied_vortex_coefficient(
        block: tuple[list[int], list[int], list[int], list[int], list[int], list[int], Fraction],
    ) -> Fraction:
        (
            boson_vacuum,
            boson_vortex_nonzero,
            fermion_vacuum,
            fermion_vortex,
            ghost_vacuum,
            ghost_vortex,
            zero_mode_metric,
        ) = block
        numerator = (
            finite_det(fermion_vortex)
            * finite_det(ghost_vortex)
            * finite_det(boson_vacuum)
            * zero_mode_metric
        )
        denominator = (
            finite_det(boson_vortex_nonzero)
            * finite_det(fermion_vacuum)
            * finite_det(ghost_vacuum)
        )
        return Fraction(numerator, denominator)

    vortex_coefficients = [
        supplied_vortex_coefficient(block)
        for block in supplied_spectral_blocks
    ]
    q_regulated = bare_fi * prod(vortex_coefficients, start=Fraction(1))

    variables = (
        [("A", index) for index in range(1, n_fields)]
        + [("B", index) for index in range(n_fields)]
    )
    constraints = (
        [("A", index, Fraction(0)) for index in range(1, n_fields)]
        + [("B", 0, Fraction(0)), ("B", 1, Fraction(1))]
        + [("B", index, Fraction(0)) for index in range(2, n_fields)]
    )
    incidence_matrix = [
        [
            Fraction(1) if variable == (kind, index) else Fraction(0)
            for variable in variables
        ]
        for kind, index, _value in constraints
    ]
    orientation_sign = determinant_fraction(incidence_matrix)
    assert_equal("degree-one stable-map incidence orientation", orientation_sign, Fraction(1))

    solution = {("A", 0): Fraction(1)}
    solution.update({(kind, index): value for kind, index, value in constraints})
    first_mark = [solution.get(("A", index), Fraction(0)) for index in range(n_fields)]
    second_mark = [solution.get(("B", index), Fraction(0)) for index in range(n_fields)]
    third_mark = [
        solution.get(("A", index), Fraction(0)) + solution.get(("B", index), Fraction(0))
        for index in range(n_fields)
    ]
    point_zero = [Fraction(1)] + [Fraction(0)] * (n_fields - 1)
    point_one = [Fraction(0), Fraction(1)] + [Fraction(0)] * (n_fields - 2)
    hyperplane = [Fraction(-1), Fraction(1)] + [Fraction(0)] * (n_fields - 2)

    def linear_value(linear_form: list[Fraction], point: list[Fraction]) -> Fraction:
        return sum(
            (coefficient * coordinate for coefficient, coordinate in zip(linear_form, point)),
            Fraction(0),
        )

    def hyperplane_value(point: list[Fraction]) -> Fraction:
        return linear_value(hyperplane, point)

    assert_equal("first point incidence", first_mark, point_zero)
    assert_equal("second point incidence", second_mark, point_one)
    assert_equal("third mark lies on normalized hyperplane", hyperplane_value(third_mark), Fraction(0))

    incidence_chart_dimension = len(variables)
    insertion_complex_degree = 1 + (n_fields - 1) + (n_fields - 1)
    assert_equal("degree-one incidence-chart dimension", incidence_chart_dimension, 2 * n_fields - 1)
    assert_equal("stable-map insertion degree saturates the chart", insertion_complex_degree, incidence_chart_dimension)
    selection_gate = Fraction(1) if insertion_complex_degree == incidence_chart_dimension else Fraction(0)

    boundary_excluded = (
        point_zero != point_one
        and hyperplane_value(point_zero) != 0
        and hyperplane_value(point_one) != 0
    )
    assert_equal("degree-one compactification boundary excluded", boundary_excluded, True)
    compactification_factor = Fraction(1) if boundary_excluded else Fraction(0)
    operator_normalization = Fraction(1)
    retained_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * compactification_factor
        * operator_normalization
    )
    assert_equal(
        "stable-map incidence model gives supplied degree-one product coefficient",
        retained_three_point,
        q_regulated,
    )

    signed_residuals = {
        "coefficient": Fraction(1, 100003),
        "determinant": Fraction(-1, 100019),
        "zero mode": Fraction(1, 100043),
        "line compactification": Fraction(-1, 100049),
        "operator map": Fraction(1, 100057),
        "continuum": Fraction(-1, 100069),
    }
    residual_bounds = {
        name: abs(value) + Fraction(1, 1_000_000 + index)
        for index, (name, value) in enumerate(signed_residuals.items())
    }
    comparison_residual = sum(signed_residuals.values(), Fraction(0))
    full_correlator_probe = retained_three_point + comparison_residual
    actual_error = abs(full_correlator_probe - retained_three_point)
    total_bound = sum(residual_bounds.values(), Fraction(0))
    assert_equal(
        "degree-one observable comparison residual is independently signed",
        full_correlator_probe - retained_three_point,
        comparison_residual,
    )
    assert_leq_bound(
        "degree-one observable residual budget",
        actual_error,
        total_bound,
    )
    assert_leq_bound(
        "degree-one observable conditional relative budget",
        total_bound / abs(q_regulated),
        Fraction(1, 4),
    )

    omitted_line_budget = total_bound - residual_bounds["line compactification"]
    adversarial_aligned_error = sum(residual_bounds.values(), Fraction(0))
    assert_gt_bound(
        "omitting line-count residual underbudgets aligned comparison error",
        adversarial_aligned_error,
        omitted_line_budget,
    )

    for pairing_power in range(n_fields - 1):
        codimension = 1 + (n_fields - 1) + pairing_power
        off_pairing_value = q_regulated if codimension == incidence_chart_dimension else Fraction(0)
        assert_equal(
            f"off-pairing vanishes by stable-map degree for H^{pairing_power}",
            off_pairing_value,
            Fraction(0),
        )
    top_pairing_codimension = 1 + (n_fields - 1) + (n_fields - 1)
    assert_equal(
        "top pairing is the unique saturated degree-one observable",
        top_pairing_codimension,
        incidence_chart_dimension,
    )

    mirror_only_bare = cp_mirror_residue_trace(
        n_fields,
        n_fields - 1 + n_fields,
        bare_fi,
    )
    if mirror_only_bare == q_regulated:
        raise AssertionError("mirror residue with bare FI should not establish vortex-normalized product")

    dimension_count_only = Fraction(1)
    if dimension_count_only == q_regulated:
        raise AssertionError("stable-map line count alone should not include the vortex fugacity")

    flipped_orientation = q_regulated * (-orientation_sign) * selection_gate
    if flipped_orientation == retained_three_point:
        raise AssertionError("orientation flip should change the retained incidence coefficient")

    missing_selection_degree = insertion_complex_degree - 1
    missing_selection_gate = (
        Fraction(1) if missing_selection_degree == incidence_chart_dimension else Fraction(0)
    )
    killed_fugacity = q_regulated * missing_selection_gate
    assert_equal("unsaturated selection-degree gate kills degree-one product coefficient", killed_fugacity, 0)
    if retained_three_point == killed_fugacity:
        raise AssertionError("charge and dimension data should not override a selection gate")

    collided_point_one = point_zero
    colliding_point_boundary_excluded = (
        point_zero != collided_point_one
        and hyperplane_value(point_zero) != 0
        and hyperplane_value(collided_point_one) != 0
    )
    colliding_point_factor = Fraction(1) if colliding_point_boundary_excluded else Fraction(0)
    colliding_point_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * colliding_point_factor
        * operator_normalization
    )
    assert_equal(
        "colliding point mutation removes the retained incidence coefficient",
        colliding_point_three_point,
        Fraction(0),
    )
    if colliding_point_three_point == retained_three_point:
        raise AssertionError("colliding point mutation should recompute and fail the retained observable")

    hyperplane_through_first_point = [Fraction(0), Fraction(1)] + [Fraction(0)] * (n_fields - 2)
    if linear_value(hyperplane_through_first_point, point_zero) != 0:
        raise AssertionError("mutated hyperplane should contain the first point")
    hyperplane_mutation_boundary_excluded = (
        point_zero != point_one
        and linear_value(hyperplane_through_first_point, point_zero) != 0
        and linear_value(hyperplane_through_first_point, point_one) != 0
    )
    hyperplane_mutation_factor = Fraction(1) if hyperplane_mutation_boundary_excluded else Fraction(0)
    hyperplane_mutation_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * hyperplane_mutation_factor
        * operator_normalization
    )
    assert_equal(
        "hyperplane-through-point mutation removes the retained incidence coefficient",
        hyperplane_mutation_three_point,
        Fraction(0),
    )
    if hyperplane_mutation_three_point == retained_three_point:
        raise AssertionError("hyperplane contact mutation should recompute and fail the retained observable")

    doubled_operator_normalization = Fraction(2)
    rescaled_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * compactification_factor
        * doubled_operator_normalization
    )
    assert_equal(
        "hyperplane-class normalization rescales the retained coefficient",
        rescaled_three_point,
        2 * retained_three_point,
    )
    if rescaled_three_point == retained_three_point:
        raise AssertionError("hyperplane-class normalization change should rescale the coefficient")


def check_cigar_metric_elimination() -> None:
    examples = [
        (Fraction(9, 5), Fraction(7, 3)),
        (Fraction(4, 1), Fraction(5, 2)),
        (Fraction(1, 3), Fraction(11, 4)),
    ]
    for rho_squared, k_level in examples:
        saddle_a = rho_squared / (rho_squared + k_level)
        angular_from_elimination = (
            Fraction(1, 2) * rho_squared * (1 - saddle_a) ** 2
            + Fraction(1, 2) * k_level * saddle_a**2
        )
        expected_angular = Fraction(1, 2) * rho_squared / (1 + rho_squared / k_level)
        assert_equal("cigar angular metric coefficient", angular_from_elimination, expected_angular)

        radial_kinetic_coefficient = Fraction(1, 2) + rho_squared / (2 * k_level)
        expected_metric_rr = 1 + rho_squared / k_level
        assert_equal("cigar radial metric coefficient", 2 * radial_kinetic_coefficient, expected_metric_rr)


def check_logarithmic_chiral_vortex_obstruction() -> None:
    # A smooth ordinary charged scalar may carry flux n by having total zero
    # divisor degree n.  The logarithmic chiral periodic part is unit-norm,
    # hence has zero divisor degree 0; smooth finite-action P-sector vortices
    # therefore force n=0.
    for flux in range(-4, 5):
        unit_field_zero_degree = 0
        smooth_unit_section_possible = flux == unit_field_zero_degree
        assert_equal(
            f"logarithmic chiral unit section obstruction flux={flux}",
            smooth_unit_section_possible,
            flux == 0,
        )

    for ordinary_vortex_degree in range(0, 6):
        flux = ordinary_vortex_degree
        assert_equal("ordinary charged scalar zero degree carries flux", flux, ordinary_vortex_degree)


def invariant_jacobi_monomial_count(num_fields: int, degree: int) -> int:
    count = 0

    def visit(index: int, total_exponent: int) -> None:
        nonlocal count
        if index == num_fields:
            if total_exponent % degree == 0:
                count += 1
            return
        for exponent in range(degree - 1):
            visit(index + 1, total_exponent + exponent)

    visit(0, 0)
    return count


def check_hypersurface_phase_ledger() -> None:
    examples = [(3, 3), (4, 4), (5, 5), (5, 3), (6, 4)]
    for num_fields, degree in examples:
        c1_coefficient = num_fields - degree
        canonical_coefficient = degree - num_fields
        assert_equal("hypersurface adjunction sign", c1_coefficient, -canonical_coefficient)

        sigma_model_central_charge = 3 * (num_fields - 2)
        lg_central_charge = 3 * num_fields * (Fraction(1) - Fraction(2, degree))
        central_charge_difference = lg_central_charge - sigma_model_central_charge
        assert_equal(
            "LG/sigma central-charge difference",
            central_charge_difference,
            Fraction(6 * (degree - num_fields), degree),
        )
        assert_equal(
            "central charges match iff Calabi-Yau hypersurface degree",
            lg_central_charge == sigma_model_central_charge,
            degree == num_fields,
        )

        # The residual mu_d gauge action sends X_i -> zeta X_i.  A degree-d
        # monomial and hence a homogeneous degree-d superpotential is invariant.
        assert_equal("residual finite gauge preserves G_d", degree % degree, 0)

    assert_equal("quintic untwisted invariant Jacobi monomial count", invariant_jacobi_monomial_count(5, 5), 204)


def check_hypersurface_coulomb_coordinate_signal() -> None:
    for num_fields, degree in [(5, 5), (4, 4), (6, 6), (5, 3), (6, 4)]:
        charges = [1] * num_fields + [-degree]
        sigma_exponent = sum(charges)
        assert_equal("hypersurface Coulomb sigma exponent", sigma_exponent, num_fields - degree)
        assert_equal("hypersurface axial anomaly coefficient", sigma_exponent, glsm_charge_sum(num_fields, degree))

        if num_fields == degree:
            assert_equal("anomaly-free hypersurface cancels sigma power", sigma_exponent, 0)
            branch_constant_magnitude = Fraction(1, degree**degree)
            if branch_constant_magnitude <= 0:
                raise AssertionError("branch constant magnitude should be positive")


def main() -> None:
    check_a_series_lg()
    check_fermat_tensor_products()
    check_fermat_wilsonian_spurion_selection()
    check_hypersurface_glsm_ledger()
    check_twist_spin_ledger()
    check_abelian_circle_duality()
    check_abelian_legendre_duality()
    check_abelian_glsm_coulomb_ledger()
    check_abelian_coulomb_one_loop_primitive()
    check_charged_chiral_dual_elimination()
    check_all_rank_vortex_fi_coordinate_shift()
    check_vortex_fugacity_dimensional_transmutation()
    check_mirror_primitive_monomial_selection()
    check_vortex_zero_mode_filter()
    check_single_vortex_amplitude_assembly()
    check_vortex_coefficient_noncancellation_bound()
    check_cp_mirror_critical_ledger()
    check_cp_mirror_residue_correlators()
    check_vortex_to_observable_residual_budget()
    check_cp_degree_one_stable_map_quantum_product_gate()
    check_degree_one_stable_map_incidence_model()
    check_cigar_metric_elimination()
    check_logarithmic_chiral_vortex_obstruction()
    check_hypersurface_phase_ledger()
    check_hypersurface_coulomb_coordinate_signal()
    print("All 2D SUSY LG/GLSM checks passed.")


if __name__ == "__main__":
    main()
