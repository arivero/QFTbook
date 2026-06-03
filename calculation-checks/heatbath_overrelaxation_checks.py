#!/usr/bin/env python3
"""Finite algebra checks for heat-bath and SU(2) overrelaxation updates."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import importlib.util
import sys
from fractions import Fraction
from itertools import permutations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "qft_scripts"
SCRIPT = SCRIPT_DIR / "su2_gauge_4d_heatbath_overrelaxation.py"
sys.path.insert(0, str(SCRIPT_DIR))
spec = importlib.util.spec_from_file_location("su2_gauge_4d_heatbath_overrelaxation", SCRIPT)
hb = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = hb
spec.loader.exec_module(hb)


Vector4 = tuple[Fraction, Fraction, Fraction, Fraction]
Matrix4 = tuple[Vector4, Vector4, Vector4, Vector4]


def qmul(a: Vector4, b: Vector4) -> Vector4:
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    )


def qconj(a: Vector4) -> Vector4:
    return (a[0], -a[1], -a[2], -a[3])


def qnorm2(a: Vector4) -> Fraction:
    return sum(x * x for x in a)


def left_matrix(a: Vector4) -> Matrix4:
    a0, a1, a2, a3 = a
    return (
        (a0, -a1, -a2, -a3),
        (a1, a0, -a3, a2),
        (a2, a3, a0, -a1),
        (a3, -a2, a1, a0),
    )


def right_matrix(a: Vector4) -> Matrix4:
    a0, a1, a2, a3 = a
    return (
        (a0, -a1, -a2, -a3),
        (a1, a0, a3, -a2),
        (a2, -a3, a0, a1),
        (a3, a2, -a1, a0),
    )


def matmul(a: Matrix4, b: Matrix4) -> Matrix4:
    rows: list[Vector4] = []
    for i in range(4):
        row: Vector4 = (
            sum(a[i][k] * b[k][0] for k in range(4)),
            sum(a[i][k] * b[k][1] for k in range(4)),
            sum(a[i][k] * b[k][2] for k in range(4)),
            sum(a[i][k] * b[k][3] for k in range(4)),
        )
        rows.append(row)
    return (rows[0], rows[1], rows[2], rows[3])


def transpose(a: Matrix4) -> Matrix4:
    return (
        (a[0][0], a[1][0], a[2][0], a[3][0]),
        (a[0][1], a[1][1], a[2][1], a[3][1]),
        (a[0][2], a[1][2], a[2][2], a[3][2]),
        (a[0][3], a[1][3], a[2][3], a[3][3]),
    )


def det4(a: Matrix4) -> Fraction:
    total = Fraction(0)
    for perm in permutations(range(4)):
        inversions = sum(
            1
            for i in range(4)
            for j in range(i + 1, 4)
            if perm[i] > perm[j]
        )
        sign = -1 if inversions % 2 else 1
        term = Fraction(sign)
        for i, j in enumerate(perm):
            term *= a[i][j]
        total += term
    return total


def identity4() -> Matrix4:
    return (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )


def assert_equal(got: object, expected: object, label: str) -> None:
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def check_heat_bath_conditional_balance() -> None:
    """Check pi(x,y) K((x,y),(x',y)) symmetry for finite conditionals."""

    y_weights = {"a": Fraction(2, 5), "b": Fraction(3, 5)}
    conditionals = {
        "a": {0: Fraction(1, 7), 1: Fraction(2, 7), 2: Fraction(4, 7)},
        "b": {0: Fraction(5, 11), 1: Fraction(3, 11), 2: Fraction(3, 11)},
    }

    for y, y_weight in y_weights.items():
        for x, px in conditionals[y].items():
            for xp, pxp in conditionals[y].items():
                forward = y_weight * px * pxp
                backward = y_weight * pxp * px
                assert_equal(
                    forward,
                    backward,
                    f"heat-bath balance y={y}, {x}->{xp}",
                )


def overrelax(w: Vector4, u: Vector4) -> Vector4:
    winv = qconj(w)
    return qmul(qmul(winv, qconj(u)), winv)


def check_su2_staple_reduction_and_overrelaxation() -> None:
    """Check V=cW reduction and U -> W^{-1} U^{-1} W^{-1} identities."""

    w: Vector4 = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    u: Vector4 = (Fraction(1, 2), -Fraction(1, 2), Fraction(1, 2), -Fraction(1, 2))
    c = Fraction(7, 3)
    v: Vector4 = (c * w[0], c * w[1], c * w[2], c * w[3])

    assert_equal(qnorm2(w), Fraction(1), "normalized staple W")
    assert_equal(qnorm2(u), Fraction(1), "link U")
    assert_equal(qnorm2(v), c * c, "staple norm c")

    local_score = qmul(u, v)[0]
    reduced_score = c * qmul(u, w)[0]
    assert_equal(local_score, reduced_score, "local staple score reduction")

    reflected = overrelax(w, u)
    reflected_twice = overrelax(w, reflected)
    assert_equal(reflected_twice, u, "overrelaxation involution")
    assert_equal(qnorm2(reflected), Fraction(1), "overrelaxed link remains SU(2)")
    assert_equal(
        qmul(reflected, w)[0],
        qmul(u, w)[0],
        "overrelaxation score preservation",
    )


def check_overrelaxation_orthogonal_map() -> None:
    """Check the S^3 map is orthogonal, hence surface-measure preserving."""

    w: Vector4 = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    winv = qconj(w)
    conjugation: Matrix4 = (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), -Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), -Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), -Fraction(1)),
    )
    transform = matmul(matmul(left_matrix(winv), right_matrix(winv)), conjugation)
    assert_equal(
        matmul(transpose(transform), transform),
        identity4(),
        "overrelaxation orthogonality",
    )
    assert_equal(abs(det4(transform)), Fraction(1), "overrelaxation absolute Jacobian")


def check_companion_script_local_identities() -> None:
    """Check that the script's staple and overrelaxation match the action."""

    rng = np.random.default_rng(20260527)
    links = hb.su2.random_links(2, rng)
    for _ in range(20):
        site = (
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
        )
        mu = int(rng.integers(hb.su2.DIRECTIONS))
        direct = hb.su2.adjacent_plaquette_score(links, site, mu)
        staple_score = hb.local_score_from_staple(links, site, mu)
        assert_close("script staple local score", staple_score, direct, tol=1.0e-10)

        before = hb.local_score_from_staple(links, site, mu)
        hb.overrelax_update_link(links, site, mu)
        after = hb.local_score_from_staple(links, site, mu)
        assert_close("script overrelaxation local score", after, before, tol=1.0e-10)
        assert_close(
            "script overrelaxation unit link",
            float(np.linalg.norm(links[site + (mu,)])),
            1.0,
            tol=1.0e-12,
        )

        hb.heatbath_update_link(links, site, mu, beta=1.3, rng=rng)
        assert_close(
            "script heat-bath unit link",
            float(np.linalg.norm(links[site + (mu,)])),
            1.0,
            tol=1.0e-12,
        )


def main() -> None:
    check_heat_bath_conditional_balance()
    check_su2_staple_reduction_and_overrelaxation()
    check_overrelaxation_orthogonal_map()
    check_companion_script_local_identities()
    print("All finite heat-bath and overrelaxation checks passed.")


if __name__ == "__main__":
    main()
