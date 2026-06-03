#!/usr/bin/env python3
"""Checks for qft_scripts/cluster/chain_ensemble_summary.py."""

from __future__ import annotations

import importlib.util
import math
import sys
import tempfile
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "cluster" / "chain_ensemble_summary.py"


def load_module():
    spec = importlib.util.spec_from_file_location("chain_ensemble_summary", SCRIPT)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load chain_ensemble_summary.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    module = load_module()
    rows = [
        module.ChainSummary("c0", 1.0, 0.5, 100.0),
        module.ChainSummary("c1", 2.0, 1.0, 40.0),
        module.ChainSummary("c2", -0.5, 1.0, 60.0),
    ]
    result = module.summarize_chains(rows)

    estimates = [Fraction(1), Fraction(2), Fraction(-1, 2)]
    errors = [Fraction(1, 2), Fraction(1), Fraction(1)]
    weights = [1 / (err * err) for err in errors]
    weight_sum = sum(weights)
    mean = sum(w * x for w, x in zip(weights, estimates)) / weight_sum
    chi2 = sum(w * (x - mean) * (x - mean) for w, x in zip(weights, estimates))
    internal_variance = 1 / weight_sum
    reduced_chi2 = chi2 / 2
    inflated_variance = internal_variance * reduced_chi2

    require(mean == Fraction(11, 12), "exact weighted mean changed")
    require(chi2 == Fraction(77, 24), "exact between-chain chi-square changed")
    require(abs(result["weighted_mean"] - float(mean)) < 1e-12, "weighted mean mismatch")
    require(abs(result["between_chain_chi2"] - float(chi2)) < 1e-12, "chi-square mismatch")
    require(
        abs(result["internal_standard_error"] - math.sqrt(float(internal_variance))) < 1e-12,
        "internal standard error mismatch",
    )
    require(
        abs(result["inflated_standard_error"] - math.sqrt(float(inflated_variance))) < 1e-12,
        "inflated standard error mismatch",
    )
    require(result["total_effective_sample_size"] == 200.0, "effective sample size sum mismatch")

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "chains.csv"
        path.write_text(
            "chain,estimate,standard_error,effective_sample_size\n"
            "c0,1,0.5,100\n"
            "c1,2,1,40\n"
            "c2,-0.5,1,60\n",
            encoding="utf-8",
        )
        from_csv = module.summarize_chains(module.read_chain_summaries(path))
    require(abs(from_csv["weighted_mean"] - float(mean)) < 1e-12, "CSV round trip failed")
    print("All cluster chain-ensemble checks passed.")


if __name__ == "__main__":
    main()
