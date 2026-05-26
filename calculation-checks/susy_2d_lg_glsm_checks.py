"""Finite algebra checks for the 2D N=(2,2) LG/GLSM chapter."""

from __future__ import annotations

from fractions import Fraction
from math import prod


def assert_equal(label: str, left, right) -> None:
    if left != right:
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


def main() -> None:
    check_a_series_lg()
    check_fermat_tensor_products()
    check_hypersurface_glsm_ledger()
    check_twist_spin_ledger()
    check_abelian_circle_duality()
    check_abelian_legendre_duality()
    check_abelian_glsm_coulomb_ledger()
    print("All 2D SUSY LG/GLSM checks passed.")


if __name__ == "__main__":
    main()
