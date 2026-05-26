#!/usr/bin/env python3
"""Finite algebra checks for Volume X hydrodynamic Ward-identity modes."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


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
    check_sound_mode_expansion()
    check_entropy_production_coefficients()
    check_diffusion_einstein_relation_and_pole()
    check_multicharge_diffusion_geometry()
    print("All hydrodynamic Ward-identity mode checks passed.")


if __name__ == "__main__":
    main()
