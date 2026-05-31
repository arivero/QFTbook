#!/usr/bin/env python3
"""Finite HMC/RHMC smoke module.

This script is a finite-regulator diagnostic for Volume XI, Chapter 6.  It
samples a periodic one-dimensional lattice scalar action by HMC and evaluates
a positive rational pseudofermion action by shifted linear solves.  The output
is a JSON certificate of finite quantities: acceptance, reversible-integration
defect, Hamiltonian change, rational action, and linear-solver residuals.

The script is not a continuum extrapolation and does not claim ergodicity of a
large lattice gauge-theory chain.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np


@dataclass
class RunConfig:
    sites: int
    mass2: float
    quartic: float
    stiffness: float
    step_size: float
    leapfrog_steps: int
    trajectories: int
    therm: int
    seed: int
    cg_tol: float


def action(q: np.ndarray, cfg: RunConfig) -> float:
    gradient_term = np.roll(q, -1) - q
    return float(
        0.5 * cfg.mass2 * np.dot(q, q)
        + 0.25 * cfg.quartic * np.sum(q**4)
        + 0.5 * cfg.stiffness * np.dot(gradient_term, gradient_term)
    )


def force(q: np.ndarray, cfg: RunConfig) -> np.ndarray:
    return (
        cfg.mass2 * q
        + cfg.quartic * q**3
        + cfg.stiffness * (2.0 * q - np.roll(q, 1) - np.roll(q, -1))
    )


def hamiltonian(q: np.ndarray, p: np.ndarray, cfg: RunConfig) -> float:
    return action(q, cfg) + 0.5 * float(np.dot(p, p))


def leapfrog(q: np.ndarray, p: np.ndarray, cfg: RunConfig, sign: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    eps = sign * cfg.step_size
    q_new = np.array(q, dtype=float, copy=True)
    p_new = np.array(p, dtype=float, copy=True)
    p_new -= 0.5 * eps * force(q_new, cfg)
    for step in range(cfg.leapfrog_steps):
        q_new += eps * p_new
        if step != cfg.leapfrog_steps - 1:
            p_new -= eps * force(q_new, cfg)
    p_new -= 0.5 * eps * force(q_new, cfg)
    return q_new, p_new


def reversibility_defect(q: np.ndarray, p: np.ndarray, cfg: RunConfig) -> float:
    q_forward, p_forward = leapfrog(q, p, cfg, sign=1.0)
    q_back, p_back = leapfrog(q_forward, p_forward, cfg, sign=-1.0)
    return float(np.linalg.norm(q_back - q) + np.linalg.norm(p_back - p))


def positive_matrix(q: np.ndarray) -> np.ndarray:
    sites = q.size
    laplacian = 2.0 * np.eye(sites)
    for i in range(sites):
        laplacian[i, (i + 1) % sites] -= 1.0
        laplacian[i, (i - 1) % sites] -= 1.0
    return np.diag(1.25 + 0.15 * q**2) + 0.05 * laplacian


def conjugate_gradient(
    matrix: np.ndarray,
    rhs: np.ndarray,
    tol: float,
    maxiter: int | None = None,
) -> tuple[np.ndarray, float, int]:
    if maxiter is None:
        maxiter = 10 * rhs.size
    x = np.zeros_like(rhs, dtype=float)
    residual = rhs - matrix @ x
    direction = residual.copy()
    residual_norm_sq = float(np.dot(residual, residual))
    if residual_norm_sq == 0.0:
        return x, 0.0, 0
    for iteration in range(1, maxiter + 1):
        mat_direction = matrix @ direction
        alpha = residual_norm_sq / float(np.dot(direction, mat_direction))
        x = x + alpha * direction
        residual = residual - alpha * mat_direction
        next_norm_sq = float(np.dot(residual, residual))
        if np.sqrt(next_norm_sq) <= tol:
            return x, float(np.sqrt(next_norm_sq)), iteration
        beta = next_norm_sq / residual_norm_sq
        direction = residual + beta * direction
        residual_norm_sq = next_norm_sq
    return x, float(np.sqrt(residual_norm_sq)), maxiter


def rational_pseudofermion_action(
    matrix: np.ndarray,
    phi: np.ndarray,
    tol: float,
) -> dict[str, float | int]:
    constant = 0.08
    shifts = [0.20, 0.75, 1.60]
    coefficients = [0.70, 0.35, 0.18]
    action_value = constant * float(np.dot(phi, phi))
    max_residual = 0.0
    total_iterations = 0
    for coefficient, shift in zip(coefficients, shifts):
        shifted = matrix + shift * np.eye(matrix.shape[0])
        solution, residual, iterations = conjugate_gradient(shifted, phi, tol)
        action_value += coefficient * float(np.dot(phi, solution))
        max_residual = max(max_residual, residual)
        total_iterations += iterations
    return {
        "rational_action": action_value,
        "max_cg_residual": max_residual,
        "total_cg_iterations": total_iterations,
    }


def run(cfg: RunConfig) -> dict[str, float | int]:
    rng = np.random.default_rng(cfg.seed)
    q = rng.normal(scale=0.3, size=cfg.sites)
    accepted = 0
    delta_h_values: list[float] = []
    q2_values: list[float] = []
    action_values: list[float] = []
    last_reversibility = 0.0

    for trajectory in range(cfg.trajectories):
        p = rng.normal(size=cfg.sites)
        h_initial = hamiltonian(q, p, cfg)
        q_proposed, p_proposed = leapfrog(q, p, cfg)
        h_final = hamiltonian(q_proposed, p_proposed, cfg)
        delta_h = h_final - h_initial
        delta_h_values.append(delta_h)
        if delta_h <= 0.0 or rng.random() < float(np.exp(-delta_h)):
            q = q_proposed
            accepted += 1
        last_reversibility = reversibility_defect(q, rng.normal(size=cfg.sites), cfg)
        if trajectory >= cfg.therm:
            q2_values.append(float(np.dot(q, q) / cfg.sites))
            action_values.append(action(q, cfg) / cfg.sites)

    if not q2_values:
        raise ValueError("therm must be smaller than trajectories")

    matrix = positive_matrix(q)
    phi = rng.normal(size=cfg.sites)
    rational = rational_pseudofermion_action(matrix, phi, cfg.cg_tol)
    min_eigenvalue = float(np.linalg.eigvalsh(matrix)[0])
    if min_eigenvalue <= 0.0:
        raise AssertionError("positive_matrix lost positive definiteness")

    result: dict[str, float | int] = {
        "sites": cfg.sites,
        "trajectories": cfg.trajectories,
        "therm": cfg.therm,
        "seed": cfg.seed,
        "acceptance": accepted / cfg.trajectories,
        "q2_mean": float(np.mean(q2_values)),
        "action_density_mean": float(np.mean(action_values)),
        "max_abs_delta_h": float(np.max(np.abs(delta_h_values))),
        "last_reversibility_defect": last_reversibility,
        "positive_matrix_min_eigenvalue": min_eigenvalue,
    }
    result.update(rational)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sites", type=int, default=16)
    parser.add_argument("--mass2", type=float, default=0.7)
    parser.add_argument("--quartic", type=float, default=0.8)
    parser.add_argument("--stiffness", type=float, default=0.5)
    parser.add_argument("--step-size", type=float, default=0.07)
    parser.add_argument("--leapfrog-steps", type=int, default=8)
    parser.add_argument("--trajectories", type=int, default=200)
    parser.add_argument("--therm", type=int, default=40)
    parser.add_argument("--seed", type=int, default=20260531)
    parser.add_argument("--cg-tol", type=float, default=1.0e-12)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.sites = 8
        args.trajectories = 32
        args.therm = 8
        args.step_size = 0.06
        args.leapfrog_steps = 5
        args.seed = 31415926
    cfg = RunConfig(
        sites=args.sites,
        mass2=args.mass2,
        quartic=args.quartic,
        stiffness=args.stiffness,
        step_size=args.step_size,
        leapfrog_steps=args.leapfrog_steps,
        trajectories=args.trajectories,
        therm=args.therm,
        seed=args.seed,
        cg_tol=args.cg_tol,
    )
    result = run(cfg)
    if args.smoke:
        if not (0.0 <= result["acceptance"] <= 1.0):
            raise AssertionError("HMC acceptance must be a probability")
        if result["positive_matrix_min_eigenvalue"] <= 0.0:
            raise AssertionError("positive matrix certificate failed")
        if result["max_cg_residual"] > 1.0e-8:
            raise AssertionError("CG residual too large in smoke mode")
        if result["last_reversibility_defect"] > 1.0e-10:
            raise AssertionError("leapfrog reversibility defect too large in smoke mode")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
