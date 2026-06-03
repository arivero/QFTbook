#!/usr/bin/env python3
"""Regression tests for finite-aware numerical calculation assertions."""

from __future__ import annotations

import ast
import math
from pathlib import Path

import numpy as np

from check_utils import assert_array_close, assert_close, assert_geq, assert_gt, assert_leq, assert_lt


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

    for value in (math.nan, math.inf, -math.inf):
        expect_failure(
            f"lower bound actual nonfinite {value!r}",
            lambda value=value: assert_geq("lower bound actual nonfinite", value, 0.0),
        )
        expect_failure(
            f"lower bound target nonfinite {value!r}",
            lambda value=value: assert_geq("lower bound target nonfinite", 1.0, value),
        )
    expect_failure(
        "lower bound tolerance nonfinite",
        lambda: assert_geq("lower bound tolerance nonfinite", 1.0, 0.0, tol=math.inf),
    )
    expect_failure(
        "lower bound excessive finite defect",
        lambda: assert_geq("lower bound excessive finite defect", 1.0 - 2.0e-12, 1.0, tol=1.0e-12),
    )
    assert_geq("lower bound finite tolerance", 1.0 - 5.0e-13, 1.0, tol=1.0e-12)
    for value in (math.nan, math.inf, -math.inf):
        expect_failure(
            f"strict lower actual nonfinite {value!r}",
            lambda value=value: assert_gt("strict lower actual nonfinite", value, 0.0),
        )
        expect_failure(
            f"strict lower target nonfinite {value!r}",
            lambda value=value: assert_gt("strict lower target nonfinite", 1.0, value),
        )
    expect_failure(
        "strict lower equality",
        lambda: assert_gt("strict lower equality", 1.0, 1.0),
    )
    assert_gt("strict lower finite", 2.0, 1.0)


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


def _contains_float_like_call(node: ast.AST) -> bool:
    return _contains_call(
        node,
        {
            "abs",
            "math.fabs",
            "math.exp",
            "math.sqrt",
            "cmath.exp",
            "float",
            "np.abs",
            "numpy.abs",
            "np.max",
            "numpy.max",
            "np.min",
            "numpy.min",
            "np.sqrt",
            "numpy.sqrt",
            "np.exp",
            "numpy.exp",
            "np.linalg.det",
            "numpy.linalg.det",
            "np.linalg.eigvalsh",
            "numpy.linalg.eigvalsh",
            "np.linalg.norm",
            "numpy.linalg.norm",
        },
    )


def _function_candidate(node: ast.FunctionDef) -> bool:
    return node.name.startswith(("check_", "assert_", "_assert_", "require_"))


def _helper_like_function(node: ast.FunctionDef) -> bool:
    argument_names = {argument.arg for argument in node.args.args}
    threshold_names = {"actual", "bound", "expected", "got", "left", "right", "tol", "value"}
    return node.name.startswith(("assert_", "_assert_", "require_")) or bool(
        argument_names.intersection(threshold_names)
    )


def _body_raises_assertion(body: list[ast.stmt]) -> bool:
    for statement in body:
        if isinstance(statement, ast.Raise):
            return True
        if isinstance(statement, ast.If) and _body_raises_assertion(statement.body):
            return True
    return False


def _comparisons_protected_by_not(node: ast.AST) -> set[int]:
    protected: set[int] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.UnaryOp) and isinstance(child.op, ast.Not):
            protected.update(
                id(compare)
                for compare in ast.walk(child.operand)
                if isinstance(compare, ast.Compare)
            )
    return protected


def _comparison_names(node: ast.Compare) -> set[str]:
    result: set[str] = set()
    for operand in [node.left, *node.comparators]:
        result.update(child.id for child in ast.walk(operand) if isinstance(child, ast.Name))
    return result


def _nan_false_failure_compare(node: ast.Compare, function_node: ast.FunctionDef) -> bool:
    if not any(isinstance(operator, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for operator in node.ops):
        return False
    operands = [node.left, *node.comparators]
    if any(_contains_float_like_call(operand) or _contains_np_max_abs(operand) for operand in operands):
        return True
    if _helper_like_function(function_node):
        threshold_names = {"actual", "bound", "expected", "got", "left", "right", "tol", "value"}
        return bool(_comparison_names(node).intersection(threshold_names))
    return False


def _has_nan_false_failure_predicate(node: ast.FunctionDef) -> bool:
    for child in ast.walk(node):
        if not isinstance(child, ast.If) or not _body_raises_assertion(child.body):
            continue
        protected = _comparisons_protected_by_not(child.test)
        for compare in ast.walk(child.test):
            if (
                isinstance(compare, ast.Compare)
                and id(compare) not in protected
                and _nan_false_failure_compare(compare, node)
            ):
                return True
    return False


def _has_explicit_finiteness_guard(segment: str) -> bool:
    return "isfinite" in segment or "is_finite" in segment or "assert_finite" in segment


def unsafe_numeric_predicate_offenders(path_name: str, text: str) -> list[str]:
    offenders: list[str] = []
    tree = ast.parse(text)
    lines = text.splitlines(True)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and _function_candidate(node):
            segment = "".join(lines[node.lineno - 1 : node.end_lineno])
            if _has_nan_false_failure_predicate(node) and not _has_explicit_finiteness_guard(segment):
                offenders.append(f"{path_name}:{node.lineno}:{node.name}")
        if isinstance(node, ast.Compare):
            operands = [node.left, *node.comparators]
            if any(_contains_np_max_abs(operand) for operand in operands):
                offenders.append(f"{path_name}:{node.lineno}:direct-np-max-abs-threshold")
    return offenders


def check_audit_rejects_unsafe_predicate_shapes() -> None:
    bad_source = """
import numpy as np

def check_value(value, tol):
    if abs(value) > tol:
        raise AssertionError("bad")

def check_budget(actual, bound):
    if actual > bound:
        raise AssertionError("bad")

def check_bad_case(actual, bound):
    if actual <= bound:
        raise AssertionError("bad")

def check_norm(actual):
    if np.linalg.norm(actual) > 1e-12:
        raise AssertionError("bad")

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
        "sample.py:4:check_value",
        "sample.py:8:check_budget",
        "sample.py:12:check_bad_case",
        "sample.py:16:check_norm",
        "sample.py:20:assert_near_integer",
        "sample.py:24:assert_leq",
        "sample.py:28:check_direct_array",
        "sample.py:29:direct-np-max-abs-threshold",
    }
    missing = expected.difference(offenders)
    if missing:
        raise AssertionError(f"audit missed unsafe predicate samples: {sorted(missing)!r}")

    safe_source = """
def check_safe_not_predicate(value, bound):
    if not value < bound:
        raise AssertionError("safe fail on nan")

def assert_guarded(actual, bound):
    assert_finite("actual", actual)
    if actual > bound:
        raise AssertionError("guarded")
"""
    safe_offenders = unsafe_numeric_predicate_offenders("safe.py", safe_source)
    if safe_offenders:
        raise AssertionError(f"audit rejected safe predicate samples: {safe_offenders!r}")


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
