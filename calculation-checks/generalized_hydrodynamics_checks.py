#!/usr/bin/env python3
"""Finite algebra checks for the generalized-hydrodynamics bridge.

Evidence contract.
Target claims: the Volume VI GHD dressing/current identity, hard-rod
effective-velocity calibration, and the observable-level residual certificate
separating Euler root-density closure from microscopic density/current
reconstruction.
Independent construction: exact finite-grid linear solves, hard-rod collision
shift algebra, signed residual telescopes, and negative controls are computed
directly from finite rational data.
Imported assumptions: the diagonal TBA local-cell variables, the finite
kernel/filling chart, the existence of the dressed inverse, and the chapter's
Euler-scale residual names are assumed as finite input.
Negative controls: bare velocities are rejected in interacting cells, exact
root-density continuity is rejected as a microscopic observable proof, and
omitting the operator-current residual underbudgets the observable error.
Scope boundary: these checks verify finite algebra and bookkeeping
interfaces; they do not prove local equilibration, finite-volume convergence,
diffusive corrections, or a microscopic GHD theorem for a local QFT.
"""

from __future__ import annotations

from fractions import Fraction


def assert_close(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def solve_2x2(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        raise AssertionError("singular two-by-two dressing matrix")
    return [
        (rhs[0] * matrix[1][1] - matrix[0][1] * rhs[1]) / det,
        (matrix[0][0] * rhs[1] - rhs[0] * matrix[1][0]) / det,
    ]


def check_two_species_dressing_current_identity() -> None:
    # Finite-grid version of h^dr = h + K n h^dr.
    kernel = [
        [Fraction(1, 5), Fraction(-1, 7)],
        [Fraction(2, 9), Fraction(1, 6)],
    ]
    filling = [Fraction(1, 3), Fraction(2, 5)]
    p_prime = [Fraction(7, 3), Fraction(5, 2)]
    e_prime = [Fraction(4, 3), Fraction(-3, 2)]
    charge = [Fraction(2, 1), Fraction(-1, 3)]

    dressing_matrix = [
        [
            (Fraction(1) if i == j else Fraction(0)) - kernel[i][j] * filling[j]
            for j in range(2)
        ]
        for i in range(2)
    ]
    p_dr = solve_2x2(dressing_matrix, p_prime)
    e_dr = solve_2x2(dressing_matrix, e_prime)
    charge_dr = solve_2x2(dressing_matrix, charge)

    for i in range(2):
        reconstructed = charge[i] + sum(kernel[i][j] * filling[j] * charge_dr[j] for j in range(2))
        assert_close(f"dressing equation component {i}", charge_dr[i], reconstructed)

    # Ignore the common 2*pi factor: rho_i = n_i (p'_i)^dr and
    # rho_i v_i^eff = n_i (E'_i)^dr.
    root_density = [filling[i] * p_dr[i] for i in range(2)]
    velocity = [e_dr[i] / p_dr[i] for i in range(2)]
    current_from_velocity = sum(charge[i] * root_density[i] * velocity[i] for i in range(2))
    current_from_dressed_energy = sum(charge[i] * filling[i] * e_dr[i] for i in range(2))
    assert_close("GHD charge current identity", current_from_velocity, current_from_dressed_energy)

    bare_velocity = [e_prime[i] / p_prime[i] for i in range(2)]
    bare_velocity_current = sum(
        charge[i] * root_density[i] * bare_velocity[i] for i in range(2)
    )
    if bare_velocity_current == current_from_velocity:
        raise AssertionError(
            "bare velocities should not replace dressed effective velocities in an interacting cell"
        )


def check_hard_rod_effective_velocity_solution() -> None:
    length = Fraction(1, 3)
    velocities = [Fraction(-2, 1), Fraction(1, 1), Fraction(5, 1)]
    densities = [Fraction(1, 10), Fraction(1, 5), Fraction(1, 8)]
    total_density = sum(densities)
    assert length * total_density < 1

    bare_current = sum(rho * velocity for rho, velocity in zip(densities, velocities, strict=True))
    effective = [
        (velocity - length * bare_current) / (1 - length * total_density)
        for velocity in velocities
    ]
    effective_current = sum(rho * velocity for rho, velocity in zip(densities, effective, strict=True))
    assert_close("hard-rod effective current equals bare velocity density", effective_current, bare_current)

    for i, velocity in enumerate(velocities):
        rhs = velocity + length * sum(
            densities[j] * (effective[i] - effective[j]) for j in range(len(velocities))
        )
        assert_close(f"hard-rod effective velocity equation {i}", effective[i], rhs)


def check_ghd_observable_residual_certificate() -> None:
    # Finite analogue of the observable certificate in
    # ca:ghd-observable-reconstruction-certificate.  The Euler-cell density and
    # current are not microscopic observables until local-cell replacement,
    # Bethe-Yang counting, dressing stability, gradients, operator projection,
    # diffusion, and integrability-breaking residuals are controlled.
    ghd_density = Fraction(7, 5)
    ghd_current = Fraction(-3, 4)

    density_residuals = {
        "cell": Fraction(1, 30),
        "Bethe-Yang": Fraction(1, 42),
        "dressing": Fraction(1, 70),
        "gradient": Fraction(1, 105),
        "operator": Fraction(1, 60),
        "dissipative": Fraction(1, 84),
        "breaking": Fraction(1, 140),
    }
    current_residuals = {
        "cell": Fraction(1, 24),
        "Bethe-Yang": Fraction(1, 36),
        "dressing": Fraction(1, 40),
        "gradient": Fraction(1, 72),
        "operator": Fraction(1, 18),
        "dissipative": Fraction(1, 90),
        "breaking": Fraction(1, 120),
    }

    microscopic_density = ghd_density + sum(density_residuals.values(), Fraction(0))
    microscopic_current = ghd_current + sum(current_residuals.values(), Fraction(0))
    actual_error = abs(microscopic_density - ghd_density) + abs(microscopic_current - ghd_current)
    certificate = sum(
        abs(value)
        for value in list(density_residuals.values()) + list(current_residuals.values())
    )
    if not actual_error <= certificate:
        raise AssertionError("GHD observable residual certificate failed")

    # Exact root-density continuity only removes the Euler closure residual.  It
    # does not remove the operator/current projection residual.
    exact_root_continuity_residual = Fraction(0)
    operator_current_residual = current_residuals["operator"]
    if exact_root_continuity_residual + operator_current_residual == 0:
        raise AssertionError("operator-current residual accidentally vanished")

    omitted_operator_budget = certificate - abs(operator_current_residual)
    all_positive_current_residuals = {
        "cell": Fraction(1, 24),
        "Bethe-Yang": Fraction(1, 36),
        "dressing": Fraction(1, 40),
        "gradient": Fraction(1, 72),
        "operator": Fraction(1, 18),
        "dissipative": Fraction(1, 90),
        "breaking": Fraction(1, 120),
    }
    positive_current_error = sum(all_positive_current_residuals.values(), Fraction(0))
    positive_current_budget_without_operator = (
        positive_current_error - all_positive_current_residuals["operator"]
    )
    if positive_current_error <= positive_current_budget_without_operator:
        raise AssertionError("omitting operator-current residual should underbudget the current error")
    if actual_error <= omitted_operator_budget:
        raise AssertionError("omitting operator-current residual should underbudget the observable certificate")


def main() -> None:
    check_two_species_dressing_current_identity()
    check_hard_rod_effective_velocity_solution()
    check_ghd_observable_residual_certificate()
    print("All generalized-hydrodynamics finite algebra checks passed.")


if __name__ == "__main__":
    main()
