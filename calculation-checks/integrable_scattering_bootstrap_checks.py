#!/usr/bin/env python3
"""Checks for scalar bootstrap blocks in two-dimensional integrable scattering."""

import cmath
import math


def assert_close(label: str, actual: complex, expected: complex, tol: float = 2.0e-12) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def block(theta: complex, x: float) -> complex:
    return cmath.sinh((theta + 1j * math.pi * x) / 2) / cmath.sinh(
        (theta - 1j * math.pi * x) / 2
    )


def block_residue_at_physical_pole(x: float) -> complex:
    return 2j * math.sin(math.pi * x)


def crossing_pair_residue_at_x_pole(x: float) -> complex:
    theta0 = 1j * math.pi * x
    return block_residue_at_physical_pole(x) * block(theta0, 1 - x)


def crossing_pair_residue_at_one_minus_x_pole(x: float) -> complex:
    theta0 = 1j * math.pi * (1 - x)
    return block_residue_at_physical_pole(1 - x) * block(theta0, x)


def check_elementary_block_unitarity_and_crossing_pair() -> None:
    for x in (0.2, 0.35, 0.7):
        for theta in (0.4 + 0.17j, -0.9 + 0.23j, 1.1 - 0.19j):
            assert_close(
                f"elementary block unitarity x={x} theta={theta}",
                block(theta, x) * block(-theta, x),
                1.0 + 0.0j,
            )
            assert_close(
                f"elementary crossing relation x={x} theta={theta}",
                block(1j * math.pi - theta, x),
                -block(theta, 1 - x),
            )
            pair = block(theta, x) * block(theta, 1 - x)
            assert_close(
                f"crossing pair unitarity x={x} theta={theta}",
                pair * block(-theta, x) * block(-theta, 1 - x),
                1.0 + 0.0j,
            )
            assert_close(
                f"crossing pair crossing x={x} theta={theta}",
                pair,
                block(1j * math.pi - theta, x) * block(1j * math.pi - theta, 1 - x),
            )


def check_residue_signs() -> None:
    for x in (0.2, 0.35, 0.7):
        direct = -1j * block_residue_at_physical_pole(x)
        if direct.real <= 0 or abs(direct.imag) > 1.0e-13:
            raise AssertionError(f"single block direct residue sign failed at x={x}: {direct!r}")

        residue_x = -1j * crossing_pair_residue_at_x_pole(x)
        residue_one_minus_x = -1j * crossing_pair_residue_at_one_minus_x_pole(x)
        assert_close(
            f"crossing-pair residue at x pole x={x}",
            residue_x,
            -2 * math.tan(math.pi * x),
        )
        assert_close(
            f"crossing-pair residue at one-minus-x pole x={x}",
            residue_one_minus_x,
            2 * math.tan(math.pi * x),
        )
        assert_close(
            f"opposite crossing-pair residue signs x={x}",
            residue_x + residue_one_minus_x,
            0.0 + 0.0j,
        )


def main() -> None:
    check_elementary_block_unitarity_and_crossing_pair()
    check_residue_signs()
    print("All integrable scattering bootstrap scalar-block checks passed.")


if __name__ == "__main__":
    main()
