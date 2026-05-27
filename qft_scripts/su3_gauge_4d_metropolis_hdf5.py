#!/usr/bin/env python3
"""Finite 4D SU(3) Wilson-gauge subgroup Metropolis sampler.

The theorem anchor is Volume XI, Chapter 6: finite SU(3) subgroup-update
invariance.  The script samples the finite periodic pure-gauge model

    probability(U) proportional to exp(beta * sum_p (1/3) Re Tr U_p)

by proposing small left multiplications in the three embedded SU(2) color
subgroups of SU(3).  It is a finite-regulator data generator: it can write an
HDF5 file containing measurements, metadata, and a final link checkpoint, and
it can also write a CSV table with columns sample,R,T,W for the static
potential analysis script.  It is not a proof of mixing, a continuum
extrapolation, or a replacement for mature production lattice-QCD codes.

HDF5 output requires the optional Python package h5py.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


DIRECTIONS = 4
COLOR = 3
COLOR_PAIRS = ((0, 1), (0, 2), (1, 2))


@dataclass(frozen=True)
class RunConfig:
    L: int
    beta: float
    proposal_width: float
    sweeps: int
    therm: int
    measure_every: int
    seed: int
    max_r: int
    max_t: int
    output_hdf5: Path | None = None
    samples_csv: Path | None = None
    resume_from: Path | None = None
    start: str = "hot"


@dataclass(frozen=True)
class RunResult:
    L: int
    beta: float
    proposal_width: float
    sweeps: int
    therm: int
    measure_every: int
    seed: int
    acceptance: float
    measurement_count: int
    plaquette_mean: float
    plaquette_stderr_naive: float
    max_r: int
    max_t: int
    hdf5_output: str | None
    samples_csv: str | None
    max_unitarity_error: float
    max_det_error: float


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shift_site(site: tuple[int, int, int, int], direction: int, step: int, L: int) -> tuple[int, int, int, int]:
    coords = list(site)
    coords[direction] = (coords[direction] + step) % L
    return (coords[0], coords[1], coords[2], coords[3])


def dagger(matrix: np.ndarray) -> np.ndarray:
    return np.conjugate(matrix.T)


def project_to_su3(matrix: np.ndarray) -> np.ndarray:
    u, _, vh = np.linalg.svd(matrix)
    unitary = u @ vh
    det = np.linalg.det(unitary)
    require(abs(det) > 0.0, "cannot project matrix with zero determinant")
    return unitary / det ** (1.0 / COLOR)


def random_su3(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(COLOR, COLOR)) + 1j * rng.normal(size=(COLOR, COLOR))
    q, r = np.linalg.qr(z)
    diagonal = np.diag(r)
    phases = np.ones_like(diagonal)
    nonzero = np.abs(diagonal) > 0.0
    phases[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    q = q @ np.diag(np.conjugate(phases))
    return project_to_su3(q)


def cold_links(L: int) -> np.ndarray:
    links = np.empty((L, L, L, L, DIRECTIONS, COLOR, COLOR), dtype=np.complex128)
    identity = np.eye(COLOR, dtype=np.complex128)
    for index in np.ndindex((L, L, L, L, DIRECTIONS)):
        links[index] = identity
    return links


def hot_links(L: int, rng: np.random.Generator) -> np.ndarray:
    links = np.empty((L, L, L, L, DIRECTIONS, COLOR, COLOR), dtype=np.complex128)
    for index in np.ndindex((L, L, L, L, DIRECTIONS)):
        links[index] = random_su3(rng)
    return links


def initial_links(L: int, start: str, rng: np.random.Generator) -> np.ndarray:
    if start == "cold":
        return cold_links(L)
    if start == "hot":
        return hot_links(L, rng)
    raise ValueError("start must be 'hot' or 'cold'")


def su2_block_from_axis_angle(axis: np.ndarray, angle: float) -> np.ndarray:
    norm = float(np.linalg.norm(axis))
    require(norm > 0.0, "axis must be nonzero")
    n1, n2, n3 = axis / norm
    c = math.cos(angle)
    s = math.sin(angle)
    return np.array(
        [
            [c + 1j * n3 * s, n2 * s + 1j * n1 * s],
            [-n2 * s + 1j * n1 * s, c - 1j * n3 * s],
        ],
        dtype=np.complex128,
    )


def embedded_su2(block: np.ndarray, pair: tuple[int, int]) -> np.ndarray:
    i, j = pair
    matrix = np.eye(COLOR, dtype=np.complex128)
    matrix[np.ix_([i, j], [i, j])] = block
    return matrix


def random_small_su3_subgroup(
    rng: np.random.Generator,
    width: float,
    pair: tuple[int, int] | None = None,
) -> tuple[np.ndarray, tuple[int, int]]:
    require(width > 0.0, "proposal width must be positive")
    chosen_pair = COLOR_PAIRS[int(rng.integers(len(COLOR_PAIRS)))] if pair is None else pair
    axis = rng.normal(size=3)
    if float(np.linalg.norm(axis)) == 0.0:
        axis = np.array([1.0, 0.0, 0.0], dtype=float)
    angle = float(rng.uniform(-width, width))
    return embedded_su2(su2_block_from_axis_angle(axis, angle), chosen_pair), chosen_pair


def plaquette(links: np.ndarray, site: tuple[int, int, int, int], mu: int, nu: int) -> np.ndarray:
    require(mu != nu, "plaquette directions must be distinct")
    L = links.shape[0]
    x_mu = shift_site(site, mu, 1, L)
    x_nu = shift_site(site, nu, 1, L)
    return (
        links[site + (mu,)]
        @ links[x_mu + (nu,)]
        @ dagger(links[x_nu + (mu,)])
        @ dagger(links[site + (nu,)])
    )


def plaquette_score(plaquette_matrix: np.ndarray) -> float:
    return float(np.real(np.trace(plaquette_matrix)) / COLOR)


def total_plaquette_score(links: np.ndarray) -> float:
    L = links.shape[0]
    score = 0.0
    for site in np.ndindex((L, L, L, L)):
        for mu in range(DIRECTIONS):
            for nu in range(mu + 1, DIRECTIONS):
                score += plaquette_score(plaquette(links, site, mu, nu))
    return score


def adjacent_plaquette_score(links: np.ndarray, site: tuple[int, int, int, int], mu: int) -> float:
    L = links.shape[0]
    score = 0.0
    for nu in range(DIRECTIONS):
        if nu == mu:
            continue
        score += plaquette_score(plaquette(links, site, mu, nu))
        score += plaquette_score(plaquette(links, shift_site(site, nu, -1, L), mu, nu))
    return score


def left_multiply_link_in_place(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
    proposal: np.ndarray,
) -> None:
    links[site + (mu,)] = proposal @ links[site + (mu,)]


def local_score_change_for_left_multiply(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
    proposal: np.ndarray,
) -> float:
    before = adjacent_plaquette_score(links, site, mu)
    old_link = links[site + (mu,)].copy()
    left_multiply_link_in_place(links, site, mu, proposal)
    after = adjacent_plaquette_score(links, site, mu)
    links[site + (mu,)] = old_link
    return after - before


def metropolis_sweep(links: np.ndarray, cfg: RunConfig, rng: np.random.Generator) -> int:
    L = cfg.L
    accepted = 0
    attempts = DIRECTIONS * L**DIRECTIONS
    for _ in range(attempts):
        site = (
            int(rng.integers(L)),
            int(rng.integers(L)),
            int(rng.integers(L)),
            int(rng.integers(L)),
        )
        mu = int(rng.integers(DIRECTIONS))
        proposal, _ = random_small_su3_subgroup(rng, cfg.proposal_width)
        delta_score = local_score_change_for_left_multiply(links, site, mu, proposal)
        if delta_score >= 0.0 or rng.random() < math.exp(cfg.beta * delta_score):
            left_multiply_link_in_place(links, site, mu, proposal)
            accepted += 1
    return accepted


def gauge_transform(links: np.ndarray, gauges: np.ndarray) -> np.ndarray:
    L = links.shape[0]
    transformed = np.empty_like(links)
    for site in np.ndindex((L, L, L, L)):
        for mu in range(DIRECTIONS):
            target = shift_site(site, mu, 1, L)
            transformed[site + (mu,)] = gauges[site] @ links[site + (mu,)] @ dagger(gauges[target])
    return transformed


def wilson_loop_rectangle(links: np.ndarray, r: int, t: int) -> float:
    require(r > 0 and t > 0, "rectangle sizes must be positive")
    L = links.shape[0]
    total = 0.0
    count = 0
    identity = np.eye(COLOR, dtype=np.complex128)
    for site in np.ndindex((L, L, L, L)):
        for mu in range(DIRECTIONS):
            for nu in range(mu + 1, DIRECTIONS):
                cursor = site
                loop = identity.copy()
                for _ in range(r):
                    loop = loop @ links[cursor + (mu,)]
                    cursor = shift_site(cursor, mu, 1, L)
                for _ in range(t):
                    loop = loop @ links[cursor + (nu,)]
                    cursor = shift_site(cursor, nu, 1, L)
                for _ in range(r):
                    cursor = shift_site(cursor, mu, -1, L)
                    loop = loop @ dagger(links[cursor + (mu,)])
                for _ in range(t):
                    cursor = shift_site(cursor, nu, -1, L)
                    loop = loop @ dagger(links[cursor + (nu,)])
                total += float(np.real(np.trace(loop)) / COLOR)
                count += 1
    return total / float(count)


def rectangular_wilson_loop_grid(links: np.ndarray, max_r: int, max_t: int) -> np.ndarray:
    require(max_r >= 1 and max_t >= 1, "max_r and max_t must be positive")
    grid = np.empty((max_r, max_t), dtype=float)
    for r in range(1, max_r + 1):
        for t in range(1, max_t + 1):
            grid[r - 1, t - 1] = wilson_loop_rectangle(links, r, t)
    return grid


def max_group_errors(links: np.ndarray) -> tuple[float, float]:
    identity = np.eye(COLOR, dtype=np.complex128)
    max_unitarity = 0.0
    max_det = 0.0
    for matrix in links.reshape((-1, COLOR, COLOR)):
        max_unitarity = max(max_unitarity, float(np.linalg.norm(dagger(matrix) @ matrix - identity)))
        max_det = max(max_det, abs(np.linalg.det(matrix) - 1.0))
    return max_unitarity, max_det


def import_h5py():
    try:
        import h5py  # type: ignore
    except ImportError as exc:
        raise RuntimeError("HDF5 output requires h5py; install h5py or omit --output-hdf5") from exc
    return h5py


def rng_from_state_json(state_json: str) -> np.random.Generator:
    rng = np.random.default_rng()
    rng.bit_generator.state = json.loads(state_json)
    return rng


def load_checkpoint(path: Path) -> tuple[np.ndarray, np.random.Generator, dict[str, Any]]:
    h5py = import_h5py()
    with h5py.File(path, "r") as handle:
        links = np.array(handle["checkpoint/links"], dtype=np.complex128)
        state_json = handle["checkpoint"].attrs["rng_state_json"]
        attrs = dict(handle.attrs)
    return links, rng_from_state_json(state_json), attrs


def write_hdf5_output(
    path: Path,
    cfg: RunConfig,
    result: RunResult,
    sweeps: np.ndarray,
    plaquettes: np.ndarray,
    acceptances: np.ndarray,
    wilson_loops: np.ndarray,
    links: np.ndarray,
    rng: np.random.Generator,
) -> None:
    h5py = import_h5py()
    path.parent.mkdir(parents=True, exist_ok=True)
    with h5py.File(path, "w") as handle:
        handle.attrs["script"] = Path(__file__).name
        handle.attrs["theorem_anchor"] = "Volume XI Chapter 6 SU(3) subgroup-update invariance"
        handle.attrs["L"] = cfg.L
        handle.attrs["beta"] = cfg.beta
        handle.attrs["proposal_width"] = cfg.proposal_width
        handle.attrs["sweeps"] = cfg.sweeps
        handle.attrs["therm"] = cfg.therm
        handle.attrs["measure_every"] = cfg.measure_every
        handle.attrs["seed"] = cfg.seed
        handle.attrs["max_r"] = cfg.max_r
        handle.attrs["max_t"] = cfg.max_t
        handle.attrs["start"] = cfg.start
        handle.attrs["resume_from"] = "" if cfg.resume_from is None else str(cfg.resume_from)
        handle.attrs["acceptance"] = result.acceptance
        handle.attrs["max_unitarity_error"] = result.max_unitarity_error
        handle.attrs["max_det_error"] = result.max_det_error
        measurements = handle.create_group("measurements")
        measurements.create_dataset("sweep", data=sweeps)
        measurements.create_dataset("plaquette", data=plaquettes)
        measurements.create_dataset("acceptance_per_sweep", data=acceptances)
        measurements.create_dataset("wilson_loops", data=wilson_loops)
        measurements["wilson_loops"].attrs["index_convention"] = "wilson_loops[sample, R-1, T-1]"
        checkpoint = handle.create_group("checkpoint")
        checkpoint.create_dataset("links", data=links, compression="gzip")
        checkpoint.attrs["rng_state_json"] = json.dumps(rng.bit_generator.state)


def write_samples_csv(path: Path, wilson_loops: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["sample", "R", "T", "W"])
        writer.writeheader()
        for sample in range(wilson_loops.shape[0]):
            for r_index in range(wilson_loops.shape[1]):
                for t_index in range(wilson_loops.shape[2]):
                    writer.writerow(
                        {
                            "sample": sample,
                            "R": r_index + 1,
                            "T": t_index + 1,
                            "W": f"{wilson_loops[sample, r_index, t_index]:.17g}",
                        }
                    )


def run(cfg: RunConfig) -> RunResult:
    require(cfg.L >= 2, "L must be at least two")
    require(cfg.beta >= 0.0, "beta must be nonnegative")
    require(cfg.proposal_width > 0.0, "proposal width must be positive")
    require(cfg.sweeps > 0, "sweeps must be positive")
    require(0 <= cfg.therm < cfg.sweeps, "therm must satisfy 0 <= therm < sweeps")
    require(cfg.measure_every >= 1, "measure_every must be positive")
    require(cfg.max_r >= 1 and cfg.max_t >= 1, "max_r and max_t must be positive")

    if cfg.resume_from is None:
        rng = np.random.default_rng(cfg.seed)
        links = initial_links(cfg.L, cfg.start, rng)
    else:
        links, rng, _ = load_checkpoint(cfg.resume_from)
        require(links.shape == (cfg.L, cfg.L, cfg.L, cfg.L, DIRECTIONS, COLOR, COLOR), "checkpoint shape does not match L")

    sweeps: list[int] = []
    plaquettes: list[float] = []
    acceptances: list[float] = []
    loop_samples: list[np.ndarray] = []
    attempts_per_sweep = DIRECTIONS * cfg.L**DIRECTIONS
    accepted_total = 0

    for sweep_index in range(cfg.sweeps):
        accepted = metropolis_sweep(links, cfg, rng)
        accepted_total += accepted
        if sweep_index >= cfg.therm and (sweep_index - cfg.therm) % cfg.measure_every == 0:
            sweeps.append(sweep_index)
            plaquettes.append(total_plaquette_score(links) / float(6 * cfg.L**DIRECTIONS))
            acceptances.append(accepted / float(attempts_per_sweep))
            loop_samples.append(rectangular_wilson_loop_grid(links, cfg.max_r, cfg.max_t))

    require(len(loop_samples) >= 1, "run produced no measurements")
    sweep_array = np.array(sweeps, dtype=np.int64)
    plaquette_array = np.array(plaquettes, dtype=float)
    acceptance_array = np.array(acceptances, dtype=float)
    wilson_loop_array = np.stack(loop_samples, axis=0)
    max_unitarity_error, max_det_error = max_group_errors(links)
    stderr = 0.0 if len(plaquette_array) == 1 else float(np.std(plaquette_array, ddof=1) / math.sqrt(len(plaquette_array)))
    result = RunResult(
        L=cfg.L,
        beta=cfg.beta,
        proposal_width=cfg.proposal_width,
        sweeps=cfg.sweeps,
        therm=cfg.therm,
        measure_every=cfg.measure_every,
        seed=cfg.seed,
        acceptance=accepted_total / float(cfg.sweeps * attempts_per_sweep),
        measurement_count=len(loop_samples),
        plaquette_mean=float(np.mean(plaquette_array)),
        plaquette_stderr_naive=stderr,
        max_r=cfg.max_r,
        max_t=cfg.max_t,
        hdf5_output=None if cfg.output_hdf5 is None else str(cfg.output_hdf5),
        samples_csv=None if cfg.samples_csv is None else str(cfg.samples_csv),
        max_unitarity_error=max_unitarity_error,
        max_det_error=max_det_error,
    )
    if cfg.output_hdf5 is not None:
        write_hdf5_output(cfg.output_hdf5, cfg, result, sweep_array, plaquette_array, acceptance_array, wilson_loop_array, links, rng)
    if cfg.samples_csv is not None:
        write_samples_csv(cfg.samples_csv, wilson_loop_array)
    return result


def result_to_json(result: RunResult) -> str:
    return json.dumps(result.__dict__, sort_keys=True)


def run_smoke_test() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        cfg = RunConfig(
            L=2,
            beta=5.4,
            proposal_width=0.35,
            sweeps=5,
            therm=1,
            measure_every=1,
            seed=8675309,
            max_r=1,
            max_t=1,
            samples_csv=Path(tmp) / "su3_samples.csv",
            start="cold",
        )
        result = run(cfg)
        require(0.0 <= result.acceptance <= 1.0, "acceptance is outside [0,1]")
        require(-1.0 <= result.plaquette_mean <= 1.0, "plaquette mean is outside normalized trace range")
        require(result.measurement_count == 4, "unexpected smoke measurement count")
        require(result.max_unitarity_error < 1.0e-10, "unitarity drift is too large in smoke run")
        require(result.max_det_error < 1.0e-10, "determinant drift is too large in smoke run")
        require(cfg.samples_csv is not None and cfg.samples_csv.exists(), "sample CSV was not written")
        print(result_to_json(result))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", type=int, default=3)
    parser.add_argument("--beta", type=float, default=5.5)
    parser.add_argument("--proposal-width", type=float, default=0.32)
    parser.add_argument("--sweeps", type=int, default=24)
    parser.add_argument("--therm", type=int, default=8)
    parser.add_argument("--measure-every", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--max-r", type=int, default=2)
    parser.add_argument("--max-t", type=int, default=3)
    parser.add_argument("--output-hdf5", type=Path)
    parser.add_argument("--samples-csv", type=Path)
    parser.add_argument("--resume-from", type=Path)
    parser.add_argument("--start", choices=["hot", "cold"], default="hot")
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    cfg = RunConfig(
        L=args.L,
        beta=args.beta,
        proposal_width=args.proposal_width,
        sweeps=args.sweeps,
        therm=args.therm,
        measure_every=args.measure_every,
        seed=args.seed,
        max_r=args.max_r,
        max_t=args.max_t,
        output_hdf5=args.output_hdf5,
        samples_csv=args.samples_csv,
        resume_from=args.resume_from,
        start=args.start,
    )
    print(result_to_json(run(cfg)))


if __name__ == "__main__":
    main()
