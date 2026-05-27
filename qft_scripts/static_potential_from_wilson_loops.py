#!/usr/bin/env python3
"""Extract static-potential diagnostics from rectangular Wilson-loop data.

The theorem anchor is Volume XI, Chapter 5,
Proposition ``Spectral extraction of the finite-lattice static energy'' and
the Creutz-ratio definition in the same chapter.  The script is deliberately
finite-regulator: it reads positive Wilson-loop estimates W(R,T), computes
effective-mass ratios in the Euclidean-time direction, and computes Creutz
ratios when the required neighboring rectangles are present.

Aggregate-input CSV columns:
    R,T,W[,dW]

Sample-input CSV columns:
    sample,R,T,W

Aggregate-output CSV columns:
    observable,R,T,value,error

Sample-output CSV columns:
    observable,R,T,value,jackknife_error,bootstrap_error

Here R and T are integer lattice extents.  The optional error column dW is
treated as an independent standard error for elementary propagation only; a
serious Monte Carlo analysis must use the sample-level mode, which recomputes
nonlinear effective-mass and Creutz-ratio functions on each deleted or
resampled block and therefore keeps correlations among Wilson loops.
"""

from __future__ import annotations

import argparse
import csv
import io
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class WilsonLoopDatum:
    r: int
    t: int
    value: float
    error: float | None = None


@dataclass(frozen=True)
class WilsonLoopSampleDatum:
    sample: int
    r: int
    t: int
    value: float


@dataclass(frozen=True)
class ObservableDatum:
    observable: str
    r: int
    t: int
    value: float
    error: float | None = None


@dataclass(frozen=True)
class ResampledObservableDatum:
    observable: str
    r: int
    t: int
    value: float
    jackknife_error: float | None = None
    bootstrap_error: float | None = None


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_wilson_loop_csv(path: Path) -> list[WilsonLoopDatum]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, "input CSV must have a header")
        required = {"R", "T", "W"}
        require(required.issubset(set(reader.fieldnames)), "input CSV columns must include R,T,W")
        data: list[WilsonLoopDatum] = []
        for row in reader:
            r = int(row["R"])
            t = int(row["T"])
            value = float(row["W"])
            error_text = row.get("dW", "")
            error = float(error_text) if error_text not in ("", None) else None
            require(r >= 0 and t >= 0, "R and T must be nonnegative")
            require(value > 0.0, "Wilson-loop values used in logarithms must be positive")
            if error is not None:
                require(error >= 0.0, "dW must be nonnegative")
            data.append(WilsonLoopDatum(r, t, value, error))
    return data


def read_wilson_loop_sample_csv(path: Path) -> list[WilsonLoopSampleDatum]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, "input CSV must have a header")
        required = {"sample", "R", "T", "W"}
        require(required.issubset(set(reader.fieldnames)), "sample CSV columns must include sample,R,T,W")
        data: list[WilsonLoopSampleDatum] = []
        for row in reader:
            sample = int(row["sample"])
            r = int(row["R"])
            t = int(row["T"])
            value = float(row["W"])
            require(sample >= 0, "sample labels must be nonnegative integers")
            require(r >= 0 and t >= 0, "R and T must be nonnegative")
            require(value > 0.0, "Wilson-loop values used in logarithms must be positive")
            data.append(WilsonLoopSampleDatum(sample, r, t, value))
    return data


def import_h5py():
    try:
        import h5py  # type: ignore
    except ImportError as exc:
        raise RuntimeError("HDF5 input requires h5py; install h5py or use CSV input") from exc
    return h5py


def wilson_loop_grid_to_sample_data(wilson_loop_grid: Any) -> list[WilsonLoopSampleDatum]:
    """Convert a sampler Wilson-loop array into correlated sample data.

    The finite SU(3) sampler writes an array with index convention
    ``wilson_loops[sample, R-1, T-1]``.  The sample labels used here are the
    consecutive row labels of that array, not the Monte Carlo sweep numbers.
    This is the right coordinate for blocking because the block construction
    acts on the ordered measurement stream.
    """

    try:
        shape = tuple(wilson_loop_grid.shape)
    except AttributeError as exc:
        raise ValueError("Wilson-loop grid must have a shape attribute") from exc
    require(len(shape) == 3, "HDF5 Wilson-loop dataset must have shape (sample, R, T)")
    nsamples, max_r, max_t = shape
    require(nsamples >= 1, "HDF5 Wilson-loop dataset must contain at least one sample")
    require(max_r >= 1 and max_t >= 1, "HDF5 Wilson-loop dataset must contain at least one rectangle")
    data: list[WilsonLoopSampleDatum] = []
    for sample in range(nsamples):
        for r_index in range(max_r):
            for t_index in range(max_t):
                value = float(wilson_loop_grid[sample, r_index, t_index])
                require(value > 0.0, "Wilson-loop values used in logarithms must be positive")
                data.append(WilsonLoopSampleDatum(sample, r_index + 1, t_index + 1, value))
    return data


def read_wilson_loop_sample_hdf5(
    path: Path,
    dataset: str = "measurements/wilson_loops",
) -> list[WilsonLoopSampleDatum]:
    h5py = import_h5py()
    with h5py.File(path, "r") as handle:
        require(dataset in handle, f"HDF5 dataset {dataset!r} not found")
        return wilson_loop_grid_to_sample_data(handle[dataset][...])


def index_data(data: list[WilsonLoopDatum]) -> dict[tuple[int, int], WilsonLoopDatum]:
    indexed: dict[tuple[int, int], WilsonLoopDatum] = {}
    for datum in data:
        key = (datum.r, datum.t)
        require(key not in indexed, f"duplicate Wilson-loop datum for R={datum.r}, T={datum.t}")
        indexed[key] = datum
    return indexed


def index_sample_data(data: list[WilsonLoopSampleDatum]) -> dict[int, dict[tuple[int, int], float]]:
    indexed: dict[int, dict[tuple[int, int], float]] = {}
    for datum in data:
        by_rectangle = indexed.setdefault(datum.sample, {})
        key = (datum.r, datum.t)
        require(key not in by_rectangle, f"duplicate Wilson-loop datum for sample={datum.sample}, R={datum.r}, T={datum.t}")
        by_rectangle[key] = datum.value
    require(len(indexed) >= 2, "sample-level analysis needs at least two samples")
    reference_keys = next(iter(indexed.values())).keys()
    reference_set = set(reference_keys)
    require(len(reference_set) > 0, "sample-level analysis needs at least one rectangle")
    for sample, by_rectangle in indexed.items():
        require(set(by_rectangle.keys()) == reference_set, f"sample {sample} does not have the common rectangle set")
    return indexed


def ratio_error(numerator: WilsonLoopDatum, denominator: WilsonLoopDatum, scale: float) -> float | None:
    if numerator.error is None or denominator.error is None:
        return None
    return scale * math.sqrt((numerator.error / numerator.value) ** 2 + (denominator.error / denominator.value) ** 2)


def effective_masses(data: list[WilsonLoopDatum], lattice_spacing: float) -> list[ObservableDatum]:
    require(lattice_spacing > 0.0, "lattice spacing must be positive")
    indexed = index_data(data)
    output: list[ObservableDatum] = []
    for (r, t), datum in sorted(indexed.items()):
        next_datum = indexed.get((r, t + 1))
        if next_datum is None:
            continue
        value = -math.log(next_datum.value / datum.value) / lattice_spacing
        error = ratio_error(next_datum, datum, 1.0 / lattice_spacing)
        output.append(ObservableDatum("effective_mass", r, t, value, error))
    return output


def creutz_ratios(data: list[WilsonLoopDatum]) -> list[ObservableDatum]:
    indexed = index_data(data)
    output: list[ObservableDatum] = []
    for (r, t), datum in sorted(indexed.items()):
        if r <= 0 or t <= 0:
            continue
        left = indexed.get((r - 1, t - 1))
        down = indexed.get((r, t - 1))
        back = indexed.get((r - 1, t))
        if left is None or down is None or back is None:
            continue
        ratio = datum.value * left.value / (down.value * back.value)
        require(ratio > 0.0, "Creutz-ratio logarithm requires positive ratio")
        value = -math.log(ratio)
        error = None
        if all(x.error is not None for x in (datum, left, down, back)):
            error = math.sqrt(
                (datum.error / datum.value) ** 2
                + (left.error / left.value) ** 2
                + (down.error / down.value) ** 2
                + (back.error / back.value) ** 2
            )
        output.append(ObservableDatum("creutz_ratio", r, t, value, error))
    return output


def observable_key(datum: ObservableDatum) -> tuple[str, int, int]:
    return (datum.observable, datum.r, datum.t)


def observable_map(data: list[ObservableDatum]) -> dict[tuple[str, int, int], float]:
    return {observable_key(datum): datum.value for datum in data}


def mean_wilson_loop_data(
    indexed: dict[int, dict[tuple[int, int], float]],
    sample_ids: list[int],
) -> list[WilsonLoopDatum]:
    require(len(sample_ids) >= 1, "mean Wilson-loop data need at least one sample")
    rectangles = sorted(next(iter(indexed.values())).keys())
    count = float(len(sample_ids))
    output: list[WilsonLoopDatum] = []
    for r, t in rectangles:
        value = sum(indexed[sample][(r, t)] for sample in sample_ids) / count
        require(value > 0.0, "mean Wilson-loop values used in logarithms must be positive")
        output.append(WilsonLoopDatum(r, t, value))
    return output


def observables_from_sample_ids(
    indexed: dict[int, dict[tuple[int, int], float]],
    sample_ids: list[int],
    lattice_spacing: float,
    include_effective_mass: bool,
    include_creutz: bool,
) -> dict[tuple[str, int, int], float]:
    averaged = mean_wilson_loop_data(indexed, sample_ids)
    output: list[ObservableDatum] = []
    if include_effective_mass:
        output.extend(effective_masses(averaged, lattice_spacing))
    if include_creutz:
        output.extend(creutz_ratios(averaged))
    return observable_map(output)


def consecutive_blocks(sample_ids: list[int], block_size: int) -> list[list[int]]:
    require(block_size >= 1, "block_size must be positive")
    sorted_ids = sorted(sample_ids)
    nblocks = len(sorted_ids) // block_size
    require(nblocks >= 2, "need at least two complete blocks")
    return [sorted_ids[j * block_size : (j + 1) * block_size] for j in range(nblocks)]


def sample_variance(values: list[float]) -> float:
    require(len(values) >= 2, "sample variance needs at least two values")
    average = sum(values) / len(values)
    return sum((value - average) ** 2 for value in values) / (len(values) - 1)


def lcg(seed: int):
    state = seed % (2**64)
    while True:
        state = (6364136223846793005 * state + 1442695040888963407) % (2**64)
        yield state


def resampled_static_observables(
    data: list[WilsonLoopSampleDatum],
    lattice_spacing: float,
    block_size: int,
    bootstrap_samples: int,
    seed: int,
    include_effective_mass: bool = True,
    include_creutz: bool = True,
) -> list[ResampledObservableDatum]:
    require(bootstrap_samples >= 0, "bootstrap sample count must be nonnegative")
    indexed = index_sample_data(data)
    blocks = consecutive_blocks(list(indexed.keys()), block_size)
    complete_sample_ids = [sample for block in blocks for sample in block]
    central = observables_from_sample_ids(
        indexed,
        complete_sample_ids,
        lattice_spacing,
        include_effective_mass,
        include_creutz,
    )
    require(len(central) > 0, "no static-potential observables could be formed")
    nblocks = len(blocks)
    delete_estimates: list[dict[tuple[str, int, int], float]] = []
    complete_set = set(complete_sample_ids)
    for block in blocks:
        keep = sorted(complete_set.difference(block))
        delete_estimates.append(
            observables_from_sample_ids(indexed, keep, lattice_spacing, include_effective_mass, include_creutz)
        )

    jackknife_errors: dict[tuple[str, int, int], float] = {}
    for key in central:
        estimates = [estimate[key] for estimate in delete_estimates]
        theta_bar = sum(estimates) / nblocks
        variance = (nblocks - 1) / nblocks * sum((theta - theta_bar) ** 2 for theta in estimates)
        jackknife_errors[key] = math.sqrt(variance)

    bootstrap_errors: dict[tuple[str, int, int], float] = {}
    if bootstrap_samples >= 2:
        rng = lcg(seed)
        bootstrap_values: dict[tuple[str, int, int], list[float]] = {key: [] for key in central}
        for _ in range(bootstrap_samples):
            resampled_ids: list[int] = []
            for _ in range(nblocks):
                resampled_ids.extend(blocks[(next(rng) >> 32) % nblocks])
            estimate = observables_from_sample_ids(
                indexed,
                resampled_ids,
                lattice_spacing,
                include_effective_mass,
                include_creutz,
            )
            for key in central:
                bootstrap_values[key].append(estimate[key])
        bootstrap_errors = {
            key: math.sqrt(sample_variance(values))
            for key, values in bootstrap_values.items()
        }

    output: list[ResampledObservableDatum] = []
    for observable, r, t in sorted(central):
        key = (observable, r, t)
        output.append(
            ResampledObservableDatum(
                observable,
                r,
                t,
                central[key],
                jackknife_errors.get(key),
                bootstrap_errors.get(key),
            )
        )
    return output


def write_observables(path: Path, data: list[ObservableDatum]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["observable", "R", "T", "value", "error"])
        writer.writeheader()
        for datum in data:
            writer.writerow(
                {
                    "observable": datum.observable,
                    "R": datum.r,
                    "T": datum.t,
                    "value": f"{datum.value:.17g}",
                    "error": "" if datum.error is None else f"{datum.error:.17g}",
                }
            )


def write_resampled_observables(path: Path, data: list[ResampledObservableDatum]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["observable", "R", "T", "value", "jackknife_error", "bootstrap_error"])
        writer.writeheader()
        for datum in data:
            writer.writerow(
                {
                    "observable": datum.observable,
                    "R": datum.r,
                    "T": datum.t,
                    "value": f"{datum.value:.17g}",
                    "jackknife_error": "" if datum.jackknife_error is None else f"{datum.jackknife_error:.17g}",
                    "bootstrap_error": "" if datum.bootstrap_error is None else f"{datum.bootstrap_error:.17g}",
                }
            )


def synthetic_area_perimeter_data(sigma: float, mu: float, constant: float, max_r: int, max_t: int) -> list[WilsonLoopDatum]:
    data: list[WilsonLoopDatum] = []
    for r in range(max_r + 1):
        for t in range(max_t + 1):
            exponent = sigma * r * t + mu * (r + t) + constant
            data.append(WilsonLoopDatum(r, t, math.exp(-exponent)))
    return data


def synthetic_area_perimeter_sample_data(
    sigmas: list[float],
    mu: float,
    constant: float,
    max_r: int,
    max_t: int,
) -> list[WilsonLoopSampleDatum]:
    data: list[WilsonLoopSampleDatum] = []
    for sample, sigma in enumerate(sigmas):
        for r in range(max_r + 1):
            for t in range(max_t + 1):
                exponent = sigma * r * t + mu * (r + t) + constant
                data.append(WilsonLoopSampleDatum(sample, r, t, math.exp(-exponent)))
    return data


def run_smoke_test() -> None:
    sigma = 0.37
    mu = 0.19
    constant = 0.11
    data = synthetic_area_perimeter_data(sigma, mu, constant, max_r=4, max_t=5)
    eff = effective_masses(data, lattice_spacing=1.0)
    creutz = creutz_ratios(data)
    for datum in eff:
        expected = sigma * datum.r + mu
        require(abs(datum.value - expected) < 1e-12, "synthetic effective mass mismatch")
    for datum in creutz:
        require(abs(datum.value - sigma) < 1e-12, "synthetic Creutz ratio mismatch")

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=["observable", "R", "T", "value", "error"])
    writer.writeheader()
    for datum in eff[:2] + creutz[:2]:
        writer.writerow(
            {
                "observable": datum.observable,
                "R": datum.r,
                "T": datum.t,
                "value": f"{datum.value:.17g}",
                "error": "",
            }
        )
    require("effective_mass" in buffer.getvalue(), "smoke CSV output should contain effective masses")
    samples = synthetic_area_perimeter_sample_data([0.29, 0.31, 0.36, 0.42], mu, constant, max_r=3, max_t=4)
    resampled = resampled_static_observables(samples, lattice_spacing=1.0, block_size=1, bootstrap_samples=16, seed=2026)
    require(any(datum.jackknife_error is not None and datum.jackknife_error > 0.0 for datum in resampled), "resampled smoke check should have a positive jackknife error")
    print("static_potential_from_wilson_loops.py smoke test passed.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="CSV file with columns R,T,W[,dW]")
    parser.add_argument("--samples-input", type=Path, help="CSV file with columns sample,R,T,W")
    parser.add_argument("--samples-hdf5", type=Path, help="HDF5 file with measurements/wilson_loops[sample,R-1,T-1]")
    parser.add_argument("--hdf5-dataset", default="measurements/wilson_loops", help="Wilson-loop dataset inside --samples-hdf5")
    parser.add_argument("--output", type=Path, help="output CSV for extracted observables")
    parser.add_argument("--lattice-spacing", type=float, default=1.0)
    parser.add_argument("--block-size", type=int, default=4)
    parser.add_argument("--bootstrap-samples", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--no-effective-mass", action="store_true")
    parser.add_argument("--no-creutz", action="store_true")
    parser.add_argument("--smoke", action="store_true", help="run the built-in synthetic-data smoke test")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    require(args.output is not None, "--output is required outside --smoke")
    input_count = sum(
        value is not None
        for value in (args.input, args.samples_input, args.samples_hdf5)
    )
    require(input_count == 1, "choose exactly one of --input, --samples-input, and --samples-hdf5")
    if not args.no_effective_mass:
        include_effective_mass = True
    else:
        include_effective_mass = False
    include_creutz = not args.no_creutz
    if args.input is not None:
        data = read_wilson_loop_csv(args.input)
        output: list[ObservableDatum] = []
        if include_effective_mass:
            output.extend(effective_masses(data, args.lattice_spacing))
        if include_creutz:
            output.extend(creutz_ratios(data))
        write_observables(args.output, output)
        return
    if args.samples_input is not None:
        sample_data = read_wilson_loop_sample_csv(args.samples_input)
    else:
        sample_data = read_wilson_loop_sample_hdf5(args.samples_hdf5, args.hdf5_dataset)
    resampled = resampled_static_observables(
        sample_data,
        args.lattice_spacing,
        args.block_size,
        args.bootstrap_samples,
        args.seed,
        include_effective_mass,
        include_creutz,
    )
    write_resampled_observables(args.output, resampled)


if __name__ == "__main__":
    main()
