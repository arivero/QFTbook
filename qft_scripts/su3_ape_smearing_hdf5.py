#!/usr/bin/env python3
"""Finite SU(3) APE-smearing tool for checkpointed lattice links.

The theorem anchor is Volume XI, Chapter 5: gauge-covariant link smearing.
The script applies the finite-regulator APE map

    U_mu(x) -> Proj_SU(3)((1-alpha) U_mu(x)
                 + alpha/(2(d_active-1)) C_mu(x))

where C_mu(x) is the staple sum over the active smearing directions.  In
``spatial`` mode the active directions are 1,2,3 and temporal links are left
unchanged; in ``all`` mode all four Euclidean directions are smeared.

This is an operator-construction utility for finite lattice data.  It is not
a continuum extrapolation, not an improvement theorem, and not a replacement
for a variational excited-state analysis.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

import su3_gauge_4d_metropolis_hdf5 as su3


@dataclass(frozen=True)
class SmearingConfig:
    L: int
    alpha: float
    steps: int
    seed: int
    start: str = "cold"
    mode: str = "spatial"
    input_hdf5: Path | None = None
    input_dataset: str = "auto"
    output_hdf5: Path | None = None


@dataclass(frozen=True)
class SmearingResult:
    L: int
    alpha: float
    steps: int
    seed: int
    start: str
    mode: str
    input_hdf5: str | None
    input_dataset: str
    output_hdf5: str | None
    initial_plaquette: float
    final_plaquette: float
    max_unitarity_error: float
    max_det_error: float


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def active_directions(mode: str) -> tuple[int, ...]:
    if mode == "spatial":
        return (1, 2, 3)
    if mode == "all":
        return tuple(range(su3.DIRECTIONS))
    raise ValueError("mode must be 'spatial' or 'all'")


def plaquette_mean(links: np.ndarray) -> float:
    return su3.total_plaquette_score(links) / float(6 * links.shape[0] ** su3.DIRECTIONS)


def staple_sum(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
    directions: tuple[int, ...],
) -> np.ndarray:
    L = links.shape[0]
    staple = np.zeros((su3.COLOR, su3.COLOR), dtype=np.complex128)
    for nu in directions:
        if nu == mu:
            continue
        x_mu = su3.shift_site(site, mu, 1, L)
        x_nu = su3.shift_site(site, nu, 1, L)
        x_minus_nu = su3.shift_site(site, nu, -1, L)
        x_minus_nu_plus_mu = su3.shift_site(x_minus_nu, mu, 1, L)
        staple += (
            links[site + (nu,)]
            @ links[x_nu + (mu,)]
            @ su3.dagger(links[x_mu + (nu,)])
        )
        staple += (
            su3.dagger(links[x_minus_nu + (nu,)])
            @ links[x_minus_nu + (mu,)]
            @ links[x_minus_nu_plus_mu + (nu,)]
        )
    return staple


def ape_smear_once(links: np.ndarray, alpha: float, mode: str) -> np.ndarray:
    directions = active_directions(mode)
    require(len(directions) >= 2, "at least two active directions are needed")
    L = links.shape[0]
    smeared = links.copy()
    normalization = 2.0 * (len(directions) - 1)
    for site in np.ndindex((L, L, L, L)):
        for mu in directions:
            preprojection = (
                (1.0 - alpha) * links[site + (mu,)]
                + (alpha / normalization) * staple_sum(links, site, mu, directions)
            )
            smeared[site + (mu,)] = su3.project_to_su3(preprojection)
    return smeared


def ape_smear(links: np.ndarray, alpha: float, steps: int, mode: str) -> tuple[np.ndarray, np.ndarray]:
    require(0.0 <= alpha <= 1.0, "alpha must lie in [0,1]")
    require(steps >= 1, "steps must be positive")
    trajectory = [plaquette_mean(links)]
    current = links.copy()
    for _ in range(steps):
        current = ape_smear_once(current, alpha, mode)
        trajectory.append(plaquette_mean(current))
    return current, np.array(trajectory, dtype=float)


def import_h5py():
    try:
        import h5py  # type: ignore
    except ImportError as exc:
        raise RuntimeError("HDF5 input/output requires h5py") from exc
    return h5py


def resolve_dataset(handle, requested: str) -> str:
    if requested != "auto":
        require(requested in handle, f"input dataset {requested!r} not found")
        return requested
    if "checkpoint/smeared_links" in handle:
        return "checkpoint/smeared_links"
    if "checkpoint/flowed_links" in handle:
        return "checkpoint/flowed_links"
    if "checkpoint/links" in handle:
        return "checkpoint/links"
    raise ValueError("input HDF5 file has no recognized link checkpoint")


def load_links_from_hdf5(path: Path, requested_dataset: str) -> tuple[np.ndarray, str]:
    h5py = import_h5py()
    with h5py.File(path, "r") as handle:
        dataset = resolve_dataset(handle, requested_dataset)
        return np.array(handle[dataset], dtype=np.complex128), dataset


def initial_links(cfg: SmearingConfig) -> tuple[np.ndarray, str]:
    if cfg.input_hdf5 is not None:
        links, dataset = load_links_from_hdf5(cfg.input_hdf5, cfg.input_dataset)
        require(links.shape == (cfg.L, cfg.L, cfg.L, cfg.L, su3.DIRECTIONS, su3.COLOR, su3.COLOR), "input shape does not match L")
        return links, dataset
    rng = np.random.default_rng(cfg.seed)
    return su3.initial_links(cfg.L, cfg.start, rng), "generated/" + cfg.start


def write_hdf5_output(
    path: Path,
    cfg: SmearingConfig,
    result: SmearingResult,
    trajectory: np.ndarray,
    links: np.ndarray,
) -> None:
    h5py = import_h5py()
    path.parent.mkdir(parents=True, exist_ok=True)
    with h5py.File(path, "w") as handle:
        handle.attrs["script"] = Path(__file__).name
        handle.attrs["theorem_anchor"] = "Volume XI Chapter 5 gauge-covariant link smearing"
        handle.attrs["input_hdf5"] = "" if cfg.input_hdf5 is None else str(cfg.input_hdf5)
        handle.attrs["input_dataset"] = result.input_dataset
        handle.attrs["L"] = cfg.L
        handle.attrs["alpha"] = cfg.alpha
        handle.attrs["steps"] = cfg.steps
        handle.attrs["mode"] = cfg.mode
        handle.attrs["active_directions_json"] = json.dumps(active_directions(cfg.mode))
        handle.attrs["initial_plaquette"] = result.initial_plaquette
        handle.attrs["final_plaquette"] = result.final_plaquette
        smearing = handle.create_group("smearing")
        smearing.create_dataset("plaquette_trajectory", data=trajectory)
        checkpoint = handle.create_group("checkpoint")
        checkpoint.create_dataset("smeared_links", data=links, compression="gzip")


def run(cfg: SmearingConfig) -> SmearingResult:
    require(cfg.L >= 2, "L must be at least two")
    links, input_dataset = initial_links(cfg)
    smeared, trajectory = ape_smear(links, cfg.alpha, cfg.steps, cfg.mode)
    max_unitarity_error, max_det_error = su3.max_group_errors(smeared)
    result = SmearingResult(
        L=cfg.L,
        alpha=cfg.alpha,
        steps=cfg.steps,
        seed=cfg.seed,
        start=cfg.start,
        mode=cfg.mode,
        input_hdf5=None if cfg.input_hdf5 is None else str(cfg.input_hdf5),
        input_dataset=input_dataset,
        output_hdf5=None if cfg.output_hdf5 is None else str(cfg.output_hdf5),
        initial_plaquette=float(trajectory[0]),
        final_plaquette=float(trajectory[-1]),
        max_unitarity_error=max_unitarity_error,
        max_det_error=max_det_error,
    )
    if cfg.output_hdf5 is not None:
        write_hdf5_output(cfg.output_hdf5, cfg, result, trajectory, smeared)
    return result


def result_to_json(result: SmearingResult) -> str:
    return json.dumps(result.__dict__, sort_keys=True)


def run_smoke_test() -> None:
    cfg = SmearingConfig(L=2, alpha=0.5, steps=3, seed=20260527, start="cold")
    result = run(cfg)
    require(abs(result.initial_plaquette - 1.0) < 1.0e-12, "cold initial plaquette should be one")
    require(abs(result.final_plaquette - 1.0) < 1.0e-12, "cold smeared plaquette should be one")
    require(result.max_unitarity_error < 1.0e-12, "smeared cold links are not unitary")
    require(result.max_det_error < 1.0e-12, "smeared cold links do not have determinant one")
    print(result_to_json(result))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=2)
    parser.add_argument("--alpha", type=float, default=0.5)
    parser.add_argument("--steps", type=int, default=4)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--start", choices=["hot", "cold"], default="cold")
    parser.add_argument("--mode", choices=["spatial", "all"], default="spatial")
    parser.add_argument("--input-hdf5", type=Path)
    parser.add_argument("--input-dataset", default="auto")
    parser.add_argument("--output-hdf5", type=Path)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    cfg = SmearingConfig(
        L=args.L,
        alpha=args.alpha,
        steps=args.steps,
        seed=args.seed,
        start=args.start,
        mode=args.mode,
        input_hdf5=args.input_hdf5,
        input_dataset=args.input_dataset,
        output_hdf5=args.output_hdf5,
    )
    print(result_to_json(run(cfg)))


if __name__ == "__main__":
    main()
