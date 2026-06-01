#!/usr/bin/env python3
"""Finite DLCQ matrix for a 1+1 dimensional scalar phi^4 warmup.

The script works at fixed harmonic resolution K and omits the p^+=0 mode.
The finite basis consists of bosonic occupation vectors (N_1,...,N_K) with

    sum_{n=1}^K n N_n = K.

It builds the invariant-mass matrix

    M_K^2 = K m^2 sum_n N_n/n + g K Q_K,

where Q_K is the normal-ordered quartic finite-mode operator with coefficients
1/sqrt(n_1 n_2 n_3 n_4) and longitudinal momentum conservation.  The
normalization of g is a finite-regulator convention; with the common field
normalization phi = sum_{n>0} (a_n e^{-inx/R} + a_n^dag e^{inx/R})/sqrt(4 pi n),
g equals lambda/(96 pi) in M^2 units.  The script is a finite light-front
regulator benchmark, not a continuum theorem; zero-mode constraints and
counterterm extrapolation are separate data.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from dataclasses import dataclass

import numpy as np


State = tuple[int, ...]
Term = tuple[tuple[int, ...], tuple[int, ...]]


@dataclass(frozen=True)
class RunConfig:
    K: int = 8
    mass: float = 1.0
    quartic_coupling: float = 0.05
    max_particles: int | None = None


def generate_basis(K: int, max_particles: int | None = None) -> list[State]:
    if K < 1:
        raise ValueError("K must be positive")
    if max_particles is not None and max_particles < 1:
        raise ValueError("max_particles must be positive when supplied")
    state = [0] * K
    basis: list[State] = []

    def rec(mode: int, remaining: int, particles: int) -> None:
        if mode == 0:
            if remaining == 0 and (max_particles is None or particles <= max_particles):
                basis.append(tuple(state))
            return
        max_occ = remaining // mode
        for occ in range(max_occ + 1):
            if max_particles is not None and particles + occ > max_particles:
                break
            state[mode - 1] = occ
            rec(mode - 1, remaining - mode * occ, particles + occ)
        state[mode - 1] = 0

    rec(K, K, 0)
    basis.sort(key=lambda item: (sum(item), tuple(reversed(item))))
    return basis


def total_resolution(state: State) -> int:
    return sum((idx + 1) * occupation for idx, occupation in enumerate(state))


def particle_number(state: State) -> int:
    return sum(state)


def free_invariant_mass_squared(state: State, K: int, mass: float) -> float:
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    return float(K * mass * mass * sum(occupation / float(idx + 1) for idx, occupation in enumerate(state)))


def apply_normal_ordered(
    state: State,
    creations: tuple[int, ...],
    annihilations: tuple[int, ...],
) -> tuple[State, float] | None:
    new_state = list(state)
    amplitude = 1.0
    for mode in annihilations:
        idx = mode - 1
        occupation = new_state[idx]
        if occupation == 0:
            return None
        amplitude *= math.sqrt(float(occupation))
        new_state[idx] = occupation - 1
    for mode in creations:
        idx = mode - 1
        occupation = new_state[idx]
        amplitude *= math.sqrt(float(occupation + 1))
        new_state[idx] = occupation + 1
    return tuple(new_state), amplitude


def quartic_terms(K: int) -> dict[Term, float]:
    """Return the dimensionless normal-ordered DLCQ quartic operator Q_K."""
    if K < 1:
        raise ValueError("K must be positive")
    modes = tuple(range(1, K + 1))
    terms: dict[Term, float] = {}
    for kinds in itertools.product(("create", "annihilate"), repeat=4):
        for mode_tuple in itertools.product(modes, repeat=4):
            created: list[int] = []
            annihilated: list[int] = []
            coefficient = 1.0
            for kind, mode in zip(kinds, mode_tuple):
                coefficient /= math.sqrt(float(mode))
                if kind == "create":
                    created.append(mode)
                else:
                    annihilated.append(mode)
            if sum(created) != sum(annihilated):
                continue
            if not created or not annihilated:
                continue
            key = (tuple(sorted(created)), tuple(sorted(annihilated)))
            terms[key] = terms.get(key, 0.0) + coefficient
    return terms


def quartic_matrix(cfg: RunConfig, basis: list[State] | None = None) -> np.ndarray:
    if basis is None:
        basis = generate_basis(cfg.K, cfg.max_particles)
    lookup = {state: idx for idx, state in enumerate(basis)}
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    terms = quartic_terms(cfg.K)
    for col, state in enumerate(basis):
        for (creations, annihilations), coefficient in terms.items():
            result = apply_normal_ordered(state, creations, annihilations)
            if result is None:
                continue
            final_state, amplitude = result
            row = lookup.get(final_state)
            if row is None:
                continue
            matrix[row, col] += coefficient * amplitude
    return matrix


def invariant_mass_matrix(cfg: RunConfig) -> tuple[list[State], np.ndarray, np.ndarray]:
    basis = generate_basis(cfg.K, cfg.max_particles)
    free = np.diag([free_invariant_mass_squared(state, cfg.K, cfg.mass) for state in basis])
    quartic = quartic_matrix(cfg, basis)
    matrix = free + cfg.quartic_coupling * cfg.K * quartic
    return basis, free, matrix


def run(cfg: RunConfig) -> dict[str, object]:
    basis, free, matrix = invariant_mass_matrix(cfg)
    eigenvalues = np.linalg.eigvalsh(matrix)
    free_eigenvalues = np.linalg.eigvalsh(free)
    hermiticity_error = float(np.max(np.abs(matrix - matrix.T))) if basis else 0.0
    return {
        "K": cfg.K,
        "dimension": len(basis),
        "mass": cfg.mass,
        "quartic_coupling": cfg.quartic_coupling,
        "max_particles": cfg.max_particles,
        "hermiticity_error": hermiticity_error,
        "lowest_M2": [float(x) for x in eigenvalues[: min(8, len(eigenvalues))]],
        "free_lowest_M2": [float(x) for x in free_eigenvalues[: min(8, len(free_eigenvalues))]],
        "interpretation": "finite DLCQ regulator only; zero modes and cutoff extrapolation are separate data",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--mass", type=float, default=1.0)
    parser.add_argument("--quartic-coupling", type=float, default=0.05)
    parser.add_argument("--max-particles", type=int, default=None)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = RunConfig(
        K=5 if args.smoke else args.K,
        mass=1.0 if args.smoke else args.mass,
        quartic_coupling=0.03 if args.smoke else args.quartic_coupling,
        max_particles=None if args.smoke else args.max_particles,
    )
    result = run(cfg)
    if args.smoke:
        if result["dimension"] <= 0:
            raise AssertionError("finite DLCQ phi^4 basis is empty")
        if result["hermiticity_error"] > 1.0e-11:
            raise AssertionError("finite DLCQ phi^4 matrix is not Hermitian")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
