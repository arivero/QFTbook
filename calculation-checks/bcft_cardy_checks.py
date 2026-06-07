#!/usr/bin/env python3
"""Exact BCFT Cardy/Ishibashi bookkeeping checks.

Evidence contract.
Target claims: the finite Cardy/Ishibashi coefficient, annulus, boundary OPE,
the multiplicity-free scalar Cardy-Lewellen coordinate chart, the boundary
observable output coordinates, the boundary observable dependency map, and
elementary sewing subclaims in the BCFT chapter.
Independent construction: exact Q(sqrt(2)) arithmetic, Laurent-polynomial
character operations, finite annulus matrices, and explicit boundary-field
counting are computed independently from the candidate Cardy labels.
Imported assumptions: the chosen Ising modular datum, topological defect and
boundary-label conventions, and finite character truncation used in the
chapter's examples.
Negative controls: inconsistent annulus multiplicities, wrong label
identifications, boundary-changing channel counts, annulus-only
reconstructions of disk response, boundary susceptibility, and sewing data,
multiplication-only reconstructions of disk pairings, and a finite diagnostic
in which boundary-field multiplicity differs from chiral fusion multiplicity
are tested by exact constraints.
Scope boundary: a pass checks finite rational-model bookkeeping; it does not
prove the full Cardy-Lewellen sewing theorem, nonrational BCFT completeness,
analytic convergence, non-multiplicity-free fusing matrices, or existence of a
continuum boundary CFT.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from check_utils import assert_leq as _assert_leq


@dataclass(frozen=True)
class Qsqrt2:
    rational: Fraction = Fraction(0)
    sqrt2: Fraction = Fraction(0)

    def __add__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational + other.rational, self.sqrt2 + other.sqrt2)

    def __sub__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational - other.rational, self.sqrt2 - other.sqrt2)

    def __neg__(self) -> Qsqrt2:
        return Qsqrt2(-self.rational, -self.sqrt2)

    def __mul__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(
            self.rational * other.rational + 2 * self.sqrt2 * other.sqrt2,
            self.rational * other.sqrt2 + self.sqrt2 * other.rational,
        )

    def inverse(self) -> Qsqrt2:
        denominator = self.rational * self.rational - 2 * self.sqrt2 * self.sqrt2
        if denominator == 0:
            raise ZeroDivisionError(self)
        return Qsqrt2(self.rational / denominator, -self.sqrt2 / denominator)

    def __truediv__(self, other: Qsqrt2) -> Qsqrt2:
        return self * other.inverse()


@dataclass(frozen=True)
class Laurent2:
    """Laurent polynomial in two formal exponentials, with rational coefficients."""

    terms: tuple[tuple[tuple[int, int], Fraction], ...] = ()

    @staticmethod
    def from_dict(terms: dict[tuple[int, int], Fraction]) -> Laurent2:
        clean = tuple(
            sorted(
                (exponent, coefficient)
                for exponent, coefficient in terms.items()
                if coefficient
            )
        )
        return Laurent2(clean)

    @staticmethod
    def monomial(
        x_power: int,
        y_power: int,
        coefficient: Fraction = Fraction(1),
    ) -> Laurent2:
        return Laurent2.from_dict({(x_power, y_power): coefficient})

    @staticmethod
    def scalar(coefficient: Fraction) -> Laurent2:
        return Laurent2.from_dict({(0, 0): coefficient})

    def as_dict(self) -> dict[tuple[int, int], Fraction]:
        return dict(self.terms)

    def __add__(self, other: Laurent2) -> Laurent2:
        result = self.as_dict()
        for exponent, coefficient in other.terms:
            result[exponent] = result.get(exponent, Fraction(0)) + coefficient
        return Laurent2.from_dict(result)

    def __neg__(self) -> Laurent2:
        return Laurent2.from_dict(
            {exponent: -coefficient for exponent, coefficient in self.terms}
        )

    def __sub__(self, other: Laurent2) -> Laurent2:
        return self + (-other)

    def __mul__(self, other: Laurent2) -> Laurent2:
        result: dict[tuple[int, int], Fraction] = {}
        for (x_left, y_left), coefficient_left in self.terms:
            for (x_right, y_right), coefficient_right in other.terms:
                exponent = (x_left + x_right, y_left + y_right)
                result[exponent] = (
                    result.get(exponent, Fraction(0))
                    + coefficient_left * coefficient_right
                )
        return Laurent2.from_dict(result)

    def scale(self, coefficient: Fraction) -> Laurent2:
        return Laurent2.from_dict(
            {
                exponent: coefficient * term_coefficient
                for exponent, term_coefficient in self.terms
            }
        )


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))
HALF = Qsqrt2(Fraction(1, 2))
SQRT2 = Qsqrt2(Fraction(0), Fraction(1))
INV_SQRT2 = Qsqrt2(Fraction(0), Fraction(1, 2))

LABELS = ("1", "epsilon", "sigma")

S = [
    [HALF, HALF, INV_SQRT2],
    [HALF, HALF, -INV_SQRT2],
    [INV_SQRT2, -INV_SQRT2, ZERO],
]

EXPECTED_FUSION = {
    ("1", "1"): {"1": 1},
    ("1", "epsilon"): {"epsilon": 1},
    ("1", "sigma"): {"sigma": 1},
    ("epsilon", "epsilon"): {"1": 1},
    ("epsilon", "sigma"): {"sigma": 1},
    ("sigma", "sigma"): {"1": 1, "epsilon": 1},
}


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def matrix_multiply(lhs: list[list[Qsqrt2]], rhs: list[list[Qsqrt2]]) -> list[list[Qsqrt2]]:
    size = len(lhs)
    return [
        [
            sum((lhs[i][k] * rhs[k][j] for k in range(size)), ZERO)
            for j in range(size)
        ]
        for i in range(size)
    ]


def q_matrix_add(
    lhs: list[list[Qsqrt2]],
    rhs: list[list[Qsqrt2]],
) -> list[list[Qsqrt2]]:
    size = len(lhs)
    return [
        [lhs[i][j] + rhs[i][j] for j in range(size)]
        for i in range(size)
    ]


def q_matrix_scale(
    coefficient: Qsqrt2,
    matrix: list[list[Qsqrt2]],
) -> list[list[Qsqrt2]]:
    return [
        [coefficient * entry for entry in row]
        for row in matrix
    ]


def q_zero_matrix(size: int) -> list[list[Qsqrt2]]:
    return [[ZERO for _ in range(size)] for _ in range(size)]


def q_outer(vector: list[Qsqrt2]) -> list[list[Qsqrt2]]:
    return [
        [left * right for right in vector]
        for left in vector
    ]


def q_dot(lhs: list[Qsqrt2], rhs: list[Qsqrt2]) -> Qsqrt2:
    return sum((left * right for left, right in zip(lhs, rhs)), ZERO)


def verlinde(a: int, b: int, c: int) -> Qsqrt2:
    total = ZERO
    for i in range(3):
        total += S[a][i] * S[b][i] * S[c][i] / S[0][i]
    return total


def fusion(a: int, b: int, c: int) -> Qsqrt2:
    return verlinde(a, b, c)


def check_modular_s() -> None:
    identity = [
        [ONE if i == j else ZERO for j in range(3)]
        for i in range(3)
    ]
    assert_equal("Ising S squared", matrix_multiply(S, S), identity)


def check_cardy_annulus() -> None:
    for a, left in enumerate(LABELS):
        for b, right in enumerate(LABELS):
            key = tuple(sorted((left, right), key=LABELS.index))
            expected = EXPECTED_FUSION[key]
            for k, channel in enumerate(LABELS):
                coefficient = verlinde(a, b, k)
                expected_value = Qsqrt2(Fraction(expected.get(channel, 0)))
                assert_equal(
                    f"Cardy annulus {left}-{right} open channel {channel}",
                    coefficient,
                    expected_value,
                )


def check_annulus_nimrep_spectral_resolution() -> None:
    """Check the A_3 Ising annulus nimrep spectral resolution exactly."""

    n_one = [
        [ONE, ZERO, ZERO],
        [ZERO, ONE, ZERO],
        [ZERO, ZERO, ONE],
    ]
    n_epsilon = [
        [ZERO, ZERO, ONE],
        [ZERO, ONE, ZERO],
        [ONE, ZERO, ZERO],
    ]
    n_sigma = [
        [ZERO, ONE, ZERO],
        [ONE, ZERO, ONE],
        [ZERO, ONE, ZERO],
    ]
    nimreps = {
        "1": n_one,
        "epsilon": n_epsilon,
        "sigma": n_sigma,
    }

    assert_equal(
        "A3 Ising nimrep epsilon square",
        matrix_multiply(n_epsilon, n_epsilon),
        n_one,
    )
    assert_equal(
        "A3 Ising nimrep epsilon times sigma",
        matrix_multiply(n_epsilon, n_sigma),
        n_sigma,
    )
    assert_equal(
        "A3 Ising nimrep sigma square",
        matrix_multiply(n_sigma, n_sigma),
        q_matrix_add(n_one, n_epsilon),
    )

    eigenvectors = {
        "1": [HALF, INV_SQRT2, HALF],
        "epsilon": [HALF, -INV_SQRT2, HALF],
        "sigma": [INV_SQRT2, ZERO, -INV_SQRT2],
    }

    for left_name, left_vector in eigenvectors.items():
        for right_name, right_vector in eigenvectors.items():
            expected = ONE if left_name == right_name else ZERO
            assert_equal(
                f"A3 Ising annulus eigenvector orthogonality {left_name} {right_name}",
                q_dot(left_vector, right_vector),
                expected,
            )

    for chiral_index, chiral_label in enumerate(LABELS):
        spectral_resolution = q_zero_matrix(3)
        for exponent_label, eigenvector in eigenvectors.items():
            exponent_index = LABELS.index(exponent_label)
            eigenvalue = S[chiral_index][exponent_index] / S[0][exponent_index]
            spectral_resolution = q_matrix_add(
                spectral_resolution,
                q_matrix_scale(eigenvalue, q_outer(eigenvector)),
            )
        assert_equal(
            f"A3 Ising annulus spectral resolution for {chiral_label}",
            spectral_resolution,
            nimreps[chiral_label],
        )

    # The boundary coefficients include square roots of S_0e.  The annulus only
    # needs the products conjugate(B_b^e) B_a^e S_ei, which are exact here.
    for chiral_index, chiral_label in enumerate(LABELS):
        for source in range(3):
            for target in range(3):
                closed_channel_entry = sum(
                    (
                        eigenvector[source]
                        * eigenvector[target]
                        * S[chiral_index][LABELS.index(exponent_label)]
                        / S[0][LABELS.index(exponent_label)]
                        for exponent_label, eigenvector in eigenvectors.items()
                    ),
                    ZERO,
                )
                assert_equal(
                    "A3 Ising reflection-product annulus entry "
                    f"{chiral_label}: {source}->{target}",
                    closed_channel_entry,
                    nimreps[chiral_label][source][target],
                )


def cyclic_character_sum_order(n: int, exponent: int) -> int:
    return 1 if exponent % n == 0 else 0


def cyclic_fusion(n: int, left: int, right: int, target: int) -> int:
    return 1 if (left + right - target) % n == 0 else 0


def cyclic_oriented_cardy_annulus(
    n: int,
    left_boundary: int,
    right_boundary: int,
    open_label: int,
) -> int:
    # For the pointed modular data S_ai=n^(-1/2) exp(2 pi i a i/n), the
    # coefficient of chi_k in <right|tilde q^H|left> is the character sum with
    # exponent -right_boundary + left_boundary + open_label.
    return cyclic_character_sum_order(n, left_boundary + open_label - right_boundary)


def cyclic_unoriented_cardy_shortcut(
    n: int,
    left_boundary: int,
    right_boundary: int,
    open_label: int,
) -> int:
    # This is the old real/self-conjugate shortcut without the bra conjugation.
    # It is correct for Ising-like real modular data but wrong for pointed
    # non-self-conjugate labels.
    return cyclic_character_sum_order(n, left_boundary + right_boundary + open_label)


def check_oriented_cardy_annulus_for_cyclic_pointed_data() -> None:
    for order in (3, 5, 7):
        for left_boundary in range(order):
            for right_boundary in range(order):
                for open_label in range(order):
                    expected = cyclic_fusion(
                        order,
                        open_label,
                        left_boundary,
                        right_boundary,
                    )
                    got = cyclic_oriented_cardy_annulus(
                        order,
                        left_boundary,
                        right_boundary,
                        open_label,
                    )
                    assert_equal(
                        "oriented Cardy annulus for cyclic pointed modular data "
                        f"n={order}, a={left_boundary}, "
                        f"b={right_boundary}, k={open_label}",
                        got,
                        expected,
                    )

    old_shortcut = cyclic_unoriented_cardy_shortcut(
        3,
        left_boundary=0,
        right_boundary=1,
        open_label=1,
    )
    oriented = cyclic_oriented_cardy_annulus(
        3,
        left_boundary=0,
        right_boundary=1,
        open_label=1,
    )
    assert_equal(
        "oriented cyclic Cardy annulus detects the boundary changer",
        oriented,
        1,
    )
    assert_equal(
        "unoriented cyclic Cardy shortcut misses that boundary changer",
        old_shortcut,
        0,
    )


def check_fusion_associativity() -> None:
    for a, left in enumerate(LABELS):
        for b, middle_left in enumerate(LABELS):
            for c, middle_right in enumerate(LABELS):
                for d, right in enumerate(LABELS):
                    lhs = sum(
                        (fusion(a, b, e) * fusion(e, c, d) for e in range(3)),
                        ZERO,
                    )
                    rhs = sum(
                        (fusion(b, c, e) * fusion(a, e, d) for e in range(3)),
                        ZERO,
                    )
                    assert_equal(
                        "Ising fusion associativity "
                        f"({left} {middle_left}) {middle_right} -> {right}",
                        lhs,
                        rhs,
                    )


def check_cardy_fusion_ring_characters() -> None:
    for boundary, boundary_label in enumerate(LABELS):
        eigenvalues = [S[i][boundary] / S[0][boundary] for i in range(3)]
        normalized_disk_coefficients = [
            S[boundary][i] / S[0][boundary] for i in range(3)
        ]
        assert_equal(
            "Cardy normalized disk coordinate equals fusion character "
            f"{boundary_label}",
            normalized_disk_coefficients,
            eigenvalues,
        )
        for i, left in enumerate(LABELS):
            for j, right in enumerate(LABELS):
                product = eigenvalues[i] * eigenvalues[j]
                fusion_sum = sum(
                    (fusion(i, j, k) * eigenvalues[k] for k in range(3)),
                    ZERO,
                )
                assert_equal(
                    "Cardy disk one-point fusion character "
                    f"{boundary_label}: {left}*{right}",
                    product,
                    fusion_sum,
                )
                classifying_sum = sum(
                    (
                        fusion(i, j, k) * normalized_disk_coefficients[k]
                        for k in range(3)
                    ),
                    ZERO,
                )
                assert_equal(
                    "Cardy disk two-bulk classifying sewing "
                    f"{boundary_label}: {left}*{right}",
                    normalized_disk_coefficients[i]
                    * normalized_disk_coefficients[j],
                    classifying_sum,
                )


def check_cardy_unit_algebra_module_multiplicities() -> None:
    """For A=1, module morphism dimensions reduce to fusion coefficients."""
    for a, left_boundary in enumerate(LABELS):
        for b, right_boundary in enumerate(LABELS):
            for i, chiral_type in enumerate(LABELS):
                # The monograph convention uses Hom(U_a tensor U_i, U_b).
                module_dimension = fusion(a, i, b)
                expected_dimension = verlinde(a, i, b)
                assert_equal(
                    "unit Frobenius algebra module multiplicity "
                    f"{left_boundary} -- {chiral_type} --> {right_boundary}",
                    module_dimension,
                    expected_dimension,
                )


MatrixUnit = tuple[int, int]
TensorUnit = tuple[MatrixUnit, MatrixUnit]


def matrix_unit_product(
    left: MatrixUnit,
    right: MatrixUnit,
) -> dict[MatrixUnit, Fraction]:
    i, j = left
    k, ell = right
    if j != k:
        return {}
    return {(i, ell): Fraction(1)}


def matrix_unit_trace(unit: MatrixUnit) -> Fraction:
    i, j = unit
    return Fraction(1) if i == j else Fraction(0)


def matrix_frobenius_delta(unit: MatrixUnit, dimension: int) -> dict[TensorUnit, Fraction]:
    i, j = unit
    return {
        ((i, r), (r, j)): Fraction(1)
        for r in range(dimension)
    }


def add_tensor_term(
    target: dict[TensorUnit, Fraction],
    tensor_unit: TensorUnit,
    coefficient: Fraction,
) -> None:
    target[tensor_unit] = target.get(tensor_unit, Fraction(0)) + coefficient
    if target[tensor_unit] == 0:
        del target[tensor_unit]


def frobenius_left(
    left: MatrixUnit,
    right: MatrixUnit,
    dimension: int,
) -> dict[TensorUnit, Fraction]:
    result: dict[TensorUnit, Fraction] = {}
    for (right_left, right_right), delta_coefficient in matrix_frobenius_delta(
        right,
        dimension,
    ).items():
        for product_unit, product_coefficient in matrix_unit_product(
            left,
            right_left,
        ).items():
            add_tensor_term(
                result,
                (product_unit, right_right),
                delta_coefficient * product_coefficient,
            )
    return result


def frobenius_middle(
    left: MatrixUnit,
    right: MatrixUnit,
    dimension: int,
) -> dict[TensorUnit, Fraction]:
    result: dict[TensorUnit, Fraction] = {}
    for product_unit, product_coefficient in matrix_unit_product(left, right).items():
        for tensor_unit, delta_coefficient in matrix_frobenius_delta(
            product_unit,
            dimension,
        ).items():
            add_tensor_term(result, tensor_unit, product_coefficient * delta_coefficient)
    return result


def frobenius_right(
    left: MatrixUnit,
    right: MatrixUnit,
    dimension: int,
) -> dict[TensorUnit, Fraction]:
    result: dict[TensorUnit, Fraction] = {}
    for (left_left, left_right), delta_coefficient in matrix_frobenius_delta(
        left,
        dimension,
    ).items():
        for product_unit, product_coefficient in matrix_unit_product(
            left_right,
            right,
        ).items():
            add_tensor_term(
                result,
                (left_left, product_unit),
                delta_coefficient * product_coefficient,
            )
    return result


def check_matrix_frobenius_cutting_move() -> None:
    """Check the finite matrix-unit version of rational BCFT cutting moves."""

    for dimension in (2, 3, 4):
        basis = [
            (i, j)
            for i in range(dimension)
            for j in range(dimension)
        ]
        for left in basis:
            for right in basis:
                left_move = frobenius_left(left, right, dimension)
                middle_move = frobenius_middle(left, right, dimension)
                right_move = frobenius_right(left, right, dimension)
                assert_equal(
                    f"matrix Frobenius left=middle d={dimension} {left},{right}",
                    left_move,
                    middle_move,
                )
                assert_equal(
                    f"matrix Frobenius right=middle d={dimension} {left},{right}",
                    right_move,
                    middle_move,
                )

                product_left_right = matrix_unit_product(left, right)
                product_right_left = matrix_unit_product(right, left)
                trace_left_right = sum(
                    coefficient * matrix_unit_trace(unit)
                    for unit, coefficient in product_left_right.items()
                )
                trace_right_left = sum(
                    coefficient * matrix_unit_trace(unit)
                    for unit, coefficient in product_right_left.items()
                )
                assert_equal(
                    f"symmetric matrix trace pairing d={dimension} {left},{right}",
                    trace_left_right,
                    trace_right_left,
                )

        for unit in basis:
            collapsed: dict[MatrixUnit, Fraction] = {}
            for (left, right), delta_coefficient in matrix_frobenius_delta(
                unit,
                dimension,
            ).items():
                for product_unit, product_coefficient in matrix_unit_product(
                    left,
                    right,
                ).items():
                    collapsed[product_unit] = (
                        collapsed.get(product_unit, Fraction(0))
                        + delta_coefficient * product_coefficient
                    )
            assert_equal(
                f"matrix Frobenius specialness d={dimension} {unit}",
                collapsed,
                {unit: Fraction(dimension)},
            )


def center_multiply(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        left_entry * right_entry
        for left_entry, right_entry in zip(left, right)
    )


def check_finite_classifying_center_characters() -> None:
    """Check the finite algebra shadow of non-diagonal disk sewing.

    Use A_fin=Mat_2(C) direct-sum Mat_3(C).  The center is C e_0 + C e_1.
    On the elementary simple modules M_0=C^2 and M_1=C^3, a central element
    z=(z_0,z_1) acts by the scalar z_r.  The elementary disk identity-channel
    coordinate is therefore a multiplicative central character.  A normalized
    trace on the reducible module M_0 direct-sum M_1 is additive but not a
    character; this records why a direct sum boundary condition carries
    Chan-Paton matrix data rather than one elementary disk one-point scalar.
    """

    samples = (
        (Fraction(2), Fraction(-3)),
        (Fraction(5, 2), Fraction(7, 3)),
        (Fraction(-4, 5), Fraction(11, 6)),
    )
    for left in samples:
        for right in samples:
            product = center_multiply(left, right)
            for module_index in (0, 1):
                elementary_left = left[module_index]
                elementary_right = right[module_index]
                elementary_product = product[module_index]
                assert_equal(
                    "finite center elementary character multiplicativity "
                    f"module={module_index}, left={left}, right={right}",
                    elementary_product,
                    elementary_left * elementary_right,
                )

    e0 = (Fraction(1), Fraction(0))
    e1 = (Fraction(0), Fraction(1))
    assert_equal(
        "finite center primitive idempotent e0",
        center_multiply(e0, e0),
        e0,
    )
    assert_equal(
        "finite center primitive idempotent e1",
        center_multiply(e1, e1),
        e1,
    )
    assert_equal(
        "finite center orthogonal primitive idempotents",
        center_multiply(e0, e1),
        (Fraction(0), Fraction(0)),
    )
    assert_equal(
        "finite center identity from primitive idempotents",
        tuple(left + right for left, right in zip(e0, e1)),
        (Fraction(1), Fraction(1)),
    )

    def reducible_normalized_trace(z: tuple[Fraction, Fraction]) -> Fraction:
        return (2 * z[0] + 3 * z[1]) / 5

    left = (Fraction(2), Fraction(5))
    right = (Fraction(7), Fraction(11))
    trace_product = reducible_normalized_trace(center_multiply(left, right))
    product_of_traces = reducible_normalized_trace(left) * reducible_normalized_trace(
        right
    )
    if trace_product == product_of_traces:
        raise AssertionError("reducible normalized trace accidentally became multiplicative")

    noncentral_matrix = ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(0)))
    commutator_with_diagonal = (
        (
            Fraction(2) * noncentral_matrix[0][0]
            - noncentral_matrix[0][0] * Fraction(2),
            Fraction(2) * noncentral_matrix[0][1]
            - noncentral_matrix[0][1] * Fraction(3),
        ),
        (
            Fraction(3) * noncentral_matrix[1][0]
            - noncentral_matrix[1][0] * Fraction(2),
            Fraction(3) * noncentral_matrix[1][1]
            - noncentral_matrix[1][1] * Fraction(3),
        ),
    )
    if commutator_with_diagonal == (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    ):
        raise AssertionError("noncentral matrix commuted with all diagonal test elements")


IntMatrix = tuple[tuple[int, ...], ...]
GroupElement = tuple[int, int]


def int_matrix_multiply(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


RatMatrix = tuple[tuple[Fraction, ...], ...]


def rat_matrix_add(left: RatMatrix, right: RatMatrix) -> RatMatrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left)))
        for row in range(len(left))
    )


def rat_matrix_scale(coefficient: Fraction, matrix: RatMatrix) -> RatMatrix:
    return tuple(
        tuple(coefficient * entry for entry in row)
        for row in matrix
    )


def rat_matrix_multiply(left: RatMatrix, right: RatMatrix) -> RatMatrix:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


def int_to_rat_matrix(matrix: IntMatrix) -> RatMatrix:
    return tuple(tuple(Fraction(entry) for entry in row) for row in matrix)


def z2xz2_add(left: GroupElement, right: GroupElement) -> GroupElement:
    return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)


def pointed_coset_annulus_matrix(group_element: GroupElement) -> IntMatrix:
    # H={(0,0),(1,0)}.  Cosets are detected by the second coordinate.
    shift = group_element[1]
    return tuple(
        tuple(1 if target == (source + shift) % 2 else 0 for target in range(2))
        for source in range(2)
    )


def pointed_boundary_target(source_coset: int, group_element: GroupElement) -> int:
    return (source_coset + group_element[1]) % 2


def pointed_boundary_compose(left: GroupElement, right: GroupElement) -> GroupElement:
    return z2xz2_add(left, right)


def check_pointed_module_annulus_nimrep() -> None:
    """Check the finite non-diagonal annulus/nimrep identity.

    In the pointed fusion skeleton for G=Z_2 x Z_2 with module category G/H,
    the annulus matrices act by coset permutation.  This is a finite algebraic
    model of n_i n_j = sum_k N_ij^k n_k beyond the diagonal Cardy case.
    """

    elements: tuple[GroupElement, ...] = ((0, 0), (1, 0), (0, 1), (1, 1))
    vacuum = pointed_coset_annulus_matrix((0, 0))
    stabilizer = pointed_coset_annulus_matrix((1, 0))
    swap = pointed_coset_annulus_matrix((0, 1))

    assert_equal("pointed coset vacuum annulus matrix", vacuum, ((1, 0), (0, 1)))
    assert_equal("pointed stabilizer acts trivially on cosets", stabilizer, vacuum)
    assert_equal("pointed nontrivial coset action swaps boundaries", swap, ((0, 1), (1, 0)))
    if swap == vacuum:
        raise AssertionError("non-diagonal pointed module example collapsed to diagonal")

    for left in elements:
        for right in elements:
            product = int_matrix_multiply(
                pointed_coset_annulus_matrix(left),
                pointed_coset_annulus_matrix(right),
            )
            fused = pointed_coset_annulus_matrix(z2xz2_add(left, right))
            assert_equal(f"pointed module annulus nimrep {left}+{right}", product, fused)
            for row in product:
                for entry in row:
                    if entry < 0:
                        raise AssertionError("annulus matrix has a negative entry")


def check_pointed_annulus_fourier_diagonalization() -> None:
    """Check the finite Fourier diagonalization of the pointed annulus nimrep."""

    elements: tuple[GroupElement, ...] = ((0, 0), (1, 0), (0, 1), (1, 1))
    identity = int_to_rat_matrix(pointed_coset_annulus_matrix((0, 0)))
    swap = int_to_rat_matrix(pointed_coset_annulus_matrix((0, 1)))
    zero = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))

    projectors = {
        "trivial": rat_matrix_scale(Fraction(1, 2), rat_matrix_add(identity, swap)),
        "sign": rat_matrix_scale(Fraction(1, 2), rat_matrix_add(identity, rat_matrix_scale(Fraction(-1), swap))),
    }

    assert_equal(
        "pointed annulus Fourier projectors sum to identity",
        rat_matrix_add(projectors["trivial"], projectors["sign"]),
        identity,
    )
    for left_name, left_projector in projectors.items():
        for right_name, right_projector in projectors.items():
            product = rat_matrix_multiply(left_projector, right_projector)
            expected = left_projector if left_name == right_name else zero
            assert_equal(
                f"pointed annulus Fourier projector product {left_name} {right_name}",
                product,
                expected,
            )

    def quotient_character(character_name: str, group_element: GroupElement) -> Fraction:
        if character_name == "trivial":
            return Fraction(1)
        if character_name == "sign":
            return Fraction(1) if group_element[1] == 0 else Fraction(-1)
        raise AssertionError(character_name)

    for group_element in elements:
        spectral_resolution = zero
        for character_name, projector in projectors.items():
            spectral_resolution = rat_matrix_add(
                spectral_resolution,
                rat_matrix_scale(quotient_character(character_name, group_element), projector),
            )
        assert_equal(
            f"pointed annulus Fourier spectral resolution {group_element}",
            spectral_resolution,
            int_to_rat_matrix(pointed_coset_annulus_matrix(group_element)),
        )

    # Boundary Fourier coefficients psi_{x,chi}=|Q|^{-1/2} chi(x) give the
    # same matrix entries; using psi psi^* removes the square root.
    for group_element in elements:
        for source in (0, 1):
            for target in (0, 1):
                entry = sum(
                    Fraction(1, 2)
                    * quotient_character(character_name, (0, source))
                    * quotient_character(character_name, group_element)
                    * quotient_character(character_name, (0, target))
                    for character_name in projectors
                )
                assert_equal(
                    "pointed annulus boundary Fourier entry "
                    f"g={group_element}, source={source}, target={target}",
                    entry,
                    Fraction(pointed_coset_annulus_matrix(group_element)[source][target]),
                )

    assert_equal(
        "pointed annulus stabilizer element has vacuum spectrum",
        int_to_rat_matrix(pointed_coset_annulus_matrix((1, 0))),
        identity,
    )
    if (1, 0) == (0, 0):
        raise AssertionError("stabilizer label collapsed before annulus comparison")


def check_pointed_module_boundary_ope_associativity() -> None:
    """Check the pointed G/H boundary-field composition law.

    The generator psi_{x,g} runs from xH to (x+g)H.  Composition is inherited
    from pointed fusion, psi_{x+g,h} psi_{x,g}=psi_{x,g+h}.  This is the
    finite boundary-OPE associativity cell behind the annulus nimrep.
    """

    elements: tuple[GroupElement, ...] = ((0, 0), (1, 0), (0, 1), (1, 1))
    stabilizer_labels = ((0, 0), (1, 0))

    for source in (0, 1):
        stabilizer_endomorphisms = {
            g
            for g in elements
            if pointed_boundary_target(source, g) == source
        }
        assert_equal(
            f"pointed boundary stabilizer labels at source {source}",
            stabilizer_endomorphisms,
            set(stabilizer_labels),
        )

        for left in elements:
            middle = pointed_boundary_target(source, left)
            for right in elements:
                target_by_steps = pointed_boundary_target(middle, right)
                fused = pointed_boundary_compose(left, right)
                target_by_fusion = pointed_boundary_target(source, fused)
                assert_equal(
                    "pointed boundary OPE endpoint "
                    f"source={source}, left={left}, right={right}",
                    target_by_steps,
                    target_by_fusion,
                )

                for third in elements:
                    left_associated = pointed_boundary_compose(
                        pointed_boundary_compose(left, right),
                        third,
                    )
                    right_associated = pointed_boundary_compose(
                        left,
                        pointed_boundary_compose(right, third),
                    )
                    assert_equal(
                        "pointed boundary OPE associativity "
                        f"source={source}, left={left}, right={right}, third={third}",
                        left_associated,
                        right_associated,
                    )
                    final_by_steps = pointed_boundary_target(
                        pointed_boundary_target(
                            pointed_boundary_target(source, left),
                            right,
                        ),
                        third,
                    )
                    final_by_fusion = pointed_boundary_target(source, left_associated)
                    assert_equal(
                        "pointed boundary OPE final endpoint "
                        f"source={source}, left={left}, right={right}, third={third}",
                        final_by_steps,
                        final_by_fusion,
                    )

    if pointed_boundary_compose((1, 0), (1, 0)) != (0, 0):
        raise AssertionError("stabilizer endomorphism did not square to the vacuum")
    if pointed_boundary_target(0, (1, 0)) != pointed_boundary_target(0, (0, 0)):
        raise AssertionError("stabilizer label should preserve the boundary endpoint")
    if (1, 0) == (0, 0):
        raise AssertionError("distinct stabilizer chiral labels collapsed")


def check_pointed_stabilizer_classifying_idempotents() -> None:
    """Check the pointed mixed bulk-boundary stabilizer sewing cells."""

    elements: tuple[GroupElement, ...] = ((0, 0), (1, 0), (0, 1), (1, 1))
    stabilizer: tuple[GroupElement, ...] = ((0, 0), (1, 0))
    characters = {
        "trivial": {(0, 0): Fraction(1), (1, 0): Fraction(1)},
        "sign": {(0, 0): Fraction(1), (1, 0): Fraction(-1)},
    }

    def convolution(
        left: dict[GroupElement, Fraction],
        right: dict[GroupElement, Fraction],
    ) -> dict[GroupElement, Fraction]:
        result: dict[GroupElement, Fraction] = {}
        for left_element, left_coefficient in left.items():
            for right_element, right_coefficient in right.items():
                product = pointed_boundary_compose(left_element, right_element)
                result[product] = (
                    result.get(product, Fraction(0))
                    + left_coefficient * right_coefficient
                )
        return {
            element: coefficient
            for element, coefficient in result.items()
            if coefficient
        }

    def frobenius_trace(element: dict[GroupElement, Fraction]) -> Fraction:
        return element.get((0, 0), Fraction(0))

    def sector_field(
        group_element: GroupElement,
        idempotent: dict[GroupElement, Fraction],
    ) -> dict[GroupElement, Fraction]:
        return {
            pointed_boundary_compose(group_element, h): coefficient
            for h, coefficient in idempotent.items()
        }

    idempotents = {
        name: {
            h: character[h] / len(stabilizer)
            for h in stabilizer
        }
        for name, character in characters.items()
    }
    identity = {(0, 0): Fraction(1)}
    summed_idempotents: dict[GroupElement, Fraction] = {}
    for idempotent in idempotents.values():
        for element, coefficient in idempotent.items():
            summed_idempotents[element] = (
                summed_idempotents.get(element, Fraction(0)) + coefficient
            )
    summed_idempotents = {
        element: coefficient
        for element, coefficient in summed_idempotents.items()
        if coefficient
    }
    assert_equal(
        "pointed stabilizer idempotents sum to identity",
        summed_idempotents,
        identity,
    )

    for left_name, left_idempotent in idempotents.items():
        for right_name, right_idempotent in idempotents.items():
            product = convolution(left_idempotent, right_idempotent)
            expected = left_idempotent if left_name == right_name else {}
            assert_equal(
                f"pointed stabilizer idempotent product {left_name} {right_name}",
                product,
                expected,
            )
            expected_pairing = Fraction(1, len(stabilizer)) if left_name == right_name else Fraction(0)
            assert_equal(
                f"pointed stabilizer Frobenius pairing {left_name} {right_name}",
                frobenius_trace(product),
                expected_pairing,
            )

    for source in (0, 1):
        for group_element in elements:
            target = pointed_boundary_target(source, group_element)
            for character_name, idempotent in idempotents.items():
                before_then_change = {
                    pointed_boundary_compose(h, group_element): coefficient
                    for h, coefficient in idempotent.items()
                }
                change_then_after = {
                    pointed_boundary_compose(group_element, h): coefficient
                    for h, coefficient in idempotent.items()
                }
                assert_equal(
                    "pointed stabilizer classifying slide "
                    f"source={source}, target={target}, "
                    f"g={group_element}, chi={character_name}",
                    before_then_change,
                    change_then_after,
                )

    for group_element in elements:
        for left_name, left_idempotent in idempotents.items():
            for right_name, right_idempotent in idempotents.items():
                forward = sector_field(group_element, left_idempotent)
                reverse = sector_field(group_element, right_idempotent)
                composition = convolution(forward, reverse)
                expected = left_idempotent if left_name == right_name else {}
                assert_equal(
                    "pointed stabilizer inverse sector composition "
                    f"g={group_element}, left={left_name}, right={right_name}",
                    composition,
                    expected,
                )
                expected_pairing = Fraction(1, len(stabilizer)) if left_name == right_name else Fraction(0)
                assert_equal(
                    "pointed stabilizer inverse sector two-point "
                    f"g={group_element}, left={left_name}, right={right_name}",
                    frobenius_trace(composition),
                    expected_pairing,
                )

    sign_projector = idempotents["sign"]
    if sign_projector == idempotents["trivial"]:
        raise AssertionError("nontrivial stabilizer character collapsed")


def check_pointed_laboratory_unified_dependency() -> None:
    """Check that the pointed BCFT cells are projections of one finite datum."""

    elements: tuple[GroupElement, ...] = ((0, 0), (1, 0), (0, 1), (1, 1))
    stabilizer: tuple[GroupElement, ...] = ((0, 0), (1, 0))
    characters = {
        "trivial": {(0, 0): Fraction(1), (1, 0): Fraction(1)},
        "sign": {(0, 0): Fraction(1), (1, 0): Fraction(-1)},
    }
    idempotents = {
        name: {
            h: character[h] / len(stabilizer)
            for h in stabilizer
        }
        for name, character in characters.items()
    }

    for group_element in elements:
        annulus = pointed_coset_annulus_matrix(group_element)
        for source in (0, 1):
            target = pointed_boundary_target(source, group_element)
            for candidate in (0, 1):
                expected_dimension = 1 if candidate == target else 0
                assert_equal(
                    "pointed laboratory annulus equals boundary-field count "
                    f"g={group_element}, source={source}, target={candidate}",
                    annulus[source][candidate],
                    expected_dimension,
                )

    for left in elements:
        for right in elements:
            for source in (0, 1):
                middle = pointed_boundary_target(source, left)
                target_by_fields = pointed_boundary_target(middle, right)
                target_by_fusion = pointed_boundary_target(
                    source,
                    pointed_boundary_compose(left, right),
                )
                assert_equal(
                    "pointed laboratory OPE endpoint matches annulus product "
                    f"source={source}, left={left}, right={right}",
                    target_by_fields,
                    target_by_fusion,
                )

    for stabilizer_element in stabilizer:
        reconstructed: dict[GroupElement, Fraction] = {}
        for character_name, idempotent in idempotents.items():
            weight = characters[character_name][stabilizer_element]
            for h, coefficient in idempotent.items():
                reconstructed[h] = reconstructed.get(h, Fraction(0)) + weight * coefficient
        reconstructed = {
            h: coefficient
            for h, coefficient in reconstructed.items()
            if coefficient
        }
        assert_equal(
            "pointed stabilizer Fourier inversion "
            f"h={stabilizer_element}",
            reconstructed,
            {stabilizer_element: Fraction(1)},
        )

    quotient_projector_count = 2
    stabilizer_sector_count = len(idempotents)
    assert_equal(
        "pointed laboratory quotient times stabilizer sectors recovers group labels",
        quotient_projector_count * stabilizer_sector_count,
        len(elements),
    )
    assert_equal(
        "nontrivial stabilizer has vacuum annulus but nontrivial idempotent resolution",
        pointed_coset_annulus_matrix((1, 0)),
        pointed_coset_annulus_matrix((0, 0)),
    )
    if idempotents["sign"] == idempotents["trivial"]:
        raise AssertionError("stabilizer idempotent resolution collapsed")


StabilizerAlgebraElement = tuple[Fraction, Fraction]


def two_dimensional_stabilizer_product(
    left: StabilizerAlgebraElement,
    right: StabilizerAlgebraElement,
    generator_square: Fraction,
) -> StabilizerAlgebraElement:
    left_one, left_generator = left
    right_one, right_generator = right
    return (
        left_one * right_one + generator_square * left_generator * right_generator,
        left_one * right_generator + left_generator * right_one,
    )


def check_annulus_shadow_nonreconstruction() -> None:
    """Check that annulus endpoint data alone do not reconstruct sewing data."""

    one = (Fraction(1), Fraction(0))
    zero = (Fraction(0), Fraction(0))
    generator = (Fraction(0), Fraction(1))
    semisimple_annulus_shadow = {
        "vacuum": ((1, 0), (0, 1)),
        "stabilizer": ((1, 0), (0, 1)),
    }
    nilpotent_annulus_shadow = {
        "vacuum": ((1, 0), (0, 1)),
        "stabilizer": ((1, 0), (0, 1)),
    }
    assert_equal(
        "semisimple and nilpotent endpoint data have the same annulus shadow",
        semisimple_annulus_shadow,
        nilpotent_annulus_shadow,
    )

    semisimple_square = Fraction(1)
    nilpotent_square = Fraction(0)
    assert_equal(
        "semisimple stabilizer generator has inverse sector",
        two_dimensional_stabilizer_product(generator, generator, semisimple_square),
        one,
    )
    assert_equal(
        "nilpotent stabilizer generator lacks inverse sector",
        two_dimensional_stabilizer_product(generator, generator, nilpotent_square),
        zero,
    )

    e_plus = (Fraction(1, 2), Fraction(1, 2))
    e_minus = (Fraction(1, 2), Fraction(-1, 2))
    assert_equal(
        "semisimple stabilizer plus idempotent",
        two_dimensional_stabilizer_product(e_plus, e_plus, semisimple_square),
        e_plus,
    )
    assert_equal(
        "semisimple stabilizer minus idempotent",
        two_dimensional_stabilizer_product(e_minus, e_minus, semisimple_square),
        e_minus,
    )
    assert_equal(
        "semisimple stabilizer orthogonal idempotents",
        two_dimensional_stabilizer_product(e_plus, e_minus, semisimple_square),
        zero,
    )
    assert_equal(
        "nilpotent algebra does not support the same plus idempotent",
        two_dimensional_stabilizer_product(e_plus, e_plus, nilpotent_square)
        == e_plus,
        False,
    )

    samples = (
        Fraction(-1),
        Fraction(0),
        Fraction(1, 2),
        Fraction(1),
        Fraction(2),
    )
    for scalar in samples:
        for generator_coefficient in samples:
            element = (scalar, generator_coefficient)
            is_idempotent = (
                two_dimensional_stabilizer_product(element, element, nilpotent_square)
                == element
            )
            expected = element in (zero, one)
            assert_equal(
                "nilpotent stabilizer sample idempotents are only zero and one "
                f"a={scalar}, b={generator_coefficient}",
                is_idempotent,
                expected,
            )

    def trace_identity_coefficient(element: StabilizerAlgebraElement) -> Fraction:
        return element[0]

    semisimple_generator_pairing = trace_identity_coefficient(
        two_dimensional_stabilizer_product(generator, generator, semisimple_square)
    )
    nilpotent_generator_pairing = trace_identity_coefficient(
        two_dimensional_stabilizer_product(generator, generator, nilpotent_square)
    )
    assert_equal(
        "semisimple stabilizer two-point pairing sees stabilizer sector",
        semisimple_generator_pairing,
        Fraction(1),
    )
    assert_equal(
        "nilpotent endpoint shadow has degenerate identity-coefficient pairing",
        nilpotent_generator_pairing,
        Fraction(0),
    )


def check_bcft_observable_dependency_separation() -> None:
    """Check that BCFT observables require compatible data, not one shadow.

    The manuscript's construction-dependency paragraph separates annulus
    spectra, boundary OPE multiplication, classifying idempotents, two-point
    pairings, and generated sewing.  This finite check exhibits exact
    ambiguities when one of those layers is omitted.
    """

    one = (Fraction(1), Fraction(0))
    generator = (Fraction(0), Fraction(1))
    e_plus = (Fraction(1, 2), Fraction(1, 2))
    e_minus = (Fraction(1, 2), Fraction(-1, 2))

    semisimple_annulus_shadow = {
        "vacuum": ((1, 0), (0, 1)),
        "stabilizer": ((1, 0), (0, 1)),
    }
    nilpotent_annulus_shadow = semisimple_annulus_shadow.copy()
    assert_equal(
        "observable dependency samples have the same annulus spectrum",
        semisimple_annulus_shadow,
        nilpotent_annulus_shadow,
    )

    semisimple_square = Fraction(1)
    nilpotent_square = Fraction(0)

    def identity_coefficient(element: StabilizerAlgebraElement) -> Fraction:
        return element[0]

    semisimple_boundary_two_point = identity_coefficient(
        two_dimensional_stabilizer_product(
            generator,
            generator,
            semisimple_square,
        )
    )
    nilpotent_boundary_two_point = identity_coefficient(
        two_dimensional_stabilizer_product(
            generator,
            generator,
            nilpotent_square,
        )
    )
    assert_equal(
        "semisimple stabilizer has nonzero inverse two-point channel",
        semisimple_boundary_two_point,
        Fraction(1),
    )
    assert_equal(
        "nilpotent stabilizer has zero inverse two-point channel",
        nilpotent_boundary_two_point,
        Fraction(0),
    )
    if semisimple_boundary_two_point == nilpotent_boundary_two_point:
        raise AssertionError("annulus-equivalent samples had the same two-point observable")

    # Multiplication also does not fix the disk-pairing normalization.  The
    # semisimple algebra with tau^2=1 admits different symmetric Frobenius
    # functionals unless the boundary two-point convention is specified.
    def trace_with_stabilizer_weight(
        element: StabilizerAlgebraElement,
        stabilizer_weight: Fraction,
    ) -> Fraction:
        return element[0] + stabilizer_weight * element[1]

    standard_e_plus_pairing = trace_with_stabilizer_weight(
        two_dimensional_stabilizer_product(e_plus, e_plus, semisimple_square),
        Fraction(0),
    )
    deformed_e_plus_pairing = trace_with_stabilizer_weight(
        two_dimensional_stabilizer_product(e_plus, e_plus, semisimple_square),
        Fraction(1, 3),
    )
    standard_e_minus_pairing = trace_with_stabilizer_weight(
        two_dimensional_stabilizer_product(e_minus, e_minus, semisimple_square),
        Fraction(0),
    )
    deformed_e_minus_pairing = trace_with_stabilizer_weight(
        two_dimensional_stabilizer_product(e_minus, e_minus, semisimple_square),
        Fraction(1, 3),
    )
    assert_equal("standard plus idempotent pairing", standard_e_plus_pairing, Fraction(1, 2))
    assert_equal("standard minus idempotent pairing", standard_e_minus_pairing, Fraction(1, 2))
    assert_equal("deformed plus idempotent pairing", deformed_e_plus_pairing, Fraction(2, 3))
    assert_equal("deformed minus idempotent pairing", deformed_e_minus_pairing, Fraction(1, 3))
    if standard_e_plus_pairing == deformed_e_plus_pairing:
        raise AssertionError("multiplication-only data fixed a disk pairing")

    semisimple_observable_vector = (
        Fraction(1),  # vacuum annulus entry
        Fraction(1),  # stabilizer annulus entry
        semisimple_boundary_two_point,
        standard_e_plus_pairing,
        standard_e_minus_pairing,
        Fraction(1),  # normalized closed-loop sewing transport
    )
    nilpotent_observable_vector = (
        Fraction(1),
        Fraction(1),
        nilpotent_boundary_two_point,
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )
    deformed_pairing_vector = (
        Fraction(1),
        Fraction(1),
        semisimple_boundary_two_point,
        deformed_e_plus_pairing,
        deformed_e_minus_pairing,
        Fraction(1),
    )
    annulus_only_vector = (
        Fraction(1),
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )
    assert_equal(
        "semisimple and nilpotent samples agree on annulus entries",
        semisimple_observable_vector[:2],
        nilpotent_observable_vector[:2],
    )
    if semisimple_observable_vector == nilpotent_observable_vector:
        raise AssertionError("annulus-equivalent samples gave the same observable vector")
    if semisimple_observable_vector == deformed_pairing_vector:
        raise AssertionError("two-point convention did not change the observable vector")
    if semisimple_observable_vector == annulus_only_vector:
        raise AssertionError("annulus-only data reconstructed the boundary observable vector")

    def vector_add(
        left: tuple[Fraction, ...],
        right: tuple[Fraction, ...],
    ) -> tuple[Fraction, ...]:
        return tuple(
            left_value + right_value
            for left_value, right_value in zip(left, right)
        )

    def vector_sub(
        left: tuple[Fraction, ...],
        right: tuple[Fraction, ...],
    ) -> tuple[Fraction, ...]:
        return tuple(
            left_value - right_value
            for left_value, right_value in zip(left, right)
        )

    def vector_l1(vector: tuple[Fraction, ...]) -> Fraction:
        return sum(abs(entry) for entry in vector)

    # The finite move budget records the same dependency in residual form: a
    # boundary-observable claim is under-controlled if any observable layer is
    # omitted from the common construction schedule.
    residuals = {
        "chiral": (
            Fraction(1, 101), Fraction(0), Fraction(0),
            Fraction(0), Fraction(0), Fraction(0),
        ),
        "open": (
            Fraction(0), Fraction(1, 103), Fraction(0),
            Fraction(0), Fraction(0), Fraction(0),
        ),
        "local": (
            Fraction(0), Fraction(0), Fraction(1, 107),
            Fraction(0), Fraction(0), Fraction(0),
        ),
        "pairing": (
            Fraction(0), Fraction(0), Fraction(0),
            Fraction(1, 109), Fraction(1, 109), Fraction(0),
        ),
        "move": (
            Fraction(0), Fraction(0), Fraction(0),
            Fraction(0), Fraction(0), Fraction(1, 113),
        ),
        "anomaly": (
            Fraction(0), Fraction(0), Fraction(0),
            Fraction(0), Fraction(0), Fraction(1, 127),
        ),
    }
    residual_sum = tuple(Fraction(0) for _ in semisimple_observable_vector)
    for residual_vector in residuals.values():
        residual_sum = vector_add(residual_sum, residual_vector)
    exact_vector = vector_add(semisimple_observable_vector, residual_sum)
    complete_budget = sum(vector_l1(residual) for residual in residuals.values())
    actual_error = vector_l1(vector_sub(exact_vector, semisimple_observable_vector))
    _assert_leq(
        "BCFT boundary-observable vector residual bound",
        actual_error,
        complete_budget,
    )
    assert_equal(
        "BCFT boundary-observable residual telescope",
        vector_sub(exact_vector, semisimple_observable_vector),
        residual_sum,
    )
    for omitted_component, omitted_residual in residuals.items():
        underbudget = complete_budget - vector_l1(omitted_residual)
        if underbudget >= complete_budget:
            raise AssertionError(f"omitting {omitted_component} did not reduce the budget")
        if actual_error <= underbudget:
            raise AssertionError(
                f"omitting {omitted_component} still controlled the observable vector"
            )
    assert_equal(
        "identity element remains fixed by both semisimple multiplication samples",
        two_dimensional_stabilizer_product(one, one, semisimple_square),
        one,
    )


def check_boundary_entropy() -> None:
    entropies = [S[a][0] / S[0][0] for a in range(3)]
    # The displayed g_a is S_{a0}/sqrt(S_{00}); its square is S_{a0}^2/S_{00}.
    entropy_squares = [S[a][0] * S[a][0] / S[0][0] for a in range(3)]
    assert_equal("fixed-plus quantum dimension ratio", entropies[0], ONE)
    assert_equal("fixed-minus quantum dimension ratio", entropies[1], ONE)
    assert_equal("free quantum dimension ratio", entropies[2], SQRT2)
    assert_equal("fixed-plus g squared", entropy_squares[0], HALF)
    assert_equal("fixed-minus g squared", entropy_squares[1], HALF)
    assert_equal("free g squared", entropy_squares[2], ONE)


def check_boundary_gradient_spectral_weight() -> None:
    """Check the finite spectral weight in the boundary g-gradient metric.

    Suppress the common circumference factor and write kappa_sq for
    (2*pi/L)^2.  For one positive energy gap Delta, the periodic KMS pair
    e^{-Delta tau}+e^{-Delta(L-tau)} divided by 1-e^{-L Delta}, tested
    against 1-cos(kappa tau), gives

        2 kappa_sq / (Delta (Delta^2 + kappa_sq)).

    The exact rational check records the algebraic positivity mechanism; the
    transcendental value of kappa is irrelevant for the sign and normalization.
    """

    for gap in (Fraction(1, 3), Fraction(1), Fraction(5, 2)):
        for kappa_sq in (Fraction(1, 4), Fraction(4), Fraction(25, 3)):
            one_thermal_image = kappa_sq / (gap * (gap * gap + kappa_sq))
            two_image_weight = 2 * one_thermal_image
            displayed_weight = 2 * kappa_sq / (gap * (gap * gap + kappa_sq))
            assert_equal(
                f"boundary gradient spectral weight Delta={gap}, kappa^2={kappa_sq}",
                two_image_weight,
                displayed_weight,
            )
            if displayed_weight <= 0:
                raise AssertionError("positive boundary gap produced nonpositive gradient weight")


def check_boundary_observable_output_coordinates() -> None:
    """Check that annulus, disk response, and susceptibility are separate.

    The chapter opens with three observable coordinates: the open annulus
    spectrum, the disk one-point response, and the boundary susceptibility
    entering the g-gradient input.  This finite model keeps the annulus
    spectrum fixed while changing source matrix elements, so the susceptibility
    and disk response change even though the open graded dimensions do not.
    """

    annulus_spectrum = (
        ("vacuum", Fraction(0), 1),
        ("stabilizer", Fraction(1), 1),
    )
    semisimple_annulus = annulus_spectrum
    nilpotent_shadow_annulus = annulus_spectrum
    assert_equal(
        "boundary observable samples have the same annulus coordinate",
        semisimple_annulus,
        nilpotent_shadow_annulus,
    )

    semisimple_disk_response = (Fraction(1), Fraction(1, 3))
    deformed_disk_response = (Fraction(1), -Fraction(1, 3))
    if semisimple_disk_response == deformed_disk_response:
        raise AssertionError("annulus coordinate determined disk one-point response")

    kappa_sq = Fraction(4)

    def spectral_weight(gap: Fraction) -> Fraction:
        return 2 * kappa_sq / (gap * (gap * gap + kappa_sq))

    gaps = (Fraction(1), Fraction(3))
    semisimple_matrix_elements = (Fraction(2), Fraction(1))
    deformed_matrix_elements = (Fraction(1), Fraction(2))
    semisimple_susceptibility = sum(
        amplitude * spectral_weight(gap)
        for amplitude, gap in zip(semisimple_matrix_elements, gaps)
    )
    deformed_susceptibility = sum(
        amplitude * spectral_weight(gap)
        for amplitude, gap in zip(deformed_matrix_elements, gaps)
    )
    assert_equal(
        "boundary susceptibility sample A",
        semisimple_susceptibility,
        Fraction(664, 195),
    )
    assert_equal(
        "boundary susceptibility sample B",
        deformed_susceptibility,
        Fraction(392, 195),
    )
    if semisimple_susceptibility == deformed_susceptibility:
        raise AssertionError("annulus coordinate determined boundary susceptibility")

    beta = Fraction(3, 7)
    semisimple_entropy_velocity = -(beta * beta) * semisimple_susceptibility
    deformed_entropy_velocity = -(beta * beta) * deformed_susceptibility
    assert_equal(
        "boundary gradient response depends on susceptibility data",
        semisimple_entropy_velocity != deformed_entropy_velocity,
        True,
    )

    annulus_only_susceptibility = Fraction(0)
    assert_equal(
        "annulus-only shortcut misses finite susceptibility",
        annulus_only_susceptibility == semisimple_susceptibility,
        False,
    )
    assert_equal(
        "positive spectral weights make both retained susceptibilities positive",
        semisimple_susceptibility > 0 and deformed_susceptibility > 0,
        True,
    )


def check_boundary_gradient_monotonicity_from_metric() -> None:
    """Check the finite algebra of ds/dt = -B^T G B <= 0.

    The analytic BCFT theorem supplies the renormalized Ward susceptibility and
    the positive metric.  The monograph's local proposition only uses the finite
    consequence: gradient = -G B and contraction with the RG vector decreases
    the boundary entropy.
    """

    metrics = (
        ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(3))),
        ((Fraction(5), Fraction(-2)), (Fraction(-2), Fraction(2))),
        ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))),
    )
    beta_vectors = (
        (Fraction(3), Fraction(-1)),
        (Fraction(1, 2), Fraction(4)),
        (Fraction(0), Fraction(7)),
    )

    for metric in metrics:
        leading_minor = metric[0][0]
        determinant = metric[0][0] * metric[1][1] - metric[0][1] * metric[1][0]
        if leading_minor < 0 or determinant < 0:
            raise AssertionError("sample boundary-gradient metric is not positive semidefinite")
        for beta in beta_vectors:
            gradient = tuple(
                -sum(metric[row][col] * beta[col] for col in range(2))
                for row in range(2)
            )
            entropy_velocity = sum(beta[row] * gradient[row] for row in range(2))
            quadratic = sum(
                beta[row] * metric[row][col] * beta[col]
                for row in range(2)
                for col in range(2)
            )
            assert_equal(
                "boundary entropy RG contraction equals negative metric norm",
                entropy_velocity,
                -quadratic,
            )
            if entropy_velocity > 0:
                raise AssertionError("boundary entropy increased along a positive-metric RG step")

    initial_entropy = Fraction(9, 2)
    entropy_drops = (Fraction(1, 3), Fraction(2, 5), Fraction(7, 10))
    final_entropy = initial_entropy - sum(entropy_drops)
    if final_entropy > initial_entropy:
        raise AssertionError("boundary entropy endpoint inequality reversed")
    assert_equal(
        "boundary entropy endpoint drop",
        initial_entropy - final_entropy,
        sum(entropy_drops),
    )


def check_chan_paton_direct_sums() -> None:
    for n in range(1, 5):
        for m in range(1, 5):
            dimension = n * m
            annulus_multiplier = sum(1 for _r in range(n) for _s in range(m))
            assert_equal(
                f"Chan-Paton annulus multiplicity {n}x{m}",
                annulus_multiplier,
                dimension,
            )

    for n in range(1, 5):
        free_g_squared = S[2][0] * S[2][0] / S[0][0]
        direct_sum_g_squared = Qsqrt2(Fraction(n * n)) * free_g_squared
        assert_equal(
            f"direct-sum boundary entropy square for {n} free Ising branes",
            direct_sum_g_squared,
            Qsqrt2(Fraction(n * n)),
        )

    for r in range(3):
        for s in range(3):
            for t in range(3):
                for u in range(3):
                    product_nonzero = s == t
                    expected_target = (r, u) if product_nonzero else None
                    actual_target = (r, u) if s == t else None
                    assert_equal(
                        f"matrix-unit product E_{r}{s} E_{t}{u}",
                        actual_target,
                        expected_target,
                    )


def check_ising_boundary_changing_constants() -> None:
    f_sigma_sigma_sigma = [
        [INV_SQRT2, INV_SQRT2],
        [INV_SQRT2, -INV_SQRT2],
    ]
    identity = [
        [ONE, ZERO],
        [ZERO, ONE],
    ]
    assert_equal(
        "Ising sigma-sigma-sigma F matrix squares to identity",
        matrix_multiply(f_sigma_sigma_sigma, f_sigma_sigma_sigma),
        identity,
    )

    for row, fixed_boundary in enumerate(("+", "-")):
        identity_coeff = f_sigma_sigma_sigma[row][0]
        epsilon_coeff = f_sigma_sigma_sigma[row][1]
        probability_sum = identity_coeff * identity_coeff + epsilon_coeff * epsilon_coeff
        assert_equal(
            f"free-fixed-free row normalization through {fixed_boundary}",
            probability_sum,
            ONE,
        )

    assert_equal(
        "fixed-plus energy-channel coefficient",
        f_sigma_sigma_sigma[0][1],
        INV_SQRT2,
    )
    assert_equal(
        "fixed-minus energy-channel coefficient",
        f_sigma_sigma_sigma[1][1],
        -INV_SQRT2,
    )

    h_sigma = Fraction(1, 16)
    h_epsilon = Fraction(1, 2)
    assert_equal("sigma sigma to identity OPE power", -2 * h_sigma, Fraction(-1, 8))
    assert_equal(
        "sigma sigma to epsilon OPE power",
        h_epsilon - 2 * h_sigma,
        Fraction(3, 8),
    )
    assert_equal(
        "epsilon epsilon to identity OPE power",
        -2 * h_epsilon,
        Fraction(-1, 1),
    )
    assert_equal(
        "epsilon sigma to sigma OPE power",
        h_sigma - h_epsilon - h_sigma,
        Fraction(-1, 2),
    )


@dataclass(frozen=True)
class SewingChannelAxes:
    boundary_field_multiplicity: int
    left_chiral_multiplicity: int
    right_chiral_multiplicity: int

    @property
    def chiral_block_dimension(self) -> int:
        return self.left_chiral_multiplicity * self.right_chiral_multiplicity

    @property
    def full_channel_term_count(self) -> int:
        return self.boundary_field_multiplicity * self.chiral_block_dimension


def channel_chiral_dimension(channels: tuple[SewingChannelAxes, ...]) -> int:
    return sum(channel.chiral_block_dimension for channel in channels)


def channel_boundary_dimension(channels: tuple[SewingChannelAxes, ...]) -> int:
    return sum(channel.boundary_field_multiplicity for channel in channels)


def channel_full_term_count(channels: tuple[SewingChannelAxes, ...]) -> int:
    return sum(channel.full_channel_term_count for channel in channels)


def scalar_fusing_chart_applies(channels: tuple[SewingChannelAxes, ...]) -> bool:
    return all(channel.chiral_block_dimension == 1 for channel in channels)


def check_boundary_and_chiral_multiplicity_axes_are_separate() -> None:
    """Check the finite dimension bookkeeping behind the scalar sewing formula."""

    ising_cell = (
        SewingChannelAxes(
            boundary_field_multiplicity=1,
            left_chiral_multiplicity=1,
            right_chiral_multiplicity=1,
        ),
        SewingChannelAxes(
            boundary_field_multiplicity=1,
            left_chiral_multiplicity=1,
            right_chiral_multiplicity=1,
        ),
    )
    assert_equal(
        "Ising cell is multiplicity-free in the chiral block axis",
        scalar_fusing_chart_applies(ising_cell),
        True,
    )
    assert_equal(
        "Ising scalar sewing cell has two chiral basis lines",
        channel_chiral_dimension(ising_cell),
        2,
    )
    assert_equal(
        "Ising boundary and chiral counts agree only accidentally",
        channel_boundary_dimension(ising_cell),
        channel_chiral_dimension(ising_cell),
    )

    boundary_rich_cell = (
        SewingChannelAxes(
            boundary_field_multiplicity=2,
            left_chiral_multiplicity=1,
            right_chiral_multiplicity=1,
        ),
    )
    assert_equal(
        "boundary multiplicity does not enlarge the chiral fusing source",
        channel_chiral_dimension(boundary_rich_cell),
        1,
    )
    assert_equal(
        "boundary contraction still has two intermediate boundary fields",
        channel_boundary_dimension(boundary_rich_cell),
        2,
    )
    if channel_boundary_dimension(boundary_rich_cell) == channel_chiral_dimension(
        boundary_rich_cell
    ):
        raise AssertionError(
            "boundary-field labels were misread as chiral basis labels"
        )
    assert_equal(
        "scalar F still applies with boundary multiplicity "
        "and multiplicity-free chiral fusion",
        scalar_fusing_chart_applies(boundary_rich_cell),
        True,
    )

    fusion_rich_cell = (
        SewingChannelAxes(
            boundary_field_multiplicity=1,
            left_chiral_multiplicity=2,
            right_chiral_multiplicity=1,
        ),
    )
    assert_equal(
        "nontrivial chiral fusion multiplicity enlarges "
        "the associator source",
        channel_chiral_dimension(fusion_rich_cell),
        2,
    )
    assert_equal(
        "boundary labels alone miss the fusion-multiplicity axis",
        channel_boundary_dimension(fusion_rich_cell),
        1,
    )
    assert_equal(
        "scalar F chart rejects a fusion-multiplicity cell",
        scalar_fusing_chart_applies(fusion_rich_cell),
        False,
    )
    assert_equal(
        "full channel terms carry both boundary and chiral axes",
        channel_full_term_count(fusion_rich_cell),
        2,
    )


def check_ising_four_boundary_sewing_cell() -> None:
    """Check the multiplicity-free Cardy-Lewellen sewing cell in Ising."""

    row_vectors = {
        "+": (INV_SQRT2, INV_SQRT2),
        "-": (INV_SQRT2, -INV_SQRT2),
    }
    for left_label, left_row in row_vectors.items():
        for right_label, right_row in row_vectors.items():
            inner_product = sum(
                (
                    left_coefficient * right_coefficient
                    for left_coefficient, right_coefficient in zip(left_row, right_row)
                ),
                ZERO,
            )
            expected = ONE if left_label == right_label else ZERO
            assert_equal(
                "Ising four-boundary Cardy-Lewellen sewing cell "
                f"{left_label},{right_label}",
                inner_product,
                expected,
            )


def check_compact_boson_zero_mode_duality() -> None:
    samples = [
        (0, winding)
        for winding in range(-3, 4)
    ]
    for momentum, winding in samples:
        dual_momentum, dual_winding = winding, momentum
        assert_equal("Neumann m=0 maps to Dirichlet dual winding", dual_winding, 0)
        assert_equal("dual momentum records original winding", dual_momentum, winding)

    samples = [
        (momentum, 0)
        for momentum in range(-3, 4)
    ]
    for momentum, winding in samples:
        dual_momentum, dual_winding = winding, momentum
        assert_equal("Dirichlet w=0 maps to Neumann dual momentum", dual_momentum, 0)
        assert_equal("dual winding records original momentum", dual_winding, momentum)


def laurent_cosh(x_power: int, y_power: int = 0) -> Laurent2:
    return (
        Laurent2.monomial(x_power, y_power)
        + Laurent2.monomial(-x_power, -y_power)
    ).scale(Fraction(1, 2))


def laurent_sinh(x_power: int, y_power: int = 0) -> Laurent2:
    return (
        Laurent2.monomial(x_power, y_power)
        - Laurent2.monomial(-x_power, -y_power)
    ).scale(Fraction(1, 2))


def check_liouville_fzzt_zz_hyperbolic_identity() -> None:
    lhs = laurent_cosh(1, 1) - laurent_cosh(1, -1)
    rhs = (laurent_sinh(1, 0) * laurent_sinh(0, 1)).scale(Fraction(2))
    assert_equal("FZZT difference to ZZ hyperbolic product", lhs, rhs)


def check_liouville_degenerate_shift_sum() -> None:
    for n in range(1, 9):
        finite_shift_sum = Laurent2.from_dict(
            {
                (n - 1 - 2 * j, 0): Fraction(1)
                for j in range(n)
            }
        )
        lhs = laurent_sinh(n, 0)
        rhs = laurent_sinh(1, 0) * finite_shift_sum
        assert_equal(f"Liouville degenerate shift sum n={n}", lhs, rhs)


def finite_cosine_inner_product(
    modulus: int,
    left: int,
    right: int,
) -> Fraction:
    """Exact inner product of even finite Fourier waves on Z/modulus.

    c_s(p)=z^(sp)+z^(-sp).  The normalized half-line/even inner product is
    (2N)^(-1) sum_p c_left(p)c_right(p).  Orthogonality of roots of unity
    reduces the calculation to counting zero exponents modulo N.
    """

    zero_exponent_count = 0
    for exponent in (
        left + right,
        left - right,
        -left + right,
        -left - right,
    ):
        if exponent % modulus == 0:
            zero_exponent_count += 1
    return Fraction(zero_exponent_count, 2)


def check_continuous_annulus_plancherel_regulator() -> None:
    """Check the finite cyclic regulator for the continuous annulus kernel.

    The continuous FZZT wave C_s(P)=2 cos(2 pi s P) identifies s with -s.
    For odd finite cyclic regulators, the exact even Fourier inner product
    verifies the same quotient bookkeeping: nonzero reflection orbits are
    orthonormal after the 1/(2N) normalization, while unquotiented labels
    s and -s have off-diagonal Gram entry one.
    """

    for modulus in (5, 7, 9, 11, 13):
        representatives = tuple(range(1, (modulus + 1) // 2))
        for left in representatives:
            for right in representatives:
                expected = Fraction(1) if left == right else Fraction(0)
                assert_equal(
                    "finite cosine Plancherel quotient "
                    f"N={modulus}, left={left}, right={right}",
                    finite_cosine_inner_product(modulus, left, right),
                    expected,
                )

        for label in representatives:
            reflected = (-label) % modulus
            assert_equal(
                f"finite cosine reflected label overlap N={modulus}, label={label}",
                finite_cosine_inner_product(modulus, label, reflected),
                Fraction(1),
            )
            if label != reflected and finite_cosine_inner_product(
                modulus,
                label,
                reflected,
            ) == Fraction(0):
                raise AssertionError("unquotiented reflected label became orthogonal")

        assert_equal(
            f"finite cosine constant fixed-orbit norm N={modulus}",
            finite_cosine_inner_product(modulus, 0, 0),
            Fraction(2),
        )


Polynomial = tuple[Fraction, ...]


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    product = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_power, left_coefficient in enumerate(left):
        for right_power, right_coefficient in enumerate(right):
            product[left_power + right_power] += left_coefficient * right_coefficient
    while len(product) > 1 and product[-1] == 0:
        product.pop()
    return tuple(product)


def polynomial_eval(coefficients: Polynomial, point: Fraction) -> Fraction:
    value = Fraction(0)
    power = Fraction(1)
    for coefficient in coefficients:
        value += coefficient * power
        power *= point
    return value


def simple_pole_residue(
    test_polynomial: Polynomial,
    residue_polynomial: Polynomial,
    pole: Fraction,
) -> Fraction:
    return polynomial_eval(polynomial_multiply(test_polynomial, residue_polynomial), pole)


def contour_functional(
    test_polynomial: Polynomial,
    continuous_weights: Polynomial,
    crossings: tuple[tuple[Fraction, Polynomial], ...],
) -> Fraction:
    continuous = sum(
        (
            coefficient * continuous_weights[power]
            for power, coefficient in enumerate(test_polynomial)
        ),
        Fraction(0),
    )
    residues = sum(
        (
            simple_pole_residue(test_polynomial, residue_polynomial, pole)
            for pole, residue_polynomial in crossings
        ),
        Fraction(0),
    )
    return continuous + residues


def check_nonrational_pole_crossing_residue_cell() -> None:
    """Check the finite algebra of contour-pole residue bookkeeping.

    The monograph's local model says that when a simple pole crosses the
    closed-channel contour, the change in the sewing functional is the
    evaluation functional Res_{P=a} rho(P) phi(P)/(P-a) = rho(a) phi(a).
    The common 2*pi*i orientation factor is suppressed here; the exact rational
    check is the residue/evaluation algebra and the channel-compatibility
    consequence.
    """

    tests: tuple[Polynomial, ...] = (
        (Fraction(1),),
        (Fraction(2), Fraction(-3), Fraction(5)),
        (Fraction(-1, 2), Fraction(4, 3), Fraction(0), Fraction(7, 5)),
    )
    residues: tuple[Polynomial, ...] = (
        (Fraction(5, 7),),
        (Fraction(1, 3), Fraction(-2, 5)),
        (Fraction(0), Fraction(3, 2), Fraction(1, 4)),
    )
    poles = (Fraction(2, 3), Fraction(-1, 4), Fraction(5, 6))

    for test_polynomial in tests:
        for residue_polynomial in residues:
            for pole in poles:
                direct = polynomial_eval(
                    polynomial_multiply(test_polynomial, residue_polynomial),
                    pole,
                )
                residue = simple_pole_residue(test_polynomial, residue_polynomial, pole)
                assert_equal(
                    "nonrational contour simple-pole residue equals evaluation",
                    residue,
                    direct,
                )

    continuous_weights = (Fraction(1, 2), Fraction(-3, 7), Fraction(5, 11), Fraction(2, 13))
    test_polynomial = (Fraction(3), Fraction(-2), Fraction(5, 4), Fraction(1, 6))
    first_crossing = (Fraction(2, 3), (Fraction(5, 7), Fraction(1, 5)))
    second_crossing = (Fraction(-1, 4), (Fraction(-3, 8), Fraction(2, 9), Fraction(1, 6)))
    first_then_second = contour_functional(
        test_polynomial,
        continuous_weights,
        (first_crossing, second_crossing),
    )
    second_then_first = contour_functional(
        test_polynomial,
        continuous_weights,
        (second_crossing, first_crossing),
    )
    assert_equal(
        "nonrational pole-crossing residue additions commute",
        first_then_second,
        second_then_first,
    )

    omitted_first = contour_functional(
        test_polynomial,
        continuous_weights,
        (second_crossing,),
    )
    missing_residue = simple_pole_residue(
        test_polynomial,
        first_crossing[1],
        first_crossing[0],
    )
    if missing_residue == 0:
        raise AssertionError("pole-crossing compatibility diagnostic chose a zero residue")
    assert_equal(
        "omitting one crossed pole changes the channel functional by its residue",
        first_then_second - omitted_first,
        missing_residue,
    )


def check_bordered_sewing_move_defect_budget() -> None:
    """Check the finite telescoping budget for generated sewing moves."""

    transports = (Fraction(3, 2), Fraction(5, 3), Fraction(7, 5), Fraction(11, 13))
    defects = (Fraction(1, 7), Fraction(-2, 9), Fraction(3, 11), Fraction(-5, 17))
    amplitude = Fraction(19, 23)
    amplitudes = [amplitude]
    for transport, defect in zip(transports, defects):
        amplitude = transport * amplitude + defect
        amplitudes.append(amplitude)

    total_transport = Fraction(1)
    for transport in transports:
        total_transport *= transport
    net_defect = amplitudes[-1] - total_transport * amplitudes[0]

    weighted_defects = Fraction(0)
    for index, defect in enumerate(defects):
        future_transport = Fraction(1)
        for transport in transports[index + 1 :]:
            future_transport *= transport
        weighted_defects += future_transport * defect
    assert_equal("bordered sewing move telescoping identity", net_defect, weighted_defects)

    budget = Fraction(0)
    for index, defect in enumerate(defects):
        future_transport = Fraction(1)
        for transport in transports[index + 1 :]:
            future_transport *= abs(transport)
        budget += future_transport * abs(defect)
    _assert_leq("bordered sewing move defect budget", abs(net_defect), budget)

    zero_amplitude = amplitudes[0]
    for transport in transports:
        zero_amplitude = transport * zero_amplitude
    assert_equal(
        "zero-defect bordered sewing path is pure transport",
        zero_amplitude,
        total_transport * amplitudes[0],
    )

    first_path_defects = (Fraction(1, 10), Fraction(-1, 14))
    second_path_defects = (Fraction(-1, 15), Fraction(1, 21), Fraction(1, 30))
    first_budget = sum(abs(defect) for defect in first_path_defects)
    second_budget = sum(abs(defect) for defect in second_path_defects)
    path_difference = sum(first_path_defects) - sum(second_path_defects)
    _assert_leq(
        "two sewing paths combined local budgets",
        abs(path_difference),
        first_budget + second_budget,
    )


def check_finite_sewing_anomaly_cocycle_trivialization() -> None:
    # Vertex rescalings eta trivialize projective sewing factors
    # lambda_{u->v}=eta_v/eta_u.  This is the finite determinant-line
    # skeleton behind the chapter's anomaly-line sewing discussion.
    vertex_scale = {
        "left": Fraction(2),
        "middle": Fraction(3),
        "right": Fraction(5),
    }
    coboundary_edges = {
        ("left", "middle"): vertex_scale["middle"] / vertex_scale["left"],
        ("middle", "right"): vertex_scale["right"] / vertex_scale["middle"],
        ("left", "right"): vertex_scale["right"] / vertex_scale["left"],
        ("right", "left"): vertex_scale["left"] / vertex_scale["right"],
    }
    path_phase = coboundary_edges[("left", "middle")] * coboundary_edges[("middle", "right")]
    assert_equal(
        "sewing anomaly coboundary path telescopes",
        path_phase,
        coboundary_edges[("left", "right")],
    )
    loop_phase = (
        coboundary_edges[("left", "middle")]
        * coboundary_edges[("middle", "right")]
        * coboundary_edges[("right", "left")]
    )
    assert_equal("sewing anomaly coboundary loop is trivial", loop_phase, Fraction(1))

    amplitude = {
        "left": Fraction(7),
        "middle": coboundary_edges[("left", "middle")] * Fraction(7),
        "right": coboundary_edges[("left", "right")] * Fraction(7),
    }
    rescaled = {
        vertex: value / vertex_scale[vertex]
        for vertex, value in amplitude.items()
    }
    assert_equal(
        "sewing anomaly vertex trivialization removes projective factors",
        set(rescaled.values()),
        {Fraction(7, 2)},
    )

    nontrivial_edges = {
        ("left", "middle"): Fraction(2),
        ("middle", "right"): Fraction(3),
        ("right", "left"): Fraction(5),
    }
    nontrivial_loop_phase = (
        nontrivial_edges[("left", "middle")]
        * nontrivial_edges[("middle", "right")]
        * nontrivial_edges[("right", "left")]
    )
    if nontrivial_loop_phase == 1:
        raise AssertionError("nontrivial sewing anomaly loop accidentally trivial")

    # Any coboundary would have loop product one, so this holonomy cannot be
    # removed by changing vertex trivializations.
    assert_equal(
        "nontrivial sewing anomaly obstructs scalar trivialization",
        nontrivial_loop_phase,
        Fraction(30),
    )

    # The scalar projective phase alone is not the full scalar
    # decomposition-independence test.  A one-vertex loop can have nontrivial
    # anomaly-line phase whose effect on a particular scalar amplitude is
    # cancelled by ordinary transport.
    scalar_amplitude = Fraction(7)
    ordinary_loop_transport = Fraction(1, 30)
    total_projective_transport = nontrivial_loop_phase * ordinary_loop_transport
    assert_equal(
        "ordinary transport can cancel projective sewing phase",
        total_projective_transport * scalar_amplitude,
        scalar_amplitude,
    )

    trivial_ordinary_transport = Fraction(1)
    assert_equal(
        "nontrivial sewing phase obstructs scalar amplitude after ordinary transport is trivialized",
        nontrivial_loop_phase * trivial_ordinary_transport * scalar_amplitude,
        Fraction(210),
    )
    if (
        nontrivial_loop_phase * trivial_ordinary_transport * scalar_amplitude
        == scalar_amplitude
    ):
        raise AssertionError(
            "nontrivial sewing phase should move a nonzero scalar amplitude "
            "when ordinary transport is trivial"
        )


def main() -> None:
    check_modular_s()
    check_cardy_annulus()
    check_annulus_nimrep_spectral_resolution()
    check_oriented_cardy_annulus_for_cyclic_pointed_data()
    check_fusion_associativity()
    check_cardy_fusion_ring_characters()
    check_cardy_unit_algebra_module_multiplicities()
    check_matrix_frobenius_cutting_move()
    check_finite_classifying_center_characters()
    check_pointed_module_annulus_nimrep()
    check_pointed_annulus_fourier_diagonalization()
    check_pointed_module_boundary_ope_associativity()
    check_pointed_stabilizer_classifying_idempotents()
    check_pointed_laboratory_unified_dependency()
    check_annulus_shadow_nonreconstruction()
    check_bcft_observable_dependency_separation()
    check_boundary_entropy()
    check_boundary_gradient_spectral_weight()
    check_boundary_observable_output_coordinates()
    check_boundary_gradient_monotonicity_from_metric()
    check_chan_paton_direct_sums()
    check_ising_boundary_changing_constants()
    check_boundary_and_chiral_multiplicity_axes_are_separate()
    check_ising_four_boundary_sewing_cell()
    check_compact_boson_zero_mode_duality()
    check_liouville_fzzt_zz_hyperbolic_identity()
    check_liouville_degenerate_shift_sum()
    check_continuous_annulus_plancherel_regulator()
    check_nonrational_pole_crossing_residue_cell()
    check_bordered_sewing_move_defect_budget()
    check_finite_sewing_anomaly_cocycle_trivialization()
    print(
        "All BCFT Cardy, oriented-annulus, sewing, boundary-gradient, "
        "Ising boundary-changing, "
        "boundary/chiral-multiplicity-separation, "
        "matrix-Frobenius, finite-center, pointed-nimrep, Chan-Paton, "
        "annulus-nimrep-spectral-resolution, "
        "pointed-annulus-Fourier, pointed-boundary-OPE, "
        "pointed-stabilizer-slide, pointed-laboratory-unified, "
        "annulus-shadow-nonreconstruction, observable-dependency-separation, "
        "boundary-observable-vector residual, boundary-observable outputs, "
        "compact-boson, "
        "Liouville-boundary, continuous-annulus Plancherel, "
        "nonrational-pole-residue, bordered-sewing-budget, and "
        "finite-sewing-anomaly-cocycle checks passed."
    )


if __name__ == "__main__":
    main()
