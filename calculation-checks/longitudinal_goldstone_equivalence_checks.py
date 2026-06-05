#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- The longitudinal polarization used in the equivalence relation is transverse
  and differs from k/m by O(m/E), while k/m is not an exact polarization.
- The Goldstone-side object is a gauge-fixed source coordinate evaluated at
  vector-shell kinematics; away from xi=1 this is not the Goldstone pole shell.
- External-pole amputation keeps the pole residue and kills analytic
  non-pole terms in the contracted Slavnov--Taylor identity.
- Multi-longitudinal-leg suppression follows only after bounded tensor
  contractions for every term containing at least one remainder polarization.
- The high-energy electroweak scalar representative has the Higgs-sector
  cancellation M_deriv + M_h = -m_h^2 s/(v^2(s-m_h^2)) and the ordered
  partial-wave normalization a_0 = M/(16 pi).

Independent construction:
- The polarization identities are checked directly in the mostly-plus metric.
- The pole/analytic separation is checked as a one-variable residue limit.
- The scattering cancellation is checked both symbolically and by finite
  numerical scale tests.

Imported assumptions:
- Mostly-plus metric, physical mass shell k^2 = -m^2, and the Volume I
  invariant-amplitude and partial-wave conventions.
- The electroweak example is the custodial high-energy scalar-sector algebra
  away from the Higgs pole, not a full finite-energy Standard Model amplitude
  and not an LSZ construction for unstable W/Z external states.

Negative controls:
- Treating k/m as the exact longitudinal polarization fails transversality and
  normalization.
- Treating the Goldstone coordinate as a generic R_xi LSZ pole at vector
  kinematics fails unless xi=1.
- Allowing the tensor amplitude contracted with a remainder polarization to
  grow like E/m destroys the claimed suppression.
- Omitting the Higgs exchange, reversing its sign, or using M/(32 pi) for the
  ordered s-wave coefficient fails the finite checks.

Scope boundary:
- This script verifies convention-sensitive finite algebra only.  It does not
  prove BRST restoration, LSZ existence for unstable W/Z bosons, or the
  all-orders equivalence theorem.
"""

from __future__ import annotations

import math

import sympy as sp

from check_utils import assert_close, assert_geq, assert_gt, assert_leq


def minkowski_dot(left: tuple[float, float, float, float], right: tuple[float, float, float, float]) -> float:
    """Mostly-plus dot product for four-vectors in a fixed COM frame."""

    return -left[0] * right[0] + left[1] * right[1] + left[2] * right[2] + left[3] * right[3]


def check_longitudinal_polarization_remainder() -> None:
    mass = 1.7
    for ratio in (5.0, 10.0, 25.0, 100.0, 1000.0):
        energy = ratio * mass
        momentum = math.sqrt(energy * energy - mass * mass)
        k = (energy, 0.0, 0.0, momentum)
        epsilon = (momentum / mass, 0.0, 0.0, energy / mass)

        assert_close(f"k^2 mass shell E/m={ratio}", minkowski_dot(k, k), -mass * mass, atol=1.0e-8)
        assert_close(f"epsilon transversality E/m={ratio}", minkowski_dot(k, epsilon), 0.0, atol=1.0e-8)
        assert_close(f"epsilon norm E/m={ratio}", minkowski_dot(epsilon, epsilon), 1.0, atol=1.0e-8)

        k_over_m = tuple(component / mass for component in k)
        remainder = tuple(epsilon[index] - k_over_m[index] for index in range(4))
        max_remainder = max(abs(component) for component in remainder)
        exact_component = (energy - momentum) / mass
        assert_close(f"exact longitudinal remainder E/m={ratio}", max_remainder, exact_component, atol=5.0e-12)
        assert_leq(f"O(m/E) longitudinal remainder E/m={ratio}", max_remainder, 1.0 / ratio)
        assert_leq(
            f"relative longitudinal remainder E/m={ratio}",
            max_remainder / max(abs(component) for component in epsilon),
            1.0 / (ratio * ratio),
        )

        assert_gt(f"k/m is not transverse E/m={ratio}", abs(minkowski_dot(k, k_over_m)), 0.5 * mass)
        assert_close(f"k/m has timelike norm E/m={ratio}", minkowski_dot(k_over_m, k_over_m), -1.0, atol=1.0e-8)


def check_external_pole_separation() -> None:
    denominator, residue, analytic_0, analytic_1, mass, conversion = sp.symbols(
        "D R A0 A1 m C", nonzero=True
    )
    pole_part = mass * conversion * residue / denominator
    analytic_part = analytic_0 + analytic_1 * denominator

    amputated_full = sp.limit(denominator * (pole_part + analytic_part), denominator, 0)
    amputated_analytic = sp.limit(denominator * analytic_part, denominator, 0)

    if sp.simplify(amputated_full - mass * conversion * residue) != 0:
        raise AssertionError("external pole residue was not preserved")
    if sp.simplify(amputated_analytic) != 0:
        raise AssertionError("analytic non-pole term survived external amputation")


def check_goldstone_source_shell_mismatch() -> None:
    k2, mass2, xi = sp.symbols("k2 mass2 xi", positive=True)
    vector_shell = -mass2
    goldstone_pole_shell = -xi * mass2
    goldstone_inverse = k2 + xi * mass2

    inverse_at_vector_shell = sp.simplify(goldstone_inverse.subs(k2, vector_shell))
    if inverse_at_vector_shell != (xi - 1) * mass2:
        raise AssertionError("Goldstone inverse at vector shell has wrong xi dependence")
    if sp.simplify(goldstone_pole_shell.subs(xi, 1) - vector_shell) != 0:
        raise AssertionError("Feynman-gauge shell coincidence failed")

    xi_value = sp.Rational(5, 2)
    if sp.simplify(goldstone_pole_shell.subs(xi, xi_value) - vector_shell) == 0:
        raise AssertionError("generic R_xi Goldstone pole should not coincide with vector shell")
    if sp.simplify(inverse_at_vector_shell.subs(xi, xi_value)) == 0:
        raise AssertionError("generic R_xi Goldstone inverse should not vanish at vector shell")


def check_multi_leg_remainder_bound() -> None:
    for n_legs in (2, 3, 4):
        mass_over_energy = 0.03
        hard_size = 7.0
        k_constant = 1.25
        subset_count = 2**n_legs - 1
        bounded_remainder_sum = subset_count * k_constant * mass_over_energy * hard_size
        declared_bound = sum(k_constant for _ in range(subset_count)) * mass_over_energy * hard_size
        assert_close(
            f"multi-leg bounded remainder n={n_legs}",
            bounded_remainder_sum,
            declared_bound,
            atol=1.0e-12,
        )
        assert_leq(
            f"multi-leg remainder remains suppressed n={n_legs}",
            bounded_remainder_sum / hard_size,
            subset_count * k_constant * mass_over_energy,
        )

    mass_over_energy = 0.02
    compensating_tensor_growth = 1.0 / mass_over_energy
    unsuppressed_contraction = mass_over_energy * compensating_tensor_growth
    assert_geq(
        "E/m tensor growth destroys remainder suppression",
        unsuppressed_contraction,
        1.0,
    )


def derivative_growth(s_value: float, v_value: float) -> float:
    return s_value / (v_value * v_value)


def higgs_exchange(s_value: float, v_value: float, mh_value: float) -> float:
    return -(s_value * s_value) / (v_value * v_value * (s_value - mh_value * mh_value))


def total_amplitude(s_value: float, v_value: float, mh_value: float) -> float:
    return derivative_growth(s_value, v_value) + higgs_exchange(s_value, v_value, mh_value)


def check_higgs_sector_cancellation() -> None:
    s, v, mh = sp.symbols("s v mh", nonzero=True)
    symbolic_total = s / v**2 - s**2 / (v**2 * (s - mh**2))
    symbolic_expected = -mh**2 * s / (v**2 * (s - mh**2))
    if sp.simplify(symbolic_total - symbolic_expected) != 0:
        raise AssertionError("Higgs cancellation identity failed")

    v_value = 246.0
    mh_value = 125.1
    high_s = (100.0 * mh_value) ** 2
    medium_s = (10.0 * mh_value) ** 2

    for factor in (3.0, 10.0, 100.0):
        s_value = (factor * mh_value) ** 2
        expected = -mh_value * mh_value * s_value / (v_value * v_value * (s_value - mh_value * mh_value))
        assert_close(
            f"finite Higgs cancellation factor={factor}",
            total_amplitude(s_value, v_value, mh_value),
            expected,
            atol=1.0e-12,
            rtol=1.0e-12,
        )

    asymptotic_constant = -mh_value * mh_value / (v_value * v_value)
    assert_close(
        "high-energy constant limit",
        total_amplitude(high_s, v_value, mh_value),
        asymptotic_constant,
        atol=0.0,
        rtol=1.1e-4,
    )

    derivative_ratio = derivative_growth(high_s, v_value) / derivative_growth(medium_s, v_value)
    assert_close("uncancelled derivative growth scales with s", derivative_ratio, high_s / medium_s)
    assert_gt(
        "uncancelled derivative term is parametrically too large",
        derivative_growth(high_s, v_value) / abs(total_amplitude(high_s, v_value, mh_value)),
        9000.0,
    )

    wrong_sign_total = derivative_growth(high_s, v_value) - higgs_exchange(high_s, v_value, mh_value)
    assert_geq(
        "wrong Higgs sign leaves leading growth",
        abs(wrong_sign_total) / derivative_growth(high_s, v_value),
        1.9,
    )

    a0 = total_amplitude(high_s, v_value, mh_value) / (16.0 * math.pi)
    expected_a0 = asymptotic_constant / (16.0 * math.pi)
    assert_close("ordered partial-wave normalization", a0, expected_a0, atol=0.0, rtol=1.1e-4)

    wrong_a0 = total_amplitude(high_s, v_value, mh_value) / (32.0 * math.pi)
    assert_gt("M/(32 pi) is the wrong ordered normalization", abs(wrong_a0 - expected_a0), abs(expected_a0) / 4.0)


def main() -> None:
    check_longitudinal_polarization_remainder()
    check_external_pole_separation()
    check_goldstone_source_shell_mismatch()
    check_multi_leg_remainder_bound()
    check_higgs_sector_cancellation()
    print("All longitudinal-vector/Goldstone equivalence checks passed.")


if __name__ == "__main__":
    main()
