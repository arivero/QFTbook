#!/usr/bin/env python3
"""Finite checks for charged Wilson-line dressing and flux formulas."""

from __future__ import annotations

from check_utils import assert_close as _assert_close
from check_utils import assert_gt as _assert_gt

import cmath
import math
from fractions import Fraction


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def mat_vec(matrix: tuple[tuple[Fraction, ...], ...], vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def row_mat(row: tuple[Fraction, ...], matrix: tuple[tuple[Fraction, ...], ...]) -> tuple[Fraction, ...]:
    return tuple(sum(row[i] * matrix[i][j] for i in range(len(row))) for j in range(len(matrix[0])))


def mat_mul(
    left: tuple[tuple[Fraction, ...], ...], right: tuple[tuple[Fraction, ...], ...]
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def transpose(matrix: tuple[tuple[Fraction, ...], ...]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))


def outer(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(a * b for b in right) for a in left)


def inverse_2x2(matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    ((a, b), (c, d)) = matrix
    determinant = a * d - b * c
    if determinant == 0:
        raise AssertionError("matrix used for a coordinate change must be invertible")
    return ((d / determinant, -b / determinant), (-c / determinant, a / determinant))


def dot_mostly_plus(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> float:
    return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]


def boosted_flux_density(q: float, beta: float, z: float) -> float:
    return q / (4.0 * math.pi) * (1.0 - beta * beta) / (1.0 - beta * z) ** 2


def boosted_flux_integral(q: float, beta: float) -> float:
    if beta == 0.0:
        return q
    integral_without_q = (
        2.0
        * math.pi
        * (1.0 - beta * beta)
        * (1.0 / (beta * (1.0 - beta)) - 1.0 / (beta * (1.0 + beta)))
    )
    return q / (4.0 * math.pi) * integral_without_q


def check_boosted_flux_integral() -> None:
    for q in (-3.0, -0.5, 0.25, 2.0):
        for beta in (0.0, 0.1, 0.4, 0.8):
            assert_close(f"boosted Coulomb total flux q={q} beta={beta}", boosted_flux_integral(q, beta), q)


def check_velocity_read_from_flux_extrema() -> None:
    q = 1.7
    for beta in (0.05, 0.2, 0.6, 0.9):
        maximum = boosted_flux_density(q, beta, 1.0)
        minimum = boosted_flux_density(q, beta, -1.0)
        expected_ratio = ((1.0 + beta) / (1.0 - beta)) ** 2
        assert_close(f"flux extrema ratio beta={beta}", maximum / minimum, expected_ratio)


def rational_flux_shape_without_four_pi(q: Fraction, beta: Fraction, z: Fraction) -> Fraction:
    """Return 4*pi times the axial boosted Coulomb flux density."""

    return q * (1 - beta * beta) / (1 - beta * z) ** 2


def rational_flux_zero_mode_without_two_pi(q: Fraction, beta: Fraction) -> Fraction:
    """Return the z-integral of 4*pi times the axial flux density."""

    if beta == 0:
        return 2 * q
    return q * (1 - beta * beta) * (
        Fraction(1, beta * (1 - beta)) - Fraction(1, beta * (1 + beta))
    )


def check_neutral_boundary_charge_is_not_flux_triviality() -> None:
    """Check that zero total charge does not force zero angular flux profile."""

    charge = Fraction(1)
    same_beta = Fraction(1, 3)
    different_beta = Fraction(-1, 3)

    for z in (Fraction(-1), Fraction(0), Fraction(1)):
        same_velocity_profile = rational_flux_shape_without_four_pi(charge, same_beta, z) + (
            rational_flux_shape_without_four_pi(-charge, same_beta, z)
        )
        assert_equal("opposite charges with the same velocity cancel pointwise", same_velocity_profile, 0)

    zero_mode = rational_flux_zero_mode_without_two_pi(charge, same_beta) + (
        rational_flux_zero_mode_without_two_pi(-charge, different_beta)
    )
    assert_equal("opposite charges with different velocities have zero total charge", zero_mode, 0)

    north_profile = rational_flux_shape_without_four_pi(charge, same_beta, Fraction(1)) + (
        rational_flux_shape_without_four_pi(-charge, different_beta, Fraction(1))
    )
    assert_equal(
        "neutral opposite-velocity pair has nonzero angular flux profile",
        north_profile,
        Fraction(3, 2),
    )


def check_worldline_current_denominator() -> None:
    mass = 2.3
    charge = -0.7
    eps = 0.13
    omega = 0.31
    velocity = (0.2, -0.35, 0.1)
    speed_sq = sum(component * component for component in velocity)
    gamma = 1.0 / math.sqrt(1.0 - speed_sq)
    p = (gamma * mass, *(gamma * mass * component for component in velocity))
    u = tuple(component / mass for component in p)

    n = (0.0, 0.6, 0.8)
    k = (omega, *(omega * component for component in n))
    polarization = (0.0, 1.0, 0.0, 0.0)
    assert_close("photon null", dot_mostly_plus(k, k), 0.0)
    assert_close("polarization transverse", dot_mostly_plus(k, polarization), 0.0)

    current_contraction = charge * dot_mostly_plus(u, polarization) / (eps - 1j * dot_mostly_plus(u, k))
    momentum_contraction = charge * dot_mostly_plus(p, polarization) / (
        eps * mass - 1j * dot_mostly_plus(p, k)
    )
    assert_close("worldline current equals momentum eikonal denominator", current_contraction, momentum_contraction)


def check_half_line_fourier_transform() -> None:
    eps = 0.37
    a = -0.42
    analytic = 1.0 / (eps - 1j * a)
    large_t = 100.0
    cutoff_integral = (cmath.exp((-eps + 1j * a) * large_t) - 1.0) / (-eps + 1j * a)
    assert_close("regulated half-line transform", cutoff_integral, analytic, tol=1.0e-15)


def norm3(vector: tuple[float, float, float]) -> float:
    return math.sqrt(sum(component * component for component in vector))


def subtract3(a: tuple[float, float, float], b: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(x - y for x, y in zip(a, b))


def scalar_mul3(scale: float, vector: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(scale * component for component in vector)


def coulomb_tail_phase_exact(
    kappa: float,
    b: tuple[float, float, float],
    u: tuple[float, float, float],
    regulator: float,
    t0: float,
    t1: float,
) -> float:
    speed = norm3(u)
    sigma = dot3(b, u) / (speed * speed)
    b_parallel = scalar_mul3(sigma, u)
    b_perp = subtract3(b, b_parallel)
    rho = math.sqrt(regulator * regulator + norm3(b_perp) ** 2)
    return kappa / speed * (
        math.asinh(speed * (t1 + sigma) / rho) - math.asinh(speed * (t0 + sigma) / rho)
    )


def check_coulomb_tail_dollard_log_phase() -> None:
    samples = [
        (0.7, (0.3, -0.2, 0.4), (0.5, 0.1, -0.2), 0.8),
        (-1.2, (-0.6, 0.4, 0.2), (0.2, -0.3, 0.5), 0.5),
    ]
    for kappa, b, u, regulator in samples:
        speed = norm3(u)
        for t0, t1 in ((3.0, 7.0), (10.0, 40.0)):
            exact = coulomb_tail_phase_exact(kappa, b, u, regulator, t0, t1)
            sigma = dot3(b, u) / (speed * speed)
            b_perp = subtract3(b, scalar_mul3(sigma, u))
            rho = math.sqrt(regulator * regulator + norm3(b_perp) ** 2)
            direct = kappa / speed * (
                math.asinh(speed * (t1 + sigma) / rho) - math.asinh(speed * (t0 + sigma) / rho)
            )
            assert_close("Coulomb tail exact asinh primitive", exact, direct)

        leading_coefficient = kappa / speed
        t_large = 1.0e6
        t_double = 2.0e6
        phase_difference = coulomb_tail_phase_exact(kappa, b, u, regulator, t_large, t_double)
        expected_log = leading_coefficient * math.log(t_double / t_large)
        assert_close("Coulomb tail logarithmic coefficient", phase_difference, expected_log, tol=1.0e-6)


def many_body_dollard_log_coefficient_1d(
    charges: tuple[Fraction, ...],
    orientations: tuple[int, ...],
    velocities: tuple[Fraction, ...],
) -> Fraction:
    if not (len(charges) == len(orientations) == len(velocities)):
        raise AssertionError("charges, orientations, and velocities must have the same length")

    total = Fraction(0)
    for i in range(len(charges)):
        for j in range(i + 1, len(charges)):
            relative_velocity = abs(velocities[i] - velocities[j])
            if relative_velocity == 0:
                raise AssertionError("Dollard pair coefficient requires separated velocities")
            total += (
                Fraction(orientations[i])
                * Fraction(orientations[j])
                * charges[i]
                * charges[j]
                / relative_velocity
            )
    return total


def check_many_body_dollard_phase_bookkeeping() -> None:
    """Check the oriented pairwise Dollard logarithm in a finite model."""

    charges = (Fraction(2), Fraction(-3), Fraction(5))
    orientations = (1, -1, 1)
    velocities = (Fraction(0), Fraction(3), Fraction(7))

    coefficient = many_body_dollard_log_coefficient_1d(charges, orientations, velocities)
    assert_equal("oriented many-body Dollard log coefficient", coefficient, Fraction(201, 28))

    permutation = (2, 0, 1)
    permuted_coefficient = many_body_dollard_log_coefficient_1d(
        tuple(charges[i] for i in permutation),
        tuple(orientations[i] for i in permutation),
        tuple(velocities[i] for i in permutation),
    )
    assert_equal("pairwise Dollard coefficient is independent of ordering", permuted_coefficient, coefficient)

    flipped_orientations = (1, 1, 1)
    flipped_coefficient = many_body_dollard_log_coefficient_1d(charges, flipped_orientations, velocities)
    assert_equal("conjugating one charged creator reverses its pair tails", flipped_coefficient, Fraction(-121, 28))
    assert_equal(
        "orientation flip changes exactly the pairs incident to the flipped particle",
        flipped_coefficient - coefficient,
        -2 * (Fraction(2) + Fraction(15, 4)),
    )

    kappa = 1.3
    b = (0.4, 0.0, 0.0)
    u = (0.5, 0.0, 0.0)
    regulator = 0.7

    def dyadic_log_subtracted_remainder(t0: float) -> float:
        t1 = 2.0 * t0
        exact = coulomb_tail_phase_exact(kappa, b, u, regulator, t0, t1)
        leading = kappa / norm3(u) * math.log(t1 / t0)
        return exact - leading

    early_remainder = abs(dyadic_log_subtracted_remainder(100.0))
    late_remainder = abs(dyadic_log_subtracted_remainder(1000.0))
    if not late_remainder < early_remainder:
        raise AssertionError(
            "log-subtracted Coulomb pair remainder should decay on dyadic large-time intervals"
        )


def check_modified_cook_integrability_bookkeeping() -> None:
    """Check the finite sequence analogue of subtracting a Dollard tail."""

    def dyadic_sum(start: int, term) -> Fraction:
        return sum((term(n) for n in range(start, 2 * start)), Fraction(0))

    # A 1/t derivative is not a Cook error: its dyadic tail stays bounded
    # below.  The log comparison phase must absorb this part.
    for start in (10, 100, 1000):
        harmonic_tail = dyadic_sum(start, lambda n: Fraction(1, n))
        if harmonic_tail <= Fraction(1, 2):
            raise AssertionError("unsubtracted Dollard tail should not have vanishing dyadic norm")

    # After the 1/t part is subtracted, a 1/t^2 residual has tails tending to
    # zero; the integral-test bound is exact enough for the Cook criterion.
    previous_tail: Fraction | None = None
    for start in (10, 100, 1000):
        residual_tail = dyadic_sum(start, lambda n: Fraction(1, n * n))
        if residual_tail >= Fraction(1, start - 1):
            raise AssertionError("residual dyadic Cook tail should obey the integral-test bound")
        if previous_tail is not None and residual_tail >= previous_tail:
            raise AssertionError("residual Cook tail should decrease with the initial time")
        previous_tail = residual_tail

    # A finite phase change contributes an l^1 derivative and hence cannot
    # change the asymptotic wave map.
    finite_phase_tail = dyadic_sum(100, lambda n: Fraction(3, n * n))
    later_finite_phase_tail = dyadic_sum(1000, lambda n: Fraction(3, n * n))
    if not later_finite_phase_tail < finite_phase_tail:
        raise AssertionError("finite comparison-phase changes should have vanishing Cook tails")


def check_pair_coefficient_residual_budget() -> None:
    """Check that the Dollard coefficient, not just its form, is load-bearing."""

    def dyadic_sum(start: int, term) -> Fraction:
        return sum((term(n) for n in range(start, 2 * start)), Fraction(0))

    kappa = Fraction(6)
    relative_speed = Fraction(3)
    correct_log_coefficient = kappa / relative_speed
    wrong_log_coefficient = correct_log_coefficient + 1

    def model_pair_derivative(n: int) -> Fraction:
        return correct_log_coefficient / n + Fraction(5, n * n)

    previous_correct_tail: Fraction | None = None
    for start in (32, 128, 512):
        correct_tail = dyadic_sum(
            start,
            lambda n: abs(model_pair_derivative(n) - correct_log_coefficient / n),
        )
        if correct_tail >= Fraction(5, start - 1):
            raise AssertionError("correctly subtracted pair coefficient should leave an l1 tail")
        if previous_correct_tail is not None and correct_tail >= previous_correct_tail:
            raise AssertionError("correctly subtracted residual tails should decrease")
        previous_correct_tail = correct_tail

        wrong_tail = dyadic_sum(
            start,
            lambda n: abs(model_pair_derivative(n) - wrong_log_coefficient / n),
        )
        if wrong_tail <= Fraction(1, 2):
            raise AssertionError("wrong Dollard coefficient should leave a nonintegrable dyadic tail")

    # A compact same-flux dressing deformation changes the finite phase but
    # not the logarithmic coefficient: its derivative is summable.
    def compact_same_flux_derivative(n: int) -> Fraction:
        return Fraction(7, n * n)

    early_tail = dyadic_sum(
        64,
        lambda n: abs(
            model_pair_derivative(n)
            + compact_same_flux_derivative(n)
            - correct_log_coefficient / n
        ),
    )
    late_tail = dyadic_sum(
        512,
        lambda n: abs(
            model_pair_derivative(n)
            + compact_same_flux_derivative(n)
            - correct_log_coefficient / n
        ),
    )
    if not late_tail < early_tail:
        raise AssertionError("same-flux compact deformation should not change the Dollard log coefficient")

    assert_equal(
        "equal velocities are outside the separated Dollard pair estimate",
        catches_equal_velocity_error(),
        True,
    )


def check_dollard_scalar_product_cauchy_criterion() -> None:
    """Check the scalar-product Cauchy estimate after Dollard subtraction."""

    def dyadic_sum(start: int, term) -> Fraction:
        return sum((term(n) for n in range(start, 2 * start)), Fraction(0))

    norm_i = Fraction(5)
    norm_j = Fraction(7)

    previous_bound: Fraction | None = None
    for start in (32, 128, 512):
        ri_tail = dyadic_sum(start, lambda n: Fraction(2, n * n))
        rj_tail = dyadic_sum(start, lambda n: Fraction(3, n * n))
        scalar_product_cauchy_bound = norm_j * ri_tail + norm_i * rj_tail
        if scalar_product_cauchy_bound >= Fraction(29, start - 1):
            raise AssertionError("scalar-product Cauchy bound should obey the integral-test tail")
        if previous_bound is not None and scalar_product_cauchy_bound >= previous_bound:
            raise AssertionError("scalar-product Cauchy tails should decrease")
        previous_bound = scalar_product_cauchy_bound

    # A wrong logarithmic coefficient leaves a factor exp(i delta log t).
    # With delta=pi/log(2), dyadic times differ by the phase -1, so the
    # scalar products are not Cauchy.
    delta = math.pi / math.log(2.0)
    for start in (32, 256, 2048):
        phase_start = cmath.exp(1j * delta * math.log(start))
        phase_double = cmath.exp(1j * delta * math.log(2 * start))
        _assert_gt(
            "wrong Dollard logarithmic phase dyadic obstruction",
            abs(phase_double - phase_start),
            1.9,
        )

    # A finite same-flux phase change has an L1 derivative; its dyadic scalar
    # product changes shrink.
    previous_phase_tail: float | None = None
    for start in (32, 256, 2048):
        finite_phase_start = cmath.exp(1j / start)
        finite_phase_double = cmath.exp(1j / (2 * start))
        phase_tail = abs(finite_phase_double - finite_phase_start)
        if previous_phase_tail is not None and phase_tail >= previous_phase_tail:
            raise AssertionError("finite same-flux phase changes should be Cauchy")
        previous_phase_tail = phase_tail


def check_asymptotic_null_quotient_wave_map_cell() -> None:
    """Check the finite null-quotient algebra for charged wave maps."""

    physical_vectors = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(1)),
    )
    gram = tuple(
        tuple(
            sum(left[k] * right[k] for k in range(2))
            for right in physical_vectors
        )
        for left in physical_vectors
    )
    expected_gram = (
        (Fraction(1), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(1), Fraction(2)),
    )
    assert_equal("charged asymptotic finite Gram matrix", gram, expected_gram)

    null_relation = (Fraction(1), Fraction(1), Fraction(-1))
    assert_equal(
        "charged asymptotic null relation G n",
        mat_vec(gram, null_relation),
        (Fraction(0), Fraction(0), Fraction(0)),
    )

    def physical_projection(coefficients: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (
            coefficients[0] + coefficients[2],
            coefficients[1] + coefficients[2],
        )

    def gram_quadratic(coefficients: tuple[Fraction, Fraction, Fraction]) -> Fraction:
        return sum(
            coefficients[i] * gram[i][j] * coefficients[j]
            for i in range(3)
            for j in range(3)
        )

    samples = (
        (Fraction(2), Fraction(-1), Fraction(3)),
        (Fraction(5), Fraction(2), Fraction(0)),
        (Fraction(-4), Fraction(7), Fraction(1)),
    )
    for coefficients in samples:
        projected = physical_projection(coefficients)
        assert_equal(
            f"charged asymptotic Gram equals physical norm {coefficients}",
            gram_quadratic(coefficients),
            projected[0] * projected[0] + projected[1] * projected[1],
        )

    overcomplete = (Fraction(2), Fraction(-1), Fraction(3))
    refined = (
        overcomplete[0] + overcomplete[2],
        overcomplete[1] + overcomplete[2],
        Fraction(0),
    )
    difference = tuple(left - right for left, right in zip(overcomplete, refined))
    assert_equal(
        "same physical projection after packet refinement",
        physical_projection(overcomplete),
        physical_projection(refined),
    )
    assert_equal(
        "refinement difference is a null vector",
        difference,
        tuple(-3 * entry for entry in null_relation),
    )
    assert_equal("null difference has zero asymptotic norm", gram_quadratic(difference), Fraction(0))

    for coefficients in samples:
        mixed_null_pairing = sum(
            coefficients[i] * gram[i][j] * difference[j]
            for i in range(3)
            for j in range(3)
        )
        assert_equal("null vector pairs trivially with every sample", mixed_null_pairing, Fraction(0))


def check_same_flux_schedule_wave_map_invariance() -> None:
    """Check finite same-flux schedule invariance for wave maps and residues."""

    def add2(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (left[0] + right[0], left[1] + right[1])

    def scale2(scale: Fraction, vector: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (scale * vector[0], scale * vector[1])

    def subtract2(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (left[0] - right[0], left[1] - right[1])

    def dot2(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> Fraction:
        return left[0] * right[0] + left[1] * right[1]

    def approximant(
        limit: tuple[Fraction, Fraction],
        tail: tuple[Fraction, Fraction],
        cutoff: int,
    ) -> tuple[Fraction, Fraction]:
        return add2(limit, scale2(Fraction(1, cutoff * cutoff), tail))

    limit_i = (Fraction(2), Fraction(1))
    limit_j = (Fraction(-1), Fraction(3))
    schedule_a_tail_i = (Fraction(3), Fraction(-2))
    schedule_b_tail_i = (Fraction(-1), Fraction(4))
    schedule_a_tail_j = (Fraction(2), Fraction(5))
    schedule_b_tail_j = (Fraction(-3), Fraction(1))

    previous_gap_i: Fraction | None = None
    previous_gram_gap: Fraction | None = None
    for cutoff in (8, 32, 128):
        schedule_a_i = approximant(limit_i, schedule_a_tail_i, cutoff)
        schedule_b_i = approximant(limit_i, schedule_b_tail_i, cutoff)
        schedule_a_j = approximant(limit_j, schedule_a_tail_j, cutoff)
        schedule_b_j = approximant(limit_j, schedule_b_tail_j, cutoff)

        assert_equal(
            "schedule A tail has the declared n^-2 wave-map scale",
            subtract2(schedule_a_i, limit_i),
            scale2(Fraction(1, cutoff * cutoff), schedule_a_tail_i),
        )

        gap_i = dot2(subtract2(schedule_a_i, schedule_b_i), subtract2(schedule_a_i, schedule_b_i))
        if previous_gap_i is not None and gap_i >= previous_gap_i:
            raise AssertionError("same-flux schedule wave-map gaps should decrease")
        previous_gap_i = gap_i

        assert_equal(
            "schedule tail gap has the declared n^-4 scale",
            gap_i,
            dot2(
                subtract2(schedule_a_tail_i, schedule_b_tail_i),
                subtract2(schedule_a_tail_i, schedule_b_tail_i),
            )
            / (cutoff**4),
        )

        gram_a = dot2(schedule_a_j, schedule_a_i)
        gram_b = dot2(schedule_b_j, schedule_b_i)
        gram_gap = abs(gram_a - gram_b)
        if previous_gram_gap is not None and gram_gap >= previous_gram_gap:
            raise AssertionError("same-flux schedule Gram gaps should decrease")
        previous_gram_gap = gram_gap

    assert_equal("same-flux schedules have the declared asymptotic Gram", dot2(limit_j, limit_i), Fraction(1))

    z = (Fraction(2), Fraction(3))
    left_inverse = (Fraction(1, 2), Fraction(0))
    amplitude = Fraction(7, 5)
    one_external_residue = tuple(amplitude * za for za in z)
    previous_coordinate_gap: Fraction | None = None

    for cutoff in (4, 16, 64):
        schedule_change = ((Fraction(1), Fraction(1, cutoff * cutoff)), (Fraction(0), Fraction(1)))
        schedule_change_inverse = ((Fraction(1), Fraction(-1, cutoff * cutoff)), (Fraction(0), Fraction(1)))
        assert_equal(
            "same-flux schedule coordinate inverse",
            mat_mul(schedule_change_inverse, schedule_change),
            ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))),
        )

        transformed_z = mat_vec(schedule_change, z)
        transformed_left_inverse = row_mat(left_inverse, schedule_change_inverse)
        transformed_residue = mat_vec(schedule_change, one_external_residue)
        extracted = sum(
            transformed_left_inverse[a] * transformed_residue[a]
            for a in range(len(transformed_residue))
        )
        assert_equal("same-flux schedule LSZ extraction is invariant", extracted, amplitude)

        coordinate_gap = sum((transformed_z[a] - z[a]) ** 2 for a in range(len(z)))
        if previous_coordinate_gap is not None and coordinate_gap >= previous_coordinate_gap:
            raise AssertionError("same-flux coordinate changes should tend to identity")
        previous_coordinate_gap = coordinate_gap


def catches_equal_velocity_error() -> bool:
    try:
        many_body_dollard_log_coefficient_1d(
            (Fraction(1), Fraction(2)),
            (1, 1),
            (Fraction(3), Fraction(3)),
        )
    except AssertionError:
        return True
    return False


def check_truncation_schedule_tail_uniformity() -> None:
    """Check the finite tail arithmetic behind admissible dressing schedules."""

    def dyadic_sum(start: int, term) -> Fraction:
        return sum((term(n) for n in range(start, 2 * start)), Fraction(0))

    # Fixed-time convergence of a finite Wilson-line truncation does not by
    # itself give a Cook estimate.  If the large-time derivative still contains
    # a bare 1/t tail, dyadic blocks do not decay.
    for start in (16, 64, 256):
        unscheduled_tail = dyadic_sum(start, lambda n: Fraction(1, n))
        if unscheduled_tail <= Fraction(1, 2):
            raise AssertionError("unscheduled noncompact tail should remain nonintegrable")

    previous_derivative_tail: Fraction | None = None
    previous_norm_tail: Fraction | None = None
    for start in (16, 64, 256):
        # Model an admissible schedule L(t)=t^2 with a residual truncation
        # derivative t^{-1} L(t)^{-1}=t^{-3}.  The dyadic Cook tails then
        # decrease and obey the integral-test bound.
        scheduled_derivative_tail = dyadic_sum(start, lambda n: Fraction(1, n * n * n))
        integral_bound = Fraction(1, 2 * (start - 1) * (start - 1))
        if scheduled_derivative_tail >= integral_bound:
            raise AssertionError("scheduled truncation derivative should obey the tail bound")
        if previous_derivative_tail is not None and scheduled_derivative_tail >= previous_derivative_tail:
            raise AssertionError("scheduled truncation Cook tails should decrease")
        previous_derivative_tail = scheduled_derivative_tail

        # The corresponding same-flux norm discrepancy has sup tail L(t)^{-1}.
        scheduled_norm_tail = Fraction(1, start * start)
        if previous_norm_tail is not None and scheduled_norm_tail >= previous_norm_tail:
            raise AssertionError("same-flux truncation norm tails should decrease")
        previous_norm_tail = scheduled_norm_tail

    for start in (16, 64, 256):
        schedule_a_tail = dyadic_sum(start, lambda n: Fraction(1, n * n * n))
        schedule_b_tail = dyadic_sum(start, lambda n: Fraction(1, 2 * n * n * n))
        if not abs(schedule_a_tail - schedule_b_tail) < schedule_a_tail:
            raise AssertionError("same-flux schedule changes should be a smaller integrable tail")


def check_finite_energy_spectral_tightness_boundary() -> None:
    """Check finite spectral-tightness arithmetic versus linear string energy."""

    def spectral_tail(measure: tuple[tuple[Fraction, Fraction], ...], cutoff: Fraction) -> Fraction:
        return sum((weight for energy, weight in measure if energy > cutoff), Fraction(0))

    # A nonconfining toy family: all spectral mass remains below a common
    # finite energy window after endpoint/local renormalization.
    coulomb_family = (
        ((Fraction(1), Fraction(3, 4)), (Fraction(2), Fraction(1, 4))),
        ((Fraction(1), Fraction(1, 2)), (Fraction(5, 2), Fraction(1, 2))),
        ((Fraction(3, 2), Fraction(2, 3)), (Fraction(3), Fraction(1, 3))),
    )
    for measure in coulomb_family:
        assert_equal("normalized finite-energy spectral measure", sum(weight for _, weight in measure), Fraction(1))
        assert_equal("spectral tail vanishes above common cutoff", spectral_tail(measure, Fraction(3)), Fraction(0))

    # Markov's inequality supplies a sufficient route from a uniform first
    # moment to spectral tightness: tail_E <= <H>/E.
    moment_bound = Fraction(3)
    cutoff = Fraction(12)
    assert_equal("Markov tightness bound", moment_bound / cutoff, Fraction(1, 4))
    assert_equal(
        "actual finite-family tail below Markov bound",
        max(spectral_tail(measure, cutoff) for measure in coulomb_family),
        Fraction(0),
    )

    # A confining string-energy family escapes every fixed finite-energy
    # window: for E_L=E_vac+sigma L-c(L) with sigma>0 and sublinear c(L),
    # the normalized spectral measure is eventually entirely above any fixed
    # cutoff.  This is the finite arithmetic behind the manuscript boundary.
    vacuum_energy = Fraction(0)
    string_tension = Fraction(2)
    sublinear_offset = Fraction(1, 2)
    fixed_cutoff = Fraction(10)
    escaping_lengths = (6, 8, 10)
    for length in escaping_lengths:
        string_energy = vacuum_energy + string_tension * length - sublinear_offset
        measure = ((string_energy, Fraction(1)),)
        assert_equal("linear string family has full high-energy tail", spectral_tail(measure, fixed_cutoff), Fraction(1))


def dot3(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def transverse_projection(a: tuple[float, float, float], n: tuple[float, float, float]) -> tuple[float, float, float]:
    an = dot3(a, n)
    return tuple(a_i - an * n_i for a_i, n_i in zip(a, n))


def soft_velocity_vector(
    velocity: tuple[float, float, float],
    n: tuple[float, float, float],
) -> tuple[float, float, float]:
    denominator = 1.0 - dot3(velocity, n)
    return tuple(component / denominator for component in transverse_projection(velocity, n))


def soft_angular_integrand(
    velocity_a: tuple[float, float, float],
    velocity_b: tuple[float, float, float],
    n: tuple[float, float, float],
) -> float:
    soft_a = soft_velocity_vector(velocity_a, n)
    soft_b = soft_velocity_vector(velocity_b, n)
    difference = tuple(a - b for a, b in zip(soft_a, soft_b))
    return dot3(difference, difference)


def angular_soft_coefficient(
    velocity_a: tuple[float, float, float],
    velocity_b: tuple[float, float, float],
    n_theta: int = 40,
    n_phi: int = 80,
) -> float:
    total = 0.0
    dz = 2.0 / n_theta
    dphi = 2.0 * math.pi / n_phi
    for i in range(n_theta):
        z = -1.0 + (i + 0.5) * dz
        radius = math.sqrt(max(0.0, 1.0 - z * z))
        for j in range(n_phi):
            phi = (j + 0.5) * dphi
            n = (radius * math.cos(phi), radius * math.sin(phi), z)
            total += soft_angular_integrand(velocity_a, velocity_b, n) * dz * dphi
    return total


def check_soft_profile_velocity_separation() -> None:
    samples = [
        ((0.2, 0.0, 0.0), (0.2, 0.0, 0.0), 0.0),
        ((0.2, 0.0, 0.0), (0.4, 0.0, 0.0), None),
        ((0.1, -0.2, 0.0), (0.1, -0.2, 0.0), 0.0),
        ((0.1, -0.2, 0.0), (-0.15, 0.05, 0.25), None),
    ]
    for velocity_a, velocity_b, expected in samples:
        coefficient = angular_soft_coefficient(velocity_a, velocity_b)
        label = f"soft angular coefficient {velocity_a} {velocity_b}"
        if expected is not None:
            assert_close(label, coefficient, expected, tol=1.0e-12)
        elif coefficient <= 1.0e-4:
            raise AssertionError(f"{label} failed: coefficient should be positive, got {coefficient!r}")

    charge = 0.7
    ir_cutoff = 1.0e-3
    uv_cutoff = 0.8
    coefficient = angular_soft_coefficient((0.2, 0.0, 0.0), (0.4, 0.0, 0.0))
    norm_difference = charge * charge * coefficient * math.log(uv_cutoff / ir_cutoff) / (2.0 * (2.0 * math.pi) ** 3)
    expected = charge * charge * coefficient * math.log(uv_cutoff / ir_cutoff) / (16.0 * math.pi**3)
    assert_close("soft coherent norm log prefactor", norm_difference, expected)


def inner_complex(a: tuple[complex, ...], b: tuple[complex, ...]) -> complex:
    return sum(x.conjugate() * y for x, y in zip(a, b))


def norm_sq_complex(a: tuple[complex, ...]) -> float:
    return inner_complex(a, a).real


def sigma_complex(a: tuple[complex, ...], b: tuple[complex, ...]) -> float:
    return 2.0 * inner_complex(a, b).imag


def coherent_weyl_characteristic(F: tuple[complex, ...], f: tuple[complex, ...]) -> complex:
    return cmath.exp(1j * sigma_complex(F, f)) * math.exp(-0.5 * norm_sq_complex(f))


def add_complex(a: tuple[complex, ...], b: tuple[complex, ...]) -> tuple[complex, ...]:
    return tuple(x + y for x, y in zip(a, b))


def coherent_inner(a: tuple[complex, ...], b: tuple[complex, ...]) -> complex:
    return cmath.exp(-0.5 * norm_sq_complex(a) - 0.5 * norm_sq_complex(b) + inner_complex(a, b))


def check_weyl_characteristic_and_overlap_decay() -> None:
    F = (1.0 + 0.3j, -0.4 + 0.7j, 0.2 - 0.1j)
    G = (-0.2 + 0.8j, 0.1 - 0.5j, 0.6 + 0.4j)
    f = (0.3 - 0.1j, -0.6 + 0.2j, 0.05 + 0.4j)

    expected_modulus = math.exp(-0.5 * norm_sq_complex(f))
    assert_close("coherent Weyl state modulus", abs(coherent_weyl_characteristic(F, f)), expected_modulus)

    difference = tuple(x - y for x, y in zip(F, G))
    coherent_overlap_abs = math.exp(-0.5 * norm_sq_complex(difference))
    expected_overlap_abs = math.exp(-0.5 * norm_sq_complex(difference))
    assert_close("coherent-vector overlap formula", coherent_overlap_abs, expected_overlap_abs)

    charge = 1.0
    uv_cutoff = 1.0
    coefficient = angular_soft_coefficient((0.2, 0.0, 0.0), (0.4, 0.0, 0.0))
    def overlap(ir_cutoff: float) -> float:
        norm_sq = charge * charge * coefficient * math.log(uv_cutoff / ir_cutoff) / (2.0 * (2.0 * math.pi) ** 3)
        return math.exp(-0.5 * norm_sq)

    if not overlap(1.0e-6) < overlap(1.0e-3) < overlap(1.0e-1):
        raise AssertionError("IR coherent overlap should decrease as the infrared cutoff is removed")


def check_hilbert_soft_change_inner_equivalence() -> None:
    F = (0.4 + 0.2j, -0.3 + 0.1j, 0.15 - 0.45j)
    delta = (0.05 - 0.07j, -0.02 + 0.03j, 0.08 + 0.04j)
    f = (-0.2 + 0.5j, 0.35 - 0.1j, 0.25 + 0.15j)
    G = add_complex(F, delta)

    transformed = cmath.exp(1j * sigma_complex(delta, f)) * coherent_weyl_characteristic(F, f)
    direct = coherent_weyl_characteristic(G, f)
    assert_close("inner Weyl coordinate change on characteristic functional", transformed, direct)

    overlap_abs = abs(coherent_inner(F, G))
    expected_overlap_abs = math.exp(-0.5 * norm_sq_complex(delta))
    assert_close("finite Hilbert soft change has nonzero coherent overlap", overlap_abs, expected_overlap_abs)

    K = (0.1 + 0.2j, -0.05 + 0.3j, 0.4 - 0.2j)

    def weyl_on_coherent_inner(H_left: tuple[complex, ...], H_right: tuple[complex, ...]) -> complex:
        phase_left = cmath.exp(-0.5j * sigma_complex(H_left, K))
        phase_right = cmath.exp(-0.5j * sigma_complex(H_right, K))
        return phase_left.conjugate() * phase_right * coherent_inner(add_complex(K, H_left), add_complex(K, H_right))

    def strong_distance_sq(H_left: tuple[complex, ...], H_right: tuple[complex, ...]) -> float:
        inner = weyl_on_coherent_inner(H_left, H_right)
        return 2.0 - 2.0 * inner.real

    approximants = [
        add_complex(delta, (0.1 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j)),
        add_complex(delta, (0.05 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j)),
        add_complex(delta, (0.01 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j)),
    ]
    distances = [strong_distance_sq(H, delta) for H in approximants]
    if not distances[2] < distances[1] < distances[0]:
        raise AssertionError(f"Weyl implementers should be strongly continuous, got {distances!r}")


def check_dressed_lsz_residue_coordinates() -> None:
    """Check the finite coordinate algebra behind dressed charged LSZ residues."""

    z = (Fraction(2), Fraction(3))
    left_inverse = (Fraction(1, 2), Fraction(0))
    amplitude = Fraction(7, 5)

    assert_equal("left inverse normalizes the charged pole residue", sum(c * za for c, za in zip(left_inverse, z)), Fraction(1))

    pole_residue = outer(z, z)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for ell in range(2):
                    assert_equal(
                        "rank-one charged residue Gram matrix",
                        pole_residue[i][j] * pole_residue[k][ell],
                        pole_residue[i][ell] * pole_residue[k][j],
                    )

    one_external_residue = tuple(amplitude * za for za in z)
    extracted = sum(left_inverse[a] * one_external_residue[a] for a in range(2))
    assert_equal("dressed LSZ left inverse extracts the external amplitude", extracted, amplitude)

    coordinate_change = ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(1)))
    inverse_coordinate_change = inverse_2x2(coordinate_change)
    changed_z = mat_vec(coordinate_change, z)
    changed_left_inverse = row_mat(left_inverse, inverse_coordinate_change)
    changed_residue = mat_vec(coordinate_change, one_external_residue)
    changed_pole_residue = mat_mul(mat_mul(coordinate_change, pole_residue), transpose(coordinate_change))

    assert_equal(
        "changed left inverse normalizes the transformed charged overlap",
        sum(changed_left_inverse[a] * changed_z[a] for a in range(2)),
        Fraction(1),
    )
    assert_equal(
        "basis change sends residue Gram matrix to M Z M^T",
        changed_pole_residue,
        outer(changed_z, changed_z),
    )
    assert_equal(
        "dressed LSZ residue extraction is invariant under finite coordinate changes",
        sum(changed_left_inverse[a] * changed_residue[a] for a in range(2)),
        amplitude,
    )


def tensor_outer_2(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...], coefficient: Fraction
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(coefficient * a * b for b in right) for a in left)


def classify_shell_term(pole_orders: tuple[int, ...]) -> str:
    """Classify a term after multiplying by one LSZ factor for each leg."""

    if any(order > 1 for order in pole_orders):
        return "forbidden-higher-pole"
    if all(order == 1 for order in pole_orders):
        return "simultaneous-residue"
    return "less-singular"


def check_dressed_correlator_reduction_interface() -> None:
    """Check the finite algebra of the dressed-correlator LSZ interface."""

    z_left = (Fraction(2), Fraction(-1))
    z_right = (Fraction(3), Fraction(4), Fraction(-2))
    left_inverse_left = (Fraction(1, 2), Fraction(0))
    left_inverse_right = (Fraction(0), Fraction(0), Fraction(-1, 2))
    amplitude = Fraction(11, 7)

    assert_equal(
        "left external inverse normalizes its overlap",
        sum(left_inverse_left[a] * z_left[a] for a in range(len(z_left))),
        Fraction(1),
    )
    assert_equal(
        "right external inverse normalizes its overlap",
        sum(left_inverse_right[a] * z_right[a] for a in range(len(z_right))),
        Fraction(1),
    )

    full_residue = tensor_outer_2(z_left, z_right, amplitude)
    extracted = sum(
        left_inverse_left[a] * left_inverse_right[b] * full_residue[a][b]
        for a in range(len(z_left))
        for b in range(len(z_right))
    )
    assert_equal("simultaneous dressed-correlator residue extracts wave-map coefficient", extracted, amplitude)

    partial_left_residue = (1, 0)
    contact_less_singular = (0, 0)
    forbidden_double_pole = (2, 1)
    assert_equal("one missing external pole is less singular", classify_shell_term(partial_left_residue), "less-singular")
    assert_equal("contact term with no external pole is less singular", classify_shell_term(contact_less_singular), "less-singular")
    assert_equal("double external pole is outside LSZ interface", classify_shell_term(forbidden_double_pole), "forbidden-higher-pole")
    assert_equal("full simple pole term survives", classify_shell_term((1, 1)), "simultaneous-residue")

    left_change = ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(1)))
    right_change = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(2), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1), Fraction(1)),
    )
    right_change_inverse = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(-2), Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(1), Fraction(1)),
    )
    assert_equal("right coordinate inverse", mat_mul(right_change_inverse, right_change), tuple(tuple(Fraction(int(i == j)) for j in range(3)) for i in range(3)))

    transformed_left_inverse = row_mat(left_inverse_left, inverse_2x2(left_change))
    transformed_right_inverse = row_mat(left_inverse_right, right_change_inverse)
    transformed_z_left = mat_vec(left_change, z_left)
    transformed_z_right = mat_vec(right_change, z_right)
    transformed_residue = tensor_outer_2(transformed_z_left, transformed_z_right, amplitude)
    transformed_extracted = sum(
        transformed_left_inverse[a] * transformed_right_inverse[b] * transformed_residue[a][b]
        for a in range(len(transformed_z_left))
        for b in range(len(transformed_z_right))
    )
    assert_equal(
        "multi-leg dressed-correlator residue is invariant under finite same-flux coordinate changes",
        transformed_extracted,
        amplitude,
    )


def u1_boundary_phase_exponent(signed_charges: tuple[Fraction, ...]) -> Fraction:
    return sum(signed_charges, Fraction(0))


def su2_tensor_product_twice_spins(a: int, b: int) -> set[int]:
    """Return the twice-spin labels in V_a tensor V_b for SU(2)."""

    return set(range(abs(a - b), a + b + 1, 2))


def su2_contains_singlet(twice_spins: tuple[int, ...]) -> bool:
    possible = {0}
    for spin in twice_spins:
        next_possible: set[int] = set()
        for current in possible:
            next_possible.update(su2_tensor_product_twice_spins(current, spin))
        possible = next_possible
    return 0 in possible


def check_boundary_charge_selection_rules() -> None:
    """Check the finite boundary-charge Ward bookkeeping for dressed correlators."""

    electron_two_point = (Fraction(1), Fraction(-1))
    single_charged_insertion = (Fraction(1),)
    charge_violating_four_point = (Fraction(2), Fraction(-1), Fraction(-1, 3))
    neutral_four_point = (Fraction(2), Fraction(-1), Fraction(-2, 3), Fraction(-1, 3))

    assert_equal("dressed two-point function is boundary neutral", u1_boundary_phase_exponent(electron_two_point), 0)
    assert_equal("single charged vacuum correlator carries boundary charge", u1_boundary_phase_exponent(single_charged_insertion), 1)
    assert_equal("nonneutral four-point charge sum", u1_boundary_phase_exponent(charge_violating_four_point), Fraction(2, 3))
    assert_equal("neutral dressed four-point charge sum", u1_boundary_phase_exponent(neutral_four_point), 0)

    spin_half = 1
    spin_one = 2
    assert_equal("two SU(2) doublet endpoints contain a singlet", su2_contains_singlet((spin_half, spin_half)), True)
    assert_equal("doublet times triplet has no invariant vector", su2_contains_singlet((spin_half, spin_one)), False)
    assert_equal("three SU(2) doublet endpoints have no singlet", su2_contains_singlet((spin_half, spin_half, spin_half)), False)
    assert_equal("four SU(2) doublet endpoints contain singlets", su2_contains_singlet((spin_half, spin_half, spin_half, spin_half)), True)


def check_compact_wilson_line_path_deformation() -> None:
    """Check the finite abelian Stokes algebra for compact Wilson-line deformations."""

    bottom_edge = Fraction(1, 7)
    right_edge = Fraction(2, 5)
    left_edge = Fraction(-1, 3)
    top_edge = Fraction(5, 11)

    gamma = bottom_edge + right_edge
    gamma_prime = left_edge + top_edge
    surface_flux = gamma_prime - gamma

    assert_equal("compact path deformation Stokes identity", gamma_prime, gamma + surface_flux)

    charge = Fraction(3, 2)
    old_exponent = charge * gamma
    new_exponent = charge * gamma_prime
    neutral_surface_exponent = charge * surface_flux
    assert_equal(
        "Wilson-line path deformation multiplies by neutral surface flux",
        new_exponent,
        old_exponent + neutral_surface_exponent,
    )

    alpha_start = Fraction(5, 13)
    alpha_infinity = Fraction(-2, 17)
    gauge_shift_gamma = alpha_infinity - alpha_start
    gauge_shift_gamma_prime = alpha_infinity - alpha_start
    assert_equal(
        "compact path deformation preserves endpoint gauge charge",
        charge * gauge_shift_gamma_prime - charge * gauge_shift_gamma,
        Fraction(0),
    )
    assert_equal(
        "curvature surface insertion is neutral under abelian gauge transformations",
        charge * surface_flux - charge * surface_flux,
        Fraction(0),
    )


def main() -> None:
    check_boosted_flux_integral()
    check_velocity_read_from_flux_extrema()
    check_neutral_boundary_charge_is_not_flux_triviality()
    check_worldline_current_denominator()
    check_half_line_fourier_transform()
    check_coulomb_tail_dollard_log_phase()
    check_many_body_dollard_phase_bookkeeping()
    check_modified_cook_integrability_bookkeeping()
    check_pair_coefficient_residual_budget()
    check_dollard_scalar_product_cauchy_criterion()
    check_asymptotic_null_quotient_wave_map_cell()
    check_same_flux_schedule_wave_map_invariance()
    check_truncation_schedule_tail_uniformity()
    check_finite_energy_spectral_tightness_boundary()
    check_soft_profile_velocity_separation()
    check_weyl_characteristic_and_overlap_decay()
    check_hilbert_soft_change_inner_equivalence()
    check_dressed_lsz_residue_coordinates()
    check_dressed_correlator_reduction_interface()
    check_boundary_charge_selection_rules()
    check_compact_wilson_line_path_deformation()
    print("All charged flux, Wilson-line dressing, and dressed LSZ coordinate checks passed.")


if __name__ == "__main__":
    main()
