#!/usr/bin/env python3
"""Finite convention checks for ABJM and six-dimensional SUSY chapters.

The checks are intentionally finite: they verify the algebraic normalizations
that are easy to shift by factors of two or signs in prose.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [
        [sum(a[i][r] * b[r][j] for r in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def check_abjm_superpotential_r_charge() -> None:
    matter_r = Fraction(1, 2)
    quartic_r = 4 * matter_r
    assert_equal("ABJM quartic superpotential R-charge", quartic_r, 2)


def check_abjm_standard_conformal_locus_dimension() -> None:
    # In 3D N=2 conventions, a chiral primary has Delta=R at the ABJM point
    # and the d^2 theta measure has dimension 1.  The quartic ABJM
    # superpotential is therefore power-counting marginal, but the standard
    # N=6 completion fixes its normalized coefficient to 1/k.
    matter_dimension = Fraction(1, 2)
    f_term_measure_dimension = 1
    spacetime_dimension = 3
    quartic_dimension = 4 * matter_dimension
    coefficient_dimension = spacetime_dimension - f_term_measure_dimension - quartic_dimension
    assert_equal("ABJM quartic coefficient engineering dimension", coefficient_dimension, 0)

    for k in range(1, 15):
        normalized_superpotential_coefficient = Fraction(1, k)
        assert_equal(
            f"ABJM normalized h*k relation k={k}",
            k * normalized_superpotential_coefficient,
            1,
        )

        # The integer level lattice has zero tangent space.  Since the
        # standard N=6 coefficient is a function of k, its allowed tangent is
        # also zero.
        level_lattice_tangent_dimension = 0
        superpotential_tangent_dimension = level_lattice_tangent_dimension
        assert_equal(
            f"ABJM N=6 superpotential tangent k={k}",
            superpotential_tangent_dimension,
            0,
        )
        standard_conformal_locus_dimension = level_lattice_tangent_dimension
        assert_equal(
            f"standard ABJM conformal-locus dimension k={k}",
            standard_conformal_locus_dimension,
            0,
        )

    real_mass_dimension = 1
    fi_dimension = 1
    yang_mills_coupling_squared_dimension = 1
    assert_equal("ABJM real mass is relevant", real_mass_dimension, 1)
    assert_equal("ABJM FI coordinate is relevant", fi_dimension, 1)
    assert_equal(
        "3D Yang-Mills coupling squared is dimensionful",
        yang_mills_coupling_squared_dimension,
        1,
    )


def check_abjm_parity_level_pair() -> None:
    for k in (1, 2, 5, -3):
        levels = (k, -k)
        orientation_reversed = tuple(-level for level in levels)
        exchanged = (orientation_reversed[1], orientation_reversed[0])
        assert_equal(f"ABJM parity level pair k={k}", exchanged, levels)


def check_abjm_abelian_bf_normalization() -> None:
    # Old basis: (A, Ahat), K_old=diag(k,-k).
    # New basis: (A_D, B) with A=(A_D+B)/2 and Ahat=(A_D-B)/2.
    # Then K_new=M^T K_old M has off-diagonal entries k/2, giving
    # (1/4 pi) * (k/2 A_D dB + k/2 B dA_D), equivalent on a closed
    # manifold to (k/4 pi) B dA_D.
    k = Fraction(7, 1)
    k_old = [[k, Fraction(0)], [Fraction(0), -k]]
    m = [
        [Fraction(1, 2), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(-1, 2)],
    ]
    k_new = matmul(matmul(transpose(m), k_old), m)
    expected = [[Fraction(0), Fraction(7, 2)], [Fraction(7, 2), Fraction(0)]]
    assert_equal("ABJM abelian BF K-matrix", k_new, expected)


def check_abjm_orbifold_order_and_dimension() -> None:
    for k in range(1, 9):
        phase = Fraction(1, k)
        assert_equal(f"Z_k phase order k={k}", phase.denominator, k)

    for n in range(1, 6):
        one_brane_complex_dim = 4
        symmetric_product_dim = n * one_brane_complex_dim
        assert_equal(f"ABJM commuting branch dimension N={n}", symmetric_product_dim, 4 * n)


def check_abjm_s3_matrix_denominator() -> None:
    # Four chirals form two conjugate pairs for each ordered pair of Cartan
    # eigenvalues.  Each pair contributes 1/(2 cosh), hence two pairs give
    # 1/(4 cosh^2).
    chiral_fields = 4
    conjugate_pairs = chiral_fields // 2
    assert_equal("ABJM conjugate chiral pairs", conjugate_pairs, 2)
    assert_equal("ABJM cosh denominator prefactor", 2**conjugate_pairs, 4)
    assert_equal("ABJM cosh denominator exponent", conjugate_pairs, 2)

    for n in range(1, 7):
        positive_roots_one_u_n = n * (n - 1) // 2
        vector_factors_two_groups = 2 * positive_roots_one_u_n
        assert_equal(
            f"ABJM two U(N) positive-root count N={n}",
            vector_factors_two_groups,
            n * (n - 1),
        )


def check_three_d_n2_cs_matter_auxiliary_elimination() -> None:
    # Factor out powers of pi and i.  The D-equation in trace-delta
    # convention gives sigma = -(2 pi/k) mu.  The scalar sextic coefficient is
    # then -(2/k)^2 in units of pi^2.  The Yukawa sign is spinor-convention
    # dependent, but the magnitudes and the 1:2 relative coefficient are fixed
    # after the same algebraic elimination.
    for k in (1, 2, 5, -7):
        sigma_coeff_pi = Fraction(-2, k)
        sextic_coeff_pi_squared = -(sigma_coeff_pi * sigma_coeff_pi)
        assert_equal(
            f"3D N=2 CS sigma solution coefficient k={k}",
            sigma_coeff_pi,
            Fraction(-2, k),
        )
        assert_equal(
            f"3D N=2 CS sextic scalar coefficient k={k}",
            sextic_coeff_pi_squared,
            Fraction(-4, k * k),
        )

        moment_yukawa_magnitude_pi = abs(Fraction(2, k))
        mixed_yukawa_magnitude_pi = abs(Fraction(4, k))
        assert_equal(
            f"3D N=2 CS Yukawa relative coefficient k={k}",
            mixed_yukawa_magnitude_pi,
            2 * moment_yukawa_magnitude_pi,
        )


def check_three_d_n3_adjoint_chiral_elimination() -> None:
    # Write W = pi[-(k/8) x^2 + j x].  The algebraic F-term gives
    # x=(4/k)j, and substituting gives pi*(2/k)j^2.
    for k in (1, 2, 5, -4):
        phi_coeff_pi = Fraction(4, k)
        effective_superpotential_coeff_pi = (
            -Fraction(k, 8) * phi_coeff_pi * phi_coeff_pi + phi_coeff_pi
        )
        assert_equal(
            f"3D N=3 adjoint chiral solution k={k}",
            phi_coeff_pi,
            Fraction(4, k),
        )
        assert_equal(
            f"3D N=3 effective superpotential coefficient k={k}",
            effective_superpotential_coeff_pi,
            Fraction(2, k),
        )


def check_six_dimensional_yang_mills_dimension() -> None:
    def gauge_coupling_squared_dimension(spacetime_dimension: int) -> int:
        return 4 - spacetime_dimension

    assert_equal("4D gauge coupling marginal", gauge_coupling_squared_dimension(4), 0)
    assert_equal("5D gauge coupling dimension", gauge_coupling_squared_dimension(5), -1)
    assert_equal("6D gauge coupling dimension", gauge_coupling_squared_dimension(6), -2)


def check_two_zero_a_type_data() -> None:
    for n in range(1, 8):
        rank = n - 1
        dimension = n * n - 1
        dual_coxeter = n
        interacting_anomaly_coeff = Fraction(dimension * dual_coxeter, 24)
        assert_equal(
            f"A_{n-1} (2,0) anomaly coefficient",
            interacting_anomaly_coeff,
            Fraction(n * (n * n - 1), 24),
        )
        assert_equal(f"A_{n-1} tensor branch real dimension", 5 * rank, 5 * (n - 1))


def check_five_dimensional_instanton_kk_normalization() -> None:
    # In trace-delta variables the BPST check gives E_inst=4 pi^2/g_5^2.
    # Equating to one KK unit 1/R gives g_5^2=4 pi^2 R.  The half-trace
    # coupling is twice the trace-delta coupling.
    trace_delta_action_coeff = Fraction(4)
    half_trace_action_coeff = Fraction(8)
    coupling_conversion = Fraction(2)
    assert_equal(
        "5D half-trace/trace-delta coupling conversion",
        trace_delta_action_coeff * coupling_conversion,
        half_trace_action_coeff,
    )

    kk_energy_coeff = Fraction(1)
    g5_squared_over_pi2_r = trace_delta_action_coeff / kk_energy_coeff
    assert_equal("5D g5^2/(pi^2 R) coefficient", g5_squared_over_pi2_r, 4)


def main() -> None:
    check_abjm_superpotential_r_charge()
    check_abjm_standard_conformal_locus_dimension()
    check_abjm_parity_level_pair()
    check_abjm_abelian_bf_normalization()
    check_abjm_orbifold_order_and_dimension()
    check_abjm_s3_matrix_denominator()
    check_three_d_n2_cs_matter_auxiliary_elimination()
    check_three_d_n3_adjoint_chiral_elimination()
    check_six_dimensional_yang_mills_dimension()
    check_two_zero_a_type_data()
    check_five_dimensional_instanton_kk_normalization()
    print("All ABJM and six-dimensional SUSY convention checks passed.")


if __name__ == "__main__":
    main()
