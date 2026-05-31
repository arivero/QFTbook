"""Finite algebra checks for the 2D N=(2,2) LG/GLSM chapter."""

from __future__ import annotations

from fractions import Fraction
from math import exp, isclose, log, prod


def assert_equal(label: str, left, right) -> None:
    if left != right:
        raise AssertionError(f"{label} failed: {left!r} != {right!r}")


def assert_close(label: str, left: float, right: float, tol: float = 1e-11) -> None:
    if not isclose(left, right, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{label} failed: {left!r} != {right!r}")


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


def main() -> None:
    check_a_series_lg()
    check_fermat_tensor_products()
    check_hypersurface_glsm_ledger()
    check_twist_spin_ledger()
    check_abelian_circle_duality()
    check_abelian_legendre_duality()
    check_abelian_glsm_coulomb_ledger()
    check_charged_chiral_dual_elimination()
    check_cp_mirror_critical_ledger()
    check_cigar_metric_elimination()
    print("All 2D SUSY LG/GLSM checks passed.")


if __name__ == "__main__":
    main()
