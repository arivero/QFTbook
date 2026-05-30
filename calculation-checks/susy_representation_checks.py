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


def check_hls_central_charge_combined_symmetry():
    # The left-left anticommutator is 2 epsilon_{alpha beta} Z^{IJ}; the
    # factor 2 is irrelevant for the combined-index symmetry checked here.
    # It must be symmetric under exchange of the combined labels
    # (I, alpha) <-> (J, beta).  This holds exactly when Z is antisymmetric.
    epsilon_spinor = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): -1,
        (1, 1): 0,
    }
    z_internal = {}
    for i in range(3):
        for j in range(3):
            if i == j:
                z_internal[(i, j)] = 0
            elif i < j:
                z_internal[(i, j)] = Fraction(i + j + 1)
                z_internal[(j, i)] = -z_internal[(i, j)]

    for i in range(3):
        for j in range(3):
            for alpha in range(2):
                for beta in range(2):
                    lhs = epsilon_spinor[(alpha, beta)] * z_internal[(i, j)]
                    rhs = epsilon_spinor[(beta, alpha)] * z_internal[(j, i)]
                    assert_equal(
                        lhs,
                        rhs,
                        f"HLS central-charge combined symmetry {(i, alpha, j, beta)}",
                    )


def check_hls_internal_invariance_condition():
    # For N=2 the antisymmetric tensor epsilon_{IJ} is invariant under the
    # infinitesimal SO(2) generator T, while a diagonal U(1)-like generator
    # fails the invariance equation T Z + Z T^T = 0.
    z = [[0, 1], [-1, 0]]
    so2_generator = [[0, 1], [-1, 0]]
    diagonal_generator = [[1, 0], [0, 1]]

    def matmul(a, b):
        return [
            [sum(a[row][k] * b[k][col] for k in range(2)) for col in range(2)]
            for row in range(2)
        ]

    def transpose(a):
        return [[a[col][row] for col in range(2)] for row in range(2)]

    def add(a, b):
        return [[a[row][col] + b[row][col] for col in range(2)] for row in range(2)]

    zero = [[0, 0], [0, 0]]
    so2_variation = add(matmul(so2_generator, z), matmul(z, transpose(so2_generator)))
    diagonal_variation = add(
        matmul(diagonal_generator, z),
        matmul(z, transpose(diagonal_generator)),
    )
    assert_equal(so2_variation, zero, "SO(2) leaves N=2 central charge invariant")
    assert_equal(
        diagonal_variation == zero,
        False,
        "diagonal phase does not leave fixed N=2 central charge invariant",
    )


def check_hls_lorentz_tensor_dimension_ledger():
    # (1/2,0) x (0,1/2) is the four-dimensional vector representation.
    left_dim = 2
    right_dim = 2
    assert_equal(left_dim * right_dim, 4, "mixed Weyl product is vector-dimensional")

    # Sym^2 C^2 has dimension 3 and wedge^2 C^2 has dimension 1:
    # the former would be a self-dual tensor charge, the latter is the
    # scalar central-charge structure used in the HLS algebra.
    sym_square_dim = 2 * (2 + 1) // 2
    wedge_square_dim = 2 * (2 - 1) // 2
    assert_equal(sym_square_dim, 3, "left-left symmetric spinor tensor dimension")
    assert_equal(wedge_square_dim, 1, "left-left antisymmetric spinor scalar dimension")


def main():
    check_massive_n1_fock_dimensions()
    check_massive_spin_decomposition_dimension()
    check_massless_rank_one_norm_matrix()
    check_bps_bound_block_eigenvalues()
    check_bps_bound_violation_detected()
    check_hls_central_charge_combined_symmetry()
    check_hls_internal_invariance_condition()
    check_hls_lorentz_tensor_dimension_ledger()
    print("All supersymmetry representation checks passed.")


if __name__ == "__main__":
    main()
