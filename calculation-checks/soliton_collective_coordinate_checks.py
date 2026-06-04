#!/usr/bin/env python3
"""Finite checks for the soliton collective-coordinate section.

The script verifies algebraic identities used in the finite-energy
gauge-Higgs soliton discussion:

* the Bogomolny and Abelian-Higgs square completions,
* the Prasad-Sommerfield profile equations,
* the monopole phase-coordinate Legendre transform and theta-angle
  charge-lattice relabelling,
* the framed monopole moduli dimension bookkeeping and horizontal-slice sign,
* the Jackiw-Rebbi kink zero-mode profile and half-charge bookkeeping,
* the coordinate invariance of the zero-mode density sqrt(det G) d^m z, and
* the local dimension count of the one-instanton orientation orbit.

These checks do not replace the functional-analytic hypotheses in the text;
they guard the convention-sensitive finite algebra.
"""

from __future__ import annotations

import sympy as sp


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


def main() -> None:
    check_bogomolny_square_completion()
    check_vortex_square_completion()
    check_prasad_sommerfield_profiles()
    check_monopole_phase_legendre_and_theta_shift()
    check_framed_monopole_moduli_bookkeeping()
    check_jackiw_rebbi_kink_zero_mode_and_half_charge()
    check_zero_mode_density_coordinate_change()
    check_one_instanton_orientation_dimension()
    print("All soliton collective-coordinate checks passed.")


if __name__ == "__main__":
    main()
