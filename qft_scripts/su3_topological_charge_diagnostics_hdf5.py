#!/usr/bin/env python3
"""Finite SU(3) clover topological-charge diagnostics for lattice links.

The theorem anchor is Volume XI, Chapter 5: finite-lattice Wilson flow and
topological charge.  The script computes the clover curvature diagnostic

    Q_clover = (32*pi^2)^(-1) sum_x eps_{mu nu rho sigma}
               Re Tr(F_mu_nu^clover(x) F_rho_sigma^clover(x))

from a finite periodic SU(3) configuration.  It can read the flowed-link
checkpoint written by su3_wilson_flow_hdf5.py or the raw-link checkpoint
written by su3_gauge_4d_metropolis_hdf5.py.

This is not a geometric or index-theoretic topological charge definition.
It is a finite-regulator diagnostic whose continuum interpretation requires
a scaling trajectory and a separate admissibility or Dirac-index construction.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np

import su3_gauge_4d_metropolis_hdf5 as su3
import su3_wilson_flow_hdf5 as flow


POSITIVE_DIRECTIONS = tuple(range(su3.DIRECTIONS))


@dataclass(frozen=True)
class TopologyConfig:
    L: int
    seed: int
    start: str = "cold"
    input_hdf5: Path | None = None
    input_dataset: str = "auto"
    output_hdf5: Path | None = None
    write_density: bool = False


@dataclass(frozen=True)
class TopologyResult:
    L: int
    seed: int
    input_hdf5: str | None
    input_dataset: str
    output_hdf5: str | None
    plaquette_mean: float
    clover_action_density: float
    q_clover: float
    max_plaquette_deviation: float
    max_clover_antihermitian_error: float
    max_clover_trace_abs: float
    max_unitarity_error: float
    max_det_error: float


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def direction_axis(direction: int) -> int:
    if direction >= 0:
        return direction
    return -direction - 1


def direction_sign(direction: int) -> int:
    return 1 if direction >= 0 else -1


def shift_signed(site: tuple[int, int, int, int], direction: int, L: int) -> tuple[int, int, int, int]:
    return su3.shift_site(site, direction_axis(direction), direction_sign(direction), L)


def reverse_direction(direction: int) -> int:
    return -direction - 1 if direction >= 0 else -direction - 1


def directed_link(links: np.ndarray, site: tuple[int, int, int, int], direction: int) -> np.ndarray:
    axis = direction_axis(direction)
    if direction >= 0:
        return links[site + (axis,)]
    start = su3.shift_site(site, axis, -1, links.shape[0])
    return su3.dagger(links[start + (axis,)])


def oriented_plaquette(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    first: int,
    second: int,
) -> np.ndarray:
    after_first = shift_signed(site, first, links.shape[0])
    after_second = shift_signed(site, second, links.shape[0])
    after_first_second = shift_signed(after_first, second, links.shape[0])
    return (
        directed_link(links, site, first)
        @ directed_link(links, after_first, second)
        @ directed_link(links, after_first_second, reverse_direction(first))
        @ directed_link(links, after_second, reverse_direction(second))
    )


def clover_matrix(links: np.ndarray, site: tuple[int, int, int, int], mu: int, nu: int) -> np.ndarray:
    require(mu != nu, "clover directions must be distinct")
    if mu > nu:
        return -clover_matrix(links, site, nu, mu)
    minus_mu = reverse_direction(mu)
    minus_nu = reverse_direction(nu)
    return (
        oriented_plaquette(links, site, mu, nu)
        + oriented_plaquette(links, site, nu, minus_mu)
        + oriented_plaquette(links, site, minus_mu, minus_nu)
        + oriented_plaquette(links, site, minus_nu, mu)
    )


def clover_field_strength(links: np.ndarray, site: tuple[int, int, int, int], mu: int, nu: int) -> np.ndarray:
    return flow.antihermitian_traceless(clover_matrix(links, site, mu, nu)) / 4.0


def permutation_sign(values: tuple[int, int, int, int]) -> int:
    sign = 1
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return 0
            if values[i] > values[j]:
                sign *= -1
    return sign


def local_q_density(links: np.ndarray, site: tuple[int, int, int, int]) -> float:
    fields: dict[tuple[int, int], np.ndarray] = {}
    for mu in POSITIVE_DIRECTIONS:
        for nu in POSITIVE_DIRECTIONS:
            if mu == nu:
                continue
            if mu < nu:
                fields[(mu, nu)] = clover_field_strength(links, site, mu, nu)
            else:
                fields[(mu, nu)] = -fields[(nu, mu)]
    total = 0.0
    for mu in POSITIVE_DIRECTIONS:
        for nu in POSITIVE_DIRECTIONS:
            for rho in POSITIVE_DIRECTIONS:
                for sigma in POSITIVE_DIRECTIONS:
                    eps = permutation_sign((mu, nu, rho, sigma))
                    if eps:
                        total += eps * float(np.real(np.trace(fields[(mu, nu)] @ fields[(rho, sigma)])))
    return total / (32.0 * math.pi * math.pi)


def local_clover_action_density(links: np.ndarray, site: tuple[int, int, int, int]) -> float:
    total = 0.0
    for mu in range(su3.DIRECTIONS):
        for nu in range(mu + 1, su3.DIRECTIONS):
            field = clover_field_strength(links, site, mu, nu)
            total += -float(np.real(np.trace(field @ field)))
    return total


def diagnostic_arrays(links: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    L = links.shape[0]
    q_density = np.empty((L, L, L, L), dtype=float)
    action_density = np.empty((L, L, L, L), dtype=float)
    for site in np.ndindex((L, L, L, L)):
        q_density[site] = local_q_density(links, site)
        action_density[site] = local_clover_action_density(links, site)
    return q_density, action_density


def max_plaquette_deviation(links: np.ndarray) -> float:
    identity = np.eye(su3.COLOR, dtype=np.complex128)
    max_deviation = 0.0
    L = links.shape[0]
    for site in np.ndindex((L, L, L, L)):
        for mu in range(su3.DIRECTIONS):
            for nu in range(mu + 1, su3.DIRECTIONS):
                max_deviation = max(
                    max_deviation,
                    float(np.linalg.norm(identity - su3.plaquette(links, site, mu, nu))),
                )
    return max_deviation


def clover_quality(links: np.ndarray) -> tuple[float, float]:
    max_antihermitian_error = 0.0
    max_trace_abs = 0.0
    L = links.shape[0]
    for site in np.ndindex((L, L, L, L)):
        for mu in range(su3.DIRECTIONS):
            for nu in range(mu + 1, su3.DIRECTIONS):
                field = clover_field_strength(links, site, mu, nu)
                max_antihermitian_error = max(
                    max_antihermitian_error,
                    float(np.linalg.norm(su3.dagger(field) + field)),
                )
                max_trace_abs = max(max_trace_abs, abs(np.trace(field)))
    return max_antihermitian_error, float(max_trace_abs)


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
    if "checkpoint/flowed_links" in handle:
        return "checkpoint/flowed_links"
    if "checkpoint/links" in handle:
        return "checkpoint/links"
    raise ValueError("input HDF5 file has neither checkpoint/flowed_links nor checkpoint/links")


def load_links_from_hdf5(path: Path, requested_dataset: str) -> tuple[np.ndarray, str]:
    h5py = import_h5py()
    with h5py.File(path, "r") as handle:
        dataset = resolve_dataset(handle, requested_dataset)
        return np.array(handle[dataset], dtype=np.complex128), dataset


def initial_links(cfg: TopologyConfig) -> tuple[np.ndarray, str]:
    if cfg.input_hdf5 is not None:
        links, dataset = load_links_from_hdf5(cfg.input_hdf5, cfg.input_dataset)
        require(links.shape == (cfg.L, cfg.L, cfg.L, cfg.L, su3.DIRECTIONS, su3.COLOR, su3.COLOR), "input shape does not match L")
        return links, dataset
    rng = np.random.default_rng(cfg.seed)
    return su3.initial_links(cfg.L, cfg.start, rng), "generated/" + cfg.start


def write_hdf5_output(
    path: Path,
    cfg: TopologyConfig,
    result: TopologyResult,
    q_density: np.ndarray,
    action_density: np.ndarray,
) -> None:
    h5py = import_h5py()
    path.parent.mkdir(parents=True, exist_ok=True)
    with h5py.File(path, "w") as handle:
        handle.attrs["script"] = Path(__file__).name
        handle.attrs["theorem_anchor"] = "Volume XI Chapter 5 clover topological-charge diagnostic"
        handle.attrs["input_hdf5"] = "" if cfg.input_hdf5 is None else str(cfg.input_hdf5)
        handle.attrs["input_dataset"] = result.input_dataset
        handle.attrs["L"] = cfg.L
        handle.attrs["q_clover"] = result.q_clover
        handle.attrs["clover_action_density"] = result.clover_action_density
        handle.attrs["plaquette_mean"] = result.plaquette_mean
        handle.attrs["max_plaquette_deviation"] = result.max_plaquette_deviation
        diagnostics = handle.create_group("diagnostics")
        diagnostics.attrs["write_density"] = cfg.write_density
        if cfg.write_density:
            diagnostics.create_dataset("q_density", data=q_density)
            diagnostics.create_dataset("clover_action_density", data=action_density)


def run(cfg: TopologyConfig) -> TopologyResult:
    require(cfg.L >= 2, "L must be at least two")
    links, input_dataset = initial_links(cfg)
    q_density, action_density = diagnostic_arrays(links)
    max_antihermitian_error, max_trace_abs = clover_quality(links)
    max_unitarity_error, max_det_error = su3.max_group_errors(links)
    plaquette_mean = flow.plaquette_mean(links)
    result = TopologyResult(
        L=cfg.L,
        seed=cfg.seed,
        input_hdf5=None if cfg.input_hdf5 is None else str(cfg.input_hdf5),
        input_dataset=input_dataset,
        output_hdf5=None if cfg.output_hdf5 is None else str(cfg.output_hdf5),
        plaquette_mean=plaquette_mean,
        clover_action_density=float(np.mean(action_density)),
        q_clover=float(np.sum(q_density)),
        max_plaquette_deviation=max_plaquette_deviation(links),
        max_clover_antihermitian_error=max_antihermitian_error,
        max_clover_trace_abs=max_trace_abs,
        max_unitarity_error=max_unitarity_error,
        max_det_error=max_det_error,
    )
    if cfg.output_hdf5 is not None:
        write_hdf5_output(cfg.output_hdf5, cfg, result, q_density, action_density)
    return result


def result_to_json(result: TopologyResult) -> str:
    return json.dumps(result.__dict__, sort_keys=True)


def run_smoke_test() -> None:
    cfg = TopologyConfig(L=2, seed=20260527, start="cold")
    result = run(cfg)
    require(abs(result.q_clover) < 1.0e-12, "cold configuration should have zero clover charge")
    require(abs(result.clover_action_density) < 1.0e-12, "cold configuration should have zero clover action density")
    require(result.max_plaquette_deviation < 1.0e-12, "cold plaquettes should be identity")
    require(result.max_clover_antihermitian_error < 1.0e-12, "clover field is not anti-Hermitian")
    require(result.max_clover_trace_abs < 1.0e-12, "clover field is not traceless")
    print(result_to_json(result))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=2)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--start", choices=["hot", "cold"], default="cold")
    parser.add_argument("--input-hdf5", type=Path)
    parser.add_argument("--input-dataset", default="auto")
    parser.add_argument("--output-hdf5", type=Path)
    parser.add_argument("--write-density", action="store_true")
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    cfg = TopologyConfig(
        L=args.L,
        seed=args.seed,
        start=args.start,
        input_hdf5=args.input_hdf5,
        input_dataset=args.input_dataset,
        output_hdf5=args.output_hdf5,
        write_density=args.write_density,
    )
    print(result_to_json(run(cfg)))


if __name__ == "__main__":
    main()
