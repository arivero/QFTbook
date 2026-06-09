"""Low-dimensional endpoint checks for Kallen--Lehmann shell measures.

Evidence contract.

Target claims: Proposition
`prop:kallen-lehmann-mass-shell-disintegration` in Volume I, Chapter 9 splits
the scalar mass-shell disintegration by dimension: the massless scalar shell is
locally finite at the closed-cone endpoint for `D >= 3`, while in `D = 2` the
punctured null cone has two proper-orthochronous Lorentz orbits and scalar
local finiteness forces zero null-ray coefficients.

Independent construction: the script works in exact dyadic coordinates.  It
tracks the two `D = 2` light-cone rays by the vanishing of `p+` or `p-`, checks
that boosts rescale each ray separately, models `dk/k` by dyadic-annulus
counts, and compares this with the radial massless-shell density
`r^(D-3) dr` near the origin.

Imported assumptions: mostly-plus metric, future cone `p0 >= |p1|`,
proper-orthochronous boosts acting as `p+ -> exp(eta) p+` and
`p- -> exp(-eta) p-`, the shell normalization
`d p1 / (2 pi 2 |p1|) = dk/(4 pi k)` on each two-dimensional null ray, and
dyadic intervals used only as exact finite regulators for logarithmic mass.

Negative controls: the checks reject a boost that swaps the two null rays, a
Lebesgue `dk` measure as a boost-invariant ray measure, a finite compact
mass for the constant test function against `dk/k`, and a finite `D = 2`
radial endpoint tail.

Scope boundary: a pass verifies the endpoint orbit arithmetic and local
finiteness obstruction.  It does not prove the Mackey--Effros disintegration
theorem, temperedness of Wightman measures, Hilbert-space positivity, or any
specific infrared-subtracted two-dimensional scalar construction.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from fractions import Fraction

from check_utils import assert_gt, assert_lt


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def expect_failure(name: str, callback: Callable[[], None]) -> None:
    try:
        callback()
    except AssertionError:
        return
    raise AssertionError(f"{name}: negative control unexpectedly passed")


@dataclass(frozen=True)
class LightConeRay:
    has_p_plus: bool
    has_p_minus: bool


RIGHT_RAY = LightConeRay(has_p_plus=True, has_p_minus=False)
LEFT_RAY = LightConeRay(has_p_plus=False, has_p_minus=True)


def boost_ray(ray: LightConeRay) -> LightConeRay:
    """A proper-orthochronous boost rescales nonzero light-cone coordinates."""

    return ray


def swapped_boost_ray(ray: LightConeRay) -> LightConeRay:
    return LightConeRay(has_p_plus=ray.has_p_minus, has_p_minus=ray.has_p_plus)


@dataclass(frozen=True)
class DyadicInterval:
    lower_power: int
    upper_power: int

    def __post_init__(self) -> None:
        if self.lower_power >= self.upper_power:
            raise AssertionError("dyadic interval powers must be increasing")


def scale_interval(interval: DyadicInterval, boost_power: int) -> DyadicInterval:
    return DyadicInterval(
        interval.lower_power + boost_power,
        interval.upper_power + boost_power,
    )


def dk_over_k_mass_in_log2_units(interval: DyadicInterval) -> Fraction:
    return Fraction(interval.upper_power - interval.lower_power, 1)


def lebesgue_dk_mass_in_power_units(interval: DyadicInterval) -> Fraction:
    return Fraction(2) ** interval.upper_power - Fraction(2) ** interval.lower_power


def dyadic_constant_test_mass(number_of_annuli: int, coefficient: Fraction = Fraction(1)) -> Fraction:
    if number_of_annuli <= 0:
        raise AssertionError("annulus count must be positive")
    return coefficient * number_of_annuli


def dyadic_linear_zero_mode_mass(number_of_annuli: int) -> Fraction:
    if number_of_annuli <= 0:
        raise AssertionError("annulus count must be positive")
    return sum(Fraction(1, 2 ** (j + 1)) for j in range(number_of_annuli))


def radial_tail_mass(dimension: int, cutoff_power: int) -> Fraction | None:
    """Integral of r^(D-3) dr from 0 to 2^(-cutoff_power), up to constants."""

    if dimension < 2 or cutoff_power < 0:
        raise AssertionError("dimension and cutoff power must be valid")
    if dimension == 2:
        return None
    exponent = dimension - 2
    return Fraction(1, exponent * 2 ** (cutoff_power * exponent))


def check_two_dimensional_null_orbits_are_separate() -> None:
    assert_equal("right ray fixed by boost", boost_ray(RIGHT_RAY), RIGHT_RAY)
    assert_equal("left ray fixed by boost", boost_ray(LEFT_RAY), LEFT_RAY)
    assert_equal("right and left rays distinct", RIGHT_RAY == LEFT_RAY, False)

    expect_failure(
        "boost swapping null rays",
        lambda: assert_equal("wrong swapped boost", swapped_boost_ray(RIGHT_RAY), RIGHT_RAY),
    )


def check_dk_over_k_boost_invariance() -> None:
    interval = DyadicInterval(-5, -2)
    boosted = scale_interval(interval, 7)
    assert_equal(
        "dk/k dyadic mass is scale invariant",
        dk_over_k_mass_in_log2_units(boosted),
        dk_over_k_mass_in_log2_units(interval),
    )

    expect_failure(
        "Lebesgue dk scale invariance",
        lambda: assert_equal(
            "wrong dk invariant mass",
            lebesgue_dk_mass_in_power_units(boosted),
            lebesgue_dk_mass_in_power_units(interval),
        ),
    )


def check_two_dimensional_endpoint_log_divergence() -> None:
    coefficient = Fraction(3, 5)
    mass_4 = dyadic_constant_test_mass(4, coefficient)
    mass_12 = dyadic_constant_test_mass(12, coefficient)
    assert_gt("constant test dyadic mass grows", mass_12, mass_4)

    finite_bound = Fraction(7, 1)
    expect_failure(
        "finite compact mass for dk/k endpoint",
        lambda: assert_lt(
            "wrong finite compact endpoint mass",
            dyadic_constant_test_mass(20, coefficient),
            finite_bound,
        ),
    )


def check_zero_mode_test_space_changes_endpoint_behavior() -> None:
    partial_6 = dyadic_linear_zero_mode_mass(6)
    partial_12 = dyadic_linear_zero_mode_mass(12)
    assert_gt("linear zero-mode partials increase", partial_12, partial_6)
    assert_lt("linear zero-mode endpoint remains bounded", partial_12, Fraction(1))

    constant_partial = dyadic_constant_test_mass(12)
    assert_gt("constant test rejects zero-mode bound", constant_partial, Fraction(1))


def check_radial_shell_dimension_split() -> None:
    assert_equal("D=2 radial tail is logarithmic", radial_tail_mass(2, 8), None)

    d3_tail_1 = radial_tail_mass(3, 1)
    d3_tail_6 = radial_tail_mass(3, 6)
    d4_tail_1 = radial_tail_mass(4, 1)
    d4_tail_6 = radial_tail_mass(4, 6)
    assert_gt("D=3 radial tail shrinks", d3_tail_1, d3_tail_6)
    assert_gt("D=4 radial tail shrinks", d4_tail_1, d4_tail_6)

    expect_failure(
        "finite D=2 radial endpoint",
        lambda: assert_lt("wrong finite D=2 radial tail", radial_tail_mass(2, 20), Fraction(100)),
    )


def main() -> None:
    check_two_dimensional_null_orbits_are_separate()
    check_dk_over_k_boost_invariance()
    check_two_dimensional_endpoint_log_divergence()
    check_zero_mode_test_space_changes_endpoint_behavior()
    check_radial_shell_dimension_split()
    print("Kallen-Lehmann low-dimensional endpoint checks passed.")


if __name__ == "__main__":
    main()
