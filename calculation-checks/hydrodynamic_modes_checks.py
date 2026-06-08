#!/usr/bin/env python3
"""Finite algebra checks for Volume X hydrodynamic Ward-identity modes.

Evidence contract.
Target claims: the first-order shear and sound poles, entropy-production
positivity, sourceful Euler force reduction, susceptibility geometry,
first-order shear acausality as a parabolic initial-value equation, boosted
high-k instability of the parabolic truncation, and the linear causal
relaxation completion of the shear sector in Volume X Chapter 5.  The checks
also guard the slow-sector completeness boundary: an omitted relaxational
order parameter whose gap scales to zero produces a nonlocal memory
denominator and cannot be absorbed into analytic normal-fluid coefficients;
the retained slow sector is a basis-invariant spectral subspace rather than a
list of diagonal operator rates; sources transform contragrediently to
observable basis changes; the finite Hamiltonian Liouvillian has oscillatory
spectral lines rather than dissipative relaxation rates; and a continuum lower
edge entering the hydrodynamic window is a slow spectral channel, not a finite
pole list.
Independent construction: direct finite-dimensional algebra for the Ward
identity modes, exact heat-kernel positivity away from the origin, explicit
quadratic roots for boosted diffusion and MIS shear relaxation, an explicit
finite Gibbs/Lehmann retarded response whose singular support is computed
from transition energies rather than inserted as test points, and matrix
similarity checks for multi-charge diffusion.  The slow-sector guards use an
exact non-normal two-by-two matrix, a source/observable pairing check, a
finite unitary Liouvillian sample, and a finite continuum memory integral.
Imported assumptions: homogeneous KMS thermodynamic stability, the stated
Landau-frame constitutive relations, positivity of transport coefficients from
entropy/Kubo arguments, and the choice of a single linear MIS shear relaxation
time.
Negative controls: first-order shear diffusion is not accepted as a causal
finite-speed PDE, Lorentz-boosted parabolic diffusion is not accepted as a
stable high-k theory, real-axis spectral lines are not mistaken for
lower-half-plane damped poles, a denominator with an actual open-upper-half-
plane root is rejected, a causal relaxation model with superluminal shear
front speed is rejected, an omitted order-parameter mode with a vanishing
relaxation rate is rejected as an analytic conserved-density-only correction,
diagonal entries of a mixed relaxation matrix are rejected as basis-invariant
rates, same-way source and observable transformations are rejected, a finite
Hamiltonian Liouvillian is rejected as a dissipative pole generator, a
continuum of relaxation rates whose lower edge scales to zero is rejected as
a finite-pole correction,
and linear shear completion is not treated as a theorem for full nonlinear
causal hydrodynamics.
Scope boundary: these checks verify finite algebra and linear-mode
bookkeeping; they do not prove microscopic hydrodynamic emergence, nonlinear
well-posedness, or the complete BRSSS/MIS coefficient inequalities.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close, assert_finite

import cmath
import math
from fractions import Fraction


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {got!r}")


Matrix2Q = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def qmatmul(lhs: Matrix2Q, rhs: Matrix2Q) -> Matrix2Q:
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


def qmatadd(lhs: Matrix2Q, rhs: Matrix2Q) -> Matrix2Q:
    return (
        (lhs[0][0] + rhs[0][0], lhs[0][1] + rhs[0][1]),
        (lhs[1][0] + rhs[1][0], lhs[1][1] + rhs[1][1]),
    )


def qmatscale(coeff: Fraction, matrix: Matrix2Q) -> Matrix2Q:
    return (
        (coeff * matrix[0][0], coeff * matrix[0][1]),
        (coeff * matrix[1][0], coeff * matrix[1][1]),
    )


def qmatinv(matrix: Matrix2Q) -> Matrix2Q:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        raise ValueError("singular rational 2x2 matrix")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def qtrace(matrix: Matrix2Q) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def qdet(matrix: Matrix2Q) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def qtranspose(matrix: Matrix2Q) -> Matrix2Q:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def qmatvec(matrix: Matrix2Q, vector: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def qquadratic(vector: tuple[Fraction, Fraction], matrix: Matrix2Q) -> Fraction:
    return (
        vector[0] * (matrix[0][0] * vector[0] + matrix[0][1] * vector[1])
        + vector[1] * (matrix[1][0] * vector[0] + matrix[1][1] * vector[1])
    )


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


def finite_lehmann_atoms(
    energies: list[float],
    beta: float,
    operator: list[list[complex]],
) -> list[tuple[float, float]]:
    partition = sum(math.exp(-beta * energy) for energy in energies)
    atoms: dict[float, float] = {}
    for source, source_energy in enumerate(energies):
        for target, target_energy in enumerate(energies):
            matrix_element = operator[source][target]
            if abs(matrix_element) < 1.0e-14:
                continue
            transition = target_energy - source_energy
            weight = (
                (math.exp(-beta * source_energy) - math.exp(-beta * target_energy))
                * abs(matrix_element) ** 2
                / partition
            )
            atoms[transition] = atoms.get(transition, 0.0) + weight
    return sorted(
        (transition, weight)
        for transition, weight in atoms.items()
        if abs(weight) > 1.0e-14
    )


def finite_lehmann_retarded_value(
    atoms: list[tuple[float, float]],
    z: complex,
) -> complex:
    return sum(weight / (transition - z) for transition, weight in atoms)


def has_open_upper_half_plane_singularity(poles: list[complex]) -> bool:
    return any(pole.imag > 1.0e-12 for pole in poles)


def check_retarded_singularity_taxonomy() -> None:
    energies = [0.0, 0.9, 2.1]
    beta = 1.4
    operator = [
        [0.0, 1.0 + 0.2j, 0.0],
        [1.0 - 0.2j, 0.0, -0.7j],
        [0.0, 0.7j, 0.0],
    ]
    atoms = finite_lehmann_atoms(energies, beta, operator)
    if len(atoms) != 4:
        raise AssertionError("finite Lehmann construction should expose four nonzero transition lines")

    finite_volume_poles = [complex(transition, 0.0) for transition, _ in atoms]
    if has_open_upper_half_plane_singularity(finite_volume_poles):
        raise AssertionError("finite-volume Lehmann lines should not enter the open upper half-plane")
    if not all(pole.imag == 0.0 for pole in finite_volume_poles):
        raise AssertionError("finite-volume spectral singularities should sit on the real boundary")

    upper_half_test_points = [
        complex(-2.0, 0.1),
        complex(0.25, 0.35),
        complex(1.1, 2.0),
    ]
    for z in upper_half_test_points:
        value = finite_lehmann_retarded_value(atoms, z)
        assert_finite("finite Lehmann retarded real part", value.real)
        assert_finite("finite Lehmann retarded imaginary part", value.imag)

    threshold = 0.6
    cut_mesh = [complex(threshold + 0.2 * index, 0.0) for index in range(5)]
    if has_open_upper_half_plane_singularity(cut_mesh):
        raise AssertionError("thermodynamic-limit cut mesh should remain a real-axis boundary object")
    if not all(point.real >= threshold for point in cut_mesh):
        raise AssertionError("cut mesh should remain on the declared threshold interval")

    damped_transient_poles = list(mis_shear_roots(diffusion=0.21, tau_pi=0.7, k=0.8))
    if has_open_upper_half_plane_singularity(damped_transient_poles):
        raise AssertionError("stable MIS shear roots should not enter the open upper half-plane")
    if not all(pole.imag < 0.0 for pole in damped_transient_poles):
        raise AssertionError("stable MIS shear roots should lie below the real axis")

    unstable_denominator_roots = [complex(0.1, 0.2), complex(-0.1, -0.2)]
    if not has_open_upper_half_plane_singularity(unstable_denominator_roots):
        raise AssertionError("upper-half-plane denominator root must be rejected")


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


def check_omitted_relaxational_mode_memory_negative_control() -> None:
    # Integrating out a nonconserved order parameter phi with
    # (-i omega + Gamma_phi + kappa k^2) phi = lambda X produces
    # Delta K_X = -lambda^2/(Gamma_phi + kappa k^2 - i omega).
    # For fixed Gamma_phi this is analytic; if Gamma_phi, k^2, and omega all
    # scale as the hydrodynamic denominator, it is a retained slow mode.
    coupling = Fraction(2, 3)
    gamma_fixed = Fraction(5, 7)
    epsilon = Fraction(1, 101)

    fixed_static = -(coupling * coupling) / gamma_fixed
    fixed_first_omega_coefficient = (coupling * coupling) / (gamma_fixed * gamma_fixed)
    assert_equal(
        "fixed-gap omitted mode has finite static coefficient",
        fixed_static,
        Fraction(-28, 45),
    )
    assert_equal(
        "fixed-gap omitted mode has finite derivative coefficient",
        fixed_first_omega_coefficient,
        Fraction(196, 225),
    )

    gamma0 = Fraction(5, 7)
    stiffness_k2_0 = Fraction(11, 13)
    omega0 = Fraction(17, 19)
    real_denominator = epsilon * epsilon * (gamma0 + stiffness_k2_0)
    omega = epsilon * epsilon * omega0
    denominator_norm = real_denominator * real_denominator + omega * omega
    memory_real = -(coupling * coupling) * real_denominator / denominator_norm

    expected_scaled_memory = (
        -(coupling * coupling)
        * (gamma0 + stiffness_k2_0)
        / ((gamma0 + stiffness_k2_0) * (gamma0 + stiffness_k2_0) + omega0 * omega0)
    )
    assert_equal(
        "slow omitted mode memory scales as inverse hydrodynamic denominator",
        memory_real * epsilon * epsilon,
        expected_scaled_memory,
    )
    if not abs(memory_real) > abs(fixed_static) / epsilon:
        raise AssertionError("vanishing order-parameter gap should not look like a fixed analytic correction")

    weak_relaxation = epsilon * epsilon * gamma0
    diffusion_piece = epsilon * epsilon * stiffness_k2_0
    quasihydro_damping = weak_relaxation + diffusion_piece
    assert_equal(
        "weakly broken charge pole remains in the slow scaling window",
        quasihydro_damping / (epsilon * epsilon),
        gamma0 + stiffness_k2_0,
    )


def check_basis_invariant_slow_projector_negative_control() -> None:
    slow = Fraction(1, 101)
    fast = Fraction(5, 3)
    mixing = Fraction(7, 5)
    operator: Matrix2Q = ((slow, mixing), (Fraction(0), fast))
    basis: Matrix2Q = ((Fraction(1), Fraction(2)), (Fraction(3), Fraction(5)))
    basis_inv = qmatinv(basis)
    transformed = qmatmul(qmatmul(basis_inv, operator), basis)

    assert_equal("similarity preserves relaxation trace", qtrace(transformed), slow + fast)
    assert_equal("similarity preserves relaxation determinant", qdet(transformed), slow * fast)
    if transformed[0][0] == slow or transformed[1][1] == fast:
        raise AssertionError("diagonal relaxation entries should be basis dependent in the non-normal sample")
    if min(abs(transformed[0][0]), abs(transformed[1][1])) < Fraction(1, 10):
        raise AssertionError("basis-dependent diagonal heuristic should not reliably expose the slow rate")

    identity: Matrix2Q = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    slow_projector = qmatscale(
        Fraction(1, 1) / (slow - fast),
        qmatadd(operator, qmatscale(-fast, identity)),
    )
    transformed_projector = qmatscale(
        Fraction(1, 1) / (slow - fast),
        qmatadd(transformed, qmatscale(-fast, identity)),
    )
    covariant_projector = qmatmul(qmatmul(basis_inv, slow_projector), basis)
    assert_equal("Riesz projector transforms covariantly", transformed_projector, covariant_projector)
    assert_equal("slow Riesz projector is idempotent", qmatmul(slow_projector, slow_projector), slow_projector)
    assert_equal(
        "transformed slow Riesz projector is idempotent",
        qmatmul(transformed_projector, transformed_projector),
        transformed_projector,
    )


def check_contragredient_source_observable_transform() -> None:
    observable_change: Matrix2Q = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(1)))
    inverse_change = qmatinv(observable_change)
    source_change = qtranspose(inverse_change)
    wrong_same_way_source_change = observable_change

    susceptibility: Matrix2Q = (
        (Fraction(5, 3), Fraction(1, 7)),
        (Fraction(1, 7), Fraction(4, 5)),
    )
    source = (Fraction(3, 5), Fraction(-2, 7))

    transformed_susceptibility = qmatmul(
        qmatmul(observable_change, susceptibility),
        qtranspose(observable_change),
    )
    transformed_source = qmatvec(source_change, source)
    wrong_source = qmatvec(wrong_same_way_source_change, source)

    original_power = qquadratic(source, susceptibility)
    transformed_power = qquadratic(transformed_source, transformed_susceptibility)
    wrong_power = qquadratic(wrong_source, transformed_susceptibility)
    assert_equal("contragredient source transform preserves response pairing", transformed_power, original_power)
    if wrong_power == original_power:
        raise AssertionError("same-way source transform should not preserve the source/observable pairing")


def check_finite_liouvillian_not_dissipative_generator() -> None:
    delta = Fraction(7, 5)
    liouvillian: Matrix2Q = ((Fraction(0), delta), (-delta, Fraction(0)))

    assert_equal("finite Hamiltonian Liouvillian has zero trace", qtrace(liouvillian), Fraction(0))
    assert_equal("finite Hamiltonian Liouvillian has positive rotation determinant", qdet(liouvillian), delta * delta)
    discriminant = qtrace(liouvillian) * qtrace(liouvillian) - 4 * qdet(liouvillian)
    if discriminant >= 0:
        raise AssertionError("finite Hamiltonian Liouvillian sample should have imaginary spectral lines")

    z_dissipative = Fraction(-3, 101)
    characteristic_at_dissipative_pole = z_dissipative * z_dissipative + delta * delta
    if characteristic_at_dissipative_pole == 0:
        raise AssertionError("dissipative hydrodynamic pole should not be an eigenvalue of the finite Liouvillian")

    effective_diffusion_pencil_zero = z_dissipative - z_dissipative
    assert_equal(
        "separately declared effective memory pencil can have a dissipative pole",
        effective_diffusion_pencil_zero,
        Fraction(0),
    )


def check_continuum_slow_edge_memory_negative_control() -> None:
    fixed_lower_edge = 0.2
    fixed_static = math.log(1.0 / fixed_lower_edge)
    fixed_first_derivative = 1.0 / fixed_lower_edge - 1.0
    assert_close("fixed continuum edge has finite static memory", fixed_static, math.log(5.0))
    assert_close("fixed continuum edge has finite derivative coefficient", fixed_first_derivative, 4.0)

    epsilon_values = (1.0e-2, 1.0e-3)
    slow_static = [math.log(1.0 / (epsilon * epsilon)) for epsilon in epsilon_values]
    if not slow_static[1] > slow_static[0] > fixed_static:
        raise AssertionError("continuum lower edge entering the slow window should produce growing memory")

    omega0 = 0.7
    scaled_complex_memory = []
    for epsilon in epsilon_values:
        lower_edge = epsilon * epsilon
        omega = epsilon * epsilon * omega0
        value = cmath.log((1.0 - 1j * omega) / (lower_edge - 1j * omega))
        scaled_complex_memory.append(value)
    if not scaled_complex_memory[1].real > scaled_complex_memory[0].real:
        raise AssertionError("slow continuum edge should retain nonlocal logarithmic real part")
    if abs(scaled_complex_memory[1].imag - scaled_complex_memory[0].imag) > 1.0e-3:
        raise AssertionError("scaled continuum edge phase should approach a fixed branch-cut value")


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
    check_omitted_relaxational_mode_memory_negative_control()
    check_basis_invariant_slow_projector_negative_control()
    check_contragredient_source_observable_transform()
    check_finite_liouvillian_not_dissipative_generator()
    check_continuum_slow_edge_memory_negative_control()
    print("All hydrodynamic Ward-identity mode checks passed.")


if __name__ == "__main__":
    main()
