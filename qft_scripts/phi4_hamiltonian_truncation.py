#!/usr/bin/env python3
"""Finite normal-ordered 1+1 dimensional phi^4 Hamiltonian truncation.

The script builds a finite Fock-space matrix for a real scalar field on a
circle of circumference L, using the free massive modes as the basis and the
normal-ordered interaction

    H = H0 + lambda/4! * int_0^L :phi(x)^4: dx.

It is a regulator benchmark, not a continuum construction.  The cutoff is the
intersection of a momentum sector, a particle-number cutoff, a free-energy
cutoff, and a finite Fourier-mode window.  Continuum statements require a
separate counterterm and cutoff-extrapolation analysis.
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
    nmax: int = 2
    max_particles: int = 4
    energy_cutoff: float = 8.0
    mass: float = 1.0
    circumference: float = 8.0
    quartic_coupling: float = 0.4
    total_momentum: int = 0


def mode_labels(nmax: int) -> tuple[int, ...]:
    if nmax < 0:
        raise ValueError("nmax must be nonnegative")
    return tuple(range(-nmax, nmax + 1))


def frequencies(labels: tuple[int, ...], mass: float, circumference: float) -> dict[int, float]:
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    if circumference <= 0.0:
        raise ValueError("circumference must be positive")
    return {
        n: math.sqrt(mass * mass + (2.0 * math.pi * n / circumference) ** 2)
        for n in labels
    }


def free_energy(state: State, labels: tuple[int, ...], omega: dict[int, float]) -> float:
    return float(sum(occupation * omega[label] for occupation, label in zip(state, labels)))


def total_momentum_units(state: State, labels: tuple[int, ...]) -> int:
    return int(sum(occupation * label for occupation, label in zip(state, labels)))


def generate_basis(cfg: RunConfig) -> list[State]:
    labels = mode_labels(cfg.nmax)
    omega = frequencies(labels, cfg.mass, cfg.circumference)
    basis: list[State] = []
    for occupations in itertools.product(range(cfg.max_particles + 1), repeat=len(labels)):
        state = tuple(int(x) for x in occupations)
        if sum(state) > cfg.max_particles:
            continue
        if total_momentum_units(state, labels) != cfg.total_momentum:
            continue
        if free_energy(state, labels, omega) > cfg.energy_cutoff + 1.0e-12:
            continue
        basis.append(state)
    basis.sort(key=lambda state: (free_energy(state, labels, omega), sum(state), state))
    return basis


def apply_normal_ordered(
    state: State,
    creations: tuple[int, ...],
    annihilations: tuple[int, ...],
    labels: tuple[int, ...],
) -> tuple[State, float] | None:
    index = {label: idx for idx, label in enumerate(labels)}
    new_state = list(state)
    amplitude = 1.0

    for label in annihilations:
        pos = index[label]
        occupation = new_state[pos]
        if occupation == 0:
            return None
        amplitude *= math.sqrt(float(occupation))
        new_state[pos] = occupation - 1

    for label in creations:
        pos = index[label]
        occupation = new_state[pos]
        amplitude *= math.sqrt(float(occupation + 1))
        new_state[pos] = occupation + 1

    return tuple(new_state), amplitude


def normal_ordered_phi4_terms(
    labels: tuple[int, ...],
    omega: dict[int, float],
    circumference: float,
) -> dict[Term, float]:
    """Return coefficients of int :phi^4: dx in normal-ordered monomials."""
    terms: dict[Term, float] = {}
    norms = {label: 1.0 / math.sqrt(2.0 * circumference * omega[label]) for label in labels}
    for kinds in itertools.product(("create", "annihilate"), repeat=4):
        for mode_tuple in itertools.product(labels, repeat=4):
            phase_momentum = 0
            coefficient = circumference
            creations: list[int] = []
            annihilations: list[int] = []
            for kind, label in zip(kinds, mode_tuple):
                coefficient *= norms[label]
                if kind == "create":
                    phase_momentum -= label
                    creations.append(label)
                else:
                    phase_momentum += label
                    annihilations.append(label)
            if phase_momentum != 0:
                continue
            key = (tuple(sorted(creations)), tuple(sorted(annihilations)))
            terms[key] = terms.get(key, 0.0) + coefficient
    return terms


def interaction_matrix(cfg: RunConfig, basis: list[State] | None = None) -> np.ndarray:
    labels = mode_labels(cfg.nmax)
    omega = frequencies(labels, cfg.mass, cfg.circumference)
    if basis is None:
        basis = generate_basis(cfg)
    lookup = {state: idx for idx, state in enumerate(basis)}
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    terms = normal_ordered_phi4_terms(labels, omega, cfg.circumference)

    for col, state in enumerate(basis):
        for (creations, annihilations), coefficient in terms.items():
            result = apply_normal_ordered(state, creations, annihilations, labels)
            if result is None:
                continue
            final_state, amplitude = result
            row = lookup.get(final_state)
            if row is None:
                continue
            matrix[row, col] += coefficient * amplitude
    return matrix


def hamiltonian_matrix(cfg: RunConfig) -> tuple[list[State], np.ndarray, np.ndarray]:
    labels = mode_labels(cfg.nmax)
    omega = frequencies(labels, cfg.mass, cfg.circumference)
    basis = generate_basis(cfg)
    free = np.diag([free_energy(state, labels, omega) for state in basis])
    interaction = interaction_matrix(cfg, basis)
    hamiltonian = free + (cfg.quartic_coupling / math.factorial(4)) * interaction
    return basis, free, hamiltonian


def run(cfg: RunConfig) -> dict[str, object]:
    basis, free, hamiltonian = hamiltonian_matrix(cfg)
    eigenvalues = np.linalg.eigvalsh(hamiltonian)
    hermiticity_error = float(np.max(np.abs(hamiltonian - hamiltonian.T))) if basis else 0.0
    free_eigenvalues = np.linalg.eigvalsh(free)
    return {
        "nmax": cfg.nmax,
        "max_particles": cfg.max_particles,
        "energy_cutoff": cfg.energy_cutoff,
        "mass": cfg.mass,
        "circumference": cfg.circumference,
        "quartic_coupling": cfg.quartic_coupling,
        "total_momentum": cfg.total_momentum,
        "dimension": len(basis),
        "hermiticity_error": hermiticity_error,
        "lowest_energies": [float(x) for x in eigenvalues[: min(8, len(eigenvalues))]],
        "free_lowest_energies": [float(x) for x in free_eigenvalues[: min(8, len(free_eigenvalues))]],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nmax", type=int, default=2)
    parser.add_argument("--max-particles", type=int, default=4)
    parser.add_argument("--energy-cutoff", type=float, default=8.0)
    parser.add_argument("--mass", type=float, default=1.0)
    parser.add_argument("--circumference", type=float, default=8.0)
    parser.add_argument("--quartic-coupling", type=float, default=0.4)
    parser.add_argument("--total-momentum", type=int, default=0)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = RunConfig(
        nmax=1 if args.smoke else args.nmax,
        max_particles=3 if args.smoke else args.max_particles,
        energy_cutoff=5.0 if args.smoke else args.energy_cutoff,
        mass=1.0 if args.smoke else args.mass,
        circumference=6.0 if args.smoke else args.circumference,
        quartic_coupling=0.25 if args.smoke else args.quartic_coupling,
        total_momentum=args.total_momentum,
    )
    result = run(cfg)
    if args.smoke:
        if result["dimension"] <= 0:
            raise AssertionError("finite phi^4 truncation produced an empty basis")
        if result["hermiticity_error"] > 1.0e-11:
            raise AssertionError("finite phi^4 truncation matrix is not Hermitian")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
