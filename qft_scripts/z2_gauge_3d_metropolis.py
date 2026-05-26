#!/usr/bin/env python3
"""Finite 3D Z2 lattice gauge Metropolis sampler.

The script samples the finite periodic cubic lattice gauge model

    probability(U) proportional to exp(beta * sum_p P_p),

where link variables U_l are +/-1 and P_p is the product around a plaquette.
It is a reader-facing finite-regulator demonstration for the monograph.  It
does not claim a continuum limit or an infinite-volume phase transition.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np


DIRECTIONS = 3


@dataclass
class RunConfig:
    L: int
    betas: list[float]
    sweeps: int
    therm: int
    seed: int
    rectangle_r: int
    rectangle_t: int


def shift_site(site: tuple[int, int, int], direction: int, step: int, L: int) -> tuple[int, int, int]:
    coords = list(site)
    coords[direction] = (coords[direction] + step) % L
    return (coords[0], coords[1], coords[2])


def random_links(L: int, rng: np.random.Generator) -> np.ndarray:
    return rng.choice(np.array([-1, 1], dtype=np.int8), size=(L, L, L, DIRECTIONS))


def plaquette(links: np.ndarray, site: tuple[int, int, int], mu: int, nu: int) -> int:
    if mu == nu:
        raise ValueError("plaquette directions must be distinct")
    L = links.shape[0]
    x_mu = shift_site(site, mu, 1, L)
    x_nu = shift_site(site, nu, 1, L)
    return int(
        links[site + (mu,)]
        * links[x_mu + (nu,)]
        * links[x_nu + (mu,)]
        * links[site + (nu,)]
    )


def total_plaquette_score(links: np.ndarray) -> int:
    L = links.shape[0]
    score = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                site = (x0, x1, x2)
                for mu in range(DIRECTIONS):
                    for nu in range(mu + 1, DIRECTIONS):
                        score += plaquette(links, site, mu, nu)
    return int(score)


def adjacent_plaquette_sum(links: np.ndarray, site: tuple[int, int, int], mu: int) -> int:
    L = links.shape[0]
    total = 0
    for nu in range(DIRECTIONS):
        if nu == mu:
            continue
        total += plaquette(links, site, mu, nu)
        total += plaquette(links, shift_site(site, nu, -1, L), mu, nu)
    return int(total)


def local_score_change_for_flip(links: np.ndarray, site: tuple[int, int, int], mu: int) -> int:
    return int(-2 * adjacent_plaquette_sum(links, site, mu))


def flip_link_in_place(links: np.ndarray, site: tuple[int, int, int], mu: int) -> None:
    links[site + (mu,)] *= -1


def metropolis_sweep(links: np.ndarray, beta: float, rng: np.random.Generator) -> int:
    L = links.shape[0]
    accepted = 0
    attempts = DIRECTIONS * L**3
    for _ in range(attempts):
        site = (
            int(rng.integers(L)),
            int(rng.integers(L)),
            int(rng.integers(L)),
        )
        mu = int(rng.integers(DIRECTIONS))
        delta_score = local_score_change_for_flip(links, site, mu)
        if delta_score >= 0 or rng.random() < np.exp(beta * delta_score):
            flip_link_in_place(links, site, mu)
            accepted += 1
    return accepted


def gauge_transform(links: np.ndarray, signs: np.ndarray) -> np.ndarray:
    L = links.shape[0]
    transformed = np.empty_like(links)
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                site = (x0, x1, x2)
                for mu in range(DIRECTIONS):
                    transformed[site + (mu,)] = (
                        signs[site]
                        * links[site + (mu,)]
                        * signs[shift_site(site, mu, 1, L)]
                    )
    return transformed


def wilson_loop_rectangle(links: np.ndarray, r: int, t: int) -> float:
    if r < 1 or t < 1:
        raise ValueError("rectangle sides must be positive")
    L = links.shape[0]
    total = 0
    count = 0
    for mu in range(DIRECTIONS):
        for nu in range(mu + 1, DIRECTIONS):
            for x0 in range(L):
                for x1 in range(L):
                    for x2 in range(L):
                        site = (x0, x1, x2)
                        position = site
                        value = 1
                        for _ in range(r):
                            value *= int(links[position + (mu,)])
                            position = shift_site(position, mu, 1, L)
                        for _ in range(t):
                            value *= int(links[position + (nu,)])
                            position = shift_site(position, nu, 1, L)
                        for _ in range(r):
                            position = shift_site(position, mu, -1, L)
                            value *= int(links[position + (mu,)])
                        for _ in range(t):
                            position = shift_site(position, nu, -1, L)
                            value *= int(links[position + (nu,)])
                        total += value
                        count += 1
    return float(total / count)


def run_one_beta(
    L: int,
    beta: float,
    sweeps: int,
    therm: int,
    seed: int,
    rectangle_r: int,
    rectangle_t: int,
) -> dict[str, float | int]:
    if therm >= sweeps:
        raise ValueError("therm must be smaller than sweeps")
    rng = np.random.default_rng(seed)
    links = random_links(L, rng)
    accepted = 0
    plaquette_values: list[float] = []
    loop_values: list[float] = []
    plaquette_count = 3 * L**3

    for sweep_index in range(sweeps):
        accepted += metropolis_sweep(links, beta, rng)
        if sweep_index >= therm:
            plaquette_values.append(total_plaquette_score(links) / plaquette_count)
            loop_values.append(wilson_loop_rectangle(links, rectangle_r, rectangle_t))

    attempts = sweeps * DIRECTIONS * L**3
    return {
        "L": L,
        "beta": beta,
        "sweeps": sweeps,
        "therm": therm,
        "seed": seed,
        "acceptance": float(accepted / attempts),
        "plaquette_mean": float(np.mean(plaquette_values)),
        "plaquette_stderr_naive": float(np.std(plaquette_values, ddof=1) / np.sqrt(len(plaquette_values))),
        "wilson_loop_r": rectangle_r,
        "wilson_loop_t": rectangle_t,
        "wilson_loop_mean": float(np.mean(loop_values)),
        "wilson_loop_stderr_naive": float(np.std(loop_values, ddof=1) / np.sqrt(len(loop_values))),
    }


def run(cfg: RunConfig) -> dict[str, object]:
    results = []
    for index, beta in enumerate(cfg.betas):
        results.append(
            run_one_beta(
                cfg.L,
                beta,
                cfg.sweeps,
                cfg.therm,
                cfg.seed + 1009 * index,
                cfg.rectangle_r,
                cfg.rectangle_t,
            )
        )
    return {"model": "3d_z2_lattice_gauge", "results": results}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=6)
    parser.add_argument("--betas", type=float, nargs="+", default=[0.45, 0.65, 0.80, 1.00])
    parser.add_argument("--sweeps", type=int, default=400)
    parser.add_argument("--therm", type=int, default=120)
    parser.add_argument("--seed", type=int, default=20260526)
    parser.add_argument("--rectangle-r", type=int, default=2)
    parser.add_argument("--rectangle-t", type=int, default=2)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.L = 4
        args.betas = [0.55, 0.85]
        args.sweeps = 48
        args.therm = 12
        args.seed = 161803
        args.rectangle_r = 1
        args.rectangle_t = 2
    cfg = RunConfig(
        L=args.L,
        betas=[float(beta) for beta in args.betas],
        sweeps=args.sweeps,
        therm=args.therm,
        seed=args.seed,
        rectangle_r=args.rectangle_r,
        rectangle_t=args.rectangle_t,
    )
    result = run(cfg)
    if args.smoke:
        for entry in result["results"]:
            if not (0.0 <= entry["acceptance"] <= 1.0):
                raise AssertionError("acceptance must be a probability")
            if not (-1.0 <= entry["plaquette_mean"] <= 1.0):
                raise AssertionError("plaquette mean is outside the finite Z2 range")
            if not (-1.0 <= entry["wilson_loop_mean"] <= 1.0):
                raise AssertionError("Wilson-loop mean is outside the finite Z2 range")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
