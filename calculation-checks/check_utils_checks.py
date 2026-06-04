#!/usr/bin/env python3
"""Regression tests for finite-aware numerical calculation assertions."""

from __future__ import annotations

import ast
import math
from pathlib import Path

import numpy as np

from check_utils import (
    assert_array_close,
    assert_close,
    assert_finite_array,
    assert_geq,
    assert_gt,
    assert_leq,
    assert_lt,
    finite_matmul,
    finite_max_abs,
)


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


def check_finite_matrix_helpers() -> None:
    left = np.array([[1.0, 2.0], [3.0, 4.0]])
    right = np.array([[5.0, 6.0], [7.0, 8.0]])
    assert_array_close("finite matmul matrix", finite_matmul("finite matmul matrix", left, right), left @ right)
    assert_array_close("finite matmul vector", finite_matmul("finite matmul vector", left, right[:, 0]), left @ right[:, 0])
    assert_close("finite max abs", finite_max_abs("finite max abs", np.array([3.0 + 4.0j, -2.0])), 5.0)
    expect_failure(
        "finite array rejects input nonfinite",
        lambda: assert_finite_array("finite array rejects input nonfinite", np.array([1.0, math.inf])),
    )
    bad = np.eye(2)
    bad[0, 1] = math.nan
    expect_failure("finite matmul rejects nonfinite input", lambda: finite_matmul("bad input", bad, np.eye(2)))
    huge = np.array([[1.0e308, 1.0e308], [1.0e308, 1.0e308]])
    expect_failure("finite matmul rejects nonfinite output", lambda: finite_matmul("bad output", huge, huge))
    expect_failure("finite max abs rejects nonfinite", lambda: finite_max_abs("bad max", np.array([1.0, math.nan])))


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
    ignored_names = {
        "abs",
        "bool",
        "cmath",
        "complex",
        "float",
        "int",
        "math",
        "mp",
        "np",
        "numpy",
        "sp",
    }
    result: set[str] = set()
    for operand in [node.left, *node.comparators]:
        result.update(child.id for child in ast.walk(operand) if isinstance(child, ast.Name))
    return result.difference(ignored_names)


def _comparison_required_guards(node: ast.Compare, function_node: ast.FunctionDef) -> set[str]:
    if not any(isinstance(operator, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for operator in node.ops):
        return set()
    operands = [node.left, *node.comparators]
    names = _comparison_names(node)
    if any(_contains_float_like_call(operand) or _contains_np_max_abs(operand) for operand in operands):
        return names
    if _helper_like_function(function_node):
        threshold_names = {"actual", "bound", "expected", "got", "left", "right", "tol", "value"}
        return names.intersection(threshold_names)
    return set()


def _finite_guard_call_names(node: ast.AST) -> set[str]:
    if not isinstance(node, ast.Call):
        return set()
    call_name = _call_name(node.func)
    if (
        call_name in {"math.isfinite", "mp.isfinite", "np.isfinite", "numpy.isfinite", "isfinite", "is_finite"}
        and node.args
    ):
        argument = node.args[0]
        if isinstance(argument, ast.Name):
            return {argument.id}
        return set()
    if call_name in {"np.all", "numpy.all", "all", "bool"} and node.args:
        return _finite_guard_truth_names(node.args[0])
    if isinstance(node.func, ast.Attribute) and node.func.attr == "all":
        return _finite_guard_truth_names(node.func.value)
    return set()


def _finite_guard_truth_names(node: ast.AST) -> set[str]:
    call_names = _finite_guard_call_names(node)
    if call_names:
        return call_names
    if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And):
        names: set[str] = set()
        for value in node.values:
            names.update(_finite_guard_truth_names(value))
        return names
    return set()


def _finite_guard_false_names(node: ast.AST) -> set[str]:
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return _finite_guard_truth_names(node.operand)
    if (
        isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.IsNot)
        and len(node.comparators) == 1
        and isinstance(node.comparators[0], ast.Constant)
        and node.comparators[0].value is True
        and isinstance(node.left, ast.Attribute)
        and node.left.attr == "is_finite"
        and isinstance(node.left.value, ast.Name)
    ):
        return {node.left.value.id}
    if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
        names: set[str] = set()
        for value in node.values:
            names.update(_finite_guard_false_names(value))
        return names
    return set()


def _body_unconditionally_raises_assertion(body: list[ast.stmt]) -> bool:
    for statement in body:
        if isinstance(statement, ast.Raise):
            return True
        if (
            isinstance(statement, ast.If)
            and _body_unconditionally_raises_assertion(statement.body)
            and _body_unconditionally_raises_assertion(statement.orelse)
        ):
            return True
    return False


def _statement_explicit_guard_names(statement: ast.stmt) -> set[str]:
    if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
        call = statement.value
        call_name = _call_name(call.func)
        if call_name in {
            "assert_finite",
            "_assert_finite",
            "check_utils.assert_finite",
            "assert_finite_array",
            "_assert_finite_array",
        }:
            guarded_argument = call.args[1] if len(call.args) >= 2 else call.args[0] if call.args else None
            if isinstance(guarded_argument, ast.Name):
                return {guarded_argument.id}
        return set()
    if isinstance(statement, ast.Assign) and isinstance(statement.value, ast.Call):
        call_name = _call_name(statement.value.func)
        if call_name in {"assert_finite_array", "_assert_finite_array", "check_utils.assert_finite_array"}:
            return {target.id for target in statement.targets if isinstance(target, ast.Name)}
    if isinstance(statement, ast.Assert):
        return _finite_guard_truth_names(statement.test)
    if isinstance(statement, ast.If) and _body_unconditionally_raises_assertion(statement.body):
        return _finite_guard_false_names(statement.test)
    return set()


def _audit_unsafe_numeric_predicates(
    path_name: str,
    function_node: ast.FunctionDef,
    statements: list[ast.stmt],
    guarded_names: set[str],
    offenders: list[str],
) -> set[str]:
    active_guards = set(guarded_names)
    for statement in statements:
        if isinstance(statement, ast.If):
            protected = _comparisons_protected_by_not(statement.test)
            same_test_guards = active_guards.union(_finite_guard_false_names(statement.test))
            if _body_raises_assertion(statement.body):
                for compare in ast.walk(statement.test):
                    if not isinstance(compare, ast.Compare) or id(compare) in protected:
                        continue
                    required = _comparison_required_guards(compare, function_node)
                    missing = required.difference(same_test_guards)
                    if missing:
                        offenders.append(
                            f"{path_name}:{compare.lineno}:{function_node.name}:"
                            f"unguarded-{','.join(sorted(missing))}"
                        )

            body_guards = active_guards.union(_finite_guard_truth_names(statement.test))
            else_guards = active_guards.union(_finite_guard_false_names(statement.test))
            _audit_unsafe_numeric_predicates(path_name, function_node, statement.body, body_guards, offenders)
            _audit_unsafe_numeric_predicates(path_name, function_node, statement.orelse, else_guards, offenders)

            if _body_unconditionally_raises_assertion(statement.body):
                active_guards.update(_finite_guard_false_names(statement.test))
            elif statement.orelse and _body_unconditionally_raises_assertion(statement.orelse):
                active_guards.update(_finite_guard_truth_names(statement.test))
            continue

        if isinstance(statement, (ast.For, ast.While, ast.With, ast.Try)):
            for body_name in ("body", "orelse", "finalbody"):
                child_body = getattr(statement, body_name, [])
                if child_body:
                    _audit_unsafe_numeric_predicates(path_name, function_node, child_body, active_guards, offenders)
            for handler in getattr(statement, "handlers", []):
                _audit_unsafe_numeric_predicates(path_name, function_node, handler.body, active_guards, offenders)
            continue

        active_guards.update(_statement_explicit_guard_names(statement))
    return active_guards


def unsafe_numeric_predicate_offenders(path_name: str, text: str) -> list[str]:
    offenders: list[str] = []
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and _function_candidate(node):
            _audit_unsafe_numeric_predicates(path_name, node, node.body, set(), offenders)
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

def check_bad_guarded_only_tol(actual, expected, tol):
    assert_finite("tol", tol)
    if abs(actual - expected) > tol:
        raise AssertionError("bad")

def check_bad_guarded_only_actual(actual, expected, tol):
    if not isfinite(actual):
        raise AssertionError("bad")
    if abs(actual - expected) > tol:
        raise AssertionError("bad")

def check_bad_non_dominating_guard(actual, bound):
    if isfinite(actual):
        pass
    if actual > bound:
        raise AssertionError("bad")

def check_bad_docstring_guard_mention(actual, bound):
    \"\"\"A textual assert_finite mention is not a semantic guard.\"\"\"
    if actual > bound:
        raise AssertionError("bad")

def check_bad_comment_guard_mention(actual, bound):
    # isfinite(actual) is only a comment here.
    if actual > bound:
        raise AssertionError("bad")
"""
    offenders = unsafe_numeric_predicate_offenders("sample.py", bad_source)
    expected_function_names = {
        "check_value",
        "check_budget",
        "check_bad_case",
        "check_norm",
        "assert_near_integer",
        "assert_leq",
        "check_direct_array",
        "check_bad_guarded_only_tol",
        "check_bad_guarded_only_actual",
        "check_bad_non_dominating_guard",
        "check_bad_docstring_guard_mention",
        "check_bad_comment_guard_mention",
    }
    missing = {
        name
        for name in expected_function_names
        if not any(f":{name}:" in offender for offender in offenders)
    }
    if missing:
        raise AssertionError(f"audit missed unsafe predicate samples: {sorted(missing)!r}")

    safe_source = """
def check_safe_not_predicate(value, bound):
    if not value < bound:
        raise AssertionError("safe fail on nan")

def assert_guarded(actual, bound):
    assert_finite("actual", actual)
    assert_finite("bound", bound)
    if actual > bound:
        raise AssertionError("guarded")

def assert_guarded_by_rejecting_branch(actual, bound):
    if not isfinite(actual) or not isfinite(bound):
        raise AssertionError("nonfinite")
    if actual > bound:
        raise AssertionError("guarded")

def check_exact_integer_predicate(count, target):
    if count > target:
        raise AssertionError("integer count exceeds target")
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
