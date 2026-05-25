#!/usr/bin/env python3
"""Convention checks for gamma traces and anomaly normalizations.

The matrices here use the monograph's mostly-plus convention
eta = diag(-1, +1, +1, +1), Dirac adjoint convention, and
gamma_5 = -i gamma^0 gamma^1 gamma^2 gamma^3.

The four-dimensional matrices are the Weinberg-compatible matrices used in
the stringbook spinor appendix and in its "gamma matrices.nb" notebook:

    gamma^0 = -i [[0, I], [I, 0]],
    gamma^j = -i [[0, sigma_j], [-sigma_j, 0]].

The script deliberately checks only finite-dimensional algebraic identities.
It does not evaluate divergent loop integrals.
"""

from __future__ import annotations

import itertools
import numpy as np


I2 = np.eye(2, dtype=complex)
ZERO2 = np.zeros((2, 2), dtype=complex)

sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)


def block(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    return np.block([[a, b], [c, d]])


# Weinberg-compatible chiral representation adapted to mostly-plus signature.
gamma = [
    -1j * block(ZERO2, I2, I2, ZERO2),
    -1j * block(ZERO2, sigma1, -sigma1, ZERO2),
    -1j * block(ZERO2, sigma2, -sigma2, ZERO2),
    -1j * block(ZERO2, sigma3, -sigma3, ZERO2),
]

gamma_wess_bagger = [
    block(ZERO2, I2, -I2, ZERO2),
    block(ZERO2, sigma1, sigma1, ZERO2),
    block(ZERO2, sigma2, sigma2, ZERO2),
    block(ZERO2, sigma3, sigma3, ZERO2),
]
U_CHIRAL_PHASE = block(I2, ZERO2, ZERO2, 1j * I2)

eta = np.diag([-1, 1, 1, 1])
eps4 = {(0, 1, 2, 3): 1}


def levi_civita(indices: tuple[int, ...]) -> int:
    if len(set(indices)) != len(indices):
        return 0
    inv = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            inv += indices[i] > indices[j]
    return -1 if inv % 2 else 1


gamma5 = -1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]


def assert_close(name: str, lhs: np.ndarray | complex, rhs: np.ndarray | complex) -> None:
    if not np.allclose(lhs, rhs, atol=1e-12):
        raise AssertionError(f"{name} failed:\n{lhs}\n!=\n{rhs}")


def check_clifford() -> None:
    ident4 = np.eye(4, dtype=complex)
    for mu, nu in itertools.product(range(4), repeat=2):
        anti = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
        assert_close(f"Clifford {mu}{nu}", anti, 2 * eta[mu, nu] * ident4)


def check_gamma5() -> None:
    assert_close("gamma5 squared", gamma5 @ gamma5, np.eye(4, dtype=complex))
    assert_close("gamma5 explicit diagonal", gamma5, np.diag([1, 1, -1, -1]))
    for mu in range(4):
        assert_close(f"gamma5 anticommutes {mu}", gamma5 @ gamma[mu] + gamma[mu] @ gamma5, ZERO4)


def check_wess_bagger_phase_relation() -> None:
    inv_u = np.linalg.inv(U_CHIRAL_PHASE)
    for mu in range(4):
        assert_close(
            f"Weinberg/Wess-Bagger chiral phase {mu}",
            gamma[mu],
            U_CHIRAL_PHASE @ gamma_wess_bagger[mu] @ inv_u,
        )


def check_four_gamma_trace() -> None:
    for inds in itertools.product(range(4), repeat=4):
        lhs = np.trace(gamma5 @ gamma[inds[0]] @ gamma[inds[1]] @ gamma[inds[2]] @ gamma[inds[3]])
        rhs = 4j * levi_civita(inds)
        assert_close(f"gamma5 trace {inds}", lhs, rhs)


def check_two_dimensional_trace() -> None:
    # The two-dimensional anomaly calculation uses a two-component Dirac
    # fermion.  Restricting the four-dimensional matrices would double the
    # finite trace and would be the wrong calculation.  These are the d=2
    # starting matrices of the stringbook Clifford-recursion appendix.
    gamma2 = [1j * sigma2, sigma1]
    gamma2_chirality = gamma2[0] @ gamma2[1]
    for current_index in (0, 1):
        for rho in (0, 1):
            lhs = np.trace(gamma2[current_index] @ gamma2_chirality @ gamma2[rho])
            # The anomaly chapter uses
            #   tr(gamma^nu gamma pslash) = 2 epsilon^{rho nu} p_rho.
            # Equivalently, tr(gamma^nu gamma gamma^rho)=2 epsilon^{rho nu}.
            rhs = 2 * levi_civita((rho, current_index))
            assert_close(f"2D chirality trace {current_index}{rho}", lhs, rhs)


def check_abelian_anticommutator_normalization() -> None:
    one = np.array([[1]], dtype=complex)
    axial_left = one
    axial_right = -one
    vector = one
    coeff_without_half = np.trace(axial_left @ (vector @ vector + vector @ vector)) - np.trace(
        axial_right @ (vector @ vector + vector @ vector)
    )
    coeff_with_half = 0.5 * coeff_without_half
    assert_close("raw anticommutator gives four", coeff_without_half, 4)
    assert_close("mixed-anomaly coefficient gives two", coeff_with_half, 2)


ZERO4 = np.zeros((4, 4), dtype=complex)


def main() -> None:
    check_clifford()
    check_gamma5()
    check_wess_bagger_phase_relation()
    check_four_gamma_trace()
    check_two_dimensional_trace()
    check_abelian_anticommutator_normalization()
    print("All gamma-trace and anomaly-normalization checks passed.")


if __name__ == "__main__":
    main()
