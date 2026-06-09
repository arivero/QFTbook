#!/usr/bin/env python3
"""Finite checks for scattering cluster limits and low-dimensional support.

Evidence contract.
Target claims:
- The Volume II cluster-decomposition theorem uses a joint
  Haag--Ruelle/separation diagonal, not uniformity in a partial relative
  translation derived from global unitarity.
- Polynomial finite-time growth can be beaten by spacelike-separation decay
  when T(a)=o(|a|), while T comparable to |a| is not a valid separation
  diagonal from the displayed rho lower bound.
- In 1+1-dimensional elastic kinematics, total momentum conservation pulls
  back to permutation graphs in rapidity variables, so connected-kernel
  subtraction removes proper product blocks but does not erase all graph
  delta support compatible with total conservation.
Independent construction:
- The diagonal test is a separate exponent model with |a|=L^q, T=L^p, and a
  symbolic finite-time bound T^M rho^{-N}.
- The 1+1 support test reconstructs the outgoing lightcone variables as the
  roots of a quadratic fixed by total p^+ and p^- conservation.
Imported assumptions:
- The finite Haag--Ruelle cluster estimate has polynomial T growth and
  inverse-power rho decay, and the joint approximation error contains a model
  term T^{-s}+T/|a| for the chosen wave packets.
- The 1+1 example is away from coincident rapidities and thresholds.
Negative controls:
- Choosing T with the same scaling power as |a| fails the tube-separation
  lower-bound test.
- Choosing too small an inverse-separation power N fails to dominate the
  polynomial finite-time growth.
- Subtracting separate one-particle product blocks is checked not to remove
  the elastic exchange graph.
Scope boundary:
- These are finite arithmetic and support-shape checks.  They are not a proof
  of the Haag--Ruelle estimates, asymptotic completeness, LSZ, or
  distributional existence of a particular model's scattering kernel.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def cluster_decay_exponent(t_power: int, a_power: int, m_power: int, n_power: int) -> int:
    """Exponent of L in T^M rho^{-N} when T=L^p and rho~|a|=L^q."""

    if not (0 < t_power < a_power):
        raise ValueError("the diagonal must satisfy T=o(|a|)")
    return t_power * m_power - a_power * n_power


def joint_error_exponents(t_power: int, a_power: int, spectral_power: int) -> tuple[int, int]:
    """Exponents for the model error T^{-s}+T/|a|."""

    if not (0 < t_power < a_power):
        raise ValueError("the diagonal must satisfy T=o(|a|)")
    return (-spectral_power * t_power, t_power - a_power)


def check_diagonal_limit_arithmetic() -> None:
    # A sample diagonal: |a|=L^2 and T=L.  The finite-time clustering term
    # T^3 rho^{-2} scales as L^{-1}, and the model joint Haag--Ruelle error
    # T^{-2}+T/|a| scales as L^{-2}+L^{-1}.
    t_power = 1
    a_power = 2
    assert_equal(
        "finite-time cluster exponent",
        cluster_decay_exponent(t_power, a_power, m_power=3, n_power=2),
        -1,
    )
    assert_equal(
        "joint Haag-Ruelle model exponents",
        joint_error_exponents(t_power, a_power, spectral_power=2),
        (-2, -1),
    )

    try:
        cluster_decay_exponent(t_power=1, a_power=1, m_power=3, n_power=10)
    except ValueError:
        pass
    else:
        raise AssertionError("T comparable to |a| incorrectly passed as a separation diagonal")

    insufficient_decay = cluster_decay_exponent(t_power, a_power, m_power=3, n_power=1)
    assert_true("insufficient N should not dominate polynomial T growth", insufficient_decay > 0)


def total_lightcone_data(x1: Fraction, x2: Fraction) -> tuple[Fraction, Fraction]:
    """Return total p^+/m and p^-/m for two rapidity variables x=e^theta."""

    return (x1 + x2, Fraction(1, x1) + Fraction(1, x2))


def quadratic_roots_from_totals(total_plus: Fraction, total_minus: Fraction) -> tuple[Fraction, Fraction]:
    # Since total_minus=(x1+x2)/(x1*x2), the product is total_plus/total_minus.
    product = total_plus / total_minus
    # The samples below are chosen so the discriminant is a perfect square.
    discriminant = total_plus * total_plus - 4 * product
    numerator_root = isqrt(discriminant.numerator)
    denominator_root = isqrt(discriminant.denominator)
    if (
        numerator_root * numerator_root != discriminant.numerator
        or denominator_root * denominator_root != discriminant.denominator
    ):
        raise AssertionError("sample discriminant was not a perfect square")
    sqrt_disc = Fraction(numerator_root, denominator_root)
    return ((total_plus - sqrt_disc) / 2, (total_plus + sqrt_disc) / 2)


def check_one_plus_one_elastic_support() -> None:
    x1 = Fraction(2)
    x2 = Fraction(5)
    total_plus, total_minus = total_lightcone_data(x1, x2)
    roots = quadratic_roots_from_totals(total_plus, total_minus)
    assert_equal("1+1 total conservation roots", roots, (x1, x2))

    identity = total_lightcone_data(x1, x2)
    exchange = total_lightcone_data(x2, x1)
    assert_equal("identity graph conserves total momentum", identity, (total_plus, total_minus))
    assert_equal("exchange graph conserves total momentum", exchange, (total_plus, total_minus))

    wrong_output = total_lightcone_data(Fraction(3), Fraction(4))
    assert_true("same p+ alone is not enough in 1+1", wrong_output[0] == total_plus)
    assert_true("wrong graph fails p- conservation", wrong_output[1] != total_minus)


def check_connected_subtraction_boundary() -> None:
    full_regular_support = {
        "separate_one_particle_product",
        "elastic_exchange_graph",
    }
    proper_product_blocks = {"separate_one_particle_product"}
    connected_support = full_regular_support - proper_product_blocks
    assert_equal(
        "proper product subtraction leaves exchange graph",
        connected_support,
        {"elastic_exchange_graph"},
    )


def main() -> None:
    check_diagonal_limit_arithmetic()
    check_one_plus_one_elastic_support()
    check_connected_subtraction_boundary()
    print("All scattering cluster-decomposition checks passed.")


if __name__ == "__main__":
    main()
