#!/usr/bin/env python3
"""Finite-volume two-dimensional Ising Metropolis sampler.

The script samples the periodic L x L Ising model

    H(s) = -J sum_<xy> s_x s_y - h sum_x s_x,   s_x in {-1,+1}.

It is a finite-regulator demonstration for the monograph, not a continuum
extrapolation.  The Metropolis proposal flips one spin chosen uniformly; the
acceptance probability min(1, exp(-beta Delta H)) obeys detailed balance with
respect to the finite Boltzmann probability.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np


@dataclass
class RunConfig:
    L: int
    beta: float
    J: float
    h: float
    sweeps: int
    therm: int
    seed: int


def local_energy_change(spins: np.ndarray, i: int, j: int, J: float, h: float) -> float:
    L = spins.shape[0]
    s = spins[i, j]
    neighbor_sum = (
        spins[(i + 1) % L, j]
        + spins[(i - 1) % L, j]
        + spins[i, (j + 1) % L]
        + spins[i, (j - 1) % L]
    )
    return 2.0 * s * (J * neighbor_sum + h)


def total_energy(spins: np.ndarray, J: float, h: float) -> float:
    right = np.roll(spins, shift=-1, axis=1)
    down = np.roll(spins, shift=-1, axis=0)
    return float(-J * np.sum(spins * (right + down)) - h * np.sum(spins))


def sweep(spins: np.ndarray, cfg: RunConfig, rng: np.random.Generator) -> int:
    L = cfg.L
    accepted = 0
    for _ in range(L * L):
        i = int(rng.integers(L))
        j = int(rng.integers(L))
        dE = local_energy_change(spins, i, j, cfg.J, cfg.h)
        if dE <= 0.0 or rng.random() < np.exp(-cfg.beta * dE):
            spins[i, j] *= -1
            accepted += 1
    return accepted


def autocorrelation_time(values: np.ndarray, max_lag: int | None = None) -> float:
    x = np.asarray(values, dtype=float)
    if x.size < 4:
        return float("nan")
    x = x - np.mean(x)
    variance = float(np.dot(x, x) / x.size)
    if variance == 0.0:
        return 0.5
    if max_lag is None:
        max_lag = min(x.size // 2, 200)
    tau = 0.5
    for lag in range(1, max_lag + 1):
        corr = float(np.dot(x[:-lag], x[lag:]) / (x.size - lag) / variance)
        if corr <= 0.0:
            break
        tau += corr
    return tau


def run(cfg: RunConfig) -> dict[str, float | int]:
    rng = np.random.default_rng(cfg.seed)
    spins = rng.choice(np.array([-1, 1], dtype=np.int8), size=(cfg.L, cfg.L))
    accepted = 0
    measurements_energy: list[float] = []
    measurements_abs_mag: list[float] = []

    for sweep_index in range(cfg.sweeps):
        accepted += sweep(spins, cfg, rng)
        if sweep_index >= cfg.therm:
            volume = cfg.L * cfg.L
            measurements_energy.append(total_energy(spins, cfg.J, cfg.h) / volume)
            measurements_abs_mag.append(abs(float(np.mean(spins))))

    if not measurements_energy:
        raise ValueError("therm must be smaller than sweeps")

    energies = np.array(measurements_energy, dtype=float)
    mags = np.array(measurements_abs_mag, dtype=float)
    attempts = cfg.sweeps * cfg.L * cfg.L
    return {
        "L": cfg.L,
        "beta": cfg.beta,
        "sweeps": cfg.sweeps,
        "therm": cfg.therm,
        "seed": cfg.seed,
        "acceptance": accepted / attempts,
        "energy_per_site_mean": float(np.mean(energies)),
        "energy_per_site_stderr_naive": float(np.std(energies, ddof=1) / np.sqrt(energies.size)),
        "abs_magnetization_mean": float(np.mean(mags)),
        "tau_int_energy_windowed": float(autocorrelation_time(energies)),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=16)
    parser.add_argument("--beta", type=float, default=0.44068679350977147)
    parser.add_argument("--J", type=float, default=1.0)
    parser.add_argument("--h", type=float, default=0.0)
    parser.add_argument("--sweeps", type=int, default=2000)
    parser.add_argument("--therm", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260525)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.L = 8
        args.sweeps = 160
        args.therm = 40
        args.seed = 314159
    cfg = RunConfig(
        L=args.L,
        beta=args.beta,
        J=args.J,
        h=args.h,
        sweeps=args.sweeps,
        therm=args.therm,
        seed=args.seed,
    )
    result = run(cfg)
    if args.smoke:
        if not (0.0 < result["acceptance"] < 1.0):
            raise AssertionError("acceptance must be a nontrivial probability in smoke mode")
        if result["tau_int_energy_windowed"] <= 0.0:
            raise AssertionError("autocorrelation time must be positive in smoke mode")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
