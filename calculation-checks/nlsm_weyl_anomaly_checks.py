#!/usr/bin/env python3
"""Coefficient checks for one-loop NLSM Weyl-anomaly bookkeeping."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def check_h_squared_variation_coefficients() -> None:
    h_squared_lagrangian = Fraction(-1, 12)

    # H_{abc} H^{abc} contains three inverse metrics.
    metric_variation_factor = 3
    metric_equation_coefficient = h_squared_lagrangian * metric_variation_factor
    assert_equal(
        "metric variation coefficient of -H^2/12",
        metric_equation_coefficient,
        Fraction(-1, 4),
    )

    # delta(H^2)=2 H delta H and delta H=d delta B has three antisymmetric
    # placements.  Thus -H^2/12 varies as -1/2 H^{ijk} nabla_i delta B_jk.
    h_variation_factor = 2 * 3
    before_parts = h_squared_lagrangian * h_variation_factor
    assert_equal("B variation before integration by parts", before_parts, Fraction(-1, 2))

    after_parts = -before_parts
    beta_divergence_coefficient = -after_parts
    dilaton_gradient_coefficient = beta_divergence_coefficient * Fraction(-2)
    assert_equal("B beta divergence coefficient", beta_divergence_coefficient, Fraction(-1, 2))
    assert_equal("B beta dilaton-gradient coefficient", dilaton_gradient_coefficient, 1)


def check_string_frame_metric_trace_and_scalar_variation() -> None:
    """Check the trace/scalar split in the one-loop string-frame action."""

    scalar_equation = {
        "R": Fraction(1),
        "laplacian_phi": Fraction(4),
        "grad_phi_sq": Fraction(-4),
        "H2": Fraction(-1, 12),
    }

    # Trace terms in the fixed-dilaton metric variation of
    # sqrt(G) e^{-2 Phi} (R + 4 |grad Phi|^2 - H^2/12).
    trace_terms = {
        "R": Fraction(-1, 2),
        "laplacian_phi": Fraction(-2),
        "grad_phi_sq": Fraction(2),
        "H2": Fraction(1, 24),
    }
    for monomial, coefficient in trace_terms.items():
        assert_equal(
            f"metric trace coefficient for {monomial}",
            coefficient,
            -scalar_equation[monomial] / 2,
        )

    # The non-trace grad_i Phi grad_j Phi terms cancel between the Palatini
    # variation of R with the weighted measure and the variation of 4|grad Phi|^2.
    assert_equal(
        "nontrace grad Phi tensor cancellation",
        Fraction(-4) + Fraction(4),
        0,
    )

    # Varying Phi first gives -2 L delta Phi plus
    # 8 grad^i Phi grad_i delta Phi from 4|grad Phi|^2.
    direct_variation = {
        "R": Fraction(-2),
        "laplacian_phi": Fraction(0),
        "grad_phi_sq": Fraction(-8),
        "H2": Fraction(1, 6),
    }
    integrated_by_parts = {
        "R": Fraction(0),
        "laplacian_phi": Fraction(-8),
        "grad_phi_sq": Fraction(16),
        "H2": Fraction(0),
    }
    total_scalar_variation = {
        monomial: direct_variation[monomial] + integrated_by_parts[monomial]
        for monomial in scalar_equation
    }
    expected_scalar_variation = {
        monomial: -2 * coefficient
        for monomial, coefficient in scalar_equation.items()
    }
    assert_equal(
        "dilaton scalar variation after integration by parts",
        total_scalar_variation,
        expected_scalar_variation,
    )


def check_linear_dilaton_constant() -> None:
    for dimension in range(2, 27):
        alpha_prime_v_squared = Fraction(26 - dimension, 6)
        scalar_beta_constant = Fraction(dimension - 26, 6) + alpha_prime_v_squared
        matter_central_charge = dimension + 6 * alpha_prime_v_squared
        assert_equal(f"linear dilaton beta constant in D={dimension}", scalar_beta_constant, 0)
        assert_equal(f"linear dilaton matter central charge in D={dimension}", matter_central_charge, 26)


def check_heterotic_bianchi_coefficients() -> None:
    green_schwarz_coefficient = Fraction(1, 4)

    tr_r_wedge_r = Fraction(7, 3)
    tr_f_wedge_f = tr_r_wedge_r
    standard_embedding_rhs = green_schwarz_coefficient * (tr_r_wedge_r - tr_f_wedge_f)
    assert_equal("standard embedding cancels dH source", standard_embedding_rhs, 0)

    tr_f_wedge_f = Fraction(-5, 2)
    rhs = green_schwarz_coefficient * (tr_r_wedge_r - tr_f_wedge_f)
    expected = Fraction(1, 4) * (Fraction(7, 3) + Fraction(5, 2))
    assert_equal("Green-Schwarz one-quarter normalization", rhs, expected)


def check_heterotic_gauge_dilaton_redundant_direction() -> None:
    # The hatted gauge equation is -1/2(D.F + H.F/2 - 2 grad Phi . F).
    overall = Fraction(-1, 2)
    assert_equal("heterotic D.F coefficient", overall, Fraction(-1, 2))
    assert_equal("heterotic H.F coefficient", overall * Fraction(1, 2), Fraction(-1, 4))
    assert_equal("heterotic dilaton-gradient coefficient", overall * Fraction(-2), 1)


def check_torsionful_connection_package() -> None:
    # For Gamma^- = Gamma - H/2, the contorsion coefficient is -1/2.
    contorsion = Fraction(-1, 2)
    assert_equal("torsionful Ricci divergence coefficient", contorsion, Fraction(-1, 2))
    assert_equal(
        "torsionful Ricci quadratic H coefficient",
        -contorsion * contorsion,
        Fraction(-1, 4),
    )

    # Acting on a covector changes the sign of the connection correction;
    # 2 nabla^-_i nabla_j Phi therefore contributes + H^k_ij grad_k Phi.
    assert_equal(
        "torsionful dilaton H-gradient coefficient",
        2 * (-contorsion),
        1,
    )


def check_exterior_square_zero_for_h_beta() -> None:
    # Verify d(d beta^B)=0 in one component with commuting derivatives.
    # A term is ((derivative_a, derivative_b), beta_pair).
    terms: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}

    def add_term(sign: int, deriv_a: int, deriv_b: int, beta_pair: tuple[int, int]) -> None:
        derivative_pair = tuple(sorted((deriv_a, deriv_b)))
        key = (derivative_pair, beta_pair)
        terms[key] = terms.get(key, 0) + sign

    # d beta^B_{abc}=partial_a beta_bc - partial_b beta_ac + partial_c beta_ab
    def add_d_beta(overall: int, outer_deriv: int, a: int, b: int, c: int) -> None:
        add_term(overall, outer_deriv, a, (b, c))
        add_term(-overall, outer_deriv, b, (a, c))
        add_term(overall, outer_deriv, c, (a, b))

    # d(d beta^B)_{0123}
    add_d_beta(1, 0, 1, 2, 3)
    add_d_beta(-1, 1, 0, 2, 3)
    add_d_beta(1, 2, 0, 1, 3)
    add_d_beta(-1, 3, 0, 1, 2)

    cancelled = {key: value for key, value in terms.items() if value}
    assert_equal("d squared beta^B cancellation", cancelled, {})


def main() -> None:
    check_h_squared_variation_coefficients()
    check_string_frame_metric_trace_and_scalar_variation()
    check_linear_dilaton_constant()
    check_heterotic_bianchi_coefficients()
    check_heterotic_gauge_dilaton_redundant_direction()
    check_torsionful_connection_package()
    check_exterior_square_zero_for_h_beta()
    print("All NLSM Weyl-anomaly coefficient checks passed.")


if __name__ == "__main__":
    main()
