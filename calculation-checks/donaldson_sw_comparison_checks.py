#!/usr/bin/env python3
"""Finite checks for Donaldson-Witten and Seiberg-Witten comparison formulas.

Includes a theorem-boundary status gate for the Bauer-Furuta stable
cohomotopy target data: unparameterized classes, Picard-torus families,
chamber-fixed cases, and invalid missing orientation/properness/reducible-wall
inputs.
"""

from __future__ import annotations

from fractions import Fraction

from check_utils import assert_geq as _assert_geq
from check_utils import assert_leq as _assert_leq


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def vector_add(*vectors: list[Fraction]) -> list[Fraction]:
    return [sum(vector[i] for vector in vectors) for i in range(len(vectors[0]))]


def vector_sub(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [left[i] - right[i] for i in range(len(left))]


def dot(row: list[Fraction], column: list[Fraction]) -> Fraction:
    return sum(row[i] * column[i] for i in range(len(row)))


def l1_norm(vector: list[Fraction]) -> Fraction:
    return sum(abs(entry) for entry in vector)


def linfty_norm(vector: list[Fraction]) -> Fraction:
    return max(abs(entry) for entry in vector)


def solve_linear_system(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    size = len(rhs)
    augmented = [row[:] + [rhs_entry] for row, rhs_entry in zip(matrix, rhs)]
    for pivot_col in range(size):
        pivot_row = next(
            row for row in range(pivot_col, size) if augmented[row][pivot_col] != 0
        )
        augmented[pivot_col], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[pivot_col],
        )
        pivot = augmented[pivot_col][pivot_col]
        augmented[pivot_col] = [entry / pivot for entry in augmented[pivot_col]]
        for row in range(size):
            if row == pivot_col:
                continue
            factor = augmented[row][pivot_col]
            if factor == 0:
                continue
            augmented[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(augmented[row], augmented[pivot_col])
            ]
    return [augmented[row][-1] for row in range(size)]


def chi(b1: int, b2_plus: int, b2_minus: int) -> int:
    return 2 - 2 * b1 + b2_plus + b2_minus


def signature(b2_plus: int, b2_minus: int) -> int:
    return b2_plus - b2_minus


def asd_virtual_dimension(k: int, b1: int, b2_plus: int) -> int:
    return 8 * k - 3 * (1 - b1 + b2_plus)


def asd_index_from_pontryagin(
    p1_ad: int, chi_value: int, sigma_value: int
) -> Fraction:
    """Index of d_A^* plus d_A^+ for an SU(2) bundle."""

    return -2 * p1_ad - Fraction(3, 2) * (chi_value + sigma_value)


def sw_expected_dimension(c1_square: int, chi_value: int, sigma_value: int) -> Fraction:
    return Fraction(c1_square - (2 * chi_value + 3 * sigma_value), 4)


def four_manifold_c1_square(chi_value: int, sigma_value: int) -> int:
    return 2 * chi_value + 3 * sigma_value


def holomorphic_euler_characteristic(chi_value: int, sigma_value: int) -> Fraction:
    return Fraction(chi_value + sigma_value, 4)


def feehan_leness_many_manifolds_status(
    *,
    b1: int,
    b2_plus: int,
    chi_value: int,
    sigma_value: int,
    sw_simple_type: bool,
    abundant: bool,
) -> bool:
    """Predicate for the theorem class quoted in the chapter.

    This is not the Witten comparison conjecture itself.  It is the visible
    theorem-subclass gate: b1=0, odd b2+ at least three, SW simple type, and
    either c1^2 >= chi_h - 3 or abundance.
    """

    topological_bound = (
        Fraction(four_manifold_c1_square(chi_value, sigma_value))
        >= holomorphic_euler_characteristic(chi_value, sigma_value) - 3
    )
    return (
        b1 == 0
        and b2_plus >= 3
        and b2_plus % 2 == 1
        and sw_simple_type
        and (topological_bound or abundant)
    )


def has_metric_chamber_dependence(b2_plus: int) -> bool:
    return b2_plus == 1


def bauer_furuta_target_status(
    *,
    b1: int,
    b2_plus: int,
    homology_orientation: bool,
    proper_monopole_map: bool,
    chamber_fixed: bool,
    avoids_reducible_wall: bool,
) -> str:
    """Finite gate for the theorem-boundary data in the Bauer-Furuta statement."""

    if not homology_orientation or not proper_monopole_map:
        return "invalid-missing-orientation-or-properness"
    if has_metric_chamber_dependence(b2_plus) and not chamber_fixed:
        return "invalid-missing-chamber"
    if not avoids_reducible_wall:
        return "invalid-reducible-wall"
    if b1 > 0:
        return "parameterized-picard-torus-family"
    if has_metric_chamber_dependence(b2_plus):
        return "unparameterized-chamber-class"
    return "unparameterized-chamber-stable-class"


def spinc_tensor_c1(c1_value: int, line_c1: int) -> int:
    return c1_value + 2 * line_c1


def sw_index_from_dirac_and_gauge(
    c1_square: int, b1: int, b2_plus: int, sigma_value: int
) -> Fraction:
    real_dirac_index = Fraction(c1_square - sigma_value, 4)
    abelian_gauge_index = -(1 - b1 + b2_plus)
    return real_dirac_index + abelian_gauge_index


def donaldson_descent_degree(cycle_dimension: int) -> int:
    return 4 - cycle_dimension


def check_asd_index_formula() -> None:
    examples = [
        # k, b1, b2_plus, b2_minus
        (1, 0, 1, 0),   # CP^2 topology
        (2, 0, 3, 19),  # K3 topology
        (3, 1, 2, 5),
    ]
    for k, b1, b2_plus, b2_minus in examples:
        chi_value = chi(b1, b2_plus, b2_minus)
        sigma_value = signature(b2_plus, b2_minus)
        p1_ad = -4 * k
        index_value = asd_index_from_pontryagin(p1_ad, chi_value, sigma_value)
        closed_form = asd_virtual_dimension(k, b1, b2_plus)
        assert_equal(index_value, closed_form, "ASD index closed form")


def check_sw_index_formula() -> None:
    examples = [
        # b1, b2_plus, b2_minus, c1_square, expected
        (0, 1, 0, 9, Fraction(0)),     # CP^2, c1 = 3H
        (0, 1, 0, 1, Fraction(-2)),    # CP^2, c1 = H
        (0, 3, 19, 0, Fraction(0)),    # K3, c1 = 0
        (1, 2, 5, -3, None),
    ]
    for b1, b2_plus, b2_minus, c1_square, expected in examples:
        chi_value = chi(b1, b2_plus, b2_minus)
        sigma_value = signature(b2_plus, b2_minus)
        formula = sw_expected_dimension(c1_square, chi_value, sigma_value)
        index_sum = sw_index_from_dirac_and_gauge(
            c1_square, b1, b2_plus, sigma_value
        )
        assert_equal(formula, index_sum, "SW index decomposition")
        if expected is not None:
            assert_equal(formula, expected, "SW example dimension")


def check_topological_identity_in_sw_dimension() -> None:
    for b1 in range(4):
        for b2_plus in range(5):
            for b2_minus in range(5):
                chi_value = chi(b1, b2_plus, b2_minus)
                sigma_value = signature(b2_plus, b2_minus)
                lhs = 2 * chi_value + 3 * sigma_value
                rhs = 4 * (1 - b1 + b2_plus) + sigma_value
                assert_equal(lhs, rhs, "2 chi plus 3 sigma identity")


def check_feehan_leness_theorem_status_gate() -> None:
    # K3 lies in the theorem gate: b1=0, b2+=3, SW simple type, and
    # c1^2=0 >= chi_h-3=-1.
    assert_equal(
        feehan_leness_many_manifolds_status(
            b1=0,
            b2_plus=3,
            chi_value=24,
            sigma_value=-16,
            sw_simple_type=True,
            abundant=False,
        ),
        True,
        "K3 Feehan-Leness theorem gate",
    )

    # E(n) has chi=12n, sigma=-8n, b2+=2n-1.  For n >= 4 the
    # c1^2 >= chi_h-3 inequality fails, so abundance is a genuinely separate
    # theorem hypothesis rather than a decoration.
    for n in range(4, 8):
        chi_en = 12 * n
        sigma_en = -8 * n
        assert_equal(
            Fraction(four_manifold_c1_square(chi_en, sigma_en)),
            Fraction(0),
            "E(n) topological c1 square",
        )
        assert_equal(
            holomorphic_euler_characteristic(chi_en, sigma_en),
            Fraction(n),
            "E(n) holomorphic Euler characteristic",
        )
        assert_equal(
            feehan_leness_many_manifolds_status(
                b1=0,
                b2_plus=2 * n - 1,
                chi_value=chi_en,
                sigma_value=sigma_en,
                sw_simple_type=True,
                abundant=False,
            ),
            False,
            "non-abundant E(n>=4) fails the c1-square gate",
        )
        assert_equal(
            feehan_leness_many_manifolds_status(
                b1=0,
                b2_plus=2 * n - 1,
                chi_value=chi_en,
                sigma_value=sigma_en,
                sw_simple_type=True,
                abundant=True,
            ),
            True,
            "abundant E(n>=4) passes the theorem gate",
        )

    # The chapter's central conjecture is broader than this theorem gate.  In
    # particular b2+>1 alone is not the standard Feehan-Leness theorem
    # hypothesis: odd b2+ >= 3 is part of the visible theorem ledger.
    assert_equal(
        feehan_leness_many_manifolds_status(
            b1=0,
            b2_plus=2,
            chi_value=7,
            sigma_value=-1,
            sw_simple_type=True,
            abundant=True,
        ),
        False,
        "even b2+ is outside the theorem gate",
    )

    assert_equal(has_metric_chamber_dependence(1), True, "b2+=1 has chambers")
    assert_equal(
        has_metric_chamber_dependence(3),
        False,
        "changing w at b2+>1 is not chamber dependence",
    )


def check_donaldson_degree_bookkeeping() -> None:
    assert_equal(donaldson_descent_degree(0), 4, "point insertion degree")
    assert_equal(donaldson_descent_degree(1), 3, "loop insertion degree")
    assert_equal(donaldson_descent_degree(2), 2, "surface insertion degree")
    assert_equal(donaldson_descent_degree(3), 1, "three-cycle insertion degree")
    assert_equal(donaldson_descent_degree(4), 0, "fundamental-cycle degree")

    # CP^2 topology, k = 1: virtual dimension is 2, so one surface insertion
    # has the matching Donaldson degree.
    dimension = asd_virtual_dimension(k=1, b1=0, b2_plus=1)
    assert_equal(dimension, 2, "CP^2 k=1 ASD virtual dimension")
    assert_equal(donaldson_descent_degree(2), dimension, "surface degree match")


def check_spinc_characteristic_lift_bookkeeping() -> None:
    # CP^2: characteristic classes are odd multiples of the hyperplane class.
    base_c1 = 3
    for line_c1 in range(-3, 4):
        shifted = spinc_tensor_c1(base_c1, line_c1)
        assert_equal(shifted % 2, 1, "CP2 Spin^c characteristic parity")

    # K3 is spin; even line twists keep c1 even and the untwisted structure has
    # c1 = 0.
    for line_c1 in range(-3, 4):
        shifted = spinc_tensor_c1(0, line_c1)
        assert_equal(shifted % 2, 0, "K3 Spin^c characteristic parity")


def check_sw_simple_type_examples() -> None:
    # K3.
    chi_k3 = 24
    sigma_k3 = -16
    assert_equal(2 * chi_k3 + 3 * sigma_k3, 0, "K3 simple-type target")
    assert_equal(
        sw_expected_dimension(0, chi_k3, sigma_k3),
        Fraction(0),
        "K3 zero basic class dimension",
    )

    # E(n): chi = 12 n, sigma = -8 n, fiber square zero.  The classes
    # (n - 2 - 2 j) F therefore all have zero square and dimension zero.
    for n in range(2, 8):
        chi_en = 12 * n
        sigma_en = -8 * n
        assert_equal(2 * chi_en + 3 * sigma_en, 0, "E(n) simple-type target")
        for j in range(n - 1):
            fiber_multiple = n - 2 - 2 * j
            c1_square = 0  # (fiber_multiple * F)^2 because F^2 = 0.
            assert_equal(
                sw_expected_dimension(c1_square, chi_en, sigma_en),
                Fraction(0),
                "E(n) fiber basic-class dimension",
            )


def check_blowup_simple_type_square_shift() -> None:
    examples = [
        (24, -16),  # K3
        (48, -32),  # E(4), fiber basic classes square zero
        (7, -3),
    ]
    for chi_value, sigma_value in examples:
        k_square = 2 * chi_value + 3 * sigma_value
        new_chi = chi_value + 1
        new_sigma = sigma_value - 1
        assert_equal(
            k_square - 1,
            2 * new_chi + 3 * new_sigma,
            "blow-up simple-type square shift",
        )


def check_elliptic_surface_binomial_coefficients() -> None:
    # (e^F - e^{-F})^(n-2) gives classes (n-2-2j)F with coefficients
    # (-1)^j binomial(n-2, j).  Check the exponent pattern and coefficient sum.
    for n in range(2, 8):
        degree = n - 2
        exponents = [degree - 2 * j for j in range(degree + 1)]
        expected = list(range(degree, -degree - 1, -2))
        assert_equal(exponents, expected, "E(n) exponent ladder")
        coeff_sum = sum(((-1) ** j) * binomial(degree, j) for j in range(degree + 1))
        target = 1 if degree == 0 else 0
        assert_equal(coeff_sum, target, "E(n) binomial alternating sum")


def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    numerator = 1
    denominator = 1
    for j in range(1, k + 1):
        numerator *= n + 1 - j
        denominator *= j
    return numerator // denominator


def check_furuta_examples() -> None:
    # K3 saturates Furuta's 10/8+2 inequality.
    b2_k3 = 22
    sigma_k3 = -16
    rhs_units = Fraction(10, 8) * abs(sigma_k3) + 2
    assert_equal(Fraction(b2_k3), rhs_units, "K3 Furuta saturation")
    assert_equal(
        Fraction(-sigma_k3, 8),
        Fraction(2),
        "K3 spin Dirac quaternionic index",
    )

    # Spin elliptic surfaces E(2m) obey the inequality; this is only an
    # arithmetic check of the topological numbers used in the chapter.
    for m in range(1, 5):
        n = 2 * m
        b2 = 12 * n - 2
        sigma_value = -8 * n
        _assert_geq("E(2m) Furuta arithmetic check", Fraction(b2), Fraction(10, 8) * abs(sigma_value) + 2)
        assert_equal(
            Fraction(-sigma_value, 8),
            Fraction(n),
            "E(2m) spin Dirac quaternionic index",
        )


def check_bauer_furuta_theorem_boundary_gate() -> None:
    assert_equal(
        bauer_furuta_target_status(
            b1=0,
            b2_plus=3,
            homology_orientation=True,
            proper_monopole_map=True,
            chamber_fixed=True,
            avoids_reducible_wall=True,
        ),
        "unparameterized-chamber-stable-class",
        "b1=0, b2+>1 Bauer-Furuta status",
    )
    assert_equal(
        bauer_furuta_target_status(
            b1=2,
            b2_plus=3,
            homology_orientation=True,
            proper_monopole_map=True,
            chamber_fixed=True,
            avoids_reducible_wall=True,
        ),
        "parameterized-picard-torus-family",
        "b1>0 Bauer-Furuta Picard-torus family status",
    )
    assert_equal(
        bauer_furuta_target_status(
            b1=0,
            b2_plus=1,
            homology_orientation=True,
            proper_monopole_map=True,
            chamber_fixed=False,
            avoids_reducible_wall=True,
        ),
        "invalid-missing-chamber",
        "b2+=1 needs chamber data",
    )
    assert_equal(
        bauer_furuta_target_status(
            b1=0,
            b2_plus=1,
            homology_orientation=True,
            proper_monopole_map=True,
            chamber_fixed=True,
            avoids_reducible_wall=True,
        ),
        "unparameterized-chamber-class",
        "b2+=1 chamber-fixed Bauer-Furuta status",
    )
    assert_equal(
        bauer_furuta_target_status(
            b1=0,
            b2_plus=3,
            homology_orientation=False,
            proper_monopole_map=True,
            chamber_fixed=True,
            avoids_reducible_wall=True,
        ),
        "invalid-missing-orientation-or-properness",
        "Bauer-Furuta needs orientation data",
    )
    assert_equal(
        bauer_furuta_target_status(
            b1=0,
            b2_plus=3,
            homology_orientation=True,
            proper_monopole_map=True,
            chamber_fixed=True,
            avoids_reducible_wall=False,
        ),
        "invalid-reducible-wall",
        "Bauer-Furuta gate rejects reducible-wall paths",
    )


def moore_witten_constant_exponent(chi_value: int, sigma_value: int) -> Fraction:
    return Fraction(2, 1) + Fraction(7 * chi_value + 11 * sigma_value, 4)


def check_moore_witten_constants_for_tables() -> None:
    # K3 has C_X = 2^0 in the common Moore-Witten normalization.
    assert_equal(
        moore_witten_constant_exponent(24, -16),
        Fraction(0),
        "K3 Moore-Witten exponent",
    )

    # E(n): chi = 12 n, sigma = -8 n, hence exponent 2 - n.
    for n in range(2, 8):
        assert_equal(
            moore_witten_constant_exponent(12 * n, -8 * n),
            Fraction(2 - n),
            "E(n) Moore-Witten exponent",
        )

    # Blow-up changes chi by +1 and sigma by -1, so the exponent drops by one.
    examples = [(24, -16), (36, -24), (48, -32), (7, -3)]
    for chi_value, sigma_value in examples:
        before = moore_witten_constant_exponent(chi_value, sigma_value)
        after = moore_witten_constant_exponent(chi_value + 1, sigma_value - 1)
        assert_equal(after, before - 1, "blow-up halves Moore-Witten constant")


def km_normal_form_surface_degree_terms(n: int) -> list[tuple[int, int, int]]:
    """Triples (j, ell, lambda_power) allowed by j + 2 ell <= n."""

    terms: list[tuple[int, int, int]] = []
    for j in range(n + 1):
        for ell in range((n - j) // 2 + 1):
            terms.append((j, ell, n - j - 2 * ell))
    return terms


def check_kotschick_morgan_degree_bookkeeping() -> None:
    for n in range(8):
        terms = km_normal_form_surface_degree_terms(n)
        for j, ell, lambda_power in terms:
            assert_equal(
                j + 2 * ell + lambda_power,
                n,
                "KM polynomial surface-degree bookkeeping",
            )
        # The leading monomial <lambda,h>^n is always present in the normal
        # form, and Q(h,h) can appear only when n >= 2.
        if (0, 0, n) not in terms:
            raise AssertionError("missing leading KM lambda monomial")
        if n < 2 and any(ell > 0 for _, ell, _ in terms):
            raise AssertionError("Q term appeared below surface degree two")


def check_donaldson_blowup_cosh_bookkeeping() -> None:
    # Under the comparison datum, the blow-up has two exceptional basic classes
    # K +/- E and the Moore-Witten constant is halved.  The two equal phases
    # therefore combine to (1/2)(e^t + e^{-t}) = cosh(t).  Check the first few
    # even Taylor coefficients as exact rationals.
    for m in range(5):
        cosh_coeff = Fraction(1, factorial(2 * m))
        combined_coeff = Fraction(1, 2) * (
            Fraction(1, factorial(2 * m)) + Fraction(1, factorial(2 * m))
        )
        assert_equal(combined_coeff, cosh_coeff, "Donaldson blow-up cosh coefficient")

    def gaussian_contact_coeff(power: int) -> Fraction:
        if power % 2 != 0:
            return Fraction(0)
        r = power // 2
        return Fraction((-1) ** r, (2**r) * factorial(r))

    def hyperbolic_coeff(branch: str, power: int) -> Fraction:
        if branch == "even":
            return Fraction(1, factorial(power)) if power % 2 == 0 else Fraction(0)
        if branch == "odd":
            return Fraction(1, factorial(power)) if power % 2 == 1 else Fraction(0)
        raise ValueError(f"unknown branch {branch!r}")

    def blowup_factor_coeff(branch: str, power: int) -> Fraction:
        return sum(
            gaussian_contact_coeff(contact_power)
            * hyperbolic_coeff(branch, power - contact_power)
            for contact_power in range(power + 1)
        )

    for m in range(6):
        even_formula = sum(
            Fraction((-1) ** r, (2**r) * factorial(r) * factorial(2 * m - 2 * r))
            for r in range(m + 1)
        )
        odd_formula = sum(
            Fraction(
                (-1) ** r,
                (2**r) * factorial(r) * factorial(2 * m + 1 - 2 * r),
            )
            for r in range(m + 1)
        )
        assert_equal(
            blowup_factor_coeff("even", 2 * m),
            even_formula,
            "Donaldson even-lift exceptional coefficient",
        )
        assert_equal(
            blowup_factor_coeff("even", 2 * m + 1),
            Fraction(0),
            "Donaldson even-lift odd exceptional coefficient",
        )
        assert_equal(
            blowup_factor_coeff("odd", 2 * m + 1),
            odd_formula,
            "Donaldson adjacent-lift exceptional coefficient",
        )
        assert_equal(
            blowup_factor_coeff("odd", 2 * m),
            Fraction(0),
            "Donaldson adjacent-lift even exceptional coefficient",
        )

    even_table = {0: Fraction(1), 2: Fraction(0), 4: Fraction(-1, 12)}
    odd_table = {1: Fraction(1), 3: Fraction(-1, 3), 5: Fraction(1, 20)}
    for power, expected in even_table.items():
        assert_equal(
            blowup_factor_coeff("even", power),
            expected,
            "Donaldson even-lift low-degree table",
        )
    for power, expected in odd_table.items():
        assert_equal(
            blowup_factor_coeff("odd", power),
            expected,
            "Donaldson adjacent-lift low-degree table",
        )


def check_donaldson_exponential_moment_reconstruction() -> None:
    # If F(t)=sum_i a_i exp(lambda_i t), the first N moments recover the
    # coefficients once the distinct weights lambda_i are known.
    weights = [Fraction(-2), Fraction(1), Fraction(3)]
    coefficients = [Fraction(5), Fraction(-7), Fraction(11)]
    moments = [
        sum(coefficient * (weight**power) for coefficient, weight in zip(coefficients, weights))
        for power in range(len(weights))
    ]
    vandermonde = [
        [weight**power for weight in weights]
        for power in range(len(weights))
    ]
    recovered = solve_linear_system(vandermonde, moments)
    assert_equal(recovered, coefficients, "Donaldson finite exponential moments")


def check_u_plane_wall_normal_delta_sequence() -> None:
    # For E_t(x)=erf(sqrt(pi t) x), the derivative is
    # 2 sqrt(t) exp(-pi t x^2).  Its total mass is exactly 2, and its second
    # moment is 1/(pi t).  We suppress the common pi^{-1} in the second
    # moment because the script uses rational arithmetic.
    for t in (1, 2, 5, 13):
        prefactor_squared = 4 * t
        gaussian_mass_squared = Fraction(1, t)
        total_mass_squared = prefactor_squared * gaussian_mass_squared
        second_moment_in_inverse_pi_units = Fraction(1, t)
        assert_equal(total_mass_squared, Fraction(4), "wall-normal jump mass squared")
        assert_equal(
            t * second_moment_in_inverse_pi_units,
            Fraction(1),
            "wall-normal second moment concentration",
        )

    left_chamber_sign = -1
    right_chamber_sign = 1
    assert_equal(
        right_chamber_sign - left_chamber_sign,
        2,
        "completed sign-factor chamber jump",
    )


def check_donaldson_sw_comparison_proof_obligation_map() -> None:
    # A finite Donaldson insertion test space sees the comparison as a
    # telescoping chain of linear functionals.  This is a proof-obligation map:
    # the differences become estimates only after the intermediate QFT
    # functionals and the corresponding bounds have been constructed.
    comparison = [
        Fraction(5, 7),
        Fraction(-3, 11),
        Fraction(13, 17),
        Fraction(-2, 19),
    ]
    residual_norm = [
        Fraction(1, 23),
        Fraction(-2, 29),
        Fraction(3, 31),
        Fraction(-1, 37),
    ]
    residual_singular = [
        Fraction(-2, 41),
        Fraction(1, 43),
        Fraction(5, 47),
        Fraction(-3, 53),
    ]
    residual_u_plane = [
        Fraction(3, 59),
        Fraction(4, 61),
        Fraction(-1, 67),
        Fraction(2, 71),
    ]
    residual_rg = [
        Fraction(-5, 73),
        Fraction(2, 79),
        Fraction(1, 83),
        Fraction(3, 89),
    ]
    residual_q = [
        Fraction(1, 97),
        Fraction(-1, 101),
        Fraction(2, 103),
        Fraction(-2, 107),
    ]

    monopole_raw = vector_add(comparison, residual_norm)
    split = vector_add(monopole_raw, residual_singular)
    coulomb = vector_add(split, residual_u_plane)
    asd = vector_add(coulomb, residual_rg)
    uv = vector_add(asd, residual_q)

    telescoped = vector_add(
        residual_q,
        residual_rg,
        residual_u_plane,
        residual_singular,
        residual_norm,
    )
    assert_equal(
        vector_sub(uv, comparison),
        telescoped,
        "Donaldson-SW comparison proof-obligation telescope",
    )

    test = [
        Fraction(2, 5),
        Fraction(-3, 7),
        Fraction(5, 9),
        Fraction(-7, 11),
    ]
    discrepancy = dot(vector_sub(uv, comparison), test)
    residual_sum = sum(
        dot(residual, test)
        for residual in (
            residual_q,
            residual_rg,
            residual_u_plane,
            residual_singular,
            residual_norm,
        )
    )
    assert_equal(
        discrepancy,
        residual_sum,
        "Donaldson-SW proof-obligation map evaluates on finite tests",
    )

    bound = sum(
        l1_norm(residual) * linfty_norm(test)
        for residual in (
            residual_q,
            residual_rg,
            residual_u_plane,
            residual_singular,
            residual_norm,
        )
    )
    _assert_leq(
        "Donaldson-SW conditional residual norm propagation",
        abs(discrepancy),
        bound,
    )

    omitted_singular = vector_add(
        residual_q,
        residual_rg,
        residual_u_plane,
        residual_norm,
    )
    omitted_discrepancy = dot(omitted_singular, test)
    if omitted_discrepancy == discrepancy:
        raise AssertionError(
            "omitting the singular-fiber replacement difference should not "
            "preserve the same finite-test discrepancy"
        )

    shifted_target = vector_add(comparison, residual_singular)
    assert_equal(
        vector_sub(uv, shifted_target),
        omitted_singular,
        "dropping one proof-obligation arrow changes the comparison target",
    )
    if shifted_target == comparison:
        raise AssertionError("absorbed singular residual left the target unchanged")

    # If every comparison arrow is exact, the UV and SW functionals agree on
    # the finite test space.
    exact_uv = comparison[:]
    assert_equal(
        dot(vector_sub(exact_uv, comparison), test),
        Fraction(0),
        "zero residuals give exact finite Donaldson-SW comparison",
    )


def factorial(n: int) -> int:
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value


def check_trace_delta_action_normalization() -> None:
    # The BPST normalization used elsewhere in the repository gives
    # integral tr_delta(F wedge *F) = 8 pi^2 for k = 1.  With the monograph
    # action (2 g_YM^2)^(-1) integral tr(F wedge *F), this is 4 pi^2/g_YM^2.
    form_norm_units = 8
    action_units = Fraction(form_norm_units, 2)
    assert_equal(action_units, 4, "trace-delta instanton action coefficient")


def main() -> None:
    check_asd_index_formula()
    check_sw_index_formula()
    check_topological_identity_in_sw_dimension()
    check_feehan_leness_theorem_status_gate()
    check_donaldson_degree_bookkeeping()
    check_spinc_characteristic_lift_bookkeeping()
    check_sw_simple_type_examples()
    check_blowup_simple_type_square_shift()
    check_elliptic_surface_binomial_coefficients()
    check_furuta_examples()
    check_bauer_furuta_theorem_boundary_gate()
    check_moore_witten_constants_for_tables()
    check_kotschick_morgan_degree_bookkeeping()
    check_donaldson_blowup_cosh_bookkeeping()
    check_donaldson_exponential_moment_reconstruction()
    check_u_plane_wall_normal_delta_sequence()
    check_donaldson_sw_comparison_proof_obligation_map()
    check_trace_delta_action_normalization()
    print("Donaldson-Witten and Seiberg-Witten comparison checks passed.")


if __name__ == "__main__":
    main()
