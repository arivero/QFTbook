#!/usr/bin/env python3
"""Checks for local-counterterm power counting and one-loop pole algebra."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def check_phi3_six_one_loop_poles():
    # Gamma(-1 + eps/2) has pole -2/eps.  The symmetry factor in the
    # displayed self-energy is 1/2, so the common pole multiplier is -1/eps.
    common = Fraction(-1, 1)
    feynman_parameter_mass = Fraction(1, 1)
    feynman_parameter_k2 = Fraction(1, 6)
    assert_equal(common * feynman_parameter_k2, Fraction(-1, 6), "phi3_6 k2 pole")
    assert_equal(common * feynman_parameter_mass, Fraction(-1, 1), "phi3_6 mass pole")


def check_power_counting_finite_list_logic():
    # For vertices with d_v <= D, the inequality
    # D - d_I - sum_v(D - d_v) >= 0 forces d_I <= D.
    examples = [
        {"D": 4, "vertices": [4, 4], "max_counterterm_dimension": 4},
        {"D": 6, "vertices": [6, 6, 6], "max_counterterm_dimension": 6},
        {"D": 4, "vertices": [2, 4, 4], "max_counterterm_dimension": 2},
    ]
    for item in examples:
        d = item["D"]
        allowed = d - sum(d - dv for dv in item["vertices"])
        assert_equal(allowed, item["max_counterterm_dimension"], f"allowed d_I in {item}")
        if all(dv <= d for dv in item["vertices"]):
            assert allowed <= d


def check_irrelevant_repeated_insertions_can_proliferate():
    # In D=4, a phi^6 vertex has engineering dimension 6.  Repeated insertions
    # raise the allowed counterterm dimension: D - d_I - V(D - 6) >= 0 gives
    # d_I <= 4 + 2V.
    d = 4
    vertex_dimension = 6
    for vertex_count, expected_bound in [(1, 6), (2, 8), (3, 10)]:
        allowed = d - vertex_count * (d - vertex_dimension)
        assert_equal(allowed, expected_bound, f"phi6 insertion bound V={vertex_count}")


def check_supported_distribution_scaling_degrees():
    # In R^n, partial^alpha delta has scaling degree n + |alpha|.  The
    # extension ambiguity for scaling degree s is |alpha| <= floor(s) - n.
    n = 4
    floor_s = 6
    ambiguity_order = floor_s - n
    assert_equal(ambiguity_order, 2, "ambiguity order")
    for alpha_abs in range(ambiguity_order + 1):
        assert (n + alpha_abs) <= floor_s
    assert (n + ambiguity_order + 1) > floor_s


def main():
    check_phi3_six_one_loop_poles()
    check_power_counting_finite_list_logic()
    check_irrelevant_repeated_insertions_can_proliferate()
    check_supported_distribution_scaling_degrees()
    print("All renormalizability-counterterm checks passed.")


if __name__ == "__main__":
    main()
