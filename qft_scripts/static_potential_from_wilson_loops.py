#!/usr/bin/env python3
"""Extract static-potential diagnostics from rectangular Wilson-loop data.

The theorem anchor is Volume XI, Chapter 5,
Proposition ``Spectral extraction of the finite-lattice static energy'' and
the Creutz-ratio definition in the same chapter.  The script is deliberately
finite-regulator: it reads positive Wilson-loop estimates W(R,T), computes
effective-mass ratios in the Euclidean-time direction, and computes Creutz
ratios when the required neighboring rectangles are present.

Input CSV columns:
    R,T,W[,dW]

Output CSV columns:
    observable,R,T,value,error

Here R and T are integer lattice extents.  The optional error column dW is
treated as an independent standard error for elementary propagation only; a
serious Monte Carlo analysis must use jackknife/bootstrap bins upstream.
"""

from __future__ import annotations

import argparse
import csv
import io
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class WilsonLoopDatum:
    r: int
    t: int
    value: float
    error: float | None = None


@dataclass(frozen=True)
class ObservableDatum:
    observable: str
    r: int
    t: int
    value: float
    error: float | None = None


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


def index_data(data: list[WilsonLoopDatum]) -> dict[tuple[int, int], WilsonLoopDatum]:
    indexed: dict[tuple[int, int], WilsonLoopDatum] = {}
    for datum in data:
        key = (datum.r, datum.t)
        require(key not in indexed, f"duplicate Wilson-loop datum for R={datum.r}, T={datum.t}")
        indexed[key] = datum
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


def synthetic_area_perimeter_data(sigma: float, mu: float, constant: float, max_r: int, max_t: int) -> list[WilsonLoopDatum]:
    data: list[WilsonLoopDatum] = []
    for r in range(max_r + 1):
        for t in range(max_t + 1):
            exponent = sigma * r * t + mu * (r + t) + constant
            data.append(WilsonLoopDatum(r, t, math.exp(-exponent)))
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
    print("static_potential_from_wilson_loops.py smoke test passed.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="CSV file with columns R,T,W[,dW]")
    parser.add_argument("--output", type=Path, help="output CSV for extracted observables")
    parser.add_argument("--lattice-spacing", type=float, default=1.0)
    parser.add_argument("--no-effective-mass", action="store_true")
    parser.add_argument("--no-creutz", action="store_true")
    parser.add_argument("--smoke", action="store_true", help="run the built-in synthetic-data smoke test")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        run_smoke_test()
        return
    require(args.input is not None and args.output is not None, "--input and --output are required outside --smoke")
    data = read_wilson_loop_csv(args.input)
    output: list[ObservableDatum] = []
    if not args.no_effective_mass:
        output.extend(effective_masses(data, args.lattice_spacing))
    if not args.no_creutz:
        output.extend(creutz_ratios(data))
    write_observables(args.output, output)


if __name__ == "__main__":
    main()
