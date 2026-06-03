#!/usr/bin/env python3
"""Correlated finite-regulator extrapolation diagnostics.

The script implements the finite linear algebra described in the monograph's
finite-regulator and scaling-window chapters.  It fits finite data to

    A_K = c_0 + c_1 K^{-omega} + ... + c_p K^{-p omega}

on one or more fit windows, propagates a declared covariance matrix, and
reports the deterministic systematic coordinate obtained from declared
remainder envelopes together with a finite evidence-budget summary.  The
output is a finite-regulator diagnostic.  It is not a proof that a QFT
observable has the chosen cutoff expansion.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class DataSet:
    regulators: np.ndarray
    values: np.ndarray
    covariance: np.ndarray
    remainder_envelopes: np.ndarray
    covariance_source: str


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def design_matrix(regulators: Sequence[float], fit_order: int, base_exponent: float) -> np.ndarray:
    require(fit_order >= 0, "fit_order must be nonnegative")
    require(base_exponent > 0.0, "base_exponent must be positive")
    k = np.asarray(regulators, dtype=float)
    require(k.ndim == 1 and k.size >= fit_order + 1, "need at least fit_order + 1 regulators")
    require(bool(np.all(k > 0.0)), "all regulators must be positive")
    q = k ** (-base_exponent)
    powers = np.arange(fit_order + 1, dtype=float)
    matrix = q[:, np.newaxis] ** powers[np.newaxis, :]
    rank = int(np.linalg.matrix_rank(matrix))
    require(rank == fit_order + 1, "fit design matrix is rank deficient")
    return matrix


def positive_definite_inverse(covariance: np.ndarray) -> np.ndarray:
    covariance = np.asarray(covariance, dtype=float)
    require(covariance.ndim == 2, "covariance must be a matrix")
    require(covariance.shape[0] == covariance.shape[1], "covariance must be square")
    require(float(np.max(np.abs(covariance - covariance.T))) <= 1.0e-10, "covariance must be symmetric")
    eigenvalues = np.linalg.eigvalsh(covariance)
    require(float(eigenvalues[0]) > 0.0, "covariance must be positive definite")
    return np.linalg.inv(covariance)


def fit_window(
    regulators: Sequence[float],
    values: Sequence[float],
    covariance: np.ndarray,
    remainder_envelopes: Sequence[float],
    fit_order: int,
    base_exponent: float,
) -> dict[str, object]:
    regulators_array = np.asarray(regulators, dtype=float)
    values_array = np.asarray(values, dtype=float)
    remainders = np.asarray(remainder_envelopes, dtype=float)
    require(values_array.shape == regulators_array.shape, "values and regulators must have the same shape")
    require(remainders.shape == regulators_array.shape, "remainder envelopes and regulators must have the same shape")
    require(bool(np.all(remainders >= 0.0)), "remainder envelopes must be nonnegative")

    design = design_matrix(regulators_array, fit_order, base_exponent)
    inverse_covariance = positive_definite_inverse(covariance)
    gram = design.T @ inverse_covariance @ design
    gram_eigs = np.linalg.eigvalsh(gram)
    require(float(gram_eigs[0]) > 0.0, "weighted Gram matrix is not positive definite")
    gram_inverse = np.linalg.inv(gram)
    propagator = gram_inverse @ design.T @ inverse_covariance
    coefficients = propagator @ values_array
    fitted = design @ coefficients
    residual = values_array - fitted
    intercept_weights = propagator[0, :]
    coefficient_covariance = propagator @ covariance @ propagator.T
    intercept_variance = float(coefficient_covariance[0, 0])
    systematic_bound = float(np.sum(np.abs(intercept_weights) * remainders))
    chi_square = float(residual @ inverse_covariance @ residual)
    dof = int(values_array.size - (fit_order + 1))
    return {
        "regulators": [float(x) for x in regulators_array],
        "fit_order": int(fit_order),
        "base_exponent": float(base_exponent),
        "coefficients": [float(x) for x in coefficients],
        "intercept": float(coefficients[0]),
        "intercept_stat_error": float(np.sqrt(max(intercept_variance, 0.0))),
        "intercept_systematic_bound": systematic_bound,
        "intercept_weights": [float(x) for x in intercept_weights],
        "chi_square": chi_square,
        "degrees_of_freedom": dof,
        "chi_square_per_dof": None if dof <= 0 else float(chi_square / dof),
        "condition_number": float(np.linalg.cond(gram)),
        "fitted_values": [float(x) for x in fitted],
        "residuals": [float(x) for x in residual],
    }


def parse_windows(text: str, size: int) -> list[tuple[int, int]]:
    if not text.strip():
        return [(0, size)]
    windows: list[tuple[int, int]] = []
    for piece in text.replace(";", ",").split(","):
        item = piece.strip()
        if not item:
            continue
        if ":" not in item:
            raise ValueError("window entries must have the half-open form start:end")
        start_text, end_text = item.split(":", 1)
        start = int(start_text)
        end = int(end_text)
        require(0 <= start < end <= size, f"invalid window {item!r} for {size} data points")
        windows.append((start, end))
    require(bool(windows), "at least one nonempty window must be supplied")
    return windows


def load_covariance(path: Path) -> np.ndarray:
    rows: list[list[float]] = []
    with path.open(newline="") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if not row:
                continue
            rows.append([float(entry) for entry in row])
    require(bool(rows), "covariance CSV is empty")
    matrix = np.array(rows, dtype=float)
    require(matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1], "covariance CSV must be square")
    return matrix


def load_dataset(data_csv: Path, covariance_csv: Path | None) -> DataSet:
    regulators: list[float] = []
    values: list[float] = []
    errors: list[float] = []
    remainders: list[float] = []
    with data_csv.open(newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, "data CSV must have a header")
        require("regulator" in reader.fieldnames and "value" in reader.fieldnames, "data CSV needs regulator,value columns")
        for row in reader:
            regulators.append(float(row["regulator"]))
            values.append(float(row["value"]))
            errors.append(float(row.get("error") or 0.0))
            remainders.append(float(row.get("remainder") or 0.0))
    require(bool(regulators), "data CSV has no rows")
    require(regulators == sorted(regulators), "regulators must be sorted increasingly in the CSV")
    if covariance_csv is not None:
        covariance = load_covariance(covariance_csv)
        require(covariance.shape == (len(regulators), len(regulators)), "covariance size does not match data rows")
        source = str(covariance_csv)
    else:
        if any(error > 0.0 for error in errors):
            require(all(error > 0.0 for error in errors), "either every error must be positive or none may be supplied")
            covariance = np.diag(np.array(errors, dtype=float) ** 2)
            source = "diagonal errors from data CSV"
        else:
            covariance = np.eye(len(regulators), dtype=float)
            source = "identity diagnostic covariance"
    return DataSet(
        regulators=np.array(regulators, dtype=float),
        values=np.array(values, dtype=float),
        covariance=np.array(covariance, dtype=float),
        remainder_envelopes=np.array(remainders, dtype=float),
        covariance_source=source,
    )


def smoke_dataset() -> DataSet:
    regulators = np.array([8.0, 10.0, 12.0, 16.0, 20.0, 28.0], dtype=float)
    q = 1.0 / regulators
    coefficients = np.array([1.75, -0.8, 0.35], dtype=float)
    design = np.column_stack([np.ones_like(q), q, q * q])
    deterministic_remainder = np.array([0.0035, -0.0020, 0.0013, -0.0007, 0.0004, -0.0002], dtype=float)
    finite_fluctuation = np.array([0.006, -0.004, 0.003, -0.0015, 0.0008, -0.0004], dtype=float)
    covariance = np.array(
        [
            [0.025, 0.010, 0.006, 0.003, 0.002, 0.001],
            [0.010, 0.022, 0.008, 0.004, 0.002, 0.001],
            [0.006, 0.008, 0.020, 0.006, 0.003, 0.001],
            [0.003, 0.004, 0.006, 0.018, 0.005, 0.002],
            [0.002, 0.002, 0.003, 0.005, 0.016, 0.004],
            [0.001, 0.001, 0.001, 0.002, 0.004, 0.014],
        ],
        dtype=float,
    )
    values = design @ coefficients + deterministic_remainder + finite_fluctuation
    return DataSet(
        regulators=regulators,
        values=values,
        covariance=covariance,
        remainder_envelopes=np.abs(deterministic_remainder),
        covariance_source="built-in correlated smoke covariance",
    )


def run(dataset: DataSet, fit_order: int, base_exponent: float, windows: Sequence[tuple[int, int]]) -> dict[str, object]:
    results = []
    for start, end in windows:
        window_slice = slice(start, end)
        results.append(
            {
                "window": [int(start), int(end)],
                **fit_window(
                    regulators=dataset.regulators[window_slice],
                    values=dataset.values[window_slice],
                    covariance=dataset.covariance[window_slice, window_slice],
                    remainder_envelopes=dataset.remainder_envelopes[window_slice],
                    fit_order=fit_order,
                    base_exponent=base_exponent,
                ),
            }
        )
    require(bool(results), "at least one fit window is required")
    intercepts = np.array([entry["intercept"] for entry in results], dtype=float)
    stat_errors = np.array([entry["intercept_stat_error"] for entry in results], dtype=float)
    systematic_bounds = np.array([entry["intercept_systematic_bound"] for entry in results], dtype=float)
    window_intercept_spread = float(np.max(intercepts) - np.min(intercepts)) if len(intercepts) > 1 else 0.0
    max_stat_error = float(np.max(stat_errors))
    max_systematic_bound = float(np.max(systematic_bounds))
    finite_evidence_budget = window_intercept_spread + max_stat_error + max_systematic_bound
    return {
        "fit_order": int(fit_order),
        "base_exponent": float(base_exponent),
        "covariance_source": dataset.covariance_source,
        "windows": results,
        "window_intercept_spread": window_intercept_spread,
        "max_intercept_stat_error": max_stat_error,
        "max_intercept_systematic_bound": max_systematic_bound,
        "finite_evidence_budget": float(finite_evidence_budget),
        "evidence_budget_components": {
            "window_intercept_spread": window_intercept_spread,
            "max_intercept_stat_error": max_stat_error,
            "max_intercept_systematic_bound": max_systematic_bound,
        },
        "interpretation": (
            "finite correlated extrapolation diagnostic only; continuum control requires "
            "a separately proved cutoff expansion, remainder estimate, and scaling-window "
            "or reconstruction argument"
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-csv", type=Path)
    parser.add_argument("--covariance-csv", type=Path)
    parser.add_argument("--fit-order", type=int, default=2)
    parser.add_argument("--base-exponent", type=float, default=1.0)
    parser.add_argument("--windows", default="")
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        dataset = smoke_dataset()
        args.fit_order = 2
        args.base_exponent = 1.0
        args.windows = "0:5,1:6,0:6"
    else:
        require(args.data_csv is not None, "supply --data-csv or use --smoke")
        dataset = load_dataset(args.data_csv, args.covariance_csv)
    windows = parse_windows(args.windows, int(dataset.regulators.size))
    result = run(dataset, args.fit_order, args.base_exponent, windows)
    if args.smoke:
        for entry in result["windows"]:
            require(np.isfinite(float(entry["intercept"])), "smoke intercept is not finite")
            require(float(entry["intercept_stat_error"]) > 0.0, "smoke statistical error should be positive")
            require(float(entry["intercept_systematic_bound"]) > 0.0, "smoke systematic bound should be positive")
            require(float(entry["condition_number"]) > 1.0, "smoke condition number should be nontrivial")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
