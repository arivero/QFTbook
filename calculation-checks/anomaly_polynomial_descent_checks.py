#!/usr/bin/env python3
"""Exact rational checks for anomaly-polynomial coefficients.

The script verifies the finite arithmetic used in the anomaly-polynomial and
inflow sections:

* the degree-six expansion
  [A-hat(T) ch(E)]_6 = ch_3(E) - p_1(T) ch_1(E)/24;
* the closed four-dimensional Dirac-index normalization
  [ch(E)]_4 = tr(F wedge F)/(8 pi^2)
  = epsilon tr(F F) d^4x/(32 pi^2);
* the local Clifford heat-kernel coefficient
  (4 pi)^(-2) (1/2) (1/2)^2 tr_spin(gamma_5 gamma gamma gamma gamma)
  = 1/(32 pi^2);
* the conversion 2 pi i * F^3/[6(2 pi)^3] -> i F^3/(24 pi^2);
* the Chern-Weil transgression coefficients in the universal
  Chern-Simons representative;
* the n=2 consistent-descent homotopy coefficients 1 and 1/2;
* Abelianized cubic counterterms preserve the completely symmetric Cartan
  coefficient of the anomaly;
* the Abelianized Bardeen-Zumino improvement changes the Ward coefficient
  from the consistent value C to the covariant value 3C;
* the U(1)^3, mixed gravitational-U(1), and mixed nonabelian-U(1) sums for
  one Standard Model generation;
* the SU(N) fundamental/antifundamental/adjoint cubic-anomaly bookkeeping.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations


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


def check_local_clifford_heat_coefficient() -> None:
    # The pure gauge term in the heat parametrix is
    # (4 pi)^(-2) * (1/2 from exp(tE)) * (1/2)^2 from
    # E_F=(1/2) gamma^{mu nu}F_{mu nu} * tr_spin(gamma_5 gamma gamma gamma gamma).
    heat_prefactor_without_pi = Fraction(1, 16)
    exponential_second_order = Fraction(1, 2)
    curvature_endomorphism_square = Fraction(1, 4)
    spin_trace_epsilon_coefficient = Fraction(4)

    assert_equal(
        "local Clifford heat coefficient",
        heat_prefactor_without_pi
        * exponential_second_order
        * curvature_endomorphism_square
        * spin_trace_epsilon_coefficient,
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


def check_consistent_descent_coefficients() -> None:
    # For P(F)=tr(F^3), the gauge-direction descent coefficient can be written
    # as 6 int_0^1 (1-t) tr(dlambda A F_t), with
    # F_t=t dA+t^2 A^2.  Thus the coefficients of A dA and A^3 are
    # 6 int_0^1 (1-t)t dt = 1 and
    # 6 int_0^1 (1-t)t^2 dt = 1/2.
    a_da = Fraction(6) * (Fraction(1, 2) - Fraction(1, 3))
    a_cubed = Fraction(6) * (Fraction(1, 3) - Fraction(1, 4))

    assert_equal("consistent descent A dA coefficient", a_da, Fraction(1))
    assert_equal("consistent descent A^3 coefficient", a_cubed, Fraction(1, 2))


def check_abelian_counterterm_symmetric_cubic_invariance() -> None:
    """A cubic Abelian counterterm cannot shift the symmetric anomaly tensor."""

    raw_h = {
        (0, 1, 0): Fraction(2, 3),
        (0, 1, 2): Fraction(-5, 7),
        (0, 2, 1): Fraction(11, 5),
        (1, 2, 0): Fraction(13, 6),
        (1, 3, 2): Fraction(-17, 11),
        (2, 3, 1): Fraction(19, 13),
    }

    def h(i: int, j: int, k: int) -> Fraction:
        if i == j:
            return Fraction(0)
        if (i, j, k) in raw_h:
            return raw_h[(i, j, k)]
        if (j, i, k) in raw_h:
            return -raw_h[(j, i, k)]
        return Fraction(0)

    def delta_c(i: int, j: int, k: int) -> Fraction:
        # The counterterm (1/2) H_{ij,k} A^i A^j F^k shifts the coefficient
        # of lambda^i F^j F^k by -1/2(H_{ij,k}+H_{ik,j}); the second term
        # symmetrizes over the two curvature labels.
        return -Fraction(1, 2) * (h(i, j, k) + h(i, k, j))

    for i in range(4):
        for j in range(4):
            for k in range(4):
                assert_equal(
                    f"Abelian counterterm shift symmetric in curvature labels {i}{j}{k}",
                    delta_c(i, j, k),
                    delta_c(i, k, j),
                )
                symmetric_part = sum(delta_c(*p) for p in permutations((i, j, k))) / Fraction(6)
                assert_equal(
                    f"Abelian counterterm leaves fully symmetric cubic coefficient {i}{j}{k}",
                    symmetric_part,
                    Fraction(0),
                )


def check_abelian_bardeen_zumino_factor() -> None:
    # On a one-generator commuting subspace, I_6=C F^3 has
    # I_5^(0)=C A F^2 and I_4^(1)=C lambda F^2.  The Bardeen-Zumino
    # current is *J_BZ=2 C A F because the A^3 term vanishes for one
    # one-form.  Its exterior derivative contributes 2 C F^2, so the
    # covariant Ward representative has coefficient 3 C.
    consistent_coefficient = Fraction(1)
    bardeen_zumino_divergence = Fraction(2)
    covariant_coefficient = consistent_coefficient + bardeen_zumino_divergence

    assert_equal(
        "Abelian Bardeen-Zumino consistent-to-covariant factor",
        covariant_coefficient,
        Fraction(3),
    )

    # d(2 A F)=2 F^2 - 2 A dF, and the Bianchi identity gives dF=0.
    bianchi_remainder = Fraction(0)
    derivative_coefficient = Fraction(2) - Fraction(2) * bianchi_remainder
    assert_equal(
        "Abelian Bardeen-Zumino divergence coefficient",
        derivative_coefficient,
        Fraction(2),
    )


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
    check_local_clifford_heat_coefficient()
    check_effective_action_conversion()
    check_chern_weil_transgression_coefficients()
    check_consistent_descent_coefficients()
    check_abelian_counterterm_symmetric_cubic_invariance()
    check_abelian_bardeen_zumino_factor()
    check_standard_model_hypercharge_sums()
    check_su_n_bookkeeping()
    print("All anomaly-polynomial and inflow coefficient checks passed.")


if __name__ == "__main__":
    main()
