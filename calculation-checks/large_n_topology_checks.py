#!/usr/bin/env python3
"""Finite checks for the large-N color-topology section.

The checks are deliberately algebraic.  They verify the SU(N) completeness
relation in the monograph convention tr_fund(t^a t^b)=delta^{ab}, and the
Euler-characteristic powers used in the planar expansion.  They do not test
spacetime loop integrals or convergence of the perturbation series.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np


def assert_equal(name: str, lhs: int | Fraction, rhs: int | Fraction) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs}, expected {rhs}")


def assert_close(name: str, lhs: complex, rhs: complex, tol: float = 1e-12) -> None:
    if abs(lhs - rhs) > tol:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def su_n_trace_delta_basis(n: int) -> list[np.ndarray]:
    """Hermitian traceless basis with tr(t_a t_b)=delta_ab."""

    basis: list[np.ndarray] = []

    for i in range(n):
        for j in range(i + 1, n):
            symmetric = np.zeros((n, n), dtype=complex)
            symmetric[i, j] = 1 / np.sqrt(2)
            symmetric[j, i] = 1 / np.sqrt(2)
            basis.append(symmetric)

            antisymmetric = np.zeros((n, n), dtype=complex)
            antisymmetric[i, j] = -1j / np.sqrt(2)
            antisymmetric[j, i] = 1j / np.sqrt(2)
            basis.append(antisymmetric)

    for k in range(1, n):
        diagonal = np.zeros((n, n), dtype=complex)
        diagonal[:k, :k] += np.eye(k) / np.sqrt(k * (k + 1))
        diagonal[k, k] = -k / np.sqrt(k * (k + 1))
        basis.append(diagonal)

    if len(basis) != n * n - 1:
        raise AssertionError(f"basis size for SU({n}) is {len(basis)}")
    return basis


def check_trace_normalization(n: int) -> None:
    basis = su_n_trace_delta_basis(n)
    for a, ta in enumerate(basis):
        for b, tb in enumerate(basis):
            expected = 1.0 if a == b else 0.0
            value = np.trace(ta @ tb)
            assert_close(f"SU({n}) trace normalization a={a} b={b}", value, expected)


def check_su_completeness(n: int) -> None:
    basis = su_n_trace_delta_basis(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for ell in range(n):
                    lhs = sum(ta[i, j] * ta[k, ell] for ta in basis)
                    rhs = (1 if i == ell and k == j else 0) - Fraction(
                        (1 if i == j else 0) * (1 if k == ell else 0), n
                    )
                    assert_close(
                        f"SU({n}) completeness i={i} j={j} k={k} ell={ell}",
                        lhs,
                        complex(rhs),
                    )


def euler_power(vertices: int, edges: int, faces: int) -> int:
    return vertices - edges + faces


def surface_power(genus: int, boundaries: int) -> int:
    return 2 - 2 * genus - boundaries


def check_theta_graph_suppression() -> None:
    vertices = 2
    edges = 3
    planar_faces = 3
    one_handle_faces = 1
    planar_power = euler_power(vertices, edges, planar_faces)
    handle_power = euler_power(vertices, edges, one_handle_faces)

    assert_equal("planar theta graph is sphere", planar_power, surface_power(0, 0))
    assert_equal("one-handle theta graph is torus", handle_power, surface_power(1, 0))
    assert_equal("one-handle suppression", handle_power - planar_power, -2)


def check_single_trace_and_quark_boundary_scaling() -> None:
    for genus in range(4):
        for insertions in range(1, 6):
            unnormalized = surface_power(genus, insertions)
            normalized_by_one_over_n = unnormalized - insertions
            assert_equal(
                f"normalized single-trace power h={genus} m={insertions}",
                normalized_by_one_over_n,
                2 - 2 * genus - 2 * insertions,
            )

    vacuum_planar = surface_power(0, 0)
    one_quark_loop_fixed_nf = surface_power(0, 1)
    two_quark_loops_fixed_nf = surface_power(0, 2)
    assert_equal("one fixed-Nf quark loop suppression", one_quark_loop_fixed_nf - vacuum_planar, -1)
    assert_equal("two fixed-Nf quark loop suppression", two_quark_loops_fixed_nf - vacuum_planar, -2)

    for quark_boundaries in range(5):
        veneziano_power = surface_power(0, quark_boundaries) + quark_boundaries
        assert_equal(
            f"Veneziano quark-boundary restoration b={quark_boundaries}",
            veneziano_power,
            vacuum_planar,
        )


def check_baryon_large_n_scaling() -> None:
    # In the Hartree estimate, N quarks give N one-body terms while
    # N(N-1)/2 pairs interact through g^2 = lambda/N.  We check the exact
    # coefficient multiplying lambda after division by N.
    for n_colors in range(2, 15):
        pair_coefficient = Fraction(n_colors * (n_colors - 1), 2 * n_colors)
        assert_equal(
            f"baryon pair coefficient N={n_colors}",
            pair_coefficient,
            Fraction(n_colors - 1, 2),
        )

        pair_per_color = pair_coefficient / n_colors
        assert_equal(
            f"baryon pair term per color N={n_colors}",
            pair_per_color,
            Fraction(n_colors - 1, 2 * n_colors),
        )

    # A collective rotor with I_rot proportional to N gives fixed-spin
    # splittings proportional to 1/N.  The ratio between N and 2N is exactly 2
    # at fixed J when I_rot doubles.
    spin_factor = Fraction(3, 1) * Fraction(4, 1) / 2
    for n_colors in range(2, 10):
        splitting_n = spin_factor / n_colors
        splitting_2n = spin_factor / (2 * n_colors)
        assert_equal(
            f"baryon rotor fixed-spin 1/N scaling N={n_colors}",
            splitting_n / splitting_2n,
            Fraction(2, 1),
        )


def main() -> None:
    for n in range(2, 7):
        check_trace_normalization(n)
        check_su_completeness(n)
    check_theta_graph_suppression()
    check_single_trace_and_quark_boundary_scaling()
    check_baryon_large_n_scaling()
    print("All large-N color-topology checks passed.")


if __name__ == "__main__":
    main()
