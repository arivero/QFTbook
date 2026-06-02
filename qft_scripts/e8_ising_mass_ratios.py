#!/usr/bin/env python3
"""Exact E8 mass-ratio target data for magnetic-Ising benchmarks.

The script records the standard eight mass ratios of the integrable
two-dimensional Ising field theory at vanishing thermal coupling and nonzero
magnetic coupling.  Its role in the numerical chapter is deliberately narrow:
it supplies exact target data and a finite algebraic consistency check for
TCSA/TFFSA comparisons.  It is not a finite-truncation computation of the
magnetic-Ising spectrum.

The smoke check compares two descriptions of the same target ratios:

1. the trigonometric Zamolodchikov mass-ratio formula;
2. the positive Perron-Frobenius eigenvector of the E8 Dynkin adjacency
   matrix, normalized by its smallest component.

The equality of these two finite lists is a convention check for the
target table used in plots and extrapolation diagnostics.
"""

from __future__ import annotations

import argparse
import json
import math

import numpy as np


def mass_ratios() -> np.ndarray:
    """Return the increasing E8 magnetic-Ising mass ratios m_a / m_1."""

    rho2 = 2.0 * math.cos(math.pi / 5.0)
    return np.array(
        [
            1.0,
            rho2,
            2.0 * math.cos(math.pi / 30.0),
            2.0 * rho2 * math.cos(7.0 * math.pi / 30.0),
            2.0 * rho2 * math.cos(2.0 * math.pi / 15.0),
            2.0 * rho2 * math.cos(math.pi / 30.0),
            4.0 * rho2 * math.cos(math.pi / 5.0) * math.cos(7.0 * math.pi / 30.0),
            4.0 * rho2 * math.cos(math.pi / 5.0) * math.cos(2.0 * math.pi / 15.0),
        ],
        dtype=float,
    )


def e8_adjacency() -> np.ndarray:
    """Return an E8 Dynkin adjacency matrix.

    The nodes 0,...,6 form a chain and node 7 is attached to node 2.  This is
    the same graph as the common drawing with branch attached to the third
    node from one end, up to relabeling.
    """

    adjacency = np.zeros((8, 8), dtype=float)
    for node in range(6):
        adjacency[node, node + 1] = 1.0
        adjacency[node + 1, node] = 1.0
    adjacency[2, 7] = 1.0
    adjacency[7, 2] = 1.0
    return adjacency


def perron_frobenius_check() -> dict[str, object]:
    """Return finite adjacency-eigenvector data for the E8 ratios."""

    adjacency = e8_adjacency()
    eigenvalues, eigenvectors = np.linalg.eigh(adjacency)
    index = int(np.argmax(eigenvalues))
    vector = np.abs(eigenvectors[:, index])
    ratios = np.sort(vector / np.min(vector))
    target = np.sort(mass_ratios())
    return {
        "coxeter_number": 30,
        "largest_adjacency_eigenvalue": float(eigenvalues[index]),
        "expected_largest_adjacency_eigenvalue": float(2.0 * math.cos(math.pi / 30.0)),
        "pf_component_ratios": [float(x) for x in ratios],
        "trigonometric_mass_ratios": [float(x) for x in target],
        "max_ratio_error": float(np.max(np.abs(ratios - target))),
    }


def run() -> dict[str, object]:
    ratios = mass_ratios()
    pf_check = perron_frobenius_check()
    return {
        "model": "magnetic Ising integrable E8 target data",
        "mass_ratios_m_over_m1": [float(x) for x in ratios],
        "golden_ratio_check": float(abs(ratios[1] - (1.0 + math.sqrt(5.0)) / 2.0)),
        "pf_check": pf_check,
        "interpretation": (
            "exact continuum target data for benchmark comparison; not a "
            "finite TCSA or TFFSA spectrum computation"
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run()
    if args.smoke:
        ratios = np.array(result["mass_ratios_m_over_m1"], dtype=float)
        if abs(ratios[0] - 1.0) > 1.0e-14:
            raise AssertionError("E8 ratios are not normalized by m1")
        if np.min(np.diff(ratios)) <= 0.0:
            raise AssertionError("E8 ratios are not strictly increasing")
        if result["golden_ratio_check"] > 1.0e-14:
            raise AssertionError("E8 second mass ratio is not the golden ratio")
        pf_check = result["pf_check"]
        if abs(
            pf_check["largest_adjacency_eigenvalue"]
            - pf_check["expected_largest_adjacency_eigenvalue"]
        ) > 1.0e-13:
            raise AssertionError("E8 adjacency eigenvalue does not match 2 cos(pi/30)")
        if pf_check["max_ratio_error"] > 1.0e-12:
            raise AssertionError("E8 PF component ratios do not match mass-ratio table")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
