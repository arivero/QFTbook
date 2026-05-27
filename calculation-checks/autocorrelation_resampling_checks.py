#!/usr/bin/env python3
"""Checks for qft_scripts/autocorrelation_resampling.py."""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "autocorrelation_resampling.py"


def load_module():
    spec = importlib.util.spec_from_file_location("autocorrelation_resampling", SCRIPT)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load autocorrelation_resampling.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    module = load_module()
    values = [float(x) for x in range(8)]
    blocks = module.block_means(values, 2)
    require(blocks == [0.5, 2.5, 4.5, 6.5], "block means failed")
    expected_error = math.sqrt(5.0 / 3.0)
    require(abs(module.blocked_standard_error(values, 2) - expected_error) < 1e-12, "blocked standard error failed")
    require(
        abs(module.delete_one_block_jackknife_error(values, 2) - expected_error) < 1e-12,
        "delete-one-block jackknife error failed",
    )
    cov = module.autocovariances(values, 1)
    require(abs(cov[0] - 5.25) < 1e-12, "lag-zero autocovariance failed")
    require(abs(cov[1] - 105.0 / 32.0) < 1e-12, "lag-one autocovariance failed")
    tau = module.integrated_autocorrelation_time(values, 1)
    require(abs(tau - (0.5 + (105.0 / 32.0) / 5.25)) < 1e-12, "windowed tau_int failed")
    result = module.analyze(values, window=1, block_size=2, bootstrap_samples=16, seed=7)
    require(result["n"] == 8 and result["nblocks"] == 4, "analysis counts failed")
    require(result["block_bootstrap_error"] > 0.0, "bootstrap error should be positive on the test data")
    print("All autocorrelation/resampling checks passed.")


if __name__ == "__main__":
    main()
