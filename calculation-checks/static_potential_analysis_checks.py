#!/usr/bin/env python3
"""Checks for the static-potential Wilson-loop analysis script."""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "static_potential_from_wilson_loops.py"


def load_module():
    spec = importlib.util.spec_from_file_location("static_potential_from_wilson_loops", SCRIPT)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load static-potential analysis script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    module = load_module()
    sigma = 0.41
    mu = 0.23
    constant = 0.07
    data = module.synthetic_area_perimeter_data(sigma, mu, constant, max_r=5, max_t=6)
    eff = module.effective_masses(data, lattice_spacing=1.0)
    creutz = module.creutz_ratios(data)
    require(len(eff) > 0, "effective-mass output should be nonempty")
    require(len(creutz) > 0, "Creutz-ratio output should be nonempty")
    for datum in eff:
        require(abs(datum.value - (sigma * datum.r + mu)) < 1e-12, "effective mass should recover sigma R + mu")
    for datum in creutz:
        require(abs(datum.value - sigma) < 1e-12, "Creutz ratio should recover sigma")

    noisy_error_data = [
        module.WilsonLoopDatum(1, 1, math.exp(-0.3), 0.01),
        module.WilsonLoopDatum(1, 2, math.exp(-0.6), 0.02),
    ]
    one_eff = module.effective_masses(noisy_error_data, lattice_spacing=2.0)[0]
    expected_error = 0.5 * math.sqrt((0.02 / math.exp(-0.6)) ** 2 + (0.01 / math.exp(-0.3)) ** 2)
    require(abs(one_eff.error - expected_error) < 1e-14, "effective-mass error propagation failed")

    sigmas = [0.25, 0.34, 0.39, 0.52]
    sample_data = module.synthetic_area_perimeter_sample_data(sigmas, mu=0.17, constant=0.03, max_r=3, max_t=4)
    resampled = module.resampled_static_observables(
        sample_data,
        lattice_spacing=1.0,
        block_size=1,
        bootstrap_samples=12,
        seed=19,
    )
    resampled_map = {
        (datum.observable, datum.r, datum.t): datum
        for datum in resampled
    }
    key = ("effective_mass", 2, 1)
    datum = resampled_map[key]

    indexed = module.index_sample_data(sample_data)
    all_samples = sorted(indexed)
    central = module.observables_from_sample_ids(indexed, all_samples, 1.0, True, True)
    require(abs(datum.value - central[key]) < 1e-14, "central resampled observable failed")

    delete_values = []
    for removed in all_samples:
        kept = [sample for sample in all_samples if sample != removed]
        delete_values.append(module.observables_from_sample_ids(indexed, kept, 1.0, True, True)[key])
    theta_bar = sum(delete_values) / len(delete_values)
    expected_jackknife = math.sqrt(
        (len(delete_values) - 1) / len(delete_values)
        * sum((theta - theta_bar) ** 2 for theta in delete_values)
    )
    require(abs(datum.jackknife_error - expected_jackknife) < 1e-14, "correlated jackknife error failed")
    require(datum.bootstrap_error > 0.0, "block bootstrap error should be positive on varying samples")

    print("All static-potential analysis checks passed.")


if __name__ == "__main__":
    main()
