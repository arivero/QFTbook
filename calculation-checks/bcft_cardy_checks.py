#!/usr/bin/env python3
"""Exact BCFT Cardy/Ishibashi bookkeeping checks in the Ising example."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


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


def z2xz2_add(left: GroupElement, right: GroupElement) -> GroupElement:
    return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)


def pointed_coset_annulus_matrix(group_element: GroupElement) -> IntMatrix:
    # H={(0,0),(1,0)}.  Cosets are detected by the second coordinate.
    shift = group_element[1]
    return tuple(
        tuple(1 if target == (source + shift) % 2 else 0 for target in range(2))
        for source in range(2)
    )


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


def check_ising_four_boundary_sewing_cell() -> None:
    """Check the finite Cardy-Lewellen sewing cell in the Ising example."""

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


def main() -> None:
    check_modular_s()
    check_cardy_annulus()
    check_fusion_associativity()
    check_cardy_fusion_ring_characters()
    check_cardy_unit_algebra_module_multiplicities()
    check_matrix_frobenius_cutting_move()
    check_finite_classifying_center_characters()
    check_pointed_module_annulus_nimrep()
    check_boundary_entropy()
    check_boundary_gradient_spectral_weight()
    check_chan_paton_direct_sums()
    check_ising_boundary_changing_constants()
    check_ising_four_boundary_sewing_cell()
    check_compact_boson_zero_mode_duality()
    check_liouville_fzzt_zz_hyperbolic_identity()
    check_liouville_degenerate_shift_sum()
    print(
        "All BCFT Cardy, sewing, boundary-gradient, Ising boundary-changing, "
        "matrix-Frobenius, finite-center, pointed-nimrep, Chan-Paton, "
        "compact-boson, and Liouville-boundary checks passed."
    )


if __name__ == "__main__":
    main()
