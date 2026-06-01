#!/usr/bin/env python3
"""Finite two-dimensional scalar phi^4 Metropolis sampler.

The script samples the periodic L x L Euclidean lattice action

    S(phi) = sum_x [
        1/2 sum_mu (phi_{x+mu} - phi_x)^2
        + 1/2 m^2 phi_x^2 + lambda/24 phi_x^4
    ]

with respect to the finite-dimensional density exp(-S) dphi.  It is a
finite-regulator demonstration: no continuum limit, critical exponent, or
constructive continuum theorem is inferred from the output.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np


@dataclass
class RunConfig:
    L: int
    mass_sq: float
    quartic: float
    proposal_width: float
    sweeps: int
    therm: int
    seed: int


def validate_config(cfg: RunConfig) -> None:
    if cfg.L < 2:
        raise ValueError("L must be at least 2")
    if cfg.quartic < 0.0:
        raise ValueError("quartic coupling must be nonnegative")
    if cfg.quartic == 0.0 and cfg.mass_sq <= 0.0:
        raise ValueError("with zero quartic coupling mass_sq must be positive")
    if cfg.proposal_width <= 0.0:
        raise ValueError("proposal_width must be positive")
    if cfg.therm >= cfg.sweeps:
        raise ValueError("therm must be smaller than sweeps")


def potential(value: np.ndarray | float, mass_sq: float, quartic: float) -> np.ndarray | float:
    return 0.5 * mass_sq * value * value + (quartic / 24.0) * value**4


def total_action(field: np.ndarray, mass_sq: float, quartic: float) -> float:
    right = np.roll(field, shift=-1, axis=1)
    down = np.roll(field, shift=-1, axis=0)
    kinetic = 0.5 * np.sum((right - field) ** 2 + (down - field) ** 2)
    return float(kinetic + np.sum(potential(field, mass_sq, quartic)))


def oriented_bonds_touching_site(
    L: int, i: int, j: int
) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    """Return the positive-direction kinetic bonds whose term changes."""

    return (
        ((i, j), (i, (j + 1) % L)),
        ((i, (j - 1) % L), (i, j)),
        ((i, j), ((i + 1) % L, j)),
        (((i - 1) % L, j), (i, j)),
    )


def local_action_change(
    field: np.ndarray,
    i: int,
    j: int,
    new_value: float,
    mass_sq: float,
    quartic: float,
) -> float:
    L = field.shape[0]
    old_value = float(field[i, j])
    delta = float(potential(new_value, mass_sq, quartic) - potential(old_value, mass_sq, quartic))

    for a, b in oriented_bonds_touching_site(L, i, j):
        old_a = old_value if a == (i, j) else float(field[a])
        old_b = old_value if b == (i, j) else float(field[b])
        new_a = new_value if a == (i, j) else float(field[a])
        new_b = new_value if b == (i, j) else float(field[b])
        delta += 0.5 * ((new_b - new_a) ** 2 - (old_b - old_a) ** 2)
    return float(delta)


def sweep(field: np.ndarray, cfg: RunConfig, rng: np.random.Generator) -> int:
    accepted = 0
    for _ in range(cfg.L * cfg.L):
        i = int(rng.integers(cfg.L))
        j = int(rng.integers(cfg.L))
        proposal = float(field[i, j] + rng.uniform(-cfg.proposal_width, cfg.proposal_width))
        delta_s = local_action_change(field, i, j, proposal, cfg.mass_sq, cfg.quartic)
        if delta_s <= 0.0 or rng.random() < np.exp(-delta_s):
            field[i, j] = proposal
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
    validate_config(cfg)
    rng = np.random.default_rng(cfg.seed)
    field = rng.normal(loc=0.0, scale=1.0, size=(cfg.L, cfg.L))
    accepted = 0
    action_density: list[float] = []
    phi_mean: list[float] = []
    phi_abs_mean: list[float] = []
    phi2: list[float] = []
    phi4: list[float] = []

    volume = cfg.L * cfg.L
    for sweep_index in range(cfg.sweeps):
        accepted += sweep(field, cfg, rng)
        if sweep_index >= cfg.therm:
            mean_phi = float(np.mean(field))
            action_density.append(total_action(field, cfg.mass_sq, cfg.quartic) / volume)
            phi_mean.append(mean_phi)
            phi_abs_mean.append(abs(mean_phi))
            phi2.append(float(np.mean(field**2)))
            phi4.append(float(np.mean(field**4)))

    actions = np.asarray(action_density, dtype=float)
    means = np.asarray(phi_mean, dtype=float)
    phi2_values = np.asarray(phi2, dtype=float)
    attempts = cfg.sweeps * volume
    return {
        "L": cfg.L,
        "mass_sq": cfg.mass_sq,
        "quartic": cfg.quartic,
        "proposal_width": cfg.proposal_width,
        "sweeps": cfg.sweeps,
        "therm": cfg.therm,
        "seed": cfg.seed,
        "acceptance": accepted / attempts,
        "action_density_mean": float(np.mean(actions)),
        "action_density_stderr_naive": float(np.std(actions, ddof=1) / np.sqrt(actions.size)),
        "field_mean": float(np.mean(means)),
        "abs_field_mean": float(np.mean(phi_abs_mean)),
        "phi2_mean": float(np.mean(phi2_values)),
        "phi4_mean": float(np.mean(phi4)),
        "susceptibility_like_mean": float(volume * np.mean(means**2)),
        "tau_int_phi2_windowed": float(autocorrelation_time(phi2_values)),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=12)
    parser.add_argument("--mass-sq", type=float, default=0.6)
    parser.add_argument("--quartic", type=float, default=1.0)
    parser.add_argument("--proposal-width", type=float, default=1.0)
    parser.add_argument("--sweeps", type=int, default=2000)
    parser.add_argument("--therm", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260601)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.L = 6
        args.sweeps = 160
        args.therm = 40
        args.seed = 271828
    cfg = RunConfig(
        L=args.L,
        mass_sq=args.mass_sq,
        quartic=args.quartic,
        proposal_width=args.proposal_width,
        sweeps=args.sweeps,
        therm=args.therm,
        seed=args.seed,
    )
    result = run(cfg)
    if args.smoke:
        if not (0.0 < result["acceptance"] < 1.0):
            raise AssertionError("acceptance must be a nontrivial probability in smoke mode")
        if result["phi2_mean"] <= 0.0:
            raise AssertionError("phi2 must be positive in smoke mode")
        if result["tau_int_phi2_windowed"] <= 0.0:
            raise AssertionError("autocorrelation time must be positive in smoke mode")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
