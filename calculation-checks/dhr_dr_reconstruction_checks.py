#!/usr/bin/env python3
"""Finite pointed Doplicher--Roberts reconstruction checks.

The check models the categorical part of Volume IV, Chapter 4 for the pointed
sector category with simple objects labelled by Z/NZ.  Tensor automorphisms of
the one-dimensional fiber functor are characters, and averaging over the
reconstructed compact group keeps exactly the neutral degree.
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


def main() -> None:
    for n in range(2, 13):
        check_tensor_automorphisms(n)
        check_fixed_degree_projection(n)
    print("All finite pointed DHR/DR reconstruction checks passed.")


if __name__ == "__main__":
    main()
