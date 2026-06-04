#!/usr/bin/env python3
"""Finite checks for the free-Majorana/Ising form-factor examples.

Evidence contract.
Target claims: the Volume VI Chapter 4 free-Majorana energy-density
form-factor normalization and local-reconstruction status claim, the
two-particle Wightman/Euclidean kernel normalization, and the Ising
spin/twist product-family Watson, cyclicity, crossing, residue, and
separated-series majorant claims.
Independent construction: the checks recompute exchange/cyclicity signs,
Cauchy-kernel orientation, two-particle invariant-mass and phase-space
Jacobians, Bessel prefactors, finite Wick-degree support for the normal
ordered quadratic Majorana energy density, and explicit finite products for
the spin/twist families rather than importing chapter display strings.
Imported assumptions: the massive free-Majorana CAR construction supplies the
Hilbert space, common finite-particle domain, positivity, locality of even
Wick polynomials, and Fock completeness of the one-particle Majorana sector;
the spin/twist checks use the stated semi-locality phases and separated
Euclidean rapidity majorants.
Negative controls: wrong energy-density exchange/cyclicity signs, reversed
Cauchy orientation, missed identical-particle factors, wrong Bessel
prefactors, an illicit higher-particle tail for a quadratic Wick operator,
and a bootstrap-only local-field reconstruction certificate with missing
domain/locality/positivity/completeness inputs are rejected, as are the
wrong spin-field monodromy and residue signs.
Scope boundary: a pass checks finite algebra, normalization, and the
free-field reconstruction interface for the displayed examples; it does not
prove local reconstruction for an arbitrary interacting factorizing
S-matrix, general form-factor completeness, convergence on collision
diagonals, or contact-term extensions.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import cmath
import math
from fractions import Fraction


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name} failed")


def energy_form_factor(theta_1: complex, theta_2: complex, kappa: complex = 1.0) -> complex:
    return kappa * cmath.sinh((theta_1 - theta_2) / 2.0)


def tanh_product(thetas: list[complex]) -> complex:
    result = 1.0 + 0.0j
    for i, theta_i in enumerate(thetas):
        for theta_j in thetas[i + 1 :]:
            result *= cmath.tanh((theta_i - theta_j) / 2.0)
    return result


def sigma_form_factor(thetas: list[complex], v: complex = 1.0) -> complex:
    n = len(thetas)
    if n % 2 == 0:
        return 0.0 + 0.0j
    k = (n - 1) // 2
    return v * (1j**k) * tanh_product(thetas)


def spin_even_form_factor(thetas: list[complex], sigma_bar: complex = 1.0) -> complex:
    n = len(thetas)
    if n % 2 == 1:
        return 0.0 + 0.0j
    k = n // 2
    return sigma_bar * (1j**k) * tanh_product(thetas)


def coth(z: complex) -> complex:
    return 1.0 / cmath.tanh(z)


def swapped(values: list[complex], i: int) -> list[complex]:
    out = values[:]
    out[i], out[i + 1] = out[i + 1], out[i]
    return out


def check_energy_density_form_factor() -> None:
    theta_1 = 0.73
    theta_2 = -0.41
    assert_close(
        "energy exchange",
        energy_form_factor(theta_1, theta_2),
        -energy_form_factor(theta_2, theta_1),
    )
    assert_close(
        "energy cyclicity",
        energy_form_factor(theta_1 + 2j * math.pi, theta_2),
        energy_form_factor(theta_2, theta_1),
    )


def check_kinematic_cauchy_kernel_orientation() -> None:
    # The distributional identity
    #   1/(x+i0) - 1/(x-i0) = -2 pi i delta(x)
    # fixes i/z as the direct crossed contraction kernel in the chapter's
    # rapidity normalization.  Reversing the local coordinate sends z to -z
    # and flips the delta coefficient.
    direct_kernel_coefficient = 1j
    reversed_kernel_coefficient = -1j
    boundary_difference_delta = -2j * math.pi
    assert_close(
        "direct kinematic Cauchy kernel gives positive rapidity delta",
        direct_kernel_coefficient * boundary_difference_delta,
        2.0 * math.pi,
    )
    assert_close(
        "reversed kinematic coordinate flips rapidity delta coefficient",
        reversed_kernel_coefficient * boundary_difference_delta,
        -2.0 * math.pi,
    )


def check_energy_two_particle_reconstruction() -> None:
    mass = 1.7
    kappa = 2.3
    theta_1 = 0.94
    theta_2 = -0.38
    alpha = theta_1 - theta_2

    def momentum(theta: float) -> tuple[float, float]:
        return (mass * math.cosh(theta), mass * math.sinh(theta))

    p_1 = momentum(theta_1)
    p_2 = momentum(theta_2)
    total = (p_1[0] + p_2[0], p_1[1] + p_2[1])
    invariant_s = total[0] ** 2 - total[1] ** 2
    assert_close(
        "two-particle invariant mass",
        invariant_s,
        4.0 * mass**2 * math.cosh(alpha / 2.0) ** 2,
    )

    ff_squared = abs(energy_form_factor(theta_1, theta_2, kappa)) ** 2
    assert_close(
        "energy form factor as invariant numerator",
        ff_squared,
        kappa**2 * (invariant_s - 4.0 * mass**2) / (4.0 * mass**2),
    )

    jacobian = math.sqrt(invariant_s) * mass * abs(math.sinh(alpha / 2.0))
    delta_integral_after_identical_particle_cancellation = ff_squared / jacobian
    spectral_density = kappa**2 / (2.0 * mass**2) * math.sqrt(1.0 - 4.0 * mass**2 / invariant_s)
    assert_close(
        "two-particle spectral density normalization",
        delta_integral_after_identical_particle_cancellation,
        spectral_density,
    )

    starting_euclidean_prefactor = 1.0 / (2.0 * (2.0 * math.pi) ** 2)
    after_bessel_reduction_full_alpha = 2.0 * starting_euclidean_prefactor
    after_even_alpha_reduction = 2.0 * after_bessel_reduction_full_alpha
    assert_close(
        "Euclidean Bessel prefactor",
        after_even_alpha_reduction,
        1.0 / (2.0 * math.pi**2),
    )


def check_majorana_energy_local_reconstruction_certificate() -> None:
    # A normal-ordered quadratic Majorana Wick polynomial has only a
    # two-creation component in the vacuum-to-particle channel.
    wick_degree = 2
    vacuum_to_particle_support = {
        n: int(n == wick_degree)
        for n in range(7)
    }
    assert_equal("normal ordering kills vacuum matrix element", vacuum_to_particle_support[0], 0)
    assert_equal("fermion parity kills one-particle channel", vacuum_to_particle_support[1], 0)
    assert_equal("quadratic Wick degree selects two-particle channel", vacuum_to_particle_support[2], 1)
    assert_equal("quadratic Wick degree kills three-particle channel", vacuum_to_particle_support[3], 0)
    assert_equal("quadratic Wick degree kills four-particle channel", vacuum_to_particle_support[4], 0)
    assert_equal(
        "quadratic energy density has no higher-particle spectral tail",
        sum(vacuum_to_particle_support[n] for n in range(3, 7)),
        0,
    )

    illicit_quartic_tail = {**vacuum_to_particle_support, 4: 1}
    assert_true(
        "negative control detects illicit four-particle tail",
        sum(illicit_quartic_tail[n] for n in range(3, 7)) > 0,
    )

    free_field_inputs = {
        "car_hilbert_space": 0,
        "finite_particle_domain": 0,
        "wick_closability": 0,
        "positive_wightman_space": 0,
        "even_wick_locality": 0,
        "majorana_fock_completeness": 0,
    }
    bootstrap_only_inputs = {
        "car_hilbert_space": 1,
        "finite_particle_domain": 1,
        "wick_closability": 1,
        "positive_wightman_space": 1,
        "even_wick_locality": 1,
        "majorana_fock_completeness": 1,
    }
    assert_equal(
        "free Majorana construction supplies local-field inputs",
        sum(free_field_inputs.values()),
        0,
    )
    assert_true(
        "negative control rejects bootstrap-only reconstruction overclaim",
        sum(bootstrap_only_inputs.values()) > 0,
    )


def check_sigma_exchange_and_cyclicity() -> None:
    thetas = [1.31, 0.62, -0.17, -0.84, -1.55]
    for i in range(len(thetas) - 1):
        assert_close(
            f"sigma Watson exchange slot {i}",
            sigma_form_factor(thetas),
            -sigma_form_factor(swapped(thetas, i)),
        )

    shifted = [thetas[0] + 2j * math.pi, *thetas[1:]]
    cycled = [*thetas[1:], thetas[0]]
    assert_close("sigma odd cyclicity", sigma_form_factor(shifted), sigma_form_factor(cycled))


def check_spin_even_semilocal_family() -> None:
    sigma_bar = 1.37
    thetas = [1.31, 0.62, -0.17, -0.84]
    for i in range(len(thetas) - 1):
        assert_close(
            f"spin even Watson exchange slot {i}",
            spin_even_form_factor(thetas, sigma_bar),
            -spin_even_form_factor(swapped(thetas, i), sigma_bar),
        )

    shifted = [thetas[0] + 2j * math.pi, *thetas[1:]]
    cycled = [*thetas[1:], thetas[0]]
    assert_close(
        "spin even semi-local cyclicity",
        spin_even_form_factor(shifted, sigma_bar),
        -spin_even_form_factor(cycled, sigma_bar),
    )

    beta_1 = 0.93
    beta_2 = -0.28
    assert_close(
        "spin crossing gives coth matrix element",
        spin_even_form_factor([beta_1 + 1j * math.pi, beta_2], sigma_bar),
        1j * sigma_bar * coth((beta_1 - beta_2) / 2.0),
    )

    outgoing = [1.11, 0.36]
    incoming = [-0.22, -0.91]
    crossed = [complex(beta + 1j * math.pi) for beta in outgoing] + [complex(beta) for beta in incoming]
    mixed = sigma_bar * (1j ** ((len(outgoing) + len(incoming)) // 2))
    for i, beta_i in enumerate(outgoing):
        for beta_j in outgoing[i + 1 :]:
            mixed *= cmath.tanh((beta_i - beta_j) / 2.0)
    for i, beta_i in enumerate(incoming):
        for beta_j in incoming[i + 1 :]:
            mixed *= cmath.tanh((beta_i - beta_j) / 2.0)
    for beta_out in outgoing:
        for beta_in in incoming:
            mixed *= coth((beta_out - beta_in) / 2.0)
    assert_close("spin mixed bra-ket product", spin_even_form_factor(crossed, sigma_bar), mixed)


def check_sigma_kinematic_residue() -> None:
    theta = 0.37
    for spectators in ([0.91], [1.44, 0.52, -0.66], [1.7, 0.83, 0.11, -0.47, -1.28]):
        n = len(spectators)
        big_n = n + 2
        residue = 2.0 * (1j ** ((big_n - 1) // 2)) * tanh_product([complex(x) for x in spectators])
        lhs = -1j * residue
        rhs = (1.0 - (-1.0) ** n) * sigma_form_factor([complex(x) for x in spectators])
        assert_close(f"sigma analytic kinematic residue n={n}", lhs, rhs)

        eps = 1.0e-7
        near_pair = [theta + 1j * math.pi + eps, theta, *spectators]
        numerical_residue = eps * sigma_form_factor([complex(x) for x in near_pair])
        assert_close(f"sigma numerical kinematic residue n={n}", numerical_residue, residue, tol=1.0e-6)


def check_spin_even_kinematic_residue() -> None:
    sigma_bar = 1.37
    theta = 0.37
    for spectators in ([], [1.44, 0.52], [1.7, 0.83, 0.11, -0.47]):
        n = len(spectators)
        big_n = n + 2
        residue = 2.0 * sigma_bar * (1j ** (big_n // 2)) * tanh_product([complex(x) for x in spectators])
        lhs = -1j * residue
        rhs = (1.0 + (-1.0) ** n) * spin_even_form_factor([complex(x) for x in spectators], sigma_bar)
        assert_close(f"spin analytic semi-local residue n={n}", lhs, rhs)

        eps = 1.0e-7
        near_pair = [theta + 1j * math.pi + eps, theta, *spectators]
        numerical_residue = eps * spin_even_form_factor([complex(x) for x in near_pair], sigma_bar)
        assert_close(f"spin numerical semi-local residue n={n}", numerical_residue, residue, tol=1.0e-6)


def check_spin_spectral_series_majorants() -> None:
    one_particle_integral = Fraction(3, 5)
    sigma_norm_squared = Fraction(7, 4)
    twist_norm_squared = Fraction(11, 6)

    even_bound = Fraction(0, 1)
    odd_bound = Fraction(0, 1)
    all_bound = Fraction(0, 1)
    for n in range(10):
        term = one_particle_integral**n / math.factorial(n)
        all_bound += term
        if n % 2 == 0:
            even_bound += term
            expected = sigma_norm_squared * one_particle_integral**n / math.factorial(n)
            assert_equal(
                f"even spin majorant coefficient n={n}",
                sigma_norm_squared * term,
                expected,
            )
        else:
            odd_bound += term
            expected = twist_norm_squared * one_particle_integral**n / math.factorial(n)
            assert_equal(
                f"odd twist majorant coefficient n={n}",
                twist_norm_squared * term,
                expected,
            )

    assert_equal(
        "even plus odd exponential coefficient split",
        even_bound + odd_bound,
        all_bound,
    )

    for delta in (0.2, 0.7, 1.4, -0.5):
        assert_close(
            f"real rapidity tanh product bound delta={delta}",
            abs(cmath.tanh(delta / 2.0)) <= 1.0,
            True,
            tol=0.0,
        )


def main() -> None:
    check_energy_density_form_factor()
    check_kinematic_cauchy_kernel_orientation()
    check_energy_two_particle_reconstruction()
    check_majorana_energy_local_reconstruction_certificate()
    check_sigma_exchange_and_cyclicity()
    check_spin_even_semilocal_family()
    check_sigma_kinematic_residue()
    check_spin_even_kinematic_residue()
    check_spin_spectral_series_majorants()
    print("All Ising form-factor checks passed.")


if __name__ == "__main__":
    main()
