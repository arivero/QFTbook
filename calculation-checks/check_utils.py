"""Shared numerical assertions for public calculation checks."""

from __future__ import annotations

import math
from typing import Any


def _finite_scalar(value: Any) -> bool:
    try:
        real = value.real
        imag = value.imag
    except AttributeError:
        real = value
        imag = 0.0
    try:
        return math.isfinite(float(real)) and math.isfinite(float(imag))
    except (TypeError, ValueError, OverflowError):
        return False


def assert_finite(name: str, value: Any) -> None:
    if not _finite_scalar(value):
        raise AssertionError(f"{name}: nonfinite value {value!r}")


def assert_close(
    name: str,
    actual: complex | float,
    expected: complex | float,
    tol: float = 1.0e-12,
    *,
    atol: float | None = None,
    rtol: float = 0.0,
) -> None:
    """Assert a finite scalar equality within absolute plus relative tolerance."""

    absolute_tolerance = tol if atol is None else atol
    if absolute_tolerance < 0.0 or rtol < 0.0:
        raise AssertionError(f"{name}: negative tolerance")
    assert_finite(f"{name} actual", actual)
    assert_finite(f"{name} expected", expected)
    error = abs(actual - expected)
    assert_finite(f"{name} error", error)
    threshold = absolute_tolerance + rtol * abs(expected)
    assert_finite(f"{name} tolerance", threshold)
    if error > threshold:
        raise AssertionError(
            f"{name}: got {actual!r}, expected {expected!r}, "
            f"error {error!r}, tolerance {threshold!r}"
        )


def assert_leq(
    name: str,
    actual: Any,
    bound: Any,
    tol: Any = 0.0,
) -> None:
    """Assert a finite scalar upper bound with an optional tolerance."""

    if tol < 0.0:
        raise AssertionError(f"{name}: negative tolerance")
    assert_finite(f"{name} actual", actual)
    assert_finite(f"{name} bound", bound)
    assert_finite(f"{name} tolerance", tol)
    if actual > bound + tol:
        raise AssertionError(f"{name}: got {actual!r}, bound {bound!r}, tolerance {tol!r}")


def assert_lt(
    name: str,
    actual: Any,
    bound: Any,
) -> None:
    """Assert a finite strict scalar upper bound."""

    assert_finite(f"{name} actual", actual)
    assert_finite(f"{name} bound", bound)
    if not actual < bound:
        raise AssertionError(f"{name}: expected {actual!r} < {bound!r}")


def assert_array_close(
    name: str,
    actual: Any,
    expected: Any,
    tol: float = 1.0e-12,
    *,
    atol: float | None = None,
    rtol: float = 0.0,
) -> None:
    """Assert finite NumPy-compatible arrays agree elementwise."""

    import numpy as np

    absolute_tolerance = tol if atol is None else atol
    if absolute_tolerance < 0.0 or rtol < 0.0:
        raise AssertionError(f"{name}: negative tolerance")
    actual_array = np.asarray(actual)
    expected_array = np.asarray(expected)
    if actual_array.shape != expected_array.shape:
        raise AssertionError(
            f"{name}: shape mismatch {actual_array.shape!r} != {expected_array.shape!r}"
        )
    if not bool(np.all(np.isfinite(actual_array))):
        raise AssertionError(f"{name}: actual array contains nonfinite entries")
    if not bool(np.all(np.isfinite(expected_array))):
        raise AssertionError(f"{name}: expected array contains nonfinite entries")
    diff = np.abs(actual_array - expected_array)
    if not bool(np.all(np.isfinite(diff))):
        raise AssertionError(f"{name}: difference contains nonfinite entries")
    tolerance = absolute_tolerance + rtol * np.abs(expected_array)
    if not bool(np.all(np.isfinite(tolerance))):
        raise AssertionError(f"{name}: tolerance contains nonfinite entries")
    if diff.size == 0:
        return
    excess = diff - tolerance
    max_excess = float(np.max(excess))
    if max_excess > 0.0:
        max_error = float(np.max(diff))
        max_tolerance = float(np.max(tolerance))
        raise AssertionError(
            f"{name}: max error {max_error:.3e}, "
            f"max tolerance {max_tolerance:.3e}, exceeded by {max_excess:.3e}"
        )


if __name__ == "__main__":
    print("check_utils is a helper module; run check_utils_checks.py for tests.")
