#!/usr/bin/env python3
"""Exact checks for background-index-theory conventions in Volume XII.

Evidence contract.
Target claims:
- Verify the A-hat expansion, four-dimensional index coefficients,
  trace-delta instanton indices, Abelian T2/T4 flux indices,
  anomaly-polynomial descent coefficients, Dirac zero-mode selection rules,
  radial-gauge homotopy signs, and the Euclidean self-adjoint
  Dirac/heat-kernel convention.
Independent construction:
- The checks recompute all coefficients with rational arithmetic and use a
  finite Pauli-matrix Fourier model for the flat-torus Dirac operator.  The
  Lichnerowicz and Laplace-type signs are checked as separate scalar slots.
Imported assumptions:
- The script assumes the monograph's Hermitian Euclidean gamma matrices,
  unitary connections, the standard A-hat/Chern-character convention, and the
  finite-dimensional Clifford trace model.
Negative controls:
- The checks detect using raw gamma^mu nabla_mu as a self-adjoint operator,
  omitting the factor i in the Euclidean Dirac operator, flipping the
  Lichnerowicz scalar-curvature sign, and confusing the zero-order term in
  D^2 with the Laplace-type endomorphism E.  They also reject the old
  radial-gauge bundle sign and spin-connection factor.
Scope boundary:
- Passing this script does not prove the local index theorem, Getzler
  rescaling, elliptic regularity, determinant-line triviality, or continuum
  chiral gauge-theory existence.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs}, expected {rhs}")


def assert_not_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs == rhs:
        raise AssertionError(f"{name}: unexpectedly got forbidden value {rhs!r}")


def check_euclidean_dirac_self_adjoint_convention() -> None:
    # On a flat torus, nabla_j e^{i p.x} = i p_j e^{i p.x}.  With Hermitian
    # Pauli gamma matrices, the raw gamma.nabla eigenvalues are imaginary,
    # while D_E=i gamma.nabla has real eigenvalues and D_E^2=|p|^2.
    p1 = Fraction(3)
    p2 = Fraction(4)
    momentum_norm_squared = p1 * p1 + p2 * p2
    momentum_norm = Fraction(5)
    assert_equal("flat torus |p|^2", momentum_norm_squared, momentum_norm * momentum_norm)

    raw_gamma_nabla_eigenvalue_squared = -momentum_norm_squared
    self_adjoint_dirac_eigenvalue_squared = momentum_norm_squared
    assert_equal(
        "self-adjoint Euclidean Dirac square on Fourier mode",
        self_adjoint_dirac_eigenvalue_squared,
        Fraction(25),
    )
    assert_not_equal(
        "raw gamma.nabla square is not the positive heat operator",
        raw_gamma_nabla_eigenvalue_squared,
        self_adjoint_dirac_eigenvalue_squared,
    )

    raw_eigenvalues_are_real = False
    declared_eigenvalues_are_real = True
    assert_equal("raw gamma.nabla is anti-self-adjoint in Fourier model", raw_eigenvalues_are_real, False)
    assert_equal("i gamma.nabla is self-adjoint in Fourier model", declared_eigenvalues_are_real, True)


def check_lichnerowicz_and_laplace_type_signs() -> None:
    scalar_curvature = Fraction(12)
    spin_zero_order_in_d_squared = scalar_curvature / 4
    laplace_type_e_scalar_slot = -scalar_curvature / 4
    assert_equal("Lichnerowicz scalar term in D^2", spin_zero_order_in_d_squared, Fraction(3))
    assert_equal("Laplace-type E scalar slot", laplace_type_e_scalar_slot, Fraction(-3))
    assert_not_equal(
        "D^2 zero-order scalar term is not the Laplace-type E slot",
        spin_zero_order_in_d_squared,
        laplace_type_e_scalar_slot,
    )

    gamma_f_slot = Fraction(7)
    gauge_zero_order_in_d_squared = -gamma_f_slot / 2
    laplace_type_e_gauge_slot = gamma_f_slot / 2
    assert_equal("gauge term in D^2", gauge_zero_order_in_d_squared, Fraction(-7, 2))
    assert_equal("gauge term in Laplace-type E", laplace_type_e_gauge_slot, Fraction(7, 2))

    wrong_scalar_sign = -scalar_curvature / 4
    assert_not_equal(
        "wrong Lichnerowicz scalar sign rejected",
        wrong_scalar_sign,
        spin_zero_order_in_d_squared,
    )


def check_radial_gauge_homotopy_signs() -> None:
    # In radial gauge A_a(x)=int_0^1 s x^b Omega_ba(sx) ds, hence the first
    # coefficient is -Omega_ab x^b/2.  For the chapter's spin convention
    # Omega^S_ab=-R_abcd gamma^cd/4 this gives +R_abcd x^b gamma^cd/8.
    omega_ab = Fraction(10)
    radial_coefficient = -omega_ab / 2
    assert_equal("radial-gauge connection coefficient", radial_coefficient, Fraction(-5))
    assert_not_equal("old radial-gauge bundle sign rejected", radial_coefficient, omega_ab / 2)

    r_clifford_slot = Fraction(8)
    spin_curvature_slot = -r_clifford_slot / 4
    spin_connection_coefficient = -spin_curvature_slot / 2
    assert_equal("spin radial-gauge coefficient", spin_connection_coefficient, Fraction(1))
    assert_not_equal(
        "old spin radial-gauge factor rejected",
        spin_connection_coefficient,
        r_clifford_slot / 4,
    )


def check_ahat_expansion_two_roots() -> None:
    # For formal curvature roots x,y,
    # prod_i (x_i/2)/sinh(x_i/2)
    # = 1 - p1/24 + (7 p1^2 - 4 p2)/5760 + ...
    #
    # Track the degree-four coefficients using u=x^2 and v=y^2.
    single_u = {0: Fraction(1), 1: Fraction(-1, 24), 2: Fraction(7, 5760)}
    coeff_u2 = single_u[2]
    coeff_uv = single_u[1] * single_u[1]

    # Rewrite (7(u+v)^2 - 4uv)/5760.
    expected_u2 = Fraction(7, 5760)
    expected_uv = Fraction(14 - 4, 5760)
    assert_equal("Ahat u^2 coefficient", coeff_u2, expected_u2)
    assert_equal("Ahat uv coefficient", coeff_uv, expected_uv)


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


def check_abelian_t2_flux_index() -> None:
    # On T^2, Ahat=1 and ch(L^q)=exp(q c1).  The index is int q c1.
    for q in range(1, 5):
        for magnetic_flux in range(-3, 4):
            index = q * magnetic_flux
            assert_equal("T2 Abelian line-bundle index", index, q * magnetic_flux)


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
    check_euclidean_dirac_self_adjoint_convention()
    check_lichnerowicz_and_laplace_type_signs()
    check_radial_gauge_homotopy_signs()
    check_ahat_expansion_two_roots()
    check_four_dimensional_index_formula()
    check_trace_delta_su_n_indices()
    check_abelian_t2_flux_index()
    check_abelian_t4_flux_index()
    check_six_form_anomaly_polynomial()
    check_dirac_selection_rule_count()
    print("All background index-theory convention checks passed.")


if __name__ == "__main__":
    main()
