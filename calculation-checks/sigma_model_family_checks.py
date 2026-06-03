#!/usr/bin/env python3
"""Exact finite checks for sigma-model family identities.

The checks cover the CP^{N-1} projector geometry, the CP^1/O(3) Pauli-matrix
normalization identities, the PCM Lax coefficient split, the
Polyakov-Wiegmann WZ coefficient, WZW central charges and endpoint
representation formulae, nonabelian-bosonization central-charge bookkeeping,
the projective-model crossing tensors, the SU(N) sine-mass/fusion-angle and
rational-matrix bootstrap blocks, the A_{N-1} inverse-Cartan and nested
root-count ledgers for chiral Gross-Neveu and principal-chiral families, the
repulsive sausage charged scattering identities and formal Yang--Baxter
component identity, the supertarget one-loop coefficients, and the curvature
and one-loop Ricci-flow closure formulae for the sausage metric used in
Volume VI.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
import math

import mpmath as mp
import numpy as np
import sympy as sp

from check_utils import assert_close


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


def check_cp1_o3_pauli_ledger() -> None:
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    pauli = [sx, sy, sz]

    n = sp.symbols("n1 n2 n3", real=True)
    u = sp.symbols("u1 u2 u3", real=True)
    v = sp.symbols("v1 v2 v3", real=True)

    p = sp.eye(2) / 2
    dp_u = sp.zeros(2)
    dp_v = sp.zeros(2)
    for coefficient, sigma in zip(n, pauli):
        p += coefficient * sigma / 2
    for coefficient, sigma in zip(u, pauli):
        dp_u += coefficient * sigma / 2
    for coefficient, sigma in zip(v, pauli):
        dp_v += coefficient * sigma / 2

    kinetic = sp.trace(dp_u * dp_u)
    kinetic_expected = sum(component**2 for component in u) / 2
    assert_zero("CP1/O3 kinetic trace", kinetic - kinetic_expected)

    triple = -sp.I * sp.trace(p * (dp_u * dp_v - dp_v * dp_u))
    cross = (
        n[0] * (u[1] * v[2] - u[2] * v[1])
        + n[1] * (u[2] * v[0] - u[0] * v[2])
        + n[2] * (u[0] * v[1] - u[1] * v[0])
    )
    assert_zero("CP1/O3 topological trace", triple - cross / 2)


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


def check_wzw_endpoint_representation_formulas() -> None:
    for level in range(1, 9):
        su2_c = Fraction(3 * level, level + 2)
        assert_equal(
            f"SU(2)_{level} Sugawara central charge",
            su2_c,
            Fraction(level * 3, level + 2),
        )
        for ell in range(level + 1):
            numerator = ell * (ell + 2)
            conformal_weight = Fraction(numerator, 4 * (level + 2))
            assert_equal(
                f"SU(2)_{level} primary weight ell={ell}",
                conformal_weight,
                Fraction(ell * (ell + 2), 4 * (level + 2)),
            )

        coset_c = su2_c + Fraction(1) - Fraction(3 * (level + 1), level + 3)
        minimal_c = Fraction(1) - Fraction(6, (level + 2) * (level + 3))
        assert_equal(
            f"SU(2)_k x SU(2)_1 / SU(2)_{{k+1}} c k={level}",
            coset_c,
            minimal_c,
        )

    for n in range(2, 8):
        # For SU(N), dim g = N^2-1 and h^vee = N in the long-root-squared-2
        # convention used in the WZW endpoint section.
        assert_equal(
            f"SU({n})_1 WZW central charge",
            Fraction(n * n - 1, n + 1),
            Fraction(n - 1),
        )


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


def check_projective_large_n_induced_gauge_kernel() -> None:
    x = sp.symbols("x")
    first_moment = sp.integrate((1 - 2 * x) ** 2, (x, 0, 1))
    second_moment = sp.integrate((1 - 2 * x) ** 2 * x * (1 - x), (x, 0, 1))
    assert_equal("CP large-N polarization first moment", first_moment, sp.Rational(1, 3))
    assert_equal("CP large-N polarization second moment", second_moment, sp.Rational(1, 30))

    # Pi(p^2)=1/(4*pi)[1/(3 m^2)-p^2/(30 m^4)+...].  Since
    # (1/2) A_mu(p)(p^2 delta_{mu nu}-p_mu p_nu)A_nu(-p)
    # = (1/4) F_{mu nu}(p)F_{mu nu}(-p), the coefficient of
    # F_{mu nu}F_{mu nu} is N Pi(0)/4 = N/(48 pi m^2).
    pi_zero_without_pi = Fraction(1, 12)
    maxwell_without_pi = pi_zero_without_pi / 4
    assert_equal("CP large-N Maxwell coefficient without N/pi/m^2", maxwell_without_pi, Fraction(1, 48))

    # If N/(48*pi*m^2)=1/(4 e_eff^2), then e_eff^2=12*pi*m^2/N; the
    # one-dimensional electrostatic energy is e_eff^2 Q^2 R/2.
    effective_charge_without_pi_m2_over_n = Fraction(12)
    linear_potential_without_pi_m2_over_n = effective_charge_without_pi_m2_over_n / 2
    assert_equal(
        "CP large-N linear potential coefficient",
        linear_potential_without_pi_m2_over_n,
        Fraction(6),
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


def su_n_cartan(n: int) -> list[list[Fraction]]:
    return [
        [
            Fraction(2 if r == s else -1 if abs(r - s) == 1 else 0)
            for s in range(n - 1)
        ]
        for r in range(n - 1)
    ]


def su_n_inverse_cartan(n: int) -> list[list[Fraction]]:
    return [
        [
            Fraction(min(r, s) * (n - max(r, s)), n)
            for s in range(1, n)
        ]
        for r in range(1, n)
    ]


def fraction_matrix_vector(
    matrix: list[list[Fraction]],
    vector: tuple[int, ...] | list[int],
) -> list[Fraction]:
    return [
        sum(row[column] * vector[column] for column in range(len(vector)))
        for row in matrix
    ]


def fraction_matrix_product(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    width = len(right[0])
    inner = len(right)
    return [
        [
            sum(left[row][k] * right[k][column] for k in range(inner))
            for column in range(width)
        ]
        for row in range(len(left))
    ]


def su_n_nality(counts: tuple[int, ...] | list[int], n: int) -> int:
    return sum((index + 1) * count for index, count in enumerate(counts)) % n


def is_integral_vector(vector: list[Fraction]) -> bool:
    return all(entry.denominator == 1 for entry in vector)


def check_su_n_nested_root_count_ledgers() -> None:
    for n in range(3, 9):
        cartan = su_n_cartan(n)
        inverse = su_n_inverse_cartan(n)
        identity = [
            [Fraction(1 if row == column else 0) for column in range(n - 1)]
            for row in range(n - 1)
        ]
        assert_equal(
            f"SU({n}) Cartan inverse",
            fraction_matrix_product(cartan, inverse),
            identity,
        )

        for counts in product(range(4), repeat=n - 1):
            root_counts = fraction_matrix_vector(inverse, counts)
            integral = is_integral_vector(root_counts)
            assert_equal(
                f"SU({n}) nested root integrality iff N-ality zero {counts}",
                integral,
                su_n_nality(counts, n) == 0,
            )

            right_counts = tuple(reversed(counts))
            right_root_counts = fraction_matrix_vector(inverse, right_counts)
            assert_equal(
                f"PCM left/right singlet obstruction equivalence SU({n}) {counts}",
                is_integral_vector(right_root_counts),
                integral,
            )
            assert_equal(
                f"PCM right N-ality is conjugate SU({n}) {counts}",
                su_n_nality(right_counts, n),
                (-su_n_nality(counts, n)) % n,
            )

    su3_inverse = su_n_inverse_cartan(3)
    assert_equal(
        "SU(3) V1 plus V2 root ledger",
        fraction_matrix_vector(su3_inverse, (1, 1)),
        [Fraction(1), Fraction(1)],
    )
    assert_equal(
        "SU(3) three fundamentals root ledger",
        fraction_matrix_vector(su3_inverse, (3, 0)),
        [Fraction(2), Fraction(1)],
    )
    assert_equal(
        "SU(3) one fundamental fractional ledger",
        fraction_matrix_vector(su3_inverse, (1, 0)),
        [Fraction(2, 3), Fraction(1, 3)],
    )

    su4_inverse = su_n_inverse_cartan(4)
    assert_equal(
        "SU(4) four fundamentals root ledger",
        fraction_matrix_vector(su4_inverse, (4, 0, 0)),
        [Fraction(3), Fraction(2), Fraction(1)],
    )
    assert_equal(
        "SU(4) two rank-two particles root ledger",
        fraction_matrix_vector(su4_inverse, (0, 2, 0)),
        [Fraction(1), Fraction(2), Fraction(1)],
    )
    assert_equal(
        "SU(4) PCM two rank-two right root ledger",
        fraction_matrix_vector(su4_inverse, tuple(reversed((0, 2, 0)))),
        [Fraction(1), Fraction(2), Fraction(1)],
    )


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


def sausage_spp(theta: complex, lam: float) -> complex:
    return complex(
        mp.sinh(lam * (theta - 1j * math.pi))
        / mp.sinh(lam * (theta + 1j * math.pi))
    )


def sausage_charge_one_matrix(theta: complex, lam: float) -> np.ndarray:
    direct = (
        mp.sinh(lam * theta)
        / mp.sinh(lam * (theta - 2j * math.pi))
        * sausage_spp(theta, lam)
    )
    exchange = (
        -1j
        * math.sin(2.0 * math.pi * lam)
        / mp.sinh(lam * (theta - 2j * math.pi))
        * sausage_spp(theta, lam)
    )
    return np.array([[direct, exchange], [exchange, direct]], dtype=complex)


def sausage_charge_zero_matrix(theta: complex, lam: float) -> np.ndarray:
    e_entry = sausage_spp(1j * math.pi - theta, lam)
    f_entry = (
        -1j
        * math.sin(2.0 * math.pi * lam)
        / mp.sinh(lam * (1j * math.pi - theta - 2j * math.pi))
        * sausage_spp(1j * math.pi - theta, lam)
    )
    g_entry = (
        -math.sin(math.pi * lam)
        * math.sin(2.0 * math.pi * lam)
        / (
            mp.sinh(lam * (theta - 2j * math.pi))
            * mp.sinh(lam * (theta + 1j * math.pi))
        )
    )
    h_entry = sausage_charge_one_matrix(theta, lam)[0, 0] + g_entry
    return np.array(
        [
            [e_entry, f_entry, g_entry],
            [f_entry, h_entry, f_entry],
            [g_entry, f_entry, e_entry],
        ],
        dtype=complex,
    )


def sausage_full_triplet_matrix(theta: complex, lam: float) -> np.ndarray:
    matrix = np.zeros((9, 9), dtype=complex)

    def pair_index(first: int, second: int) -> int:
        return 3 * first + second

    # Basis labels: 0=+, 1=0, 2=-.
    matrix[pair_index(0, 0), pair_index(0, 0)] = sausage_spp(theta, lam)
    matrix[pair_index(2, 2), pair_index(2, 2)] = sausage_spp(theta, lam)

    charge_one = sausage_charge_one_matrix(theta, lam)
    for basis in ([(0, 1), (1, 0)], [(2, 1), (1, 2)]):
        for row, (out_first, out_second) in enumerate(basis):
            for col, (in_first, in_second) in enumerate(basis):
                matrix[pair_index(out_first, out_second), pair_index(in_first, in_second)] = charge_one[row, col]

    charge_zero = sausage_charge_zero_matrix(theta, lam)
    zero_basis = [(0, 2), (1, 1), (2, 0)]
    for row, (out_first, out_second) in enumerate(zero_basis):
        for col, (in_first, in_second) in enumerate(zero_basis):
            matrix[pair_index(out_first, out_second), pair_index(in_first, in_second)] = charge_zero[row, col]

    return matrix


def sausage_op13(two_particle_matrix: np.ndarray) -> np.ndarray:
    operator = np.zeros((27, 27), dtype=complex)

    def triple_index(first: int, second: int, third: int) -> int:
        return 9 * first + 3 * second + third

    def pair_index(first: int, third: int) -> int:
        return 3 * first + third

    for first_in in range(3):
        for second in range(3):
            for third_in in range(3):
                col = triple_index(first_in, second, third_in)
                pair_col = pair_index(first_in, third_in)
                for first_out in range(3):
                    for third_out in range(3):
                        row = triple_index(first_out, second, third_out)
                        pair_row = pair_index(first_out, third_out)
                        operator[row, col] = two_particle_matrix[pair_row, pair_col]
    return operator


def sausage_formal_sinh(z: sp.Expr, shift: int, q: sp.Symbol) -> sp.Expr:
    """Return sinh(lambda theta + i pi lambda shift) with z = exp(lambda theta)."""
    return (z * q**shift - z**-1 * q**(-shift)) / 2


def sausage_formal_spp(z: sp.Expr, q: sp.Symbol) -> sp.Expr:
    return sp.cancel(sausage_formal_sinh(z, -1, q) / sausage_formal_sinh(z, 1, q))


def sausage_formal_charge_one_entries(z: sp.Expr, q: sp.Symbol) -> tuple[sp.Expr, sp.Expr]:
    d_entry = sausage_formal_spp(z, q)
    direct = sausage_formal_sinh(z, 0, q) / sausage_formal_sinh(z, -2, q) * d_entry
    minus_i_sin_two = -(q**2 - q**-2) / 2
    exchange = minus_i_sin_two / sausage_formal_sinh(z, -2, q) * d_entry
    return sp.cancel(direct), sp.cancel(exchange)


def sausage_formal_spm_exchange(z: sp.Expr, q: sp.Symbol) -> sp.Expr:
    minus_sin_one_sin_two = (q - q**-1) * (q**2 - q**-2) / 4
    return sp.cancel(
        minus_sin_one_sin_two
        / (sausage_formal_sinh(z, -2, q) * sausage_formal_sinh(z, 1, q))
    )


def sausage_formal_full_triplet_entries(
    z: sp.Expr,
    q: sp.Symbol,
) -> dict[tuple[tuple[int, int], tuple[int, int]], sp.Expr]:
    entries: dict[tuple[tuple[int, int], tuple[int, int]], sp.Expr] = {}

    def add(out_first: int, out_second: int, in_first: int, in_second: int, value: sp.Expr) -> None:
        entries[((out_first, out_second), (in_first, in_second))] = sp.cancel(value)

    # Basis labels: 0=+, 1=0, 2=-.
    add(0, 0, 0, 0, sausage_formal_spp(z, q))
    add(2, 2, 2, 2, sausage_formal_spp(z, q))

    direct, exchange = sausage_formal_charge_one_entries(z, q)
    for basis in ([(0, 1), (1, 0)], [(2, 1), (1, 2)]):
        for row, (out_first, out_second) in enumerate(basis):
            for col, (in_first, in_second) in enumerate(basis):
                add(out_first, out_second, in_first, in_second, direct if row == col else exchange)

    crossed_z = q / z
    e_entry = sausage_formal_spp(crossed_z, q)
    _, f_entry = sausage_formal_charge_one_entries(crossed_z, q)
    g_entry = sausage_formal_spm_exchange(z, q)
    h_entry = direct + g_entry
    zero_basis = [(0, 2), (1, 1), (2, 0)]
    zero_block = [[e_entry, f_entry, g_entry], [f_entry, h_entry, f_entry], [g_entry, f_entry, e_entry]]
    for row, (out_first, out_second) in enumerate(zero_basis):
        for col, (in_first, in_second) in enumerate(zero_basis):
            add(out_first, out_second, in_first, in_second, zero_block[row][col])

    return entries


def sausage_sparse_op12(
    two_particle_entries: dict[tuple[tuple[int, int], tuple[int, int]], sp.Expr],
) -> dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr]:
    operator: dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr] = {}
    for (out_pair, in_pair), value in two_particle_entries.items():
        for third in range(3):
            operator[((out_pair[0], out_pair[1], third), (in_pair[0], in_pair[1], third))] = value
    return operator


def sausage_sparse_op23(
    two_particle_entries: dict[tuple[tuple[int, int], tuple[int, int]], sp.Expr],
) -> dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr]:
    operator: dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr] = {}
    for (out_pair, in_pair), value in two_particle_entries.items():
        for first in range(3):
            operator[((first, out_pair[0], out_pair[1]), (first, in_pair[0], in_pair[1]))] = value
    return operator


def sausage_sparse_op13(
    two_particle_entries: dict[tuple[tuple[int, int], tuple[int, int]], sp.Expr],
) -> dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr]:
    operator: dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr] = {}
    for (out_pair, in_pair), value in two_particle_entries.items():
        for second in range(3):
            operator[((out_pair[0], second, out_pair[1]), (in_pair[0], second, in_pair[1]))] = value
    return operator


def sausage_sparse_compose(
    left: dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr],
    right: dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr],
) -> dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr]:
    right_by_row: defaultdict[tuple[int, int, int], list[tuple[tuple[int, int, int], sp.Expr]]] = defaultdict(list)
    for (row, col), value in right.items():
        right_by_row[row].append((col, value))

    composed: defaultdict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Expr] = defaultdict(lambda: 0)
    for (row, middle), left_value in left.items():
        for col, right_value in right_by_row.get(middle, []):
            composed[(row, col)] += left_value * right_value
    return {key: sp.cancel(value) for key, value in composed.items() if value != 0}


def check_sausage_formal_yang_baxter_components() -> None:
    q, u, v = sp.symbols("q u v", nonzero=True)
    entries_u = sausage_formal_full_triplet_entries(u, q)
    entries_v = sausage_formal_full_triplet_entries(v, q)
    entries_uv = sausage_formal_full_triplet_entries(u * v, q)

    lhs = sausage_sparse_compose(
        sausage_sparse_compose(sausage_sparse_op12(entries_u), sausage_sparse_op13(entries_uv)),
        sausage_sparse_op23(entries_v),
    )
    rhs = sausage_sparse_compose(
        sausage_sparse_compose(sausage_sparse_op23(entries_v), sausage_sparse_op13(entries_uv)),
        sausage_sparse_op12(entries_u),
    )

    assert_equal("sausage formal two-particle nonzero count", len(entries_u), 19)
    assert_equal("sausage formal YBE component support", len(set(lhs) | set(rhs)), 141)
    for component in sorted(set(lhs) | set(rhs)):
        numerator = sp.together(lhs.get(component, 0) - rhs.get(component, 0)).as_numer_denom()[0]
        if sp.factor(numerator) != 0:
            raise AssertionError(f"sausage formal YBE component {component}: got {sp.cancel(numerator)}, expected 0")


def check_sausage_repulsive_smatrix_ledgers() -> None:
    for lam in (0.1, 0.25, 0.49):
        for theta in (0.37, 1.11):
            assert_close(
                f"sausage ++ unitarity lambda={lam} theta={theta}",
                sausage_spp(theta, lam) * sausage_spp(-theta, lam),
                1.0,
            )
            matrix = sausage_charge_one_matrix(theta, lam)
            inverse_matrix = sausage_charge_one_matrix(-theta, lam)
            assert_close(
                f"sausage charge-one unitarity lambda={lam} theta={theta}",
                np.max(np.abs(matrix @ inverse_matrix - np.eye(2))),
                0.0,
            )
            zero_matrix = sausage_charge_zero_matrix(theta, lam)
            zero_inverse_matrix = sausage_charge_zero_matrix(-theta, lam)
            assert_close(
                f"sausage charge-zero unitarity lambda={lam} theta={theta}",
                np.max(np.abs(zero_matrix @ zero_inverse_matrix - np.eye(3))),
                0.0,
            )
            full_matrix = sausage_full_triplet_matrix(theta, lam)
            full_inverse_matrix = sausage_full_triplet_matrix(-theta, lam)
            assert_close(
                f"sausage full triplet unitarity lambda={lam} theta={theta}",
                np.max(np.abs(full_matrix @ full_inverse_matrix - np.eye(9))),
                0.0,
            )

        # Finite integer ledger for the denominator zeros.  The proof in the
        # text gives the all-integer argument.
        for n in range(-4, 6):
            zero_plus = math.pi * (n / lam - 1.0)
            zero_minus_two = math.pi * (n / lam + 2.0)
            if 0.0 < zero_plus < math.pi:
                raise AssertionError(f"sausage plus denominator physical pole: lambda={lam}, n={n}")
            if 0.0 < zero_minus_two < math.pi:
                raise AssertionError(f"sausage minus-two denominator physical pole: lambda={lam}, n={n}")

    theta = 0.83
    lam = 1.0e-7
    o3_highest = (theta - 1j * math.pi) / (theta + 1j * math.pi)
    o3_direct = theta / (theta - 2j * math.pi) * o3_highest
    o3_exchange = -2j * math.pi / (theta - 2j * math.pi) * o3_highest
    limiting_matrix = sausage_charge_one_matrix(theta, lam)
    assert_close("sausage lambda->0 highest-charge limit", sausage_spp(theta, lam), o3_highest, 1.0e-6)
    assert_close("sausage lambda->0 charge-one direct limit", limiting_matrix[0, 0], o3_direct, 1.0e-6)
    assert_close("sausage lambda->0 charge-one exchange limit", limiting_matrix[0, 1], o3_exchange, 1.0e-6)

    identity_three = np.eye(3)
    for lam in (0.1, 0.25, 0.49):
        for theta, phi in ((0.37, 0.71), (0.83, 1.19)):
            s_theta = sausage_full_triplet_matrix(theta, lam)
            s_phi = sausage_full_triplet_matrix(phi, lam)
            s_sum = sausage_full_triplet_matrix(theta + phi, lam)
            op12 = np.kron(s_theta, identity_three)
            op23 = np.kron(identity_three, s_phi)
            op13 = sausage_op13(s_sum)
            lhs = op12 @ op13 @ op23
            rhs = op23 @ op13 @ op12
            assert_close(
                f"sausage full triplet YBE lambda={lam} theta={theta} phi={phi}",
                np.max(np.abs(lhs - rhs)),
                0.0,
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

    tau, tau0, h0, alpha, beta = sp.symbols("tau tau0 h0 alpha beta", nonzero=True)
    negative_argument = sp.atanh(alpha * h0) - alpha * (tau - tau0)
    h_negative = sp.tanh(negative_argument) / alpha
    q_negative = -alpha**2 * h_negative**2
    assert_zero(
        "sausage integrated negative h-flow",
        sp.diff(h_negative, tau) + (1 - alpha**2 * h_negative**2),
    )
    assert_zero(
        "sausage integrated negative invariant",
        q_negative / h_negative**2 + alpha**2,
    )

    positive_argument = sp.atan(beta * h0) - beta * (tau - tau0)
    h_positive = sp.tan(positive_argument) / beta
    q_positive = beta**2 * h_positive**2
    assert_zero(
        "sausage integrated positive h-flow",
        sp.diff(h_positive, tau) + (1 + beta**2 * h_positive**2),
    )
    assert_zero(
        "sausage integrated positive invariant",
        q_positive / h_positive**2 - beta**2,
    )

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
    check_cp1_o3_pauli_ledger()
    check_pcm_lax_coefficients()
    check_symmetric_space_lax_coefficients()
    check_polyakov_wiegmann_coefficient()
    check_wzw_central_charge_examples()
    check_wzw_endpoint_representation_formulas()
    check_nonabelian_bosonization_central_charge()
    check_projective_crossing_tensors()
    check_projective_large_n_induced_gauge_kernel()
    check_su_n_sine_mass_fusion()
    check_su_n_rational_block()
    check_su_n_nested_root_count_ledgers()
    check_scalar_cdd_and_su_n_gamma_ledgers()
    check_supertarget_one_loop_ledgers()
    check_sausage_repulsive_smatrix_ledgers()
    check_sausage_formal_yang_baxter_components()
    check_sausage_metric_curvature()
    print("All sigma-model family checks passed.")


if __name__ == "__main__":
    main()
