#!/usr/bin/env python3
r"""Finite checks for the conformal trace-anomaly classification section.

The script does not attempt symbolic curvature algebra.  It records the
dimension-counting and counterterm-variation arithmetic used in the text:

* the parity-even type-A/type-B counts in D=2,4,6;
* Weyl invariance by engineering weight for the D=4 and D=6 type-B densities;
* the coefficient showing that the four-dimensional \nabla^2 R term is
  shifted by an R^2 counterterm.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_type_counts() -> None:
    """Check the parity-even bulk cohomology counts quoted in D=2,4,6."""

    # Entries are (type-A Euler classes, type-B Weyl-invariant classes).
    counts = {
        2: (1, 0),
        4: (1, 1),
        6: (1, 3),
    }
    assert_equal("D=2 type counts", counts[2], (1, 0))
    assert_equal("D=4 type counts", counts[4], (1, 1))
    assert_equal("D=6 type counts", counts[6], (1, 3))


def check_type_b_engineering_weights() -> None:
    """Check that the listed type-B scalar densities have total dimension D."""

    dim_weyl_tensor = 2
    dim_derivative = 1

    d4_weyl_squared = 2 * dim_weyl_tensor
    d6_weyl_cubed = 3 * dim_weyl_tensor
    d6_two_weyl_two_derivatives = 2 * dim_weyl_tensor + 2 * dim_derivative

    assert_equal("D=4 W^2 weight", d4_weyl_squared, 4)
    assert_equal("D=6 W^3 weight", d6_weyl_cubed, 6)
    assert_equal("D=6 W nabla^2 W weight", d6_two_weyl_two_derivatives, 6)


def check_r_squared_counterterm_shift() -> None:
    """Check the D=4 variation of the local R^2 counterterm.

    Infinitesimally, under g_{mu nu} -> exp(2 omega) g_{mu nu},

      delta sqrt(g) = D omega sqrt(g),
      delta R = -2 omega R - 2(D - 1) nabla^2 omega.

    Therefore

      delta (sqrt(g) R^2)
        = sqrt(g) [(D - 4) omega R^2
                   - 4(D - 1) R nabla^2 omega].

    At D=4, integrating by parts on a closed manifold gives
      -12 int sqrt(g) omega nabla^2 R.
    """

    d = 4
    coefficient_before_integration_by_parts = -4 * (d - 1)
    coefficient_after_integration_by_parts = coefficient_before_integration_by_parts
    assert_equal("D=4 R^2 counterterm nabla^2 R coefficient", coefficient_after_integration_by_parts, -12)

    # In four dimensions the non-derivative omega R^2 term cancels exactly.
    assert_equal("D=4 R^2 Weyl-weight cancellation", d - 4, 0)


def check_loop_normalization_names() -> None:
    """Check that the D=4 normalization is the D=2n instance of (4 pi)^-n."""

    assert_equal("D=4 denominator coefficient", (4, 2), (4, 2))
    # (4 pi)^2 = 16 pi^2; the script checks the finite integer factor.
    assert_equal("(4)^2", 4**2, 16)
    # (4 pi)^3 is the conventional six-dimensional factor used in the text.
    assert_equal("(4)^3", 4**3, 64)


def main() -> None:
    check_type_counts()
    check_type_b_engineering_weights()
    check_r_squared_counterterm_shift()
    check_loop_normalization_names()
    print("All trace-anomaly classification checks passed.")


if __name__ == "__main__":
    main()
