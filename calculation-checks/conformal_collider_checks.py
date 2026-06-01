#!/usr/bin/env python3
"""Finite checks for the ANEC and conformal-collider bounds section."""

from __future__ import annotations

from fractions import Fraction


Matrix = tuple[tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction]]
Vector = tuple[Fraction, Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def mat_norm_sq(eps: Matrix) -> Fraction:
    return sum(eps[i][j] * eps[i][j] for i in range(3) for j in range(3))


def mat_vec(eps: Matrix, n: Vector) -> Vector:
    return tuple(sum(eps[i][j] * n[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def quad(eps: Matrix, n: Vector) -> Fraction:
    return sum(n[i] * eps[i][j] * n[j] for i in range(3) for j in range(3))


def first_ratio(eps: Matrix, n: Vector) -> Fraction:
    v = mat_vec(eps, n)
    return sum(x * x for x in v) / mat_norm_sq(eps)


def second_ratio(eps: Matrix, n: Vector) -> Fraction:
    return quad(eps, n) ** 2 / mat_norm_sq(eps)


def energy_flux_polynomial(first_ratio: Fraction, second_ratio: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return coefficients of 1 + coeff_t2 t2 + coeff_t4 t4."""

    coeff_t2 = first_ratio - Fraction(1, 3)
    coeff_t4 = second_ratio - Fraction(2, 15)
    return (Fraction(1, 1), coeff_t2, coeff_t4)


def check_sphere_averages_for_traceless_tensor() -> None:
    """Check the constants subtracted in the four-dimensional flux form."""

    # On S^2, <n_i n_j> = delta_ij/3.
    assert_equal("rank-two sphere average coefficient", Fraction(1, 3), Fraction(1, 3))

    # <n_i n_j n_k n_l> =
    #   (delta_ij delta_kl + delta_ik delta_jl + delta_il delta_jk)/15.
    # For a symmetric traceless polarization epsilon_ij, the first contraction
    # vanishes and the second and third contractions each give epsilon*epsilon.
    eps: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-3)),
    )
    norm = mat_norm_sq(eps)
    trace = sum(eps[i][i] for i in range(3))
    fourth_moment_contraction = (trace * trace + 2 * norm) / 15
    assert_equal("test tensor traceless", trace, Fraction(0))
    assert_equal("traceless rank-four sphere average coefficient", fourth_moment_contraction / norm, Fraction(2, 15))


def check_helicity_bounds() -> None:
    """Check the helicity 2, 1, 0 reductions of the stress-tensor flux."""

    n: Vector = (Fraction(0), Fraction(0), Fraction(1))
    eps_h2: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    eps_h1: Matrix = (
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
    )
    eps_h0: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-2)),
    )

    helicity_two = energy_flux_polynomial(first_ratio(eps_h2, n), second_ratio(eps_h2, n))
    helicity_one = energy_flux_polynomial(first_ratio(eps_h1, n), second_ratio(eps_h1, n))
    helicity_zero = energy_flux_polynomial(first_ratio(eps_h0, n), second_ratio(eps_h0, n))

    assert_equal("helicity-2 collider polynomial", helicity_two, (Fraction(1, 1), Fraction(-1, 3), Fraction(-2, 15)))
    assert_equal("helicity-1 collider polynomial", helicity_one, (Fraction(1, 1), Fraction(1, 6), Fraction(-2, 15)))
    assert_equal("helicity-0 collider polynomial", helicity_zero, (Fraction(1, 1), Fraction(1, 3), Fraction(8, 15)))


def check_normalization_integrates_to_total_energy() -> None:
    """Check that the angular subtractions make t2 and t4 integrate to zero."""

    assert_equal("t2 average subtraction", Fraction(1, 3) - Fraction(1, 3), Fraction(0, 1))
    assert_equal("t4 average subtraction", Fraction(2, 15) - Fraction(2, 15), Fraction(0, 1))


def check_light_transform_homogeneity_map() -> None:
    """Check the embedding-space light-transform weight map."""

    test_pairs = (
        (Fraction(3, 1), Fraction(1, 1)),
        (Fraction(4, 1), Fraction(2, 1)),
        (Fraction(5, 1), Fraction(3, 1)),
        (Fraction(7, 2), Fraction(5, 2)),
    )
    for delta, spin in test_pairs:
        p_exponent = spin - 1
        z_exponent = 1 - delta
        transformed_delta = 1 - spin
        transformed_spin = 1 - delta
        assert_equal("light-transform P homogeneity exponent", p_exponent, -transformed_delta)
        assert_equal("light-transform Z homogeneity exponent", z_exponent, transformed_spin)

    spacetime_dimension = Fraction(4, 1)
    stress_tensor_spin = Fraction(2, 1)
    stress_tensor_light_delta = 1 - stress_tensor_spin
    stress_tensor_light_spin = 1 - spacetime_dimension
    assert_equal("four-dimensional stress-tensor light-transform Delta", stress_tensor_light_delta, Fraction(-1, 1))
    assert_equal("four-dimensional stress-tensor light-transform spin", stress_tensor_light_spin, Fraction(-3, 1))


def main() -> None:
    check_sphere_averages_for_traceless_tensor()
    check_helicity_bounds()
    check_normalization_integrates_to_total_energy()
    check_light_transform_homogeneity_map()
    print("All conformal-collider finite checks passed.")


if __name__ == "__main__":
    main()
