#!/usr/bin/env python3
"""Exact finite checks for the 2D Ising Metropolis companion script."""

from __future__ import annotations

import importlib.util
import itertools
import math
import sys
from pathlib import Path

import numpy as np

from check_utils import assert_close as _assert_close


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "ising2d_metropolis.py"
spec = importlib.util.spec_from_file_location("ising2d_metropolis", SCRIPT)
ising = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = ising
spec.loader.exec_module(ising)


def all_spins(lattice_size: int) -> list[np.ndarray]:
    configs: list[np.ndarray] = []
    for entries in itertools.product((-1, 1), repeat=lattice_size * lattice_size):
        configs.append(np.array(entries, dtype=np.int8).reshape((lattice_size, lattice_size)))
    return configs


def key(spins: np.ndarray) -> tuple[int, ...]:
    return tuple(int(x) for x in spins.reshape(-1))


def flipped(spins: np.ndarray, i: int, j: int) -> np.ndarray:
    result = spins.copy()
    result[i, j] *= -1
    return result


def transition_probability(spins: np.ndarray, target: np.ndarray, beta: float, J: float, h: float) -> float:
    lattice_size = spins.shape[0]
    probability = 0.0
    holding = 1.0
    for i in range(lattice_size):
        for j in range(lattice_size):
            candidate = flipped(spins, i, j)
            delta_e = ising.local_energy_change(spins, i, j, J, h)
            accept = min(1.0, math.exp(-beta * delta_e))
            proposal = 1.0 / (lattice_size * lattice_size)
            if key(candidate) == key(target):
                probability += proposal * accept
            holding -= proposal * accept
    if key(spins) == key(target):
        probability += holding
    return probability


def check_local_energy_change() -> None:
    for spins in all_spins(2):
        for i in range(2):
            for j in range(2):
                direct = ising.total_energy(flipped(spins, i, j), J=0.7, h=-0.2) - ising.total_energy(spins, J=0.7, h=-0.2)
                local = ising.local_energy_change(spins, i, j, J=0.7, h=-0.2)
                _assert_close("local energy change versus total-energy difference", direct, local, tol=1.0e-12)


def check_detailed_balance() -> None:
    beta = 0.83
    J = 0.7
    h = -0.2
    configs = all_spins(2)
    weights = {
        key(spins): math.exp(-beta * ising.total_energy(spins, J=J, h=h))
        for spins in configs
    }
    partition = sum(weights.values())
    for source in configs:
        for target in configs:
            lhs = weights[key(source)] / partition * transition_probability(source, target, beta, J, h)
            rhs = weights[key(target)] / partition * transition_probability(target, source, beta, J, h)
            _assert_close("enumerated 2x2 detailed balance", lhs, rhs, tol=1.0e-12)


def main() -> None:
    check_local_energy_change()
    check_detailed_balance()
    print("All finite Ising Metropolis checks passed.")


if __name__ == "__main__":
    main()
