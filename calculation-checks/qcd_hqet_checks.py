#!/usr/bin/env python3
"""Finite checks for the HQET Wilson-line and residual-momentum conventions."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def add_poly(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mul_poly(a, b, max_power):
    out = [Fraction(0) for _ in range(max_power + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= max_power:
                out[i + j] += ai * bj
    return tuple(out)


def check_spin_projectors() -> None:
    """Check P_+^2=P_+, P_-^2=P_-, and P_+P_-=0 for s=i slash(v), s^2=1."""

    # Elements of Q[s]/(s^2-1) are represented as a + b s.
    def mul(a, b):
        a0, a1 = a
        b0, b1 = b
        return (a0 * b0 + a1 * b1, a0 * b1 + a1 * b0)

    p_plus = (Fraction(1, 2), Fraction(1, 2))
    p_minus = (Fraction(1, 2), Fraction(-1, 2))
    require(mul(p_plus, p_plus) == p_plus, "P_+ is not idempotent")
    require(mul(p_minus, p_minus) == p_minus, "P_- is not idempotent")
    require(mul(p_plus, p_minus) == (0, 0), "P_+ P_- does not vanish")
    require(add_poly(p_plus, p_minus) == (1, 0), "P_+ + P_- is not one")


def check_transverse_projector() -> None:
    """Check Pi_v^2=Pi_v and v.Pi_v=0 for v^2=-1."""

    v2 = Fraction(-1)
    coefficient_in_pi_squared = 2 + v2
    require(
        coefficient_in_pi_squared == 1,
        "Pi^2 should have the same vv coefficient as Pi",
    )
    require(1 + v2 == 0, "v_mu Pi^mu_nu should vanish")


def check_reparametrization_split() -> None:
    """Check m(v+dv)+(k-mdv)=mv+k at first order exactly."""

    # Store symbolic vector coefficients in the basis {v,k,dv}.
    before = {"v": Fraction(1), "k": Fraction(1), "dv": Fraction(0)}
    after = {"v": Fraction(1), "k": Fraction(1), "dv": Fraction(1) - Fraction(1)}
    require(before == after, "velocity-label shift did not leave p invariant")


def check_residual_dispersion_series() -> None:
    """Check sqrt(1+x)-1 through x^3 solves (1+e)^2=1+x through x^3."""

    # e = E_res/m = 1/2 x - 1/8 x^2 + 1/16 x^3 + O(x^4).
    e = (Fraction(0), Fraction(1, 2), Fraction(-1, 8), Fraction(1, 16))
    one_plus_e = add_poly((1, 0, 0, 0), e)
    squared = mul_poly(one_plus_e, one_plus_e, 3)
    target = (Fraction(1), Fraction(1), Fraction(0), Fraction(0))
    require(squared == target, "residual square-root expansion is inconsistent")


def check_nilpotent_wilson_line_solution() -> None:
    """Check dW/ds=i A W for a nilpotent constant connection A^2=0."""

    # Elements of C[A]/(A^2) are represented as a + b A.
    delta = Fraction(7, 5)
    w = (1, 1j * delta)
    derivative = (0, 1j)

    def mul_nilpotent(a, b):
        return (a[0] * b[0], a[0] * b[1] + a[1] * b[0])

    i_a = (0, 1j)
    rhs = mul_nilpotent(i_a, w)
    require(derivative == rhs, "constant nilpotent Wilson line fails dW/ds=iAW")


def main() -> None:
    check_spin_projectors()
    check_transverse_projector()
    check_reparametrization_split()
    check_residual_dispersion_series()
    check_nilpotent_wilson_line_solution()
    print("All QCD HQET Wilson-line and residual-momentum checks passed.")


if __name__ == "__main__":
    main()
