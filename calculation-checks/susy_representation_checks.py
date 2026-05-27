#!/usr/bin/env python3
"""Finite checks for supersymmetry representation-theory conventions."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_massive_n1_fock_dimensions():
    for two_j in range(0, 8):
        little_group_dimension = two_j + 1
        fock_even = 2  # Lambda^0 C^2 plus Lambda^2 C^2.
        fock_odd = 2   # Lambda^1 C^2.
        assert_equal(
            little_group_dimension * (fock_even + fock_odd),
            4 * little_group_dimension,
            f"massive N=1 total dimension 2j={two_j}",
        )
        assert_equal(
            little_group_dimension * fock_even,
            little_group_dimension * fock_odd,
            f"massive N=1 boson/fermion balance 2j={two_j}",
        )


def check_massive_spin_decomposition_dimension():
    for two_j in range(0, 8):
        one_oscillator_dimension = 2 * (two_j + 1)
        spin_up_dimension = two_j + 2
        spin_down_dimension = two_j if two_j > 0 else 0
        assert_equal(
            spin_up_dimension + spin_down_dimension,
            one_oscillator_dimension,
            f"Clebsch-Gordan dimension check 2j={two_j}",
        )


def check_massless_rank_one_norm_matrix():
    # For p=(E,0,0,E), sigma.p is proportional to diag(2E,0), hence rank one.
    for energy in (Fraction(1), Fraction(3, 2), Fraction(5)):
        diagonal = [2 * energy, 0]
        rank = sum(entry != 0 for entry in diagonal)
        assert_equal(rank, 1, f"massless sigma.p rank E={energy}")


def check_bps_bound_block_eigenvalues():
    samples = [
        (Fraction(5), Fraction(3)),
        (Fraction(7, 2), Fraction(7, 2)),
        (Fraction(9), Fraction(0)),
    ]
    for mass, singular_value in samples:
        eigenvalues = [2 * (mass + singular_value), 2 * (mass - singular_value)]
        assert_equal(
            all(value >= 0 for value in eigenvalues),
            mass >= singular_value,
            f"BPS positivity equivalent to m>=z for m={mass}, z={singular_value}",
        )
        if mass == singular_value:
            assert_equal(min(eigenvalues), 0, "saturated BPS block has null supercharge")


def check_bps_bound_violation_detected():
    mass = Fraction(2)
    singular_value = Fraction(5)
    smallest_eigenvalue = 2 * (mass - singular_value)
    assert_equal(smallest_eigenvalue < 0, True, "BPS-bound violation gives negative norm")


def main():
    check_massive_n1_fock_dimensions()
    check_massive_spin_decomposition_dimension()
    check_massless_rank_one_norm_matrix()
    check_bps_bound_block_eigenvalues()
    check_bps_bound_violation_detected()
    print("All supersymmetry representation checks passed.")


if __name__ == "__main__":
    main()
