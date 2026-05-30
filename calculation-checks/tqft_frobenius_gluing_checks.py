#!/usr/bin/env python3
"""Exact finite checks for the 2D Frobenius-algebra TQFT construction.

The bordism-functoriality chapter proves that a commutative Frobenius
algebra supplies the generators and relations of an ordinary oriented
two-dimensional TQFT.  This script checks the convention-sensitive formulas
for the semisimple idempotent model A = k^r:

* the inverse pairing tensor gives the cylinder identity;
* the adjoint comultiplication obeys the Frobenius neck-exchange identity;
* pair-of-pants gluing gives associativity;
* the genus-g closed-surface value is sum_alpha lambda_alpha^(1-g).
* the semisimple separability idempotent e = sum_alpha p_alpha tensor p_alpha
  splits the multiplication map A^e -> A and gives HH_0(A)=A in the
  commutative case.

All arithmetic is exact rational arithmetic.  The script does not replace the
proof in the text; it is a reproducible check of the displayed formulas.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

Vector = tuple[Fraction, ...]
Tensor2 = tuple[Fraction, ...]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def basis_vector(n: int, index: int) -> Vector:
    return tuple(Fraction(1 if i == index else 0) for i in range(n))


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def mul(a: Vector, b: Vector) -> Vector:
    return tuple(x * y for x, y in zip(a, b))


def unit(n: int) -> Vector:
    return tuple(Fraction(1) for _ in range(n))


def trace(weights: Vector, a: Vector) -> Fraction:
    return sum(w * x for w, x in zip(weights, a))


def pairing(weights: Vector, a: Vector, b: Vector) -> Fraction:
    return trace(weights, mul(a, b))


def tensor_index(n: int, i: int, j: int) -> int:
    return i * n + j


def delta(weights: Vector, a: Vector) -> Tensor2:
    n = len(weights)
    out = [Fraction(0) for _ in range(n * n)]
    for i in range(n):
        out[tensor_index(n, i, i)] = a[i] / weights[i]
    return tuple(out)


def multiply_tensor(n: int, tensor: Tensor2) -> Vector:
    out = [Fraction(0) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                out[i] += tensor[tensor_index(n, i, j)]
    return tuple(out)


def tensor_product_mul(n: int, left: Tensor2, right: Tensor2) -> Tensor2:
    out = [Fraction(0) for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            out[tensor_index(n, i, j)] = (
                left[tensor_index(n, i, j)] * right[tensor_index(n, i, j)]
            )
    return tuple(out)


def left_tensor_action(a: Vector, tensor: Tensor2) -> Tensor2:
    n = len(a)
    out = [Fraction(0) for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            out[tensor_index(n, i, j)] = a[i] * tensor[tensor_index(n, i, j)]
    return tuple(out)


def right_tensor_action(tensor: Tensor2, a: Vector) -> Tensor2:
    n = len(a)
    out = [Fraction(0) for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            out[tensor_index(n, i, j)] = tensor[tensor_index(n, i, j)] * a[j]
    return tuple(out)


def tensor_pairing(weights: Vector, tensor: Tensor2, b: Vector, c: Vector) -> Fraction:
    n = len(weights)
    total = Fraction(0)
    for i in range(n):
        for j in range(n):
            total += (
                tensor[tensor_index(n, i, j)]
                * weights[i]
                * b[i]
                * weights[j]
                * c[j]
            )
    return total


def scalar_mul(c: Fraction, a: Vector) -> Vector:
    return tuple(c * x for x in a)


def cylinder_from_inverse_pairing(weights: Vector, a: Vector) -> Vector:
    n = len(weights)
    out = tuple(Fraction(0) for _ in range(n))
    for i in range(n):
        e_i = basis_vector(n, i)
        e_dual_i = scalar_mul(Fraction(1, 1) / weights[i], e_i)
        coefficient = pairing(weights, e_dual_i, a)
        out = add(out, scalar_mul(coefficient, e_i))
    return out


def left_neck(weights: Vector, a: Vector, b: Vector) -> Tensor2:
    """(m tensor id)(id tensor Delta)(a tensor b)."""

    n = len(weights)
    out = [Fraction(0) for _ in range(n * n)]
    delta_b = delta(weights, b)
    for j in range(n):
        for k in range(n):
            out[tensor_index(n, j, k)] += a[j] * delta_b[tensor_index(n, j, k)]
    return tuple(out)


def right_neck(weights: Vector, a: Vector, b: Vector) -> Tensor2:
    """(id tensor m)(Delta tensor id)(a tensor b)."""

    n = len(weights)
    out = [Fraction(0) for _ in range(n * n)]
    delta_a = delta(weights, a)
    for i in range(n):
        for j in range(n):
            out[tensor_index(n, i, j)] += delta_a[tensor_index(n, i, j)] * b[j]
    return tuple(out)


def euler_element(weights: Vector) -> Vector:
    return tuple(Fraction(1, 1) / w for w in weights)


def separability_idempotent(n: int) -> Tensor2:
    out = [Fraction(0) for _ in range(n * n)]
    for i in range(n):
        out[tensor_index(n, i, i)] = Fraction(1)
    return tuple(out)


def separability_split(a: Vector) -> Tensor2:
    n = len(a)
    out = [Fraction(0) for _ in range(n * n)]
    for i in range(n):
        out[tensor_index(n, i, i)] = a[i]
    return tuple(out)


def pointwise_power(a: Vector, power: int) -> Vector:
    return tuple(x**power for x in a)


def genus_value_by_handles(weights: Vector, genus: int) -> Fraction:
    euler = euler_element(weights)
    return trace(weights, pointwise_power(euler, genus))


def genus_value_closed_form(weights: Vector, genus: int) -> Fraction:
    return sum(w ** (1 - genus) for w in weights)


def check_separability_and_hh0(weights: Vector, samples: list[Vector]) -> None:
    n = len(weights)
    e = separability_idempotent(n)
    assert_equal("separability normalization", multiply_tensor(n, e), unit(n))
    assert_equal("separability idempotent", tensor_product_mul(n, e, e), e)

    for a in samples:
        assert_equal("separability centrality", left_tensor_action(a, e), right_tensor_action(e, a))
        assert_equal("separability splitting", multiply_tensor(n, separability_split(a)), a)

    for a, b in product(samples, repeat=2):
        commutator = add(mul(a, b), scalar_mul(Fraction(-1), mul(b, a)))
        assert_equal("HH0 commutator vanishes for k^r", commutator, tuple(Fraction(0) for _ in range(n)))


def check_frobenius_identities(weights: Vector) -> None:
    n = len(weights)
    samples = [basis_vector(n, i) for i in range(n)]
    samples.append(unit(n))
    samples.append(tuple(Fraction(i + 2, i + 3) for i in range(n)))

    for a in samples:
        assert_equal("cylinder identity", cylinder_from_inverse_pairing(weights, a), a)

    for a, b, c in product(samples, repeat=3):
        assert_equal("associativity", mul(mul(a, b), c), mul(a, mul(b, c)))
        assert_equal("commutativity", mul(a, b), mul(b, a))

    for a, b in product(samples, repeat=2):
        middle = delta(weights, mul(a, b))
        assert_equal("left Frobenius neck exchange", left_neck(weights, a, b), middle)
        assert_equal("right Frobenius neck exchange", right_neck(weights, a, b), middle)
        for c in samples:
            assert_equal(
                "adjointness of Delta and multiplication",
                tensor_pairing(weights, delta(weights, a), b, c),
                trace(weights, mul(mul(a, b), c)),
            )

    for genus in range(0, 7):
        assert_equal(
            f"genus-{genus} partition function",
            genus_value_by_handles(weights, genus),
            genus_value_closed_form(weights, genus),
        )

    check_separability_and_hh0(weights, samples)


def main() -> None:
    check_frobenius_identities((Fraction(2),))
    check_frobenius_identities((Fraction(2), Fraction(3)))
    check_frobenius_identities((Fraction(2), Fraction(3), Fraction(5), Fraction(7)))
    print("All 2D Frobenius TQFT gluing checks passed.")


if __name__ == "__main__":
    main()
