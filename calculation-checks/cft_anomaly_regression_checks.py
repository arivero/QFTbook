#!/usr/bin/env python3
"""Finite arithmetic checks for issue #447 regressions.

These checks cover convention-sensitive algebra that previously suffered
factor or sign regressions in the monograph:

* the factor of two from {q, q} in the neutral-pion anomaly,
* the cubic coefficient in the identity-block expansion near z=1/2,
* the stress-tensor sign for W = -log Z and covariant metric variations,
* the sign of the radial [P, K] commutator obtained from Lorentzian charges.

The script deliberately uses only finite rational or elementary complex
arithmetic.  It does not evaluate loop integrals or conformal blocks.
"""

from __future__ import annotations

from fractions import Fraction

from check_utils import assert_close as _assert_close


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def binom3(alpha: Fraction) -> Fraction:
    return alpha * (alpha - 1) * (alpha - 2) / 6


def check_pi0_anomaly_factor() -> None:
    """Check the finite flavor trace and the coefficient ratio.

    The monograph uses T^3 = diag(1, -1)/2, q = diag(2/3, -1/3), and
    L_{pi0 gamma gamma} = (N_c e^2)/(16 pi^2 f_pi)
      Tr(T^3 {q, q}) pi0 F Ftilde.
    """

    q_u = Fraction(2, 3)
    q_d = Fraction(-1, 3)
    t3_u = Fraction(1, 2)
    t3_d = Fraction(-1, 2)
    nc = 3

    tr_t3_q2 = t3_u * q_u**2 + t3_d * q_d**2
    tr_t3_anticommutator = 2 * tr_t3_q2

    assert_equal("Tr(T3 q^2)", tr_t3_q2, Fraction(1, 6))
    assert_equal("Tr(T3 {q,q})", tr_t3_anticommutator, Fraction(1, 3))

    coefficient_without_common_units = Fraction(nc, 16) * tr_t3_anticommutator
    assert_equal("pi0 coefficient in units e^2/(pi^2 f_pi)", coefficient_without_common_units, Fraction(1, 16))

    coefficient_if_anticommutator_is_dropped = Fraction(nc, 16) * tr_t3_q2
    assert_equal("dropped-anticommutator coefficient", coefficient_if_anticommutator_is_dropped, Fraction(1, 32))


def check_identity_block_cubic_coefficient() -> None:
    """Check the x^3 coefficient after extracting the common factor.

    For z = 1/2 + x and alpha = 2 Delta_phi,

      (1/2 - x)^alpha - (1/2 + x)^alpha

    has cubic coefficient -16 * 2^{-alpha} * binom(alpha, 3).  Dividing by
    the common factor -Delta_phi * 2^{3 - 2 Delta_phi} gives

      (4/3)(Delta_phi - 1)(2 Delta_phi - 1).
    """

    for delta_phi in (Fraction(3, 2), Fraction(2, 1), Fraction(7, 3), Fraction(5, 1)):
        alpha = 2 * delta_phi
        ratio = Fraction(2, 1) * binom3(alpha) / delta_phi
        expected = Fraction(4, 3) * (delta_phi - 1) * (2 * delta_phi - 1)
        wrong_old_value = Fraction(1, 3) * (delta_phi - 1) * (2 * delta_phi - 1)
        assert_equal(f"identity block cubic coefficient at Delta={delta_phi}", ratio, expected)
        if ratio == wrong_old_value:
            raise AssertionError("identity block cubic coefficient accidentally matches the old 1/3 value")


def check_stress_tensor_source_sign() -> None:
    """Check the sign convention used in Vol. III Chapters 1 and 3.

    With Z = integral exp(-S) and W = -log Z, one has delta W = <delta S>.
    For a covariant metric variation

      delta S = -1/2 int sqrt(g) T^{mu nu} delta g_{mu nu},

    the source derivative is therefore

      <T^{mu nu}> = -2/sqrt(g) delta W / delta g_{mu nu}.
    """

    sign_delta_s_covariant = Fraction(-1, 2)
    sign_delta_w = Fraction(1, 1) * sign_delta_s_covariant
    sign_t_from_w = Fraction(1, 1) / sign_delta_w
    assert_equal("stress tensor derivative sign for W=-logZ", sign_t_from_w, Fraction(-2, 1))


def check_radial_pk_sign() -> None:
    """Check the sign conversion from Hermitian Lorentzian charges.

    Starting from [P_L, K_L] = 2 i A_L with A = delta D - J and the radial
    real form D_r = -i D_L, J_r = -i J_L, P_r = i P_L, K_r = -i K_L, the
    coefficient of A_r in [P_r, K_r] is -2.
    """

    i = 1j
    lorentzian_pk_coeff = 2 * i
    commutator_scale_from_pk_map = i * (-i)
    a_l_in_units_of_a_r = i  # since A_r = -i A_L
    radial_pk_coeff = commutator_scale_from_pk_map * lorentzian_pk_coeff * a_l_in_units_of_a_r

    _assert_close("radial [P,K] coefficient", radial_pk_coeff, -2, tol=1e-12)
    _assert_close("radial [K,P] coefficient", -radial_pk_coeff, 2, tol=1e-12)


def main() -> None:
    check_pi0_anomaly_factor()
    check_identity_block_cubic_coefficient()
    check_stress_tensor_source_sign()
    check_radial_pk_sign()
    print("All CFT/anomaly regression arithmetic checks passed.")


if __name__ == "__main__":
    main()
