#!/usr/bin/env python3
"""Regression tests for finite-aware numerical calculation assertions."""

from __future__ import annotations

import ast
import math
from pathlib import Path

import numpy as np

from check_utils import assert_array_close, assert_close, assert_leq, assert_lt


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


def check_bound_nonfinite_rejection() -> None:
    for value in (math.nan, math.inf, -math.inf):
        expect_failure(
            f"bound actual nonfinite {value!r}",
            lambda value=value: assert_leq("bound actual nonfinite", value, 1.0),
        )
        expect_failure(
            f"bound target nonfinite {value!r}",
            lambda value=value: assert_leq("bound target nonfinite", 0.0, value),
        )
    expect_failure(
        "bound tolerance nonfinite",
        lambda: assert_leq("bound tolerance nonfinite", 0.0, 1.0, tol=math.inf),
    )
    expect_failure(
        "bound excessive finite value",
        lambda: assert_leq("bound excessive finite value", 1.0 + 2.0e-12, 1.0, tol=1.0e-12),
    )
    assert_leq("bound finite tolerance", 1.0 + 5.0e-13, 1.0, tol=1.0e-12)
    for value in (math.nan, math.inf, -math.inf):
        expect_failure(
            f"strict bound actual nonfinite {value!r}",
            lambda value=value: assert_lt("strict bound actual nonfinite", value, 1.0),
        )
        expect_failure(
            f"strict bound target nonfinite {value!r}",
            lambda value=value: assert_lt("strict bound target nonfinite", 0.0, value),
        )
    expect_failure(
        "strict bound equality",
        lambda: assert_lt("strict bound equality", 1.0, 1.0),
    )
    assert_lt("strict bound finite", 1.0, 2.0)


def _call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_call_name(node.value)}.{node.attr}"
    return ""


def _contains_call(node: ast.AST, names: set[str]) -> bool:
    for child in ast.walk(node):
        if isinstance(child, ast.Call) and _call_name(child.func) in names:
            return True
    return False


def _contains_np_max_abs(node: ast.AST) -> bool:
    for child in ast.walk(node):
        if not isinstance(child, ast.Call) or _call_name(child.func) not in {"np.max", "numpy.max"}:
            continue
        if child.args and _contains_call(child.args[0], {"np.abs", "numpy.abs"}):
            return True
    return False


def _has_threshold_compare(node: ast.FunctionDef) -> bool:
    lowered = node.name.lower()
    is_bound_helper = any(marker in lowered for marker in ("leq", "less", "bound"))
    for child in ast.walk(node):
        if not isinstance(child, ast.Compare):
            continue
        operands = [child.left, *child.comparators]
        if _contains_call(child, {"abs", "math.fabs", "np.abs", "numpy.abs"}):
            return True
        if any(_contains_np_max_abs(operand) for operand in operands):
            return True
        if is_bound_helper and any(
            isinstance(operator, (ast.Lt, ast.LtE, ast.Gt, ast.GtE))
            for operator in child.ops
        ):
            return True
    return False


def _numeric_helper_name(name: str) -> bool:
    lowered = name.lower()
    return lowered.startswith(("assert", "_assert", "require")) and any(
        marker in lowered
        for marker in (
            "close",
            "near",
            "leq",
            "lt",
            "less",
            "bound",
        )
    )


def _delegates_or_guards(node: ast.FunctionDef, segment: str) -> bool:
    delegated_helpers = {
        "_assert_close",
        "_assert_array_close",
        "_assert_leq",
        "_assert_lt",
        "assert_close",
        "assert_array_close",
        "assert_leq",
        "assert_lt",
        "check_utils.assert_close",
        "check_utils.assert_array_close",
        "check_utils.assert_leq",
        "check_utils.assert_lt",
    }
    delegates = any(
        isinstance(child, ast.Call)
        and _call_name(child.func) in delegated_helpers
        and _call_name(child.func) != node.name
        for child in ast.walk(node)
    )
    return delegates or "isfinite" in segment or "assert_finite" in segment


def unsafe_numeric_predicate_offenders(path_name: str, text: str) -> list[str]:
    offenders: list[str] = []
    tree = ast.parse(text)
    lines = text.splitlines(True)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and _numeric_helper_name(node.name):
            segment = "".join(lines[node.lineno - 1 : node.end_lineno])
            if _has_threshold_compare(node) and not _delegates_or_guards(node, segment):
                offenders.append(f"{path_name}:{node.lineno}:{node.name}")
        if isinstance(node, ast.Compare):
            operands = [node.left, *node.comparators]
            if any(_contains_np_max_abs(operand) for operand in operands):
                offenders.append(f"{path_name}:{node.lineno}:direct-np-max-abs-threshold")
    return offenders


def check_audit_rejects_unsafe_predicate_shapes() -> None:
    bad_source = """
import numpy as np

def assert_near_integer(value, expected, tol):
    if abs(value - expected) > tol:
        raise AssertionError("bad")

def assert_leq(actual, bound):
    if actual > bound:
        raise AssertionError("bad")

def check_direct_array(actual, expected):
    if np.max(np.abs(actual - expected)) > 1.0e-12:
        raise AssertionError("bad")
"""
    offenders = unsafe_numeric_predicate_offenders("sample.py", bad_source)
    expected = {
        "sample.py:4:assert_near_integer",
        "sample.py:8:assert_leq",
        "sample.py:13:direct-np-max-abs-threshold",
    }
    missing = expected.difference(offenders)
    if missing:
        raise AssertionError(f"audit missed unsafe predicate samples: {sorted(missing)!r}")


def check_no_legacy_nan_accepting_helpers() -> None:
    offenders: list[str] = []
    root = Path(__file__).resolve().parent
    for path in sorted(root.glob("*.py")):
        if path.name in {"check_utils.py", "check_utils_checks.py"}:
            continue
        text = path.read_text()
        offenders.extend(unsafe_numeric_predicate_offenders(path.name, text))
    if offenders:
        raise AssertionError("NaN-accepting numerical predicates remain: " + ", ".join(offenders))


def main() -> None:
    check_scalar_nonfinite_rejection()
    check_scalar_finite_tolerance()
    check_array_nonfinite_rejection()
    check_array_finite_tolerance()
    check_bound_nonfinite_rejection()
    check_audit_rejects_unsafe_predicate_shapes()
    check_no_legacy_nan_accepting_helpers()
    print("All calculation assertion utility checks passed.")


if __name__ == "__main__":
    main()
