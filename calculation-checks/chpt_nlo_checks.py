#!/usr/bin/env python3
"""Finite arithmetic checks for the NLO chiral perturbation theory section."""

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


def main() -> None:
    check_gasser_leutwyler_basis_count()
    check_weinberg_graph_power_counting_identity()
    check_nlo_truncation_inventory_and_remainder_budget()
    check_su2_pion_mass_scale_cancellation()
    check_su3_gamma_table_entries_used_by_sources()
    print("All NLO chiral-perturbation-theory checks passed.")


if __name__ == "__main__":
    main()
