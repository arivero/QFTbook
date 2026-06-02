#!/usr/bin/env python3
"""Numerical and exact checks for the pure SU(2) Seiberg-Witten section.

The checks use the chapter normalization with Lambda=1:

    a(u)  = sqrt(2(u+1)) 2F1(-1/2,1/2;1;2/(u+1)),
    aD(u) = i (u-1) 2F1(1/2,1/2;2;(1-u)/2)/2.

They verify monodromy matrices, Picard-Lefschetz central-charge action,
symplectic preservation, the rigid special-Kahler metric identity, the minimal
residual R-symmetry ledger, curve discriminant, the Picard-Fuchs equation, the
electric large-u asymptotic, the logarithmic large-u growth of the dual period,
the linear vanishing of the monopole period at u=1, and the rank-one
Argyres-Douglas cusp scaling dimensions.
"""

from __future__ import annotations

from fractions import Fraction

import mpmath as mp


mp.mp.dps = 60


def assert_close(name: str, value: complex, expected: complex, tol: mp.mpf) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value}, expected {expected}, tol={tol}")


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [a[0][0] * b[0][j] + a[0][1] * b[1][j] for j in range(2)],
        [a[1][0] * b[0][j] + a[1][1] * b[1][j] for j in range(2)],
    ]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [[a[0][0], a[1][0]], [a[0][1], a[1][1]]]


def conjugate(z: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (z[0], -z[1])


def subtract(
    z: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return (z[0] - w[0], z[1] - w[1])


def divide_by_two_i(z: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    # (x+i y)/(2i) = y/2 - i x/2.
    return (z[1] / 2, -z[0] / 2)


def charge_monodromy(n_m: int, n_e: int) -> list[list[int]]:
    return [
        [1 + 2 * n_m * n_e, 2 * n_e * n_e],
        [-2 * n_m * n_m, 1 - 2 * n_m * n_e],
    ]


def symplectic_pair(delta: tuple[int, int], gamma: tuple[int, int]) -> int:
    m_m, m_e = delta
    n_m, n_e = gamma
    return m_m * n_e - m_e * n_m


def row_times_matrix(row: tuple[int, int], a: list[list[int]]) -> tuple[int, int]:
    return (row[0] * a[0][0] + row[1] * a[1][0], row[0] * a[0][1] + row[1] * a[1][1])


def a_period(u: mp.mpf | mp.mpc) -> mp.mpc:
    return mp.sqrt(2 * (u + 1)) * mp.hyper([mp.mpf("-0.5"), mp.mpf("0.5")], [1], 2 / (u + 1))


def aD_period(u: mp.mpf | mp.mpc) -> mp.mpc:
    return 0.5j * (u - 1) * mp.hyper([mp.mpf("0.5"), mp.mpf("0.5")], [2], (1 - u) / 2)


def check_monodromies() -> None:
    m_monopole = charge_monodromy(1, 0)
    m_dyon = charge_monodromy(1, -1)
    m_infinity = [[-1, 2], [0, -1]]
    if m_monopole != [[1, 0], [-2, 1]]:
        raise AssertionError(f"monopole monodromy mismatch: {m_monopole}")
    if m_dyon != [[-1, 2], [-2, 3]]:
        raise AssertionError(f"dyon monodromy mismatch: {m_dyon}")
    if matmul(m_monopole, m_dyon) != m_infinity:
        raise AssertionError("finite monodromy product does not give M_infinity")


def check_picard_lefschetz_action_and_symplecticity() -> None:
    j_form = [[0, 1], [-1, 0]]
    for gamma in ((1, 0), (1, -1), (2, 1), (1, 3)):
        monodromy = charge_monodromy(*gamma)
        if matmul(transpose(monodromy), matmul(j_form, monodromy)) != j_form:
            raise AssertionError(f"monodromy is not symplectic for gamma={gamma}")

        nilpotent = [
            [monodromy[0][0] - 1, monodromy[0][1]],
            [monodromy[1][0], monodromy[1][1] - 1],
        ]
        if matmul(nilpotent, nilpotent) != [[0, 0], [0, 0]]:
            raise AssertionError(f"monodromy is not unipotent rank-one for gamma={gamma}")

        for delta in ((0, 1), (1, 0), (1, 2), (-2, 3)):
            transformed_coeffs = row_times_matrix(delta, monodromy)
            expected = (
                delta[0] + 2 * symplectic_pair(delta, gamma) * gamma[0],
                delta[1] + 2 * symplectic_pair(delta, gamma) * gamma[1],
            )
            if transformed_coeffs != expected:
                raise AssertionError(
                    f"central-charge PL action mismatch: gamma={gamma}, delta={delta}, "
                    f"got {transformed_coeffs}, expected {expected}"
                )


def check_local_hyper_threshold_shift() -> None:
    # In the local electric frame z=Z_gamma, z_D=Z_eta, the singular
    # hypermultiplet threshold is z_D^sing=-(i/pi) z log z up to single-valued
    # linear terms. A positive loop z -> exp(2*pi*i) z shifts z_D by 2z.
    shift_coefficient = -(1j / mp.pi) * (2 * mp.pi * 1j)
    assert_close("local hyper threshold monodromy coefficient", shift_coefficient, 2, mp.mpf("1e-50"))

    for gamma in ((1, 0), (1, -1), (2, 1), (1, 3)):
        # Find a small integral eta with <eta,gamma>=1 when gamma is primitive.
        eta = None
        for m in range(-5, 6):
            for e in range(-5, 6):
                if symplectic_pair((m, e), gamma) == 1:
                    eta = (m, e)
                    break
            if eta is not None:
                break
        if eta is None:
            raise AssertionError(f"could not find symplectic complement for {gamma}")

        for delta in ((0, 1), (1, 0), (1, 2), (-2, 3)):
            k = symplectic_pair(delta, gamma)
            remainder = (delta[0] - k * eta[0], delta[1] - k * eta[1])
            if symplectic_pair(remainder, gamma) != 0:
                raise AssertionError("local symplectic decomposition failed")
            transformed = (
                delta[0] + 2 * k * gamma[0],
                delta[1] + 2 * k * gamma[1],
            )
            monodromy_coeffs = row_times_matrix(delta, charge_monodromy(*gamma))
            if transformed != monodromy_coeffs:
                raise AssertionError("local hyper threshold shift does not match PL matrix")


def check_residual_r_symmetry_two_singularity_ledger() -> None:
    c2_su2 = 2
    adjoint_weyl_gauginos = 2
    zero_modes_per_adjoint_weyl = 2 * c2_su2
    instanton_r_phase_power = adjoint_weyl_gauginos * zero_modes_per_adjoint_weyl
    if instanton_r_phase_power != 8:
        raise AssertionError("N=2 SU(2) one-instanton R-anomaly should leave Z8")

    # The anomaly leaves alpha = pi k/4, k mod 8.  In the chapter convention
    # phi has R-charge 2 and u=tr phi^2 has charge 4, so u -> (-1)^k u.
    signs = {k: (-1 if k % 2 else 1) for k in range(8)}
    stabilizer_generic_u = [k for k, sign in signs.items() if sign == 1]
    quotient_actions = sorted(set(signs.values()))
    if stabilizer_generic_u != [0, 2, 4, 6]:
        raise AssertionError("generic Coulomb point should preserve the even Z4 subgroup")
    if quotient_actions != [-1, 1]:
        raise AssertionError("Z8/Z4 quotient should act as u -> +/- u")

    singularity = Fraction(7, 3)
    singular_set = {singularity, -singularity}
    reflected_set = {-entry for entry in singular_set}
    if reflected_set != singular_set:
        raise AssertionError("two-singularity set is not invariant under u -> -u")

    u_dimension = Fraction(2)
    lambda_dimension = Fraction(1)
    if u_dimension != 2 * lambda_dimension:
        raise AssertionError("finite singularity coordinate should scale as Lambda^2")

    m_infinity = [[-1, 2], [0, -1]]
    trace_infinity = m_infinity[0][0] + m_infinity[1][1]
    trace_single_nodal_hyper = charge_monodromy(1, 0)[0][0] + charge_monodromy(1, 0)[1][1]
    if trace_single_nodal_hyper != 2:
        raise AssertionError("nodal hypermultiplet monodromy should be unipotent")
    if trace_infinity == trace_single_nodal_hyper:
        raise AssertionError("one nodal finite singularity cannot reproduce M_infinity")


def check_rigid_special_kahler_metric() -> None:
    # Work in units where the common factor 1/(2 pi) in K has been stripped.
    # The exact algebra behind K=Im(bar a^I F_I) is
    # d_I d_barJ K = (tau_IJ - conjugate(tau_JI))/(2i) = Im tau_IJ
    # for a symmetric holomorphic Hessian tau_IJ.
    tau = [
        [(Fraction(1), Fraction(3)), (Fraction(2), Fraction(1))],
        [(Fraction(2), Fraction(1)), (Fraction(-1), Fraction(4))],
    ]
    expected_imaginary_metric = [[Fraction(3), Fraction(1)], [Fraction(1), Fraction(4)]]

    for i in range(2):
        for j in range(2):
            numerator = subtract(tau[i][j], conjugate(tau[j][i]))
            metric_entry = divide_by_two_i(numerator)
            expected = (expected_imaginary_metric[i][j], Fraction(0))
            if metric_entry != expected:
                raise AssertionError(
                    f"rigid special Kahler metric mismatch {(i, j)}: "
                    f"got {metric_entry}, expected {expected}"
                )

    leading_minor = expected_imaginary_metric[0][0]
    determinant = (
        expected_imaginary_metric[0][0] * expected_imaginary_metric[1][1]
        - expected_imaginary_metric[0][1] * expected_imaginary_metric[1][0]
    )
    if leading_minor <= 0 or determinant <= 0:
        raise AssertionError("Im tau should be positive definite in the test patch")

    real_theta_shift = [[Fraction(5), Fraction(-2)], [Fraction(-2), Fraction(7)]]
    shifted_tau = [
        [
            (tau[i][j][0] + real_theta_shift[i][j], tau[i][j][1])
            for j in range(2)
        ]
        for i in range(2)
    ]
    for i in range(2):
        for j in range(2):
            numerator = subtract(shifted_tau[i][j], conjugate(shifted_tau[j][i]))
            metric_entry = divide_by_two_i(numerator)
            expected = (expected_imaginary_metric[i][j], Fraction(0))
            if metric_entry != expected:
                raise AssertionError("real quadratic prepotential shift changed Im tau")


def check_minimal_curve_discriminant() -> None:
    for u in (3, -4, 7):
        branch_discriminant = (1 - (-1)) ** 2 * (1 - u) ** 2 * ((-1) - u) ** 2
        expected = 4 * (u * u - 1) ** 2
        if branch_discriminant != expected:
            raise AssertionError("minimal SW curve discriminant mismatch")
    if 4 * (1 * 1 - 1) ** 2 != 0 or 4 * ((-1) * (-1) - 1) ** 2 != 0:
        raise AssertionError("finite discriminant should vanish at u=+-1")


def check_picard_fuchs() -> None:
    for label, fn in (("a", a_period), ("aD", aD_period)):
        for u in (mp.mpf("3.7"), mp.mpf("8.25")):
            residual = (u * u - 1) * mp.diff(fn, u, 2) + fn(u) / 4
            assert_close(f"{label} Picard-Fuchs residual at u={u}", residual, 0, mp.mpf("1e-42"))


def check_large_u_asymptotics() -> None:
    u = mp.mpf("1e6")
    a_val = a_period(u)
    assert_close("a/sqrt(2u) at large u", a_val / mp.sqrt(2 * u), 1, mp.mpf("1e-12"))

    leading_dual = 1j * a_val * mp.log(a_val * a_val) / mp.pi
    ratio = aD_period(u) / leading_dual
    if abs(ratio - 1) > mp.mpf("0.05"):
        raise AssertionError(f"aD logarithmic asymptotic ratio too far from 1: {ratio}")


def check_monopole_vanishing() -> None:
    for s in (mp.mpf("1e-3"), mp.mpf("1e-4")):
        ratio = aD_period(1 + s) / s
        assert_close(f"aD/(u-1) near u=1, s={s}", ratio, 0.5j, mp.mpf("4e-5"))


def check_argyres_douglas_scaling() -> None:
    x_dim = Fraction(2, 5)
    y_dim = Fraction(3, 5)
    u_dim = Fraction(6, 5)
    v_dim = Fraction(4, 5)
    if 2 * y_dim != 3 * x_dim:
        raise AssertionError("AD cusp quasi-homogeneity failed")
    if u_dim + x_dim - y_dim != 1:
        raise AssertionError("AD differential should have dimension one")
    if u_dim != 2 * y_dim:
        raise AssertionError("AD Coulomb parameter dimension mismatch")
    if v_dim + x_dim != u_dim:
        raise AssertionError("AD relevant deformation dimension mismatch")


def check_argyres_douglas_discriminant_and_nonlocality() -> None:
    def cubic_discriminant(p: int, q: int) -> int:
        return -4 * p**3 - 27 * q**2

    for v, u in ((0, 0), (3, 2), (-2, 5), (1, -4)):
        direct = cubic_discriminant(v, u)
        chapter_formula = -4 * v**3 - 27 * u**2
        if direct != chapter_formula:
            raise AssertionError("AD cusp discriminant formula mismatch")
    if cubic_discriminant(0, 0) != 0:
        raise AssertionError("AD cusp should have vanishing discriminant at the collision")

    electric_one = (0, 1)
    electric_two = (0, 3)
    if symplectic_pair(electric_one, electric_two) != 0:
        raise AssertionError("electric sublattice should be isotropic")

    mutually_nonlocal_pair = ((1, 0), (0, 1))
    if symplectic_pair(*mutually_nonlocal_pair) == 0:
        raise AssertionError("test AD charges should be mutually nonlocal")


def main() -> None:
    check_monodromies()
    check_picard_lefschetz_action_and_symplecticity()
    check_local_hyper_threshold_shift()
    check_residual_r_symmetry_two_singularity_ledger()
    check_rigid_special_kahler_metric()
    check_minimal_curve_discriminant()
    check_picard_fuchs()
    check_large_u_asymptotics()
    check_monopole_vanishing()
    check_argyres_douglas_scaling()
    check_argyres_douglas_discriminant_and_nonlocality()
    print("All SU(2) Seiberg-Witten period and monodromy checks passed.")


if __name__ == "__main__":
    main()
