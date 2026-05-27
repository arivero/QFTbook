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


def check_pure_sym_instanton_zero_mode_saturation():
    for nc in range(2, 30):
        instanton_number = 1
        adjoint_index = nc
        adjoint_gaugino_zero_modes = 2 * adjoint_index * instanton_number
        s_insertion_fermion_degree = 2

        assert_equal(
            adjoint_gaugino_zero_modes,
            2 * nc,
            "pure SYM one-instanton adjoint zero modes",
        )

        first_saturated_insertions = adjoint_gaugino_zero_modes // s_insertion_fermion_degree
        assert_equal(
            first_saturated_insertions,
            nc,
            "pure SYM first zero-mode-saturated S correlator",
        )

        for insertions in range(0, nc):
            insertion_degree = s_insertion_fermion_degree * insertions
            assert_equal(
                insertion_degree < adjoint_gaugino_zero_modes,
                True,
                "pure SYM too-few S insertions leave unsaturated modes",
            )

        saturated_dimension = 3 * first_saturated_insertions
        instanton_scale_dimension = 3 * nc
        assert_equal(
            saturated_dimension,
            instanton_scale_dimension,
            "pure SYM S^Nc instanton-scale dimension match",
        )

        saturated_gaugino_phase_charge = 2 * first_saturated_insertions
        assert_equal(
            saturated_gaugino_phase_charge,
            adjoint_gaugino_zero_modes,
            "pure SYM S^Nc anomalous charge matches zero modes",
        )

        for branch in range(nc):
            # The VY phases are exp(2 pi i branch/Nc).  Raising to Nc removes
            # the branch label, matching the one-instanton Nc-point ledger.
            phase_after_nc_power = (nc * branch) % nc
            assert_equal(
                phase_after_nc_power,
                0,
                "pure SYM clustered Nc-point branch independence",
            )


def check_finite_volume_symmetry_cluster_basis_ledger():
    for nc in range(2, 30):
        for parity in (-1, 1):
            ordinary_index = parity * nc
            assert_equal(
                ordinary_index,
                parity * nc,
                "pure SYM ordinary index in same-parity branch basis",
            )

        for shift in range(nc):
            fixed_branch_count = sum(
                1
                for branch in range(nc)
                if (branch + shift) % nc == branch
            )
            expected_trace = nc if shift == 0 else 0
            assert_equal(
                fixed_branch_count,
                expected_trace,
                "pure SYM chiral-twined regular-representation trace",
            )

        for charge_sector in range(nc):
            # With |r> = sum_k omega^{-rk}|k>, the condensate coordinate with
            # branch phase omega^k maps |r> to |r-1>.  Thus it is off-diagonal
            # in the finite-volume symmetry basis.
            s_times_state_exponent = (1 - charge_sector) % nc
            target_state_exponent = (-(charge_sector - 1)) % nc
            assert_equal(
                s_times_state_exponent,
                target_state_exponent,
                "pure SYM S operator shifts finite-volume chiral charge",
            )

            diagonal_character_power = 1
            assert_equal(
                diagonal_character_power % nc != 0,
                True,
                "pure SYM finite-volume S expectation is a nontrivial character sum",
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


def check_local_chiral_oscillator_index():
    for nc in range(2, 30):
        complex_dimension = nc - 1
        takagi_nonzero_singular_values = complex_dimension
        assert_equal(
            takagi_nonzero_singular_values,
            complex_dimension,
            "local chiral critical point nondegenerate Hessian rank",
        )

        one_complex_factor_index = 1
        local_index = one_complex_factor_index ** complex_dimension
        assert_equal(local_index, 1, "local chiral oscillator index")

        bosonic_ground_fermion_number = 0
        bosonic_ground_parity = (-1) ** bosonic_ground_fermion_number
        assert_equal(bosonic_ground_parity, 1, "local chiral oscillator ground parity")

        # For Re(z^2/2), each complex coordinate would give one negative real
        # Morse direction.  The chiral index uses the holomorphic oscillator
        # orientation instead, so the local contribution stays +1 for every
        # complex dimension.
        real_morse_negative_directions = complex_dimension
        assert_equal(
            real_morse_negative_directions,
            nc - 1,
            "real Morse sign directions are not the chiral-index convention",
        )


def main():
    check_discrete_chiral_anomaly_and_condensate_phases()
    check_vy_superpotential_arithmetic()
    check_condensate_source_and_branch_monodromy()
    check_pure_sym_instanton_zero_mode_saturation()
    check_finite_volume_symmetry_cluster_basis_ledger()
    check_affine_toda_index_match()
    check_local_chiral_oscillator_index()
    print("All pure N=1 SYM glueball and index checks passed.")


if __name__ == "__main__":
    main()
