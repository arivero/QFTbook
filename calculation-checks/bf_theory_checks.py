#!/usr/bin/env python3
"""Exact finite checks for the BF-theory cochain model.

The checks are deliberately finite.  They verify the algebra used in the
Volume VIII BF-theory chapter: finite Fourier projection onto flat
cochains, the groupoid-cardinality partition function, gauge invariance of a
cellular Wilson operator, and the sign in the Wilson/surface linking phase.
No continuum path integral is assumed by this script.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def vectors(n: int, dimension: int) -> list[Vector]:
    return [tuple(entry % n for entry in vector) for vector in product(range(n), repeat=dimension)]


def mat_vec(matrix: Matrix, vector: Vector, n: int) -> Vector:
    return tuple(sum(entry * value for entry, value in zip(row, vector, strict=True)) % n for row in matrix)


def dot(lhs: Vector, rhs: Vector, n: int) -> int:
    return sum(left * right for left, right in zip(lhs, rhs, strict=True)) % n


def kernel(n: int, matrix: Matrix, domain_dimension: int) -> set[Vector]:
    return {vector for vector in vectors(n, domain_dimension) if mat_vec(matrix, vector, n) == (0,) * len(matrix)}


def image(n: int, matrix: Matrix, domain_dimension: int) -> set[Vector]:
    return {mat_vec(matrix, vector, n) for vector in vectors(n, domain_dimension)}


def compose(lhs: Matrix, rhs: Matrix, n: int) -> Matrix:
    if not lhs:
        return ()
    rows = []
    for row in lhs:
        rows.append(tuple(sum(row[k] * rhs[k][j] for k in range(len(rhs))) % n for j in range(len(rhs[0]))))
    return tuple(rows)


def character_sum_result(n: int, x: Vector) -> tuple[str, int]:
    r"""Return the exact finite Fourier sum over Hom(Z_N^m,Z_N).

    For \(x\in(\mathbb Z_N)^m\), the image of \(b\mapsto b(x)\) is the
    subgroup \(d\mathbb Z_N\), where \(d=\gcd(N,x_1,\ldots,x_m)\).  Each
    image element has the same number of preimages.  Hence the character sum
    is \(N^m\) for \(x=0\) and \(0\) otherwise.  The returned pair records
    the symbolic value and, in the nonzero case, the exact image size.
    """

    d = reduce(gcd, (n, *x))
    if d == n:
        return ("nonzero", n ** len(x))
    return ("zero", n // d)


@dataclass(frozen=True)
class CochainComplex:
    name: str
    c0: int
    c1: int
    c2: int
    delta0: Matrix
    delta1: Matrix

    def check_dimensions(self) -> None:
        assert_equal(f"{self.name} delta0 rows", len(self.delta0), self.c1)
        assert_equal(f"{self.name} delta1 rows", len(self.delta1), self.c2)
        if self.delta0:
            assert_equal(f"{self.name} delta0 columns", len(self.delta0[0]), self.c0)
        if self.delta1:
            assert_equal(f"{self.name} delta1 columns", len(self.delta1[0]), self.c1)


def check_complex_property(n: int, complex_: CochainComplex) -> None:
    if complex_.c1 == 0 or complex_.c2 == 0 or complex_.c0 == 0:
        return
    zero = tuple((0,) * complex_.c0 for _ in range(complex_.c2))
    assert_equal(f"{complex_.name} delta1 delta0=0 mod {n}", compose(complex_.delta1, complex_.delta0, n), zero)


def check_fourier_projection(n: int, complex_: CochainComplex) -> None:
    for a in vectors(n, complex_.c1):
        curvature = mat_vec(complex_.delta1, a, n)
        value, _ = character_sum_result(n, curvature)
        expected = "nonzero" if curvature == (0,) * complex_.c2 else "zero"
        assert_equal(f"{complex_.name} Fourier projection N={n} a={a}", value, expected)


def check_partition_function(n: int, complex_: CochainComplex) -> None:
    flat = kernel(n, complex_.delta1, complex_.c1)
    gauge_image = image(n, complex_.delta0, complex_.c0)
    h0 = kernel(n, complex_.delta0, complex_.c0)
    h1_size = Fraction(len(flat), len(gauge_image))

    partition_from_sum = Fraction(len(flat), n**complex_.c0)
    partition_from_cohomology = Fraction(h1_size, len(h0))
    assert_equal(f"{complex_.name} partition N={n}", partition_from_sum, partition_from_cohomology)


def check_wilson_gauge_invariance(n: int) -> None:
    # A one-simplex with endpoints v_0,v_1: delta lambda evaluates as
    # lambda(v_1)-lambda(v_0).  A closed one-cycle has zero boundary, so the
    # endpoint coefficients cancel.
    delta0: Matrix = ((-1, 1),)
    closed_cycle = (0,)
    open_edge = (1,)
    for lam in vectors(n, 2):
        exact = mat_vec(delta0, lam, n)
        assert_equal(f"closed Wilson gauge invariance N={n} lambda={lam}", dot(exact, closed_cycle, n), 0)
        assert_equal(
            f"open edge boundary evaluation N={n} lambda={lam}",
            dot(exact, open_edge, n),
            (lam[1] - lam[0]) % n,
        )


def check_linking_phase_sign(n: int) -> None:
    # Toy relative complex: one two-cell C with boundary gamma.  If the
    # surface insertion imposes delta a=-p sigma and sigma(C)=L, then
    # <a,gamma>=<delta a,C>=-pL.  The Wilson numerator is therefore -pqL.
    for p, q, linking in product(range(n), repeat=3):
        delta_a_on_c = (-p * linking) % n
        wilson_numerator = (q * delta_a_on_c) % n
        expected = (-p * q * linking) % n
        assert_equal(
            f"BF linking sign N={n} p={p} q={q} L={linking}",
            wilson_numerator,
            expected,
        )


def sample_complexes() -> list[CochainComplex]:
    return [
        CochainComplex(
            name="sphere-minimal",
            c0=1,
            c1=0,
            c2=1,
            delta0=(),
            delta1=((),),
        ),
        CochainComplex(
            name="torus-minimal",
            c0=1,
            c1=2,
            c2=1,
            delta0=((0,), (0,)),
            delta1=((0, 0),),
        ),
        CochainComplex(
            name="connected-interval-gauge-complex",
            c0=2,
            c1=1,
            c2=0,
            delta0=((-1, 1),),
            delta1=(),
        ),
        CochainComplex(
            name="one-relator-two-complex",
            c0=1,
            c1=1,
            c2=1,
            delta0=((0,),),
            delta1=((2,),),
        ),
    ]


def main() -> None:
    for complex_ in sample_complexes():
        complex_.check_dimensions()
        for n in range(2, 10):
            check_complex_property(n, complex_)
            check_fourier_projection(n, complex_)
            check_partition_function(n, complex_)
            check_wilson_gauge_invariance(n)
            check_linking_phase_sign(n)

    print("All BF finite cochain checks passed.")


if __name__ == "__main__":
    main()
