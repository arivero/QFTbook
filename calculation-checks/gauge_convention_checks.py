#!/usr/bin/env python3
"""Finite algebra checks for the monograph's Yang-Mills conventions.

The active convention is Hermitian generators with

    [t^a,t^b] = i f^c_ab t^c,        tr(t^a t^b) = delta^ab,

and a connection-normalized action

    S = (4 g^2)^{-1} int tr(F_{mu nu} F_{mu nu}).

The checks below are finite-dimensional matrix and combinatorial checks.  They
do not attempt to evaluate loop integrals.
"""

from __future__ import annotations

import itertools
import math
import numpy as np


def assert_close(name: str, lhs: np.ndarray | complex | float, rhs: np.ndarray | complex | float) -> None:
    if not np.allclose(lhs, rhs, atol=1e-11):
        raise AssertionError(f"{name} failed:\n{lhs}\n!=\n{rhs}")


def matrix_unit(n: int, i: int, j: int) -> np.ndarray:
    out = np.zeros((n, n), dtype=complex)
    out[i, j] = 1.0
    return out


def sun_generators_trace_delta(n: int) -> list[np.ndarray]:
    """Hermitian traceless SU(n) basis with tr(t_a t_b)=delta_ab."""

    gens: list[np.ndarray] = []
    for i in range(n):
        for j in range(i + 1, n):
            eij = matrix_unit(n, i, j)
            eji = matrix_unit(n, j, i)
            gens.append((eij + eji) / math.sqrt(2.0))
            gens.append((-1j * (eij - eji)) / math.sqrt(2.0))

    for k in range(1, n):
        diag = np.zeros((n, n), dtype=complex)
        for i in range(k):
            diag[i, i] = 1.0
        diag[k, k] = -float(k)
        gens.append(diag / math.sqrt(k * (k + 1.0)))

    return gens


def structure_constants(gens: list[np.ndarray]) -> np.ndarray:
    dim = len(gens)
    f = np.zeros((dim, dim, dim), dtype=float)
    for c, a, b in itertools.product(range(dim), repeat=3):
        val = -1j * np.trace(gens[c] @ (gens[a] @ gens[b] - gens[b] @ gens[a]))
        if abs(val.imag) > 1e-10:
            raise AssertionError(f"structure constant has imaginary residue {val}")
        f[c, a, b] = val.real
    return f


def check_su2_pauli_default_basis() -> None:
    sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gens = [sigma1 / math.sqrt(2.0), sigma2 / math.sqrt(2.0), sigma3 / math.sqrt(2.0)]
    gram = np.array([[np.trace(a @ b) for b in gens] for a in gens])
    assert_close("SU(2) trace-delta Pauli basis", gram, np.eye(3))

    f = structure_constants(gens)
    for c, a, b in itertools.product(range(3), repeat=3):
        expected = math.sqrt(2.0) * levi_civita3(c, a, b)
        assert_close(f"SU(2) f^{c}_{{{a}{b}}}", f[c, a, b], expected)

    half_gens = [sigma1 / 2.0, sigma2 / 2.0, sigma3 / 2.0]
    half_gram = np.array([[np.trace(a @ b) for b in half_gens] for a in half_gens])
    assert_close("SU(2) half-trace comparison basis", half_gram, 0.5 * np.eye(3))


def levi_civita3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) < 3:
        return 0
    inversions = 0
    vals = [a, b, c]
    for i in range(3):
        for j in range(i + 1, 3):
            inversions += vals[i] > vals[j]
    return -1 if inversions % 2 else 1


def check_sun_color_factors() -> None:
    for n in (2, 3, 4):
        gens = sun_generators_trace_delta(n)
        dim = n * n - 1
        assert len(gens) == dim
        gram = np.array([[np.trace(a @ b) for b in gens] for a in gens])
        assert_close(f"SU({n}) trace delta", gram, np.eye(dim))

        f = structure_constants(gens)
        ca = np.einsum("acd,bcd->ab", f, f)
        assert_close(f"SU({n}) adjoint Casimir in trace-delta convention", ca, 2.0 * n * np.eye(dim))

        cf_matrix = sum(t @ t for t in gens)
        assert_close(
            f"SU({n}) fundamental quadratic Casimir in trace-delta convention",
            cf_matrix,
            ((n * n - 1.0) / n) * np.eye(n),
        )


def check_coupling_coordinate_conversion() -> None:
    # If T^a is the common half-trace basis and t^a = sqrt(2) T^a, then a
    # matter vertex g_here t^a equals g_common T^a with g_common=sqrt(2)g_here.
    for n, nf in [(2, 0), (3, 5), (5, 2)]:
        common_b0 = (11.0 / 3.0) * n - (2.0 / 3.0) * nf
        here_b0 = (11.0 / 3.0) * (2.0 * n) - (4.0 / 3.0) * nf
        assert_close(f"SU({n}) beta-coordinate conversion", here_b0, 2.0 * common_b0)


def check_wilson_plaquette_factor() -> None:
    rng = np.random.default_rng(20260524)
    f = np.zeros((4, 4))
    for mu in range(4):
        for nu in range(mu + 1, 4):
            f[mu, nu] = rng.normal()
            f[nu, mu] = -f[mu, nu]

    plaquette_sum = sum(0.5 * f[mu, nu] ** 2 for mu in range(4) for nu in range(mu + 1, 4))
    ordered_contraction = 0.25 * sum(f[mu, nu] ** 2 for mu in range(4) for nu in range(4))
    assert_close("Wilson plaquette gives 1/(4g^2) full contraction", plaquette_sum, ordered_contraction)


def main() -> None:
    check_su2_pauli_default_basis()
    check_sun_color_factors()
    check_coupling_coordinate_conversion()
    check_wilson_plaquette_factor()
    print("All gauge-generator, color-factor, and Wilson-normalization checks passed.")


if __name__ == "__main__":
    main()
