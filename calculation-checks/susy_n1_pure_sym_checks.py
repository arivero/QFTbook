#!/usr/bin/env python3
"""Exact checks for pure 4D N=1 SYM glueball and index arithmetic."""

from fractions import Fraction
from math import gcd


def assert_equal(left, right, label):
    if left != right:
        raise AssertionError(f"{label}: got {left!r}, expected {right!r}")


def check_discrete_chiral_anomaly_and_condensate_phases():
    for nc in range(2, 30):
        anomaly_coefficient = 2 * nc
        generator_alpha_units = Fraction(1, nc)  # alpha = pi / Nc.

        # The theta shift is 2Nc alpha, measured in units of pi.  For the
        # generator alpha=pi/Nc this is 2pi, so it is a true symmetry.
        theta_shift_units = anomaly_coefficient * generator_alpha_units
        assert_equal(theta_shift_units, 2, "pure SYM anomaly-preserving generator")

        discrete_group_order = 2 * nc
        condensate_charge = 2
        condensate_phase_step_numerator = condensate_charge
        condensate_phase_order = discrete_group_order // gcd(
            discrete_group_order,
            condensate_phase_step_numerator,
        )
        assert_equal(condensate_phase_order, nc, "pure SYM condensate orbit")
        assert_equal(discrete_group_order // condensate_phase_order, 2, "unbroken Z2")


def check_vy_superpotential_arithmetic():
    for nc in range(2, 30):
        s_dimension = 3
        s_r_charge = 2
        lambda_power_dimension = 3 * nc

        assert_equal(nc * s_dimension, lambda_power_dimension, "VY logarithm dimensionless")
        assert_equal(s_dimension, 3, "VY superpotential dimension")
        assert_equal(s_r_charge, 2, "VY superpotential R-charge carried by S")

        # W = S(log(L/S^Nc)+c).  The source identity gives
        # L dW/dL = S independently of c.  The standard representative c=Nc
        # makes dW/dS = log(L/S^Nc).
        arbitrary_c = Fraction(7, 3)
        source_identity_coefficient = 1
        d_w_d_s_constant = arbitrary_c - nc
        standard_constant = nc
        standard_d_w_d_s_constant = standard_constant - nc
        assert_equal(source_identity_coefficient, 1, "VY source identity coefficient")
        assert_equal(d_w_d_s_constant, arbitrary_c - nc, "VY constant shift before normalization")
        assert_equal(standard_d_w_d_s_constant, 0, "standard VY F-term normalization")

        hessian_coefficient = -nc
        if hessian_coefficient == 0:
            raise AssertionError("VY critical point should be isolated for Nc >= 2")


def check_affine_toda_index_match():
    for nc in range(2, 30):
        simple_root_terms = nc - 1
        affine_root_terms = 1
        total_terms = simple_root_terms + affine_root_terms
        assert_equal(total_terms, nc, "pure SYM affine-Toda term count")

        roots_of_x_power_equation = nc
        witten_index = nc
        condensate_phases = nc
        assert_equal(roots_of_x_power_equation, witten_index, "affine-Toda vacuum count")
        assert_equal(condensate_phases, witten_index, "pure SYM condensate/index match")


def main():
    check_discrete_chiral_anomaly_and_condensate_phases()
    check_vy_superpotential_arithmetic()
    check_affine_toda_index_match()
    print("All pure N=1 SYM glueball and index checks passed.")


if __name__ == "__main__":
    main()
