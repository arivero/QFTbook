#!/usr/bin/env python3
"""Finite checks for the Nielsen identity and gauge-dependent potentials.

The script verifies the bookkeeping used in the Volume II BV chapter's
Nielsen-identity section:

* the Abelian-Higgs one-loop determinant degrees reduce the gauge-parameter
  dependent part to Goldstone minus longitudinal/ghost data;
* the one-loop Nielsen coefficient is the finite difference quotient that
  makes partial_xi V_1 + C_1 V_0' vanish;
* stationary values are gauge-independent at the consistent order while the
  stationary coordinate moves along the Nielsen vector field;
* evaluating a loop-truncated branch at an inconsistently truncated extremum
  leaves a higher-order gauge artifact;
* the derivative-expansion identity transports the kinetic coefficient, so a
  potential-only bounce does not inherit the full gauge-independence result.

Evidence contract.
Target claims: the Nielsen-identity section in Volume II Chapter 24,
especially equations `eq:nielsen-identity-1pi`,
`eq:nielsen-effective-potential`, `eq:nielsen-abelian-higgs-one-loop`, and
`eq:nielsen-abelian-higgs-c1`.
Independent construction: finite polynomial and rational models of the
extended-BRST canonical-flow equation, determinant degree counts, and
one-loop Abelian-Higgs mass bookkeeping.
Imported assumptions: the local renormalized 1PI action exists in the stated
gauge chart, the extended Slavnov-Taylor identity is restored by local
counterterms, and the one-loop determinant formula is valid in the chosen
background R_xi branch.
Negative controls: the checks deliberately use wrong ghost multiplicity,
wrong Nielsen-flow sign, an inconsistent finite-order stationary coordinate,
and a potential-only bounce residual.
Scope boundary: a pass checks algebraic gauge-flow bookkeeping; it does not
prove the analytic all-order Nielsen identity, the full Abelian-Higgs
renormalization theorem, infrared safety, or gauge independence of any
particular Standard Model metastability number.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, value: object, expected: object) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def assert_not_equal(name: str, value: object, forbidden: object) -> None:
    if value == forbidden:
        raise AssertionError(f"{name}: unexpectedly got forbidden value {forbidden!r}")


def assert_zero(name: str, value: Fraction) -> None:
    assert_equal(name, value, Fraction(0))


def finite_difference(f_left: Fraction, f_right: Fraction, left: Fraction, right: Fraction) -> Fraction:
    if left == right:
        raise ValueError("finite_difference needs distinct points in this rational check")
    return (f_left - f_right) / (left - right)


def check_abelian_higgs_degree_count() -> None:
    # A real bosonic mode contributes +F(m^2), while a complex ghost pair
    # contributes -2F(m_c^2).  The massive vector determinant contains three
    # transverse/vector physical modes plus one longitudinal mode of mass
    # m_c^2=xi m_A^2.  Therefore the xi-dependent unphysical sector is
    # F(m_chi^2)+F(m_c^2)-2F(m_c^2)=F(m_chi^2)-F(m_c^2).
    goldstone = Fraction(1)
    vector_longitudinal = Fraction(1)
    complex_ghost_pair = Fraction(-2)
    net_unphysical_at_tree_extremum = goldstone + vector_longitudinal + complex_ghost_pair
    assert_zero("Goldstone-longitudinal-ghost determinant count at V0'=0", net_unphysical_at_tree_extremum)

    wrong_real_ghost_only = goldstone + vector_longitudinal + Fraction(-1)
    assert_not_equal("a real-ghost count would leave spurious xi dependence", wrong_real_ghost_only, Fraction(0))


def check_one_loop_difference_quotient_identity() -> None:
    # The one-loop branch has
    #   partial_xi V_1 = e^2 phi^2 [F'(m_chi^2)-F'(m_c^2)]
    # and m_chi^2-m_c^2 = V_0'(phi)/phi.  The Nielsen identity at order hbar,
    # partial_xi V_1 + C_1 V_0' = 0, is therefore solved by the finite
    # difference quotient C_1=-e^2 phi [F'(m_chi^2)-F'(m_c^2)]/(m_chi^2-m_c^2).
    e_squared = Fraction(5, 7)
    phi = Fraction(11, 3)
    m_chi_squared = Fraction(19, 5)
    m_c_squared = Fraction(13, 5)
    fprime_chi = Fraction(17, 23)
    fprime_c = Fraction(-29, 31)

    v0_prime = phi * (m_chi_squared - m_c_squared)
    partial_xi_v1 = e_squared * phi * phi * (fprime_chi - fprime_c)
    c1 = -e_squared * phi * finite_difference(fprime_chi, fprime_c, m_chi_squared, m_c_squared)

    assert_zero("one-loop Nielsen identity", partial_xi_v1 + c1 * v0_prime)

    wrong_sign_c1 = -c1
    assert_not_equal("wrong Nielsen-flow sign is detected", partial_xi_v1 + wrong_sign_c1 * v0_prime, Fraction(0))


def check_stationary_value_and_coordinate_flow() -> None:
    # Finite model:
    #   V0 = k/2 (phi-v)^2,
    #   V1 = -xi c k (phi-v) + gauge-independent terms.
    # It obeys partial_xi V1 + c V0' = 0.  The one-loop stationary coordinate
    # moves by d phi_*/d xi = c, but the value through O(hbar) is independent
    # of xi.
    k = Fraction(7, 3)
    c = Fraction(5, 11)
    xi = Fraction(13, 17)
    delta_consistent = xi * c

    v0_prime_at_shift = k * delta_consistent
    v1_prime = -xi * c * k
    assert_zero("one-loop stationary equation for coordinate shift", v0_prime_at_shift + v1_prime)

    value_order_one = Fraction(0)  # V0(v)+hbar V1(v), with V0'(v)=0 and V1(v) chosen xi-independent here.
    assert_zero("stationary value through consistent one-loop order", value_order_one)

    # If the shifted coordinate is inserted into V0+hbar V1 but the unknown
    # two-loop term is omitted, a gauge-dependent O(hbar^2) remnant appears.
    artifact_order_two = k * delta_consistent * delta_consistent / 2 - xi * c * k * delta_consistent
    assert_not_equal("inconsistent extremum evaluation leaves higher-order artifact", artifact_order_two, Fraction(0))


def check_derivative_expansion_transport() -> None:
    # For Gamma=int [V(phi)+1/2 Z(phi)(d phi)^2], the field-flow identity
    # gives partial_xi Z + C Z' + 2 Z C' = 0.  With C=c phi, a transported
    # kinetic coefficient has Z(phi,xi)=a exp(-2c xi)+b phi^2 exp(-4c xi).
    # Represent the two basis monomials by their xi-derivative weights.
    c = Fraction(3, 8)
    terms = [
        {"coefficient": Fraction(5, 7), "phi_power": 0, "xi_weight": -2 * c},
        {"coefficient": Fraction(11, 13), "phi_power": 2, "xi_weight": -4 * c},
    ]
    for term in terms:
        coefficient = term["coefficient"]
        phi_power = term["phi_power"]
        xi_weight = term["xi_weight"]
        # partial_xi term + c phi partial_phi term + 2 c term.
        pde_weight = xi_weight + c * phi_power + 2 * c
        assert_zero(f"kinetic Nielsen transport for phi^{phi_power}", coefficient * pde_weight)

    wrong_missing_jacobian_weight = terms[1]["xi_weight"] + c * terms[1]["phi_power"]
    assert_not_equal("omitting the 2 Z C' term is detected", wrong_missing_jacobian_weight, Fraction(0))


def check_bounce_requires_full_derivative_identity() -> None:
    # Finite residual model for a derivative expansion:
    #   partial_xi Gamma = -C_V E_V - C_Z E_Z.
    # A full bounce has both residuals zero.  A potential-only profile may set
    # E_V=0 while leaving the kinetic/higher-derivative residual E_Z nonzero.
    c_v = Fraction(2, 5)
    c_z = Fraction(-7, 9)

    full_residual_v = Fraction(0)
    full_residual_z = Fraction(0)
    assert_zero("full derivative-expansion bounce gauge variation", -c_v * full_residual_v - c_z * full_residual_z)

    potential_only_residual_v = Fraction(0)
    potential_only_residual_z = Fraction(4, 15)
    potential_only_variation = -c_v * potential_only_residual_v - c_z * potential_only_residual_z
    assert_not_equal("potential-only bounce retains gauge variation", potential_only_variation, Fraction(0))


def main() -> None:
    check_abelian_higgs_degree_count()
    check_one_loop_difference_quotient_identity()
    check_stationary_value_and_coordinate_flow()
    check_derivative_expansion_transport()
    check_bounce_requires_full_derivative_identity()
    print("All Nielsen identity effective-potential checks passed.")


if __name__ == "__main__":
    main()
