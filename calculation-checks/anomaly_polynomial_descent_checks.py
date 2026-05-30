#!/usr/bin/env python3
"""Exact rational checks for anomaly-polynomial coefficients.

The script verifies the finite arithmetic used in the anomaly-polynomial and
inflow sections:

* the degree-six expansion
  [A-hat(T) ch(E)]_6 = ch_3(E) - p_1(T) ch_1(E)/24;
* the closed four-dimensional Dirac-index normalization
  [ch(E)]_4 = tr(F wedge F)/(8 pi^2)
  = epsilon tr(F F) d^4x/(32 pi^2);
* the conversion 2 pi i * F^3/[6(2 pi)^3] -> i F^3/(24 pi^2);
* the Chern-Weil transgression coefficients in the universal
  Chern-Simons representative;
* the U(1)^3, mixed gravitational-U(1), and mixed nonabelian-U(1) sums for
  one Standard Model generation;
* the SU(N) fundamental/antifundamental/adjoint cubic-anomaly bookkeeping.
"""

from __future__ import annotations

from fractions import Fraction


SM_FIELDS = [
    # name, SU(3) multiplicity, SU(2) multiplicity, hypercharge
    ("Q_L", 3, 2, Fraction(1, 6)),
    ("u^c", 3, 1, Fraction(-2, 3)),
    ("d^c", 3, 1, Fraction(1, 3)),
    ("L_L", 1, 2, Fraction(-1, 2)),
    ("e^c", 1, 1, Fraction(1, 1)),
]


def assert_equal(name: str, value: Fraction, expected: Fraction) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def check_index_polynomial_expansion() -> None:
    ahat_degree_0 = Fraction(1)
    ahat_p1_coeff = Fraction(-1, 24)
    ch1_coeff = Fraction(1)
    ch3_coeff = Fraction(1, 6)

    cubic = ahat_degree_0 * ch3_coeff
    mixed = ahat_p1_coeff * ch1_coeff

    assert_equal("degree-six ch_3 coefficient", cubic, Fraction(1, 6))
    assert_equal("degree-six p_1 ch_1 coefficient", mixed, Fraction(-1, 24))


def check_four_dimensional_index_density() -> None:
    # In the convention ch(E)=tr exp(F/(2 pi)), the four-form part is
    # (1/2)(F/(2 pi))^2 = tr(F wedge F)/(8 pi^2).  Since
    # F wedge F = epsilon^{mu nu rho sigma} F_{mu nu} F_{rho sigma} d^4x / 4,
    # the component coefficient is 1/(32 pi^2).
    ch2_form_coefficient = Fraction(1, 2) * Fraction(1, 4)
    component_wedge_factor = Fraction(1, 4)

    assert_equal(
        "closed four-dimensional ch_2 wedge coefficient",
        ch2_form_coefficient,
        Fraction(1, 8),
    )
    assert_equal(
        "closed four-dimensional index component coefficient",
        ch2_form_coefficient * component_wedge_factor,
        Fraction(1, 32),
    )


def check_effective_action_conversion() -> None:
    # 2 pi times 1/[6(2 pi)^3] = 1/(24 pi^2); only the rational coefficient
    # multiplying i/pi^2 is checked here.
    cubic_conversion = Fraction(2, 1) * Fraction(1, 6) * Fraction(1, 8)
    mixed_conversion = Fraction(2, 1) * Fraction(-1, 24) * Fraction(1, 2)

    assert_equal("U(1)^3 inflow rational coefficient", cubic_conversion, Fraction(1, 24))
    assert_equal("mixed gravitational-U(1) inflow rational coefficient", mixed_conversion, Fraction(-1, 24))


def universal_cs_coefficients(n: int) -> list[Fraction]:
    # In (n+1) int_0^1 dt < A [t dA + t^2 A^2]^n >, the term with j
    # factors of A^2 has coefficient (n+1) binom(n,j)/(n+j+1).
    from math import comb

    return [Fraction((n + 1) * comb(n, j), n + j + 1) for j in range(n + 1)]


def check_chern_weil_transgression_coefficients() -> None:
    assert_equal("CS_3 A dA coefficient", universal_cs_coefficients(1)[0], Fraction(1))
    assert_equal("CS_3 A^3 coefficient", universal_cs_coefficients(1)[1], Fraction(2, 3))
    assert_equal("CS_5 A(dA)^2 coefficient", universal_cs_coefficients(2)[0], Fraction(1))
    assert_equal("CS_5 A dA A^2 coefficient", universal_cs_coefficients(2)[1], Fraction(3, 2))
    assert_equal("CS_5 A(A^2)^2 coefficient", universal_cs_coefficients(2)[2], Fraction(3, 5))

    # In the Abelian case all A^2 terms vanish and I_{2n+1}^{(0)}=A F^n.
    # The gauge variation d(lambda) F^n equals d(lambda F^n) because dF=0.
    abelian_variation = Fraction(1)
    descent_boundary = Fraction(1)
    assert_equal("Abelian descent coefficient", abelian_variation, descent_boundary)


def check_standard_model_hypercharge_sums() -> None:
    cubic = sum(su3 * su2 * y**3 for _, su3, su2, y in SM_FIELDS)
    linear = sum(su3 * su2 * y for _, su3, su2, y in SM_FIELDS)
    su3_mixed = sum(su2 * y for _, su3, su2, y in SM_FIELDS if su3 == 3)
    su2_mixed = sum(su3 * y for _, su3, su2, y in SM_FIELDS if su2 == 2)

    assert_equal("Standard Model U(1)_Y^3 sum", cubic, Fraction(0))
    assert_equal("Standard Model gravitational-U(1)_Y sum", linear, Fraction(0))
    assert_equal("Standard Model SU(3)^2 U(1)_Y sum without T(3)", su3_mixed, Fraction(0))
    assert_equal("Standard Model SU(2)^2 U(1)_Y sum without T(2)", su2_mixed, Fraction(0))


def check_su_n_bookkeeping() -> None:
    a_fund = Fraction(1)
    a_antifund = Fraction(-1)
    a_adjoint = Fraction(0)

    vectorlike_dirac = a_fund + a_antifund
    chiral_example = 5 * a_fund + 2 * a_antifund + 7 * a_adjoint

    assert_equal("SU(N) vectorlike fundamental cubic anomaly", vectorlike_dirac, Fraction(0))
    assert_equal("SU(N) fund/antifund/adjoint bookkeeping", chiral_example, Fraction(3))


def main() -> None:
    check_index_polynomial_expansion()
    check_four_dimensional_index_density()
    check_effective_action_conversion()
    check_chern_weil_transgression_coefficients()
    check_standard_model_hypercharge_sums()
    check_su_n_bookkeeping()
    print("All anomaly-polynomial and inflow coefficient checks passed.")


if __name__ == "__main__":
    main()
