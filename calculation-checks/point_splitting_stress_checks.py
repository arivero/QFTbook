#!/usr/bin/env python3
"""Finite checks for the point-split stress-tensor chapter.

Evidence contract.
Target claims: the Volume XII point-splitting chapter constructs a conserved
scalar stress tensor from the Hadamard smooth remainder, uses the
equation-of-motion improvement needed by the local parametrix defect,
classifies only weakly regular almost-homogeneous local freedom, computes the
flat thermal stress tensor, fixes the de Sitter conformal-anomaly diagnostic,
and uses the convention-correct scalar trace identity.
Independent construction: symbolic flat Synge identities, exact rational
Hadamard-recursion coefficients, finite divergence-defect bookkeeping for the
``eta_D = D/[2(D+2)]`` improvement, dimension/regularity filters for local
counterterms, constant-curvature reductions of the curvature-squared Euler
tensors, and trace-identity regression cases.
Imported assumptions: the analytic Hadamard recursion and Moretti/Hollands-
Wald conservation identity for the smooth parametrix defect.  The finite
checks verify the algebraic shape and negative controls, not the microlocal
existence theorem.
Negative controls: the naive point-split operator with the improvement
omitted is not conserved in the defect model, the old trace formula has the
wrong massive minimal sign and wrong improvement coefficient, and dimension
counting alone is not accepted as a proof of finite local freedom.
Scope boundary: these checks do not prove the analytic Hadamard coefficient
identities, the Hollands-Wald classification theorem, or existence of
operator-valued stress tensors on a common domain.
"""

from fractions import Fraction

import mpmath as mp
import sympy as sp


mp.mp.dps = 60


def assert_close(name, lhs, rhs, tol=mp.mpf("1e-45")):
    lhs = mp.mpf(lhs)
    rhs = mp.mpf(rhs)
    if not mp.isfinite(lhs) or not mp.isfinite(rhs):
        raise AssertionError(f"{name}: nonfinite value {lhs} or {rhs}")
    if not mp.isfinite(tol) or tol < 0:
        raise AssertionError(f"{name}: invalid tolerance {tol}")
    scale = max(mp.mpf(1), abs(lhs), abs(rhs))
    error = abs(lhs - rhs)
    threshold = tol * scale
    if not mp.isfinite(error) or not mp.isfinite(threshold):
        raise AssertionError(f"{name}: nonfinite comparison error")
    if error > threshold:
        raise AssertionError(f"{name}: {lhs} != {rhs}")


def assert_equal(name, lhs, rhs):
    if lhs != rhs:
        raise AssertionError(f"{name}: {lhs} != {rhs}")


def check_flat_hadamard_transport_identity():
    z0, z1, z2, z3 = sp.symbols("z0 z1 z2 z3")
    coordinates = [z0, z1, z2, z3]
    inverse_metric = [-1, 1, 1, 1]
    sigma = sp.Rational(1, 2) * (-z0**2 + z1**2 + z2**2 + z3**2)

    grad_sigma_squared = sum(
        inverse_metric[index] * sp.diff(sigma, coordinate) ** 2
        for index, coordinate in enumerate(coordinates)
    )
    box_sigma = sum(
        inverse_metric[index] * sp.diff(sigma, coordinate, 2)
        for index, coordinate in enumerate(coordinates)
    )

    assert_equal("flat Synge identity", sp.simplify(grad_sigma_squared - 2 * sigma), 0)
    assert_equal("flat box sigma", sp.simplify(box_sigma), 4)

    u_h = sp.Integer(1)
    leading_transport = (
        2
        * sum(
            inverse_metric[index] * sp.diff(sigma, coordinate) * sp.diff(u_h, coordinate)
            for index, coordinate in enumerate(coordinates)
        )
        + (box_sigma - 4) * u_h
    )
    assert_equal("flat Hadamard U transport", sp.simplify(leading_transport), 0)

    m_squared = sp.symbols("m_squared")
    v0_flat = m_squared / 2
    first_log_transport = (
        2
        * sum(
            inverse_metric[index] * sp.diff(sigma, coordinate) * sp.diff(v0_flat, coordinate)
            for index, coordinate in enumerate(coordinates)
        )
        + (box_sigma - 2) * v0_flat
        - m_squared
    )
    assert_equal("flat Hadamard v0 transport", sp.simplify(first_log_transport), 0)


def check_hadamard_v0_coincidence_formula():
    m_squared, xi, scalar_curvature = sp.symbols("m_squared xi scalar_curvature")
    box_sigma_diagonal = sp.Integer(4)
    p_u_diagonal = m_squared + (xi - sp.Rational(1, 6)) * scalar_curvature
    v0_diagonal = sp.Rational(1, 2) * p_u_diagonal

    assert_equal(
        "Hadamard v0 diagonal transport",
        sp.simplify((box_sigma_diagonal - 2) * v0_diagonal - p_u_diagonal),
        0,
    )
    assert_equal(
        "massless conformal v0 diagonal",
        sp.simplify(v0_diagonal.subs({m_squared: 0, xi: sp.Rational(1, 6)})),
        0,
    )


def check_flat_hadamard_logarithmic_recursion():
    # In flat space with constant coefficients, Box sigma = 4 and
    # P v_j = m^2 v_j.  The recursion gives
    # (4 + 2j) v_{j+1} = m^2 v_j/(j+1).
    m_squared = sp.symbols("m_squared")
    coefficients = [
        m_squared / 2,
        m_squared**2 / 8,
        m_squared**3 / 96,
        m_squared**4 / 2304,
    ]
    for j in range(len(coefficients) - 1):
        lhs = (4 + 2 * j) * coefficients[j + 1]
        rhs = m_squared * coefficients[j] / (j + 1)
        assert_equal(f"flat Hadamard logarithmic recursion v_{j + 1}", sp.simplify(lhs - rhs), 0)


def check_wald_finite_freedom_dimensions():
    dim_m = 1
    dim_curvature = 2
    dim_metric = 0
    dim_derivative = 1
    target_stress_dimension = 4

    term_dimensions = {
        "m^4 g_munu": 4 * dim_m + dim_metric,
        "m^2 G_munu": 2 * dim_m + dim_curvature,
        "variation R^2": 2 * dim_curvature,
        "variation Ricci^2": 2 * dim_curvature,
        "Box R trace term": 2 * dim_derivative + dim_curvature,
    }
    for name, dimension in term_dimensions.items():
        assert_equal(f"Wald local freedom dimension {name}", dimension, target_stress_dimension)


def check_curvature_squared_euler_tensor_traces():
    dimension = 4
    r_squared_trace_coefficient = 2 - Fraction(dimension, 2)
    r_squared_box_coefficient = 2 * dimension - 2
    ricci_squared_trace_coefficient = 2 - Fraction(dimension, 2)
    ricci_squared_box_coefficient = -Fraction(dimension, 2)

    assert_equal("R^2 Euler tensor algebraic trace coefficient", r_squared_trace_coefficient, 0)
    assert_equal("R^2 Euler tensor Box R trace coefficient", r_squared_box_coefficient, 6)
    assert_equal("Ricci^2 Euler tensor algebraic trace coefficient", ricci_squared_trace_coefficient, 0)
    assert_equal("Ricci^2 Euler tensor Box R trace coefficient", ricci_squared_box_coefficient, -2)


def check_point_split_conservation_improvement():
    dimension = 4
    eta_d = Fraction(dimension, 2 * (dimension + 2))
    assert_equal("four-dimensional point-split improvement eta", eta_d, Fraction(1, 3))

    # Finite model of the divergence identity after the Hadamard coefficient
    # lemma has reduced the parametrix defect to one local covector.  The
    # naive polarized Hilbert tensor leaves the displayed local defect; the
    # eta_D equation-of-motion line cancels it.
    parametrix_defect_gradient = Fraction(6)
    naive_divergence = -eta_d * parametrix_defect_gradient
    improved_divergence = naive_divergence + eta_d * parametrix_defect_gradient
    assert_equal("improved point-split divergence", improved_divergence, 0)
    if naive_divergence == 0:
        raise AssertionError("naive point-split tensor should retain the parametrix defect")

    wrong_eta = Fraction(1, 4)
    wrong_divergence = naive_divergence + wrong_eta * parametrix_defect_gradient
    if wrong_divergence == 0:
        raise AssertionError("wrong equation-of-motion coefficient accidentally conserved")


def check_local_freedom_regularity_filter():
    # Every term m^(4-2n) R^n has engineering dimension four, so dimension
    # counting alone would allow an infinite tower.  Smooth dependence at
    # m^2=0 and almost-homogeneous scaling retain only n=0,1,2.
    accepted = []
    rejected = []
    for curvature_power in range(6):
        mass_power = 4 - 2 * curvature_power
        engineering_dimension = mass_power + 2 * curvature_power
        assert_equal(
            f"dimension-alone tower n={curvature_power}",
            engineering_dimension,
            4,
        )
        if mass_power >= 0:
            accepted.append((mass_power, curvature_power))
        else:
            rejected.append((mass_power, curvature_power))

    assert_equal("regular local tensor powers", accepted, [(4, 0), (2, 1), (0, 2)])
    if not rejected:
        raise AssertionError("regularity filter failed to reject nonpolynomial tail")


def check_constant_curvature_finite_terms_vanish_massless():
    dimension = 4
    scalar_curvature = sp.symbols("R")
    ricci_eigenvalue = scalar_curvature / dimension
    ricci_squared = scalar_curvature**2 / dimension

    i_constant_curvature = 2 * scalar_curvature * ricci_eigenvalue - sp.Rational(1, 2) * scalar_curvature**2
    j_constant_curvature = (
        2 * scalar_curvature**2 / dimension**2
        - sp.Rational(1, 2) * ricci_squared
    )

    assert_equal("I_munu on four-dimensional constant curvature", sp.simplify(i_constant_curvature), 0)
    assert_equal("J_munu on four-dimensional constant curvature", sp.simplify(j_constant_curvature), 0)

    m_squared = sp.symbols("m_squared")
    assert_equal("massless m^4 finite term", (m_squared**2).subs(m_squared, 0), 0)
    assert_equal("massless m^2 finite term", m_squared.subs(m_squared, 0), 0)


def check_scalar_trace_identity_regressions():
    def xi_conformal(dimension):
        return Fraction(dimension - 2, 4 * (dimension - 1))

    def corrected_coefficients(dimension, xi):
        xi_c = xi_conformal(dimension)
        return Fraction(-1), (dimension - 1) * (xi - xi_c)

    def old_coefficients(dimension, xi):
        xi_c = xi_conformal(dimension)
        return Fraction(1), xi - xi_c

    cases = {
        "minimal massive D4": (4, Fraction(0), Fraction(-1), Fraction(-1, 2)),
        "conformal massive D4": (4, Fraction(1, 6), Fraction(-1), Fraction(0)),
        "minimal massless D4": (4, Fraction(0), Fraction(-1), Fraction(-1, 2)),
        "conformal massless D4": (4, Fraction(1, 6), Fraction(-1), Fraction(0)),
        "minimal D3": (3, Fraction(0), Fraction(-1), Fraction(-1, 4)),
    }

    for name, (dimension, xi, expected_mass, expected_box) in cases.items():
        mass_coeff, box_coeff = corrected_coefficients(dimension, xi)
        assert_equal(f"{name} trace mass coefficient", mass_coeff, expected_mass)
        assert_equal(f"{name} trace box coefficient", box_coeff, expected_box)

    old_mass, old_box = old_coefficients(4, Fraction(0))
    if old_mass == Fraction(-1) or old_box == Fraction(-1, 2):
        raise AssertionError("old minimal massive trace formula was not rejected")


def main():
    check_flat_hadamard_transport_identity()
    check_hadamard_v0_coincidence_formula()
    check_flat_hadamard_logarithmic_recursion()
    check_wald_finite_freedom_dimensions()
    check_curvature_squared_euler_tensor_traces()
    check_point_split_conservation_improvement()
    check_local_freedom_regularity_filter()
    check_constant_curvature_finite_terms_vanish_massless()
    check_scalar_trace_identity_regressions()

    w_state = Fraction(7, 5)
    w_prime_state = Fraction(11, 13)
    h_singular = Fraction(2, 3)
    smooth_shift = Fraction(5, 17)
    scale_shift = Fraction(19, 23)
    wick_state = w_state - h_singular
    wick_prime_state = w_prime_state - h_singular
    wick_shifted_subtraction = w_state - (h_singular + smooth_shift)
    wick_scale_shifted = w_state - (h_singular + scale_shift)
    assert_equal("point-split state difference", wick_state - wick_prime_state, w_state - w_prime_state)
    assert_equal("point-split smooth subtraction sign", wick_shifted_subtraction, wick_state - smooth_shift)
    assert_equal("Hadamard scale-change subtraction sign", wick_scale_shifted, wick_state - scale_shift)

    bose_integral = mp.quad(lambda x: x**3 / mp.expm1(x), [0, mp.inf])
    assert_close("Bose integral", bose_integral, mp.pi**4 / 15)

    for beta in [mp.mpf("0.7"), mp.mpf("1.0"), mp.mpf("2.3")]:
        rho = (1 / (2 * mp.pi**2)) * beta**(-4) * bose_integral
        expected_rho = mp.pi**2 / (30 * beta**4)
        pressure = rho / 3

        assert_close("thermal energy density", rho, expected_rho)
        assert_close("massless flat trace", -rho + 3 * pressure, 0)

    # Plane-wave eigenvalues of the point-split differential operators.
    # D_00 gives omega^2 on each massless plane wave; D_ii gives k_i^2.
    for kx, ky, kz in [
        (mp.mpf("1.0"), mp.mpf("2.0"), mp.mpf("3.0")),
        (mp.mpf("0.4"), mp.mpf("-0.8"), mp.mpf("1.1")),
    ]:
        k_squared = kx**2 + ky**2 + kz**2
        omega = mp.sqrt(k_squared)
        d00 = (omega**2 + k_squared) / 2
        spatial_trace_part = (omega**2 - k_squared) / 2
        assert_close("D00 massless plane-wave eigenvalue", d00, omega**2)
        assert_close("on-shell spatial trace term", spatial_trace_part, 0)

    # Four-dimensional de Sitter curvature invariants with R=12 H^2.
    H = mp.mpf("1.37")
    riem_sq = 24 * H**4
    ricci_sq = 36 * H**4
    scalar_curvature = 12 * H**2
    euler_density = riem_sq - 4 * ricci_sq + scalar_curvature**2
    assert_close("de Sitter Euler density", euler_density, 24 * H**4)

    a_scalar = mp.mpf(1) / 360
    trace = -(a_scalar * euler_density) / (16 * mp.pi**2)
    stress_constant = trace / 4
    assert_close("conformal scalar de Sitter trace", trace, -H**4 / (240 * mp.pi**2))
    assert_close(
        "conformal scalar de Sitter stress constant",
        stress_constant,
        -H**4 / (960 * mp.pi**2),
    )

    print("All point-splitting stress-tensor checks passed.")


if __name__ == "__main__":
    main()
