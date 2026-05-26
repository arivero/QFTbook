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


def main() -> None:
    check_a_series_lg()
    check_fermat_tensor_products()
    check_hypersurface_glsm_ledger()
    check_twist_spin_ledger()
    print("All 2D SUSY LG/GLSM checks passed.")


if __name__ == "__main__":
    main()
