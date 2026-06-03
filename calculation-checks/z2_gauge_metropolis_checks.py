#!/usr/bin/env python3
"""Finite checks for the 3D Z2 lattice gauge companion script."""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

import numpy as np

from check_utils import assert_close as _assert_close


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "z2_gauge_3d_metropolis.py"
spec = importlib.util.spec_from_file_location("z2_gauge_3d_metropolis", SCRIPT)
z2 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = z2
spec.loader.exec_module(z2)


def flipped(links: np.ndarray, site: tuple[int, int, int], mu: int) -> np.ndarray:
    result = links.copy()
    z2.flip_link_in_place(result, site, mu)
    return result


def check_local_score_change() -> None:
    rng = np.random.default_rng(20260526)
    links = z2.random_links(3, rng)
    for x0 in range(3):
        for x1 in range(3):
            for x2 in range(3):
                site = (x0, x1, x2)
                for mu in range(3):
                    direct = z2.total_plaquette_score(flipped(links, site, mu)) - z2.total_plaquette_score(links)
                    local = z2.local_score_change_for_flip(links, site, mu)
                    if direct != local:
                        raise AssertionError("local Z2 gauge score change does not match total score difference")


def check_pairwise_detailed_balance() -> None:
    rng = np.random.default_rng(314159)
    beta = 0.73
    links = z2.random_links(3, rng)
    proposal = 1.0 / (3 * 3**3)
    for _ in range(40):
        site = (
            int(rng.integers(3)),
            int(rng.integers(3)),
            int(rng.integers(3)),
        )
        mu = int(rng.integers(3))
        target = flipped(links, site, mu)
        delta = z2.total_plaquette_score(target) - z2.total_plaquette_score(links)
        forward = proposal * min(1.0, math.exp(beta * delta))
        backward = proposal * min(1.0, math.exp(-beta * delta))
        lhs = math.exp(beta * z2.total_plaquette_score(links)) * forward
        rhs = math.exp(beta * z2.total_plaquette_score(target)) * backward
        _assert_close("pairwise detailed balance for a Z2 gauge link flip", lhs, rhs, rtol=1.0e-10)
        links = target


def check_gauge_invariance() -> None:
    rng = np.random.default_rng(271828)
    links = z2.random_links(4, rng)
    signs = rng.choice(np.array([-1, 1], dtype=np.int8), size=(4, 4, 4))
    transformed = z2.gauge_transform(links, signs)
    if z2.total_plaquette_score(links) != z2.total_plaquette_score(transformed):
        raise AssertionError("plaquette action is not gauge invariant")
    loop_before = z2.wilson_loop_rectangle(links, 1, 2)
    loop_after = z2.wilson_loop_rectangle(transformed, 1, 2)
    _assert_close("Wilson loop gauge invariance", loop_before, loop_after, tol=1.0e-12)


def check_one_plaquette_loop_identity() -> None:
    rng = np.random.default_rng(12345)
    links = z2.random_links(5, rng)
    plaquette_mean = z2.total_plaquette_score(links) / float(3 * 5**3)
    loop_mean = z2.wilson_loop_rectangle(links, 1, 1)
    _assert_close("1x1 Wilson loop average equals plaquette average", plaquette_mean, loop_mean, tol=1.0e-12)


def main() -> None:
    check_local_score_change()
    check_pairwise_detailed_balance()
    check_gauge_invariance()
    check_one_plaquette_loop_identity()
    print("All finite Z2 gauge Metropolis checks passed.")


if __name__ == "__main__":
    main()
