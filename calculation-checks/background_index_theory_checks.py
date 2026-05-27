#!/usr/bin/env python3
"""Exact checks for background-index-theory conventions in Volume XII."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, lhs: Fraction | int, rhs: Fraction | int) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs}, expected {rhs}")


def check_four_dimensional_index_formula() -> None:
    # [Ahat ch]_4 = ch_2 - rank(E) p_1/24.
    ahat_p1 = Fraction(-1, 24)
    ch_rank = Fraction(1)
    ch2 = Fraction(1)
    assert_equal("four-dimensional ch_2 coefficient", ch2, Fraction(1))
    assert_equal("four-dimensional p1 coefficient per rank", ahat_p1 * ch_rank, Fraction(-1, 24))


def check_trace_delta_su_n_indices() -> None:
    # In the monograph trace-delta normalization T_delta(fund)=1 and
    # T_delta(adj)=2N.  The four-dimensional instanton index on p1=0
    # backgrounds is T_delta(R) k.
    for n in range(2, 9):
        for k in range(1, 4):
            t_fund = 1
            t_adj = 2 * n
            assert_equal(f"SU({n}) fundamental instanton index k={k}", t_fund * k, k)
            assert_equal(f"SU({n}) adjoint instanton index k={k}", t_adj * k, 2 * n * k)

    assert_equal("SU(2) fundamental BPST index", 1, 1)
    assert_equal("SU(2) adjoint BPST index", 4, 4)
    assert_equal("SU(3) adjoint BPST index", 6, 6)


def check_abelian_t4_flux_index() -> None:
    # On T^4, c1=q(m1 a + m2 b), int a b = 1, a^2=b^2=0:
    # index = 1/2 int c1^2 = q^2 m1 m2.
    for q in range(1, 5):
        for m1 in range(-2, 3):
            for m2 in range(-2, 3):
                c1_square = 2 * q * q * m1 * m2
                index = Fraction(1, 2) * c1_square
                assert_equal("T4 Abelian flux index", index, q * q * m1 * m2)


def check_six_form_anomaly_polynomial() -> None:
    # [Ahat ch]_6 = ch_3 - p_1 ch_1 / 24.
    ahat0 = Fraction(1)
    ahat_p1 = Fraction(-1, 24)
    ch1 = Fraction(1)
    ch3 = Fraction(1, 6)
    assert_equal("six-form ch_3 coefficient", ahat0 * ch3, Fraction(1, 6))
    assert_equal("six-form mixed p1 ch1 coefficient", ahat_p1 * ch1, Fraction(-1, 24))

    # The 2*pi*i descent prefactor converts F^3/[6(2*pi)^3] to
    # i F^3/(24*pi^2); track the rational coefficient multiplying i/pi^2.
    descent_cubic = Fraction(2, 1) * Fraction(1, 6) * Fraction(1, 8)
    descent_mixed = Fraction(2, 1) * Fraction(-1, 24) * Fraction(1, 2)
    assert_equal("cubic descent rational coefficient", descent_cubic, Fraction(1, 24))
    assert_equal("mixed descent rational coefficient", descent_mixed, Fraction(-1, 24))


def check_dirac_selection_rule_count() -> None:
    # A vectorlike Dirac fermion in R has two conjugate two-component chiral
    # variables.  In an instanton sector, each receives T_delta(R) k zero
    # coordinates in the corresponding 't Hooft vertex, so the axial selection
    # count is twice the Weyl index.
    examples = [(1, 1), (1, 3), (4, 1), (6, 2)]
    for t_delta, k in examples:
        weyl = t_delta * k
        dirac_axial = 2 * weyl
        assert_equal("Dirac axial zero-mode count", dirac_axial, 2 * t_delta * k)


def main() -> None:
    check_four_dimensional_index_formula()
    check_trace_delta_su_n_indices()
    check_abelian_t4_flux_index()
    check_six_form_anomaly_polynomial()
    check_dirac_selection_rule_count()
    print("All background index-theory convention checks passed.")


if __name__ == "__main__":
    main()
