#!/usr/bin/env python3
"""Exact finite checks for the spinor-convention section."""

from __future__ import annotations

import itertools

import sympy as sp


II = sp.I
I2 = sp.eye(2)
Z2 = sp.zeros(2)
I4 = sp.eye(4)
Z4 = sp.zeros(4)

sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -II], [II, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
pauli = [sigma1, sigma2, sigma3]


def block(a: sp.Matrix, b: sp.Matrix, c: sp.Matrix, d: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))


gamma = [
    -II * block(Z2, I2, I2, Z2),
    -II * block(Z2, sigma1, -sigma1, Z2),
    -II * block(Z2, sigma2, -sigma2, Z2),
    -II * block(Z2, sigma3, -sigma3, Z2),
]

gamma_wb = [
    block(Z2, I2, -I2, Z2),
    block(Z2, sigma1, sigma1, Z2),
    block(Z2, sigma2, sigma2, Z2),
    block(Z2, sigma3, sigma3, Z2),
]

eta4 = sp.diag(-1, 1, 1, 1)
epsilon2 = sp.Matrix([[0, 1], [-1, 0]])
beta = II * gamma[0]
gamma5 = -II * gamma[0] * gamma[1] * gamma[2] * gamma[3]


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def assert_matrix(label: str, lhs: sp.Matrix, rhs: sp.Matrix) -> None:
    diff = (lhs - rhs).applyfunc(sp.simplify)
    if diff != sp.zeros(*lhs.shape):
        raise AssertionError(f"{label} failed:\n{lhs}\n!=\n{rhs}")


def assert_scalar(label: str, lhs: sp.Expr, rhs: sp.Expr) -> None:
    if sp.simplify(lhs - rhs) != 0:
        raise AssertionError(f"{label} failed: {lhs} != {rhs}")


def levi_civita(indices: tuple[int, ...]) -> int:
    if len(set(indices)) != len(indices):
        return 0
    inversions = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            inversions += indices[i] > indices[j]
    return -1 if inversions % 2 else 1


def check_clifford_beta_and_slash_square() -> None:
    for mu, nu in itertools.product(range(4), repeat=2):
        anti = gamma[mu] * gamma[nu] + gamma[nu] * gamma[mu]
        assert_matrix(f"four-dimensional Clifford {mu}{nu}", anti, 2 * eta4[mu, nu] * I4)

    p0, p1, p2, p3 = sp.symbols("p0 p1 p2 p3")
    p = [p0, p1, p2, p3]
    slash = sum((p[mu] * gamma[mu] for mu in range(4)), Z4)
    norm = sum(eta4[mu, nu] * p[mu] * p[nu] for mu in range(4) for nu in range(4))
    assert_matrix("slash square", slash * slash, sp.simplify(norm) * I4)

    assert_matrix("beta Hermitian", dagger(beta), beta)
    assert_matrix("beta square", beta * beta, I4)
    for mu in range(4):
        assert_matrix(f"Dirac-adjoint identity {mu}", dagger(gamma[mu]) * beta, -beta * gamma[mu])


def check_spin_generators_and_gamma5_trace() -> None:
    generators = {}
    for mu, nu in itertools.product(range(4), repeat=2):
        generators[(mu, nu)] = -II * (gamma[mu] * gamma[nu] - gamma[nu] * gamma[mu]) / 4

    for mu, nu, rho in itertools.product(range(4), repeat=3):
        lhs = generators[(mu, nu)] * gamma[rho] - gamma[rho] * generators[(mu, nu)]
        rhs = -II * gamma[mu] * eta4[nu, rho] + II * gamma[nu] * eta4[mu, rho]
        assert_matrix(f"spin-generator commutator {mu}{nu}{rho}", lhs, rhs)

    for mu, nu in itertools.product(range(4), repeat=2):
        lhs = dagger(generators[(mu, nu)]) * beta
        rhs = beta * generators[(mu, nu)]
        assert_matrix(f"beta-pairing infinitesimal invariance {mu}{nu}", lhs, rhs)

    assert_matrix("gamma5 square", gamma5 * gamma5, I4)
    assert_matrix("gamma5 diagonal", gamma5, sp.diag(1, 1, -1, -1))
    for mu in range(4):
        assert_matrix(f"gamma5 anticommutator {mu}", gamma5 * gamma[mu] + gamma[mu] * gamma5, Z4)

    for indices in itertools.product(range(4), repeat=4):
        lhs = sp.trace(
            gamma5
            * gamma[indices[0]]
            * gamma[indices[1]]
            * gamma[indices[2]]
            * gamma[indices[3]]
        )
        rhs = 4 * II * levi_civita(indices)
        assert_scalar(f"gamma5 trace {indices}", lhs, rhs)


def check_two_component_rho_blocks() -> None:
    rho_pm = [gamma[mu][:2, 2:4] for mu in range(4)]
    rho_mp = [gamma[mu][2:4, :2] for mu in range(4)]
    for mu in range(4):
        rhs = (-epsilon2 * rho_mp[mu] * epsilon2).T
        assert_matrix(f"rho sign relation {mu}", rho_pm[mu], rhs)

    rho_down = [eta4[mu, mu] * rho_pm[mu] for mu in range(4)]
    for mu, nu in itertools.product(range(4), repeat=2):
        raised = epsilon2 * rho_down[nu] * epsilon2.T
        contraction = sum(rho_down[mu][a, b] * raised[a, b] for a in range(2) for b in range(2))
        assert_scalar(f"rho contraction {mu}{nu}", contraction, 2 * eta4[mu, nu])


def check_majorana_and_wess_bagger_translation() -> None:
    big_b = gamma[2]
    assert_matrix("Majorana B star B", big_b.conjugate() * big_b, I4)
    assert_matrix("Majorana B transpose", big_b.T, big_b)
    for mu in range(4):
        lhs = gamma[mu].conjugate()
        rhs = big_b * gamma[mu] * big_b.inv()
        assert_matrix(f"Majorana gamma conjugation {mu}", lhs, rhs)

    for mu, nu in itertools.product(range(4), repeat=2):
        spin = -II * (gamma[mu] * gamma[nu] - gamma[nu] * gamma[mu]) / 4
        rhs = -big_b * spin * big_b.inv()
        assert_matrix(f"Majorana spin conjugation {mu}{nu}", spin.conjugate(), rhs)

    u_ch = block(I2, Z2, Z2, II * I2)
    for mu in range(4):
        rhs = u_ch * gamma_wb[mu] * u_ch.inv()
        assert_matrix(f"Wess-Bagger phase translation {mu}", gamma[mu], rhs)


def check_low_dimensional_spinors() -> None:
    gamma3 = [II * sigma2, sigma1, sigma3]
    eta3 = sp.diag(-1, 1, 1)
    for mu, nu in itertools.product(range(3), repeat=2):
        anti = gamma3[mu] * gamma3[nu] + gamma3[nu] * gamma3[mu]
        assert_matrix(f"three-dimensional Clifford {mu}{nu}", anti, 2 * eta3[mu, nu] * I2)
    for mu in range(3):
        lowered = gamma3[mu] * epsilon2
        assert_matrix(f"three-dimensional lowered symmetry {mu}", lowered, lowered.T)

    gamma2 = [II * sigma2, sigma1]
    chirality2 = gamma2[0] * gamma2[1]
    assert_matrix("two-dimensional chirality", chirality2, sigma3)
    for nu, rho in itertools.product(range(2), repeat=2):
        lhs = sp.trace(gamma2[nu] * chirality2 * gamma2[rho])
        rhs = 2 * levi_civita((rho, nu))
        assert_scalar(f"two-dimensional chirality trace {nu}{rho}", lhs, rhs)

    chiral_component_gamma = [-II * sigma1, sigma2]
    u2 = sp.diag(-II, 1)
    assert_matrix(
        "2D chiral-component gamma0 basis change",
        u2 * gamma2[0] * u2.inv(),
        chiral_component_gamma[0],
    )
    assert_matrix(
        "2D chiral-component gamma1 basis change",
        u2 * gamma2[1] * u2.inv(),
        chiral_component_gamma[1],
    )
    assert_matrix(
        "2D chiral-component chirality basis change",
        u2 * chirality2 * u2.inv(),
        chiral_component_gamma[0] * chiral_component_gamma[1],
    )
    gamma_plus = chiral_component_gamma[1] + chiral_component_gamma[0]
    gamma_minus = chiral_component_gamma[1] - chiral_component_gamma[0]
    lowered_plus = gamma_plus * epsilon2
    lowered_minus = gamma_minus * epsilon2
    assert_matrix(
        "2D chiral-component lowered gamma plus",
        lowered_plus,
        sp.Matrix([[2 * II, 0], [0, 0]]),
    )
    assert_matrix(
        "2D chiral-component lowered gamma minus",
        lowered_minus,
        sp.Matrix([[0, 0], [0, 2 * II]]),
    )


def euclidean_gamma(dimension: int) -> list[sp.Matrix]:
    if dimension == 2:
        return [sigma1, sigma2]
    previous = euclidean_gamma(dimension - 2)
    size = previous[0].rows
    result = [sp.kronecker_product(matrix, -sigma3) for matrix in previous]
    result.append(sp.kronecker_product(sp.eye(size), sigma1))
    result.append(sp.kronecker_product(sp.eye(size), sigma2))
    return result


def check_euclidean_recursion() -> None:
    for dimension in (2, 4, 6):
        matrices = euclidean_gamma(dimension)
        identity = sp.eye(matrices[0].rows)
        zero = sp.zeros(matrices[0].rows)
        for i, j in itertools.product(range(dimension), repeat=2):
            anti = matrices[i] * matrices[j] + matrices[j] * matrices[i]
            rhs = 2 * identity if i == j else zero
            assert_matrix(f"Euclidean Clifford d={dimension} {i}{j}", anti, rhs)
        omega = identity
        for matrix in matrices:
            omega *= matrix
        chirality = II ** (-(dimension // 2)) * omega
        assert_matrix(f"Euclidean chirality square d={dimension}", chirality * chirality, identity)


def main() -> None:
    check_clifford_beta_and_slash_square()
    check_spin_generators_and_gamma5_trace()
    check_two_component_rho_blocks()
    check_majorana_and_wess_bagger_translation()
    check_low_dimensional_spinors()
    check_euclidean_recursion()
    print("All spinor-convention checks passed.")


if __name__ == "__main__":
    main()
