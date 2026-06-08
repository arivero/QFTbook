#!/usr/bin/env python3
"""Finite NS/R TFFSA-style Ising spin-field sector benchmark.

The finite-volume massive Ising free-fermion Hilbert space is the direct sum
of Neveu-Schwarz (NS) and Ramond (R) sectors.  The magnetic perturbation by
the spin field maps NS states to R states and conversely.  This script builds
a small zero-momentum NS/R sector block and keeps the spin perturbation in the
off-diagonal sector blocks.

Matrix elements use an asymptotic infinite-volume Ising spin form factor

    F_n^sigma(theta_1,...,theta_n)
      = sigma_bar i^{floor(n/2)} prod_{i<j} tanh((theta_i-theta_j)/2),

with the free Bethe-state density rho_I = prod_i m L cosh(theta_i).  Exact
finite-volume TFFSA uses NS/R finite-size spin matrix elements and vacuum
energies; the present script is a finite sector-structure and normalization
benchmark with an exp(-mL) asymptotic error indicator, not a production
magnetic-Ising spectrum.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass

import numpy as np


@dataclass
class SectorState:
    label: str
    sector: str
    parity: int
    rapidities: tuple[float, ...]
    energy: float
    density: float


@dataclass
class RunConfig:
    num_pairs: int
    mass: float
    circumference: float
    magnetic_coupling: float
    sigma_bar: float
    mass_sign: int = 1


def tanh_product(thetas: list[complex]) -> complex:
    value = 1.0 + 0.0j
    for i, theta_i in enumerate(thetas):
        for theta_j in thetas[i + 1 :]:
            value *= cmath.tanh((theta_i - theta_j) / 2.0)
    return value


def spin_sector_form_factor(thetas: list[complex], sigma_bar: float) -> complex:
    n = len(thetas)
    return sigma_bar * (1j ** (n // 2)) * tanh_product(thetas)


def required_fermion_parity(sector: str, mass_sign: int) -> int:
    if sector == "NS":
        return 0
    if sector == "R":
        return 1 if mass_sign >= 0 else 0
    raise ValueError(f"unknown sector {sector!r}")


def one_particle_data(mode: float, mass: float, circumference: float) -> tuple[float, float, float]:
    momentum = 2.0 * math.pi * mode / circumference
    theta = math.asinh(momentum / mass) if momentum != 0.0 else 0.0
    omega = math.sqrt(momentum * momentum + mass * mass)
    density = mass * circumference * math.cosh(theta)
    return theta, omega, density


def sector_basis(
    num_pairs: int,
    mass: float,
    circumference: float,
    mass_sign: int = 1,
) -> list[SectorState]:
    if num_pairs < 0:
        raise ValueError("num_pairs must be nonnegative")
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    if circumference <= 0.0:
        raise ValueError("circumference must be positive")
    if mass_sign not in (-1, 1):
        raise ValueError("mass_sign must be +1 or -1")

    states: list[SectorState] = [
        SectorState(
            label="NS:vac",
            sector="NS",
            parity=0,
            rapidities=(),
            energy=0.0,
            density=1.0,
        )
    ]
    for n in range(num_pairs):
        mode = n + 0.5
        theta, omega, density_one = one_particle_data(mode, mass, circumference)
        states.append(
            SectorState(
                label=f"NS:pair({mode:g})",
                sector="NS",
                parity=0,
                rapidities=(theta, -theta),
                energy=2.0 * omega,
                density=density_one * density_one,
            )
        )

    r_parity = required_fermion_parity("R", mass_sign)
    if r_parity == 1:
        theta_0, omega_0, density_0 = one_particle_data(0.0, mass, circumference)
        states.append(
            SectorState(
                label="R:zero",
                sector="R",
                parity=1,
                rapidities=(theta_0,),
                energy=omega_0,
                density=density_0,
            )
        )
        for n in range(1, num_pairs + 1):
            theta, omega, density_one = one_particle_data(float(n), mass, circumference)
            states.append(
                SectorState(
                    label=f"R:zero+pair({n})",
                    sector="R",
                    parity=1,
                    rapidities=(theta_0, theta, -theta),
                    energy=omega_0 + 2.0 * omega,
                    density=density_0 * density_one * density_one,
                )
            )
    else:
        states.append(
            SectorState(
                label="R:vac",
                sector="R",
                parity=0,
                rapidities=(),
                energy=0.0,
                density=1.0,
            )
        )
        for n in range(1, num_pairs + 1):
            theta, omega, density_one = one_particle_data(float(n), mass, circumference)
            states.append(
                SectorState(
                    label=f"R:pair({n})",
                    sector="R",
                    parity=0,
                    rapidities=(theta, -theta),
                    energy=2.0 * omega,
                    density=density_one * density_one,
                )
            )
    return states


def sector_spin_matrix_element(
    bra_index: int,
    ket_index: int,
    states: list[SectorState],
    sigma_bar: float,
) -> complex:
    """Asymptotic cross-sector spin matrix element before spatial integration."""

    bra = states[bra_index]
    ket = states[ket_index]
    if bra.sector == ket.sector:
        return 0.0 + 0.0j

    outgoing = list(bra.rapidities)
    incoming = list(ket.rapidities)
    crossed = [complex(theta, math.pi) for theta in outgoing] + [
        complex(theta) for theta in incoming
    ]
    density = math.sqrt(bra.density * ket.density)
    return spin_sector_form_factor(crossed, sigma_bar) / density


def finite_size_error_indicator(cfg: RunConfig) -> float:
    return math.exp(-cfg.mass * cfg.circumference)


def finite_matrix(cfg: RunConfig) -> np.ndarray:
    states = sector_basis(cfg.num_pairs, cfg.mass, cfg.circumference, cfg.mass_sign)
    size = len(states)
    matrix = np.zeros((size, size), dtype=complex)
    for i in range(size):
        matrix[i, i] = states[i].energy
    for i in range(size):
        for j in range(i + 1, size):
            value = (
                cfg.magnetic_coupling
                * cfg.circumference
                * sector_spin_matrix_element(i, j, states, cfg.sigma_bar)
            )
            matrix[i, j] = value
            matrix[j, i] = np.conjugate(value)
    return matrix


def run(cfg: RunConfig) -> dict[str, float | int | list[float]]:
    matrix = finite_matrix(cfg)
    hermiticity_error = float(np.max(np.abs(matrix - matrix.conjugate().T)))
    eigs = np.linalg.eigvalsh(matrix)
    states = sector_basis(cfg.num_pairs, cfg.mass, cfg.circumference, cfg.mass_sign)
    h_zero = finite_matrix(
        RunConfig(
            num_pairs=cfg.num_pairs,
            mass=cfg.mass,
            circumference=cfg.circumference,
            magnetic_coupling=0.0,
            sigma_bar=cfg.sigma_bar,
            mass_sign=cfg.mass_sign,
        )
    )
    perturbation = matrix - h_zero
    same_sector_mask = np.array(
        [[states[i].sector == states[j].sector for j in range(len(states))] for i in range(len(states))]
    )
    same_sector_perturbation = np.where(same_sector_mask, perturbation, 0.0)
    free_energies = [state.energy for state in states]
    return {
        "num_pairs": cfg.num_pairs,
        "mass": cfg.mass,
        "mass_sign": cfg.mass_sign,
        "circumference": cfg.circumference,
        "magnetic_coupling": cfg.magnetic_coupling,
        "sigma_bar": cfg.sigma_bar,
        "hermiticity_error": hermiticity_error,
        "ns_state_count": sum(1 for state in states if state.sector == "NS"),
        "r_state_count": sum(1 for state in states if state.sector == "R"),
        "same_sector_perturbation_max_abs": float(np.max(np.abs(same_sector_perturbation))),
        "finite_size_error_indicator": finite_size_error_indicator(cfg),
        "state_labels": [state.label for state in states[: min(8, len(states))]],
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
    parser.add_argument("--mass-sign", type=int, choices=[-1, 1], default=1)
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
        args.mass_sign = 1
    cfg = RunConfig(
        num_pairs=args.num_pairs,
        mass=args.mass,
        circumference=args.circumference,
        magnetic_coupling=args.magnetic_coupling,
        sigma_bar=args.sigma_bar,
        mass_sign=args.mass_sign,
    )
    result = run(cfg)
    if args.smoke and result["hermiticity_error"] > 1.0e-12:
        raise AssertionError("finite TFFSA block is not Hermitian")
    if args.smoke and result["same_sector_perturbation_max_abs"] > 1.0e-12:
        raise AssertionError("spin perturbation has same-sector entries")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
