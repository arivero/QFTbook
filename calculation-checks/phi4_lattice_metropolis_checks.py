#!/usr/bin/env python3
"""Finite algebra checks for the scalar phi^4 Metropolis companion script."""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

import numpy as np

from check_utils import assert_close as _assert_close
from check_utils import assert_geq as _assert_geq
from check_utils import assert_leq as _assert_leq


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "phi4_2d_metropolis.py"
spec = importlib.util.spec_from_file_location("phi4_2d_metropolis", SCRIPT)
phi4 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = phi4
spec.loader.exec_module(phi4)


def deterministic_field(L: int) -> np.ndarray:
    values = np.arange(L * L, dtype=float).reshape((L, L))
    return values / 7.0 - 0.6


def check_local_action_change() -> None:
    field = deterministic_field(4)
    mass_sq = -0.4
    quartic = 1.7
    base_action = phi4.total_action(field, mass_sq, quartic)
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            new_value = float(field[i, j] + 0.31 - 0.07 * i + 0.05 * j)
            changed = field.copy()
            changed[i, j] = new_value
            direct = phi4.total_action(changed, mass_sq, quartic) - base_action
            local = phi4.local_action_change(field, i, j, new_value, mass_sq, quartic)
            _assert_close("local phi^4 action change versus total action", direct, local, tol=1.0e-12)


def check_pairwise_detailed_balance() -> None:
    field = deterministic_field(3)
    mass_sq = 0.35
    quartic = 1.2
    old_action = phi4.total_action(field, mass_sq, quartic)
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            for shift in (-0.42, 0.17, 0.63):
                new_value = float(field[i, j] + shift)
                delta = phi4.local_action_change(field, i, j, new_value, mass_sq, quartic)
                changed = field.copy()
                changed[i, j] = new_value
                new_action = phi4.total_action(changed, mass_sq, quartic)
                forward = math.exp(-old_action) * min(1.0, math.exp(-delta))
                reverse = math.exp(-new_action) * min(1.0, math.exp(delta))
                scale = max(1.0, abs(forward), abs(reverse))
                _assert_leq("pairwise Metropolis detailed balance", abs(forward - reverse) / scale, 1.0e-12)


def check_pointwise_stability_bound() -> None:
    for mass_sq, quartic in [(-0.7, 1.3), (-2.0, 5.0), (0.4, 0.9)]:
        if mass_sq < 0.0:
            lower = -1.5 * mass_sq * mass_sq / quartic
        else:
            lower = 0.0
        samples = np.linspace(-5.0, 5.0, 401)
        values = phi4.potential(samples, mass_sq, quartic)
        _assert_geq("quartic potential grid lower bound", float(np.min(values)), lower, tol=2.0e-3)
        if mass_sq < 0.0:
            minimizer = math.sqrt(-6.0 * mass_sq / quartic)
            exact = phi4.potential(minimizer, mass_sq, quartic)
            _assert_close("analytic double-well lower bound", exact, lower, tol=1.0e-12)


def main() -> None:
    check_local_action_change()
    check_pairwise_detailed_balance()
    check_pointwise_stability_bound()
    print("All finite phi^4 lattice Metropolis checks passed.")


if __name__ == "__main__":
    main()
