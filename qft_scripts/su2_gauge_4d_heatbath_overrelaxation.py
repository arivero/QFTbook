#!/usr/bin/env python3
"""Finite 4D SU(2) lattice gauge heat-bath/overrelaxation sampler.

The script samples the finite periodic Wilson plaquette model

    probability(U) proportional to exp(beta * sum_p 1/2 Re Tr U_p),

with SU(2) links represented by unit quaternions.  It uses exact single-link
heat-bath conditional sampling for the SU(2) staple density, optionally
interleaved with deterministic microcanonical overrelaxation sweeps.  This is
a reader-facing finite-regulator demonstration, not a continuum extrapolation
or a production gauge-code benchmark.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import numpy as np

import su2_gauge_4d_metropolis as su2


@dataclass
class RunConfig:
    L: int
    beta: float
    sweeps: int
    therm: int
    seed: int
    overrelaxation_sweeps: int
    rectangle_r: int
    rectangle_t: int


def staple_sum(links: np.ndarray, site: tuple[int, int, int, int], mu: int) -> np.ndarray:
    """Return V_e such that the local score is Re_quat(U_e V_e)."""

    L = links.shape[0]
    staple = np.zeros(4, dtype=float)
    for nu in range(su2.DIRECTIONS):
        if nu == mu:
            continue

        x_mu = su2.shift_site(site, mu, 1, L)
        x_nu = su2.shift_site(site, nu, 1, L)
        forward = su2.qmul(
            su2.qmul(links[x_mu + (nu,)], su2.qconj(links[x_nu + (mu,)])),
            su2.qconj(links[site + (nu,)]),
        )
        staple += forward

        x_minus_nu = su2.shift_site(site, nu, -1, L)
        x_minus_nu_plus_mu = su2.shift_site(x_minus_nu, mu, 1, L)
        backward_cycle = su2.qmul(
            su2.qmul(su2.qconj(links[x_minus_nu + (nu,)]), links[x_minus_nu + (mu,)]),
            links[x_minus_nu_plus_mu + (nu,)],
        )
        staple += su2.qconj(backward_cycle)

    return staple


def local_score_from_staple(links: np.ndarray, site: tuple[int, int, int, int], mu: int) -> float:
    return float(su2.qmul(links[site + (mu,)], staple_sum(links, site, mu))[0])


def sample_su2_staple_density(kappa: float, rng: np.random.Generator) -> np.ndarray:
    """Sample X in SU(2) with density proportional to exp(kappa Re_quat X)."""

    if kappa < 0.0:
        raise ValueError("kappa must be nonnegative")
    if kappa == 0.0:
        return su2.random_su2(rng)

    while True:
        x0 = float(rng.uniform(-1.0, 1.0))
        accept = math.sqrt(max(0.0, 1.0 - x0 * x0)) * math.exp(kappa * (x0 - 1.0))
        if rng.random() <= accept:
            axis = rng.normal(size=3)
            axis_norm = float(np.linalg.norm(axis))
            if axis_norm == 0.0:
                axis = np.array([1.0, 0.0, 0.0], dtype=float)
            else:
                axis = axis / axis_norm
            radius = math.sqrt(max(0.0, 1.0 - x0 * x0))
            return np.array([x0, *(radius * axis)], dtype=float)


def heatbath_update_link(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
    beta: float,
    rng: np.random.Generator,
) -> None:
    staple = staple_sum(links, site, mu)
    c = float(np.linalg.norm(staple))
    if c == 0.0:
        links[site + (mu,)] = su2.random_su2(rng)
        return
    w = staple / c
    x = sample_su2_staple_density(beta * c, rng)
    links[site + (mu,)] = su2.qnormalize(su2.qmul(x, su2.qconj(w)))


def overrelax_update_link(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
) -> None:
    staple = staple_sum(links, site, mu)
    c = float(np.linalg.norm(staple))
    if c == 0.0:
        links[site + (mu,)] = su2.qconj(links[site + (mu,)])
        return
    w_inv = su2.qconj(staple / c)
    links[site + (mu,)] = su2.qnormalize(
        su2.qmul(su2.qmul(w_inv, su2.qconj(links[site + (mu,)])), w_inv)
    )


def heatbath_sweep(links: np.ndarray, beta: float, rng: np.random.Generator) -> None:
    L = links.shape[0]
    for site in np.ndindex((L, L, L, L)):
        for mu in range(su2.DIRECTIONS):
            heatbath_update_link(links, site, mu, beta, rng)


def overrelaxation_sweep(links: np.ndarray) -> None:
    L = links.shape[0]
    for site in np.ndindex((L, L, L, L)):
        for mu in range(su2.DIRECTIONS):
            overrelax_update_link(links, site, mu)


def run(cfg: RunConfig) -> dict[str, float | int]:
    if cfg.L <= 0:
        raise ValueError("L must be positive")
    if cfg.therm >= cfg.sweeps:
        raise ValueError("therm must be smaller than sweeps")
    if cfg.overrelaxation_sweeps < 0:
        raise ValueError("overrelaxation sweeps must be nonnegative")

    rng = np.random.default_rng(cfg.seed)
    links = su2.random_links(cfg.L, rng)
    plaquette_values: list[float] = []
    loop_values: list[float] = []
    plaquette_count = 6 * cfg.L**4

    for sweep_index in range(cfg.sweeps):
        heatbath_sweep(links, cfg.beta, rng)
        for _ in range(cfg.overrelaxation_sweeps):
            overrelaxation_sweep(links)
        if sweep_index >= cfg.therm:
            plaquette_values.append(su2.total_plaquette_score(links) / float(plaquette_count))
            loop_values.append(su2.wilson_loop_rectangle(links, cfg.rectangle_r, cfg.rectangle_t))

    plaquettes = np.array(plaquette_values, dtype=float)
    loops = np.array(loop_values, dtype=float)
    return {
        "L": cfg.L,
        "beta": cfg.beta,
        "sweeps": cfg.sweeps,
        "therm": cfg.therm,
        "seed": cfg.seed,
        "overrelaxation_sweeps": cfg.overrelaxation_sweeps,
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
    parser.add_argument("--sweeps", type=int, default=18)
    parser.add_argument("--therm", type=int, default=6)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--overrelaxation-sweeps", type=int, default=2)
    parser.add_argument("--rectangle-r", type=int, default=1)
    parser.add_argument("--rectangle-t", type=int, default=1)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.L = 2
        args.beta = 1.2
        args.sweeps = 8
        args.therm = 2
        args.seed = 271828
        args.overrelaxation_sweeps = 1
        args.rectangle_r = 1
        args.rectangle_t = 1
    cfg = RunConfig(
        L=args.L,
        beta=args.beta,
        sweeps=args.sweeps,
        therm=args.therm,
        seed=args.seed,
        overrelaxation_sweeps=args.overrelaxation_sweeps,
        rectangle_r=args.rectangle_r,
        rectangle_t=args.rectangle_t,
    )
    result = run(cfg)
    if args.smoke:
        if not (-1.0 <= result["plaquette_mean"] <= 1.0):
            raise AssertionError("plaquette mean is outside the SU(2) trace range")
        if not (-1.0 <= result["wilson_loop_mean"] <= 1.0):
            raise AssertionError("Wilson-loop mean is outside the SU(2) trace range")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
