#!/usr/bin/env python3
"""Finite algebra checks for the scalar four-point Mellin conventions."""

from __future__ import annotations

from fractions import Fraction


# Linear expressions in (Delta_1, Delta_2, Delta_3, Delta_4, s, t).
Expr = tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]
ZERO: Expr = (Fraction(0),) * 6


def expr(*coeffs: int | Fraction) -> Expr:
    return tuple(Fraction(c) for c in coeffs)  # type: ignore[return-value]


def add(a: Expr, b: Expr) -> Expr:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: Expr, b: Expr) -> Expr:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def neg(a: Expr) -> Expr:
    return tuple(-x for x in a)  # type: ignore[return-value]


def half(a: Expr) -> Expr:
    return tuple(x / 2 for x in a)  # type: ignore[return-value]


D1 = expr(1, 0, 0, 0, 0, 0)
D2 = expr(0, 1, 0, 0, 0, 0)
D3 = expr(0, 0, 1, 0, 0, 0)
D4 = expr(0, 0, 0, 1, 0, 0)
s = expr(0, 0, 0, 0, 1, 0)
t = expr(0, 0, 0, 0, 0, 1)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_delta_constraints() -> None:
    """Check sum_{j != i} delta_ij = Delta_i."""

    # u_M = Delta_1 + Delta_2 + Delta_3 + Delta_4 - s - t.
    delta12 = half(sub(add(D1, D2), s))
    delta34 = half(sub(add(D3, D4), s))
    delta14 = half(sub(add(D1, D4), t))
    delta23 = half(sub(add(D2, D3), t))
    delta13 = half(add(add(neg(D2), neg(D4)), add(s, t)))
    delta24 = half(add(add(neg(D1), neg(D3)), add(s, t)))

    assert_equal("constraint at point 1", add(add(delta12, delta13), delta14), D1)
    assert_equal("constraint at point 2", add(add(delta12, delta23), delta24), D2)
    assert_equal("constraint at point 3", add(add(delta13, delta23), delta34), D3)
    assert_equal("constraint at point 4", add(add(delta14, delta24), delta34), D4)


def check_prefactor_reduction() -> None:
    """Check the Mellin product reduces to the chapter's G(u,v) convention."""

    delta = {
        "12": half(sub(add(D1, D2), s)),
        "34": half(sub(add(D3, D4), s)),
        "14": half(sub(add(D1, D4), t)),
        "23": half(sub(add(D2, D3), t)),
        "13": half(add(add(neg(D2), neg(D4)), add(s, t))),
        "24": half(add(add(neg(D1), neg(D3)), add(s, t))),
    }
    mellin_exponent = {key: neg(value) for key, value in delta.items()}

    prefactor_exponent = {
        "12": neg(half(add(D1, D2))),
        "34": neg(half(add(D3, D4))),
        "24": half(sub(D1, D2)),
        "14": half(add(add(neg(D1), D2), sub(D3, D4))),
        "13": half(sub(neg(D3), neg(D4))),
        "23": ZERO,
    }

    a = half(s)
    b = half(add(add(t, neg(D2)), neg(D3)))
    expected = {
        "12": a,
        "34": a,
        "14": b,
        "23": b,
        "13": neg(add(a, b)),
        "24": neg(add(a, b)),
    }

    for key in sorted(expected):
        reduced = sub(mellin_exponent[key], prefactor_exponent[key])
        assert_equal(f"cross-ratio exponent X_{key}", reduced, expected[key])


def check_measure_jacobian() -> None:
    """Check d delta_12 d delta_14 = ds dt / 4 up to orientation."""

    d_delta12_ds = Fraction(-1, 2)
    d_delta12_dt = Fraction(0)
    d_delta14_ds = Fraction(0)
    d_delta14_dt = Fraction(-1, 2)
    determinant = d_delta12_ds * d_delta14_dt - d_delta12_dt * d_delta14_ds
    assert_equal("Mellin four-point Jacobian", determinant, Fraction(1, 4))


def check_ope_pole_exponent() -> None:
    """Check s = tau + 2m maps to u^(tau/2 + m)."""

    for tau_num in range(1, 8):
        tau = Fraction(tau_num, 3)
        for level in range(5):
            pole = tau + 2 * level
            exponent = pole / 2
            assert_equal(f"OPE exponent tau={tau} level={level}", exponent, tau / 2 + level)


def check_identical_crossing_permutation() -> None:
    """Check the identical-scalar transposition 2 <-> 4 sends s to t."""

    def identical_projection(a: Expr) -> tuple[Fraction, Fraction, Fraction]:
        """Substitute Delta_1=...=Delta_4=Delta."""

        return (sum(a[:4]), a[4], a[5])

    delta12 = half(sub(add(D1, D2), s))
    delta14 = half(sub(add(D1, D4), t))

    # For identical external dimensions, replacing labels 2 and 4 sends
    # delta_12 to delta_14.  Hence 2 Delta - 2 delta_12 maps to
    # 2 Delta - 2 delta_14, i.e. s maps to t.
    identical_delta = D1
    channel_from_delta12 = sub(add(identical_delta, identical_delta), add(delta12, delta12))
    channel_from_delta14 = sub(add(identical_delta, identical_delta), add(delta14, delta14))

    assert_equal("s channel expression", identical_projection(channel_from_delta12), identical_projection(s))
    assert_equal("t channel expression", identical_projection(channel_from_delta14), identical_projection(t))


def main() -> None:
    check_delta_constraints()
    check_prefactor_reduction()
    check_measure_jacobian()
    check_ope_pole_exponent()
    check_identical_crossing_permutation()
    print("All Mellin four-point convention checks passed.")


if __name__ == "__main__":
    main()
