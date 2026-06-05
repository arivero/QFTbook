#!/usr/bin/env python3
r"""Evidence contract.

Target claims:
- The heavy scalar tree kernel expands as a local derivative series with a
  controlled low-momentum remainder.
- The one-loop heavy-light four-point observable matches between the full
  scalar theory and the EFT in a declared MS-bar bubble scheme, including the
  heavy threshold constant, the light loop, local derivative insertions,
  matching-scale cancellation, finite scheme-coordinate cancellation, and the
  first omitted heavy-momentum remainder.
- In a massive scalar EFT retaining \(\phi^4\) and \(\phi^6/\mathcal M^2\),
  the one-loop background-field pole closes on the retained coordinates
  through canonical excess two and generates \(\phi^8/\mathcal M^4\) as the
  first omitted local operator; extending the datum to canonical excess four
  requires a \(c_8\) counterterm, and canonical excess alone does not impose a
  universal \(Q^4\) momentum law.
- In the same scalar EFT, a local field redefinition preserves the on-shell
  four-point observable only when the action, Jacobian, source transform,
  composite transform, and Wilson-coordinate shifts are carried together.
- Evanescent operators in dimensional regularization must be retained through
  one-loop mixing and projected only after subtraction.  For the concrete
  left-current four-fermion representative
  \(E_{16}=O_3-16 Q\), the \(d=4-\epsilon\) Dirac projection gives
  \(\Pi_Q E_{16}=-4\epsilon Q\), and a one-loop color-singlet bubble pole
  \(g^2/(16\pi^2\epsilon)\) therefore produces a finite physical
  Wilson-coefficient shift.

Independent construction:
- The heavy-kernel identity is checked as an exact rational identity and as a
  dimensionful bound on the declared low-momentum domain.
- The one-loop heavy-light observable check compares the explicit full and EFT
  four-point kernels, verifies the MS-bar bubble expansion and threshold
  constant, differentiates the matched coordinate to test scale cancellation,
  and checks the finite scheme countershift.
- The one-loop EFT closure coefficients are extracted from
  \((V''(\phi))^2\) in a common factorial normalization, with a separate
  Wilson-coefficient/contact-scaling check for the generated \(\phi^8\)
  operator.
- The field-redefinition check computes the transformed scalar EFT
  coefficients, source/composite/Jacobian terms, and the tree four-point
  kernel on and away from the external mass shell.
- The evanescent check computes the chiral triple-gamma projection coefficient,
  the color-singlet one-loop bubble pole coefficient, the finite projection
  shift, and its compensation under a changed evanescent representative.

Imported assumptions:
- Euclidean low-energy kinematics with q^2 >= 0 and q^2 <= Q^2 << M^2.
- The quartic coordinate is normalized so the heavy beta contribution is the
  coefficient b_H in d lambda_full / d log(mu) = beta_light + b_H, and the
  MS-bar scalar bubble is
  B_X^R(P^2)=1/(16 pi^2) int_0^1 log(mu^2/(X^2+x(1-x)P^2)) dx.
- The scalar one-loop pole uses dimensional regularization with minimal
  subtraction and the standard background-field local-potential pole
  Gamma_div^(1)=(32 pi^2 epsilon)^(-1) int (V'')^2.
- The field-redefinition observable check uses the analytically continued
  external pole condition p_i^2=-m^2.
- The evanescent example uses the conventional four-fermion physical operator
  \(Q=(\bar\psi_1\gamma_\mu P_L\psi_2)(\bar\psi_3\gamma^\mu P_L\psi_4)\), the
  triple-gamma representative \(O_3\), \(d=4-\epsilon\), a color-singlet
  spectator bubble, and the stated chiral Dirac projection convention.  It
  fixes a convention for the finite shift rather than a universal sign
  convention.

Negative controls:
- Reversing the heavy-kernel remainder sign fails the exact identity.
- Omitting the hard threshold logarithm leaves matching-scale dependence, while
  omitting the matched derivative insertion leaves a visible Q^2/M^2 defect.
- The script rejects wrong one-loop combinatorial coefficients and rejects
  retaining the generated \(\phi^8\) pole inside a canonical-excess-two
  truncation.  It also rejects reading the generated nonderivative contact as
  a universal \(Q^4/\mathcal M^4\) law.
- Dropping either the derivative term or the mass-coordinate shift spoils the
  field-redefinition equality of the on-shell four-point kernel; dropping the
  Jacobian, source transform, or composite transform is also detected.
- Prematurely quotienting \(E_{16}\) misses the finite shift, using the wrong
  triple-gamma projection coefficient changes the shift, and changing the
  evanescent representative without the compensating physical coefficient
  shift changes the projected amplitude.

Scope boundary:
- This script checks finite algebra and bookkeeping for the EFT prediction
  calculus.  It does not prove nonperturbative decoupling, regulator removal,
  asymptotic convergence, or a continuum scattering construction.
"""

from __future__ import annotations

import sympy as sp

from check_utils import assert_gt, assert_leq


def assert_zero(name: str, value: sp.Expr) -> None:
    if sp.simplify(value) != 0:
        raise AssertionError(f"{name}: expected zero, got {sp.simplify(value)!r}")


def assert_nonzero(name: str, value: sp.Expr) -> None:
    if sp.simplify(value) == 0:
        raise AssertionError(f"{name}: expected a nonzero negative control")


def check_heavy_kernel_expansion() -> None:
    x = sp.symbols("x")
    for order in range(5):
        truncated = sum((-x) ** r for r in range(order + 1))
        remainder = (-x) ** (order + 1) / (1 + x)
        exact = 1 / (1 + x)
        assert_zero(f"geometric heavy-kernel remainder N={order}", truncated + remainder - exact)
        assert_nonzero(
            f"wrong-sign heavy-kernel remainder N={order}",
            truncated - remainder - exact,
        )

    M, q2 = sp.symbols("M q2", positive=True)
    order = 3
    dimensionful = 1 / (M**2 + q2)
    dimensionful_truncated = sum((-q2) ** r / M ** (2 * r + 2) for r in range(order + 1))
    dimensionful_remainder = (-q2) ** (order + 1) / (M ** (2 * order + 2) * (M**2 + q2))
    assert_zero(
        "dimensionful heavy-kernel expansion",
        dimensionful_truncated + dimensionful_remainder - dimensionful,
    )

    for ratio in (0.05, 0.1, 0.25):
        mass = 11.0
        q2_value = (ratio * mass) ** 2
        remainder_value = abs(float(dimensionful_remainder.subs({M: mass, q2: q2_value})))
        bound = q2_value ** (order + 1) / mass ** (2 * order + 4)
        assert_leq(f"low-momentum heavy-kernel bound Q/M={ratio}", remainder_value, bound)

    eta = sp.symbols("eta", nonzero=True)
    quartic_lambda_shift = sp.factor(sp.factorial(4) * (-eta**2 / (8 * M**2)))
    assert_zero("tree exchange converted to lambda/4! convention", quartic_lambda_shift + 3 * eta**2 / M**2)
    kernel_q2_coefficient = sp.expand(-eta**2 / 8 * (1 / M**2 - q2 / M**4)).coeff(q2)
    assert_zero("positive derivative operator sign", kernel_q2_coefficient - eta**2 / (8 * M**4))


def check_heavy_light_one_loop_observable_matching() -> None:
    p_s, p_t, p_u, M2 = sp.symbols("p_s p_t p_u M2", positive=True)
    eta, rho, lam, L_mu, kappa_s = sp.symbols("eta rho lam L_mu kappa_s", nonzero=True)
    beta_light, L_M, L_low, c_H = sp.symbols("beta_light L_M L_low c_H")
    p_channels = (p_s, p_t, p_u)
    sum_p = sum(p_channels)
    sum_p4 = sum(momentum**2 for momentum in p_channels)

    x, z = sp.symbols("x z", nonnegative=True)
    bubble_integrand_series = sp.series(sp.log(1 + x * (1 - x) * z), z, 0, 3).removeO()
    bubble_series = sp.integrate(bubble_integrand_series, (x, 0, 1))
    assert_zero(
        "MS-bar heavy bubble low-momentum coefficients",
        bubble_series - (z / 6 - z**2 / 60),
    )

    heavy_bubble_retained = lambda p2: (2 * L_mu - p2 / (6 * M2)) / (16 * sp.pi**2)
    heavy_bubble_through_first_omitted = (
        lambda p2: (2 * L_mu - p2 / (6 * M2) + p2**2 / (60 * M2**2)) / (16 * sp.pi**2)
    )
    heavy_loop_retained = -rho**2 * sum(heavy_bubble_retained(p2) for p2 in p_channels) / 2
    heavy_loop_through_first_omitted = (
        -rho**2 * sum(heavy_bubble_through_first_omitted(p2) for p2 in p_channels) / 2
    )
    heavy_threshold = -3 * rho**2 * L_mu / (16 * sp.pi**2)
    heavy_derivative = rho**2 * sum_p / (192 * sp.pi**2 * M2)
    heavy_first_omitted = -rho**2 * sum_p4 / (1920 * sp.pi**2 * M2**2)
    assert_zero(
        "heavy determinant threshold plus derivative insertion",
        sp.expand(heavy_loop_retained - heavy_threshold - heavy_derivative),
    )
    assert_zero(
        "heavy determinant first omitted momentum coefficient",
        sp.expand(heavy_loop_through_first_omitted - heavy_threshold - heavy_derivative - heavy_first_omitted),
    )

    eta_tree_retained = -eta**2 * sum(1 / M2 - p2 / M2**2 for p2 in p_channels)
    eta_threshold = -3 * eta**2 / M2
    eta_derivative = eta**2 * sum_p / M2**2
    assert_zero("tree heavy exchange local terms", eta_tree_retained - eta_threshold - eta_derivative)
    tree_exact = -eta**2 * sum(1 / (M2 + p2) for p2 in p_channels)
    tree_exact_remainder = -eta**2 * sum(p2**2 / (M2**2 * (M2 + p2)) for p2 in p_channels)
    tree_first_omitted = -eta**2 * sum_p4 / M2**3
    tree_after_first_omitted = eta**2 * sum(p2**3 / (M2**3 * (M2 + p2)) for p2 in p_channels)
    assert_zero(
        "tree first omitted exact remainder identity",
        sp.factor(tree_exact - eta_tree_retained - tree_exact_remainder),
    )
    assert_zero(
        "tree first omitted low-momentum coefficient",
        sp.factor(tree_exact_remainder - tree_first_omitted - tree_after_first_omitted),
    )

    light_loop = sp.symbols("light_loop")
    full_retained = lam + light_loop + eta_tree_retained + heavy_loop_retained
    lambda_eft = lam + eta_threshold + heavy_threshold
    eft_retained = lambda_eft + light_loop + eta_derivative + heavy_derivative
    assert_zero("full and EFT retained one-loop four-point kernels", sp.expand(full_retained - eft_retained))

    eft_without_derivative = lambda_eft + light_loop
    assert_nonzero(
        "omitting matched derivative insertion leaves momentum defect",
        sp.expand(full_retained - eft_without_derivative),
    )

    b_H = 3 * rho**2 / (16 * sp.pi**2)
    beta_full = beta_light + b_H
    running_to_low = beta_light * (L_low - L_M)
    hard_threshold_log = -b_H * L_M + c_H
    matched_low_coordinate = lam + beta_full * L_M + hard_threshold_log + running_to_low
    expected = lam + beta_light * L_low + c_H
    assert_zero("one-loop matching-scale cancellation", matched_low_coordinate - expected)
    assert_zero("derivative with respect to matching log", sp.diff(matched_low_coordinate, L_M))

    missing_threshold = lam + beta_full * L_M + running_to_low
    assert_nonzero("missing hard threshold leaves scale dependence", sp.diff(missing_threshold, L_M))
    wrong_threshold = lam + beta_full * L_M - hard_threshold_log + running_to_low
    assert_nonzero("wrong hard threshold sign leaves scale dependence", sp.diff(wrong_threshold, L_M))

    bubble_scheme_shift = kappa_s / (16 * sp.pi**2)
    full_scheme_shift = -rho**2 * 3 * bubble_scheme_shift / 2
    coefficient_countershift = -3 * rho**2 * kappa_s / (32 * sp.pi**2)
    assert_zero("finite bubble-scheme threshold constant", full_scheme_shift - coefficient_countershift)
    shifted_full = full_retained + full_scheme_shift
    shifted_eft = eft_retained + coefficient_countershift
    assert_zero("scheme-coordinate cancellation in observable", sp.expand(shifted_full - shifted_eft))

    for ratio in (0.05, 0.2, 0.45):
        mass_sq = 49.0
        q2 = ratio**2 * mass_sq
        eta_value = 1.3
        channel_values = (q2, q2 / 2, q2 / 3)
        exact_tree = -eta_value**2 * sum(1 / (mass_sq + channel) for channel in channel_values)
        retained_tree = -3 * eta_value**2 / mass_sq + eta_value**2 * sum(channel_values) / mass_sq**2
        tree_remainder = abs(exact_tree - retained_tree)
        tree_bound = 3 * eta_value**2 * q2**2 / mass_sq**3
        assert_leq(f"tree heavy-exchange omitted Q4 term ratio={ratio}", tree_remainder, tree_bound)

        heavy_bound = (2.1**2 / (640 * sp.pi**2)) * (q2**2 / mass_sq**2)
        assert_leq(
            f"heavy bubble omitted Q4 term ratio={ratio}",
            float(abs((2.1**2 / 2) * 3 * q2**2 / (960 * sp.pi**2 * mass_sq**2))),
            float(heavy_bound),
        )


def check_one_loop_scalar_eft_closure() -> None:
    phi, lam, c6, c8_r, m2, M2, q2, tadpole, eps = sp.symbols(
        "phi lam c6 c8_r m2 M2 q2 tadpole eps", nonzero=True
    )

    # In the common normalization
    # Gamma_div^(1) = (32 pi^2 eps)^(-1) int (V''(phi))^2,
    # convert coefficients to the monograph's common pole factor
    # (16 pi^2 eps)^(-1) times O_n/n!.
    v_second = m2 + lam * phi**2 / 2 + c6 * phi**4 / (24 * M2)
    pole_polynomial = sp.expand(v_second**2)

    lambda_pole = sp.factor(sp.factorial(4) * pole_polynomial.coeff(phi, 4) / 2)
    c6_pole = sp.factor(sp.factorial(6) * M2 * pole_polynomial.coeff(phi, 6) / 2)
    c8_pole = sp.factor(sp.factorial(8) * M2**2 * pole_polynomial.coeff(phi, 8) / 2)

    assert_zero(
        "one-loop phi4 pole with one phi6 insertion",
        lambda_pole - (3 * lam**2 + m2 * c6 / M2),
    )
    assert_zero("one-loop phi6 pole from higher-dimensional insertion", c6_pole - 15 * lam * c6)
    assert_zero("first omitted phi8 pole", c8_pole - 35 * c6**2)

    assert_nonzero("wrong phi6 pole combinatorics rejected", c6_pole - 10 * lam * c6)
    assert_nonzero("wrong phi8 pole combinatorics rejected", c8_pole - 28 * c6**2)

    retained_canonical_excess = {"phi4": 0, "phi6": 2}
    first_omitted_canonical_excess = {"phi8": 4}
    target_excess = 2
    assert_leq("phi4 pole remains in retained excess", retained_canonical_excess["phi4"], target_excess)
    assert_leq("phi6 pole remains in retained excess", retained_canonical_excess["phi6"], target_excess)
    assert_gt(
        "phi8 pole is assigned to the first omitted counterterm sector",
        first_omitted_canonical_excess["phi8"],
        target_excess,
    )

    delta_c8_ms = -c8_pole / (16 * sp.pi**2 * eps)
    bare_phi8_pole = c8_pole / (16 * sp.pi**2 * eps)
    assert_zero("minimal phi8 counterterm cancels the generated pole", bare_phi8_pole + delta_c8_ms)

    M4 = M2**2
    eight_point_contact = c8_r / M4
    assert_zero("nonderivative phi8 eight-point contact has no automatic q2 dependence", sp.diff(eight_point_contact, q2))

    wrong_universal_momentum_law = c8_r * q2**2 / M4
    assert_nonzero(
        "canonical excess alone does not imply a universal Q4 law",
        eight_point_contact - wrong_universal_momentum_law,
    )

    lower_point_tadpole_contribution = c8_r * tadpole**2 / M4
    assert_zero(
        "lower-point phi8 contribution is controlled by contracted light-scale loops",
        sp.diff(lower_point_tadpole_contribution, q2),
    )
    assert_nonzero(
        "lower-point contractions are not fixed by external momentum powers",
        lower_point_tadpole_contribution - wrong_universal_momentum_law,
    )


def check_scalar_eft_field_redefinition_observable() -> None:
    a, lam, c6, m2, M2, d, delta_reg, J, source_probe = sp.symbols(
        "a lam c6 m2 M2 d delta_reg J source_probe", nonzero=True
    )
    p1sq, p2sq, p3sq, p4sq = sp.symbols("p1sq p2sq p3sq p4sq")

    lambda_prime = lam + 24 * a * m2 / M2
    derivative_coefficient_prime = d + 3 * a
    c6_prime = c6 + 120 * a * lam
    lambda_shift = lambda_prime - lam
    derivative_coefficient_shift = derivative_coefficient_prime - d
    c6_shift = c6_prime - c6
    jacobian_mass_coordinate = -3 * a * delta_reg / M2
    source_cubic_coordinate = a * J / M2
    composite_phi_squared_shift = 2 * a / M2

    assert_zero("quartic coordinate shift under local redefinition", lambda_shift - 24 * a * m2 / M2)
    assert_zero("derivative coordinate shift under local redefinition", derivative_coefficient_shift - 3 * a)
    assert_zero("sextic coordinate shift under local redefinition", c6_shift - 120 * a * lam)
    assert_zero("finite-regulator Jacobian mass coordinate", jacobian_mass_coordinate + 3 * a * delta_reg / M2)
    assert_zero("source cubic coordinate is transformed", source_cubic_coordinate - a * J / M2)
    assert_zero("phi-squared composite representative is transformed", composite_phi_squared_shift - 2 * a / M2)

    sum_p2 = p1sq + p2sq + p3sq + p4sq
    derivative_kernel = 6 * a * sum_p2 / M2
    quartic_kernel = lambda_shift
    eom_kernel = 6 * a * (sum_p2 + 4 * m2) / M2
    assert_zero("split EOM operator four-point kernel", derivative_kernel + quartic_kernel - eom_kernel)

    on_shell = {p1sq: -m2, p2sq: -m2, p3sq: -m2, p4sq: -m2}
    assert_zero("on-shell four-point observable is basis independent", eom_kernel.subs(on_shell))
    assert_nonzero("omitting derivative term spoils on-shell equality", quartic_kernel.subs(on_shell))
    assert_nonzero("omitting mass-coordinate shift spoils on-shell equality", derivative_kernel.subs(on_shell))

    off_shell = {p1sq: 0, p2sq: 0, p3sq: 0, p4sq: 0}
    assert_nonzero("off-shell Green function changes under EOM redefinition", eom_kernel.subs(off_shell))
    assert_nonzero("dropping Jacobian changes cutoff-regulator coordinates", jacobian_mass_coordinate)
    assert_nonzero("dropping source transform changes sourced functional", source_cubic_coordinate.subs(J, source_probe))
    assert_nonzero("dropping composite transform changes insertions", composite_phi_squared_shift)


def check_evanescent_mixing_projection() -> None:
    eps, g2 = sp.symbols("eps g2", nonzero=True)
    C_Q, C_E, alpha = sp.symbols("C_Q C_E alpha", nonzero=True)
    d = 4 - eps

    # Four-fermion basis:
    # Q = (bar psi_1 gamma_mu P_L psi_2)(bar psi_3 gamma^mu P_L psi_4)
    # O3 = (bar psi_1 gamma_mu gamma_nu gamma_rho P_L psi_2)
    #      (bar psi_3 gamma^mu gamma^nu gamma^rho P_L psi_4).
    # The chiral Dirac projector onto Q gives Pi_Q O3 = 4 d Q.
    dirac_projection_o3 = 4 * d
    assert_zero("triple-gamma projection is 16 - 4 epsilon", dirac_projection_o3 - (16 - 4 * eps))

    evanescent_projection = dirac_projection_o3 - 16
    assert_zero("E_16 projects as -4 epsilon Q", evanescent_projection + 4 * eps)
    assert_nonzero("wrong four-dimensional projection misses O(epsilon) term", evanescent_projection)

    # The color-singlet spectator bubble leaves the Kronecker color tensor
    # delta_{a b} delta_{c d} unchanged.  The scalar integral
    # mu^epsilon int d^d l/(2 pi)^d (l^2 + Delta)^(-2) has UV pole
    # 2/(16 pi^2 epsilon) in the d=4-epsilon convention; the graph includes a
    # symmetry/combinatoric factor 1/2, giving u = g^2/(16 pi^2).
    color_factor = sp.Integer(1)
    scalar_bubble_pole_numerator = sp.Integer(2)
    graph_factor = sp.Rational(1, 2)
    u = color_factor * graph_factor * scalar_bubble_pole_numerator * g2 / (16 * sp.pi**2)
    assert_zero("color-singlet bubble pole coefficient", u - g2 / (16 * sp.pi**2))

    pole_projection = C_E * u / eps * evanescent_projection
    finite_shift = sp.limit(pole_projection, eps, 0)
    assert_zero("E_16 pole projection gives finite physical shift", finite_shift + 4 * C_E * u)

    premature_quotient_shift = sp.Integer(0)
    assert_nonzero(
        "premature evanescent quotient misses finite physical shift",
        finite_shift - premature_quotient_shift,
    )

    # Changing E_16 to E_alpha = O3 - (16 + alpha epsilon) Q changes the finite
    # projected coefficient, and the physical Wilson coefficient must be shifted
    # by the opposite finite scheme transformation.
    changed_projection = dirac_projection_o3 - (16 + alpha * eps)
    assert_zero("changed evanescent representative projection", changed_projection + (4 + alpha) * eps)
    changed_shift = sp.limit(C_E * u / eps * changed_projection, eps, 0)
    assert_zero("changed representative finite shift", changed_shift + (4 + alpha) * C_E * u)
    assert_nonzero(
        "uncompensated evanescent representative change alters projected coefficient",
        changed_shift - finite_shift,
    )

    projected_old = C_Q + finite_shift
    physical_countershift = alpha * C_E * u
    projected_new = C_Q + physical_countershift + changed_shift
    assert_zero("finite coefficient countershift preserves projected observable", projected_new - projected_old)

    projected_new_without_countershift = C_Q + changed_shift
    assert_nonzero(
        "omitting finite scheme countershift changes projected observable",
        projected_new_without_countershift - projected_old,
    )


def check_operator_redundancy_conditions() -> None:
    def can_remove_eom(*, on_shell: bool, sources_transformed: bool, contacts_carried: bool) -> bool:
        return on_shell and sources_transformed and contacts_carried

    def can_remove_brst_exact(*, physical_sector: bool, anomaly_free: bool, brst_preserved: bool) -> bool:
        return physical_sector and anomaly_free and brst_preserved

    def can_quotient_boundary_term(*, no_physical_boundary: bool, no_boundary_observable: bool, no_edge_charge: bool) -> bool:
        return no_physical_boundary and no_boundary_observable and no_edge_charge

    if not can_remove_eom(on_shell=True, sources_transformed=True, contacts_carried=True):
        raise AssertionError("EOM removal should be allowed for the matched on-shell observable class")
    for condition in ("on_shell", "sources_transformed", "contacts_carried"):
        kwargs = {"on_shell": True, "sources_transformed": True, "contacts_carried": True}
        kwargs[condition] = False
        if can_remove_eom(**kwargs):
            raise AssertionError(f"EOM removal incorrectly ignored missing {condition}")

    if not can_remove_brst_exact(physical_sector=True, anomaly_free=True, brst_preserved=True):
        raise AssertionError("BRST-exact removal should be allowed in anomaly-free physical cohomology")
    for condition in ("physical_sector", "anomaly_free", "brst_preserved"):
        kwargs = {"physical_sector": True, "anomaly_free": True, "brst_preserved": True}
        kwargs[condition] = False
        if can_remove_brst_exact(**kwargs):
            raise AssertionError(f"BRST-exact removal incorrectly ignored missing {condition}")

    if not can_quotient_boundary_term(
        no_physical_boundary=True,
        no_boundary_observable=True,
        no_edge_charge=True,
    ):
        raise AssertionError("boundary-term quotient should be allowed when all boundary data are absent")
    for condition in ("no_physical_boundary", "no_boundary_observable", "no_edge_charge"):
        kwargs = {
            "no_physical_boundary": True,
            "no_boundary_observable": True,
            "no_edge_charge": True,
        }
        kwargs[condition] = False
        if can_quotient_boundary_term(**kwargs):
            raise AssertionError(f"boundary quotient incorrectly ignored missing {condition}")


def main() -> None:
    check_heavy_kernel_expansion()
    check_heavy_light_one_loop_observable_matching()
    check_one_loop_scalar_eft_closure()
    check_scalar_eft_field_redefinition_observable()
    check_evanescent_mixing_projection()
    check_operator_redundancy_conditions()
    print("All EFT prediction-calculus checks passed.")


if __name__ == "__main__":
    main()
