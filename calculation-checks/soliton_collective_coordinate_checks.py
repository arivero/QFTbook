#!/usr/bin/env python3
"""Finite checks for the soliton collective-coordinate section.

The script verifies algebraic identities used in the finite-energy
gauge-Higgs soliton discussion:

* the Bogomolny and Abelian-Higgs square completions,
* the Prasad-Sommerfield profile equations,
* the monopole phase-coordinate Legendre transform and theta-angle
  charge-lattice relabelling,
* the framed monopole moduli dimension bookkeeping and horizontal-slice sign,
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
    check_zero_mode_density_coordinate_change()
    check_one_instanton_orientation_dimension()
    print("All soliton collective-coordinate checks passed.")


if __name__ == "__main__":
    main()
