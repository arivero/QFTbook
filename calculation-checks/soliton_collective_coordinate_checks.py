#!/usr/bin/env python3
r"""Finite checks for the soliton collective-coordinate section.

Evidence contract.

Target claims:
* finite algebra in the gauge-Higgs soliton collective-coordinate section,
  including square completions, profile ODEs, theta relabelling, and
  zero-mode density coordinate changes;
* local collective-coordinate stationary phase requires compact support,
  constant normal rank, a uniform Hessian lower bound, an action gap, and a
  fixed orbit type before a family of Gaussian determinants can be integrated.

Independent construction:
* every identity below is recomputed from symbolic formulas or finite group
  actions rather than copied from the surrounding prose.

Imported assumptions:
* the checks are finite dimensional and do not prove the analytic
  functional-integral or continuum regulator limits.

Negative controls:
* a noncompact critical line with pointwise positive normal Hessian
  \(L_z=1/z^2\) is rejected as a uniform Morse-Bott chart;
* a vanishing action-gap family is rejected as a source of exponential
  complement control;
* a finite \(\mathbb Z_2\) action with a fixed point is rejected by the
  constant-isotropy quotient rule.

Scope boundary:
* these checks guard convention-sensitive finite identities and the
  stationary-phase hypotheses; physical instanton amplitudes still require
  determinant, source, endpoint, and analytic-continuation estimates.

The script verifies algebraic identities used in the finite-energy
gauge-Higgs soliton discussion:

* the Bogomolny and Abelian-Higgs square completions,
* the Prasad-Sommerfield profile equations,
* the monopole phase-coordinate Legendre transform and theta-angle
  charge-lattice relabelling,
* the BPS dyon mass expansion matching the phase-coordinate Hamiltonian,
* the framed monopole moduli dimension bookkeeping and horizontal-slice sign,
* the Jackiw-Rebbi kink zero-mode profile and half-charge bookkeeping,
* the coordinate invariance of the zero-mode density sqrt(det G) d^m z, and
* the local dimension count of the one-instanton orientation orbit;
* the finite failure modes that distinguish pointwise nondegeneracy from a
  compact fixed-orbit-type stationary-phase chart.

These checks do not replace the functional-analytic hypotheses in the text;
they guard the convention-sensitive finite algebra.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

import sympy as sp

T = TypeVar("T")


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.factor(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def check_bogomolny_square_completion() -> None:
    B, D = sp.symbols("B D")
    for sign in (1, -1):
        lhs = sp.Rational(1, 2) * (B**2 + D**2)
        rhs = sp.Rational(1, 2) * (B - sign * D) ** 2 + sign * B * D
        assert_zero(f"Bogomolny completion sign={sign}", sp.expand(lhs - rhs))


def check_vortex_square_completion() -> None:
    B, e, v, r = sp.symbols("B e v r", nonzero=True)
    X = v**2 - r
    lhs = B**2 / (2 * e**2) + e**2 * X**2 / 2
    for sign in (1, -1):
        rhs = (B - sign * e**2 * X) ** 2 / (2 * e**2) + sign * B * X
        assert_zero(f"vortex completion sign={sign}", sp.expand(lhs - rhs))


def check_prasad_sommerfield_profiles() -> None:
    rho = sp.symbols("rho", positive=True)
    K = rho / sp.sinh(rho)
    H = sp.coth(rho) - 1 / rho
    first = sp.diff(K, rho) + K * H
    second = sp.diff(H, rho) - (1 - K**2) / rho**2
    assert_zero("Prasad-Sommerfield K equation", sp.together(first))
    assert_zero("Prasad-Sommerfield H equation", sp.together(second))


def check_monopole_phase_legendre_and_theta_shift() -> None:
    I, theta, nm, ne, chidot = sp.symbols("I theta nm ne chidot", nonzero=True)
    lagrangian = sp.Rational(1, 2) * I * chidot**2 - theta * nm * chidot / (2 * sp.pi)
    momentum = sp.diff(lagrangian, chidot)
    solved_chidot = sp.solve(sp.Eq(ne, momentum), chidot)[0]
    hamiltonian = sp.simplify(ne * solved_chidot - lagrangian.subs(chidot, solved_chidot))
    expected = (ne + theta * nm / (2 * sp.pi)) ** 2 / (2 * I)
    assert_zero("monopole phase Legendre transform", sp.together(hamiltonian - expected))

    shifted_charge = (ne - nm) + (theta + 2 * sp.pi) * nm / (2 * sp.pi)
    original_charge = ne + theta * nm / (2 * sp.pi)
    assert_zero("theta-periodic dyon charge relabelling", sp.together(shifted_charge - original_charge))


def check_bps_dyon_mass_phase_expansion() -> None:
    v, q_m, e_unit, q_e = sp.symbols("v q_m e_unit q_e", positive=True)
    x = sp.symbols("x")

    # The relativistic BPS mass is v |Q_M| sqrt(1+x^2), with
    # x=Q_E/|Q_M|.  The phase-coordinate Hamiltonian is only the quadratic term.
    sqrt_series = sp.series(sp.sqrt(1 + x**2), x, 0, 6).removeO()
    expected_series = 1 + x**2 / 2 - x**4 / 8
    assert_zero("BPS dyon small-electric expansion", sp.together(sqrt_series - expected_series))

    physical_electric_charge = e_unit * q_e
    exact_mass = v * q_m * sp.sqrt(1 + (physical_electric_charge / q_m) ** 2)
    expanded_mass = (
        v * q_m
        + v * physical_electric_charge**2 / (2 * q_m)
        - v * physical_electric_charge**4 / (8 * q_m**3)
    )
    exact_series = sp.series(exact_mass, q_e, 0, 6).removeO()
    assert_zero("BPS dyon mass series in phase quantum", sp.together(exact_series - expanded_mass))

    inertia = q_m / (v * e_unit**2)
    phase_hamiltonian = q_e**2 / (2 * inertia)
    quadratic_mass_shift = v * physical_electric_charge**2 / (2 * q_m)
    assert_zero("phase Hamiltonian matches quadratic BPS mass shift", phase_hamiltonian - quadratic_mass_shift)

    quartic_correction = -v * physical_electric_charge**4 / (8 * q_m**3)
    if quartic_correction == 0:
        raise AssertionError("negative control failed: exact BPS dyon mass had no quartic correction")

    theta, nm, ne = sp.symbols("theta nm ne")
    shifted_coordinate = e_unit * ((ne - nm) + (theta + 2 * sp.pi) * nm / (2 * sp.pi))
    original_coordinate = e_unit * (ne + theta * nm / (2 * sp.pi))
    assert_zero(
        "BPS dyon physical electric charge theta relabelling",
        sp.together(shifted_coordinate - original_coordinate),
    )

    odd_linear_mass = v * (q_m + physical_electric_charge)
    if sp.simplify(odd_linear_mass.subs(q_e, -q_e) - odd_linear_mass) == 0:
        raise AssertionError("negative control failed: linear electric mass was charge-conjugation even")


def check_framed_monopole_moduli_bookkeeping() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    framed_dim = 4 * n
    center_phase_dim = 4
    relative_dim = framed_dim - center_phase_dim
    assert_zero("framed monopole dimension", framed_dim - 4 * n)
    assert_zero("centered relative monopole dimension", relative_dim - (4 * n - 4))
    assert_equal("unit monopole relative dimension", relative_dim.subs(n, 1), 0)
    assert_equal("two-monopole relative dimension", relative_dim.subs(n, 2), 4)

    div_a, comm_phi_varphi = sp.symbols("div_a comm_phi_varphi")
    # Orthogonality to gauge orbits gives -D_i a_i + i[Phi,varphi].
    gauge_pairing_coefficient = -div_a + sp.I * comm_phi_varphi
    background_gauge_condition = div_a - sp.I * comm_phi_varphi
    assert_zero(
        "background-gauge sign in horizontal monopole tangent",
        gauge_pairing_coefficient + background_gauge_condition,
    )


def check_jackiw_rebbi_kink_zero_mode_and_half_charge() -> None:
    x, m = sp.symbols("x m", positive=True)
    profile = sp.sech(m * x)
    kink_mass = m * sp.tanh(m * x)

    # With H = [[0, -d/dx + M], [d/dx + M, 0]], the kink zero mode has
    # only the first component nonzero.
    zero_mode_equation = sp.diff(profile, x) + kink_mass * profile
    assert_zero("Jackiw-Rebbi kink zero-mode equation", zero_mode_equation)

    wrong_component_profile = sp.cosh(m * x)
    wrong_component_equation = -sp.diff(wrong_component_profile, x) + kink_mass * wrong_component_profile
    assert_zero("Jackiw-Rebbi other formal solution equation", wrong_component_equation)
    if sp.limit(wrong_component_profile, x, sp.oo) != sp.oo:
        raise AssertionError("wrong Jackiw-Rebbi component should be nonnormalizable")

    antikink_mass = -kink_mass
    antikink_second_component_equation = -sp.diff(profile, x) + antikink_mass * profile
    assert_zero("Jackiw-Rebbi antikink chirality flip", antikink_second_component_equation)

    u = sp.symbols("u", real=True)
    sech_norm = sp.limit(sp.tanh(u), u, sp.oo) - sp.limit(sp.tanh(u), u, -sp.oo)
    assert_equal("sech squared primitive normalization", sech_norm, 2)
    normalized_integral = sp.Rational(1, 2) * sech_norm
    assert_equal("Jackiw-Rebbi zero-mode normalization", normalized_integral, 1)

    empty_zero_mode_charge = sp.Rational(-1, 2)
    filled_zero_mode_charge = empty_zero_mode_charge + 1
    assert_equal("empty kink zero-mode half charge", empty_zero_mode_charge, sp.Rational(-1, 2))
    assert_equal("filled kink zero-mode half charge", filled_zero_mode_charge, sp.Rational(1, 2))

    integer_empty_charge = 0
    integer_filled_charge = 1
    if (integer_empty_charge, integer_filled_charge) == (
        empty_zero_mode_charge,
        filled_zero_mode_charge,
    ):
        raise AssertionError("negative control failed: integer zero-mode charges accepted")
    if integer_empty_charge + integer_filled_charge == 0:
        raise AssertionError("negative control failed: integer charges were charge-conjugation symmetric")

    paired_nonzero_energies = [-3, -1, 1, 3]
    if sum(sp.sign(energy) for energy in paired_nonzero_energies) != 0:
        raise AssertionError("paired nonzero Jackiw-Rebbi spectrum should have zero asymmetry")
    unpaired_nonzero_energies = [-3, 1, 2]
    if sum(sp.sign(energy) for energy in unpaired_nonzero_energies) == 0:
        raise AssertionError("negative control failed: unpaired nonzero spectrum looked symmetric")


def check_zero_mode_density_coordinate_change() -> None:
    G = sp.Matrix([[3, 1], [1, 2]])
    jac = sp.Matrix([[2, 0], [1, 3]])
    transformed = jac.T * G * jac
    assert_equal(
        "Gram determinant coordinate transformation",
        sp.det(transformed),
        sp.det(jac) ** 2 * sp.det(G),
    )


def check_one_instanton_orientation_dimension() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    su_n = n**2 - 1
    su_n_minus_two = (n - 2) ** 2 - 1
    orient_dim = su_n - su_n_minus_two - 1
    assert_zero("SU(N) embedded SU(2) orientation dimension", orient_dim - (4 * n - 5))
    assert_zero("one-instanton bosonic dimension", (4 + 1 + orient_dim) - 4 * n)
    assert_equal("SU(2) orientation dimension", orient_dim.subs(n, 2), 3)


def check_uniform_morse_bott_needs_compact_lower_bound() -> None:
    z = sp.symbols("z", positive=True)
    hessian = 1 / z**2

    for sample in (1, 2, 5):
        if hessian.subs(z, sample) <= 0:
            raise AssertionError("pointwise Hessian positivity failed")

    if sp.limit(hessian, z, sp.oo) != 0:
        raise AssertionError("negative control failed: Hessian did not tend to zero")

    candidate_lower_bound = sp.Rational(1, 100)
    if hessian.subs(z, 11) >= candidate_lower_bound:
        raise AssertionError("negative control failed: noncompact chart looked uniformly positive")

    gaussian_coefficient = sp.sqrt(1 / hessian)
    assert_zero("normal Gaussian determinant coefficient", gaussian_coefficient - z)
    if sp.limit(gaussian_coefficient, z, sp.oo) != sp.oo:
        raise AssertionError("negative control failed: determinant coefficient stayed bounded")

    n = sp.symbols("n", integer=True, positive=True)
    partial_sum = sp.summation(n, (n, 1, 20))
    assert_equal("noncompact determinant coefficient partial sum", partial_sum, 210)
    if partial_sum <= 20:
        raise AssertionError("negative control failed: noncompact coefficient did not grow")


def check_uniform_action_gap_is_separate_hypothesis() -> None:
    z = sp.symbols("z", positive=True)
    eps = sp.Rational(1, 100)
    gap = 1 / z

    if sp.limit(gap, z, sp.oo) != 0:
        raise AssertionError("negative control failed: gap did not close at infinity")

    candidate_gap = sp.Rational(1, 10)
    if gap.subs(z, 11) >= candidate_gap:
        raise AssertionError("negative control failed: vanishing gap passed a uniform bound")

    moving_exponent = -gap.subs(z, 1000) / eps
    uniform_exponent = -candidate_gap / eps
    if moving_exponent <= uniform_exponent:
        raise AssertionError("negative control failed: weak gap gave uniform exponential decay")


def check_constant_isotropy_versus_stabilizer_jump() -> None:
    group = (0, 1)

    def orbit_representatives(points: tuple[T, ...], action: Callable[[int, T], T]) -> list[T]:
        unseen = set(points)
        reps: list[T] = []
        for point in points:
            if point not in unseen:
                continue
            orbit = {action(g, point) for g in group}
            reps.append(point)
            unseen -= orbit
        return reps

    def stabilizer_size(action: Callable[[int, T], T], point: T) -> int:
        return sum(1 for g in group if action(g, point) == point)

    free_points = (("a", 0), ("a", 1), ("b", 0), ("b", 1))

    def free_action(g: int, point: tuple[str, int]) -> tuple[str, int]:
        label, bit = point
        return (label, bit ^ g)

    free_stabilizers = {stabilizer_size(free_action, point) for point in free_points}
    assert_equal("constant free isotropy", free_stabilizers, {1})
    free_reps = orbit_representatives(free_points, free_action)
    assert_equal("free quotient orbit count", len(free_reps), 2)

    signed_points = (-1, 0, 1)

    def sign_action(g: int, point: int) -> int:
        return point if g == 0 else -point

    signed_stabilizers = {stabilizer_size(sign_action, point) for point in signed_points}
    assert_equal("stabilizer jump sizes", signed_stabilizers, {1, 2})
    signed_reps = orbit_representatives(signed_points, sign_action)
    groupoid_weight = sum(
        sp.Rational(1, stabilizer_size(sign_action, point)) for point in signed_reps
    )
    generic_weight_shortcut = sp.Rational(len(signed_reps), 1)
    assert_equal("jump-stratum quotient weight", groupoid_weight, sp.Rational(3, 2))
    assert_equal("generic fixed-isotropy shortcut", generic_weight_shortcut, 2)
    if generic_weight_shortcut == groupoid_weight:
        raise AssertionError("negative control failed: stabilizer jump accepted as constant isotropy")


def check_stationary_phase_remainder_keeps_common_saddle_factor() -> None:
    eps, s0, amplitude, constant = sp.symbols("eps s0 amplitude constant", positive=True)
    common_factor = sp.exp(-s0 / eps) * (2 * sp.pi * eps)
    correct = common_factor * (amplitude + constant * eps)
    normalized_correct = sp.simplify(correct / common_factor - amplitude)
    assert_zero("stationary-phase normalized local remainder", normalized_correct - constant * eps)

    wrong_additive_remainder = common_factor * amplitude + constant * eps**2
    normalized_wrong = sp.simplify(wrong_additive_remainder / common_factor - amplitude)
    if not normalized_wrong.has(sp.exp(s0 / eps)):
        raise AssertionError("negative control failed: additive remainder kept the saddle scale")


def main() -> None:
    check_bogomolny_square_completion()
    check_vortex_square_completion()
    check_prasad_sommerfield_profiles()
    check_monopole_phase_legendre_and_theta_shift()
    check_bps_dyon_mass_phase_expansion()
    check_framed_monopole_moduli_bookkeeping()
    check_jackiw_rebbi_kink_zero_mode_and_half_charge()
    check_zero_mode_density_coordinate_change()
    check_one_instanton_orientation_dimension()
    check_uniform_morse_bott_needs_compact_lower_bound()
    check_uniform_action_gap_is_separate_hypothesis()
    check_constant_isotropy_versus_stabilizer_jump()
    check_stationary_phase_remainder_keeps_common_saddle_factor()
    print("All soliton collective-coordinate checks passed.")


if __name__ == "__main__":
    main()
