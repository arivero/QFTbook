#!/usr/bin/env python3
"""Regression tests for finite-aware numerical calculation assertions."""

from __future__ import annotations

import ast
import math
from pathlib import Path

import numpy as np

from check_utils import assert_array_close, assert_close


def expect_failure(name: str, thunk) -> None:
    try:
        thunk()
    except AssertionError:
        return
    raise AssertionError(f"{name}: expected AssertionError")


def check_scalar_nonfinite_rejection() -> None:
    for value in (math.nan, math.inf, -math.inf, complex(math.inf, 0.0), complex(0.0, math.nan)):
        expect_failure(
            f"scalar nonfinite {value!r}",
            lambda value=value: assert_close("scalar nonfinite", value, 0.0),
        )
    expect_failure(
        "scalar nonfinite expected",
        lambda: assert_close("scalar nonfinite expected", 1.0, math.nan),
    )


def check_scalar_finite_tolerance() -> None:
    assert_close("scalar absolute tolerance", 1.0 + 5.0e-13, 1.0, tol=1.0e-12)
    assert_close("scalar relative tolerance", 1000.0 + 5.0e-7, 1000.0, tol=0.0, rtol=1.0e-9)
    expect_failure(
        "scalar excessive finite error",
        lambda: assert_close("scalar excessive finite error", 1.0 + 2.0e-12, 1.0, tol=1.0e-12),
    )


def check_array_nonfinite_rejection() -> None:
    expect_failure(
        "array actual nan",
        lambda: assert_array_close("array actual nan", np.array([1.0, math.nan]), np.array([1.0, 0.0])),
    )
    expect_failure(
        "array expected inf",
        lambda: assert_array_close("array expected inf", np.array([1.0, 0.0]), np.array([1.0, math.inf])),
    )
    expect_failure(
        "array shape mismatch",
        lambda: assert_array_close("array shape mismatch", np.array([1.0, 2.0]), np.array([[1.0, 2.0]])),
    )


def check_array_finite_tolerance() -> None:
    assert_array_close(
        "array finite tolerance",
        np.array([[1.0, 2.0 + 4.0e-13], [3.0, 4.0]]),
        np.array([[1.0, 2.0], [3.0, 4.0]]),
        tol=1.0e-12,
    )
    assert_array_close(
        "array relative tolerance",
        np.array([1000.0 + 5.0e-7, 2.0]),
        np.array([1000.0, 2.0]),
        tol=0.0,
        rtol=1.0e-9,
    )
    expect_failure(
        "array excessive finite error",
        lambda: assert_array_close(
            "array excessive finite error",
            np.array([1.0 + 2.0e-12]),
            np.array([1.0]),
            tol=1.0e-12,
        ),
    )


def check_no_legacy_nan_accepting_helpers() -> None:
    offenders: list[str] = []
    root = Path(__file__).resolve().parent
    names = {"assert_close", "assert_matrix_close", "assert_close_float"}
    for path in sorted(root.glob("*.py")):
        if path.name in {"check_utils.py", "check_utils_checks.py"}:
            continue
        text = path.read_text()
        tree = ast.parse(text)
        lines = text.splitlines(True)
        for node in tree.body:
            if not isinstance(node, ast.FunctionDef) or node.name not in names:
                continue
            segment = "".join(lines[node.lineno - 1 : node.end_lineno])
            has_direct_abs_threshold = "abs(" in segment and ">" in segment
            delegates_to_hardened_helper = "_assert_close" in segment or "_assert_array_close" in segment
            has_local_finiteness_guard = "isfinite" in segment
            if has_direct_abs_threshold and not delegates_to_hardened_helper and not has_local_finiteness_guard:
                offenders.append(f"{path.name}:{node.lineno}:{node.name}")
    if offenders:
        raise AssertionError("legacy NaN-accepting helpers remain: " + ", ".join(offenders))


def main() -> None:
    check_scalar_nonfinite_rejection()
    check_scalar_finite_tolerance()
    check_array_nonfinite_rejection()
    check_array_finite_tolerance()
    check_no_legacy_nan_accepting_helpers()
    print("All calculation assertion utility checks passed.")


if __name__ == "__main__":
    main()
