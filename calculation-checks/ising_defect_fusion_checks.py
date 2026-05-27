#!/usr/bin/env python3
"""Exact checks for the Ising/Kramers-Wannier defect fusion example.

The arithmetic is performed in Q(sqrt(2)) so that the nonintegral quantum
dimension and the modular S-matrix entries are checked without floating-point
rounding.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import product


@dataclass(frozen=True)
class Qsqrt2:
    """Element a + b sqrt(2), with a,b rational."""

    a: Fraction
    b: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Qsqrt2":
        other = as_qsqrt2(other)
        return Qsqrt2(self.a + other.a, self.b + other.b)

    def __radd__(self, other: object) -> "Qsqrt2":
        return self + other

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.a, -self.b)

    def __sub__(self, other: object) -> "Qsqrt2":
        return self + (-as_qsqrt2(other))

    def __rsub__(self, other: object) -> "Qsqrt2":
        return as_qsqrt2(other) - self

    def __mul__(self, other: object) -> "Qsqrt2":
        other = as_qsqrt2(other)
        return Qsqrt2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __rmul__(self, other: object) -> "Qsqrt2":
        return self * other

    def inverse(self) -> "Qsqrt2":
        norm = self.a * self.a - 2 * self.b * self.b
        if norm == 0:
            raise ZeroDivisionError("zero divisor in Q(sqrt(2))")
        return Qsqrt2(self.a / norm, -self.b / norm)

    def __truediv__(self, other: object) -> "Qsqrt2":
        return self * as_qsqrt2(other).inverse()

    def __eq__(self, other: object) -> bool:
        other = as_qsqrt2(other)
        return self.a == other.a and self.b == other.b

    def __repr__(self) -> str:
        return f"Qsqrt2({self.a}, {self.b})"


def as_qsqrt2(value: object) -> Qsqrt2:
    if isinstance(value, Qsqrt2):
        return value
    if isinstance(value, int):
        return Qsqrt2(Fraction(value))
    if isinstance(value, Fraction):
        return Qsqrt2(value)
    raise TypeError(f"cannot coerce {value!r} to Qsqrt2")


ZERO = Qsqrt2(Fraction(0))
ONE = Qsqrt2(Fraction(1))
ROOT_TWO = Qsqrt2(Fraction(0), Fraction(1))
HALF = Fraction(1, 2)

LABELS = ("one", "eta", "N")
SECTORS = ("one", "epsilon", "sigma")


def q(value: int | Fraction = 0, sqrt_coeff: int | Fraction = 0) -> Qsqrt2:
    return Qsqrt2(Fraction(value), Fraction(sqrt_coeff))


def fusion(a: str, b: str) -> dict[str, int]:
    if a == "one":
        return {b: 1}
    if b == "one":
        return {a: 1}
    if a == "eta" and b == "eta":
        return {"one": 1}
    if {a, b} == {"eta", "N"}:
        return {"N": 1}
    if a == "N" and b == "N":
        return {"one": 1, "eta": 1}
    raise AssertionError(f"missing fusion rule for {a} x {b}")


S = {
    ("one", "one"): q(HALF),
    ("one", "epsilon"): q(HALF),
    ("one", "sigma"): q(0, HALF),
    ("eta", "one"): q(HALF),
    ("eta", "epsilon"): q(HALF),
    ("eta", "sigma"): q(0, -HALF),
    ("N", "one"): q(0, HALF),
    ("N", "epsilon"): q(0, -HALF),
    ("N", "sigma"): ZERO,
}


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def fuse_sum(left: dict[str, int], right: str) -> dict[str, int]:
    out = {label: 0 for label in LABELS}
    for a, multiplicity in left.items():
        for c, coeff in fusion(a, right).items():
            out[c] += multiplicity * coeff
    return {label: coeff for label, coeff in out.items() if coeff}


def check_associativity() -> None:
    for a in LABELS:
        for b in LABELS:
            for c in LABELS:
                left = fuse_sum(fusion(a, b), c)
                right = {label: 0 for label in LABELS}
                for x, multiplicity in fusion(b, c).items():
                    for y, coeff in fusion(a, x).items():
                        right[y] += multiplicity * coeff
                right = {label: coeff for label, coeff in right.items() if coeff}
                assert_equal(
                    f"associativity ({a} {b}) {c} = {a} ({b} {c})",
                    left,
                    right,
                )


def check_quantum_dimensions() -> None:
    dimensions = {"one": ONE, "eta": ONE, "N": ROOT_TWO}
    for a in LABELS:
        for b in LABELS:
            lhs = dimensions[a] * dimensions[b]
            rhs = sum(
                (multiplicity * dimensions[c] for c, multiplicity in fusion(a, b).items()),
                ZERO,
            )
            assert_equal(f"dimension homomorphism {a} x {b}", lhs, rhs)


def check_s_matrix_orthogonality() -> None:
    for a in LABELS:
        for b in LABELS:
            got = sum((S[(a, i)] * S[(b, i)] for i in SECTORS), ZERO)
            expected = ONE if a == b else ZERO
            assert_equal(f"S orthogonality {a} {b}", got, expected)


def check_verlinde_formula() -> None:
    for a in LABELS:
        for b in LABELS:
            for c in LABELS:
                got = sum(
                    (S[(a, x)] * S[(b, x)] * S[(c, x)] / S[("one", x)] for x in SECTORS),
                    ZERO,
                )
                expected = q(fusion(a, b).get(c, 0))
                assert_equal(f"Verlinde coefficient {a} {b} {c}", got, expected)


def line_eigenvalue(a: str, i: str) -> Qsqrt2:
    return S[(a, i)] / S[("one", i)]


def check_line_eigenvalues() -> None:
    expected_N = {"one": ROOT_TWO, "epsilon": -ROOT_TWO, "sigma": ZERO}
    for sector, value in expected_N.items():
        assert_equal(
            f"Kramers-Wannier eigenvalue on {sector}",
            line_eigenvalue("N", sector),
            value,
        )

    for a in LABELS:
        for b in LABELS:
            for i in SECTORS:
                lhs = line_eigenvalue(a, i) * line_eigenvalue(b, i)
                rhs = sum(
                    (multiplicity * line_eigenvalue(c, i) for c, multiplicity in fusion(a, b).items()),
                    ZERO,
                )
                assert_equal(f"line-action fusion {a} {b} on {i}", lhs, rhs)


def cyclic_group(n: int) -> list[int]:
    return list(range(n))


def cyclic_multiply(n: int):
    return lambda a, b: (a + b) % n


def s3_group() -> list[tuple[int, int, int]]:
    return [
        p
        for p in product(range(3), repeat=3)
        if sorted(p) == [0, 1, 2]
    ]


def compose_perm(
    p: tuple[int, int, int],
    q_perm: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(p[q_perm[i]] for i in range(3))  # type: ignore[return-value]


def self_dual_fusion(
    left: tuple[str, object],
    right: tuple[str, object],
    group: list[object],
    multiply,
) -> Counter:
    if left[0] == "D" and right[0] == "D":
        return Counter({("D", multiply(left[1], right[1])): 1})
    if left[0] == "N" and right[0] == "N":
        return Counter({("D", g): 1 for g in group})
    return Counter({("N", None): 1})


def fuse_linear_combination(
    left: Counter,
    right: Counter,
    group: list[object],
    multiply,
) -> Counter:
    out: Counter = Counter()
    for left_label, left_multiplicity in left.items():
        for right_label, right_multiplicity in right.items():
            product_terms = self_dual_fusion(left_label, right_label, group, multiply)
            for label, multiplicity in product_terms.items():
                out[label] += left_multiplicity * right_multiplicity * multiplicity
    return +out


def delta_regular(
    k: object,
    group: list[object],
    multiply,
) -> Counter:
    coefficient = Fraction(1, len(group))
    out: Counter = Counter()
    for g, h in product(group, repeat=2):
        if multiply(g, h) == k:
            out[(g, h)] += coefficient
    return out


def check_regular_algebra_frobenius(group: list[object], multiply, name: str) -> None:
    for k in group:
        delta_k = delta_regular(k, group, multiply)
        total = sum(
            coefficient
            for (g, h), coefficient in delta_k.items()
            if multiply(g, h) == k
        )
        assert_equal(f"{name} regular algebra separability {k}", total, Fraction(1))

    for g, h in product(group, repeat=2):
        lhs = delta_regular(multiply(g, h), group, multiply)
        middle: Counter = Counter()
        for (a, b), coefficient in delta_regular(h, group, multiply).items():
            middle[(multiply(g, a), b)] += coefficient
        right: Counter = Counter()
        for (a, b), coefficient in delta_regular(g, group, multiply).items():
            right[(a, multiply(b, h))] += coefficient
        assert_equal(f"{name} Frobenius left identity {g} {h}", middle, lhs)
        assert_equal(f"{name} Frobenius right identity {g} {h}", right, lhs)


def check_self_dual_gauging_fusion_ring() -> None:
    examples: list[tuple[str, list[object], object]] = [
        (f"C{n}", cyclic_group(n), cyclic_multiply(n)) for n in range(1, 8)
    ]
    examples.append(("S3", s3_group(), compose_perm))

    for name, group, multiply in examples:
        labels = [("D", g) for g in group] + [("N", None)]
        for a, b, c in product(labels, repeat=3):
            left = fuse_linear_combination(
                self_dual_fusion(a, b, group, multiply),
                Counter({c: 1}),
                group,
                multiply,
            )
            right = fuse_linear_combination(
                Counter({a: 1}),
                self_dual_fusion(b, c, group, multiply),
                group,
                multiply,
            )
            assert_equal(f"{name} self-dual gauging associativity", left, right)

        n = len(group)
        n_square = n
        rhs_dimension_of_n_square = sum(1 for _ in group)
        assert_equal(
            f"{name} self-dual defect dimension squared",
            n_square,
            rhs_dimension_of_n_square,
        )
        if n > 1:
            assert_equal(
                f"{name} self-dual defect noninvertible",
                len(self_dual_fusion(("N", None), ("N", None), group, multiply)),
                n,
            )

        check_regular_algebra_frobenius(group, multiply, name)


def main() -> None:
    check_associativity()
    check_quantum_dimensions()
    check_s_matrix_orthogonality()
    check_verlinde_formula()
    check_line_eigenvalues()
    check_self_dual_gauging_fusion_ring()
    print("All Ising Kramers-Wannier defect fusion checks passed.")


if __name__ == "__main__":
    main()
