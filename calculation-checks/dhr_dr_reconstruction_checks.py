#!/usr/bin/env python3
"""Finite pointed Doplicher--Roberts reconstruction checks.

The check models the categorical part of Volume IV, Chapter 4 for the pointed
sector category with simple objects labelled by Z/NZ.  Tensor automorphisms of
the one-dimensional fiber functor are characters, and averaging over the
reconstructed compact group keeps exactly the neutral degree.  It also checks
the finite crossed-product field core for an invertible pointed sector.
"""


def assert_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def check_tensor_automorphisms(n: int) -> None:
    # Represent the phase exp(2*pi*i*k*q/n) by its exponent k*q mod n.
    # Tensor compatibility is equality of exponents modulo n.
    for k in range(n):
        for q in range(n):
            for r in range(n):
                lhs = (k * ((q + r) % n)) % n
                rhs = ((k * q) + (k * r)) % n
                assert_equal(f"tensor compatibility n={n} k={k} q={q} r={r}", lhs, rhs)

    # Pointwise multiplication of tensor automorphisms is addition of the
    # exponent label k.  This gives the reconstructed group mu_n.
    identity = 0
    for k in range(n):
        inverse = (-k) % n
        assert_equal(f"identity left n={n} k={k}", (identity + k) % n, k)
        assert_equal(f"identity right n={n} k={k}", (k + identity) % n, k)
        assert_equal(f"inverse n={n} k={k}", (k + inverse) % n, identity)


def check_fixed_degree_projection(n: int) -> None:
    # A homogeneous degree q survives averaging over mu_n iff every character
    # value zeta^q is trivial.  In exponent form this means m*q = 0 mod n for
    # every group element m.
    for q in range(n):
        invariant = all((m * q) % n == 0 for m in range(n))
        assert_equal(f"fixed degree n={n} q={q}", invariant, q == 0)


def multiply_basis(n: int, left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int] | None:
    """Multiply e_i u^q by e_j u^r in C^n cross_rho Z/NZ.

    The automorphism rho cyclically shifts idempotents by rho(e_j)=e_{j+1}.
    Thus rho^q(e_j)=e_{j+q}.  The product of idempotents is zero unless the
    idempotent labels agree.
    """
    i, q = left
    j, r = right
    shifted_j = (j + q) % n
    if i != shifted_j:
        return None
    return (i, (q + r) % n)


def star_basis(n: int, basis: tuple[int, int]) -> tuple[int, int]:
    """Involution of e_i u^q: (e_i u^q)^* = rho^{-q}(e_i) u^{-q}."""
    i, q = basis
    return ((i - q) % n, (-q) % n)


def check_crossed_product_core(n: int) -> None:
    basis = [(i, q) for i in range(n) for q in range(n)]

    for x in basis:
        for y in basis:
            for z in basis:
                xy = multiply_basis(n, x, y)
                yz = multiply_basis(n, y, z)
                left = None if xy is None else multiply_basis(n, xy, z)
                right = None if yz is None else multiply_basis(n, x, yz)
                assert_equal(f"crossed-product associativity n={n} x={x} y={y} z={z}", left, right)

    for x in basis:
        assert_equal(f"star involutive n={n} x={x}", star_basis(n, star_basis(n, x)), x)
        for y in basis:
            xy = multiply_basis(n, x, y)
            lhs = None if xy is None else star_basis(n, xy)
            right_product = multiply_basis(n, star_basis(n, y), star_basis(n, x))
            assert_equal(f"star anti-multiplicative n={n} x={x} y={y}", lhs, right_product)

    # Averaging over the dual group kills every nonzero crossed-product degree.
    for i, q in basis:
        invariant = all((m * q) % n == 0 for m in range(n))
        assert_equal(f"crossed-product fixed degree n={n} i={i} q={q}", invariant, q == 0)


def main() -> None:
    for n in range(2, 13):
        check_tensor_automorphisms(n)
        check_fixed_degree_projection(n)
        check_crossed_product_core(n)
    print("All finite pointed DHR/DR reconstruction and crossed-product checks passed.")


if __name__ == "__main__":
    main()
