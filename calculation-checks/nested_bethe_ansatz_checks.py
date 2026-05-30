#!/usr/bin/env python3
"""Finite algebra checks for the nested Bethe-ansatz chapters."""

from __future__ import annotations

import cmath
import itertools
import math


ComplexMatrix = list[list[complex]]


def assert_close(name: str, value: complex, expected: complex = 0j, tol: float = 1e-9) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def basis_tuples(dim: int, sites: int) -> list[tuple[int, ...]]:
    return list(itertools.product(range(dim), repeat=sites))


def zero_matrix(size: int) -> ComplexMatrix:
    return [[0j for _ in range(size)] for _ in range(size)]


def identity_matrix(size: int) -> ComplexMatrix:
    matrix = zero_matrix(size)
    for i in range(size):
        matrix[i][i] = 1
    return matrix


def matmul(left: ComplexMatrix, right: ComplexMatrix) -> ComplexMatrix:
    size = len(left)
    out = zero_matrix(size)
    for i in range(size):
        for k in range(size):
            if left[i][k] == 0:
                continue
            lik = left[i][k]
            for j in range(size):
                if right[k][j] != 0:
                    out[i][j] += lik * right[k][j]
    return out


def max_abs_difference(left: ComplexMatrix, right: ComplexMatrix) -> float:
    return max(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left))
    )


def add_scaled(left: ComplexMatrix, right: ComplexMatrix, scale: complex = 1) -> ComplexMatrix:
    size = len(left)
    out = zero_matrix(size)
    for i in range(size):
        for j in range(size):
            out[i][j] = left[i][j] + scale * right[i][j]
    return out


def scale_matrix(scale: complex, matrix: ComplexMatrix) -> ComplexMatrix:
    size = len(matrix)
    out = zero_matrix(size)
    for i in range(size):
        for j in range(size):
            out[i][j] = scale * matrix[i][j]
    return out


def r_operator(dim: int, sites: int, site_a: int, site_b: int, spectral: complex) -> ComplexMatrix:
    """Return R_ab(u)=u*1+i*P_ab on (C^dim)^{otimes sites}."""

    basis = basis_tuples(dim, sites)
    index = {state: n for n, state in enumerate(basis)}
    matrix = zero_matrix(len(basis))
    for col, state in enumerate(basis):
        matrix[col][col] += spectral
        swapped = list(state)
        swapped[site_a], swapped[site_b] = swapped[site_b], swapped[site_a]
        row = index[tuple(swapped)]
        matrix[row][col] += 1j
    return matrix


def check_yang_baxter() -> None:
    for dim in (2, 3):
        u = 0.37 + 0.11j
        v = -0.29 + 0.07j
        r12 = r_operator(dim, 3, 0, 1, u)
        r13 = r_operator(dim, 3, 0, 2, u + v)
        r23 = r_operator(dim, 3, 1, 2, v)
        lhs = matmul(matmul(r12, r13), r23)
        rhs = matmul(matmul(r23, r13), r12)
        assert_close(f"YBE dim={dim}", max_abs_difference(lhs, rhs))


def transfer_matrix_xxx(length: int, spectral: complex) -> ComplexMatrix:
    dim = 2
    total_sites = length + 1
    full_size = dim ** total_sites
    monodromy = identity_matrix(full_size)
    for site in range(1, length + 1):
        local = r_operator(dim, total_sites, 0, site, spectral - 0.5j)
        monodromy = matmul(local, monodromy)

    quantum_basis = basis_tuples(dim, length)
    full_basis = basis_tuples(dim, total_sites)
    full_index = {state: n for n, state in enumerate(full_basis)}
    transfer = zero_matrix(dim ** length)
    for col_q, q_in in enumerate(quantum_basis):
        for row_q, q_out in enumerate(quantum_basis):
            total = 0j
            for aux in range(dim):
                row = full_index[(aux, *q_out)]
                col = full_index[(aux, *q_in)]
                total += monodromy[row][col]
            transfer[row_q][col_q] = total
    return transfer


def monodromy_entries_xxx(length: int, spectral: complex) -> tuple[ComplexMatrix, ComplexMatrix, ComplexMatrix, ComplexMatrix]:
    dim = 2
    total_sites = length + 1
    full_size = dim ** total_sites
    monodromy = identity_matrix(full_size)
    for site in range(1, length + 1):
        local = r_operator(dim, total_sites, 0, site, spectral - 0.5j)
        monodromy = matmul(local, monodromy)

    quantum_basis = basis_tuples(dim, length)
    full_basis = basis_tuples(dim, total_sites)
    full_index = {state: n for n, state in enumerate(full_basis)}

    def block(aux_out: int, aux_in: int) -> ComplexMatrix:
        out = zero_matrix(dim ** length)
        for col_q, q_in in enumerate(quantum_basis):
            for row_q, q_out in enumerate(quantum_basis):
                row = full_index[(aux_out, *q_out)]
                col = full_index[(aux_in, *q_in)]
                out[row_q][col_q] = monodromy[row][col]
        return out

    return block(0, 0), block(0, 1), block(1, 0), block(1, 1)


def check_transfer_commutativity() -> None:
    tu = transfer_matrix_xxx(3, 0.41 + 0.17j)
    tv = transfer_matrix_xxx(3, -0.23 + 0.31j)
    commutator = matmul(tu, tv)
    reverse = matmul(tv, tu)
    assert_close("XXX transfer commutator", max_abs_difference(commutator, reverse))


def check_ab_db_relations() -> None:
    length = 2
    u = 0.41 + 0.17j
    v = -0.23 + 0.31j
    a_u, b_u, _, d_u = monodromy_entries_xxx(length, u)
    a_v, b_v, _, d_v = monodromy_entries_xxx(length, v)

    # With R(u)=u*1+iP and L(u)=R(u-i/2), the convention in the monograph is
    # T=[[A,B],[C,D]].  The signs below fix the transfer eigenvalue
    # Lambda(u)=a(u) Q(u-i)/Q(u)+d(u) Q(u+i)/Q(u).
    ab_lhs = matmul(a_u, b_v)
    ab_rhs = add_scaled(
        scale_matrix((u - v - 1j) / (u - v), matmul(b_v, a_u)),
        scale_matrix(1j / (u - v), matmul(b_u, a_v)),
    )
    assert_close("ABA A-B relation", max_abs_difference(ab_lhs, ab_rhs))

    db_lhs = matmul(d_u, b_v)
    db_rhs = add_scaled(
        scale_matrix((u - v + 1j) / (u - v), matmul(b_v, d_u)),
        scale_matrix(-1j / (u - v), matmul(b_u, d_v)),
    )
    assert_close("ABA D-B relation", max_abs_difference(db_lhs, db_rhs))


def check_one_magnon_spectrum() -> None:
    for length in (4, 6, 8):
        for mode in range(1, length):
            momentum = 2 * math.pi * mode / length
            rapidity = 0.5 / math.tan(momentum / 2)
            bethe_energy = 1 / (rapidity * rapidity + 0.25)
            plane_energy = 4 * math.sin(momentum / 2) ** 2
            assert_close(f"one-magnon energy L={length} n={mode}", bethe_energy, plane_energy)

            vector = [cmath.exp(1j * momentum * x) for x in range(length)]
            acted = [
                2 * vector[x] - vector[(x - 1) % length] - vector[(x + 1) % length]
                for x in range(length)
            ]
            residual = max(abs(acted[x] - plane_energy * vector[x]) for x in range(length))
            assert_close(f"one-magnon eigenvector L={length} n={mode}", residual)


def check_su3_nested_solution() -> None:
    length = 6
    root = math.sqrt(3) / 2
    u_roots = [-root, root]
    v_root = 0.0

    for u in u_roots:
        lhs = ((u + 0.5j) / (u - 0.5j)) ** length
        same_level = 1 + 0j
        for other in u_roots:
            if other != u:
                same_level *= (u - other + 1j) / (u - other - 1j)
        auxiliary = (u - v_root - 0.5j) / (u - v_root + 0.5j)
        assert_close(f"SU(3) first-level equation u={u}", lhs, same_level * auxiliary)

    second = 1 + 0j
    for u in u_roots:
        second *= (v_root - u - 0.5j) / (v_root - u + 0.5j)
    assert_close("SU(3) second-level equation", second, 1)

    energy = sum(1 / (u * u + 0.25) for u in u_roots)
    assert_close("SU(3) displayed energy", energy, 2)


def check_tq_pole_cancellation() -> None:
    length = 4
    root = 1 / (2 * math.sqrt(3))
    roots = [-root, root]

    def q_polynomial(z: complex) -> complex:
        out = 1 + 0j
        for r in roots:
            out *= z - r
        return out

    for u in roots:
        numerator = (u + 0.5j) ** length * q_polynomial(u - 1j)
        numerator += (u - 0.5j) ** length * q_polynomial(u + 1j)
        assert_close(f"TQ pole cancellation u={u}", numerator)

    energy = sum(1 / (u * u + 0.25) for u in roots)
    assert_close("two-magnon L=4 energy", energy, 6)


def main() -> None:
    check_yang_baxter()
    check_transfer_commutativity()
    check_ab_db_relations()
    check_one_magnon_spectrum()
    check_su3_nested_solution()
    check_tq_pole_cancellation()
    print("All nested Bethe ansatz checks passed.")


if __name__ == "__main__":
    main()
