#!/usr/bin/env python3
"""Exact finite checks for ordinary short-range scalar RG reconstruction.

Volume XI, Chapter 7 defines the block-spin reconstruction datum for an
ordinary short-range scalar lattice model.  These checks verify the finite
normalization and exponent bookkeeping used there: block kernels preserve
constant fields up to the declared field scaling, block-constant test
functions keep the distribution pairing invariant, independent-site
covariances scale with the expected block exponent, the reconstruction bound
has the displayed geometric form, and an auxiliary RG theorem transfers to
the short-range target only when the one-step intertwining defects remain
controlled after stable or relevant RG amplification.  The observable-germ
checks verify that finite-window agreement is a projective, seminorm-level
certificate rather than a substitute for full universality, and that
QFT-strength observable germs must include reflection-positivity Gram
windows rather than only a visible finite list of correlator coordinates.
The polymer checks verify the exact finite arithmetic behind the one-step
contraction budget: linear irrelevant gain, a finite pair-overlap majorant
for the quadratic circle product, and a finite local-coordinate extraction
defect.
The multiscale polymer checks verify the forced-recursion sum that turns the
one-step budget into a scale-uniform smallness condition.
The finite-range covariance check verifies the block-diagonal characteristic
function factorization behind independent fluctuation integrations on
separated polymers.
The localization checks verify the finite Taylor-remainder arithmetic and
canonical local-monomial scaling exponents used to decide whether an omitted
coordinate has an actual irrelevant gain.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def pow_int(base, exponent):
    if exponent >= 0:
        return base**exponent
    return Fraction(1, base ** (-exponent))


def uniform_block_kernel(dimension, scale):
    volume = scale**dimension
    return [Fraction(1, volume) for _ in range(volume)]


def check_block_kernel_constant_field_scaling():
    dimension = 4
    scale = 2
    delta_phi = 1
    constant = Fraction(7, 3)
    q = uniform_block_kernel(dimension, scale)
    assert_equal("block-kernel normalization", sum(q), Fraction(1))
    blocked = pow_int(scale, delta_phi) * sum(weight * constant for weight in q)
    assert_equal(
        "constant field block scaling",
        blocked,
        pow_int(scale, delta_phi) * constant,
    )


def check_distribution_pairing_for_block_constant_tests():
    # Fine lattice spacing is set to a_k=1 for exact arithmetic.  One coarse
    # block then has spacing a_{k-1}=L.  For a test function constant on the
    # block, a^{D-Delta} sum f phi is preserved by the block-spin definition.
    dimension = 4
    scale = 2
    delta_phi = 1
    fine_spacing = Fraction(1)
    coarse_spacing = Fraction(scale)
    field_values = [Fraction(i + 1) for i in range(scale**dimension)]
    test_value = Fraction(5, 7)
    q = uniform_block_kernel(dimension, scale)

    fine_pairing = (
        fine_spacing ** (dimension - delta_phi)
        * test_value
        * sum(field_values)
    )
    blocked_field = pow_int(scale, delta_phi) * sum(
        weight * value for weight, value in zip(q, field_values)
    )
    coarse_pairing = (
        coarse_spacing ** (dimension - delta_phi)
        * test_value
        * blocked_field
    )
    assert_equal("block-constant distribution pairing", coarse_pairing, fine_pairing)


def check_independent_covariance_scaling():
    dimension = 4
    scale = 2
    delta_phi = 1
    variance = Fraction(11, 5)
    q = uniform_block_kernel(dimension, scale)
    covariance_of_block_average = pow_int(scale, 2 * delta_phi) * sum(
        weight * weight * variance for weight in q
    )
    expected = variance * pow_int(scale, 2 * delta_phi - dimension)
    assert_equal("independent-site block covariance scaling", covariance_of_block_average, expected)
    assert_equal("canonical D=4 free-field covariance factor", expected / variance, Fraction(1, 4))


def check_geometric_reconstruction_bound():
    c_b = Fraction(5, 2)
    c0 = Fraction(3, 7)
    theta = Fraction(1, 3)
    eps0 = Fraction(2, 5)
    sigma = Fraction(1, 4)
    for step in range(6):
        chart_distance = c0 * theta**step
        discretization_error = eps0 * sigma**step
        bound = c_b * chart_distance + discretization_error
        expected = c_b * c0 * theta**step + eps0 * sigma**step
        assert_equal(f"geometric reconstruction bound step {step}", bound, expected)
        if step:
            previous = c_b * c0 * theta ** (step - 1) + eps0 * sigma ** (step - 1)
            assert_true(f"bound decreases at step {step}", bound < previous)


def check_correction_to_scaling_bookkeeping():
    scale = 2
    omega_1 = 1
    omega_2 = 2
    fixed_observable = Fraction(13, 17)
    correction_1 = Fraction(11, 3)
    correction_2 = Fraction(-5, 4)
    amplitude_1 = Fraction(7, 5)
    amplitude_2 = Fraction(-2, 9)

    def power_decay(omega, step):
        return Fraction(1, scale ** (omega * step))

    def observable(step):
        return (
            fixed_observable
            + amplitude_1 * power_decay(omega_1, step) * correction_1
            + amplitude_2 * power_decay(omega_2, step) * correction_2
        )

    for step in range(1, 6):
        leading_scaled_error = scale**step * (observable(step) - fixed_observable)
        expected = amplitude_1 * correction_1 + amplitude_2 * correction_2 * power_decay(1, step)
        assert_equal(f"leading correction extraction step {step}", leading_scaled_error, expected)

    for step in range(1, 5):
        subtracted_now = observable(step) - fixed_observable - amplitude_1 * power_decay(omega_1, step) * correction_1
        subtracted_next = observable(step + 1) - fixed_observable - amplitude_1 * power_decay(omega_1, step + 1) * correction_1
        assert_equal(
            f"subleading correction ratio step {step}",
            subtracted_next,
            power_decay(omega_2, 1) * subtracted_now,
        )

    other_amplitude_1 = Fraction(-3, 8)
    other_amplitude_2 = Fraction(5, 11)

    def other_observable(step):
        return (
            fixed_observable
            + other_amplitude_1 * power_decay(omega_1, step) * correction_1
            + other_amplitude_2 * power_decay(omega_2, step) * correction_2
        )

    for step in range(1, 5):
        difference = observable(step) - other_observable(step)
        leading_difference = (
            (amplitude_1 - other_amplitude_1) * power_decay(omega_1, step) * correction_1
        )
        after_leading_subtraction = difference - leading_difference
        expected_subleading = (
            (amplitude_2 - other_amplitude_2) * power_decay(omega_2, step) * correction_2
        )
        assert_equal(
            f"same limit but regulator-dependent correction amplitudes step {step}",
            after_leading_subtraction,
            expected_subleading,
        )


def check_auxiliary_transfer_telescoping_bound():
    theta = Fraction(2, 3)
    q = Fraction(1, 5)
    c = Fraction(3, 7)

    for steps in range(1, 8):
        defects = [c * q**j for j in range(steps)]
        orbit_error = Fraction(0)
        for defect in defects:
            orbit_error = theta * orbit_error + defect

        telescoping = sum(
            theta ** (steps - 1 - j) * defects[j] for j in range(steps)
        )
        closed_form = c * (theta**steps - q**steps) / (theta - q)

        assert_equal(f"auxiliary transfer recurrence step {steps}", orbit_error, telescoping)
        assert_equal(f"auxiliary transfer geometric sum step {steps}", telescoping, closed_form)

    equal_rate = Fraction(1, 4)
    c_equal = Fraction(5, 6)
    for steps in range(1, 7):
        defects = [c_equal * equal_rate**j for j in range(steps)]
        telescoping = sum(
            equal_rate ** (steps - 1 - j) * defects[j] for j in range(steps)
        )
        assert_equal(
            f"auxiliary transfer equal-rate sum step {steps}",
            telescoping,
            c_equal * steps * equal_rate ** (steps - 1),
        )


def check_relevant_direction_tuning_amplification():
    lam = Fraction(3)
    rho = Fraction(5, 7)
    for depth in range(1, 6):
        tuned_initial = rho / lam**depth
        amplified = lam**depth * tuned_initial
        assert_equal(f"relevant tuning depth {depth}", amplified, rho)

    initial = Fraction(1, 11)
    errors = [Fraction(1, 3), Fraction(-1, 9), Fraction(1, 27), Fraction(-1, 81)]
    coordinate = initial
    for error in errors:
        coordinate = lam * coordinate + error
    expected = lam ** len(errors) * initial + sum(
        lam ** (len(errors) - 1 - j) * errors[j] for j in range(len(errors))
    )
    assert_equal("relevant direction affine amplification", coordinate, expected)


def check_observable_germ_finite_window_certificate():
    # Three finite observation windows form a projective chain
    # gamma -> beta -> alpha.  The exact numbers model normalized finite lists
    # of observables; the check is the projective compatibility and the
    # finite-window triangle certificate used in the chapter.
    gamma_data = {
        "alpha": Fraction(5, 7),
        "beta_extra": Fraction(-2, 3),
        "gamma_extra": Fraction(11, 13),
    }
    beta_projection = {
        "alpha": gamma_data["alpha"],
        "beta_extra": gamma_data["beta_extra"],
    }
    alpha_projection = {"alpha": gamma_data["alpha"]}

    assert_equal("project gamma to beta", beta_projection["alpha"], gamma_data["alpha"])
    assert_equal("project beta to alpha", alpha_projection["alpha"], beta_projection["alpha"])
    assert_equal("direct gamma to alpha", alpha_projection["alpha"], gamma_data["alpha"])

    fixed_alpha = Fraction(17, 19)
    fixed_beta = Fraction(-4, 9)
    fixed_gamma = Fraction(7, 11)
    error_i = {
        "alpha": Fraction(1, 100),
        "beta": Fraction(1, 80),
        "gamma": Fraction(1, 70),
    }
    error_j = {
        "alpha": Fraction(1, 90),
        "beta": Fraction(1, 75),
        "gamma": Fraction(1, 60),
    }
    rec_i = {
        "alpha": fixed_alpha + error_i["alpha"],
        "beta": fixed_beta - error_i["beta"],
        "gamma": fixed_gamma + error_i["gamma"],
    }
    rec_j = {
        "alpha": fixed_alpha - error_j["alpha"],
        "beta": fixed_beta + error_j["beta"],
        "gamma": fixed_gamma - error_j["gamma"],
    }

    for key in ("alpha", "beta", "gamma"):
        lhs = abs(rec_i[key] - rec_j[key])
        rhs = error_i[key] + error_j[key]
        assert_equal(f"finite-window universality certificate {key}", lhs, rhs)

    hidden_window_error = Fraction(1, 7)
    declared_finite_bound = error_i["alpha"] + error_j["alpha"]
    assert_true(
        "uncontrolled window remains outside finite certificate",
        hidden_window_error > declared_finite_bound,
    )


def check_qft_strength_observable_germ_windows():
    # A visible one-coordinate window can agree while an undeclared
    # reflection-positivity Gram window fails.  This finite check models the
    # chapter's point that equality of a local QFT requires the whole
    # OS/Wightman reconstruction germ, not only a finite observable list.
    visible_two_point = Fraction(2)
    positive_gram = [
        [visible_two_point, Fraction(1)],
        [Fraction(1), Fraction(3)],
    ]
    positive_det = (
        positive_gram[0][0] * positive_gram[1][1]
        - positive_gram[0][1] ** 2
    )
    assert_equal(
        "project Gram to visible two-point",
        positive_gram[0][0],
        visible_two_point,
    )
    assert_true("declared OS Gram determinant positive", positive_det > 0)

    hidden_bad_gram = [
        [visible_two_point, Fraction(3)],
        [Fraction(3), Fraction(1)],
    ]
    hidden_bad_det = (
        hidden_bad_gram[0][0] * hidden_bad_gram[1][1]
        - hidden_bad_gram[0][1] ** 2
    )
    assert_equal(
        "hidden bad Gram has same visible coordinate",
        hidden_bad_gram[0][0],
        visible_two_point,
    )
    assert_true("hidden bad OS Gram determinant negative", hidden_bad_det < 0)

    error_i = Fraction(1, 100)
    error_j = Fraction(1, 120)
    rec_i_visible = visible_two_point + error_i
    rec_j_visible = visible_two_point - error_j
    finite_certificate = abs(rec_i_visible - rec_j_visible)
    assert_equal(
        "visible finite-window certificate",
        finite_certificate,
        error_i + error_j,
    )
    assert_true(
        "visible certificate does not detect hidden positivity failure",
        hidden_bad_det < 0 and finite_certificate < 1,
    )


def check_polymer_contraction_budget():
    # The chapter's polymer datum gives
    #   x_{k+1} <= q x_k + B x_k^2 + epsilon.
    # This exact rational test is deliberately finite: it certifies the
    # contraction-budget arithmetic, not any model-specific analytic estimate
    # for q, B, epsilon, or the large-field norm.
    linear_gain = Fraction(2, 5)
    quadratic_constant = Fraction(7, 4)
    radius = Fraction(1, 10)
    extraction_defect = Fraction(1, 200)

    theta = (
        linear_gain
        + quadratic_constant * radius
        + extraction_defect / radius
    )
    assert_equal("polymer contraction margin", theta, Fraction(5, 8))
    assert_true("polymer contraction margin below one", theta < 1)

    boundary_next = (
        linear_gain * radius
        + quadratic_constant * radius * radius
        + extraction_defect
    )
    assert_equal("polymer boundary image", boundary_next, theta * radius)
    assert_true("polymer ball maps strictly inside itself", boundary_next < radius)

    x = radius
    for step in range(1, 7):
        x_next = linear_gain * x + quadratic_constant * x * x + extraction_defect
        assert_true(f"polymer recurrence remains inside radius step {step}", x_next <= radius)
        if x >= boundary_next:
            assert_true(f"polymer recurrence decreases before fixed cell step {step}", x_next <= x)
        x = x_next

    # A finite overlap/combinatorial constant controls the quadratic
    # circle-product estimate ||K_1 circ K_2|| <= B_pol ||K_1|| ||K_2||.
    overlap_constant = Fraction(6)
    norm_1 = Fraction(1, 30)
    norm_2 = Fraction(1, 20)
    product_bound = overlap_constant * norm_1 * norm_2
    assert_equal("polymer circle-product quadratic bound", product_bound, Fraction(1, 100))


def check_polymer_pair_overlap_majorant():
    # Finite one-dimensional shadow of the pair-overlap constant
    # C_a^circ.  Polymers are connected intervals in a five-block line.
    # Two intervals are incompatible when they overlap or are adjacent, so
    # their reblocked hull is still controlled by a local counting constant.
    block_count = 5
    omega = Fraction(1, 4)  # exact stand-in for exp(-a)
    intervals = [
        (left, right)
        for left in range(block_count)
        for right in range(left, block_count)
    ]

    def length(interval):
        return interval[1] - interval[0] + 1

    def incompatible(first, second):
        return not (first[1] + 1 < second[0] or second[1] + 1 < first[0])

    def hull(first, second):
        return (min(first[0], second[0]), max(first[1], second[1]))

    block_sums = []
    for block in range(block_count):
        total = Fraction(0)
        for first in intervals:
            for second in intervals:
                if not incompatible(first, second):
                    continue
                joined = hull(first, second)
                if joined[0] <= block <= joined[1]:
                    total += omega ** (length(first) + length(second))
        block_sums.append(total)

    expected = [
        Fraction(421281, 1048576),
        Fraction(763825, 1048576),
        Fraction(866481, 1048576),
        Fraction(763825, 1048576),
        Fraction(421281, 1048576),
    ]
    assert_equal("polymer pair-overlap block sums", block_sums, expected)
    pair_majorant = max(block_sums)
    assert_equal("polymer pair-overlap majorant", pair_majorant, Fraction(866481, 1048576))

    regulator_constant = Fraction(3, 2)
    norm_1 = Fraction(1, 10)
    norm_2 = Fraction(1, 7)
    admissible_b_pol = regulator_constant * pair_majorant
    product_bound = admissible_b_pol * norm_1 * norm_2
    assert_equal(
        "polymer pair-overlap circle-product bound",
        product_bound,
        Fraction(371349, 20971520),
    )


def check_polymer_multiscale_forcing_budget():
    theta = Fraction(2, 5)
    sigma = Fraction(1, 3)
    forcing_size = Fraction(1, 100)
    initial = Fraction(1, 20)

    for steps in range(1, 8):
        x = initial
        for j in range(steps):
            x = theta * x + forcing_size * sigma**j
        expected = theta**steps * initial + forcing_size * sum(
            theta ** (steps - 1 - j) * sigma**j for j in range(steps)
        )
        closed_form = (
            theta**steps * initial
            + forcing_size * (theta**steps - sigma**steps) / (theta - sigma)
        )
        assert_equal(f"polymer multiscale forcing recurrence {steps}", x, expected)
        assert_equal(f"polymer multiscale geometric forcing {steps}", x, closed_form)

    equal_rate = Fraction(1, 4)
    equal_forcing = Fraction(3, 200)
    for steps in range(1, 7):
        forcing_sum = sum(
            equal_rate ** (steps - 1 - j) * equal_forcing * equal_rate**j
            for j in range(steps)
        )
        assert_equal(
            f"polymer equal-rate forcing sum {steps}",
            forcing_sum,
            equal_forcing * steps * equal_rate ** (steps - 1),
        )

    uniform_forcing = Fraction(1, 500)
    radius = Fraction(1, 10)
    invariant_budget = initial + uniform_forcing / (1 - theta)
    assert_true("polymer uniform-forcing invariant budget below radius", invariant_budget <= radius)
    x = initial
    for steps in range(1, 10):
        x = theta * x + uniform_forcing
        bound = theta**steps * initial + uniform_forcing * (1 - theta**steps) / (1 - theta)
        assert_equal(f"polymer uniform-forcing bound {steps}", x, bound)
        assert_true(f"polymer uniform-forcing orbit stays in radius {steps}", x <= radius)


def check_finite_range_gaussian_factorization():
    # Four finite field coordinates are split as A={0,1}, B={2,3}.  The
    # covariance has nontrivial internal correlations in A and B but vanishing
    # cross block.  The Gaussian characteristic exponent therefore splits
    # exactly into its A and B parts.  This is the finite arithmetic model of
    # the chapter's separated-polymer fluctuation factorization.
    gamma = [
        [Fraction(5), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(3), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(7), Fraction(2)],
        [Fraction(0), Fraction(0), Fraction(2), Fraction(4)],
    ]
    vector = [Fraction(1, 2), Fraction(-3, 5), Fraction(2, 7), Fraction(5, 11)]

    def quadratic_form(matrix, vec):
        total = Fraction(0)
        for i, row in enumerate(matrix):
            for j, entry in enumerate(row):
                total += vec[i] * entry * vec[j]
        return total

    full = quadratic_form(gamma, vector)
    a_block = quadratic_form(
        [row[:2] for row in gamma[:2]],
        vector[:2],
    )
    b_block = quadratic_form(
        [row[2:] for row in gamma[2:]],
        vector[2:],
    )
    assert_equal("finite-range characteristic exponent splits", full, a_block + b_block)

    # Turning on one cross covariance records exactly the mixed term that
    # prevents factorization.  The coefficient is 2 t_0 Gamma_{02} t_2 in the
    # symmetric quadratic form.
    gamma_with_tail = [row[:] for row in gamma]
    cross = Fraction(3, 13)
    gamma_with_tail[0][2] = cross
    gamma_with_tail[2][0] = cross
    full_with_tail = quadratic_form(gamma_with_tail, vector)
    mixed_term = 2 * vector[0] * cross * vector[2]
    assert_equal(
        "cross covariance creates mixed characteristic term",
        full_with_tail,
        a_block + b_block + mixed_term,
    )
    assert_true("mixed term is nonzero when covariance tail remains", mixed_term != 0)


def check_localization_taylor_remainder_bound():
    # Scalar finite-dimensional shadow of the Taylor-localization estimate.
    # F(t)=3-2t+5t^2-7t^3+11t^4 is localized through degree two.
    # On |t|<=r, sup |F'''(t)| <= 6*7 + 24*11*r, so the integral Taylor
    # remainder gives |R_2(t)| <= M_3 r^3/6 at |t|=r.
    r = Fraction(1, 5)
    c0 = Fraction(3)
    c1 = Fraction(-2)
    c2 = Fraction(5)
    c3 = Fraction(-7)
    c4 = Fraction(11)

    value = c0 + c1 * r + c2 * r**2 + c3 * r**3 + c4 * r**4
    localized = c0 + c1 * r + c2 * r**2
    remainder = abs(value - localized)
    direct_abs_sum = abs(c3) * r**3 + abs(c4) * r**4
    derivative_bound = 6 * abs(c3) + 24 * abs(c4) * r
    taylor_bound = derivative_bound * r**3 / 6

    assert_equal("Taylor localization direct omitted-coordinate sum", direct_abs_sum, Fraction(46, 625))
    assert_true("Taylor localization exact remainder below direct abs sum", remainder <= direct_abs_sum)
    assert_equal("Taylor localization derivative bound", derivative_bound, Fraction(474, 5))
    assert_equal("Taylor localization integral remainder bound", taylor_bound, Fraction(79, 625))
    assert_true("Taylor localization remainder below derivative bound", remainder <= taylor_bound)


def check_localization_scaling_exponents():
    def exponent(dimension, delta_phi, fields, differences):
        return dimension - fields * delta_phi - differences

    # Canonical D=4 scalar bookkeeping: phi^4 and (partial phi)^2 are
    # marginal, while phi^6 and four-derivative quadratic terms are
    # irrelevant by two powers of the block scale.
    d4 = Fraction(4)
    delta4 = Fraction(1)
    assert_equal("D4 mass exponent", exponent(d4, delta4, 2, 0), Fraction(2))
    assert_equal("D4 quartic exponent", exponent(d4, delta4, 4, 0), Fraction(0))
    assert_equal("D4 kinetic exponent", exponent(d4, delta4, 2, 2), Fraction(0))
    assert_equal("D4 phi6 exponent", exponent(d4, delta4, 6, 0), Fraction(-2))
    assert_equal("D4 four-derivative quadratic exponent", exponent(d4, delta4, 2, 4), Fraction(-2))
    first_omitted_gap_d4 = min(
        -exponent(d4, delta4, 6, 0),
        -exponent(d4, delta4, 2, 4),
    )
    assert_equal("D4 first omitted canonical localization gap", first_omitted_gap_d4, Fraction(2))
    assert_true("D4 omitted canonical coordinates are contractive", first_omitted_gap_d4 > 0)

    # Canonical D=3 scalar bookkeeping: phi^6 is marginal by engineering
    # power counting.  Discarding it into the irrelevant polymer activity
    # therefore requires an interacting fixed-point/scaling-field theorem or
    # a separate localization estimate, not the canonical ledger alone.
    d3 = Fraction(3)
    delta3 = Fraction(1, 2)
    assert_equal("D3 mass exponent", exponent(d3, delta3, 2, 0), Fraction(2))
    assert_equal("D3 quartic exponent", exponent(d3, delta3, 4, 0), Fraction(1))
    assert_equal("D3 phi6 exponent", exponent(d3, delta3, 6, 0), Fraction(0))
    assert_equal("D3 phi8 exponent", exponent(d3, delta3, 8, 0), Fraction(-1))
    first_omitted_gap_d3_if_phi6_omitted = -exponent(d3, delta3, 6, 0)
    assert_equal(
        "D3 no canonical irrelevant gain if phi6 is omitted",
        first_omitted_gap_d3_if_phi6_omitted,
        Fraction(0),
    )
    assert_true("D3 omitted phi6 is not canonically contractive", first_omitted_gap_d3_if_phi6_omitted <= 0)


def main():
    check_block_kernel_constant_field_scaling()
    check_distribution_pairing_for_block_constant_tests()
    check_independent_covariance_scaling()
    check_geometric_reconstruction_bound()
    check_correction_to_scaling_bookkeeping()
    check_auxiliary_transfer_telescoping_bound()
    check_relevant_direction_tuning_amplification()
    check_observable_germ_finite_window_certificate()
    check_qft_strength_observable_germ_windows()
    check_polymer_contraction_budget()
    check_polymer_pair_overlap_majorant()
    check_polymer_multiscale_forcing_budget()
    check_finite_range_gaussian_factorization()
    check_localization_taylor_remainder_bound()
    check_localization_scaling_exponents()
    print("All short-range scalar RG reconstruction checks passed.")


if __name__ == "__main__":
    main()
