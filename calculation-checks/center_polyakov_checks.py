#!/usr/bin/env python3
"""Finite checks for the thermal center-symmetry and Polyakov-loop section.

The script checks only convention-sensitive finite group arithmetic:

    z_m = exp(2 pi i m/N),
    P_R -> z_m^{k_R} P_R,
    temporal plaquette phases cancel as z_m z_m^{-1},
    P_R P_{\bar R} is center neutral,
    <P_R> = exp[-beta_T (F_R-F_0)].

It is not a lattice simulation and does not assume a deconfinement transition.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import cmath
import math


def assert_close(name: str, lhs: complex | float, rhs: complex | float, tol: float = 1e-12) -> None:
    _assert_close(name, lhs, rhs, tol=tol)


def center_phase(n: int, m: int, k: int) -> complex:
    return cmath.exp(2j * math.pi * m * k / n)


def check_temporal_plaquette_center_cancellation() -> None:
    for n in range(2, 9):
        for m in range(n):
            z = center_phase(n, m, 1)
            assert_close(f"plaquette center cancellation N={n} m={m}", z / z, 1.0)


def check_polyakov_loop_center_charge() -> None:
    n = 5
    m = 2
    for k in range(n):
        phase = center_phase(n, m, k)
        expected = center_phase(n, m, 1) ** k
        assert_close(f"Polyakov N-ality phase k={k}", phase, expected)


def check_pair_correlator_center_neutrality() -> None:
    for n in range(2, 9):
        for m in range(n):
            for k in range(n):
                source = center_phase(n, m, k)
                antisource = center_phase(n, m, -k)
                assert_close(f"neutral pair N={n} m={m} k={k}", source * antisource, 1.0)


def check_center_average_kills_charged_loop() -> None:
    for n in range(2, 9):
        for k in range(1, n):
            average = sum(center_phase(n, m, k) for m in range(n)) / n
            assert_close(f"center average N={n} k={k}", average, 0.0)


def check_static_source_free_energy_relation() -> None:
    beta_t = 3.7
    delta_f = 0.42
    loop = math.exp(-beta_t * delta_f)
    recovered = -math.log(loop) / beta_t
    assert_close("static-source free energy relation", recovered, delta_f)


def main() -> None:
    check_temporal_plaquette_center_cancellation()
    check_polyakov_loop_center_charge()
    check_pair_correlator_center_neutrality()
    check_center_average_kills_charged_loop()
    check_static_source_free_energy_relation()
    print("All thermal center-symmetry and Polyakov-loop checks passed.")


if __name__ == "__main__":
    main()
