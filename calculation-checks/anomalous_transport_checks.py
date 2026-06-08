#!/usr/bin/env python3
"""Coefficient checks for the anomalous-transport chapter."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import math
from fractions import Fraction

import sympy as sp


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-12) -> None:
    _assert_close(name, got, expected, tol=tol)


def check_chiral_magnetic_coefficients() -> None:
    mu_v = 0.7
    mu5_occ = 0.23
    mu_r = mu_v + mu5_occ
    mu_l = mu_v - mu5_occ
    pi2 = math.pi * math.pi

    right = mu_r / (4.0 * pi2)
    left = -mu_l / (4.0 * pi2)
    vector = right + left
    axial = right - left

    assert_close("prepared-imbalance vector CME", vector, mu5_occ / (2.0 * pi2))
    assert_close("source-normalized axial CME", axial, mu_v / (2.0 * pi2))

    charge = 1.9
    physical_vector = charge * charge * vector
    assert_close("electromagnetic CME charge factor", physical_vector, charge * charge * mu5_occ / (2.0 * pi2))


def check_equilibrium_cs_variation() -> None:
    a0_5 = 0.41
    beta = 1.7
    pi2 = math.pi * math.pi
    w3_cs_coefficient = -beta * a0_5 / (4.0 * pi2)
    consistent_current_coefficient = (2.0 * w3_cs_coefficient) / beta
    assert_close("source CS variation gives consistent current", consistent_current_coefficient, -a0_5 / (2.0 * pi2))


def check_cme_current_representatives_and_protocols() -> None:
    # Work in units of B/(2 pi^2).  The exact arithmetic catches three
    # convention errors: dropping beta, identifying a source holonomy with an
    # occupation imbalance, and labeling a variational source current as
    # covariant without adding the Bardeen--Zumino polynomial.
    axial_source = Fraction(7, 5)
    occupation = Fraction(11, 13)
    beta = Fraction(5, 3)
    magnetic_field = Fraction(17, 19)

    w3_cs_coefficient = -beta * axial_source / 2
    source_consistent = (2 * w3_cs_coefficient / beta) * magnetic_field
    expected_source_consistent = -axial_source * magnetic_field
    if source_consistent != expected_source_consistent:
        raise AssertionError(
            f"source-only consistent CME current failed: {source_consistent} != {expected_source_consistent}"
        )

    raw_three_dimensional_variation = 2 * w3_cs_coefficient * magnetic_field
    if raw_three_dimensional_variation == source_consistent:
        raise AssertionError("thermal-circle beta factor did not affect the source-current normalization")

    bz_shift = axial_source * magnetic_field
    source_covariant = source_consistent + bz_shift
    if source_covariant != 0:
        raise AssertionError(f"source-only covariant CME current failed: {source_covariant} != 0")

    total_consistent = occupation * magnetic_field + source_consistent
    total_covariant = total_consistent + bz_shift
    expected_consistent = (occupation - axial_source) * magnetic_field
    expected_covariant = occupation * magnetic_field
    if total_consistent != expected_consistent:
        raise AssertionError(f"combined consistent CME ledger failed: {total_consistent} != {expected_consistent}")
    if total_covariant != expected_covariant:
        raise AssertionError(f"combined covariant CME ledger failed: {total_covariant} != {expected_covariant}")
    if source_consistent == source_covariant:
        raise AssertionError("variational source current was not separated from the covariant representative")


def check_kubo_sign_from_source_hamiltonian() -> None:
    def eps3(i: int, j: int, k: int) -> int:
        if len({i, j, k}) < 3:
            return 0
        inversions = 0
        values = [i, j, k]
        for left in range(3):
            for right in range(left + 1, 3):
                if values[left] > values[right]:
                    inversions += 1
        return -1 if inversions % 2 else 1

    wave_number = sp.Rational(5, 11)
    xi_b = sp.Rational(3, 7)
    direction = 2
    retarded = [
        [sp.I * xi_b * eps3(i, j, direction) * wave_number for j in range(3)]
        for i in range(3)
    ]
    response = [[-retarded[i][j] for j in range(3)] for i in range(3)]
    contracted_response = sum(eps3(i, j, direction) * response[i][j] for i in range(3) for j in range(3))
    xi_from_response = sp.I * contracted_response / (2 * wave_number)
    if sp.simplify(xi_from_response - xi_b) != 0:
        raise AssertionError("Kubo response-kernel sign failed")

    contracted_retarded = sum(eps3(i, j, direction) * retarded[i][j] for i in range(3) for j in range(3))
    xi_from_retarded = -sp.I * contracted_retarded / (2 * wave_number)
    if sp.simplify(xi_from_retarded - xi_b) != 0:
        raise AssertionError("Kubo retarded-kernel sign failed")
    wrong_plus_sign = sp.I * contracted_retarded / (2 * wave_number)
    if sp.simplify(wrong_plus_sign - xi_b) == 0:
        raise AssertionError("old plus-sign Kubo formula passed unexpectedly")


def check_hydrostatic_magnetization_curl_has_no_periodic_net_current() -> None:
    nx, ny = 4, 5
    magnetization = [
        [Fraction((x + 1) * (2 * y + 3), 17) for y in range(ny)]
        for x in range(nx)
    ]
    total_jx = Fraction(0, 1)
    total_jy = Fraction(0, 1)
    for x in range(nx):
        for y in range(ny):
            total_jx += magnetization[x][y] - magnetization[x][(y - 1) % ny]
            total_jy -= magnetization[x][y] - magnetization[(x - 1) % nx][y]
    if total_jx != 0 or total_jy != 0:
        raise AssertionError(f"periodic magnetization current had net flow: {(total_jx, total_jy)}")

    uniform_transport = Fraction(3, 5)
    net_transport = nx * ny * uniform_transport
    if net_transport == 0:
        raise AssertionError("uniform transport current was accidentally treated as a magnetization curl")


def check_general_hydrostatic_cs_variation() -> None:
    # For W = c_AA A dA + c_Aa A da + c_aa a da on a closed three-manifold,
    # the spatial source variations are
    # delta W / delta A_i = 2 c_AA B_A^i + c_Aa B_a^i,
    # delta W / delta a_i = c_Aa B_A^i + 2 c_aa B_a^i.
    c_aa_source = Fraction(5, 7)
    c_a_kaluza = Fraction(-3, 11)
    c_kk = Fraction(2, 13)
    b_source = Fraction(17, 19)
    b_kaluza = Fraction(-23, 29)

    current_source = 2 * c_aa_source * b_source + c_a_kaluza * b_kaluza
    current_kaluza = c_a_kaluza * b_source + 2 * c_kk * b_kaluza

    expected_source = Fraction(10, 7) * Fraction(17, 19) + Fraction(69, 319)
    expected_kaluza = Fraction(-51, 209) - Fraction(92, 377)

    if current_source != expected_source:
        raise AssertionError(f"hydrostatic source-current variation failed: {current_source} != {expected_source}")
    if current_kaluza != expected_kaluza:
        raise AssertionError(f"hydrostatic KK-current variation failed: {current_kaluza} != {expected_kaluza}")


def check_chiral_vortical_coefficients() -> None:
    mu_v = 0.61
    mu_a = 0.19
    temp = 0.37
    mu_r = mu_v + mu_a
    mu_l = mu_v - mu_a
    pi2 = math.pi * math.pi

    right = mu_r * mu_r / (4.0 * pi2) + temp * temp / 12.0
    left = -(mu_l * mu_l / (4.0 * pi2) + temp * temp / 12.0)
    vector = right + left
    axial = right - left

    assert_close("vector CVE", vector, mu_v * mu_a / pi2)
    assert_close("axial CVE", axial, (mu_v * mu_v + mu_a * mu_a) / (2.0 * pi2) + temp * temp / 6.0)

    vector_temperature_piece = temp * temp / 12.0 - temp * temp / 12.0
    assert_close("no vector T^2 term for Dirac pair", vector_temperature_piece, 0.0)


def check_entropy_force_sign_and_ideal_cancellation() -> None:
    beta0, beta1, beta2, beta3 = sp.symbols("beta0 beta1 beta2 beta3")
    j0, j1, j2, j3 = sp.symbols("j0 j1 j2 j3")
    da0, da1, da2, da3 = sp.symbols("da0 da1 da2 da3")
    beta = [beta0, beta1, beta2, beta3]
    current = [j0, j1, j2, j3]
    dalpha = [da0, da1, da2, da3]
    f01, f02, f03, f12, f13, f23 = sp.symbols("f01 f02 f03 f12 f13 f23")
    field = [
        [0, f01, f02, f03],
        [-f01, 0, f12, f13],
        [-f02, -f12, 0, f23],
        [-f03, -f13, -f23, 0],
    ]

    starting_source_terms = -sum(current[mu] * dalpha[mu] for mu in range(4)) - sum(
        current[mu] * beta[nu] * field[nu][mu]
        for mu in range(4)
        for nu in range(4)
    )
    force_form = -sum(
        current[mu] * (dalpha[mu] - sum(beta[nu] * field[mu][nu] for nu in range(4)))
        for mu in range(4)
    )
    if sp.simplify(starting_source_terms - force_form) != 0:
        raise AssertionError("entropy force sign algebra failed")

    temperature, entropy, density, chemical = sp.symbols("T s n mu", nonzero=True)
    d_temperature, d_chemical = sp.symbols("dT dmu")
    pressure_derivative = entropy * d_temperature + density * d_chemical
    energy_plus_pressure = temperature * entropy + chemical * density
    # Ideal part of div(p beta - beta.T_id - alpha J_id) after expanding
    # beta = u/T and alpha = mu/T along the fluid velocity.
    ideal_divergence = (
        pressure_derivative / temperature
        - energy_plus_pressure * d_temperature / temperature**2
        - density * d_chemical / temperature
        + density * chemical * d_temperature / temperature**2
    )
    if sp.simplify(ideal_divergence) != 0:
        raise AssertionError("ideal entropy cancellation failed")


def main() -> None:
    check_chiral_magnetic_coefficients()
    check_equilibrium_cs_variation()
    check_cme_current_representatives_and_protocols()
    check_kubo_sign_from_source_hamiltonian()
    check_hydrostatic_magnetization_curl_has_no_periodic_net_current()
    check_general_hydrostatic_cs_variation()
    check_chiral_vortical_coefficients()
    check_entropy_force_sign_and_ideal_cancellation()
    print("All anomalous-transport coefficient checks passed.")


if __name__ == "__main__":
    main()
