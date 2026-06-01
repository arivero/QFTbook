#!/usr/bin/env python3
"""Finite compact-boson TCSA vertex-assembly benchmark.

The script constructs a finite compact-boson Hilbert space with momentum
labels, optional winding labels, and oscillator descendants.  It then
assembles the finite matrix of the spatially integrated sine-Gordon vertex

    cos(alpha phi) = (V_alpha + V_{-alpha}) / 2

in a declared normal-ordering convention.  This is a finite-regulator
assembly check for a sine-Gordon TCSA calculation.  It is not, by itself, a
continuum sine-Gordon spectrum calculation: counterterms, cutoff extrapolation,
sector choices, and the relation between alpha, radius, and the conventional
beta normalization remain separate data.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from itertools import product

import numpy as np


@dataclass(frozen=True, order=True)
class State:
    momentum: int
    winding: int
    left: tuple[int, ...]
    right: tuple[int, ...]


@dataclass(frozen=True)
class RunConfig:
    momentum_max: int = 2
    winding_max: int = 0
    mode_max: int = 2
    level_cutoff: int = 2
    radius: float = 1.0
    alpha: float = 0.35
    coupling: float = 0.2
    spin_zero_only: bool = True


def oscillator_level(occupations: tuple[int, ...]) -> int:
    return sum((mode + 1) * count for mode, count in enumerate(occupations))


def oscillator_partitions(mode_max: int, level_cutoff: int) -> list[tuple[int, ...]]:
    if mode_max < 0:
        raise ValueError("mode_max must be nonnegative")
    if level_cutoff < 0:
        raise ValueError("level_cutoff must be nonnegative")
    if mode_max == 0:
        return [()]
    ranges = [range(level_cutoff // mode + 1) for mode in range(1, mode_max + 1)]
    states = [
        tuple(counts)
        for counts in product(*ranges)
        if oscillator_level(tuple(counts)) <= level_cutoff
    ]
    return sorted(states, key=lambda occ: (oscillator_level(occ), occ))


def spin(state: State) -> int:
    return state.momentum * state.winding + oscillator_level(state.left) - oscillator_level(state.right)


def free_energy(state: State, radius: float) -> float:
    if radius <= 0.0:
        raise ValueError("radius must be positive")
    zero_mode = 0.5 * (state.momentum / radius) ** 2 + 0.5 * (state.winding * radius) ** 2
    return zero_mode + oscillator_level(state.left) + oscillator_level(state.right)


def generate_basis(cfg: RunConfig) -> list[State]:
    if cfg.momentum_max < 0:
        raise ValueError("momentum_max must be nonnegative")
    if cfg.winding_max < 0:
        raise ValueError("winding_max must be nonnegative")
    partitions = oscillator_partitions(cfg.mode_max, cfg.level_cutoff)
    basis: list[State] = []
    for momentum in range(-cfg.momentum_max, cfg.momentum_max + 1):
        for winding in range(-cfg.winding_max, cfg.winding_max + 1):
            for left in partitions:
                for right in partitions:
                    if oscillator_level(left) + oscillator_level(right) > cfg.level_cutoff:
                        continue
                    state = State(momentum=momentum, winding=winding, left=left, right=right)
                    if cfg.spin_zero_only and spin(state) != 0:
                        continue
                    basis.append(state)
    return sorted(
        basis,
        key=lambda state: (
            free_energy(state, cfg.radius),
            state.momentum,
            state.winding,
            oscillator_level(state.left),
            state.left,
            state.right,
        ),
    )


def one_mode_vertex_element(charge: float, bra_occ: int, ket_occ: int, mode: int) -> float:
    """Return <bra| exp(s a^dagger) exp(-s a) |ket>, s=charge/sqrt(mode)."""

    if mode <= 0:
        raise ValueError("mode must be positive")
    s = float(charge) / math.sqrt(float(mode))
    total = 0.0
    for annihilated in range(ket_occ + 1):
        intermediate = ket_occ - annihilated
        created = bra_occ - intermediate
        if created < 0:
            continue
        coefficient = ((-s) ** annihilated) / math.factorial(annihilated)
        coefficient *= math.sqrt(math.factorial(ket_occ) / math.factorial(intermediate))
        coefficient *= (s**created) / math.factorial(created)
        coefficient *= math.sqrt(math.factorial(bra_occ) / math.factorial(intermediate))
        total += coefficient
    return total


def oscillator_vertex_element(charge: float, bra: tuple[int, ...], ket: tuple[int, ...]) -> float:
    if len(bra) != len(ket):
        raise ValueError("oscillator occupation tuples must have the same length")
    element = 1.0
    for mode_index, (bra_occ, ket_occ) in enumerate(zip(bra, ket), start=1):
        element *= one_mode_vertex_element(charge, bra_occ, ket_occ, mode_index)
    return element


def vertex_shift_matrix(
    cfg: RunConfig,
    basis: list[State],
    charge_sign: int,
    *,
    integrated: bool = True,
) -> np.ndarray:
    if charge_sign not in (-1, 1):
        raise ValueError("charge_sign must be +1 or -1")
    charge = charge_sign * float(cfg.alpha)
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    for i, bra in enumerate(basis):
        for j, ket in enumerate(basis):
            if bra.momentum != ket.momentum + charge_sign:
                continue
            if bra.winding != ket.winding:
                continue
            if integrated and spin(bra) != spin(ket):
                continue
            matrix[i, j] = oscillator_vertex_element(charge, bra.left, ket.left)
            matrix[i, j] *= oscillator_vertex_element(charge, bra.right, ket.right)
    return matrix


def cosine_vertex_matrix(cfg: RunConfig, basis: list[State], *, integrated: bool = True) -> np.ndarray:
    return 0.5 * (
        vertex_shift_matrix(cfg, basis, 1, integrated=integrated)
        + vertex_shift_matrix(cfg, basis, -1, integrated=integrated)
    )


def hamiltonian_matrix(cfg: RunConfig) -> tuple[list[State], np.ndarray, np.ndarray]:
    basis = generate_basis(cfg)
    free = np.diag([free_energy(state, cfg.radius) for state in basis])
    vertex = cosine_vertex_matrix(cfg, basis, integrated=True)
    return basis, free, free + float(cfg.coupling) * vertex


def run(cfg: RunConfig) -> dict[str, object]:
    basis, free, hamiltonian = hamiltonian_matrix(cfg)
    vertex = cosine_vertex_matrix(cfg, basis, integrated=True)
    local_vertex = cosine_vertex_matrix(cfg, basis, integrated=False)
    eigenvalues = np.linalg.eigvalsh(hamiltonian) if basis else np.array([])
    hermiticity_error = float(np.max(np.abs(hamiltonian - hamiltonian.T))) if basis else 0.0
    spin_leakage = 0.0
    winding_leakage = 0.0
    for i, bra in enumerate(basis):
        for j, ket in enumerate(basis):
            if spin(bra) != spin(ket):
                spin_leakage = max(spin_leakage, abs(float(vertex[i, j])))
            if bra.winding != ket.winding:
                winding_leakage = max(winding_leakage, abs(float(vertex[i, j])))
    return {
        "momentum_max": cfg.momentum_max,
        "winding_max": cfg.winding_max,
        "mode_max": cfg.mode_max,
        "level_cutoff": cfg.level_cutoff,
        "dimension": len(basis),
        "spin_zero_only": cfg.spin_zero_only,
        "hermiticity_error": hermiticity_error,
        "integrated_spin_leakage": spin_leakage,
        "winding_leakage": winding_leakage,
        "local_minus_integrated_norm": float(np.linalg.norm(local_vertex - vertex)),
        "free_lowest": [float(x) for x in np.linalg.eigvalsh(free)[: min(6, len(basis))]],
        "lowest_eigenvalues": [float(x) for x in eigenvalues[: min(6, len(eigenvalues))]],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--momentum-max", type=int, default=2)
    parser.add_argument("--winding-max", type=int, default=0)
    parser.add_argument("--mode-max", type=int, default=2)
    parser.add_argument("--level-cutoff", type=int, default=2)
    parser.add_argument("--radius", type=float, default=1.0)
    parser.add_argument("--alpha", type=float, default=0.35)
    parser.add_argument("--coupling", type=float, default=0.2)
    parser.add_argument("--all-spins", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.momentum_max = 2
        args.winding_max = 0
        args.mode_max = 2
        args.level_cutoff = 2
        args.radius = 1.0
        args.alpha = 0.3
        args.coupling = 0.15
    cfg = RunConfig(
        momentum_max=args.momentum_max,
        winding_max=args.winding_max,
        mode_max=args.mode_max,
        level_cutoff=args.level_cutoff,
        radius=args.radius,
        alpha=args.alpha,
        coupling=args.coupling,
        spin_zero_only=not args.all_spins,
    )
    result = run(cfg)
    if args.smoke:
        if result["dimension"] <= 0:
            raise AssertionError("compact-boson TCSA basis is empty")
        if result["hermiticity_error"] > 1.0e-12:
            raise AssertionError("finite sine-Gordon TCSA matrix is not Hermitian")
        if result["integrated_spin_leakage"] > 1.0e-12:
            raise AssertionError("spatially integrated vertex violates spin conservation")
        if result["winding_leakage"] > 1.0e-12:
            raise AssertionError("sine-Gordon vertex changed the winding label")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
