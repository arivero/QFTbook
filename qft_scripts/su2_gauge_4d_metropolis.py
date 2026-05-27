#!/usr/bin/env python3
"""Finite 4D SU(2) lattice gauge Metropolis sampler.

The script samples the finite periodic hypercubic lattice model

    probability(U) proportional to exp(beta * sum_p 1/2 Re Tr U_p),

where links are SU(2) matrices represented by unit quaternions.  The local
proposal left-multiplies one link by a small random SU(2) element whose law is
invariant under inversion.  This is a finite-regulator demonstration for the
monograph: it checks compact gauge variables, Haar-symmetric proposals,
gauge-invariant Wilson loops, and finite-cutoff detailed balance.  It is not
a continuum extrapolation and not a production heat-bath or HMC code.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import numpy as np


DIRECTIONS = 4


@dataclass
class RunConfig:
    L: int
    beta: float
    proposal_width: float
    sweeps: int
    therm: int
    seed: int
    rectangle_r: int
    rectangle_t: int


def qnormalize(q: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(q))
    if norm == 0.0:
        raise ValueError("zero quaternion cannot be normalized")
    return np.asarray(q, dtype=float) / norm


def qmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return np.array(
        [
            a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
        ],
        dtype=float,
    )


def qconj(q: np.ndarray) -> np.ndarray:
    return np.array([q[0], -q[1], -q[2], -q[3]], dtype=float)


def random_su2(rng: np.random.Generator) -> np.ndarray:
    return qnormalize(rng.normal(size=4))


def random_small_su2(rng: np.random.Generator, width: float) -> np.ndarray:
    if width <= 0.0:
        raise ValueError("proposal width must be positive")
    axis = rng.normal(size=3)
    axis_norm = float(np.linalg.norm(axis))
    if axis_norm == 0.0:
        axis = np.array([1.0, 0.0, 0.0], dtype=float)
    else:
        axis = axis / axis_norm
    angle = float(rng.uniform(-width, width))
    return np.array([math.cos(angle), *(math.sin(angle) * axis)], dtype=float)


def shift_site(site: tuple[int, int, int, int], direction: int, step: int, L: int) -> tuple[int, int, int, int]:
    coords = list(site)
    coords[direction] = (coords[direction] + step) % L
    return (coords[0], coords[1], coords[2], coords[3])


def random_links(L: int, rng: np.random.Generator) -> np.ndarray:
    links = np.empty((L, L, L, L, DIRECTIONS, 4), dtype=float)
    for index in np.ndindex((L, L, L, L, DIRECTIONS)):
        links[index] = random_su2(rng)
    return links


def plaquette(links: np.ndarray, site: tuple[int, int, int, int], mu: int, nu: int) -> np.ndarray:
    if mu == nu:
        raise ValueError("plaquette directions must be distinct")
    L = links.shape[0]
    x_mu = shift_site(site, mu, 1, L)
    x_nu = shift_site(site, nu, 1, L)
    return qmul(
        qmul(qmul(links[site + (mu,)], links[x_mu + (nu,)]), qconj(links[x_nu + (mu,)])),
        qconj(links[site + (nu,)]),
    )


def total_plaquette_score(links: np.ndarray) -> float:
    L = links.shape[0]
    score = 0.0
    for site in np.ndindex((L, L, L, L)):
        for mu in range(DIRECTIONS):
            for nu in range(mu + 1, DIRECTIONS):
                score += float(plaquette(links, site, mu, nu)[0])
    return score


def adjacent_plaquette_score(links: np.ndarray, site: tuple[int, int, int, int], mu: int) -> float:
    L = links.shape[0]
    score = 0.0
    for nu in range(DIRECTIONS):
        if nu == mu:
            continue
        score += float(plaquette(links, site, mu, nu)[0])
        score += float(plaquette(links, shift_site(site, nu, -1, L), mu, nu)[0])
    return score


def local_score_change_for_left_multiply(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
    proposal: np.ndarray,
) -> float:
    before = adjacent_plaquette_score(links, site, mu)
    old_link = links[site + (mu,)].copy()
    links[site + (mu,)] = qnormalize(qmul(proposal, old_link))
    after = adjacent_plaquette_score(links, site, mu)
    links[site + (mu,)] = old_link
    return after - before


def left_multiply_link_in_place(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
    proposal: np.ndarray,
) -> None:
    links[site + (mu,)] = qnormalize(qmul(proposal, links[site + (mu,)]))


def metropolis_sweep(links: np.ndarray, cfg: RunConfig, rng: np.random.Generator) -> int:
    L = cfg.L
    accepted = 0
    attempts = DIRECTIONS * L**DIRECTIONS
    for _ in range(attempts):
        site = (
            int(rng.integers(L)),
            int(rng.integers(L)),
            int(rng.integers(L)),
            int(rng.integers(L)),
        )
        mu = int(rng.integers(DIRECTIONS))
        proposal = random_small_su2(rng, cfg.proposal_width)
        delta_score = local_score_change_for_left_multiply(links, site, mu, proposal)
        if delta_score >= 0.0 or rng.random() < math.exp(cfg.beta * delta_score):
            left_multiply_link_in_place(links, site, mu, proposal)
            accepted += 1
    return accepted


def gauge_transform(links: np.ndarray, gauges: np.ndarray) -> np.ndarray:
    L = links.shape[0]
    transformed = np.empty_like(links)
    for site in np.ndindex((L, L, L, L)):
        for mu in range(DIRECTIONS):
            target = shift_site(site, mu, 1, L)
            transformed[site + (mu,)] = qmul(qmul(gauges[site], links[site + (mu,)]), qconj(gauges[target]))
    return transformed


def wilson_loop_rectangle(links: np.ndarray, r: int, t: int) -> float:
    if r <= 0 or t <= 0:
        raise ValueError("rectangle sizes must be positive")
    L = links.shape[0]
    total = 0.0
    count = 0
    identity = np.array([1.0, 0.0, 0.0, 0.0], dtype=float)
    for site in np.ndindex((L, L, L, L)):
        for mu in range(DIRECTIONS):
            for nu in range(mu + 1, DIRECTIONS):
                cursor = site
                loop = identity.copy()
                for _ in range(r):
                    loop = qmul(loop, links[cursor + (mu,)])
                    cursor = shift_site(cursor, mu, 1, L)
                for _ in range(t):
                    loop = qmul(loop, links[cursor + (nu,)])
                    cursor = shift_site(cursor, nu, 1, L)
                for _ in range(r):
                    cursor = shift_site(cursor, mu, -1, L)
                    loop = qmul(loop, qconj(links[cursor + (mu,)]))
                for _ in range(t):
                    cursor = shift_site(cursor, nu, -1, L)
                    loop = qmul(loop, qconj(links[cursor + (nu,)]))
                total += float(loop[0])
                count += 1
    return total / float(count)


def run(cfg: RunConfig) -> dict[str, float | int]:
    if cfg.therm >= cfg.sweeps:
        raise ValueError("therm must be smaller than sweeps")
    rng = np.random.default_rng(cfg.seed)
    links = random_links(cfg.L, rng)
    accepted = 0
    plaquette_values: list[float] = []
    loop_values: list[float] = []
    plaquette_count = 6 * cfg.L**4
    attempts_per_sweep = DIRECTIONS * cfg.L**DIRECTIONS

    for sweep_index in range(cfg.sweeps):
        accepted += metropolis_sweep(links, cfg, rng)
        if sweep_index >= cfg.therm:
            plaquette_values.append(total_plaquette_score(links) / float(plaquette_count))
            loop_values.append(wilson_loop_rectangle(links, cfg.rectangle_r, cfg.rectangle_t))

    plaquettes = np.array(plaquette_values, dtype=float)
    loops = np.array(loop_values, dtype=float)
    return {
        "L": cfg.L,
        "beta": cfg.beta,
        "proposal_width": cfg.proposal_width,
        "sweeps": cfg.sweeps,
        "therm": cfg.therm,
        "seed": cfg.seed,
        "acceptance": accepted / float(cfg.sweeps * attempts_per_sweep),
        "plaquette_mean": float(np.mean(plaquettes)),
        "plaquette_stderr_naive": float(np.std(plaquettes, ddof=1) / math.sqrt(len(plaquettes))),
        "wilson_loop_r": cfg.rectangle_r,
        "wilson_loop_t": cfg.rectangle_t,
        "wilson_loop_mean": float(np.mean(loops)),
        "wilson_loop_stderr_naive": float(np.std(loops, ddof=1) / math.sqrt(len(loops))),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=3)
    parser.add_argument("--beta", type=float, default=2.0)
    parser.add_argument("--proposal-width", type=float, default=0.45)
    parser.add_argument("--sweeps", type=int, default=24)
    parser.add_argument("--therm", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--rectangle-r", type=int, default=1)
    parser.add_argument("--rectangle-t", type=int, default=1)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.L = 2
        args.beta = 1.4
        args.proposal_width = 0.55
        args.sweeps = 10
        args.therm = 3
        args.seed = 314159
        args.rectangle_r = 1
        args.rectangle_t = 1
    cfg = RunConfig(
        L=args.L,
        beta=args.beta,
        proposal_width=args.proposal_width,
        sweeps=args.sweeps,
        therm=args.therm,
        seed=args.seed,
        rectangle_r=args.rectangle_r,
        rectangle_t=args.rectangle_t,
    )
    result = run(cfg)
    if args.smoke:
        if not (0.0 < result["acceptance"] < 1.0):
            raise AssertionError("acceptance must be a nontrivial probability in smoke mode")
        if not (-1.0 <= result["plaquette_mean"] <= 1.0):
            raise AssertionError("plaquette mean is outside the SU(2) trace range")
        if not (-1.0 <= result["wilson_loop_mean"] <= 1.0):
            raise AssertionError("Wilson-loop mean is outside the SU(2) trace range")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
