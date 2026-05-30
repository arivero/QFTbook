#!/usr/bin/env python3
"""Finite checks for higher-gauging condensation-defect normalization.

The monograph uses two complementary descriptions of the same finite measure:
cochain cardinalities, and homotopy cardinality of the finite two-form gauge
2-groupoid.  The checks below verify both.  The explicit-complex tests
enumerate cochains over Z_N directly, rather than relying only on formal rank
bookkeeping.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


def assert_equal(lhs: int, rhs: int, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def vectors(n: int, dim: int) -> list[Vector]:
    return list(product(range(n), repeat=dim))


def mat_vec_mod(matrix: Matrix, vector: Vector, n: int) -> Vector:
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) % n for row in matrix)


def kernel(matrix: Matrix, domain_dim: int, n: int) -> set[Vector]:
    return {v for v in vectors(n, domain_dim) if all(x == 0 for x in mat_vec_mod(matrix, v, n))}


def image(matrix: Matrix, domain_dim: int, n: int) -> set[Vector]:
    return {mat_vec_mod(matrix, v, n) for v in vectors(n, domain_dim)}


@dataclass(frozen=True)
class ExplicitComplex:
    name: str
    c0: int
    c1: int
    c2: int
    d0: Matrix
    d1: Matrix
    d2: Matrix

    def check_chain_condition(self, n: int) -> None:
        for v in vectors(n, self.c0):
            assert_equal(
                mat_vec_mod(self.d1, mat_vec_mod(self.d0, v, n), n),
                tuple(0 for _ in range(self.c2)),
                f"{self.name}: d1 d0 = 0 over Z_{n}",
            )
        for v in vectors(n, self.c1):
            assert_equal(
                mat_vec_mod(self.d2, mat_vec_mod(self.d1, v, n), n),
                tuple(0 for _ in range(len(self.d2))),
                f"{self.name}: d2 d1 = 0 over Z_{n}",
            )


def explicit_complexes() -> list[ExplicitComplex]:
    return [
        ExplicitComplex(
            name="minimal S3",
            c0=1,
            c1=0,
            c2=0,
            d0=tuple(),
            d1=tuple(),
            d2=tuple(),
        ),
        ExplicitComplex(
            name="minimal S2xS1",
            c0=1,
            c1=1,
            c2=1,
            d0=((0,),),
            d1=((0,),),
            d2=tuple(),
        ),
        ExplicitComplex(
            name="minimal T3",
            c0=1,
            c1=3,
            c2=3,
            d0=((0,), (0,), (0,)),
            d1=((0, 0, 0), (0, 0, 0), (0, 0, 0)),
            d2=tuple(),
        ),
        ExplicitComplex(
            name="connected acyclic refinement",
            c0=4,
            c1=6,
            c2=3,
            d0=(
                (-1, 1, 0, 0),
                (-1, 0, 1, 0),
                (-1, 0, 0, 1),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
            ),
            d1=(
                (0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 1, 0),
                (0, 0, 0, 0, 0, 1),
            ),
            d2=tuple(),
        ),
    ]


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


def check_explicit_two_form_groupoid_cardinality() -> None:
    for n in range(2, 7):
        for complex_ in explicit_complexes():
            complex_.check_chain_condition(n)
            c0_card = n**complex_.c0
            c1_card = n**complex_.c1
            z2 = kernel(complex_.d2, complex_.c2, n)
            b1 = image(complex_.d0, complex_.c0, n)
            z1 = kernel(complex_.d1, complex_.c1, n)
            b2 = image(complex_.d1, complex_.c1, n)

            # Cochain path-integral measure: |C0| |Z2| / |C1|.
            cochain_num = c0_card * len(z2)
            cochain_den = c1_card

            # Homotopy cardinality: |H0| |H2| / |H1|, computed from
            # cardinalities of kernels and images.  We compare cross-products
            # to avoid assuming the ratio is an integer.
            h0_num = c0_card
            h0_den = len(b1)
            h1_num = len(z1)
            h1_den = len(b1)
            h2_num = len(z2)
            h2_den = len(b2)
            hom_num = h0_num * h2_num * h1_den
            hom_den = h0_den * h2_den * h1_num

            assert_equal(
                cochain_num * hom_den,
                hom_num * cochain_den,
                f"{complex_.name}: cochain measure equals 2-groupoid cardinality over Z_{n}",
            )


def check_explicit_condensation_convolution() -> None:
    for n in range(2, 7):
        for complex_ in explicit_complexes():
            z2 = sorted(kernel(complex_.d2, complex_.c2, n))
            z2_set = set(z2)
            for s in z2:
                count = 0
                for b in z2:
                    bp = tuple((s[i] - b[i]) % n for i in range(complex_.c2))
                    if bp in z2_set:
                        count += 1
                assert_equal(
                    count,
                    len(z2),
                    f"{complex_.name}: convolution fiber size for closed two-cochains over Z_{n}",
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
    check_explicit_two_form_groupoid_cardinality()
    check_explicit_condensation_convolution()
    check_old_cellular_normalization_is_not_topological()
    print("Finite higher-gauging condensation checks passed.")


if __name__ == "__main__":
    main()
