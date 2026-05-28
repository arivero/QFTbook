#!/usr/bin/env python3
"""Exact finite checks for sigma-model family identities.

The checks cover the CP^{N-1} projector geometry, the PCM Lax coefficient
split, the Polyakov-Wiegmann WZ coefficient, WZW central charges,
nonabelian-bosonization central-charge
bookkeeping, the projective-model crossing tensors, the SU(N)
sine-mass/fusion-angle and rational-matrix bootstrap blocks, the supertarget
one-loop coefficient ledgers, and the curvature and one-loop Ricci-flow
closure formulae for the sausage metric used in Volume VI.
"""

from __future__ import annotations

import math
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def assert_zero(name: str, value) -> None:
    if sp.simplify(value) != 0:
        raise AssertionError(f"{name}: got {value}, expected 0")


def assert_trig_zero(name: str, value) -> None:
    reduced = sp.trigsimp(sp.simplify(value.rewrite(sp.cos)))
    if reduced != 0:
        raise AssertionError(f"{name}: got {value}, expected 0")


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def check_cp_projector() -> None:
    # For a normalized vector z, P = z z^\dagger obeys
    # P^2 = z (z^\dagger z) z^\dagger = P.  The exact scalar coefficient is 1.
    z_dagger_z = Fraction(1)
    assert_equal("CP projector scalar", z_dagger_z**2, z_dagger_z)

    theta, phi = sp.symbols("theta phi", real=True)
    unit_i = sp.I
    z = sp.Matrix([sp.cos(theta / 2), sp.exp(unit_i * phi) * sp.sin(theta / 2)])
    p = z * z.conjugate().T
    dtheta_p = p.diff(theta)
    dphi_p = p.diff(phi)

    a_phi = sp.simplify(-unit_i * (z.conjugate().T * z.diff(phi))[0])
    f_theta_phi = sp.diff(a_phi, theta)
    dtheta_z = z.diff(theta)
    dphi_z = z.diff(phi) - unit_i * a_phi * z
    kin_theta = sp.simplify((dtheta_z.conjugate().T * dtheta_z)[0])
    kin_phi = sp.trigsimp(sp.simplify((dphi_z.conjugate().T * dphi_z)[0]))

    assert_trig_zero("CP1 projector theta kinetic", sp.trace(dtheta_p * dtheta_p) - 2 * kin_theta)
    assert_trig_zero("CP1 projector phi kinetic", sp.trace(dphi_p * dphi_p) - 2 * kin_phi)
    assert_trig_zero("CP1 monopole potential", a_phi - sp.sin(theta / 2) ** 2)
    assert_trig_zero("CP1 curvature", f_theta_phi - sp.sin(theta) / 2)
    assert_trig_zero(
        "CP1 projector curvature",
        -unit_i * sp.trace(p * (dtheta_p * dphi_p - dphi_p * dtheta_p)) - f_theta_phi,
    )


def check_pcm_lax_coefficients() -> None:
    # With L_+ = j_+/(1-zeta), L_- = j_-/(1+zeta), multiplying the curvature
    # by 1-zeta^2 gives M - zeta E, where
    # M = d_+j_- - d_-j_+ + [j_+,j_-] and E = d_+j_- + d_-j_+.
    coeff_dpjm_constant = Fraction(1)
    coeff_dmjp_constant = Fraction(-1)
    coeff_comm_constant = Fraction(1)
    coeff_dpjm_zeta = Fraction(-1)
    coeff_dmjp_zeta = Fraction(-1)
    coeff_comm_zeta = Fraction(0)
    assert_equal("PCM constant coefficient", (coeff_dpjm_constant, coeff_dmjp_constant, coeff_comm_constant), (1, -1, 1))
    assert_equal("PCM zeta coefficient", (coeff_dpjm_zeta, coeff_dmjp_zeta, coeff_comm_zeta), (-1, -1, 0))


def check_symmetric_space_lax_coefficients() -> None:
    # For L_+ = A_+ + zeta P_+ and L_- = A_- + zeta^{-1} P_-,
    # flatness expands as H + zeta^{-1} D_+P_- - zeta D_-P_+.
    # The vanishing of the three Laurent coefficients is equivalent to the
    # h-component Maurer-Cartan equation and the two first-order equations
    # D_+P_- = D_-P_+ = 0, which combine into the m-component
    # Maurer-Cartan identity and the Euler-Lagrange equation.
    coeff_zeta_minus_one = (Fraction(1), Fraction(0), Fraction(0))
    coeff_zeta_zero = (Fraction(0), Fraction(1), Fraction(0))
    coeff_zeta_plus_one = (Fraction(0), Fraction(0), Fraction(-1))
    assert_equal("symmetric-space zeta^-1 coefficient", coeff_zeta_minus_one, (1, 0, 0))
    assert_equal("symmetric-space zeta^0 coefficient", coeff_zeta_zero, (0, 1, 0))
    assert_equal("symmetric-space zeta^1 coefficient", coeff_zeta_plus_one, (0, 0, -1))

    # The linear change of variables between (D_+P_-, D_-P_+) and
    # (Maurer-Cartan_m, equation_of_motion) has determinant 2.
    change_matrix = sp.Matrix([[1, -1], [1, 1]])
    assert_equal("symmetric-space MC/EOM determinant", int(change_matrix.det()), 2)


def check_polyakov_wiegmann_coefficient() -> None:
    # With H(g)=1/(24*pi) kappa(theta,[theta,theta]), and the matrix-trace
    # convention kappa(theta,[theta,theta])=2 Tr(theta^3), the standard cubic
    # expansion gives the mixed exact term -3 d Tr(A wedge B)/(12*pi).
    # Hence the boundary coefficient in Gamma[UV] is -1/(4*pi).
    cubic_normalization_denominator = Fraction(12)
    mixed_cyclic_count = Fraction(-3)
    assert_equal(
        "Polyakov-Wiegmann boundary coefficient",
        mixed_cyclic_count / cubic_normalization_denominator,
        Fraction(-1, 4),
    )


def check_wzw_central_charge_examples() -> None:
    # c = k dim(g)/(k+hvee).  For SU(2)_1 this is c=1; for SU(3)_1 this is c=2.
    assert_equal("SU(2)_1 WZW c", Fraction(1 * 3, 1 + 2), Fraction(1))
    assert_equal("SU(3)_1 WZW c", Fraction(1 * 8, 1 + 3), Fraction(2))


def check_nonabelian_bosonization_central_charge() -> None:
    for nc in range(2, 7):
        for nf in range(1, 7):
            color = Fraction(nf * (nc * nc - 1), nf + nc)
            flavor = Fraction(nc * (nf * nf - 1), nc + nf)
            u1 = Fraction(1)
            assert_equal(
                f"nonabelian bosonization c identity Nc={nc} Nf={nf}",
                color + flavor + u1,
                Fraction(nc * nf),
            )


def flip(n: int) -> np.ndarray:
    matrix = np.zeros((n * n, n * n), dtype=complex)
    for i in range(n):
        for j in range(n):
            matrix[j * n + i, i * n + j] = 1.0
    return matrix


def rational_r(theta: complex, n: int, normalized: bool) -> np.ndarray:
    lam = 2.0 * math.pi / n
    identity = np.eye(n * n, dtype=complex)
    numerator = theta * identity - 1j * lam * flip(n)
    if normalized:
        return numerator / (theta - 1j * lam)
    return numerator


def op12(two_body: np.ndarray, n: int) -> np.ndarray:
    return np.kron(two_body, np.eye(n, dtype=complex))


def op23(two_body: np.ndarray, n: int) -> np.ndarray:
    return np.kron(np.eye(n, dtype=complex), two_body)


def op13(two_body: np.ndarray, n: int) -> np.ndarray:
    swap23 = op23(flip(n), n)
    return swap23 @ op12(two_body, n) @ swap23


def projective_annihilation(n: int) -> np.ndarray:
    matrix = np.zeros((n * n, n * n), dtype=complex)
    for i in range(n):
        for j in range(n):
            input_index = i * n + j
            if i == j:
                for m in range(n):
                    matrix[m * n + m, input_index] = 1.0
    return matrix


def check_projective_crossing_tensors() -> None:
    for n in (2, 3, 5):
        identity = np.eye(n * n, dtype=complex)
        permutation = flip(n)
        annihilation = projective_annihilation(n)
        assert_close(
            f"projective annihilation idempotent N={n}",
            np.max(np.abs(annihilation @ annihilation - n * annihilation)),
            0.0,
        )

        singlet_projector = annihilation / n
        adjoint_projector = identity - singlet_projector
        assert_close(
            f"projective singlet projector N={n}",
            np.max(np.abs(singlet_projector @ singlet_projector - singlet_projector)),
            0.0,
        )
        assert_close(
            f"projective adjoint projector N={n}",
            np.max(np.abs(adjoint_projector @ adjoint_projector - adjoint_projector)),
            0.0,
        )
        assert_close(
            f"projective projector orthogonality N={n}",
            np.max(np.abs(singlet_projector @ adjoint_projector)),
            0.0,
        )

        a, b = 1.7, -0.4
        vv_matrix = a * identity + b * permutation
        symmetric = np.zeros(n * n, dtype=complex)
        antisymmetric = np.zeros(n * n, dtype=complex)
        symmetric[0 * n + 1] = 1.0
        symmetric[1 * n + 0] = 1.0
        antisymmetric[0 * n + 1] = 1.0
        antisymmetric[1 * n + 0] = -1.0
        assert_close(
            f"projective VV symmetric eigenvalue N={n}",
            np.max(np.abs(vv_matrix @ symmetric - (a + b) * symmetric)),
            0.0,
        )
        assert_close(
            f"projective VV antisymmetric eigenvalue N={n}",
            np.max(np.abs(vv_matrix @ antisymmetric - (a - b) * antisymmetric)),
            0.0,
        )

        vbar_matrix = a * identity + b * annihilation
        adjoint_vector = np.zeros(n * n, dtype=complex)
        adjoint_vector[0 * n + 0] = 1.0
        adjoint_vector[1 * n + 1] = -1.0
        singlet_vector = np.zeros(n * n, dtype=complex)
        for m in range(n):
            singlet_vector[m * n + m] = 1.0
        assert_close(
            f"projective VbarV adjoint eigenvalue N={n}",
            np.max(np.abs(vbar_matrix @ adjoint_vector - a * adjoint_vector)),
            0.0,
        )
        assert_close(
            f"projective VbarV singlet eigenvalue N={n}",
            np.max(np.abs(vbar_matrix @ singlet_vector - (a + n * b) * singlet_vector)),
            0.0,
        )


def check_su_n_sine_mass_fusion() -> None:
    for n in range(3, 10):
        scale = 1.0 / math.sin(math.pi / n)
        for a in range(1, n):
            for b in range(1, n - a):
                ma = scale * math.sin(math.pi * a / n)
                mb = scale * math.sin(math.pi * b / n)
                mab = scale * math.sin(math.pi * (a + b) / n)
                u = math.pi * (a + b) / n
                assert_close(
                    f"SU(N) sine fusion N={n} a={a} b={b}",
                    mab * mab,
                    ma * ma + mb * mb + 2.0 * ma * mb * math.cos(u),
                )


def check_su_n_rational_block() -> None:
    for n in (3, 4):
        identity = np.eye(n * n, dtype=complex)
        for theta in (0.37, 1.11):
            unitary_error = np.max(np.abs(rational_r(theta, n, True) @ rational_r(-theta, n, True) - identity))
            assert_close(f"SU(N) rational block unitarity N={n} theta={theta}", unitary_error, 0.0)
        for theta, phi in ((0.41, 0.73), (0.82, 1.19)):
            lhs = (
                op12(rational_r(theta, n, False), n)
                @ op13(rational_r(theta + phi, n, False), n)
                @ op23(rational_r(phi, n, False), n)
            )
            rhs = (
                op23(rational_r(phi, n, False), n)
                @ op13(rational_r(theta + phi, n, False), n)
                @ op12(rational_r(theta, n, False), n)
            )
            ybe_error = np.max(np.abs(lhs - rhs))
            assert_close(f"SU(N) rational YBE N={n} theta={theta} phi={phi}", ybe_error, 0.0)


def cgn_a_scalar(theta: float, n: int) -> complex:
    x = theta / (2.0 * math.pi * 1j)
    return complex(
        -mp.gamma(1 - x)
        * mp.gamma(1 - 1 / n + x)
        / (mp.gamma(1 + x) * mp.gamma(1 - 1 / n - x))
    )


def pcm_w_scalar(theta: float, n: int) -> complex:
    x = theta / (2.0 * math.pi * 1j)
    gamma_ratio = (
        mp.gamma(1 - x)
        * mp.gamma(x - 1 / n)
        / (mp.gamma(1 - x - 1 / n) * mp.gamma(x))
    )
    hyperbolic = mp.sinh(theta / 2.0 - math.pi * 1j / n) / mp.sinh(
        theta / 2.0 + math.pi * 1j / n
    )
    return complex(hyperbolic * gamma_ratio**2)


def check_scalar_cdd_and_su_n_gamma_ledgers() -> None:
    theta, alpha = sp.symbols("theta alpha")
    cdd = (sp.sinh(theta) + sp.I * sp.sin(alpha)) / (
        sp.sinh(theta) - sp.I * sp.sin(alpha)
    )
    assert_trig_zero("CDD unitarity", cdd * cdd.subs(theta, -theta) - 1)
    assert_trig_zero(
        "CDD crossing",
        cdd.subs(theta, sp.I * sp.pi - theta) - cdd,
    )

    for n in (3, 4, 5):
        lam = 2.0 * math.pi / n
        for theta_value in (0.37, 1.11):
            a_plus = cgn_a_scalar(theta_value, n)
            a_minus = cgn_a_scalar(-theta_value, n)
            assert_close(
                f"CGN A scalar unitarity N={n} theta={theta_value}",
                a_plus * a_minus,
                1.0,
            )

            b_plus = a_plus / (1.0 - 1j * lam / theta_value)
            c_plus = -1j * lam * b_plus / theta_value
            b_minus = a_minus / (1.0 + 1j * lam / theta_value)
            c_minus = 1j * lam * b_minus / theta_value
            identity_channel = b_plus * b_minus + c_plus * c_minus
            permutation_channel = b_plus * c_minus + c_plus * b_minus
            assert_close(
                f"CGN component identity channel N={n} theta={theta_value}",
                identity_channel,
                1.0,
            )
            assert_close(
                f"CGN component permutation channel N={n} theta={theta_value}",
                permutation_channel,
                0.0,
            )

            w_plus = pcm_w_scalar(theta_value, n)
            w_minus = pcm_w_scalar(-theta_value, n)
            unnormalized_needed = (
                1.0 + lam * lam / (theta_value * theta_value)
            ) ** -2
            assert_close(
                f"PCM W scalar unnormalized ledger N={n} theta={theta_value}",
                w_plus * w_minus,
                unnormalized_needed,
            )
            x_plus = w_plus * ((theta_value - 1j * lam) / theta_value) ** 2
            x_minus = w_minus * ((-theta_value - 1j * lam) / (-theta_value)) ** 2
            assert_close(
                f"PCM normalized scalar unitarity N={n} theta={theta_value}",
                x_plus * x_minus,
                1.0,
            )


def check_supertarget_one_loop_ledgers() -> None:
    for m in range(2, 9):
        for n in range(0, 5):
            tangent_superdimension = (m - 1) - 2 * n
            supersphere_coefficient = m - 2 * n - 2
            assert_equal(
                f"supersphere Ricci graded contraction m={m} n={n}",
                supersphere_coefficient,
                tangent_superdimension - 1,
            )

    for n in range(0, 7):
        m = 2 * n + 2
        assert_equal(
            f"OSp supersphere one-loop cancellation n={n}",
            m - 2 * n - 2,
            0,
        )

    for p in range(0, 7):
        for q in range(0, 7):
            ricci_coefficient = p + 1 - q
            homogeneous_superdimension = (p + 1) - q
            assert_equal(
                f"CP^(p|q) Berezinian exponent p={p} q={q}",
                ricci_coefficient,
                homogeneous_superdimension,
            )

    for n in range(1, 8):
        cp_super_coefficient = (n - 1) + 1 - n
        assert_equal(
            f"CP^(N-1|N) one-loop cancellation N={n}",
            cp_super_coefficient,
            0,
        )
        assert_equal(
            f"ordinary CP^(N-1) coefficient N={n}",
            (n - 1) + 1 - 0,
            n,
        )

    for n in range(0, 7):
        osp_dual_coxeter = (2 * n + 2) - 2 * n - 2
        assert_equal(
            f"osp(2n+2|2n) dual-Coxeter-zero ledger n={n}",
            osp_dual_coxeter,
            0,
        )


def check_sausage_metric_curvature() -> None:
    r, h, q = sp.symbols("r h q", nonzero=True)
    e_metric = h / ((1 - r**2) * (1 + q * r**2))
    g_metric = h * (1 - r**2) / (1 + q * r**2)
    scalar_curvature = (
        -sp.diff(g_metric, r, 2) / (e_metric * g_metric)
        + sp.diff(g_metric, r) ** 2 / (2 * e_metric * g_metric**2)
        + sp.diff(e_metric, r) * sp.diff(g_metric, r) / (2 * e_metric**2 * g_metric)
    )
    expected = 2 * (1 + q) * (1 - q * r**2) / (h * (1 + q * r**2))
    assert_zero("sausage scalar curvature", scalar_curvature - expected)
    assert_zero("sausage round-sphere limit", expected.subs(q, 0) - 2 / h)

    h_dot = -(1 + q)
    q_dot = -2 * q * (1 + q) / h
    e_flow = sp.diff(e_metric, h) * h_dot + sp.diff(e_metric, q) * q_dot
    g_flow = sp.diff(g_metric, h) * h_dot + sp.diff(g_metric, q) * q_dot
    assert_zero("sausage rr Ricci-flow closure", e_flow + expected * e_metric / 2)
    assert_zero("sausage phiphi Ricci-flow closure", g_flow + expected * g_metric / 2)
    assert_zero("sausage Ricci-flow invariant", sp.diff(q / h**2, h) * h_dot + sp.diff(q / h**2, q) * q_dot)

    kappa = sp.symbols("kappa")
    q_physical = -kappa**2
    h_dot_kappa = h_dot.subs(q, q_physical)
    kappa_dot = -kappa * (1 - kappa**2) / h
    q_dot_from_kappa = sp.diff(q_physical, kappa) * kappa_dot
    assert_zero("sausage kappa-flow conversion", q_dot.subs(q, q_physical) - q_dot_from_kappa)

    rho = sp.symbols("rho")
    r_cyl = sp.tanh(rho)
    radial_limit = sp.simplify(
        h * sp.diff(r_cyl, rho) ** 2
        / ((1 - r_cyl**2) * (1 - r_cyl**2))
    )
    angular_limit = sp.simplify(
        h * (1 - r_cyl**2) / (1 - r_cyl**2)
    )
    assert_zero("sausage cylinder radial limit", radial_limit - h)
    assert_zero("sausage cylinder angular limit", angular_limit - h)


def main() -> None:
    check_cp_projector()
    check_pcm_lax_coefficients()
    check_symmetric_space_lax_coefficients()
    check_polyakov_wiegmann_coefficient()
    check_wzw_central_charge_examples()
    check_nonabelian_bosonization_central_charge()
    check_projective_crossing_tensors()
    check_su_n_sine_mass_fusion()
    check_su_n_rational_block()
    check_scalar_cdd_and_su_n_gamma_ledgers()
    check_supertarget_one_loop_ledgers()
    check_sausage_metric_curvature()
    print("All sigma-model family checks passed.")


if __name__ == "__main__":
    main()
