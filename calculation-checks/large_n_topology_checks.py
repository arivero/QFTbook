#!/usr/bin/env python3
"""Finite checks for the large-N color-topology section.

The checks are deliberately algebraic.  They verify the SU(N) completeness
relation in the monograph convention tr_fund(t^a t^b)=delta^{ab}, and the
Euler-characteristic powers used in the planar expansion.  They do not test
spacetime loop integrals or convergence of the perturbation series.
The genus-truncation check below verifies only the finite arithmetic of a
declared coefficient/remainder bound; it also includes a toy
order-of-limits negative control showing why fixed-graph topology is not a
continuum large-N theorem.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close


from fractions import Fraction

import numpy as np


def assert_equal(name: str, lhs: int | bool | Fraction, rhs: int | bool | Fraction) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs}, expected {rhs}")


def assert_close(name: str, lhs: complex, rhs: complex, tol: float = 1e-12) -> None:
    _assert_close(name, lhs, rhs, tol=tol)


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


def check_genus_truncation_remainder_bound() -> None:
    # After the overall leading N-power has been factored out, a controlled
    # genus expansion through H=2 requires a residual bounded by epsilon/N^6.
    n_colors = 5
    coefficients = [Fraction(3, 2), -Fraction(2, 3), Fraction(5, 7)]
    truncated = sum(
        coefficient / (n_colors ** (2 * genus))
        for genus, coefficient in enumerate(coefficients)
    )
    residual = Fraction(1, 13 * n_colors**6)
    epsilon_h = Fraction(1, 10)
    residual_bound = epsilon_h / (n_colors**6)
    exact = truncated + residual

    assert_equal("large-N genus truncation residual extraction", exact - truncated, residual)
    assert_equal(
        "large-N genus truncation residual bound",
        abs(exact - truncated) <= residual_bound,
        True,
    )

    underbudgeted_residual = Fraction(1, 2 * n_colors**6)
    assert_equal(
        "large-N genus truncation underbudgeted tail fails",
        underbudgeted_residual <= residual_bound,
        False,
    )

    # A fixed-regulator large-N limit and a volume/continuum limit cannot be
    # interchanged from color topology alone.  The rational toy observable
    # f(N,L)=N^2/(N^2+L) is close to one at fixed L=1 and close to zero along
    # L=N^4.  The check is not a QCD model; it is the finite arithmetic behind
    # the warning that uniformity in regulator variables is a separate datum.
    fixed_l_value = Fraction(n_colors * n_colors, n_colors * n_colors + 1)
    path_l_value = Fraction(n_colors * n_colors, n_colors * n_colors + n_colors**4)
    assert_equal("large-N fixed-volume sample is near planar value", fixed_l_value > Fraction(9, 10), True)
    assert_equal("large-N growing-volume sample is not near planar value", path_l_value < Fraction(1, 10), True)


def check_half_trace_coupling_conversion() -> None:
    # The same matrix connection can be expanded as A_delta^a t_delta^a or
    # A_ht^a T^a, with t_delta^a=sqrt(2) T^a.  Component curvatures therefore
    # satisfy F_ht^2=2 F_delta^2.  Matching the component action
    # (4g^2)^(-1) F_delta^2 to (4g_ht^2)^(-1) F_ht^2 gives g_ht^2=2g^2.
    g_sq = Fraction(1, 1)
    g_ht_sq = 2 * g_sq
    c_f_half_trace = Fraction(3, 4)  # SU(2), used only as a finite example.
    c_f_trace_delta = 2 * c_f_half_trace
    assert_equal(
        "invariant Coulomb/cusp product",
        g_sq * c_f_trace_delta,
        g_ht_sq * c_f_half_trace,
    )

    n_colors = Fraction(5, 1)
    lambda_delta = g_sq * n_colors
    lambda_half_trace = g_ht_sq * n_colors
    assert_equal("half-trace 't Hooft coupling", lambda_half_trace, 2 * lambda_delta)


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


def center_phase_exponents(word: list[tuple[int, int]], dimensions: int) -> tuple[int, ...]:
    """Return the exponent of each independent EK center phase.

    A reduced word ``[(mu, eps), ...]`` represents
    ``V_mu^eps ...`` with ``eps`` equal to ``+1`` or ``-1``.  Under
    ``V_mu -> z_mu V_mu`` its normalized trace is multiplied by
    ``prod_mu z_mu^{n_mu}``; this function computes the integer vector
    ``n_mu``.
    """

    charges = [0] * dimensions
    for mu, eps in word:
        if not 0 <= mu < dimensions:
            raise ValueError("direction outside lattice dimension")
        if eps not in (-1, 1):
            raise ValueError("orientation must be +/-1")
        charges[mu] += eps
    return tuple(charges)


def is_center_neutral(word: list[tuple[int, int]], dimensions: int, n_colors: int) -> bool:
    if n_colors < 2:
        raise ValueError("SU(N) center requires N >= 2")
    return all(charge % n_colors == 0 for charge in center_phase_exponents(word, dimensions))


def check_eguchi_kawai_center_selection() -> None:
    plaquette = [(0, 1), (1, 1), (0, -1), (1, -1)]
    open_corner = [(0, 1), (1, 1), (0, -1)]
    reduced_polyakov_word = [(2, 1)] * 5

    plaquette_charge = center_phase_exponents(plaquette, dimensions=3)
    open_corner_charge = center_phase_exponents(open_corner, dimensions=3)

    assert_equal("EK plaquette charge mu=0", plaquette_charge[0], 0)
    assert_equal("EK plaquette charge mu=1", plaquette_charge[1], 0)
    assert_equal("EK open word displacement mu=1", open_corner_charge[1], 1)

    assert_equal("EK plaquette neutral modulo SU(5) center", is_center_neutral(plaquette, 3, 5), True)
    assert_equal("EK open word charged modulo SU(5) center", is_center_neutral(open_corner, 3, 5), False)
    assert_equal(
        "EK length-N word neutral modulo SU(N) center",
        is_center_neutral(reduced_polyakov_word, 3, 5),
        True,
    )

    for n_colors in range(3, 9):
        charge = center_phase_exponents(open_corner, dimensions=3)[1]
        assert_equal(
            f"EK charged open corner has nontrivial SU({n_colors}) center phase",
            charge % n_colors != 0,
            True,
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
    check_genus_truncation_remainder_bound()
    check_half_trace_coupling_conversion()
    check_single_trace_and_quark_boundary_scaling()
    check_eguchi_kawai_center_selection()
    check_baryon_large_n_scaling()
    print("All large-N color-topology checks passed.")


if __name__ == "__main__":
    main()
