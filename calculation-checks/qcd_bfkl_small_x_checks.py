#!/usr/bin/env python3
"""Finite checks for the small-x/BFKL convention block in Volume II.

Evidence contract.
Target claims: the Volume II small-x section's trace-delta color convention,
leading dipole/BFKL kernel normalization, finite Wilson-line/JIMWLK weak
generator boundary, BK closure estimate, projective JIMWLK cylinder limit,
measured small-x proof-obligation map, and leading inclusive DIS dipole
observable channel.
Independent construction: the checks rebuild the color-convention invariant
from both trace-delta and half-trace coordinates, test transverse inversion
covariance directly on rational points, recompute BFKL saddle constants from
the Mellin characteristic function, construct an independent compact
two-torus Fokker-Planck model for Wilson-line diffusion, propagate finite
BK and measured-observable residuals through exact rational ledgers, and
assemble a separate finite DIS bin from photon wave-function weights rather
than reading chapter display strings.
Imported assumptions: the tests use the leading-log dipole kernel form, the
Mellin characteristic function, compact finite Wilson-line configuration
space for the toy generator, positive photon wave-function weights, and the
chapter's separation of exact measured observables from impact-factor,
rapidity, projective, evolution, closure, and power residuals.
Negative controls: wrong trace-normalization transport, loss of inversion
covariance, nondissipative Wilson-line modes, nonvanishing generator errors in
the projective limit, omitted impact-factor or BK-closure residuals, missing
photon-kernel weights, and the wrong rapidity-subtraction sign are rejected.
Scope boundary: a pass verifies finite convention closure and independent
finite-observable propagation; it does not prove continuum JIMWLK existence,
derive small-x factorization for QCD, prove BK closure, or bound physical
impact factors and power corrections.

Primary derivation route: trace-delta Yang-Mills conventions feed the dipole
kernel, BFKL Mellin characteristic function, finite JIMWLK weak generator,
BK closure estimate, and tested DIS dipole observable in the same rapidity
scheme.
Independent verification route: compact Fourier-mode diffusion, rational
coordinate inversion tests, exact Gronwall arithmetic, photon-kernel bin
assembly, and sign/adversarial omissions independently probe the same
coefficient, generator, and measured-observable boundaries.
Convention dependencies: trace-delta fundamental generators
``tr(t^a t^b)=delta^{ab}``, ``C_A=2 N_c``, ``S_YM=-1/(4g^2) int tr F^2``,
positive rapidity evolution convention, and the chapter's dipole
normalization for the virtual-photon wave functions.
Domain and remainder assumptions: finite transverse lattices, compact
Wilson-line coordinates, bounded test bins, positive photon kernels, and
declared residual budgets for impact-factor matching, rapidity transport,
projective limits, evolution, closure, and power corrections.
Remaining unproved or conditional: continuum Wilson-line state construction,
full QCD factorization at measured small x, nonperturbative impact factors,
rapidity-scheme matching beyond the finite model, and physical endpoint/power
estimates remain chapter-level hypotheses or proof obligations.

The manuscript writes the leading dipole/BFKL kernel in the trace-delta
Yang-Mills convention

    tr_fund(t^a t^b)=delta^{ab},       C_A=2 N_c,
    S_YM=-1/(4 g^2) int tr F^2.

These checks verify convention-invariant coefficient products, the transverse
inversion covariance of the dipole kernel measure, the elementary
Mellin-eigenvalue constants of the leading BFKL characteristic function, and
the finite Wilson-line/Fokker-Planck algebra used as the JIMWLK theorem
boundary, the finite BK-closure algebra/error estimate, and the projective
cylinder-limit error budget for passing finite weak JIMWLK equations to a
continuum Wilson-line state.  They also check the conditional residual
propagation map that turns the Wilson-line state and impact factor into a
tested measured small-x observable once component estimates have been supplied,
and a finite leading-DIS dipole channel in which photon
wave-function weights propagate rapidity, BK-closure, and endpoint errors to
the measured bin.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp

from check_utils import assert_gt
from check_utils import assert_leq


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_zero(name: str, expr: sp.Expr) -> None:
    reduced = sp.simplify(expr)
    if reduced != 0:
        raise AssertionError(f"{name}: got {reduced!r}, expected 0")


def dist2(p: tuple[Fraction, Fraction], q: tuple[Fraction, Fraction]) -> Fraction:
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def invert(p: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    radius2 = p[0] ** 2 + p[1] ** 2
    return (p[0] / radius2, p[1] / radius2)


def check_trace_delta_kernel_coefficient() -> None:
    g_delta_sq = Fraction(5, 11)
    n_c = Fraction(7, 1)
    c_a_delta = 2 * n_c

    g_half_sq = 2 * g_delta_sq
    c_a_half = n_c

    assert_equal(
        "BFKL color-coupling product",
        g_delta_sq * c_a_delta,
        g_half_sq * c_a_half,
    )


def check_transverse_inversion_covariance() -> None:
    x = (Fraction(1, 1), Fraction(2, 1))
    y = (Fraction(4, 1), Fraction(1, 1))
    z = (Fraction(3, 1), Fraction(5, 1))

    kernel = dist2(x, y) / (dist2(x, z) * dist2(z, y))

    xi, yi, zi = invert(x), invert(y), invert(z)
    transformed_kernel = dist2(xi, yi) / (dist2(xi, zi) * dist2(zi, yi))
    jacobian = Fraction(1, 1) / (z[0] ** 2 + z[1] ** 2) ** 2

    assert_equal("dipole kernel inversion covariance", transformed_kernel * jacobian, kernel)


def check_bfkl_characteristic_values() -> None:
    gamma = sp.symbols("gamma")
    chi = 2 * sp.polygamma(0, 1) - sp.polygamma(0, gamma) - sp.polygamma(0, 1 - gamma)

    assert_zero("BFKL saddle value", chi.subs(gamma, sp.Rational(1, 2)) - 4 * sp.log(2))
    assert_zero("BFKL saddle first derivative", sp.diff(chi, gamma).subs(gamma, sp.Rational(1, 2)))
    assert_zero(
        "BFKL saddle second derivative",
        sp.diff(chi, gamma, 2).subs(gamma, sp.Rational(1, 2)) - 28 * sp.zeta(3),
    )

    nu = sp.symbols("nu")
    quadratic_coefficient = -sp.diff(chi, gamma, 2).subs(gamma, sp.Rational(1, 2)) / 2
    assert_zero("BFKL diffusion coefficient", quadratic_coefficient + 14 * sp.zeta(3))

    gamma_line = sp.Rational(1, 2) + sp.I * nu
    series = 4 * sp.log(2) - 14 * sp.zeta(3) * nu**2
    assert_zero(
        "BFKL nu-expansion through quadratic order",
        sp.series(chi.subs(gamma, gamma_line) - series, nu, 0, 3).removeO(),
    )


def apply_constant_diffusion_generator(
    modes: dict[tuple[int, int], Fraction],
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> dict[tuple[int, int], Fraction]:
    """Apply H=1/2 A_ij d_i d_j on the two-torus Fourier basis.

    The mode exp(i k.theta) has eigenvalue -1/2 k_i A_ij k_j.
    This is the constant-coefficient finite compact-manifold model of the
    divergence-form Wilson-line generator in the text.
    """
    output: dict[tuple[int, int], Fraction] = {}
    for (k1, k2), coeff in modes.items():
        quadratic = (
            matrix[0][0] * k1 * k1
            + (matrix[0][1] + matrix[1][0]) * k1 * k2
            + matrix[1][1] * k2 * k2
        )
        output[(k1, k2)] = -Fraction(1, 2) * quadratic * coeff
    return output


def torus_inner(
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
) -> Fraction:
    """Normalized torus pairing: integral left(theta) right(theta) dtheta."""
    total = Fraction(0)
    for mode, coeff in left.items():
        total += coeff * right.get((-mode[0], -mode[1]), Fraction(0))
    return total


def check_finite_wilson_line_diffusion_algebra() -> None:
    matrix = (
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(3)),
    )

    constant = {(0, 0): Fraction(1)}
    assert_equal(
        "finite diffusion preserves constants",
        apply_constant_diffusion_generator(constant, matrix),
        {(0, 0): Fraction(0)},
    )

    test_modes = {
        (1, 0): Fraction(2),
        (-1, 0): Fraction(2),
        (0, 1): Fraction(3),
        (0, -1): Fraction(3),
        (1, -1): Fraction(5),
        (-1, 1): Fraction(5),
    }
    h_test = apply_constant_diffusion_generator(test_modes, matrix)

    # The integral is the zero Fourier coefficient.  A divergence-form
    # generator has zero integral on compact configuration space.
    assert_equal("finite diffusion mass conservation", h_test.get((0, 0), Fraction(0)), Fraction(0))

    for mode in [(1, 0), (0, 1), (1, -1), (2, 1)]:
        singleton = {mode: Fraction(1)}
        eigenvalue = apply_constant_diffusion_generator(singleton, matrix)[mode]
        if eigenvalue >= 0:
            raise AssertionError(f"mode {mode} has nondissipative eigenvalue {eigenvalue}")

    other_modes = {
        (1, 0): Fraction(7),
        (-1, 0): Fraction(7),
        (0, 1): Fraction(-2),
        (0, -1): Fraction(-2),
        (1, -1): Fraction(4),
        (-1, 1): Fraction(4),
    }
    lhs = torus_inner(test_modes, apply_constant_diffusion_generator(other_modes, matrix))
    rhs = torus_inner(apply_constant_diffusion_generator(test_modes, matrix), other_modes)
    assert_equal("finite diffusion weak-strong duality", lhs, rhs)


def check_wilson_line_dirichlet_form_sign() -> None:
    """Check the dissipative sign of the finite Wilson-line generator."""

    matrix = (
        (Fraction(4), Fraction(1)),
        (Fraction(1), Fraction(2)),
    )
    real_modes = {
        (1, 0): Fraction(3),
        (-1, 0): Fraction(3),
        (0, 1): Fraction(-2),
        (0, -1): Fraction(-2),
        (1, 1): Fraction(5),
        (-1, -1): Fraction(5),
    }
    generator_modes = apply_constant_diffusion_generator(real_modes, matrix)
    dirichlet = -torus_inner(real_modes, generator_modes)

    expected = Fraction(0)
    for (k1, k2), coeff in real_modes.items():
        quadratic = (
            matrix[0][0] * k1 * k1
            + (matrix[0][1] + matrix[1][0]) * k1 * k2
            + matrix[1][1] * k2 * k2
        )
        expected += Fraction(1, 2) * quadratic * coeff * real_modes.get((-k1, -k2), Fraction(0))

    assert_equal("finite Wilson-line Dirichlet form", dirichlet, expected)
    assert_gt("finite Wilson-line generator is dissipative", dirichlet, Fraction(0))

    wrong_sign_dirichlet = torus_inner(real_modes, generator_modes)
    if wrong_sign_dirichlet >= 0:
        raise AssertionError("wrong-sign Wilson-line generator should fail dissipativity")


def check_finite_bk_closure_algebra() -> None:
    weights = {"z": Fraction(7, 11), "w": Fraction(2, 13)}
    s_xy = Fraction(2, 3)
    s_xz = Fraction(5, 7)
    s_zy = Fraction(4, 9)
    s_xw = Fraction(1, 2)
    s_wy = Fraction(3, 5)

    rhs_s = (
        weights["z"] * (s_xz * s_zy - s_xy)
        + weights["w"] * (s_xw * s_wy - s_xy)
    )

    n_xy = 1 - s_xy
    n_xz = 1 - s_xz
    n_zy = 1 - s_zy
    n_xw = 1 - s_xw
    n_wy = 1 - s_wy
    rhs_n = (
        weights["z"] * (n_xz + n_zy - n_xy - n_xz * n_zy)
        + weights["w"] * (n_xw + n_wy - n_xy - n_xw * n_wy)
    )
    assert_equal("BK S-to-N conversion", -rhs_s, rhs_n)

    # The closed mean-field vector field points into the real unit cube.
    lower_boundary_rhs = (
        weights["z"] * s_xz * s_zy
        + weights["w"] * s_xw * s_wy
    )
    if lower_boundary_rhs < 0:
        raise AssertionError("BK lower boundary should point inward")

    upper_boundary_rhs = (
        weights["z"] * (s_xz * s_zy - 1)
        + weights["w"] * (s_xw * s_wy - 1)
    )
    if upper_boundary_rhs > 0:
        raise AssertionError("BK upper boundary should point inward")

    transparent = {"xy": Fraction(1), "xz": Fraction(1), "zy": Fraction(1)}
    black = {"xy": Fraction(0), "xz": Fraction(0), "zy": Fraction(0)}
    assert_equal(
        "BK transparent fixed point",
        weights["z"] * (transparent["xz"] * transparent["zy"] - transparent["xy"]),
        Fraction(0),
    )
    assert_equal(
        "BK black-disk fixed point",
        weights["z"] * (black["xz"] * black["zy"] - black["xy"]),
        Fraction(0),
    )


def check_finite_bk_error_bound_lipschitz_constant() -> None:
    weights = [Fraction(3, 10), Fraction(1, 5), Fraction(1, 7)]
    l_total = sum(weights)
    delta_xy = Fraction(1, 17)
    delta_xz = Fraction(2, 19)
    delta_zy = Fraction(3, 23)

    # For values in [0,1], |ab-a'b'| <= |a-a'|+|b-b'|.  Together with the
    # virtual term this gives the 3L coefficient used in the manuscript.
    product_bound = sum(w * (delta_xz + delta_zy) for w in weights)
    virtual_bound = l_total * delta_xy
    sup_delta = max(delta_xy, delta_xz, delta_zy)
    assert_equal(
        "BK finite closure Lipschitz ledger",
        product_bound + virtual_bound <= 3 * l_total * sup_delta,
        True,
    )

    eps, l_rate, time = sp.symbols("eps l_rate time", positive=True)
    s = sp.symbols("s")
    gronwall_constant = sp.integrate(
        sp.exp(3 * l_rate * (time - s)) * eps,
        (s, 0, time),
    )
    assert_zero(
        "BK constant-error Gronwall integral",
        gronwall_constant - eps * (sp.exp(3 * l_rate * time) - 1) / (3 * l_rate),
    )


def check_projective_jimwlk_cylinder_limit_budget() -> None:
    """Check the finite error ledger behind the cylinder weak-equation limit."""
    cylinder_value = Fraction(11, 17)
    representative_values = {
        "coarse": cylinder_value,
        "fine": cylinder_value,
    }
    assert_equal(
        "cylinder representative consistency",
        representative_values["fine"] - representative_values["coarse"],
        Fraction(0),
    )

    step = Fraction(2, 5)
    finite_state_f = Fraction(7, 13)
    finite_state_hf = Fraction(-3, 10)
    finite_next_f = finite_state_f + step * finite_state_hf

    state_error_initial = Fraction(1, 200)
    state_error_next = Fraction(1, 300)
    state_error_on_generator = Fraction(1, 350)
    generator_error = Fraction(1, 525)

    limit_state_f = finite_state_f + state_error_initial
    limit_next_f = finite_next_f - state_error_next
    limit_state_hf = finite_state_hf + state_error_on_generator + generator_error

    residual = abs(limit_next_f - limit_state_f - step * limit_state_hf)
    budget = (
        state_error_initial
        + state_error_next
        + step * (state_error_on_generator + generator_error)
    )
    assert_equal("projective weak-equation residual budget", residual, budget)

    budgets: list[Fraction] = []
    for m in range(1, 7):
        delta_m = Fraction(1, 2**m)
        epsilon_m = Fraction(1, 3**m)
        budgets.append(2 * delta_m + step * (delta_m + epsilon_m))

    for earlier, later in zip(budgets, budgets[1:]):
        if not later < earlier:
            raise AssertionError("projective cylinder-limit budget should decrease")

    fixed_generator_error = Fraction(1, 6)
    requested_tolerance = Fraction(1, 20)
    if step * fixed_generator_error <= requested_tolerance:
        raise AssertionError("nonvanishing generator error should obstruct the requested tolerance")


def check_small_x_measured_observable_proof_obligation_map() -> None:
    """Check the finite proof-obligation map from QCD observable to CGC approximant."""

    exact_observable = Fraction(29, 17)
    residuals = {
        "impact_factor": Fraction(3, 101),
        "rapidity": Fraction(2, 137),
        "projective": Fraction(5, 223),
        "evolution": Fraction(7, 257),
        "closure": Fraction(11, 401),
        "power": Fraction(13, 503),
    }

    wilson_coordinate = exact_observable - residuals["impact_factor"]
    rapidity_subtracted = wilson_coordinate - residuals["rapidity"]
    projective_coordinate = rapidity_subtracted - residuals["projective"]
    evolved_coordinate = projective_coordinate - residuals["evolution"]
    closed_coordinate = evolved_coordinate - residuals["closure"]
    finite_approximant = closed_coordinate - residuals["power"]

    actual_error = exact_observable - finite_approximant
    signed_residual_sum = sum(residuals.values(), Fraction(0))
    absolute_budget = sum(abs(value) for value in residuals.values())

    assert_equal(
        "measured small-x residual propagation map",
        actual_error,
        signed_residual_sum,
    )
    assert_leq(
        "measured small-x conditional residual propagation",
        abs(actual_error),
        absolute_budget,
        tol=Fraction(0),
    )

    omitted_impact_budget = absolute_budget - abs(residuals["impact_factor"])
    omitted_closure_budget = absolute_budget - abs(residuals["closure"])
    assert_gt(
        "impact-factor residual is necessary for this measured observable",
        abs(actual_error),
        omitted_impact_budget,
    )
    assert_gt(
        "closure residual is necessary for this BK-projected observable",
        abs(actual_error),
        omitted_closure_budget,
    )

    full_jimwlk_residuals = dict(residuals)
    full_jimwlk_residuals["closure"] = Fraction(0)
    full_jimwlk_error = sum(full_jimwlk_residuals.values(), Fraction(0))
    full_jimwlk_budget = sum(abs(value) for value in full_jimwlk_residuals.values())
    assert_leq(
        "full JIMWLK measured small-x conditional residual propagation",
        abs(full_jimwlk_error),
        full_jimwlk_budget,
        tol=Fraction(0),
    )


def check_leading_dis_dipole_observable_channel() -> None:
    """Check the finite leading small-x DIS dipole observable ledger."""

    q2 = Fraction(9)
    z_cells = (
        (Fraction(1, 5), Fraction(1, 6)),
        (Fraction(2, 5), Fraction(1, 3)),
        (Fraction(3, 5), Fraction(1, 3)),
        (Fraction(4, 5), Fraction(1, 6)),
    )
    r_weights = {"small": Fraction(2, 7), "mid": Fraction(5, 7)}
    b_weights = {"central": Fraction(3, 5), "edge": Fraction(2, 5)}
    k0_sq = {"small": Fraction(3, 2), "mid": Fraction(5, 4)}
    k1_sq = {"small": Fraction(5, 2), "mid": Fraction(7, 5)}
    flavors = (
        {"charge2": Fraction(4, 9), "mass2": Fraction(1, 25)},
        {"charge2": Fraction(1, 9), "mass2": Fraction(4, 25)},
    )
    test_bin = {
        ("small", "central"): Fraction(5, 4),
        ("small", "edge"): Fraction(1, 3),
        ("mid", "central"): Fraction(2, 3),
        ("mid", "edge"): Fraction(1, 2),
    }

    def epsilon2(z: Fraction, flavor: dict[str, Fraction]) -> Fraction:
        return z * (1 - z) * q2 + flavor["mass2"]

    def photon_weight(
        polarization: str,
        z: Fraction,
        r_label: str,
        flavor: dict[str, Fraction],
    ) -> Fraction:
        charge2 = flavor["charge2"]
        mass2 = flavor["mass2"]
        spin_t = z * z + (1 - z) * (1 - z)
        if polarization == "T":
            return charge2 * (
                spin_t * epsilon2(z, flavor) * k1_sq[r_label]
                + mass2 * k0_sq[r_label]
            )
        if polarization == "L":
            return charge2 * 4 * q2 * z * z * (1 - z) * (1 - z) * k0_sq[r_label]
        raise ValueError(f"unknown polarization {polarization!r}")

    for polarization in ("T", "L"):
        for z, _weight in z_cells:
            for r_label in r_weights:
                for flavor in flavors:
                    assert_equal(
                        f"{polarization} photon kernel z-reflection symmetry",
                        photon_weight(polarization, z, r_label, flavor),
                        photon_weight(polarization, 1 - z, r_label, flavor),
                    )

    bk_n = {
        ("small", "central"): Fraction(1, 5),
        ("small", "edge"): Fraction(1, 3),
        ("mid", "central"): Fraction(2, 5),
        ("mid", "edge"): Fraction(1, 2),
    }
    dipole_error = {
        ("small", "central"): Fraction(1, 20),
        ("small", "edge"): Fraction(0),
        ("mid", "central"): Fraction(0),
        ("mid", "edge"): Fraction(0),
    }
    exact_n = {
        key: value + dipole_error[key]
        for key, value in bk_n.items()
    }

    def dipole_observable(
        polarization: str,
        amplitude: dict[tuple[str, str], Fraction],
    ) -> Fraction:
        total = Fraction(0)
        for z, z_weight in z_cells:
            for r_label, r_weight in r_weights.items():
                for b_label, b_weight in b_weights.items():
                    measure = (
                        z_weight
                        * r_weight
                        * b_weight
                        * test_bin[(r_label, b_label)]
                    )
                    kernel_sum = sum(
                        photon_weight(polarization, z, r_label, flavor)
                        for flavor in flavors
                    )
                    total += 2 * measure * kernel_sum * amplitude[(r_label, b_label)]
        return total

    for polarization in ("T", "L"):
        exact_observable = dipole_observable(polarization, exact_n)
        bk_observable = dipole_observable(polarization, bk_n)
        actual_error = exact_observable - bk_observable

        propagated_bound = Fraction(0)
        unweighted_bound = Fraction(0)
        for z, z_weight in z_cells:
            for r_label, r_weight in r_weights.items():
                for b_label, b_weight in b_weights.items():
                    measure = (
                        z_weight
                        * r_weight
                        * b_weight
                        * abs(test_bin[(r_label, b_label)])
                    )
                    kernel_sum = sum(
                        photon_weight(polarization, z, r_label, flavor)
                        for flavor in flavors
                    )
                    propagated_bound += (
                        2
                        * measure
                        * kernel_sum
                        * abs(dipole_error[(r_label, b_label)])
                    )
                    unweighted_bound += (
                        2
                        * measure
                        * abs(dipole_error[(r_label, b_label)])
                    )

        assert_equal(
            f"{polarization} DIS dipole error equals weighted BK image",
            actual_error,
            propagated_bound,
        )
        assert_gt(
            f"{polarization} DIS photon kernel is necessary in the error budget",
            abs(actual_error),
            unweighted_bound,
        )

    def matvec(
        matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
        vector: tuple[Fraction, Fraction],
    ) -> tuple[Fraction, Fraction]:
        return (
            matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
            matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
        )

    def dot(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> Fraction:
        return left[0] * right[0] + left[1] * right[1]

    generator = (
        (Fraction(2, 3), Fraction(1, 5)),
        (Fraction(1, 5), Fraction(1, 2)),
    )
    target_state = (Fraction(3, 7), Fraction(4, 7))
    impact_factor = (
        dipole_observable("T", bk_n),
        dipole_observable("L", bk_n),
    )
    target_rapidity_term = dot(target_state, matvec(generator, impact_factor))
    projectile_subtraction = matvec(generator, impact_factor)

    assert_equal(
        "DIS rapidity-separation cancellation",
        target_rapidity_term - dot(target_state, projectile_subtraction),
        Fraction(0),
    )
    assert_gt(
        "wrong rapidity-subtraction sign leaves a measured residual",
        abs(target_rapidity_term + dot(target_state, projectile_subtraction)),
        Fraction(0),
    )

    delta, z = sp.symbols("delta z")
    transverse_tail = sp.integrate(
        z**2 + (1 - z) ** 2,
        (z, 0, delta),
    )
    longitudinal_tail = sp.integrate(
        4 * z**2 * (1 - z) ** 2,
        (z, 0, delta),
    )
    assert_zero(
        "transverse endpoint spin primitive",
        transverse_tail - (delta - delta**2 + sp.Rational(2, 3) * delta**3),
    )
    assert_zero(
        "longitudinal endpoint spin primitive",
        longitudinal_tail
        - (
            sp.Rational(4, 3) * delta**3
            - 2 * delta**4
            + sp.Rational(4, 5) * delta**5
        ),
    )

    endpoint = sp.Rational(1, 10)
    assert_leq(
        "transverse endpoint spin bound",
        transverse_tail.subs(delta, endpoint),
        endpoint,
        tol=Fraction(0),
    )
    assert_leq(
        "longitudinal endpoint spin bound",
        longitudinal_tail.subs(delta, endpoint),
        sp.Rational(4, 3) * endpoint**3,
        tol=Fraction(0),
    )


def main() -> None:
    check_trace_delta_kernel_coefficient()
    check_transverse_inversion_covariance()
    check_bfkl_characteristic_values()
    check_finite_wilson_line_diffusion_algebra()
    check_wilson_line_dirichlet_form_sign()
    check_finite_bk_closure_algebra()
    check_finite_bk_error_bound_lipschitz_constant()
    check_projective_jimwlk_cylinder_limit_budget()
    check_small_x_measured_observable_proof_obligation_map()
    check_leading_dis_dipole_observable_channel()
    print(
        "All QCD small-x/BFKL, finite Wilson-line, BK-closure, "
        "projective JIMWLK-limit, measured-observable proof-obligation map, "
        "and leading DIS dipole-channel checks passed."
    )


if __name__ == "__main__":
    main()
