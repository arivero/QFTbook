#!/usr/bin/env python3
"""Combine independent job-array Markov-chain summaries.

Input CSV columns:
    chain,estimate,standard_error

Optional column:
    effective_sample_size

The script forms the inverse-variance weighted estimator for a finite set of
declared independent chains, reports the internal standard error
``1/sqrt(sum w_i)``, and exposes the between-chain chi-square diagnostic.  It
is a finite estimator-record utility for cluster runs, not a proof that the
chains have mixed or that the declared errors are reliable.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


@dataclass(frozen=True)
class ChainSummary:
    chain: str
    estimate: float
    standard_error: float
    effective_sample_size: float | None = None


def read_chain_summaries(path: Path) -> list[ChainSummary]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, "input CSV must have a header")
        required = {"chain", "estimate", "standard_error"}
        missing = required.difference(reader.fieldnames)
        require(not missing, f"input CSV missing columns: {sorted(missing)}")
        has_neff = "effective_sample_size" in reader.fieldnames
        rows: list[ChainSummary] = []
        for row in reader:
            neff = None
            if has_neff and row.get("effective_sample_size", "") != "":
                neff = float(row["effective_sample_size"])
            rows.append(
                ChainSummary(
                    chain=row["chain"],
                    estimate=float(row["estimate"]),
                    standard_error=float(row["standard_error"]),
                    effective_sample_size=neff,
                )
            )
    return rows


def summarize_chains(rows: list[ChainSummary]) -> dict[str, float | int | list[str]]:
    require(len(rows) >= 1, "at least one chain summary is required")
    for row in rows:
        require(row.standard_error > 0.0, "standard errors must be positive")
        if row.effective_sample_size is not None:
            require(row.effective_sample_size > 0.0, "effective sample sizes must be positive")

    weights = [1.0 / (row.standard_error * row.standard_error) for row in rows]
    weight_sum = sum(weights)
    weighted_mean = sum(w * row.estimate for w, row in zip(weights, rows)) / weight_sum
    internal_se = math.sqrt(1.0 / weight_sum)

    chi2 = sum(
        w * (row.estimate - weighted_mean) * (row.estimate - weighted_mean)
        for w, row in zip(weights, rows)
    )
    dof = len(rows) - 1
    reduced_chi2 = chi2 / dof if dof > 0 else 0.0
    scale_factor = max(1.0, math.sqrt(reduced_chi2)) if dof > 0 else 1.0
    inflated_se = internal_se * scale_factor
    max_pull = max(abs(row.estimate - weighted_mean) / row.standard_error for row in rows)

    total_neff = sum(
        row.effective_sample_size for row in rows if row.effective_sample_size is not None
    )
    neff_count = sum(1 for row in rows if row.effective_sample_size is not None)

    return {
        "chains": [row.chain for row in rows],
        "nchains": len(rows),
        "weighted_mean": weighted_mean,
        "internal_standard_error": internal_se,
        "between_chain_chi2": chi2,
        "between_chain_dof": dof,
        "between_chain_reduced_chi2": reduced_chi2,
        "error_inflation_factor": scale_factor,
        "inflated_standard_error": inflated_se,
        "max_standardized_pull": max_pull,
        "total_effective_sample_size": total_neff if neff_count else 0.0,
        "chains_with_effective_sample_size": neff_count,
    }


def run_smoke_test() -> None:
    rows = [
        ChainSummary("beta5.7_seed11", 1.0, 0.5, 100.0),
        ChainSummary("beta5.7_seed13", 2.0, 1.0, 40.0),
        ChainSummary("beta5.7_seed17", -0.5, 1.0, 60.0),
    ]
    result = summarize_chains(rows)
    require(abs(result["weighted_mean"] - 11.0 / 12.0) < 1e-12, "weighted mean smoke check failed")
    require(abs(result["between_chain_chi2"] - 77.0 / 24.0) < 1e-12, "chi-square smoke check failed")
    require(result["chains_with_effective_sample_size"] == 3, "effective-sample count smoke check failed")
    print(json.dumps(result, sort_keys=True))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="CSV file containing per-chain summaries")
    parser.add_argument("--smoke", action="store_true", help="run deterministic smoke test")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    require(args.input is not None, "--input is required outside --smoke")
    print(json.dumps(summarize_chains(read_chain_summaries(args.input)), sort_keys=True))


if __name__ == "__main__":
    main()
