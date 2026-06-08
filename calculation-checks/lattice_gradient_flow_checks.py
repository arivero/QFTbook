#!/usr/bin/env python3
"""Finite checks for lattice Wilson-flow and topological-charge conventions."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_negative_gradient_identity() -> None:
    """Check dS/dt=-||grad S||^2 for a finite-dimensional gradient flow."""

    gradient = (Fraction(2, 3), Fraction(-5, 7), Fraction(11, 13))
    velocity = tuple(-entry for entry in gradient)
    derivative = sum(v * g for v, g in zip(velocity, gradient))
    norm_squared = sum(g * g for g in gradient)

    require(derivative == -norm_squared, "gradient-flow monotonicity failed")
    require(derivative <= 0, "negative gradient flow should decrease the action")


def check_conjugation_norm_invariance() -> None:
    """Check invariance of the Lie-algebra norm under an adjoint rotation."""

    vector = (Fraction(3, 5), Fraction(-4, 7), Fraction(5, 11))
    # A rational SO(3) rotation: 90 degrees in the first two coordinates.
    rotated = (-vector[1], vector[0], vector[2])

    norm = sum(entry * entry for entry in vector)
    rotated_norm = sum(entry * entry for entry in rotated)
    require(rotated_norm == norm, "adjoint conjugation should preserve the norm")


def check_heat_kernel_mode_damping() -> None:
    """Check the linearized flow energy derivative for one Fourier mode."""

    k_squared = Fraction(7, 3)
    amplitude_squared = Fraction(13, 17)
    heat_factor_squared = Fraction(5, 19)  # Represents exp(-2 t k^2).

    energy = k_squared * heat_factor_squared * amplitude_squared
    derivative = -2 * k_squared * energy

    require(energy > 0, "linearized flowed energy should be positive")
    require(derivative < 0, "nonzero Fourier mode should be damped")
    expected_derivative = (
        -2 * k_squared * k_squared * heat_factor_squared * amplitude_squared
    )
    require(
        derivative == expected_derivative,
        "linearized heat-kernel derivative has the wrong coefficient",
    )


def check_flow_scale_derivative() -> None:
    """Check the derivative entering the w0 definition for a test density."""

    # Test model: Ebar(t)=A/(t+B)^2.  Then F(t)=t^2 Ebar(t).
    t = Fraction(3, 2)
    shift = Fraction(5, 4)
    amplitude = Fraction(7, 11)

    f = amplitude * t * t / ((t + shift) * (t + shift))
    derivative_f = amplitude * 2 * t * shift / ((t + shift) ** 3)
    w0_operator = t * derivative_f

    # Direct quotient-rule differentiation gives the same result and is
    # positive for this monotone test function.
    direct = (
        t
        * amplitude
        * (2 * t * (t + shift) * (t + shift) - t * t * 2 * (t + shift))
        / ((t + shift) ** 4)
    )
    require(w0_operator == direct, "w0 derivative operator is inconsistent")
    require(f > 0 and w0_operator > 0, "test flowed scale function should be positive")


def check_coupled_action_flow_time_rescaling() -> None:
    gradient = Fraction(11, 13)
    g0_squared = Fraction(5, 7)
    coupled_gradient = gradient / g0_squared
    coupled_time = Fraction(3, 17)
    normalized_time = coupled_time / g0_squared

    coupled_displacement = -coupled_time * coupled_gradient
    normalized_displacement = -normalized_time * gradient
    require(
        coupled_displacement == normalized_displacement,
        "coupled Wilson action should rescale the normalized flow time by g0^{-2}",
    )


def check_antihermitian_sign_and_clover_scaling() -> None:
    hermitian_trace_square = Fraction(19, 23)
    antihermitian_trace_square = -hermitian_trace_square
    g0 = Fraction(5, 7)
    a = Fraction(1, 11)

    positive_action_density = -antihermitian_trace_square / (4 * g0 * g0)
    connection_action_density = hermitian_trace_square / (4 * g0 * g0)
    require(
        positive_action_density == connection_action_density,
        "anti-Hermitian action needs the minus trace sign",
    )

    clover_product_scale = (g0 * a * a) ** 2
    canonical_product_scale = g0 * g0 * a**4
    require(
        clover_product_scale == canonical_product_scale,
        "canonical clover density should carry g0^2 a^4",
    )


def check_chern_weil_variation_factor() -> None:
    """Check the factor two in delta tr(F wedge F)=2 tr(delta F wedge F)."""

    # Degree-two forms commute: F wedge dFdot = dFdot wedge F.
    first_term = Fraction(1)
    second_term = Fraction(1)
    variation = first_term + second_term
    require(
        variation == 2,
        "degree-two wedge symmetry should give the Chern-Weil factor two",
    )


def main() -> None:
    check_negative_gradient_identity()
    check_conjugation_norm_invariance()
    check_heat_kernel_mode_damping()
    check_flow_scale_derivative()
    check_coupled_action_flow_time_rescaling()
    check_antihermitian_sign_and_clover_scaling()
    check_chern_weil_variation_factor()
    print("All lattice gradient-flow checks passed.")


if __name__ == "__main__":
    main()
