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
    check_boundary_entropy()
    check_chan_paton_direct_sums()
    check_ising_boundary_changing_constants()
    check_compact_boson_zero_mode_duality()
    check_liouville_fzzt_zz_hyperbolic_identity()
    check_liouville_degenerate_shift_sum()
    print(
        "All BCFT Cardy, sewing, Ising boundary-changing, "
        "Chan-Paton, compact-boson, and Liouville-boundary checks passed."
    )


if __name__ == "__main__":
    main()
