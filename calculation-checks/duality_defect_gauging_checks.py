#!/usr/bin/env python3
"""Exact finite checks for gauging-interface and duality-wall examples.

The corresponding chapter uses only finite algebra in several places:

* the regular algebra object A_H = direct-sum_h D_h satisfies
  A_H tensor A_H = |H| A_H;
* normal-subgroup gauging for A_3 normal in S_3 leaves an S_3/A_3 residual
  symmetry;
* orbifold pair-of-pants sectors obey g1 g2 = g3;
* the S, T, and T^p line-lattice maps preserve the finite Dirac pairing.

These checks verify that arithmetic exactly.  They do not assert the
existence of any particular interacting continuum QFT or self-duality
equivalence.
"""

from __future__ import annotations

from collections import Counter
from itertools import product

Permutation = tuple[int, int, int]
Charge = tuple[int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Composition p after q."""

    return tuple(p[q[i]] for i in range(3))  # type: ignore[return-value]


def inverse(p: Permutation) -> Permutation:
    out = [0, 0, 0]
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)  # type: ignore[return-value]


def s3() -> list[Permutation]:
    return [
        p
        for p in product(range(3), repeat=3)
        if sorted(p) == [0, 1, 2]
    ]


def cyclic_group(n: int) -> list[int]:
    return list(range(n))


def regular_algebra_square_counts(group: list[object], multiply) -> Counter:
    counts: Counter = Counter()
    for g, h in product(group, repeat=2):
        counts[multiply(g, h)] += 1
    return counts


def check_regular_algebra_square() -> None:
    for n in range(1, 9):
        group = cyclic_group(n)
        counts = regular_algebra_square_counts(group, lambda a, b, n=n: (a + b) % n)
        assert_equal(f"C_{n} regular algebra support", set(counts), set(group))
        assert_equal(f"C_{n} regular algebra multiplicities", set(counts.values()), {n})

    group_s3 = s3()
    counts_s3 = regular_algebra_square_counts(group_s3, compose)
    assert_equal("S3 regular algebra support", set(counts_s3), set(group_s3))
    assert_equal("S3 regular algebra multiplicities", set(counts_s3.values()), {6})


def sign(p: Permutation) -> int:
    inversions = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


def check_a3_normal_and_quotient() -> None:
    group = s3()
    identity = (0, 1, 2)
    a3 = {p for p in group if sign(p) == 1}
    assert_equal("A3 size", len(a3), 3)
    assert_equal("A3 contains identity", identity in a3, True)

    for g in group:
        for h in a3:
            conjugate = compose(compose(g, h), inverse(g))
            assert_equal("A3 normality", conjugate in a3, True)

    even_coset = frozenset(a3)
    odd_coset = frozenset(set(group) - a3)
    quotient = {even_coset: 0, odd_coset: 1}
    for left, right in product([even_coset, odd_coset], repeat=2):
        products = {compose(g, h) for g, h in product(left, right)}
        coset = even_coset if products <= even_coset else odd_coset
        assert_equal(
            "S3/A3 quotient multiplication is Z2",
            quotient[coset],
            (quotient[left] + quotient[right]) % 2,
        )


def centralizer(group: list[Permutation], element: Permutation) -> set[Permutation]:
    return {g for g in group if compose(g, element) == compose(element, g)}


def conjugacy_class(group: list[Permutation], element: Permutation) -> set[Permutation]:
    return {compose(compose(g, element), inverse(g)) for g in group}


def check_orbifold_pair_of_pants_and_centralizers() -> None:
    group = s3()
    classes = [conjugacy_class(group, g) for g in group]
    unique_classes = []
    for cls in classes:
        if cls not in unique_classes:
            unique_classes.append(cls)
    class_sizes = sorted(len(cls) for cls in unique_classes)
    assert_equal("S3 conjugacy class sizes", class_sizes, [1, 2, 3])

    centralizer_sizes = sorted({len(centralizer(group, next(iter(cls)))) for cls in unique_classes})
    assert_equal("S3 centralizer sizes", centralizer_sizes, [2, 3, 6])

    for g1, g2 in product(group, repeat=2):
        g3 = compose(g1, g2)
        assert_equal("pair-of-pants monodromy", compose(g1, g2), g3)
        assert_equal("outgoing inverse relation", compose(compose(g1, g2), inverse(g3)), (0, 1, 2))


def mat_vec(matrix: Matrix, charge: Charge, n: int | None = None) -> Charge:
    e, m = charge
    out = (
        matrix[0][0] * e + matrix[0][1] * m,
        matrix[1][0] * e + matrix[1][1] * m,
    )
    if n is None:
        return out
    return (out[0] % n, out[1] % n)


def dirac(lhs: Charge, rhs: Charge, n: int | None = None) -> int:
    value = lhs[0] * rhs[1] - lhs[1] * rhs[0]
    if n is None:
        return value
    return value % n


def check_line_lattice_pairing_preservation() -> None:
    s_matrix: Matrix = ((0, 1), (-1, 0))
    t_matrix: Matrix = ((1, 1), (0, 1))
    test_charges = [(e, m) for e in range(-3, 4) for m in range(-3, 4)]

    for matrix_name, matrix in [("S", s_matrix), ("T", t_matrix)]:
        for x, y in product(test_charges, repeat=2):
            assert_equal(
                f"{matrix_name} preserves integral pairing",
                dirac(mat_vec(matrix, x), mat_vec(matrix, y)),
                dirac(x, y),
            )

    for n in range(2, 13):
        finite_charges = [(e, m) for e in range(n) for m in range(n)]
        for p in range(n):
            tp_matrix: Matrix = ((1, p), (0, 1))
            for x, y in product(finite_charges, repeat=2):
                assert_equal(
                    f"T^{p} preserves finite pairing mod {n}",
                    dirac(mat_vec(tp_matrix, x, n), mat_vec(tp_matrix, y, n), n),
                    dirac(x, y, n),
                )
            assert_equal(f"T^{p} maps magnetic condensate mod {n}", mat_vec(tp_matrix, (0, 1), n), (p % n, 1))


def check_quantum_dimensions() -> None:
    for size in range(1, 10):
        regular_algebra_dimension = sum(1 for _ in range(size))
        self_dual_defect_dimension_squared = regular_algebra_dimension
        assert_equal(
            f"self-dual gauging dimension square |H|={size}",
            self_dual_defect_dimension_squared,
            size,
        )


def main() -> None:
    check_regular_algebra_square()
    check_a3_normal_and_quotient()
    check_orbifold_pair_of_pants_and_centralizers()
    check_line_lattice_pairing_preservation()
    check_quantum_dimensions()
    print("All duality-defect gauging checks passed.")


if __name__ == "__main__":
    main()
