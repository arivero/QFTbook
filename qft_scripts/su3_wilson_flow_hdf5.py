#!/usr/bin/env python3
"""Finite SU(3) Wilson-flow evolution for checkpointed lattice links.

The theorem anchor is Volume XI, Chapter 5: finite-lattice Wilson flow.  The
script evolves a finite periodic SU(3) Wilson-gauge configuration by the
normalized Wilson-score gradient flow

    d V_mu(x) / d tau = Z_mu(x; V) V_mu(x),
    Q(V) = sum_p (1/3) Re Tr U_p,
    Z_mu = grad_left Q,

using a first-order Lie-Euler integrator.  It reads the checkpoint/links
dataset written by su3_gauge_4d_metropolis_hdf5.py, or creates a hot/cold
finite configuration when no input file is supplied.  HDF5 output records the
flow trajectory, final flowed links, and finite-regulator metadata.

This is a finite-cutoff smoothing tool.  It is not a proof of a continuum
limit, not an integer topological-charge definition, and not a production
lattice-QCD flow integrator.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

import su3_gauge_4d_metropolis_hdf5 as su3


@dataclass(frozen=True)
class FlowConfig:
    L: int
    steps: int
    step_size: float
    measure_every: int
    seed: int
    start: str = "hot"
    input_hdf5: Path | None = None
    output_hdf5: Path | None = None


@dataclass(frozen=True)
class FlowResult:
    L: int
    steps: int
    step_size: float
    measure_every: int
    seed: int
    measurement_count: int
    initial_plaquette: float
    final_plaquette: float
    initial_action_density: float
    final_action_density: float
    monotone_violations: int
    max_unitarity_error: float
    max_det_error: float
    input_hdf5: str | None
    output_hdf5: str | None


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def antihermitian_traceless(matrix: np.ndarray) -> np.ndarray:
    antihermitian = 0.5 * (matrix - su3.dagger(matrix))
    trace_part = np.trace(antihermitian) / su3.COLOR
    return antihermitian - trace_part * np.eye(su3.COLOR, dtype=np.complex128)


def staple_matrix(links: np.ndarray, site: tuple[int, int, int, int], mu: int) -> np.ndarray:
    L = links.shape[0]
    staple = np.zeros((su3.COLOR, su3.COLOR), dtype=np.complex128)
    for nu in range(su3.DIRECTIONS):
        if nu == mu:
            continue
        x_mu = su3.shift_site(site, mu, 1, L)
        x_nu = su3.shift_site(site, nu, 1, L)
        x_minus_nu = su3.shift_site(site, nu, -1, L)
        x_minus_nu_plus_mu = su3.shift_site(x_minus_nu, mu, 1, L)
        staple += (
            links[x_mu + (nu,)]
            @ su3.dagger(links[x_nu + (mu,)])
            @ su3.dagger(links[site + (nu,)])
        )
        staple += (
            su3.dagger(links[x_minus_nu_plus_mu + (nu,)])
            @ su3.dagger(links[x_minus_nu + (mu,)])
            @ links[x_minus_nu + (nu,)]
        )
    return staple


def score_gradient_generator(links: np.ndarray, site: tuple[int, int, int, int], mu: int) -> np.ndarray:
    local_matrix = links[site + (mu,)] @ staple_matrix(links, site, mu)
    return -antihermitian_traceless(local_matrix) / su3.COLOR


def antihermitian_exponential(generator: np.ndarray, step_size: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eig(generator)
    exponential = eigenvectors @ np.diag(np.exp(step_size * eigenvalues)) @ np.linalg.inv(eigenvectors)
    return su3.project_to_su3(exponential)


def flow_step(links: np.ndarray, step_size: float) -> np.ndarray:
    L = links.shape[0]
    generators = np.empty_like(links)
    for site in np.ndindex((L, L, L, L)):
        for mu in range(su3.DIRECTIONS):
            generators[site + (mu,)] = score_gradient_generator(links, site, mu)
    flowed = np.empty_like(links)
    for site in np.ndindex((L, L, L, L)):
        for mu in range(su3.DIRECTIONS):
            flowed[site + (mu,)] = antihermitian_exponential(generators[site + (mu,)], step_size) @ links[site + (mu,)]
    return flowed


def plaquette_mean(links: np.ndarray) -> float:
    L = links.shape[0]
    return su3.total_plaquette_score(links) / float(6 * L**su3.DIRECTIONS)


def action_density_from_plaquette(mean_plaquette: float) -> float:
    return 1.0 - mean_plaquette


def import_h5py():
    try:
        import h5py  # type: ignore
    except ImportError as exc:
        raise RuntimeError("HDF5 input/output requires h5py") from exc
    return h5py


def load_links_from_hdf5(path: Path) -> np.ndarray:
    h5py = import_h5py()
    with h5py.File(path, "r") as handle:
        return np.array(handle["checkpoint/links"], dtype=np.complex128)


def initial_links(cfg: FlowConfig) -> np.ndarray:
    if cfg.input_hdf5 is not None:
        links = load_links_from_hdf5(cfg.input_hdf5)
        require(links.shape == (cfg.L, cfg.L, cfg.L, cfg.L, su3.DIRECTIONS, su3.COLOR, su3.COLOR), "input checkpoint shape does not match L")
        return links
    rng = np.random.default_rng(cfg.seed)
    return su3.initial_links(cfg.L, cfg.start, rng)


def write_hdf5_output(
    path: Path,
    cfg: FlowConfig,
    result: FlowResult,
    tau: np.ndarray,
    plaquette: np.ndarray,
    action_density: np.ndarray,
    links: np.ndarray,
) -> None:
    h5py = import_h5py()
    path.parent.mkdir(parents=True, exist_ok=True)
    with h5py.File(path, "w") as handle:
        handle.attrs["script"] = Path(__file__).name
        handle.attrs["theorem_anchor"] = "Volume XI Chapter 5 finite-lattice Wilson flow"
        handle.attrs["input_hdf5"] = "" if cfg.input_hdf5 is None else str(cfg.input_hdf5)
        handle.attrs["L"] = cfg.L
        handle.attrs["steps"] = cfg.steps
        handle.attrs["step_size"] = cfg.step_size
        handle.attrs["measure_every"] = cfg.measure_every
        handle.attrs["seed"] = cfg.seed
        handle.attrs["start"] = cfg.start
        handle.attrs["monotone_violations"] = result.monotone_violations
        handle.attrs["max_unitarity_error"] = result.max_unitarity_error
        handle.attrs["max_det_error"] = result.max_det_error
        flow = handle.create_group("flow")
        flow.create_dataset("tau", data=tau)
        flow.create_dataset("plaquette", data=plaquette)
        flow.create_dataset("action_density", data=action_density)
        checkpoint = handle.create_group("checkpoint")
        checkpoint.create_dataset("flowed_links", data=links, compression="gzip")


def run(cfg: FlowConfig) -> FlowResult:
    require(cfg.L >= 2, "L must be at least two")
    require(cfg.steps >= 1, "steps must be positive")
    require(cfg.step_size > 0.0, "step size must be positive")
    require(cfg.measure_every >= 1, "measure_every must be positive")
    links = initial_links(cfg)

    tau_values: list[float] = [0.0]
    plaquette_values: list[float] = [plaquette_mean(links)]
    action_values: list[float] = [action_density_from_plaquette(plaquette_values[-1])]
    monotone_violations = 0

    for step in range(1, cfg.steps + 1):
        previous_score = su3.total_plaquette_score(links)
        links = flow_step(links, cfg.step_size)
        current_score = su3.total_plaquette_score(links)
        if current_score + 1.0e-10 < previous_score:
            monotone_violations += 1
        if step % cfg.measure_every == 0 or step == cfg.steps:
            tau_values.append(step * cfg.step_size)
            plaquette_values.append(plaquette_mean(links))
            action_values.append(action_density_from_plaquette(plaquette_values[-1]))

    max_unitarity_error, max_det_error = su3.max_group_errors(links)
    result = FlowResult(
        L=cfg.L,
        steps=cfg.steps,
        step_size=cfg.step_size,
        measure_every=cfg.measure_every,
        seed=cfg.seed,
        measurement_count=len(tau_values),
        initial_plaquette=plaquette_values[0],
        final_plaquette=plaquette_values[-1],
        initial_action_density=action_values[0],
        final_action_density=action_values[-1],
        monotone_violations=monotone_violations,
        max_unitarity_error=max_unitarity_error,
        max_det_error=max_det_error,
        input_hdf5=None if cfg.input_hdf5 is None else str(cfg.input_hdf5),
        output_hdf5=None if cfg.output_hdf5 is None else str(cfg.output_hdf5),
    )
    if cfg.output_hdf5 is not None:
        write_hdf5_output(
            cfg.output_hdf5,
            cfg,
            result,
            np.array(tau_values, dtype=float),
            np.array(plaquette_values, dtype=float),
            np.array(action_values, dtype=float),
            links,
        )
    return result


def result_to_json(result: FlowResult) -> str:
    return json.dumps(result.__dict__, sort_keys=True)


def run_smoke_test() -> None:
    cfg = FlowConfig(
        L=2,
        steps=5,
        step_size=0.015,
        measure_every=1,
        seed=20260527,
        start="hot",
    )
    result = run(cfg)
    require(result.measurement_count == 6, "unexpected flow smoke measurement count")
    require(result.monotone_violations == 0, "Wilson score decreased during smoke flow")
    require(result.final_action_density <= result.initial_action_density + 1.0e-10, "action density did not decrease")
    require(result.max_unitarity_error < 1.0e-10, "unitarity drift is too large")
    require(result.max_det_error < 1.0e-10, "determinant drift is too large")
    print(result_to_json(result))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=2)
    parser.add_argument("--steps", type=int, default=16)
    parser.add_argument("--step-size", type=float, default=0.01)
    parser.add_argument("--measure-every", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--start", choices=["hot", "cold"], default="hot")
    parser.add_argument("--input-hdf5", type=Path)
    parser.add_argument("--output-hdf5", type=Path)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    cfg = FlowConfig(
        L=args.L,
        steps=args.steps,
        step_size=args.step_size,
        measure_every=args.measure_every,
        seed=args.seed,
        start=args.start,
        input_hdf5=args.input_hdf5,
        output_hdf5=args.output_hdf5,
    )
    print(result_to_json(run(cfg)))


if __name__ == "__main__":
    main()
