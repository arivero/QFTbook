#!/usr/bin/env python3
"""Finite TFFSA-style Ising spin-field connected-block benchmark.

The finite-volume massive Ising theory has a free Majorana basis.  This
script builds a small zero-momentum block consisting of the vacuum and
two-particle states with rapidities (theta_n,-theta_n).  Off-diagonal spin
matrix elements are assembled from the connected infinite-volume form factors

    F_{2k}^sigma(theta_1,...,theta_{2k})
      = sigma_bar i^k prod_{i<j} tanh((theta_i-theta_j)/2),

with the free Bethe-state density rho_I = prod_i m L cosh(theta_i).  The
diagonal convention used here keeps the disconnected vacuum-expectation
contribution sigma_bar and omits the singular diagonal connected finite part.
Consequently this is a finite-regulator convention and normalization
benchmark for TFFSA matrix assembly, not a production magnetic-Ising spectrum.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass

import numpy as np


@dataclass
class PairState:
    mode: float
    theta: float
    energy: float
    density: float


@dataclass
class RunConfig:
    num_pairs: int
    mass: float
    circumference: float
    magnetic_coupling: float
    sigma_bar: float


def tanh_product(thetas: list[complex]) -> complex:
    value = 1.0 + 0.0j
    for i, theta_i in enumerate(thetas):
        for theta_j in thetas[i + 1 :]:
            value *= cmath.tanh((theta_i - theta_j) / 2.0)
    return value


def spin_even_form_factor(thetas: list[complex], sigma_bar: float) -> complex:
    n = len(thetas)
    if n % 2 == 1:
        return 0.0 + 0.0j
    return sigma_bar * (1j ** (n // 2)) * tanh_product(thetas)


def pair_states(num_pairs: int, mass: float, circumference: float) -> list[PairState]:
    if num_pairs < 0:
        raise ValueError("num_pairs must be nonnegative")
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    if circumference <= 0.0:
        raise ValueError("circumference must be positive")

    states: list[PairState] = []
    for n in range(num_pairs):
        mode = n + 0.5
        momentum = 2.0 * math.pi * mode / circumference
        theta = math.asinh(momentum / mass)
        omega = math.sqrt(momentum * momentum + mass * mass)
        density_one = mass * circumference * math.cosh(theta)
        states.append(
            PairState(
                mode=mode,
                theta=theta,
                energy=2.0 * omega,
                density=density_one * density_one,
            )
        )
    return states


def state_rapidities(state_index: int, states: list[PairState]) -> list[float]:
    if state_index == 0:
        return []
    state = states[state_index - 1]
    return [state.theta, -state.theta]


def state_density(state_index: int, states: list[PairState]) -> float:
    if state_index == 0:
        return 1.0
    return states[state_index - 1].density


def connected_spin_matrix_element(
    bra_index: int,
    ket_index: int,
    states: list[PairState],
    sigma_bar: float,
) -> complex:
    """Connected off-diagonal spin matrix element before the spatial integral."""

    if bra_index == ket_index:
        return complex(sigma_bar)

    outgoing = state_rapidities(bra_index, states)
    incoming = state_rapidities(ket_index, states)
    crossed = [complex(theta, math.pi) for theta in outgoing] + [
        complex(theta) for theta in incoming
    ]
    density = math.sqrt(
        state_density(bra_index, states) * state_density(ket_index, states)
    )
    return spin_even_form_factor(crossed, sigma_bar) / density


def finite_matrix(cfg: RunConfig) -> np.ndarray:
    states = pair_states(cfg.num_pairs, cfg.mass, cfg.circumference)
    size = cfg.num_pairs + 1
    matrix = np.zeros((size, size), dtype=complex)
    for i in range(size):
        if i > 0:
            matrix[i, i] = states[i - 1].energy
        matrix[i, i] += cfg.magnetic_coupling * cfg.circumference * cfg.sigma_bar
    for i in range(size):
        for j in range(i + 1, size):
            value = (
                cfg.magnetic_coupling
                * cfg.circumference
                * connected_spin_matrix_element(i, j, states, cfg.sigma_bar)
            )
            matrix[i, j] = value
            matrix[j, i] = np.conjugate(value)
    return matrix


def run(cfg: RunConfig) -> dict[str, float | int | list[float]]:
    matrix = finite_matrix(cfg)
    hermiticity_error = float(np.max(np.abs(matrix - matrix.conjugate().T)))
    eigs = np.linalg.eigvalsh(matrix)
    states = pair_states(cfg.num_pairs, cfg.mass, cfg.circumference)
    free_energies = [0.0] + [state.energy for state in states]
    return {
        "num_pairs": cfg.num_pairs,
        "mass": cfg.mass,
        "circumference": cfg.circumference,
        "magnetic_coupling": cfg.magnetic_coupling,
        "sigma_bar": cfg.sigma_bar,
        "hermiticity_error": hermiticity_error,
        "lowest_eigenvalues": [float(x) for x in eigs[: min(6, len(eigs))]],
        "free_energies": [float(x) for x in free_energies[: min(6, len(free_energies))]],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--num-pairs", type=int, default=5)
    parser.add_argument("--mass", type=float, default=1.0)
    parser.add_argument("--circumference", type=float, default=8.0)
    parser.add_argument("--magnetic-coupling", type=float, default=0.03)
    parser.add_argument("--sigma-bar", type=float, default=1.0)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.num_pairs = 4
        args.mass = 1.0
        args.circumference = 7.0
        args.magnetic_coupling = 0.02
        args.sigma_bar = 1.0
    cfg = RunConfig(
        num_pairs=args.num_pairs,
        mass=args.mass,
        circumference=args.circumference,
        magnetic_coupling=args.magnetic_coupling,
        sigma_bar=args.sigma_bar,
    )
    result = run(cfg)
    if args.smoke and result["hermiticity_error"] > 1.0e-12:
        raise AssertionError("finite TFFSA block is not Hermitian")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
