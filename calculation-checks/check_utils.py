"""Shared numerical assertions for public calculation checks."""

from __future__ import annotations

import math
import warnings
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


def assert_finite_array(name: str, value: Any, *, ndim: int | None = None):
    """Return a NumPy array after proving all entries are finite."""

    import numpy as np

    array = np.asarray(value)
    if ndim is not None and array.ndim != ndim:
        raise AssertionError(f"{name}: expected {ndim} dimensions, got {array.ndim}")
    if not bool(np.all(np.isfinite(array))):
        raise AssertionError(f"{name}: array contains nonfinite entries")
    return array


def _reference_matmul(left, right):
    import numpy as np

    if left.ndim != 2:
        raise AssertionError(f"left matrix: expected 2 dimensions, got {left.ndim}")
    if right.ndim not in {1, 2}:
        raise AssertionError(f"right factor: expected 1 or 2 dimensions, got {right.ndim}")
    if left.shape[1] != right.shape[0]:
        raise AssertionError(f"matrix product: shape mismatch {left.shape!r} @ {right.shape!r}")

    dtype = np.result_type(left, right)
    if right.ndim == 1:
        result = np.empty(left.shape[0], dtype=dtype)
        for row in range(left.shape[0]):
            total = 0
            for middle in range(left.shape[1]):
                total += left[row, middle] * right[middle]
            result[row] = total
        return result

    result = np.empty((left.shape[0], right.shape[1]), dtype=dtype)
    for row in range(left.shape[0]):
        for col in range(right.shape[1]):
            total = 0
            for middle in range(left.shape[1]):
                total += left[row, middle] * right[middle, col]
            result[row, col] = total
    return result


def finite_matmul(name: str, left: Any, right: Any):
    """Matrix product with finite input/output checks and a warning-clean fallback."""

    import numpy as np

    left_array = assert_finite_array(f"{name} left", left, ndim=2)
    right_array = assert_finite_array(f"{name} right", right)
    if right_array.ndim not in {1, 2}:
        raise AssertionError(f"{name}: right factor has unsupported dimension {right_array.ndim}")
    if left_array.shape[1] != right_array.shape[0]:
        raise AssertionError(f"{name}: shape mismatch {left_array.shape!r} @ {right_array.shape!r}")

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", RuntimeWarning)
            with np.errstate(all="raise"):
                product = np.matmul(left_array, right_array)
    except (FloatingPointError, RuntimeWarning):
        try:
            product = _reference_matmul(left_array, right_array)
        except (FloatingPointError, RuntimeWarning, OverflowError) as reference_exc:
            raise AssertionError(f"{name}: matrix product raised a finite-arithmetic warning") from reference_exc
    return assert_finite_array(f"{name} product", product)


def finite_max_abs(name: str, value: Any) -> float:
    """Return max(abs(value)) after proving the array and magnitudes are finite."""

    import numpy as np

    array = assert_finite_array(f"{name} input", value)
    if array.size == 0:
        raise AssertionError(f"{name}: empty array has no maximum")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", RuntimeWarning)
            with np.errstate(all="raise"):
                magnitudes = np.abs(array)
    except (FloatingPointError, RuntimeWarning):
        magnitudes = np.array([abs(complex(entry)) for entry in array.flat]).reshape(array.shape)
    magnitudes = assert_finite_array(f"{name} magnitudes", magnitudes)
    return float(np.max(magnitudes))


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


def assert_geq(
    name: str,
    actual: Any,
    bound: Any,
    tol: Any = 0.0,
) -> None:
    """Assert a finite scalar lower bound with an optional tolerance."""

    if tol < 0.0:
        raise AssertionError(f"{name}: negative tolerance")
    assert_finite(f"{name} actual", actual)
    assert_finite(f"{name} bound", bound)
    assert_finite(f"{name} tolerance", tol)
    if actual < bound - tol:
        raise AssertionError(f"{name}: got {actual!r}, lower bound {bound!r}, tolerance {tol!r}")


def assert_gt(
    name: str,
    actual: Any,
    bound: Any,
) -> None:
    """Assert a finite strict scalar lower bound."""

    assert_finite(f"{name} actual", actual)
    assert_finite(f"{name} bound", bound)
    if not actual > bound:
        raise AssertionError(f"{name}: expected {actual!r} > {bound!r}")


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
