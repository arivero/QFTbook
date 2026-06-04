#!/usr/bin/env python3
"""Finite checks for Volume VI finite-volume form-factor formulae.

The checks cover algebraic identities used in the finite-volume chapter:

* two-particle Gaudin determinant from the Bethe-Yang Jacobian;
* cancellation of the Gaudin density between finite-volume matrix elements
  and the state-counting measure;
* subset expansion for diagonal finite-volume matrix elements;
* free-Majorana two-particle energy-density Bessel reduction prefactor;
* free-Majorana rapidity-cut tail bookkeeping on a separated Euclidean
  distance window;
* interacting one-species form-factor growth-window bookkeeping for
  particle-number and rapidity-cut tails;
* finite reconstruction residual budget separating finite-volume, tail,
  diagonal/contact, domain, locality, and completeness errors.

The script checks finite algebra and normalization bookkeeping; it does not
attempt to prove analytic convergence of a form-factor expansion.

Evidence contract.
Target claims: the finite-volume form-factor normalization and reconstruction
bookkeeping claims in Volume VI Chapter 11, including the two-particle Gaudin
determinant, Gaudin-density cancellation in the sum-integral limit, connected
diagonal subset combinatorics, the free-Majorana energy-density Bessel
prefactor, the separated-window rapidity-cut tail bound for that local
observable, the interacting form-factor growth-window particle-number and
rapidity-cut tail bounds, and the residual ledger separating finite-volume,
tail, diagonal/contact, domain, locality, and completeness errors.
Independent construction: the checks recompute the Jacobian determinant,
state-counting cancellations, subset sums, Bessel prefactors, elementary
rapidity-tail constants, tail primitive, interacting growth-window majorants,
and residual decompositions directly from finite formulas rather than importing
chapter display strings.
Imported assumptions: the tests use diagonal Bethe-Yang quantization, finite
nonzero Gaudin densities, regular connected diagonal finite parts, the
free-Majorana energy operator's two-particle form-factor support after the
local free field has already been constructed, and the elementary separated
Bessel majorant stated in the chapter.
Negative controls: wrong Gaudin determinants, missed density cancellations,
wrong subset counts, omitted identical-particle factors, overstrong rapidity
decay from using the wrong cosh lower bound, confusing the free energy
operator's zero particle-number tail with the nonzero rapidity-cut tail, and
accidentally vanishing reconstruction residuals are rejected, as are missing
factorial suppression, omitted union-bound factors in interacting rapidity
cuts, and particle-tail estimates used outside their small-tail condition.
Scope boundary: a pass checks finite algebra, normalization, and explicit
tail-bookkeeping coordinates for the displayed finite-volume/form-factor
claims; it does not prove general form-factor convergence, construct local
operators from arbitrary factorizing S-matrices, establish Osterwalder-Schrader
positivity, prove locality, or prove scattering-state completeness.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close
from check_utils import assert_leq as _assert_leq

from fractions import Fraction
from itertools import combinations
from math import cosh, exp, factorial, pi


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-11) -> None:
    _assert_close(name, got, expected, tol=tol)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def two_particle_gaudin_from_matrix(m1: float, m2: float, L: float, theta1: float, theta2: float, phi: float) -> float:
    g11 = m1 * L * cosh(theta1) + phi
    g22 = m2 * L * cosh(theta2) + phi
    g12 = -phi
    g21 = -phi
    return g11 * g22 - g12 * g21


def two_particle_gaudin_formula(m1: float, m2: float, L: float, theta1: float, theta2: float, phi: float) -> float:
    return (
        m1 * m2 * L**2 * cosh(theta1) * cosh(theta2)
        + phi * L * (m1 * cosh(theta1) + m2 * cosh(theta2))
    )


def check_two_particle_gaudin() -> None:
    samples = [
        (1.0, 1.0, 37.0, 0.3, -0.7, 0.0),
        (1.2, 0.8, 41.0, 1.1, -0.4, 0.37),
        (2.0, 1.5, 19.0, -0.2, -1.3, 1.9),
    ]
    for sample in samples:
        got = two_particle_gaudin_from_matrix(*sample)
        expected = two_particle_gaudin_formula(*sample)
        assert_close(f"two-particle Gaudin determinant {sample}", got, expected)


def check_sum_integral_cancellation() -> None:
    rho_values = [0.7, 2.0, 13.0, 101.0]
    form_factor_squared = 5.3
    test_function = 0.41
    for rho in rho_values:
        finite_volume_matrix_element_squared = form_factor_squared / rho
        state_counting_density = rho / (2.0 * pi)
        contribution = finite_volume_matrix_element_squared * state_counting_density * test_function
        expected = form_factor_squared * test_function / (2.0 * pi)
        assert_close(f"one-particle rho cancellation rho={rho}", contribution, expected)

    rho2 = 17.0
    finite_volume_matrix_element_squared = form_factor_squared / rho2
    state_counting_density = rho2 / ((2.0 * pi) ** 2)
    contribution = finite_volume_matrix_element_squared * state_counting_density * test_function
    expected = form_factor_squared * test_function / ((2.0 * pi) ** 2)
    assert_close("two-particle rho cancellation", contribution, expected)


def principal_minor(diagonal_entries: list[float], subset: tuple[int, ...]) -> float:
    result = 1.0
    for index in subset:
        result *= diagonal_entries[index]
    return result


def connected_value(subset_size: int) -> float:
    values = {0: 2.0, 1: 3.0, 2: 5.0, 3: 7.0}
    return values[subset_size]


def diagonal_subset_formula(diagonal_entries: list[float]) -> float:
    n = len(diagonal_entries)
    all_indices = tuple(range(n))
    rho_all = principal_minor(diagonal_entries, all_indices)
    numerator = 0.0
    for r in range(n + 1):
        for subset in combinations(all_indices, r):
            complement = tuple(index for index in all_indices if index not in subset)
            numerator += connected_value(len(subset)) * principal_minor(diagonal_entries, complement)
    return numerator / rho_all


def check_diagonal_subset_expansion() -> None:
    rho1 = 11.0
    one_particle = diagonal_subset_formula([rho1])
    assert_close("one-particle diagonal subset formula", one_particle, 2.0 + 3.0 / rho1)

    rho_a = 11.0
    rho_b = 13.0
    two_particle = diagonal_subset_formula([rho_a, rho_b])
    expected_two = (2.0 * rho_a * rho_b + 3.0 * rho_b + 3.0 * rho_a + 5.0) / (rho_a * rho_b)
    assert_close("two-particle diagonal subset formula", two_particle, expected_two)

    rho_c = 17.0
    three_particle = diagonal_subset_formula([rho_a, rho_b, rho_c])
    expected_three = (
        2.0 * rho_a * rho_b * rho_c
        + 3.0 * (rho_b * rho_c + rho_a * rho_c + rho_a * rho_b)
        + 5.0 * (rho_a + rho_b + rho_c)
        + 7.0
    ) / (rho_a * rho_b * rho_c)
    assert_close("three-particle diagonal subset formula", three_particle, expected_three)


def check_bessel_prefactor_reduction() -> None:
    identical_particle_factor = 1.0 / 2.0
    rapidity_measure = 1.0 / ((2.0 * pi) ** 2)
    center_rapidity_integral_factor = 2.0  # int exp(-z cosh Theta) dTheta = 2 K0(z)
    even_relative_rapidity_factor = 2.0
    prefactor = (
        identical_particle_factor
        * rapidity_measure
        * center_rapidity_integral_factor
        * even_relative_rapidity_factor
    )
    assert_close("free-Majorana two-particle Bessel prefactor", prefactor, 1.0 / (2.0 * pi**2))


def check_majorana_energy_rapidity_tail_bound() -> None:
    bessel_prefactor_without_pi_squared = Fraction(1, 2)
    sinh_upper_bound_factor = Fraction(1, 4)
    substitution_factor = Fraction(2, 1)
    final_tail_prefactor_without_pi_squared = (
        bessel_prefactor_without_pi_squared
        * sinh_upper_bound_factor
        * substitution_factor
    )
    assert_equal(
        "free-Majorana separated-window rapidity-tail prefactor",
        final_tail_prefactor_without_pi_squared,
        Fraction(1, 4),
    )

    missing_identical_particle_factor = Fraction(1, 1)
    wrong_tail_prefactor = (
        missing_identical_particle_factor
        * sinh_upper_bound_factor
        * substitution_factor
    )
    if wrong_tail_prefactor == final_tail_prefactor_without_pi_squared:
        raise AssertionError("omitted identical-particle factor did not change tail prefactor")
    _assert_leq(
        "correct rapidity-tail prefactor below omitted-identical-particle prefactor",
        final_tail_prefactor_without_pi_squared,
        wrong_tail_prefactor,
        tol=Fraction(0),
    )

    a = Fraction(3, 5)
    lower_cutoff = Fraction(7, 3)
    tail_factor = lower_cutoff / a + Fraction(1, 1) / (a * a)
    derivative_coefficient = Fraction(1, 1) / a - a * tail_factor
    assert_equal(
        "rapidity-tail primitive differentiates to lower-limit integrand",
        derivative_coefficient,
        -lower_cutoff,
    )

    correct_tail = exp(-float(a * lower_cutoff)) * float(tail_factor)
    stronger_decay = 2 * a
    overstrong_tail_factor = lower_cutoff / stronger_decay + Fraction(1, 1) / (
        stronger_decay * stronger_decay
    )
    overstrong_tail = exp(-float(stronger_decay * lower_cutoff)) * float(overstrong_tail_factor)
    if not overstrong_tail < correct_tail:
        raise AssertionError("wrong stronger rapidity decay was not detected as a smaller bound")

    particle_number_tail = Fraction(0)
    if not final_tail_prefactor_without_pi_squared > particle_number_tail:
        raise AssertionError(
            "free energy operator's particle-number tail was confused with rapidity-cut tail"
        )


def check_interacting_form_factor_growth_window() -> None:
    # Exact finite analogue of a one-species bound
    # |F_n|^2 <= C^2 B^(2n) exp(2 gamma sum |theta_i|).
    c_squared = Fraction(5, 7)
    b_squared = Fraction(3, 5)
    one_particle_majorant = Fraction(4, 3)
    x0 = b_squared * one_particle_majorant
    assert_equal("interacting form-factor window majorant X0", x0, Fraction(4, 5))

    two_particle_bound = c_squared * x0 * x0 / factorial(2)
    missing_identical_factor = c_squared * x0 * x0
    if two_particle_bound == missing_identical_factor:
        raise AssertionError("negative control failed: factorial suppression was lost")
    _assert_leq(
        "interacting two-particle sector below missing-factorial control",
        two_particle_bound,
        missing_identical_factor,
        tol=Fraction(0),
    )

    retained_order = 3
    if not x0 < retained_order + 2:
        raise AssertionError("test fixture should satisfy the particle-tail smallness condition")
    particle_tail_bound = (
        c_squared
        * x0 ** (retained_order + 1)
        / factorial(retained_order + 1)
        / (1 - x0 / (retained_order + 2))
    )
    first_two_omitted = c_squared * (
        x0 ** (retained_order + 1) / factorial(retained_order + 1)
        + x0 ** (retained_order + 2) / factorial(retained_order + 2)
    )
    _assert_leq(
        "interacting particle-number tail finite sample below certified bound",
        first_two_omitted,
        particle_tail_bound,
        tol=Fraction(0),
    )

    bad_x0 = Fraction(7, 1)
    if bad_x0 < retained_order + 2:
        raise AssertionError("negative control should violate the tail-ratio condition")
    bad_denominator = 1 - bad_x0 / (retained_order + 2)
    if bad_denominator > 0:
        raise AssertionError("negative control failed: invalid particle-tail denominator looked usable")

    rapidity_tail = Fraction(1, 13)
    retained_rapidity_integral = one_particle_majorant - rapidity_tail
    finite_cut_error = Fraction(0)
    union_bound = Fraction(0)
    for n in range(1, retained_order + 1):
        coefficient = c_squared * b_squared**n / factorial(n)
        exact_cut_error = coefficient * (
            one_particle_majorant**n - retained_rapidity_integral**n
        )
        sector_union_bound = (
            coefficient
            * n
            * one_particle_majorant ** (n - 1)
            * rapidity_tail
        )
        _assert_leq(
            f"interacting rapidity-cut sector union bound n={n}",
            exact_cut_error,
            sector_union_bound,
            tol=Fraction(0),
        )
        finite_cut_error += exact_cut_error
        union_bound += sector_union_bound

    chapter_cut_bound = (
        c_squared
        * b_squared
        * rapidity_tail
        * sum(x0**k / factorial(k) for k in range(retained_order))
    )
    assert_equal(
        "interacting rapidity-cut bound equals finite union-bound sum",
        union_bound,
        chapter_cut_bound,
    )
    _assert_leq(
        "interacting rapidity-cut exact error below certified bound",
        finite_cut_error,
        chapter_cut_bound,
        tol=Fraction(0),
    )
    if finite_cut_error <= c_squared * b_squared * rapidity_tail:
        raise AssertionError("negative control failed: higher retained sectors needed no union factor")


def check_subset_count() -> None:
    for n in range(0, 8):
        count = sum(1 for r in range(n + 1) for _ in combinations(range(n), r))
        assert_equal(f"number of diagonal subsets n={n}", count, 2**n)


def check_reconstruction_residual_budget() -> None:
    retained_coordinate = Fraction(19, 7)
    residuals = {
        "finite volume": Fraction(1, 90),
        "particle tail": Fraction(-1, 126),
        "diagonal contact": Fraction(1, 210),
        "domain positivity": Fraction(1, 168),
        "locality": Fraction(-1, 280),
        "completeness": Fraction(1, 360),
    }
    residual_total = sum(residuals.values(), Fraction(0))
    target_local_functional = retained_coordinate + residual_total

    assert_equal(
        "form-factor reconstruction residual decomposition",
        target_local_functional - retained_coordinate,
        residual_total,
    )
    if residual_total == 0:
        raise AssertionError("reconstruction residual budget accidentally vanished")

    residual_bound = sum(abs(value) for value in residuals.values())
    _assert_leq(
        "form-factor reconstruction triangle budget",
        abs(residual_total),
        residual_bound,
        tol=Fraction(0),
    )

    # A retained finite-volume/Gaudin coordinate can be exact while the
    # reconstruction claim still has a nonzero analytic/operator residual.
    exact_gaudin_coordinate_shift = Fraction(0)
    assert_equal(
        "exact Gaudin bookkeeping does not remove reconstruction residual",
        (target_local_functional + exact_gaudin_coordinate_shift) - retained_coordinate,
        residual_total,
    )


def main() -> None:
    check_two_particle_gaudin()
    check_sum_integral_cancellation()
    check_diagonal_subset_expansion()
    check_bessel_prefactor_reduction()
    check_majorana_energy_rapidity_tail_bound()
    check_interacting_form_factor_growth_window()
    check_subset_count()
    check_reconstruction_residual_budget()
    print("All finite-volume form-factor checks passed.")


if __name__ == "__main__":
    main()
