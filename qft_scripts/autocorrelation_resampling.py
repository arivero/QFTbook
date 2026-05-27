#!/usr/bin/env python3
"""Autocorrelation, blocking, jackknife, and bootstrap diagnostics.

The theorem anchors are Volume XI, Chapter 6: the finite-N autocorrelation
variance identity and the delete-one-block jackknife identity for the mean.

Input CSV columns:
    value

Optional command-line flags select the column name, autocorrelation window,
block size, and bootstrap count.  Output is JSON so downstream scripts can
consume the result without parsing prose.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from statistics import fmean


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_series(path: Path, column: str) -> list[float]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, "input CSV must have a header")
        require(column in reader.fieldnames, f"input CSV must contain column {column!r}")
        values = [float(row[column]) for row in reader]
    require(len(values) >= 2, "time series must contain at least two values")
    return values


def mean(values: list[float]) -> float:
    return fmean(values)


def autocovariances(values: list[float], max_lag: int) -> list[float]:
    n = len(values)
    require(0 <= max_lag < n, "max_lag must lie between 0 and len(values)-1")
    m = mean(values)
    return [
        sum((values[i] - m) * (values[i + lag] - m) for i in range(n - lag)) / n
        for lag in range(max_lag + 1)
    ]


def integrated_autocorrelation_time(values: list[float], window: int) -> float:
    cov = autocovariances(values, window)
    require(cov[0] > 0.0, "integrated autocorrelation requires nonzero sample variance")
    return 0.5 + sum(c / cov[0] for c in cov[1:])


def block_means(values: list[float], block_size: int) -> list[float]:
    require(block_size >= 1, "block_size must be positive")
    nblocks = len(values) // block_size
    require(nblocks >= 2, "need at least two complete blocks")
    return [
        mean(values[j * block_size : (j + 1) * block_size])
        for j in range(nblocks)
    ]


def sample_variance(values: list[float]) -> float:
    require(len(values) >= 2, "sample variance needs at least two values")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (len(values) - 1)


def blocked_standard_error(values: list[float], block_size: int) -> float:
    blocks = block_means(values, block_size)
    return math.sqrt(sample_variance(blocks) / len(blocks))


def delete_one_block_jackknife_error(values: list[float], block_size: int) -> float:
    blocks = block_means(values, block_size)
    nblocks = len(blocks)
    total = sum(blocks)
    delete_estimates = [(total - blocks[j]) / (nblocks - 1) for j in range(nblocks)]
    theta_bar = mean(delete_estimates)
    variance = (nblocks - 1) / nblocks * sum((theta - theta_bar) ** 2 for theta in delete_estimates)
    return math.sqrt(variance)


def lcg(seed: int):
    state = seed % (2**64)
    while True:
        state = (6364136223846793005 * state + 1442695040888963407) % (2**64)
        yield state


def block_bootstrap_error(values: list[float], block_size: int, samples: int, seed: int) -> float:
    require(samples >= 2, "bootstrap sample count must be at least two")
    blocks = block_means(values, block_size)
    nblocks = len(blocks)
    rng = lcg(seed)
    estimates: list[float] = []
    for _ in range(samples):
        total = 0.0
        for _ in range(nblocks):
            total += blocks[(next(rng) >> 32) % nblocks]
        estimates.append(total / nblocks)
    return math.sqrt(sample_variance(estimates))


def analyze(values: list[float], window: int, block_size: int, bootstrap_samples: int, seed: int) -> dict[str, float | int]:
    require(0 <= window < len(values), "window must lie between 0 and len(values)-1")
    tau = integrated_autocorrelation_time(values, window)
    blocks = block_means(values, block_size)
    block_error = blocked_standard_error(values, block_size)
    jackknife_error = delete_one_block_jackknife_error(values, block_size)
    bootstrap_error = block_bootstrap_error(values, block_size, bootstrap_samples, seed)
    return {
        "n": len(values),
        "mean": mean(values),
        "window": window,
        "tau_int_windowed": tau,
        "effective_sample_size_windowed": len(values) / (2.0 * tau) if tau > 0 else math.nan,
        "block_size": block_size,
        "nblocks": len(blocks),
        "blocked_standard_error": block_error,
        "delete_one_block_jackknife_error": jackknife_error,
        "block_bootstrap_error": bootstrap_error,
        "bootstrap_samples": bootstrap_samples,
        "seed": seed,
    }


def run_smoke_test() -> None:
    values = [float(x) for x in range(8)]
    result = analyze(values, window=1, block_size=2, bootstrap_samples=32, seed=12345)
    require(abs(result["mean"] - 3.5) < 1e-12, "mean smoke check failed")
    expected_error = math.sqrt(5.0 / 3.0)
    require(abs(result["blocked_standard_error"] - expected_error) < 1e-12, "blocked error smoke check failed")
    require(
        abs(result["delete_one_block_jackknife_error"] - expected_error) < 1e-12,
        "jackknife error smoke check failed",
    )
    require(result["nblocks"] == 4, "block count smoke check failed")
    print(json.dumps(result, sort_keys=True))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="CSV file containing the time series")
    parser.add_argument("--column", default="value", help="CSV column to analyze")
    parser.add_argument("--window", type=int, default=5, help="autocorrelation window")
    parser.add_argument("--block-size", type=int, default=8)
    parser.add_argument("--bootstrap-samples", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260527)
    parser.add_argument("--smoke", action="store_true", help="run deterministic smoke test")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    require(args.input is not None, "--input is required outside --smoke")
    values = read_series(args.input, args.column)
    print(json.dumps(analyze(values, args.window, args.block_size, args.bootstrap_samples, args.seed), sort_keys=True))


if __name__ == "__main__":
    main()
