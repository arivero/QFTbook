#!/usr/bin/env python3
"""Finite Weyl-algebra checks for the massive scalar Weyl-net benchmark.

The continuum Weyl net in Volume IV uses compact-support partitions and the
Green-hyperbolic quotient.  This script checks only the finite symplectic
algebra of Weyl phases used after those analytic steps have produced a finite
decomposition of a generator.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


Vector = tuple[Fraction, ...]


def F(n: int, d: int = 1) -> Fraction:
    return Fraction(n, d)


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def add_vec(u: Vector, v: Vector) -> Vector:
    return tuple(a + b for a, b in zip(u, v, strict=True))


def neg_vec(u: Vector) -> Vector:
    return tuple(-a for a in u)


def zero_like(u: Vector) -> Vector:
    return tuple(F(0) for _ in u)


def sigma(u: Vector, v: Vector) -> Fraction:
    """Canonical alternating form on Q^4 with two symplectic planes."""

    return (
        u[0] * v[1]
        - u[1] * v[0]
        + u[2] * v[3]
        - u[3] * v[2]
    )


@dataclass(frozen=True)
class WeylElement:
    """Formal element exp(i phase) W(vector)."""

    phase: Fraction
    vector: Vector


def central(phase: Fraction, dimension: int = 4) -> WeylElement:
    return WeylElement(phase, tuple(F(0) for _ in range(dimension)))


def generator(u: Vector) -> WeylElement:
    return WeylElement(F(0), u)


def multiply(a: WeylElement, b: WeylElement) -> WeylElement:
    """Weyl product for W(u)W(v)=exp(-i sigma(u,v)/2)W(u+v)."""

    return WeylElement(
        a.phase + b.phase - sigma(a.vector, b.vector) / 2,
        add_vec(a.vector, b.vector),
    )


def star(a: WeylElement) -> WeylElement:
    """Involution: (exp(i phase) W(u))^*=exp(-i phase) W(-u)."""

    return WeylElement(-a.phase, neg_vec(a.vector))


def product(elements: list[WeylElement]) -> WeylElement:
    if not elements:
        return central(F(0))
    out = central(F(0), len(elements[0].vector))
    for elt in elements:
        out = multiply(out, elt)
    return out


def check_associativity() -> None:
    u = (F(1), F(2), F(-1), F(3))
    v = (F(0), F(5), F(2), F(-4))
    w = (F(3), F(-1), F(1), F(1))
    lhs = multiply(multiply(generator(u), generator(v)), generator(w))
    rhs = multiply(generator(u), multiply(generator(v), generator(w)))
    assert_equal("Weyl product associativity", lhs, rhs)


def check_commutator_phase() -> None:
    u = (F(2), F(-1), F(3), F(0))
    v = (F(1), F(4), F(-2), F(5))
    s = sigma(u, v)
    wu = generator(u)
    wv = generator(v)

    lhs = multiply(wu, wv)
    rhs = multiply(central(-s), multiply(wv, wu))
    assert_equal("W(u)W(v)=exp(-i sigma)W(v)W(u)", lhs, rhs)

    group_commutator = multiply(multiply(multiply(wu, wv), star(wu)), star(wv))
    assert_equal("Weyl group commutator phase", group_commutator, central(-s))


def check_locality_when_pairing_vanishes() -> None:
    u = (F(1), F(0), F(0), F(0))
    v = (F(0), F(0), F(1), F(0))
    assert_equal("chosen vectors are symplectically orthogonal", sigma(u, v), F(0))
    assert_equal(
        "orthogonal Weyl generators commute",
        multiply(generator(u), generator(v)),
        multiply(generator(v), generator(u)),
    )


def check_additivity_partition_phase() -> None:
    pieces = [
        (F(1), F(0), F(2), F(-1)),
        (F(0), F(3), F(-1), F(4)),
        (F(2), F(-2), F(0), F(1)),
    ]
    total = tuple(sum(piece[i] for piece in pieces) for i in range(4))
    raw_product = product([generator(piece) for piece in pieces])
    pair_sum = sum(sigma(a, b) for a, b in combinations(pieces, 2))
    compensated = multiply(central(pair_sum / 2), raw_product)
    assert_equal(
        "partition-of-support Weyl phase reconstructs W(sum u_j)",
        compensated,
        generator(total),
    )


def check_star_is_inverse_on_generators() -> None:
    u = (F(5), F(-3), F(7), F(2))
    wu = generator(u)
    assert_equal("W(u)^*=W(-u)", star(wu), generator(neg_vec(u)))
    assert_equal("W(u)W(u)^*=1", multiply(wu, star(wu)), central(F(0)))


def main() -> None:
    check_associativity()
    check_commutator_phase()
    check_locality_when_pairing_vanishes()
    check_additivity_partition_phase()
    check_star_is_inverse_on_generators()
    print("All free Weyl-net finite algebra checks passed.")


if __name__ == "__main__":
    main()
