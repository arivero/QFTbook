#!/usr/bin/env python3
"""Exact finite checks for ordinary short-range scalar RG reconstruction.

Volume XI, Chapter 7 defines the block-spin reconstruction datum for an
ordinary short-range scalar lattice model.  These checks verify the finite
normalization and exponent bookkeeping used there: block kernels preserve
constant fields up to the declared field scaling, block-constant test
functions keep the distribution pairing invariant, independent-site
covariances scale with the expected block exponent, and the reconstruction
bound has the displayed geometric form.
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


def main():
    check_block_kernel_constant_field_scaling()
    check_distribution_pairing_for_block_constant_tests()
    check_independent_covariance_scaling()
    check_geometric_reconstruction_bound()
    check_correction_to_scaling_bookkeeping()
    print("All short-range scalar RG reconstruction checks passed.")


if __name__ == "__main__":
    main()
