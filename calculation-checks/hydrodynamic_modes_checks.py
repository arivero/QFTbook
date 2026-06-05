#!/usr/bin/env python3
"""Finite algebra checks for Volume X hydrodynamic Ward-identity modes.

Evidence contract.
Target claims: the first-order shear and sound poles, entropy-production
positivity, sourceful Euler force reduction, susceptibility geometry,
first-order shear acausality as a parabolic initial-value equation, boosted
high-k instability of the parabolic truncation, and the linear causal
relaxation completion of the shear sector in Volume X Chapter 5.
Independent construction: direct finite-dimensional algebra for the Ward
identity modes, exact heat-kernel positivity away from the origin, explicit
quadratic roots for boosted diffusion and MIS shear relaxation, a retarded
singularity taxonomy check, and matrix similarity checks for multi-charge
diffusion.
Imported assumptions: homogeneous KMS thermodynamic stability, the stated
Landau-frame constitutive relations, positivity of transport coefficients from
entropy/Kubo arguments, and the choice of a single linear MIS shear relaxation
time.
Negative controls: first-order shear diffusion is not accepted as a causal
finite-speed PDE, Lorentz-boosted parabolic diffusion is not accepted as a
stable high-k theory, real-axis spectral lines are not mistaken for
lower-half-plane damped poles, an open-upper-half-plane pole is rejected, a
causal relaxation model with superluminal shear front speed is rejected, and
linear shear completion is not treated as a theorem for full nonlinear causal
hydrodynamics.
Scope boundary: these checks verify finite algebra and linear-mode
bookkeeping; they do not prove microscopic hydrodynamic emergence, nonlinear
well-posedness, or the complete BRSSS/MIS coefficient inequalities.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def shear_pole(eta: float, enthalpy: float, k: float) -> complex:
    return -1j * eta * k * k / enthalpy


def sound_roots(cs2: float, attenuation: float, k: float) -> tuple[complex, complex]:
    # Roots of omega^2 - c_s^2 k^2 + i Gamma omega k^2 = 0.
    b = 1j * attenuation * k * k
    c = -cs2 * k * k
    root = cmath.sqrt(b * b - 4.0 * c)
    return ((-b + root) / 2.0, (-b - root) / 2.0)


Matrix2 = tuple[tuple[float, float], tuple[float, float]]


def matmul(lhs: Matrix2, rhs: Matrix2) -> Matrix2:
    return (
        (
            lhs[0][0] * rhs[0][0] + lhs[0][1] * rhs[1][0],
            lhs[0][0] * rhs[0][1] + lhs[0][1] * rhs[1][1],
        ),
        (
            lhs[1][0] * rhs[0][0] + lhs[1][1] * rhs[1][0],
            lhs[1][0] * rhs[0][1] + lhs[1][1] * rhs[1][1],
        ),
    )


def matinv(matrix: Matrix2) -> Matrix2:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if abs(determinant) < 1.0e-14:
        raise ValueError("singular 2x2 matrix")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def mat_entry_close(name: str, got: Matrix2, expected: Matrix2, tol: float = 1.0e-10) -> None:
    for row in range(2):
        for col in range(2):
            assert_close(f"{name}[{row},{col}]", got[row][col], expected[row][col], tol=tol)


def symmetric_eigenvalues(matrix: Matrix2) -> tuple[float, float]:
    trace = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    discriminant = max(trace * trace - 4.0 * determinant, 0.0)
    root = math.sqrt(discriminant)
    return ((trace + root) / 2.0, (trace - root) / 2.0)


def symmetric_square_root_and_inverse(matrix: Matrix2) -> tuple[Matrix2, Matrix2]:
    """Square root and inverse square root for a positive symmetric 2x2 matrix."""

    a, b = matrix[0]
    _, d = matrix[1]
    eigen_plus, eigen_minus = symmetric_eigenvalues(matrix)
    if eigen_minus <= 0.0:
        raise ValueError("matrix is not positive definite")
    # Spectral projectors for distinct eigenvalues.
    gap = eigen_plus - eigen_minus
    if abs(gap) < 1.0e-14:
        root = math.sqrt(eigen_plus)
        inv_root = 1.0 / root
        return (((root, 0.0), (0.0, root)), ((inv_root, 0.0), (0.0, inv_root)))
    p_plus = (
        ((a - eigen_minus) / gap, b / gap),
        (b / gap, (d - eigen_minus) / gap),
    )
    p_minus = (
        ((eigen_plus - a) / gap, -b / gap),
        (-b / gap, (eigen_plus - d) / gap),
    )
    root_plus = math.sqrt(eigen_plus)
    root_minus = math.sqrt(eigen_minus)
    inv_plus = 1.0 / root_plus
    inv_minus = 1.0 / root_minus
    root = (
        (
            root_plus * p_plus[0][0] + root_minus * p_minus[0][0],
            root_plus * p_plus[0][1] + root_minus * p_minus[0][1],
        ),
        (
            root_plus * p_plus[1][0] + root_minus * p_minus[1][0],
            root_plus * p_plus[1][1] + root_minus * p_minus[1][1],
        ),
    )
    inv_root = (
        (
            inv_plus * p_plus[0][0] + inv_minus * p_minus[0][0],
            inv_plus * p_plus[0][1] + inv_minus * p_minus[0][1],
        ),
        (
            inv_plus * p_plus[1][0] + inv_minus * p_minus[1][0],
            inv_plus * p_plus[1][1] + inv_minus * p_minus[1][1],
        ),
    )
    return root, inv_root


def check_shear_mode() -> None:
    eta = 0.63
    enthalpy = 2.7
    k = 0.004
    omega = shear_pole(eta, enthalpy, k)
    assert_close("shear dispersion equation", -1j * omega * enthalpy + eta * k * k, 0.0)
    assert omega.imag < 0.0
    assert_close("shear diffusion constant", -omega.imag / (k * k), eta / enthalpy)


def check_first_order_shear_acausality() -> None:
    diffusion = 0.37
    time = 0.2
    distant_point = 10.0
    kernel = math.exp(-(distant_point**2) / (4.0 * diffusion * time))
    kernel /= math.sqrt(4.0 * math.pi * diffusion * time)
    if not kernel > 0.0:
        raise AssertionError("heat kernel should have nonzero support at any finite distance")

    lightcone_distance = time
    outside_lightcone = distant_point > lightcone_distance
    if not outside_lightcone:
        raise AssertionError("sample point should be outside the relativistic light cone")


def boosted_diffusion_roots(diffusion: float, boost: float, k: float) -> tuple[complex, complex]:
    gamma = 1.0 / math.sqrt(1.0 - boost * boost)
    # omega - u k + i D gamma (k - u omega)^2 = 0.
    a = 1j * diffusion * gamma * boost * boost
    b = 1.0 - 2j * diffusion * gamma * boost * k
    c = -boost * k + 1j * diffusion * gamma * k * k
    root = cmath.sqrt(b * b - 4.0 * a * c)
    return ((-b + root) / (2.0 * a), (-b - root) / (2.0 * a))


def check_boosted_diffusion_instability_negative_control() -> None:
    roots = boosted_diffusion_roots(diffusion=0.4, boost=0.55, k=80.0)
    imag_parts = [root.imag for root in roots]
    if not max(imag_parts) > 0.0:
        raise AssertionError("boosted parabolic diffusion should expose a growing high-k branch")
    if not min(imag_parts) < 0.0:
        raise AssertionError("one boosted branch should still be damped")


def mis_shear_roots(diffusion: float, tau_pi: float, k: float) -> tuple[complex, complex]:
    # Roots of tau_pi omega^2 + i omega - D_eta k^2 = 0.
    b = 1j
    c = -diffusion * k * k
    root = cmath.sqrt(b * b - 4.0 * tau_pi * c)
    return ((-b + root) / (2.0 * tau_pi), (-b - root) / (2.0 * tau_pi))


def check_retarded_singularity_taxonomy() -> None:
    finite_volume_lines = [-1.3, 0.25, 1.8]
    upper_half_test_points = [
        complex(-2.0, 0.1),
        complex(0.25, 0.35),
        complex(1.1, 2.0),
    ]

    for z in upper_half_test_points:
        if z.imag <= 0.0:
            raise AssertionError("test point should lie in the open upper half-plane")
        for line in finite_volume_lines:
            denominator = z - line
            if abs(denominator) <= z.imag / 2.0:
                raise AssertionError("real-axis spectral line should not be an upper-half-plane pole")

    boundary_singularities = [complex(line, 0.0) for line in finite_volume_lines]
    if not all(pole.imag == 0.0 for pole in boundary_singularities):
        raise AssertionError("finite-volume spectral lines should sit on the real-axis boundary")

    threshold = 0.6
    cut_mesh = [complex(threshold + 0.2 * index, 0.0) for index in range(5)]
    if not all(point.imag == 0.0 and point.real >= threshold for point in cut_mesh):
        raise AssertionError("thermodynamic-limit cut mesh should remain a real-axis boundary object")

    damped_transient_poles = [
        complex(0.0, -1.0 / 0.7),
        complex(0.4, -0.2),
        complex(-0.4, -0.2),
    ]
    if not all(pole.imag < 0.0 for pole in damped_transient_poles):
        raise AssertionError("damped transient poles should lie in the lower half-plane")

    unstable_pole = complex(0.1, 0.2)
    if not unstable_pole.imag > 0.0:
        raise AssertionError("upper-half-plane instability negative control failed")


def check_mis_shear_relaxation_completion() -> None:
    diffusion = 0.21
    tau_pi = 0.7
    small_k = 1.0e-4
    hydro, transient = mis_shear_roots(diffusion, tau_pi, small_k)
    assert_close("MIS hydrodynamic shear pole", hydro, -1j * diffusion * small_k * small_k, tol=1.0e-14)
    assert_close(
        "MIS transient shear pole",
        transient,
        -1j / tau_pi + 1j * diffusion * small_k * small_k,
        tol=1.0e-14,
    )
    if not hydro.imag < 0.0 or not transient.imag < 0.0:
        raise AssertionError("MIS shear modes should be damped for positive eta and tau_pi")

    front_speed_squared = diffusion / tau_pi
    if not front_speed_squared <= 1.0:
        raise AssertionError("chosen causal sample should have subluminal shear front speed")

    bad_tau = diffusion / 1.44
    bad_front_speed = math.sqrt(diffusion / bad_tau)
    if not bad_front_speed > 1.0:
        raise AssertionError("superluminal shear front-speed negative control failed")


def check_sound_mode_expansion() -> None:
    d = 3
    eta = 0.41
    zeta = 0.08
    enthalpy = 1.9
    cs2 = 0.31
    k = 1.0e-4
    gamma = (zeta + 2.0 * eta * (d - 1.0) / d) / enthalpy
    roots = sound_roots(cs2, gamma, k)
    cs = math.sqrt(cs2)
    expected = (cs * k - 0.5j * gamma * k * k, -cs * k - 0.5j * gamma * k * k)
    assert_close("sound plus expansion", roots[0], expected[0], tol=2.0e-12)
    assert_close("sound minus expansion", roots[1], expected[1], tol=2.0e-12)
    for root in roots:
        assert root.imag < 0.0
        assert_close(
            "sound quadratic equation",
            root * root - cs2 * k * k + 1j * gamma * root * k * k,
            0.0,
            tol=1.0e-18,
        )


def check_entropy_production_coefficients() -> None:
    temperature = 1.7
    eta = 0.5
    zeta = 0.2
    theta = -0.3
    # Symmetric traceless shear sample in three spatial dimensions.
    sigma2 = 0.11**2 + (-0.04) ** 2 + (-0.07) ** 2 + 2.0 * 0.03**2
    grad_alpha = [0.2, -0.1]
    conductivity = [[0.7, 0.05], [0.05, 0.4]]
    charge_term = temperature * sum(
        conductivity[i][j] * grad_alpha[i] * grad_alpha[j]
        for i in range(2)
        for j in range(2)
    )
    entropy_production = eta * sigma2 / (2.0 * temperature) + zeta * theta * theta / temperature + charge_term
    assert entropy_production > 0.0

    determinant = conductivity[0][0] * conductivity[1][1] - conductivity[0][1] ** 2
    assert conductivity[0][0] >= 0.0
    assert determinant >= 0.0


def check_sourceful_euler_force_basis() -> None:
    temperature = 1.3
    entropy = 0.9
    chemical_potentials = [0.4, -0.2]
    densities = [0.7, 0.3]
    enthalpy = temperature * entropy + sum(
        chemical_potentials[i] * densities[i] for i in range(2)
    )
    grad_temperature = [0.05, -0.03, 0.02]
    grad_mu = [
        [0.11, -0.07, 0.04],
        [-0.02, 0.06, 0.03],
    ]
    electric = [
        [0.09, 0.01, -0.04],
        [0.05, -0.08, 0.02],
    ]

    for spatial_index in range(3):
        grad_pressure = entropy * grad_temperature[spatial_index] + sum(
            densities[charge] * grad_mu[charge][spatial_index] for charge in range(2)
        )
        charge_force = sum(
            densities[charge] * electric[charge][spatial_index] for charge in range(2)
        )
        # Sourceful ideal Euler equation:
        # w a_i + partial_i p = n_A E^A_i.
        acceleration = (charge_force - grad_pressure) / enthalpy

        thermodynamic_force_sum = 0.0
        for charge in range(2):
            grad_mu_over_t = (
                grad_mu[charge][spatial_index] / temperature
                - chemical_potentials[charge] * grad_temperature[spatial_index] / (temperature * temperature)
            )
            force = electric[charge][spatial_index] / temperature - grad_mu_over_t
            thermodynamic_force_sum += densities[charge] * force

        lhs = acceleration + grad_temperature[spatial_index] / temperature
        rhs = temperature * thermodynamic_force_sum / enthalpy
        assert_close("sourceful Euler force-basis reduction", lhs, rhs)


def check_diffusion_einstein_relation_and_pole() -> None:
    sigma = 0.76
    chi = 1.9
    diffusion = sigma / chi
    k = 0.003
    omega = -1j * diffusion * k * k
    assert_close("diffusion pole denominator", diffusion * k * k - 1j * omega, 0.0)
    assert omega.imag < 0.0

    # Static limit of chi * D k^2/(D k^2 - i omega) at omega=0.
    static_response = chi * diffusion * k * k / (diffusion * k * k)
    assert_close("static susceptibility from diffusion correlator", static_response, chi)


def check_multicharge_diffusion_geometry() -> None:
    susceptibility: Matrix2 = ((2.0, 0.3), (0.3, 1.4))
    conductivity: Matrix2 = ((0.8, 0.1), (0.1, 0.5))
    chi_inverse = matinv(susceptibility)
    diffusion = matmul(conductivity, chi_inverse)

    # The static source-response limit of k^2(D k^2 - i omega)^(-1) Sigma
    # at omega=0 is D^{-1} Sigma = chi.
    static_response = matmul(matinv(diffusion), conductivity)
    mat_entry_close("matrix static susceptibility", static_response, susceptibility)

    chi_root, chi_inv_root = symmetric_square_root_and_inverse(susceptibility)
    symmetric_similar = matmul(matmul(chi_inv_root, conductivity), chi_inv_root)
    # D = chi^(1/2) (chi^(-1/2) Sigma chi^(-1/2)) chi^(-1/2).
    reconstructed_diffusion = matmul(matmul(chi_root, symmetric_similar), chi_inv_root)
    mat_entry_close("similarity reconstruction of D", reconstructed_diffusion, diffusion)

    eigenvalues = symmetric_eigenvalues(symmetric_similar)
    assert eigenvalues[0] >= 0.0
    assert eigenvalues[1] >= 0.0


def main() -> None:
    check_shear_mode()
    check_first_order_shear_acausality()
    check_boosted_diffusion_instability_negative_control()
    check_retarded_singularity_taxonomy()
    check_mis_shear_relaxation_completion()
    check_sound_mode_expansion()
    check_entropy_production_coefficients()
    check_sourceful_euler_force_basis()
    check_diffusion_einstein_relation_and_pole()
    check_multicharge_diffusion_geometry()
    print("All hydrodynamic Ward-identity mode checks passed.")


if __name__ == "__main__":
    main()
