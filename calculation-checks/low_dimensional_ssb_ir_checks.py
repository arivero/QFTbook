"""Infrared checks for Coleman and Mermin--Wagner--Hohenberg estimates.

Evidence contract.

Target claim: Section `sec:low-dimensional-continuous-ssb-no-go` uses the
Coleman equal-time massless-scalar logarithm
`asinh(Lambda/m)/(2*pi) ~ log(2 Lambda/m)/(2*pi)` and the
Mermin--Wagner--Hohenberg spin-wave integrals whose infrared behavior
diverges in spatial dimensions one and two but is finite in dimension three.

Independent construction: the script evaluates the regulated one-dimensional
energy integral and the radial `d=1,2,3` fluctuation integrals from their
elementary antiderivatives, then checks scale changes and limiting ratios
rather than substituting only the displayed asymptotic statements.

Imported assumptions: sharp momentum cutoff `Lambda`, positive infrared mass
regulator `m`, rotationally invariant small-momentum dispersion proportional
to `k^2`, and the monograph Fourier convention with `(2*pi)^d` in the
momentum measure.

Negative controls: the script rejects the wrong Coleman coefficient
`1/(4*pi)`, the wrong two-dimensional MWH logarithm coefficient, a finite
`d=2` limit, and a logarithmically divergent `d=3` limit.

Scope boundary: a pass verifies only the displayed infrared algebra.  It does
not prove the Wightman theorem, Gibbs/KMS thermodynamic-limit hypotheses,
positivity, clustering, locality, or existence of the regulated continuum
models.
"""

from __future__ import annotations

import math
from collections.abc import Callable

from check_utils import assert_close, assert_lt


def expect_failure(name: str, callback: Callable[[], None]) -> None:
    try:
        callback()
    except AssertionError:
        return
    raise AssertionError(f"{name}: negative control unexpectedly passed")


def coleman_equal_time_variance(mass: float, cutoff: float) -> float:
    if mass <= 0.0 or cutoff <= 0.0:
        raise AssertionError("Coleman regulators must be positive")
    return math.asinh(cutoff / mass) / (2.0 * math.pi)


def mwh_integral_1d(mass: float, cutoff: float) -> float:
    if mass <= 0.0 or cutoff <= 0.0:
        raise AssertionError("MWH regulators must be positive")
    return math.atan(cutoff / mass) / (math.pi * mass)


def mwh_integral_2d(mass: float, cutoff: float) -> float:
    if mass <= 0.0 or cutoff <= 0.0:
        raise AssertionError("MWH regulators must be positive")
    return math.log((cutoff * cutoff + mass * mass) / (mass * mass)) / (4.0 * math.pi)


def mwh_integral_3d(mass: float, cutoff: float) -> float:
    if mass <= 0.0 or cutoff <= 0.0:
        raise AssertionError("MWH regulators must be positive")
    return (cutoff - mass * math.atan(cutoff / mass)) / (2.0 * math.pi * math.pi)


def check_coleman_logarithm() -> None:
    cutoff = 7.0
    mass = 1.0e-6
    value = coleman_equal_time_variance(mass, cutoff)
    leading = math.log(2.0 * cutoff / mass) / (2.0 * math.pi)
    assert_close("Coleman logarithm leading coefficient", value, leading, atol=1.0e-12)

    ratio = 100.0
    increment = coleman_equal_time_variance(mass / ratio, cutoff) - value
    expected_increment = math.log(ratio) / (2.0 * math.pi)
    assert_close("Coleman logarithm scale increment", increment, expected_increment, atol=1.0e-12)

    expect_failure(
        "wrong Coleman coefficient",
        lambda: assert_close(
            "wrong Coleman coefficient",
            increment,
            math.log(ratio) / (4.0 * math.pi),
            atol=1.0e-6,
        ),
    )


def check_mwh_dimension_split() -> None:
    cutoff = 5.0
    mass = 1.0e-7
    ratio = 100.0

    d1_scaled = mass * mwh_integral_1d(mass, cutoff)
    assert_close("MWH d=1 power divergence coefficient", d1_scaled, 0.5, atol=1.0e-8)

    d2_increment = mwh_integral_2d(mass / ratio, cutoff) - mwh_integral_2d(mass, cutoff)
    expected_d2_increment = math.log(ratio) / (2.0 * math.pi)
    assert_close("MWH d=2 logarithm coefficient", d2_increment, expected_d2_increment, atol=1.0e-12)

    d3_value = mwh_integral_3d(mass, cutoff)
    d3_limit = cutoff / (2.0 * math.pi * math.pi)
    assert_close("MWH d=3 finite infrared limit", d3_value, d3_limit, atol=1.0e-7)

    d3_increment = mwh_integral_3d(mass / ratio, cutoff) - d3_value
    assert_lt("MWH d=3 scale increment is small", abs(d3_increment), 1.0e-6)

    expect_failure(
        "wrong MWH d=2 logarithm coefficient",
        lambda: assert_close(
            "wrong MWH d=2 logarithm coefficient",
            d2_increment,
            math.log(ratio) / (4.0 * math.pi),
            atol=1.0e-6,
        ),
    )
    expect_failure(
        "wrong finite MWH d=2 limit",
        lambda: assert_close(
            "wrong finite MWH d=2 limit",
            mwh_integral_2d(mass / ratio, cutoff),
            mwh_integral_2d(mass, cutoff),
            atol=1.0e-3,
        ),
    )
    expect_failure(
        "wrong logarithmic MWH d=3 divergence",
        lambda: assert_close(
            "wrong logarithmic MWH d=3 divergence",
            d3_increment,
            expected_d2_increment,
            atol=1.0e-3,
        ),
    )


def main() -> int:
    check_coleman_logarithm()
    check_mwh_dimension_split()
    print("All low-dimensional SSB infrared checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
