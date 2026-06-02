#!/usr/bin/env python3
"""Finite cross-method benchmark-manifest consistency check.

The script implements the finite check described in Volume XI,
Chapter 10.  A manifest records several regulator methods that purport to
estimate the same finite coordinate of a declared target observable after
normalization.  For each pair of methods the script checks

    |x_m - x_n| <= e_m + e_n

componentwise, where e_m is the declared sum of statistical error,
finite-regulator envelope, and scheme-matching error.  Passing this check is
only a finite-regulator consistency check.  It is not a proof of the
continuum extrapolation hypothesis or of the correctness of the error model.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Any, Sequence

import numpy as np


@dataclass(frozen=True)
class MethodDatum:
    name: str
    regulator: str
    normalization: str
    coordinate: np.ndarray
    statistical_error: np.ndarray
    regulator_envelope: np.ndarray
    matching_error: np.ndarray
    covariance: np.ndarray | None
    provenance: dict[str, Any]

    @property
    def total_error(self) -> np.ndarray:
        return self.statistical_error + self.regulator_envelope + self.matching_error


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def as_vector(value: Any, name: str) -> np.ndarray:
    array = np.asarray(value, dtype=float)
    require(array.ndim == 1 and array.size > 0, f"{name} must be a nonempty vector")
    require(bool(np.all(np.isfinite(array))), f"{name} must be finite")
    return array


def optional_covariance(value: Any, dimension: int) -> np.ndarray | None:
    if value is None:
        return None
    matrix = np.asarray(value, dtype=float)
    require(matrix.shape == (dimension, dimension), "covariance has the wrong shape")
    require(bool(np.all(np.isfinite(matrix))), "covariance must be finite")
    require(float(np.max(np.abs(matrix - matrix.T))) <= 1.0e-10, "covariance must be symmetric")
    eigenvalues = np.linalg.eigvalsh(matrix)
    require(float(eigenvalues[0]) >= -1.0e-10, "covariance must be positive semidefinite")
    return matrix


def parse_method(raw: dict[str, Any], dimension: int) -> MethodDatum:
    required = [
        "name",
        "regulator",
        "normalization",
        "coordinate",
        "statistical_error",
        "regulator_envelope",
        "matching_error",
        "provenance",
    ]
    for key in required:
        require(key in raw, f"method entry is missing {key!r}")

    coordinate = as_vector(raw["coordinate"], "coordinate")
    require(coordinate.size == dimension, "coordinate dimension does not match the observable")
    stat = as_vector(raw["statistical_error"], "statistical_error")
    reg = as_vector(raw["regulator_envelope"], "regulator_envelope")
    match = as_vector(raw["matching_error"], "matching_error")
    for label, vector in [
        ("statistical_error", stat),
        ("regulator_envelope", reg),
        ("matching_error", match),
    ]:
        require(vector.size == dimension, f"{label} dimension does not match the observable")
        require(bool(np.all(vector >= 0.0)), f"{label} must be componentwise nonnegative")

    provenance = raw["provenance"]
    require(isinstance(provenance, dict) and bool(provenance), "provenance must be a nonempty object")
    return MethodDatum(
        name=str(raw["name"]),
        regulator=str(raw["regulator"]),
        normalization=str(raw["normalization"]),
        coordinate=coordinate,
        statistical_error=stat,
        regulator_envelope=reg,
        matching_error=match,
        covariance=optional_covariance(raw.get("covariance"), dimension),
        provenance=provenance,
    )


def parse_manifest(raw: dict[str, Any]) -> tuple[dict[str, Any], list[MethodDatum]]:
    require("observable" in raw, "manifest is missing 'observable'")
    observable = raw["observable"]
    require(isinstance(observable, dict), "observable must be an object")
    require("name" in observable and "dimension" in observable and "norm" in observable, "observable needs name, dimension, norm")
    dimension = int(observable["dimension"])
    require(dimension > 0, "observable dimension must be positive")
    norm = str(observable["norm"])
    require(norm == "componentwise", "only componentwise benchmark checks are implemented")

    methods_raw = raw.get("methods")
    require(isinstance(methods_raw, list) and len(methods_raw) >= 2, "manifest must contain at least two methods")
    methods = [parse_method(entry, dimension) for entry in methods_raw]
    names = [entry.name for entry in methods]
    require(len(names) == len(set(names)), "method names must be distinct")
    return observable, methods


def analyze_manifest(raw: dict[str, Any]) -> dict[str, Any]:
    observable, methods = parse_manifest(raw)
    pairs: list[dict[str, Any]] = []
    all_pass = True
    for left, right in combinations(methods, 2):
        difference = np.abs(left.coordinate - right.coordinate)
        bound = left.total_error + right.total_error
        margin = bound - difference
        passed = bool(np.all(margin >= -1.0e-12))
        all_pass = all_pass and passed
        pairs.append(
            {
                "left": left.name,
                "right": right.name,
                "normalizations_match": left.normalization == right.normalization,
                "max_difference": float(np.max(difference)),
                "min_margin": float(np.min(margin)),
                "component_differences": [float(x) for x in difference],
                "component_bounds": [float(x) for x in bound],
                "component_margins": [float(x) for x in margin],
                "passes": passed,
            }
        )
    return {
        "observable": observable,
        "method_count": len(methods),
        "methods": [
            {
                "name": entry.name,
                "regulator": entry.regulator,
                "normalization": entry.normalization,
                "total_error": [float(x) for x in entry.total_error],
                "has_covariance": entry.covariance is not None,
                "provenance": entry.provenance,
            }
            for entry in methods
        ],
        "pairs": pairs,
        "all_pairs_pass": all_pass,
        "interpretation": (
            "finite benchmark-manifest consistency only; continuum claims require "
            "independent cutoff, volume, normalization, and reconstruction estimates"
        ),
    }


def smoke_manifest() -> dict[str, Any]:
    return {
        "observable": {
            "name": "dimensionless first mass ratio",
            "dimension": 2,
            "norm": "componentwise",
            "coordinate_labels": ["m2_over_m1", "m3_over_m1"],
        },
        "methods": [
            {
                "name": "lattice-transfer-matrix",
                "regulator": "finite Euclidean lattice, a/L declared",
                "normalization": "mass-gap ratio in common target convention",
                "coordinate": [1.61810, 1.9890],
                "statistical_error": [0.0010, 0.0030],
                "regulator_envelope": [0.0015, 0.0050],
                "matching_error": [0.0005, 0.0020],
                "covariance": [[1.0e-6, 2.0e-7], [2.0e-7, 9.0e-6]],
                "provenance": {"script": "qft_scripts/static_potential_from_wilson_loops.py", "seed": 17},
            },
            {
                "name": "hamiltonian-truncation",
                "regulator": "finite energy cutoff and sector projection",
                "normalization": "mass-gap ratio in common target convention",
                "coordinate": [1.6170, 1.9970],
                "statistical_error": [0.0, 0.0],
                "regulator_envelope": [0.0020, 0.0060],
                "matching_error": [0.0005, 0.0020],
                "provenance": {"script": "qft_scripts/tffsa_ising_spectral_flow.py", "cutoff": 8},
            },
            {
                "name": "dlcq",
                "regulator": "finite harmonic resolution K",
                "normalization": "mass-gap ratio in common target convention",
                "coordinate": [1.6200, 1.9910],
                "statistical_error": [0.0, 0.0],
                "regulator_envelope": [0.0040, 0.0090],
                "matching_error": [0.0005, 0.0020],
                "provenance": {"script": "qft_scripts/thooft_dlcq_extrapolation.py", "K": [8, 10, 12]},
            },
        ],
    }


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        raw = json.load(handle)
    require(isinstance(raw, dict), "manifest JSON root must be an object")
    return raw


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, help="benchmark-manifest JSON file")
    parser.add_argument("--smoke", action="store_true", help="run the built-in smoke manifest")
    parser.add_argument("--allow-failures", action="store_true", help="return exit code 0 even if a pair fails")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    require(args.smoke or args.manifest is not None, "supply --manifest or use --smoke")
    raw = smoke_manifest() if args.smoke else load_manifest(args.manifest)
    result = analyze_manifest(raw)
    print(json.dumps(result, sort_keys=True))
    if not args.allow_failures and not result["all_pairs_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
