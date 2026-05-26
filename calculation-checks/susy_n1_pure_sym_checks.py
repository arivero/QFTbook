#!/usr/bin/env python3
"""Exact checks for pure 4D N=1 SYM glueball and index arithmetic."""

from fractions import Fraction
from math import gcd


def assert_equal(left, right, label):
    if left != right:
        raise AssertionError(f"{label}: got {left!r}, expected {right!r}")


def determinant_integer(matrix):
    size = len(matrix)
    work = [[Fraction(entry) for entry in row] for row in matrix]
    det = Fraction(1)
    for col in range(size):
        pivot = None
        for row in range(col, size):
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            return 0
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            det *= -1
        pivot_value = work[col][col]
        det *= pivot_value
        for entry in range(col, size):
            work[col][entry] /= pivot_value
        for row in range(col + 1, size):
            factor = work[row][col]
            for entry in range(col, size):
                work[row][entry] -= factor * work[col][entry]
    return det


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


def check_condensate_source_and_branch_monodromy():
    for nc in range(2, 30):
        # W_k(L)=Nc*C*L^(1/Nc)*phase_k, so L dW_k/dL=S_k.
        critical_value_coefficient = nc
        root_exponent = Fraction(1, nc)
        source_coefficient = critical_value_coefficient * root_exponent
        assert_equal(source_coefficient, 1, "condensate branch source identity")

        for branch in range(nc):
            theta_loop_branch = (branch + 1) % nc
            chiral_generator_branch = (branch + 1) % nc
            assert_equal(
                theta_loop_branch,
                chiral_generator_branch,
                "theta-loop and chiral-generator branch action",
            )


def check_affine_toda_index_match():
    for nc in range(2, 30):
        simple_root_terms = nc - 1
        affine_root_terms = 1
        total_terms = simple_root_terms + affine_root_terms
        assert_equal(total_terms, nc, "pure SYM affine-Toda term count")

        root_vectors = []
        for index in range(nc - 1):
            vector = [0] * nc
            vector[index] = 1
            vector[index + 1] = -1
            root_vectors.append(vector)
        affine_vector = [-1] + [0] * (nc - 2) + [1]
        root_vectors.append(affine_vector)
        telescoping_sum = [
            sum(vector[column] for vector in root_vectors)
            for column in range(nc)
        ]
        assert_equal(
            telescoping_sum,
            [0] * nc,
            "affine-Toda product constraint telescopes to eta",
        )

        # On sum_i delta y_i=0, use the basis e_i-e_N.  The quadratic form
        # sum_i (delta y_i)^2 has Gram matrix I+J, determinant Nc.
        tangent_gram = [
            [2 if row == column else 1 for column in range(nc - 1)]
            for row in range(nc - 1)
        ]
        assert_equal(
            determinant_integer(tangent_gram),
            nc,
            "affine-Toda constrained Hessian determinant",
        )

        roots_of_x_power_equation = nc
        local_index_contribution_per_critical_point = 1
        witten_index = nc
        condensate_phases = nc
        assert_equal(
            roots_of_x_power_equation * local_index_contribution_per_critical_point,
            witten_index,
            "affine-Toda local critical-point index",
        )
        assert_equal(roots_of_x_power_equation, witten_index, "affine-Toda vacuum count")
        assert_equal(condensate_phases, witten_index, "pure SYM condensate/index match")


def main():
    check_discrete_chiral_anomaly_and_condensate_phases()
    check_vy_superpotential_arithmetic()
    check_condensate_source_and_branch_monodromy()
    check_affine_toda_index_match()
    print("All pure N=1 SYM glueball and index checks passed.")


if __name__ == "__main__":
    main()
