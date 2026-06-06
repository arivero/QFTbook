#!/usr/bin/env python3
r"""Finite arithmetic checks for the NLO chiral perturbation theory section.

Evidence contract.
Target claims: the finite coefficient and projection subclaims in
`sec:chiral-perturbation-theory-nlo`, including Weinberg graph power counting,
the NLO graph inventory, pion-mass scale cancellation, and the threshold
projection from the chiral amplitude to the physical \(\pi\pi\) scattering
length coordinates.
Independent construction: exact finite topology counts, rational RG
coefficient arithmetic, and direct isospin plus partial-wave projection of the
threshold amplitude, rather than substituting the final scattering-length
formulas.
Imported assumptions: the chapter's \(SU(2)\) stereographic normalization
`F_st=2 f_pi`, the partial-wave normalization inherited from the QCD Roy
section, and the displayed local \(C_4,C'_4\) representative for the
two-flavor \(O(p^4)\) amplitude.
Negative controls: the check rejects using the chiral-limit amplitude
`A=s/f_pi^2` at physical threshold, and it rejects silently absorbing loop or
remainder terms into fitted \(O(p^4)\) constants.
Scope boundary: these checks do not prove convergence of ChPT, determine the
physical low-energy constants from QCD, compute the full one-loop massive
\(\pi\pi\) amplitude, or replace Roy/lattice/experimental input for physical
scattering lengths.
"""

from __future__ import annotations

from fractions import Fraction


def assert_eq(name: str, value: object, expected: object) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def check_gasser_leutwyler_basis_count() -> None:
    labels = tuple(range(1, 11))
    assert_eq("Gasser-Leutwyler L_i count", len(labels), 10)
    assert_eq("first L_i label", labels[0], 1)
    assert_eq("last L_i label", labels[-1], 10)


def connected_loop_count(internal_lines: int, vertex_count: int) -> int:
    return internal_lines - vertex_count + 1


def graph_order_from_topology(internal_lines: int, vertex_orders: list[int]) -> int:
    loops = connected_loop_count(internal_lines, len(vertex_orders))
    return 4 * loops - 2 * internal_lines + sum(vertex_orders)


def weinberg_graph_order(loop_count: int, vertex_orders: list[int]) -> int:
    return 2 + 2 * loop_count + sum(order - 2 for order in vertex_orders)


def check_weinberg_graph_power_counting_identity() -> None:
    samples = [
        (0, [2], "tree L2 vertex"),
        (2, [2, 2], "one-loop L2 graph"),
        (0, [4], "tree L4 vertex"),
        (2, [4, 2], "one-loop L4-L2 graph"),
        (3, [2, 2], "two-loop L2 graph"),
        (0, [6], "tree L6 vertex"),
    ]
    expected_orders = {
        "tree L2 vertex": 2,
        "one-loop L2 graph": 4,
        "tree L4 vertex": 4,
        "one-loop L4-L2 graph": 6,
        "two-loop L2 graph": 6,
        "tree L6 vertex": 6,
    }
    for internal_lines, vertex_orders, name in samples:
        loops = connected_loop_count(internal_lines, len(vertex_orders))
        assert_eq(f"{name} loop count", loops, internal_lines - len(vertex_orders) + 1)
        topological_order = graph_order_from_topology(internal_lines, vertex_orders)
        weinberg_order = weinberg_graph_order(loops, vertex_orders)
        assert_eq(f"{name} Weinberg identity", topological_order, weinberg_order)
        assert_eq(f"{name} chiral order", weinberg_order, expected_orders[name])


def check_nlo_truncation_inventory_and_remainder_budget() -> None:
    graph_classes = {
        "tree_L2": (0, [2]),
        "one_loop_L2": (2, [2, 2]),
        "tree_L4": (0, [4]),
        "one_loop_L4_L2": (2, [4, 2]),
        "two_loop_L2": (3, [2, 2]),
        "tree_L6": (0, [6]),
    }
    retained = []
    omitted_first = []
    for label, (internal_lines, vertex_orders) in graph_classes.items():
        loops = connected_loop_count(internal_lines, len(vertex_orders))
        order = weinberg_graph_order(loops, vertex_orders)
        if order <= 4:
            retained.append(label)
        elif order == 6:
            omitted_first.append(label)
    assert_eq("NLO retained class count", len(retained), 3)
    assert_eq("NLO retained classes", tuple(retained), ("tree_L2", "one_loop_L2", "tree_L4"))
    assert_eq(
        "first omitted O(p^6) classes",
        tuple(omitted_first),
        ("one_loop_L4_L2", "two_loop_L2", "tree_L6"),
    )

    epsilon = Fraction(1, 5)
    c2, c4, c6 = Fraction(3), Fraction(7), Fraction(11)
    retained_bound = c2 * epsilon**2 + c4 * epsilon**4
    first_omitted_bound = c6 * epsilon**6
    assert_eq("NLO retained sample bound", retained_bound, Fraction(82, 625))
    assert_eq("first omitted sample bound", first_omitted_bound, Fraction(11, 15625))
    if not first_omitted_bound < retained_bound:
        raise AssertionError("O(p^6) remainder was not parametrically smaller on epsilon=1/5 window")


def check_su2_pion_mass_scale_cancellation() -> None:
    """Check d/d log(mu) of the NLO M_pi^2 bracket vanishes.

    The bracket is

        1 + M^2/(32 pi^2 f^2) log(M^2/mu^2)
          + 2 l_3^r(mu) M^2/f^2,

    with mu d l_3^r / d mu = 1/(32 pi^2).  We strip the common factor
    M^2/(pi^2 f^2).
    """

    log_derivative = Fraction(-2, 32)
    local_derivative = 2 * Fraction(1, 32)
    assert_eq("SU(2) pion mass NLO scale cancellation", log_derivative + local_derivative, 0)


def check_su3_gamma_table_entries_used_by_sources() -> None:
    gamma = {
        1: Fraction(3, 32),
        2: Fraction(3, 16),
        3: Fraction(0, 1),
        4: Fraction(1, 8),
        5: Fraction(3, 8),
        6: Fraction(11, 144),
        7: Fraction(0, 1),
        8: Fraction(5, 48),
        9: Fraction(1, 4),
        10: Fraction(-1, 4),
    }
    assert_eq("ten Gamma_i entries", len(gamma), 10)
    assert_eq("Gamma_3 vanishes", gamma[3], 0)
    assert_eq("Gamma_7 vanishes", gamma[7], 0)
    assert_eq("Gamma_9 plus Gamma_10", gamma[9] + gamma[10], 0)


def check_threshold_pion_scattering_projection() -> None:
    """Project the leading threshold amplitude and local O(p^4) terms.

    The chapter uses the stereographic normalization F_st=2 f_pi.  After
    stripping the common factor 1/pi, the S-wave projection is T^I/32.
    """

    m2 = Fraction(1)
    f_st_sq = Fraction(1)

    def a2_massive(s: Fraction, _t: Fraction, _u: Fraction) -> Fraction:
        return 4 * (s - m2) / f_st_sq

    def a2_chiral_limit(s: Fraction, _t: Fraction, _u: Fraction) -> Fraction:
        return 4 * s / f_st_sq

    def isospin_threshold(amplitude) -> tuple[Fraction, Fraction, Fraction]:
        s = 4 * m2
        t = Fraction(0)
        u = Fraction(0)
        a_stu = amplitude(s, t, u)
        a_tsu = amplitude(t, s, u)
        a_uts = amplitude(u, t, s)
        t0 = 3 * a_stu + a_tsu + a_uts
        t1 = a_tsu - a_uts
        t2 = a_tsu + a_uts
        return t0, t1, t2

    t0, t1, t2 = isospin_threshold(a2_massive)
    assert_eq("threshold I=0 leading pion amplitude", t0, Fraction(28))
    assert_eq("threshold I=1 leading pion amplitude", t1, Fraction(0))
    assert_eq("threshold I=2 leading pion amplitude", t2, Fraction(-8))

    # These are pi * F_st^2 * a_0^I / m_pi^2.
    assert_eq("Weinberg a00 in F_st convention", t0 / 32, Fraction(7, 8))
    assert_eq("Weinberg a02 in F_st convention", t2 / 32, Fraction(-1, 4))

    wrong_t0, _wrong_t1, wrong_t2 = isospin_threshold(a2_chiral_limit)
    if wrong_t0 / 32 == Fraction(7, 8) or wrong_t2 / 32 == Fraction(-1, 4):
        raise AssertionError("chiral-limit amplitude was accepted at physical threshold")

    # Local O(p^4) representative from the displayed C4,C4' terms:
    # A_4^loc=-(C4 s^2 + C4'(t^2+u^2))/(2 F_st^4).  Work with the
    # stripped coordinates pi F_st^4 a_0^I/m_pi^4.
    c4 = Fraction(5, 7)
    cp = Fraction(-3, 11)

    def a4_local(s: Fraction, t: Fraction, u: Fraction) -> Fraction:
        return -Fraction(1, 2) * c4 * s * s - Fraction(1, 2) * cp * (t * t + u * u)

    local_t0, _local_t1, local_t2 = isospin_threshold(a4_local)
    projected_00 = local_t0 / 32
    projected_02 = local_t2 / 32
    expected_00 = -Fraction(3, 4) * c4 - Fraction(1, 2) * cp
    expected_02 = -Fraction(1, 2) * cp
    assert_eq("local O(p^4) threshold a00 projection", projected_00, expected_00)
    assert_eq("local O(p^4) threshold a02 projection", projected_02, expected_02)

    # The two threshold coordinates determine the two local representatives only
    # after loop, mass-spurion, and O(p^6) residual terms have been subtracted.
    matrix = (
        (Fraction(-3, 4), Fraction(-1, 2)),
        (Fraction(0), Fraction(-1, 2)),
    )
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    assert_eq("threshold local-fit determinant", det, Fraction(3, 8))
    inverse = (
        (matrix[1][1] / det, -matrix[0][1] / det),
        (-matrix[1][0] / det, matrix[0][0] / det),
    )
    assert_eq("threshold local-fit inverse 00", inverse[0][0], Fraction(-4, 3))
    assert_eq("threshold local-fit inverse 01", inverse[0][1], Fraction(4, 3))
    assert_eq("threshold local-fit inverse 11", inverse[1][1], Fraction(-2))

    residual = (Fraction(1, 17) + Fraction(1, 23), -Fraction(1, 19) + Fraction(1, 29))
    shifted_c4 = inverse[0][0] * residual[0] + inverse[0][1] * residual[1]
    shifted_cp = inverse[1][0] * residual[0] + inverse[1][1] * residual[1]
    if shifted_c4 == 0 or shifted_cp == 0:
        raise AssertionError("unsubtracted loop/remainder terms did not move fitted LECs")
    bound_c4 = Fraction(4, 3) * (abs(residual[0]) + abs(residual[1]))
    bound_cp = 2 * abs(residual[1])
    if not abs(shifted_c4) <= bound_c4:
        raise AssertionError("C4 residual propagation bound failed")
    if not abs(shifted_cp) <= bound_cp:
        raise AssertionError("C4' residual propagation bound failed")


def main() -> None:
    check_gasser_leutwyler_basis_count()
    check_weinberg_graph_power_counting_identity()
    check_nlo_truncation_inventory_and_remainder_budget()
    check_su2_pion_mass_scale_cancellation()
    check_su3_gamma_table_entries_used_by_sources()
    check_threshold_pion_scattering_projection()
    print("All NLO chiral-perturbation-theory checks passed.")


if __name__ == "__main__":
    main()
