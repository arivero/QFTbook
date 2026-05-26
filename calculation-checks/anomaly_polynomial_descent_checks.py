#!/usr/bin/env python3
"""Exact rational checks for anomaly-polynomial coefficients.

The script verifies the finite arithmetic used in the anomaly-polynomial and
inflow sections:

* the degree-six expansion
  [A-hat(T) ch(E)]_6 = ch_3(E) - p_1(T) ch_1(E)/24;
* the conversion 2 pi i * F^3/[6(2 pi)^3] -> i F^3/(24 pi^2);
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


def check_effective_action_conversion() -> None:
    # 2 pi times 1/[6(2 pi)^3] = 1/(24 pi^2); only the rational coefficient
    # multiplying i/pi^2 is checked here.
    cubic_conversion = Fraction(2, 1) * Fraction(1, 6) * Fraction(1, 8)
    mixed_conversion = Fraction(2, 1) * Fraction(-1, 24) * Fraction(1, 2)

    assert_equal("U(1)^3 inflow rational coefficient", cubic_conversion, Fraction(1, 24))
    assert_equal("mixed gravitational-U(1) inflow rational coefficient", mixed_conversion, Fraction(-1, 24))


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
    check_effective_action_conversion()
    check_standard_model_hypercharge_sums()
    check_su_n_bookkeeping()
    print("All anomaly-polynomial and inflow coefficient checks passed.")


if __name__ == "__main__":
    main()
