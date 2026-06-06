#!/usr/bin/env python3
r"""Convention checks for gamma traces and anomaly normalizations.

The matrices here use the monograph's mostly-plus convention
eta = diag(-1, +1, +1, +1), Dirac adjoint convention, and
gamma_5 = -i gamma^0 gamma^1 gamma^2 gamma^3.

The four-dimensional matrices are the Weinberg-compatible matrices used in
the stringbook spinor appendix and in its "gamma matrices.nb" notebook:

    gamma^0 = -i [[0, I], [I, 0]],
    gamma^j = -i [[0, sigma_j], [-sigma_j, 0]].

The script deliberately checks only finite-dimensional algebraic identities.
It does not evaluate divergent loop integrals.

Evidence contract.

Target claims:
  Volume I spinor conventions and Volume II anomaly calculations use the
  mostly-plus Clifford algebra, the monograph chirality matrix
  gamma_5=-i gamma^0 gamma^1 gamma^2 gamma^3, the orientation convention
  epsilon^{0123}=+1, the two-dimensional Dirac anomaly trace, the
  Weinberg/Wess-Bagger chiral phase translation, and the factor-one-half
  anticommutator normalization entering nonabelian anomaly coefficients.

Independent construction:
  The checks build the gamma matrices directly from Pauli blocks, reconstruct
  gamma_5 from their ordered product, extract the oriented four-dimensional
  epsilon coefficient by antisymmetrizing all finite traces, repeat that
  coefficient in the Wess-Bagger-related basis, and compute the two-dimensional
  anomaly trace from an independent two-by-two Clifford system.  They do not
  use a manuscript-expanded anomaly coefficient as input.

Imported assumptions:
  The use of these finite traces inside a renormalized anomaly calculation
  imports the regulator prescription, Ward-identity/counterterm convention,
  gauge-generator trace normalization, and loop-integral normalization from
  the anomaly chapter.  The companion checks the finite spin-trace slots only.

Negative controls:
  The suite rejects flipping the gamma_5 orientation sign, replacing the
  two-dimensional trace by a four-dimensional restricted block, using a
  four-dimensional gamma_5 trace for the two-dimensional anomaly, and omitting
  the factor one half that converts the raw anticommutator trace to the mixed
  anomaly coefficient.

Scope boundary:
  These are finite Clifford, trace, orientation, and convention-translation
  checks.  They are not loop calculations, anomaly nonrenormalization proofs,
  regulator constructions, or nonperturbative definitions of chiral fermion
  path integrals.

Primary derivation route:
  The manuscript route fixes the mostly-plus spinor pairing, defines gamma_5
  and epsilon orientation, states the four-gamma trace identity, and then uses
  those finite spin traces as convention input for perturbative and
  heat-kernel anomaly representatives.

Independent verification route:
  The executable route starts from explicit Pauli matrices and reconstructs
  every trace coefficient by matrix multiplication, basis conjugation,
  antisymmetric projection, and a separate two-dimensional Clifford algebra.

Convention dependencies:
  Mostly-plus metric eta=(-,+,+,+), Dirac adjoint beta=i gamma^0, gamma_5=-i
  gamma^0 gamma^1 gamma^2 gamma^3, epsilon^{0123}=+1, epsilon^{01}=+1 in the
  two-dimensional Dirac anomaly convention, and Hermitian generator traces
  normalized separately in the gauge chapters.

Domain and remainder assumptions:
  The checks apply to finite spinor trace algebra before loop integration.
  Physical anomaly formulae still require the regulator split, local
  counterterm representative, gauge trace convention, source normalization,
  and distributional Ward-identity manipulations to be supplied.

Remaining unproved or conditional:
  Divergent triangle integrals, heat-kernel asymptotics, index-theorem input,
  anomaly-line/global-anomaly claims, and all-order anomaly conclusions remain
  outside this finite companion.
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


def assert_not_close(name: str, lhs: np.ndarray | complex, rhs: np.ndarray | complex) -> None:
    if np.allclose(lhs, rhs, atol=1e-12):
        raise AssertionError(f"{name} unexpectedly matched:\n{lhs}\n==\n{rhs}")


def gamma5_trace(
    chirality: np.ndarray,
    matrices: list[np.ndarray],
    indices: tuple[int, int, int, int],
) -> complex:
    return np.trace(
        chirality
        @ matrices[indices[0]]
        @ matrices[indices[1]]
        @ matrices[indices[2]]
        @ matrices[indices[3]]
    )


def four_dimensional_orientation_coefficient(
    chirality: np.ndarray,
    matrices: list[np.ndarray],
) -> complex:
    total = 0j
    for indices in itertools.permutations(range(4)):
        total += levi_civita(indices) * gamma5_trace(chirality, matrices, indices)
    return total / 24


def two_dimensional_trace_coefficient(
    matrices: list[np.ndarray],
    chirality: np.ndarray,
) -> complex:
    total = 0j
    for current_index, rho in itertools.product(range(2), repeat=2):
        trace = np.trace(matrices[current_index] @ chirality @ matrices[rho])
        total += levi_civita((rho, current_index)) * trace
    return total / 2


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
        lhs = gamma5_trace(gamma5, gamma, inds)
        rhs = 4j * levi_civita(inds)
        assert_close(f"gamma5 trace {inds}", lhs, rhs)


def check_four_dimensional_orientation_contract() -> None:
    assert_close(
        "oriented gamma5 trace coefficient",
        four_dimensional_orientation_coefficient(gamma5, gamma),
        4j,
    )

    gamma5_wess_bagger = (
        -1j
        * gamma_wess_bagger[0]
        @ gamma_wess_bagger[1]
        @ gamma_wess_bagger[2]
        @ gamma_wess_bagger[3]
    )
    assert_close(
        "Wess-Bagger basis preserves oriented gamma5 trace coefficient",
        four_dimensional_orientation_coefficient(gamma5_wess_bagger, gamma_wess_bagger),
        4j,
    )

    wrong_gamma5 = -gamma5
    wrong_orientation_coefficient = four_dimensional_orientation_coefficient(wrong_gamma5, gamma)
    assert_close("wrong gamma5 sign flips anomaly trace coefficient", wrong_orientation_coefficient, -4j)
    assert_not_close(
        "wrong gamma5 sign is not the monograph anomaly convention",
        wrong_orientation_coefficient,
        4j,
    )


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


def check_two_dimensional_trace_contract() -> None:
    gamma2 = [1j * sigma2, sigma1]
    gamma2_chirality = gamma2[0] @ gamma2[1]
    assert_close(
        "2D anomaly trace coefficient",
        two_dimensional_trace_coefficient(gamma2, gamma2_chirality),
        2,
    )

    four_dimensional_two_plane_chirality = gamma[0] @ gamma[1]
    doubled_block_coefficient = two_dimensional_trace_coefficient(
        [gamma[0], gamma[1]],
        four_dimensional_two_plane_chirality,
    )
    assert_close("4D two-plane block doubles the 2D trace coefficient", doubled_block_coefficient, 4)
    assert_not_close(
        "4D two-plane block is not the 2D Dirac anomaly trace",
        doubled_block_coefficient,
        2,
    )

    four_dimensional_gamma5_projection = two_dimensional_trace_coefficient(
        [gamma[0], gamma[1]],
        gamma5,
    )
    assert_close("4D gamma5 gives no 2D two-gamma chirality trace", four_dimensional_gamma5_projection, 0)
    assert_not_close(
        "4D gamma5 projection is not the 2D Dirac anomaly trace",
        four_dimensional_gamma5_projection,
        2,
    )


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
    check_four_dimensional_orientation_contract()
    check_two_dimensional_trace()
    check_two_dimensional_trace_contract()
    check_abelian_anticommutator_normalization()
    print("All gamma-trace and anomaly-normalization checks passed.")


if __name__ == "__main__":
    main()
