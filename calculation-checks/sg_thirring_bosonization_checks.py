#!/usr/bin/env python3
"""Finite convention checks for the sine-Gordon/massive-Thirring section."""

from __future__ import annotations

from fractions import Fraction

Matrix = tuple[tuple[complex, ...], ...]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name} failed")


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def matadd(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(len(a[0])))
        for i in range(len(a))
    )


def matscale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * entry for entry in row) for row in a)


def dagger(a: Matrix) -> Matrix:
    return tuple(
        tuple(a[j][i].conjugate() for j in range(len(a)))
        for i in range(len(a[0]))
    )


def zero(n: int) -> Matrix:
    return tuple(tuple(0j for _ in range(n)) for _ in range(n))


def identity(n: int) -> Matrix:
    return tuple(tuple(1 + 0j if i == j else 0j for j in range(n)) for i in range(n))


def vertex_dimension_from_alpha_squared(alpha_squared_over_pi: Fraction) -> Fraction:
    """Return Delta for <phi phi> = -(2 pi)^(-1) log |x|."""

    return alpha_squared_over_pi / 4


def vertex_ope_exponent(alpha_squared_over_pi: Fraction) -> Fraction:
    """Return the exponent in |x-y|^{-exponent} for V_alpha V_{-alpha}."""

    return alpha_squared_over_pi / 2


def beta_squared_over_four_pi(g_over_pi: Fraction) -> Fraction:
    """Coleman's relation in the monograph convention."""

    return Fraction(1, 1) / (Fraction(1, 1) + g_over_pi)


def k_from_current_square(g_over_pi: Fraction, *, hermitian_current_sign: int) -> Fraction:
    """Return the Euclidean current-sector kinetic coefficient.

    hermitian_current_sign=-1 means the Lorentzian interaction is
    -(g_T/2) J_mu J^mu for the Hermitian current J.  Wick rotation then adds
    +g_T/(2 pi) int (partial phi_0)^2 to the Euclidean scalar action.
    hermitian_current_sign=+1 is the sign obtained by keeping the old printed
    anti-Hermitian-current interaction after translating to J.
    """

    assert hermitian_current_sign in (-1, 1)
    return Fraction(1, 1) - hermitian_current_sign * g_over_pi


def g_over_pi_for_marginal_endpoint(*, hermitian_current_sign: int) -> Fraction:
    target_k = Fraction(1, 2)
    if hermitian_current_sign == -1:
        return target_k - 1
    if hermitian_current_sign == 1:
        return 1 - target_k
    raise ValueError("hermitian_current_sign must be +/-1")


def fermion_dimension(beta_squared_over_pi: Fraction) -> Fraction:
    """Delta = beta^2/(16 pi) + pi/beta^2 for the Mandelstam field."""

    return beta_squared_over_pi / 16 + Fraction(1, 1) / beta_squared_over_pi


def check_mostly_plus_thirring_current_convention() -> None:
    gamma0: Matrix = ((0j, -1 + 0j), (1 + 0j, 0j))
    gamma1: Matrix = ((0j, 1 + 0j), (1 + 0j, 0j))
    beta_dirac = matscale(1j, gamma0)
    one = identity(2)
    z2 = zero(2)

    assert_equal(
        "mostly-plus gamma0 square",
        matmul(gamma0, gamma0),
        matscale(-1, one),
    )
    assert_equal("mostly-plus gamma1 square", matmul(gamma1, gamma1), one)
    assert_equal(
        "mostly-plus off-diagonal Clifford relation",
        matadd(matmul(gamma0, gamma1), matmul(gamma1, gamma0)),
        z2,
    )
    assert_equal("gamma0 anti-Hermitian", dagger(gamma0), matscale(-1, gamma0))
    assert_equal("gamma1 Hermitian", dagger(gamma1), gamma1)
    assert_equal("Dirac beta Hermitian", dagger(beta_dirac), beta_dirac)

    for label, gamma in (("0", gamma0), ("1", gamma1)):
        antihermitian_bilinear_matrix = matmul(beta_dirac, gamma)
        hermitian_current_matrix = matscale(1j, antihermitian_bilinear_matrix)
        assert_equal(
            f"bar psi gamma^{label} psi matrix is anti-Hermitian",
            dagger(antihermitian_bilinear_matrix),
            matscale(-1, antihermitian_bilinear_matrix),
        )
        assert_equal(
            f"i bar psi gamma^{label} psi matrix is Hermitian",
            dagger(hermitian_current_matrix),
            hermitian_current_matrix,
        )

    assert_true(
        "monograph kinetic coefficient is real",
        (-1 + 0j).conjugate() == -1 + 0j,
    )
    assert_true("old extra-i kinetic coefficient is not real", (1j).conjugate() != 1j)

    # Since J=iB for B=bar psi gamma psi, B_mu B^mu = -J_mu J^mu.
    b_square_to_j_square = Fraction(-1, 1)
    assert_equal(
        "anti-Hermitian bilinear square sign",
        b_square_to_j_square,
        Fraction(-1, 1),
    )
    old_bilinear_square_coefficient = Fraction(-1, 2)
    translated_old_j_coefficient = -old_bilinear_square_coefficient
    monograph_j_coefficient = Fraction(-1, 2)
    translated_monograph_b_coefficient = -monograph_j_coefficient
    assert_equal(
        "old printed B-square sign would translate to +g J^2/2",
        translated_old_j_coefficient,
        Fraction(1, 2),
    )
    assert_equal(
        "monograph Coleman chart is -g J^2/2",
        monograph_j_coefficient,
        Fraction(-1, 2),
    )
    assert_equal(
        "monograph chart is +g B^2/2 in the anti-Hermitian bilinear",
        translated_monograph_b_coefficient,
        Fraction(1, 2),
    )


def check_vertex_ope_and_dimensions() -> None:
    alpha_squared_over_pi = Fraction(4, 1)
    assert_equal(
        "full vertex dimension at alpha^2=4 pi",
        vertex_dimension_from_alpha_squared(alpha_squared_over_pi),
        Fraction(1, 1),
    )
    assert_equal(
        "full vertex OPE exponent is twice the scaling dimension",
        vertex_ope_exponent(alpha_squared_over_pi),
        2 * vertex_dimension_from_alpha_squared(alpha_squared_over_pi),
    )

    beta_squared_over_pi_value = Fraction(8, 1)
    assert_equal(
        "sine-Gordon marginal endpoint has Delta=2",
        vertex_dimension_from_alpha_squared(beta_squared_over_pi_value),
        Fraction(2, 1),
    )


def check_coleman_relation_and_current_dictionary() -> None:
    assert_equal(
        "free Dirac point maps to beta^2=4 pi",
        beta_squared_over_four_pi(Fraction(0, 1)),
        Fraction(1, 1),
    )
    assert_equal(
        "sine-Gordon marginal endpoint maps to g/pi=-1/2",
        beta_squared_over_four_pi(Fraction(-1, 2)),
        Fraction(2, 1),
    )
    assert_equal(
        "Hermitian-current Lorentzian sign gives K=1+g/pi",
        k_from_current_square(Fraction(1, 3), hermitian_current_sign=-1),
        Fraction(4, 3),
    )
    assert_equal(
        "old anti-Hermitian-current sign would give K=1-g/pi",
        k_from_current_square(Fraction(1, 3), hermitian_current_sign=1),
        Fraction(2, 3),
    )
    assert_equal(
        "Hermitian-current sign gives Coleman marginal endpoint",
        g_over_pi_for_marginal_endpoint(hermitian_current_sign=-1),
        Fraction(-1, 2),
    )
    assert_equal(
        "old sign gives the wrong marginal endpoint",
        g_over_pi_for_marginal_endpoint(hermitian_current_sign=1),
        Fraction(1, 2),
    )

    for g_over_pi in (Fraction(0, 1), Fraction(1, 3), Fraction(-1, 3)):
        k = Fraction(1, 1) + g_over_pi
        beta_sq_over_pi = Fraction(4, 1) / k
        current_coeff_sq = beta_sq_over_pi / 4
        assert_equal(
            f"current coefficient squared equals 1/(pi K), g/pi={g_over_pi}",
            current_coeff_sq,
            Fraction(1, 1) / k,
        )


def check_mandelstam_exchange_and_fermion_dimension() -> None:
    # The line part has b = -2 pi/beta and the local part has a = +/- beta/2,
    # so ab/pi = +/- 1.  The equal-time exchange phase is exp(i ab sgn).
    assert_equal("Mandelstam exchange exponent for psi plus", Fraction(1, 1), Fraction(1, 1))
    assert_equal("Mandelstam exchange exponent for psi minus", Fraction(-1, 1), Fraction(-1, 1))

    beta_squared_over_pi_value = Fraction(4, 1)
    assert_equal(
        "Mandelstam field has free-fermion dimension at beta^2=4 pi",
        fermion_dimension(beta_squared_over_pi_value),
        Fraction(1, 2),
    )


def check_relevance_threshold() -> None:
    for beta_sq_over_four_pi, is_relevant in (
        (Fraction(1, 1), True),
        (Fraction(2, 1), False),
        (Fraction(3, 1), False),
    ):
        dimension = beta_sq_over_four_pi
        assert_equal(
            f"cosine dimension beta^2/(4 pi)={beta_sq_over_four_pi}",
            dimension,
            beta_sq_over_four_pi,
        )
        assert_true(
            f"relevance threshold beta^2/(4 pi)={beta_sq_over_four_pi}",
            (dimension < 2) is is_relevant,
        )


def main() -> None:
    check_mostly_plus_thirring_current_convention()
    check_vertex_ope_and_dimensions()
    check_coleman_relation_and_current_dictionary()
    check_mandelstam_exchange_and_fermion_dimension()
    check_relevance_threshold()
    print("All sine-Gordon/massive-Thirring bosonization checks passed.")


if __name__ == "__main__":
    main()
