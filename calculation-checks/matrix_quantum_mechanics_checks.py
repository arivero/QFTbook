"""Exact checks for intrinsic matrix quantum mechanics.

Evidence contract.
Target claims:
- Hermitian one-matrix quantum mechanics has the radial Laplacian
  Delta_X f = Delta(lambda)^(-2) sum_i partial_i(Delta(lambda)^2 partial_i f)
  on singlet wavefunctions, and conjugation by the Vandermonde maps the
  singlet sector to antisymmetric eigenvalue wavefunctions with a free
  fermion kinetic operator away from collision hyperplanes.
- The large-N singlet collective-field Hamiltonian is the hydrodynamic form
  obtained from the two Fermi-surface branches p_+ and p_-.
- In matrix gauge quantum mechanics the Gauss generators close as the gauge
  algebra and the supercharge anticommutator closes on the Hamiltonian modulo
  Gauss-law generators.
Independent construction:
- The script builds polynomial Vandermonde identities directly in SymPy for
  N=2 and N=3; no monograph formula is parsed or reused.
- The Gauss and supercharge checks use an explicit finite SU(2) two-matrix
  reduction with real Clifford matrices, then simplify the polynomial
  identities exactly.
Imported assumptions:
- The radial identities are checked on the regular locus of distinct
  eigenvalues, where the eigenvalue-angle coordinates are valid.
- The supercharge identity checks the bosonic coefficient skeleton of the
  dimensionally reduced supersymmetry algebra; the full sixteen-supercharge
  BFSS algebra uses the same Gauss-law mechanism plus the standard SO(9)
  Clifford/Fierz identities.
Negative controls:
- The Vandermonde exponent is also tested with the wrong power, which must
  fail to produce the free-fermion kinetic operator.
- The supercharge closure is tested with the Gauss term omitted, which must
  leave a nonzero polynomial obstruction.
Scope boundary:
- These are finite symbolic checks of local algebra and coordinate changes.
  They do not prove the continuum threshold-bound-state theorem, a large-N
  limit, double-scaling universality, c=1 string duality, BFSS/M-theory
  equivalence, or matrix-string perturbation theory.
"""

from __future__ import annotations

import sympy as sp


def require_zero(label: str, expr) -> None:
    simplified = sp.factor(sp.cancel(sp.expand(expr)))
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")


def require_nonzero(label: str, expr) -> None:
    simplified = sp.factor(sp.cancel(sp.expand(expr)))
    if simplified == 0:
        raise AssertionError(f"{label} should have produced a nonzero obstruction")


def vandermonde(xs):
    out = sp.Integer(1)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            out *= xs[i] - xs[j]
    return sp.expand(out)


def radial_laplacian(f, xs, power: int = 2):
    delta = vandermonde(xs)
    numerator = sum(sp.diff(delta**power * sp.diff(f, x), x) for x in xs)
    return sp.cancel(numerator / delta**power)


def radial_component_formula(f, xs):
    second = sum(sp.diff(f, x, 2) for x in xs)
    first = sp.Integer(0)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            first += 2 * (sp.diff(f, xs[i]) - sp.diff(f, xs[j])) / (xs[i] - xs[j])
    return sp.cancel(second + first)


def symmetric_test_polynomial(xs):
    return sp.expand(
        1
        + sum(x**2 for x in xs)
        + sum(xs[i] * xs[j] for i in range(len(xs)) for j in range(i + 1, len(xs)))
        + sp.prod(xs)
    )


def check_vandermonde_radial_laplacian() -> None:
    for n in (2, 3):
        xs = sp.symbols(f"x0:{n}")
        f = symmetric_test_polynomial(xs)
        delta = vandermonde(xs)

        require_zero(
            f"radial component formula N={n}",
            radial_laplacian(f, xs) - radial_component_formula(f, xs),
        )

        antisymmetric_wavefunction = sp.expand(delta * f)
        require_zero(
            f"Vandermonde conjugates radial kinetic operator N={n}",
            delta * radial_laplacian(f, xs)
            - sum(sp.diff(antisymmetric_wavefunction, x, 2) for x in xs),
        )

        swapped = antisymmetric_wavefunction.xreplace({xs[0]: xs[1], xs[1]: xs[0]})
        require_zero(f"Vandermonde wavefunction antisymmetry N={n}", swapped + antisymmetric_wavefunction)
        require_zero(
            f"Vandermonde wavefunction vanishes at collision N={n}",
            antisymmetric_wavefunction.subs(xs[0], xs[1]),
        )

        negative_control = sum(
            xs[i] * xs[j] for i in range(len(xs)) for j in range(i + 1, len(xs))
        )
        negative_control_wavefunction = sp.expand(delta * negative_control)
        wrong_power_laplacian = radial_laplacian(negative_control, xs, power=1)
        require_nonzero(
            f"wrong Vandermonde power obstruction N={n}",
            delta * wrong_power_laplacian
            - sum(sp.diff(negative_control_wavefunction, x, 2) for x in xs),
        )


def check_collective_field_hydrodynamics() -> None:
    rho, velocity, hbar, potential = sp.symbols("rho velocity hbar potential")
    p_plus = velocity + sp.pi * hbar * rho
    p_minus = velocity - sp.pi * hbar * rho
    fermi_surface_density = (p_plus - p_minus) / (2 * sp.pi * hbar)
    require_zero("density from Fermi-surface branches", fermi_surface_density - rho)

    phase_space_hamiltonian = (p_plus**3 - p_minus**3) / (12 * sp.pi * hbar)
    phase_space_hamiltonian += potential * (p_plus - p_minus) / (2 * sp.pi * hbar)
    collective_hamiltonian = rho * velocity**2 / 2 + sp.pi**2 * hbar**2 * rho**3 / 6 + potential * rho
    require_zero("collective-field hydrodynamic Hamiltonian", phase_space_hamiltonian - collective_hamiltonian)

    lam, mu = sp.symbols("lam mu", positive=True)
    p_ground_plus = sp.sqrt(lam**2 - 2 * mu)
    p_ground_minus = -p_ground_plus
    density = (p_ground_plus - p_ground_minus) / (2 * sp.pi)
    require_zero("inverted-oscillator Fermi-sea density", density - sp.sqrt(lam**2 - 2 * mu) / sp.pi)


def epsilon3(a: int, b: int, c: int) -> int:
    if len({a, b, c}) < 3:
        return 0
    perm = [a, b, c]
    inversions = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
    return -1 if inversions % 2 else 1


def check_su2_gauss_and_supercharge_closure() -> None:
    # Two adjoint matrices X_i^a and momenta P_i^a, with SU(2) color index a.
    xs = {(i, a): sp.symbols(f"X{i}{a}") for i in range(2) for a in range(3)}
    ps = {(i, a): sp.symbols(f"P{i}{a}") for i in range(2) for a in range(3)}

    def poisson(f, g):
        out = sp.Integer(0)
        for i in range(2):
            for a in range(3):
                out += sp.diff(f, xs[(i, a)]) * sp.diff(g, ps[(i, a)])
                out -= sp.diff(f, ps[(i, a)]) * sp.diff(g, xs[(i, a)])
        return sp.expand(out)

    def commutator_component(i: int, j: int, a: int):
        return sum(epsilon3(a, b, c) * xs[(i, b)] * xs[(j, c)] for b in range(3) for c in range(3))

    gauss = {
        a: sum(
            epsilon3(a, b, c) * xs[(i, b)] * ps[(i, c)]
            for i in range(2)
            for b in range(3)
            for c in range(3)
        )
        for a in range(3)
    }

    for a in range(3):
        for b in range(3):
            expected = sum(epsilon3(a, b, c) * gauss[c] for c in range(3))
            require_zero(f"SU(2) Gauss algebra {a},{b}", poisson(gauss[a], gauss[b]) - expected)

    p_squared = sum(ps[(i, a)] ** 2 for i in range(2) for a in range(3))
    c_squared = sum(commutator_component(0, 1, a) ** 2 for a in range(3))
    hamiltonian = sp.Rational(1, 2) * (p_squared + c_squared)
    for a in range(3):
        require_zero(f"bosonic matrix Hamiltonian gauge invariance {a}", poisson(gauss[a], hamiltonian))

    gamma1 = sp.Matrix([[0, 1], [1, 0]])
    gamma2 = sp.Matrix([[1, 0], [0, -1]])
    gamma12 = (gamma1 * gamma2 - gamma2 * gamma1) / 2
    identity = sp.eye(2)

    # Q_alpha = A_{alpha,a,beta} psi_{a,beta}; the fermion bracket contracts
    # the psi variables, leaving the bosonic coefficient identity.
    coefficient = {}
    for alpha in range(2):
        for a in range(3):
            for beta in range(2):
                coefficient[(alpha, a, beta)] = sp.expand(
                    ps[(0, a)] * gamma1[alpha, beta]
                    + ps[(1, a)] * gamma2[alpha, beta]
                    - commutator_component(0, 1, a) * gamma12[alpha, beta]
                )

    for alpha in range(2):
        for beta in range(2):
            bracket = sum(
                coefficient[(alpha, a, spin)] * coefficient[(beta, a, spin)]
                for a in range(3)
                for spin in range(2)
            )
            gauss_term = -2 * sum(
                (gamma1[alpha, beta] * xs[(0, a)] + gamma2[alpha, beta] * xs[(1, a)])
                * gauss[a]
                for a in range(3)
            )
            require_zero(
                f"supercharge closure modulo Gauss {alpha},{beta}",
                bracket - (identity[alpha, beta] * (p_squared + c_squared) + gauss_term),
            )
            if alpha == beta:
                require_nonzero(
                    f"supercharge closure needs Gauss term {alpha},{beta}",
                    bracket - identity[alpha, beta] * (p_squared + c_squared),
                )


def main() -> None:
    check_vandermonde_radial_laplacian()
    check_collective_field_hydrodynamics()
    check_su2_gauss_and_supercharge_closure()
    print("All matrix quantum mechanics radial, collective-field, Gauss-law, and supercharge checks passed.")


if __name__ == "__main__":
    main()
