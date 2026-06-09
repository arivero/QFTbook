#!/usr/bin/env python3
"""Finite combinatorial checks for the BPHZ forest formula.

Evidence contract.

Target claims:
- The Bogoliubov preparation recursion expands to Zimmermann's forest formula
  in finite nested, disjoint, and overlapping subdivergence posets.
- Finite forest algebra and one-scale Taylor counting do not prove the uniform
  Hepp-Zimmermann sector estimate.

Independent construction:
- The recursion is built directly from spinneys and counterterm appending,
  then compared with an independently enumerated compatible-forest sum.
- Negative controls use finite dyadic shell sums and a two-loop routing matrix
  to separate one-scale decay and global loop coordinates from a true
  multiscale sector estimate.

Imported assumptions:
- The Hepp-Zimmermann analytic theorem supplies sector charts, adapted loop
  bases, uniform denominator comparisons, simultaneous subgraph/quotient
  exponents, and bounds for extra global forest terms.

Negative controls:
- A dyadic model with one decaying scale but an omitted quotient exponent grows
  with the second cutoff, while the full product-decay model stays bounded.
- The line variables q1=l1+l2 and q2=l1-l2 share both original loop variables,
  so disjoint branch estimates require an adapted basis rather than a naive
  factorization in the original routing.

Scope boundary:
- No loop integration, sector partition, Jacobian estimate, or uniform
  analytic majorant is proved here.

The manuscript proves Zimmermann's forest formula from the Bogoliubov
preparation recursion.  These checks verify the finite poset algebra in small
models: nested subdivergences, disjoint subdivergences, and overlapping
subdivergences.  No loop integration is performed here.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product


Term = tuple[str, ...]
Expansion = dict[Term, int]


class DivergencePoset:
    def __init__(self, labels: list[str], parent: dict[str, str | None]):
        self.labels = labels
        self.parent = parent
        self.children = {label: [] for label in labels}
        for label, par in parent.items():
            if par is not None:
                self.children[par].append(label)

    def is_ancestor(self, small: str, large: str) -> bool:
        current = self.parent[small]
        while current is not None:
            if current == large:
                return True
            current = self.parent[current]
        return False

    def compatible(self, left: str, right: str) -> bool:
        return (
            self.is_ancestor(left, right)
            or self.is_ancestor(right, left)
            or self.disjoint(left, right)
        )

    def disjoint(self, left: str, right: str) -> bool:
        return not self.is_ancestor(left, right) and not self.is_ancestor(right, left)

    def proper_subgraphs(self, graph: str) -> list[str]:
        return [label for label in self.labels if self.is_ancestor(label, graph)]

    def spinneys(self, graph: str) -> list[tuple[str, ...]]:
        proper = self.proper_subgraphs(graph)
        out: list[tuple[str, ...]] = [()]
        for size in range(1, len(proper) + 1):
            for subset in combinations(proper, size):
                if all(self.disjoint(a, b) for a, b in combinations(subset, 2)):
                    out.append(tuple(sorted(subset, key=self.labels.index)))
        return out

    def forests(self, graph: str) -> list[tuple[str, ...]]:
        candidates = self.proper_subgraphs(graph) + [graph]
        out: list[tuple[str, ...]] = [()]
        for size in range(1, len(candidates) + 1):
            for subset in combinations(candidates, size):
                if all(self.compatible(a, b) for a, b in combinations(subset, 2)):
                    out.append(tuple(sorted(subset, key=self.depth_then_order)))
        return out

    def depth_then_order(self, label: str) -> tuple[int, int]:
        depth = 0
        current = self.parent[label]
        while current is not None:
            depth += 1
            current = self.parent[current]
        # Larger depth means smaller/nested deeper graph, so it acts earlier.
        return (-depth, self.labels.index(label))


def add_expansion(left: Expansion, right: Expansion, scale: int = 1) -> Expansion:
    out = dict(left)
    for term, coeff in right.items():
        out[term] = out.get(term, 0) + scale * coeff
        if out[term] == 0:
            del out[term]
    return out


def multiply_expansions(left: Expansion, right: Expansion) -> Expansion:
    out: Expansion = {}
    for left_term, left_coeff in left.items():
        for right_term, right_coeff in right.items():
            term = left_term + right_term
            out[term] = out.get(term, 0) + left_coeff * right_coeff
    return {term: coeff for term, coeff in out.items() if coeff}


def append_operator(expansion: Expansion, label: str, scale: int) -> Expansion:
    return {term + (label,): scale * coeff for term, coeff in expansion.items()}


def bogoliubov_prepared(poset: DivergencePoset, graph: str) -> Expansion:
    prepared: Expansion = {(): 1}
    for spinney in poset.spinneys(graph):
        if not spinney:
            continue
        product_expansion: Expansion = {(): 1}
        for subgraph in spinney:
            product_expansion = multiply_expansions(
                product_expansion,
                bogoliubov_counterterm(poset, subgraph),
            )
        prepared = add_expansion(prepared, product_expansion)
    return prepared


def bogoliubov_counterterm(poset: DivergencePoset, graph: str) -> Expansion:
    return append_operator(bogoliubov_prepared(poset, graph), graph, -1)


def bogoliubov_r_operation(poset: DivergencePoset, graph: str) -> Expansion:
    prepared = bogoliubov_prepared(poset, graph)
    return add_expansion(prepared, append_operator(prepared, graph, -1))


def forest_formula(poset: DivergencePoset, graph: str) -> Expansion:
    out: Expansion = {}
    for forest in poset.forests(graph):
        sign = -1 if len(forest) % 2 else 1
        out[forest] = out.get(forest, 0) + sign
    return {term: coeff for term, coeff in out.items() if coeff}


def assert_equal(name: str, actual: Expansion, expected: Expansion) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def check_case(name: str, labels: list[str], parent: dict[str, str | None], graph: str) -> None:
    poset = DivergencePoset(labels, parent)
    recursive = bogoliubov_r_operation(poset, graph)
    forest = forest_formula(poset, graph)
    assert_equal(name, recursive, forest)


def check_nested_chain() -> None:
    check_case(
        "single nested subdivergence",
        labels=["gamma", "Gamma"],
        parent={"gamma": "Gamma", "Gamma": None},
        graph="Gamma",
    )
    check_case(
        "two nested subdivergences",
        labels=["gamma1", "gamma2", "Gamma"],
        parent={"gamma1": "gamma2", "gamma2": "Gamma", "Gamma": None},
        graph="Gamma",
    )


def check_overlapping_subgraphs() -> None:
    # The two proper subgraphs are modeled as siblings.  They are not nested,
    # and in this simplified poset they are declared incompatible by replacing
    # the disjoint test with a direct expected forest list.
    poset = DivergencePoset(
        labels=["gammaL", "gammaR", "Gamma"],
        parent={"gammaL": "Gamma", "gammaR": "Gamma", "Gamma": None},
    )

    def overlap_disjoint(left: str, right: str) -> bool:
        pair = {left, right}
        if pair == {"gammaL", "gammaR"}:
            return False
        return DivergencePoset.disjoint(poset, left, right)

    poset.disjoint = overlap_disjoint  # type: ignore[method-assign]
    expected = {
        (): 1,
        ("gammaL",): -1,
        ("gammaR",): -1,
        ("Gamma",): -1,
        ("gammaL", "Gamma"): 1,
        ("gammaR", "Gamma"): 1,
    }
    assert_equal("overlapping diamond forest list", forest_formula(poset, "Gamma"), expected)
    assert_equal(
        "overlapping diamond recursion",
        bogoliubov_r_operation(poset, "Gamma"),
        expected,
    )


def check_disjoint_subgraphs() -> None:
    poset = DivergencePoset(
        labels=["gammaL", "gammaR", "Gamma"],
        parent={"gammaL": "Gamma", "gammaR": "Gamma", "Gamma": None},
    )
    expected = {
        (): 1,
        ("gammaL",): -1,
        ("gammaR",): -1,
        ("Gamma",): -1,
        ("gammaL", "gammaR"): 1,
        ("gammaL", "Gamma"): 1,
        ("gammaR", "Gamma"): 1,
        ("gammaL", "gammaR", "Gamma"): -1,
    }
    assert_equal("disjoint subgraph forest list", forest_formula(poset, "Gamma"), expected)
    assert_equal(
        "disjoint subgraph recursion",
        bogoliubov_r_operation(poset, "Gamma"),
        expected,
    )


def check_counterterm_appends_largest_element() -> None:
    poset = DivergencePoset(
        labels=["a", "b", "Gamma"],
        parent={"a": "b", "b": "Gamma", "Gamma": None},
    )
    counterterm_b = bogoliubov_counterterm(poset, "b")
    expected = {("b",): -1, ("a", "b"): 1}
    assert_equal("counterterm appends largest element", counterterm_b, expected)


def check_all_subsets_for_nested_chain() -> None:
    poset = DivergencePoset(
        labels=["a", "b", "c", "Gamma"],
        parent={"a": "b", "b": "c", "c": "Gamma", "Gamma": None},
    )
    result = forest_formula(poset, "Gamma")
    expected: Expansion = {}
    chain = ["a", "b", "c", "Gamma"]
    for choices in product([False, True], repeat=len(chain)):
        term = tuple(label for label, keep in zip(chain, choices) if keep)
        expected[term] = -1 if len(term) % 2 else 1
    assert_equal("nested chain produces every subset", result, expected)


def check_one_scale_decay_does_not_imply_sector_product_bound() -> None:
    def one_scale_decay(cutoff: int) -> Fraction:
        return sum(Fraction(1, 2**n) for n in range(1, cutoff + 1))

    def missing_quotient_decay(cutoff: int) -> Fraction:
        return sum(
            Fraction(1, 2**n)
            for n in range(1, cutoff + 1)
            for _m in range(1, cutoff + 1)
        )

    def product_decay(cutoff: int) -> Fraction:
        return sum(
            Fraction(1, 2 ** (n + m))
            for n in range(1, cutoff + 1)
            for m in range(1, cutoff + 1)
        )

    small_cutoff = 8
    large_cutoff = 16
    if one_scale_decay(large_cutoff) >= 1:
        raise AssertionError("one decaying dyadic scale should remain bounded")
    if product_decay(large_cutoff) >= 1:
        raise AssertionError("two decaying dyadic scales should remain bounded")
    if missing_quotient_decay(large_cutoff) <= 2 * missing_quotient_decay(small_cutoff):
        raise AssertionError(
            "omitting quotient decay should grow with the independent cutoff"
        )
    if missing_quotient_decay(large_cutoff) <= 8 * product_decay(large_cutoff):
        raise AssertionError(
            "one-scale decay alone should not mimic a sector product bound"
        )


def check_adapted_routing_is_extra_analytic_input() -> None:
    # A two-loop routing can make two line momenta share both original loops.
    # The change to line variables is invertible, but factorization is not
    # visible until an adapted coordinate choice has been made.
    line_from_loop = ((1, 1), (1, -1))
    determinant = (
        line_from_loop[0][0] * line_from_loop[1][1]
        - line_from_loop[0][1] * line_from_loop[1][0]
    )
    supports = [
        {index for index, coefficient in enumerate(row) if coefficient}
        for row in line_from_loop
    ]
    if determinant == 0:
        raise AssertionError("routing change should be an invertible linear map")
    if supports != [{0, 1}, {0, 1}]:
        raise AssertionError("both line variables should share both loop variables")
    if supports[0].isdisjoint(supports[1]):
        raise AssertionError("original routing should not already factor branches")


def main() -> None:
    check_nested_chain()
    check_disjoint_subgraphs()
    check_overlapping_subgraphs()
    check_counterterm_appends_largest_element()
    check_all_subsets_for_nested_chain()
    check_one_scale_decay_does_not_imply_sector_product_bound()
    check_adapted_routing_is_extra_analytic_input()
    print("All BPHZ forest-formula combinatorial checks passed.")


if __name__ == "__main__":
    main()
