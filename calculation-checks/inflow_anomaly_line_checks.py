#!/usr/bin/env python3
"""Exact checks for anomaly-line cocycles and finite inflow identities."""

from __future__ import annotations

from itertools import combinations


Simplex = tuple[int, ...]
Cochain = dict[Simplex, int]


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def anomaly_cocycle(n: int, level: int, gauge: int, background: int) -> int:
    """A Z_n translation-groupoid 1-cocycle in a chosen frame.

    The action is background -> background + gauge.  The term
    gauge * (gauge - 1) / 2 is integral for every integer gauge and is the
    finite-difference correction that makes composition functorial.
    """

    return level * (gauge * background + gauge * (gauge - 1) // 2) % n


def counterterm(n: int, quadratic: int, linear: int, background: int) -> int:
    """A local frame change used to test coboundary shifts of representatives."""

    return (quadratic * background * background + linear * background) % n


def check_functorial_cocycle_condition() -> None:
    for n in range(2, 17):
        for level in range(n):
            for background in range(n):
                for first in range(n):
                    for second in range(n):
                        lhs = anomaly_cocycle(n, level, first + second, background)
                        rhs = (
                            anomaly_cocycle(n, level, first, background + second)
                            + anomaly_cocycle(n, level, second, background)
                        ) % n
                        assert_equal(lhs, rhs, "anomaly-line functorial cocycle condition")


def transformed_cocycle(n: int, level: int, quadratic: int, linear: int, gauge: int, background: int) -> int:
    shifted = (background + gauge) % n
    return (
        anomaly_cocycle(n, level, gauge, background)
        + counterterm(n, quadratic, linear, background)
        - counterterm(n, quadratic, linear, shifted)
    ) % n


def check_counterterm_frame_change_preserves_cocycle() -> None:
    for n in range(2, 17):
        samples = sorted({0, 1, n // 2, n - 1})
        for level in samples:
            for quadratic in samples:
                for linear in samples:
                    for background in samples:
                        for first in samples:
                            for second in samples:
                                lhs = transformed_cocycle(n, level, quadratic, linear, first + second, background)
                                rhs = (
                                    transformed_cocycle(n, level, quadratic, linear, first, background + second)
                                    + transformed_cocycle(n, level, quadratic, linear, second, background)
                                ) % n
                                assert_equal(
                                    lhs,
                                    rhs,
                                    "local counterterm frame change preserves the anomaly cocycle condition",
                                )


def simplices(top_dimension: int, degree: int) -> list[Simplex]:
    return list(combinations(range(top_dimension + 1), degree + 1))


def coboundary(cochain: Cochain, degree: int, top_dimension: int, modulus: int) -> Cochain:
    result: Cochain = {}
    for simplex in simplices(top_dimension, degree + 1):
        total = 0
        for index in range(degree + 2):
            face = simplex[:index] + simplex[index + 1 :]
            total += (-1) ** index * cochain.get(face, 0)
        result[simplex] = total % modulus
    return result


def cup(lhs: Cochain, lhs_degree: int, rhs: Cochain, rhs_degree: int, top_dimension: int, modulus: int) -> Cochain:
    result: Cochain = {}
    for simplex in simplices(top_dimension, lhs_degree + rhs_degree):
        left_face = simplex[: lhs_degree + 1]
        right_face = simplex[lhs_degree:]
        result[simplex] = lhs.get(left_face, 0) * rhs.get(right_face, 0) % modulus
    return result


def integrate_simplex(cochain: Cochain, top_dimension: int, modulus: int) -> int:
    return cochain[tuple(range(top_dimension + 1))] % modulus


def integrate_boundary(cochain: Cochain, top_dimension: int, modulus: int) -> int:
    total = 0
    top = tuple(range(top_dimension + 1))
    for index in range(top_dimension + 1):
        face = top[:index] + top[index + 1 :]
        total += (-1) ** index * cochain.get(face, 0)
    return total % modulus


def deterministic_cochain(top_dimension: int, degree: int, modulus: int, seed: int) -> Cochain:
    values: Cochain = {}
    for simplex in simplices(top_dimension, degree):
        raw = seed
        for place, vertex in enumerate(simplex, start=1):
            raw += place * (vertex + 1) * (seed + 2)
        values[simplex] = raw % modulus
    return values


def check_finite_bf_boundary_variation() -> None:
    top_dimension = 5
    for modulus in range(2, 13):
        lam = deterministic_cochain(top_dimension, 1, modulus, seed=3)
        c_field = deterministic_cochain(top_dimension, 2, modulus, seed=5)
        kappa = deterministic_cochain(top_dimension, 1, modulus, seed=7)

        delta_lam = coboundary(lam, 1, top_dimension, modulus)
        delta_c = coboundary(c_field, 2, top_dimension, modulus)
        variation = cup(delta_lam, 2, delta_c, 3, top_dimension, modulus)

        boundary_cochain = cup(lam, 1, delta_c, 3, top_dimension, modulus)
        boundary_term = integrate_boundary(boundary_cochain, top_dimension, modulus)
        assert_equal(
            integrate_simplex(variation, top_dimension, modulus),
            boundary_term,
            "finite BF inflow variation equals boundary Stokes term",
        )

        delta_kappa = coboundary(kappa, 1, top_dimension, modulus)
        shifted_c = {
            simplex: (c_field[simplex] + delta_kappa[simplex]) % modulus
            for simplex in simplices(top_dimension, 2)
        }
        assert_equal(
            coboundary(shifted_c, 2, top_dimension, modulus),
            delta_c,
            "finite BF action is invariant under c -> c + delta kappa",
        )


def main() -> None:
    check_functorial_cocycle_condition()
    check_counterterm_frame_change_preserves_cocycle()
    check_finite_bf_boundary_variation()
    print("Anomaly-line and finite-inflow cochain checks passed.")


if __name__ == "__main__":
    main()
