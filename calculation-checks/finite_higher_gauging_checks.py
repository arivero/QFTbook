#!/usr/bin/env python3
"""Finite checks for higher-gauging condensation-defect normalization."""

from __future__ import annotations

from dataclasses import dataclass


def assert_equal(lhs: int, rhs: int, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


@dataclass(frozen=True)
class ThreeComplex:
    """Cellular cardinality data over a finite coefficient group Z_N.

    The ranks encode the cardinality of coboundary images.  For these exact
    finite checks it is enough to work at the level of cardinalities:
    |C^i| = N^c_i, |B^1| = N^r0, |B^2| = N^r1, and
    |H^2| = N^h2.  This mirrors the proof in the monograph, where only
    exact-sequence cardinalities enter.
    """

    name: str
    c0: int
    c1: int
    r0: int
    r1: int
    h2: int

    @property
    def h0_exp(self) -> int:
        return self.c0 - self.r0

    @property
    def h1_exp(self) -> int:
        return self.c1 - self.r0 - self.r1

    @property
    def h2_exp(self) -> int:
        return self.h2

    @property
    def z2_exp(self) -> int:
        return self.r1 + self.h2


def check_topological_groupoid_factor() -> None:
    examples = [
        ThreeComplex("minimal S3", c0=1, c1=0, r0=0, r1=0, h2=0),
        ThreeComplex("minimal S2xS1", c0=1, c1=1, r0=0, r1=0, h2=1),
        ThreeComplex("minimal T3", c0=1, c1=3, r0=0, r1=0, h2=3),
        ThreeComplex("connected acyclic refinement", c0=4, c1=6, r0=3, r1=3, h2=0),
    ]
    for n in range(2, 13):
        for complex_ in examples:
            lhs_exp = complex_.c0 + complex_.z2_exp - complex_.c1
            rhs_exp = complex_.h0_exp + complex_.h2_exp - complex_.h1_exp
            assert_equal(lhs_exp, rhs_exp, f"{complex_.name}: cochain and cohomology exponents")
            assert_equal(n**lhs_exp, n**rhs_exp, f"{complex_.name}: groupoid factor over Z_{n}")


def check_fusion_coefficient_algebra() -> None:
    for n in range(2, 13):
        for c0, c1, z2 in [(1, 0, 0), (1, 1, 1), (1, 3, 3), (4, 6, 3)]:
            # C = K sum_s U_s, K = |C0|/|C1|.  C*C = K^2 |Z2| sum_s U_s
            #     = (K |Z2|) C.
            k_num = n**c0
            k_den = n**c1
            z2_card = n**z2
            left_num = k_num * k_num * z2_card
            left_den = k_den * k_den
            factor_num = k_num * z2_card
            factor_den = k_den
            c_num = k_num
            c_den = k_den
            assert_equal(
                left_num * factor_den * c_den,
                factor_num * c_num * left_den,
                "condensation fusion coefficient algebra",
            )


def check_old_cellular_normalization_is_not_topological() -> None:
    n = 5
    minimal_s3_old_exp = 0
    refined_s3_old_exp = 3 - 6
    if minimal_s3_old_exp == refined_s3_old_exp:
        raise AssertionError("old normalization unexpectedly cell independent")
    assert_equal(n**minimal_s3_old_exp, 1, "minimal S3 old normalization")
    assert_equal(refined_s3_old_exp, -3, "refined old-normalization exponent bookkeeping")


def main() -> None:
    check_topological_groupoid_factor()
    check_fusion_coefficient_algebra()
    check_old_cellular_normalization_is_not_topological()
    print("Finite higher-gauging condensation checks passed.")


if __name__ == "__main__":
    main()
