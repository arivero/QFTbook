#!/usr/bin/env python3
"""Finite checks for thermal path-integral conventions.

Evidence contract.
Target claims: circle eigenvalue quantization, finite-volume spectral
representation of Euclidean correlators, the separate zero mode, Matsubara
Cauchy transforms, chemical-potential twist bookkeeping, and the
Euclidean-to-real-time reconstruction instability example in Volume X
Chapter 2.
Independent construction: direct finite Gibbs sums, direct Matsubara
integration, exact boundary phases, finite Berezin-sign arithmetic, and a
low-frequency positive spectral-slope family whose Euclidean transform is
bounded while its transport-channel slope is fixed, including a
finite-sum-rule-preserving compensator test with a smooth integrable
reference spectrum, a restricted polynomial-weight compensator system, and a
uniform positivity margin.
Imported assumptions: the finite-regulator Gibbs trace, the bosonic spectral
kernel stated in the chapter, positivity of Hermitian positive-frequency
spectral weights, and the use of Euclidean norms as data-error topology.
Negative controls: the Euclidean zero mode is not inferred from the
commutator spectral density, finite Matsubara values are not accepted as
stable spectral reconstruction, small Euclidean error is not accepted as
control of the low-frequency transport-channel slope, and a nonintegrable
constant spectral floor is not used to preserve positivity.  An adversarial
weight pair whose restrictions agree on the allowed compensator region is
rejected as outside the compensator hypothesis.
Scope boundary: these checks verify finite algebra and the explicit
ill-conditioning construction; they do not prove a continuum reconstruction
theorem, Carlson-class uniqueness, arbitrary finite-sum-rule compensator
existence, or the correctness of any numerical analytic-continuation prior.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import cmath
import math


def assert_close(lhs: complex, rhs: complex, message: str, tol: float = 1e-10) -> None:
    _assert_close(message, lhs, rhs, tol=tol)


def check_matsubara_boundary_phases() -> None:
    beta = 1.7
    for n in range(-4, 5):
        omega_b = 2.0 * math.pi * n / beta
        assert_close(cmath.exp(1j * omega_b * beta), 1.0, "bosonic mode is periodic")

        omega_f = (2 * n + 1) * math.pi / beta
        assert_close(cmath.exp(1j * omega_f * beta), -1.0, "fermionic mode is antiperiodic")


def check_one_mode_fermionic_trace_identity() -> None:
    """Check the Berezin sign convention used in the coherent-state trace.

    With ordered integral dbar eta d eta, the chapter convention is
    integral(bar eta eta) = -1.  The coefficient of bar eta eta in
    exp(-bar eta eta)<-eta|O|eta> is therefore minus Tr O.
    """

    operator = [
        [1.2 + 0.3j, -0.4 + 0.8j],
        [0.9 - 0.2j, -0.7 + 0.5j],
    ]
    o00 = operator[0][0]
    o11 = operator[1][1]

    berezin_bar_eta_eta = -1.0
    trace_integrand_coeff = -(o00 + o11)
    graded_integrand_coeff = -(o00 - o11)

    assert_close(
        trace_integrand_coeff * berezin_bar_eta_eta,
        o00 + o11,
        "fermionic coherent-state trace identity",
    )
    assert_close(
        graded_integrand_coeff * berezin_bar_eta_eta,
        o00 - o11,
        "fermionic coherent-state graded trace identity",
    )


def off_diagonal_matrix(entries: dict[tuple[int, int], complex], size: int) -> list[list[complex]]:
    matrix = [[0j for _ in range(size)] for _ in range(size)]
    for (i, j), value in entries.items():
        if i == j:
            raise ValueError("use off-diagonal entries to avoid zero-frequency contact terms")
        matrix[i][j] = complex(value)
    return matrix


def direct_euclidean_correlator(
    energies: list[float],
    beta: float,
    tau: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> complex:
    z = sum(math.exp(-beta * energy) for energy in energies)
    total = 0j
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            total += (
                math.exp(-beta * en)
                * math.exp(-tau * (em - en))
                * a_matrix[n][m]
                * b_matrix[m][n]
            )
    return total / z


def spectral_atoms(
    energies: list[float],
    beta: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> list[tuple[float, complex]]:
    z = sum(math.exp(-beta * energy) for energy in energies)
    atoms: list[tuple[float, complex]] = []
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            weight = (
                (math.exp(-beta * en) - math.exp(-beta * em))
                * a_matrix[n][m]
                * b_matrix[m][n]
                / z
            )
            if abs(weight) > 1e-14:
                atoms.append((em - en, weight))
    return atoms


def zero_mode_contribution(
    energies: list[float],
    beta: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> complex:
    z = sum(math.exp(-beta * energy) for energy in energies)
    total = 0j
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            if abs(em - en) < 1e-14:
                total += math.exp(-beta * en) * a_matrix[n][m] * b_matrix[m][n]
    return total / z


def spectral_euclidean_correlator(atoms: list[tuple[float, complex]], beta: float, tau: float) -> complex:
    total = 0j
    for omega, weight in atoms:
        total += math.exp(-omega * tau) * weight / (1.0 - math.exp(-beta * omega))
    return total


def direct_matsubara_transform(
    energies: list[float],
    beta: float,
    matsubara_frequency: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> complex:
    z = sum(math.exp(-beta * energy) for energy in energies)
    total = 0j
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            omega = em - en
            coefficient = math.exp(-beta * en) * a_matrix[n][m] * b_matrix[m][n] / z
            if abs(coefficient) < 1e-14:
                continue
            exponent = -omega + 1j * matsubara_frequency
            if abs(exponent) < 1e-14:
                total += coefficient * beta
            else:
                total += coefficient * (cmath.exp(exponent * beta) - 1.0) / exponent
    return total


def cauchy_matsubara_transform(atoms: list[tuple[float, complex]], matsubara_frequency: float) -> complex:
    return sum(weight / (omega - 1j * matsubara_frequency) for omega, weight in atoms)


def euclidean_transport_kernel(beta: float, tau: float, omega: float) -> float:
    """Kernel multiplying sigma(omega)=rho(omega)/(2 omega) for omega>0."""

    if abs(omega) < 1.0e-12:
        return 4.0 / beta
    return 2.0 * omega * math.cosh(omega * (0.5 * beta - tau)) / math.sinh(0.5 * beta * omega)


def low_frequency_transport_bump(beta: float, tau: float, epsilon: float, eta_star: float) -> float:
    intervals = 400
    step = epsilon / intervals
    total = 0.0
    for index in range(intervals):
        omega = (index + 0.5) * step
        total += eta_star * euclidean_transport_kernel(beta, tau, omega) * step
    return total


def check_bosonic_spectral_representation() -> None:
    energies = [0.25, 1.1, 2.3]
    beta = 1.4
    a_matrix = off_diagonal_matrix({(0, 1): 2.0, (1, 2): -0.7j, (2, 0): 1.1}, 3)
    b_matrix = off_diagonal_matrix({(1, 0): 0.4, (2, 1): 1.3j, (0, 2): -0.2}, 3)
    atoms = spectral_atoms(energies, beta, a_matrix, b_matrix)

    for tau in [0.2, 0.6, 1.1]:
        assert_close(
            direct_euclidean_correlator(energies, beta, tau, a_matrix, b_matrix),
            spectral_euclidean_correlator(atoms, beta, tau),
            "finite spectral formula reproduces Euclidean correlator",
        )

    for ell in [1, 2, 3]:
        matsubara = 2.0 * math.pi * ell / beta
        assert_close(
            direct_matsubara_transform(energies, beta, matsubara, a_matrix, b_matrix),
            cauchy_matsubara_transform(atoms, matsubara),
            "Matsubara transform equals spectral Cauchy transform",
        )

    diagonal_a = [[1.0, 0j, 0j], [0j, -0.3, 0j], [0j, 0j, 0.8]]
    diagonal_b = [[0.2, 0j, 0j], [0j, 1.4, 0j], [0j, 0j, -0.5]]
    zero_mode = zero_mode_contribution(energies, beta, diagonal_a, diagonal_b)
    for tau in [0.15, 0.75, 1.25]:
        assert_close(
            direct_euclidean_correlator(energies, beta, tau, diagonal_a, diagonal_b),
            zero_mode,
            "degenerate spectral contribution is a separate Euclidean zero mode",
        )
    assert_close(
        direct_matsubara_transform(energies, beta, 0.0, diagonal_a, diagonal_b),
        beta * zero_mode,
        "zero Matsubara mode includes beta times the constant spectral term",
    )
    first_nonzero_bosonic = 2.0 * math.pi / beta
    assert_close(
        direct_matsubara_transform(energies, beta, first_nonzero_bosonic, diagonal_a, diagonal_b),
        0.0,
        "constant spectral term has no nonzero Matsubara coefficient",
    )


def check_low_frequency_transport_instability() -> None:
    beta = 2.0
    eta_star = 0.9
    epsilon = 1.0e-4
    tau_samples = [0.1, 0.4, 0.9, 1.6, 1.9]
    noise_floor = 1.0e-3

    # The positive-frequency spectral family has rho(omega)=2 eta_star omega
    # on (0, epsilon), hence the channel slope rho/(2 omega) is eta_star for
    # every epsilon even though its Euclidean transform is O(epsilon).
    for omega in [0.25 * epsilon, 0.5 * epsilon, 0.75 * epsilon]:
        rho = 2.0 * eta_star * omega
        assert_close(rho / (2.0 * omega), eta_star, "fixed low-frequency channel slope")

    bound = 6.0 * eta_star * epsilon / beta
    for tau in tau_samples:
        delta_g = low_frequency_transport_bump(beta, tau, epsilon, eta_star)
        if not 0.0 <= delta_g <= bound:
            raise AssertionError("Euclidean low-frequency bump exceeded chapter bound")
        if not delta_g < noise_floor:
            raise AssertionError("finite noisy Euclidean samples should not resolve this fixed-slope bump")

    larger = low_frequency_transport_bump(beta, beta / 2.0, 4.0 * epsilon, eta_star)
    smaller = low_frequency_transport_bump(beta, beta / 2.0, epsilon, eta_star)
    ratio = larger / smaller
    if not 3.9 < ratio < 4.1:
        raise AssertionError("Euclidean bump should scale linearly with epsilon at small epsilon")


def smooth_step_01(x: float) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    left = math.exp(-1.0 / x)
    right = math.exp(-1.0 / (1.0 - x))
    return left / (left + right)


def fixed_plateau_profile(x: float) -> float:
    if x < 0.0 or x >= 1.0:
        return 0.0
    transition = smooth_step_01(3.0 * x - 1.0)
    return 1.0 - transition


def smooth_plateau_bump(omega: float, epsilon: float, eta_star: float) -> float:
    return eta_star * fixed_plateau_profile(omega / epsilon)


def smooth_compensator(omega: float, center: float, radius: float) -> float:
    x = (omega - center) / radius
    if abs(x) >= 1.0:
        return 0.0
    return math.exp(-1.0 / (1.0 - x * x))


def integrate_midpoint(function, left: float, right: float, intervals: int = 900) -> float:
    step = (right - left) / intervals
    total = 0.0
    for index in range(intervals):
        total += function(left + (index + 0.5) * step) * step
    return total


def solve_two_by_two(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if abs(det) < 1.0e-14:
        raise AssertionError("compensator moment matrix must be invertible")
    return [
        (rhs[0] * matrix[1][1] - matrix[0][1] * rhs[1]) / det,
        (matrix[0][0] * rhs[1] - rhs[0] * matrix[1][0]) / det,
    ]


def check_finite_sum_rule_preserving_instability() -> None:
    beta = 2.0
    eta_star = 0.7
    epsilon0 = 1.0e-3
    epsilon = 1.0e-4
    centers = [0.75, 1.25]
    radius = 0.08

    # Preserve the two polynomial smooth sum rules int sigma and
    # int omega*sigma.  The bump is a fixed uniformly bounded profile scaled
    # into [0, epsilon].  The compensators are smooth compactly supported bumps
    # in fixed intervals away from the origin, where the polynomial weights
    # remain linearly independent.
    sum_rule_weights = [
        ("1", lambda omega: 1.0),
        ("omega", lambda omega: omega),
    ]
    moment_matrix = [
        [
            integrate_midpoint(
                lambda omega, weight=weight, center=center: weight(omega)
                * smooth_compensator(omega, center, radius),
                center - radius,
                center + radius,
            )
            for center in centers
        ]
        for _, weight in sum_rule_weights
    ]

    def compensated_data(trial_epsilon: float) -> tuple[list[float], list[float]]:
        bump_moments = [
            integrate_midpoint(
                lambda omega, weight=weight: weight(omega)
                * smooth_plateau_bump(omega, trial_epsilon, eta_star),
                0.0,
                trial_epsilon,
            )
            for _, weight in sum_rule_weights
        ]
        coefficients = solve_two_by_two(moment_matrix, [-bump_moments[0], -bump_moments[1]])
        return bump_moments, coefficients

    bump_moments, coefficients = compensated_data(epsilon)
    h_moments = [
        bump_moments[row] + sum(coefficients[index] * moment_matrix[row][index] for index in range(2))
        for row in range(2)
    ]
    for (name, _), moment in zip(sum_rule_weights, h_moments):
        assert_close(moment, 0.0, f"compensated perturbation preserves polynomial sum rule {name}")

    def h_value(omega: float, trial_epsilon: float, trial_coefficients: list[float]) -> float:
        return smooth_plateau_bump(omega, trial_epsilon, eta_star) + sum(
            trial_coefficients[index] * smooth_compensator(omega, centers[index], radius)
            for index in range(2)
        )

    support_right = max(centers) + radius
    reference_scale = 3.0

    def reference_spectrum(omega: float) -> float:
        return reference_scale * math.exp(-omega)

    grid = [support_right * index / 2000.0 for index in range(2001)]
    trial_epsilons = [epsilon0, epsilon0 / 2.0, epsilon0 / 4.0, epsilon]
    h_sup = 0.0
    coefficient_samples = {}
    for trial_epsilon in trial_epsilons:
        profile_sup = max(
            abs(smooth_plateau_bump(trial_epsilon * index / 200.0, trial_epsilon, eta_star))
            for index in range(201)
        )
        if profile_sup > eta_star * (1.0 + 1.0e-12):
            raise AssertionError("fixed bump profile should be uniformly bounded")
        _, trial_coefficients = compensated_data(trial_epsilon)
        coefficient_samples[trial_epsilon] = trial_coefficients
        h_sup = max(
            h_sup,
            max(abs(h_value(omega, trial_epsilon, trial_coefficients)) for omega in grid),
        )
    positivity_margin = reference_spectrum(support_right)
    amplitude = 0.5 * positivity_margin / h_sup
    if not 0.0 < amplitude < positivity_margin / h_sup:
        raise AssertionError("amplitude should obey the uniform positivity margin")

    for trial_epsilon, trial_coefficients in coefficient_samples.items():
        for omega in grid:
            perturbation = h_value(omega, trial_epsilon, trial_coefficients)
            plus = reference_spectrum(omega) + amplitude * perturbation
            minus = reference_spectrum(omega) - amplitude * perturbation
            if plus <= 0.0 or minus <= 0.0:
                raise AssertionError("smooth integrable reference spectrum should keep both perturbation signs positive")

    slope_plus = reference_spectrum(0.0) + amplitude * eta_star
    slope_minus = reference_spectrum(0.0) - amplitude * eta_star
    assert_close(
        slope_plus - slope_minus,
        2.0 * amplitude * eta_star,
        "same finite sum rules can have different slopes",
    )

    tau_samples = [0.25, 0.8, 1.5]

    scaled_changes = []
    for trial_epsilon in [epsilon0, epsilon0 / 2.0, epsilon0 / 4.0]:
        trial_coefficients = coefficient_samples[trial_epsilon]
        max_scaled_change = 0.0
        for tau in tau_samples:
            euclidean_change = integrate_midpoint(
                lambda omega: h_value(omega, trial_epsilon, trial_coefficients)
                * euclidean_transport_kernel(beta, tau, omega),
                0.0,
                trial_epsilon,
            )
            for center in centers:
                euclidean_change += integrate_midpoint(
                    lambda omega: h_value(omega, trial_epsilon, trial_coefficients)
                    * euclidean_transport_kernel(beta, tau, omega),
                    center - radius,
                    center + radius,
                )
            max_scaled_change = max(max_scaled_change, abs(euclidean_change) / trial_epsilon)
        scaled_changes.append(max_scaled_change)
        if max_scaled_change > 20.0:
            raise AssertionError("finite-sum-rule-preserving perturbation should remain Euclidean O(epsilon)")
    if max(scaled_changes) > 2.0 * min(scaled_changes):
        raise AssertionError("smooth compensated perturbation should have a stable O(epsilon) scale")


def check_adversarial_weights_need_restricted_independence() -> None:
    epsilon0 = 1.0e-3
    centers = [0.75, 1.25]
    radius = 0.08

    def low_frequency_weight_bump(omega: float) -> float:
        return smooth_compensator(omega, 0.25 * epsilon0, 0.10 * epsilon0)

    weights = [
        lambda omega: 1.0,
        lambda omega: 1.0 + low_frequency_weight_bump(omega),
    ]
    if abs(weights[1](0.25 * epsilon0) - weights[0](0.25 * epsilon0)) < 1.0e-6:
        raise AssertionError("adversarial weights should be globally independent")

    moment_matrix = [
        [
            integrate_midpoint(
                lambda omega, weight=weight, center=center: weight(omega)
                * smooth_compensator(omega, center, radius),
                center - radius,
                center + radius,
            )
            for center in centers
        ]
        for weight in weights
    ]
    row_gap = max(abs(moment_matrix[0][column] - moment_matrix[1][column]) for column in range(2))
    if row_gap > 1.0e-12:
        raise AssertionError("low-frequency-only weight difference should vanish on compensator supports")

    det = moment_matrix[0][0] * moment_matrix[1][1] - moment_matrix[0][1] * moment_matrix[1][0]
    if abs(det) > 1.0e-12:
        raise AssertionError("dependent restricted weights must not admit this compensator matrix")


def check_chemical_potential_twist() -> None:
    beta = 2.0
    mu = 0.37
    charge = 3
    spin_sign = -1
    twist = spin_sign * math.exp(beta * mu * charge)

    # If a field with the original thermal spin structure is redefined by
    # Phi(tau)=exp(mu*q*tau) phi(tau), the new variable has the twisted
    # boundary condition used in the chapter.
    phi_zero = 1.2 - 0.4j
    phi_beta = spin_sign * phi_zero
    big_phi_zero = phi_zero
    big_phi_beta = math.exp(beta * mu * charge) * phi_beta
    assert_close(big_phi_beta, twist * big_phi_zero, "chemical potential is a thermal twist")

    imaginary_mu_period = 2.0 * math.pi / beta
    phase = cmath.exp(1j * beta * imaginary_mu_period * charge)
    assert_close(phase, 1.0, "integer charges give large-gauge periodicity for imaginary chemical potential")


def main() -> None:
    check_matsubara_boundary_phases()
    check_one_mode_fermionic_trace_identity()
    check_bosonic_spectral_representation()
    check_low_frequency_transport_instability()
    check_finite_sum_rule_preserving_instability()
    check_adversarial_weights_need_restricted_independence()
    check_chemical_potential_twist()
    print("Finite-temperature path-integral convention and compensator-scope checks passed.")


if __name__ == "__main__":
    main()
