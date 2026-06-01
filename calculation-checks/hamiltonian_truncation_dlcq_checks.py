#!/usr/bin/env python3
"""Finite checks for Hamiltonian truncation and DLCQ benchmark algebra."""

from __future__ import annotations

import pathlib
import sys
from fractions import Fraction

import numpy as np


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "qft_scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import tcsa_ising_energy_benchmark as tcsa  # noqa: E402
import phi4_dlcq  # noqa: E402
import phi4_hamiltonian_truncation as phi4_truncation  # noqa: E402
import tffsa_ising_spin_connected as tffsa  # noqa: E402
import tffsa_ising_spectral_flow as tffsa_flow  # noqa: E402
import thooft_dlcq  # noqa: E402
import thooft_dlcq_extrapolation as thooft_extrapolation  # noqa: E402


def assert_close(name: str, actual: float, expected: float, tol: float = 1.0e-11) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_leq(name: str, actual: float, bound: float, tol: float = 1.0e-12) -> None:
    if actual > bound + tol:
        raise AssertionError(f"{name}: got {actual!r}, bound {bound!r}")


def assert_matrix_close(name: str, actual: np.ndarray, expected: np.ndarray, tol: float = 1.0e-11) -> None:
    if float(np.max(np.abs(actual - expected))) > tol:
        raise AssertionError(f"{name}: max error {float(np.max(np.abs(actual - expected))):.3e}")


def krylov_orthonormal_basis(matrix: np.ndarray, seed: np.ndarray, dim: int) -> np.ndarray:
    basis: list[np.ndarray] = []
    vector = seed.astype(float) / np.linalg.norm(seed)
    for power in range(dim):
        if power == 0:
            candidate = vector.copy()
        else:
            candidate = matrix @ basis[-1]
        for old in basis:
            candidate = candidate - old * float(old @ candidate)
        norm = float(np.linalg.norm(candidate))
        if norm < 1.0e-13:
            raise AssertionError("Krylov basis broke down before requested dimension")
        basis.append(candidate / norm)
    return np.column_stack(basis)


def check_ising_bogoliubov_benchmark() -> None:
    result = tcsa.run(num_modes=7, mass=0.8, circumference=9.0)
    assert_leq("Ising Bogoliubov finite spectrum", result["max_abs_error"], 1.0e-12)


def check_phi4_hamiltonian_truncation_matrix() -> None:
    cfg = phi4_truncation.RunConfig(
        nmax=1,
        max_particles=3,
        energy_cutoff=5.0,
        mass=1.0,
        circumference=6.0,
        quartic_coupling=0.25,
        total_momentum=0,
    )
    basis, free, hamiltonian = phi4_truncation.hamiltonian_matrix(cfg)
    if not basis:
        raise AssertionError("phi^4 truncation basis unexpectedly empty")
    labels = phi4_truncation.mode_labels(cfg.nmax)
    omega = phi4_truncation.frequencies(labels, cfg.mass, cfg.circumference)
    for state in basis:
        assert_equal("phi^4 total momentum sector", phi4_truncation.total_momentum_units(state, labels), 0)
        if phi4_truncation.free_energy(state, labels, omega) > cfg.energy_cutoff + 1.0e-12:
            raise AssertionError("phi^4 basis state exceeds the free-energy cutoff")
    assert_leq("phi^4 finite Hamiltonian Hermiticity", float(np.max(np.abs(hamiltonian - hamiltonian.T))), 1.0e-12)

    free_cfg = phi4_truncation.RunConfig(
        nmax=cfg.nmax,
        max_particles=cfg.max_particles,
        energy_cutoff=cfg.energy_cutoff,
        mass=cfg.mass,
        circumference=cfg.circumference,
        quartic_coupling=0.0,
        total_momentum=cfg.total_momentum,
    )
    _, free_matrix, zero_coupling_hamiltonian = phi4_truncation.hamiltonian_matrix(free_cfg)
    assert_matrix_close("phi^4 zero-coupling Hamiltonian", zero_coupling_hamiltonian, free_matrix)

    zero_mode_cfg = phi4_truncation.RunConfig(
        nmax=0,
        max_particles=2,
        energy_cutoff=10.0,
        mass=2.0,
        circumference=5.0,
        quartic_coupling=0.0,
        total_momentum=0,
    )
    zero_basis = phi4_truncation.generate_basis(zero_mode_cfg)
    interaction = phi4_truncation.interaction_matrix(zero_mode_cfg, zero_basis)
    lookup = {state: idx for idx, state in enumerate(zero_basis)}
    assert_close("phi^4 normal-ordered vacuum diagonal", interaction[lookup[(0,)], lookup[(0,)]], 0.0)
    expected_two_particle_diagonal = 3.0 / (zero_mode_cfg.circumference * zero_mode_cfg.mass**2)
    assert_close(
        "phi^4 zero-mode two-particle diagonal",
        interaction[lookup[(2,)], lookup[(2,)]],
        expected_two_particle_diagonal,
    )


def check_phi4_dlcq_matrix() -> None:
    cfg = phi4_dlcq.RunConfig(K=5, mass=1.0, quartic_coupling=0.03)
    basis, free, matrix = phi4_dlcq.invariant_mass_matrix(cfg)
    if not basis:
        raise AssertionError("DLCQ phi^4 basis unexpectedly empty")
    for state in basis:
        assert_equal("DLCQ phi^4 total resolution", phi4_dlcq.total_resolution(state), cfg.K)
    assert_leq("DLCQ phi^4 finite matrix Hermiticity", float(np.max(np.abs(matrix - matrix.T))), 1.0e-12)

    zero_cfg = phi4_dlcq.RunConfig(K=cfg.K, mass=cfg.mass, quartic_coupling=0.0)
    _, zero_free, zero_matrix = phi4_dlcq.invariant_mass_matrix(zero_cfg)
    assert_matrix_close("DLCQ phi^4 zero-coupling invariant mass", zero_matrix, zero_free)

    small_cfg = phi4_dlcq.RunConfig(K=3, mass=1.0, quartic_coupling=0.0)
    small_basis = phi4_dlcq.generate_basis(3)
    quartic = phi4_dlcq.quartic_matrix(small_cfg, small_basis)
    lookup = {state: idx for idx, state in enumerate(small_basis)}
    assert_close(
        "DLCQ phi^4 one-to-three matrix element",
        quartic[lookup[(0, 0, 1)], lookup[(3, 0, 0)]],
        4.0 * np.sqrt(2.0),
    )
    assert_close(
        "DLCQ phi^4 three-particle diagonal",
        quartic[lookup[(3, 0, 0)], lookup[(3, 0, 0)]],
        36.0,
    )


def check_tffsa_connected_spin_block() -> None:
    cfg = tffsa.RunConfig(
        num_pairs=4,
        mass=1.0,
        circumference=7.0,
        magnetic_coupling=0.02,
        sigma_bar=1.3,
    )
    states = tffsa.pair_states(cfg.num_pairs, cfg.mass, cfg.circumference)
    matrix = tffsa.finite_matrix(cfg)
    hermiticity_error = float(np.max(np.abs(matrix - matrix.conjugate().T)))
    assert_leq("TFFSA finite block Hermiticity", hermiticity_error, 1.0e-12)

    theta = states[0].theta
    density = states[0].density
    expected_vacuum_pair = (
        cfg.magnetic_coupling
        * cfg.circumference
        * 1j
        * cfg.sigma_bar
        * np.tanh(theta)
        / np.sqrt(density)
    )
    assert_close("TFFSA vacuum-pair form factor", matrix[0, 1], expected_vacuum_pair)

    theta_1 = states[0].theta
    theta_2 = states[1].theta
    crossed = [complex(theta_1, np.pi), complex(-theta_1, np.pi), theta_2, -theta_2]
    expected_pair_pair = (
        cfg.magnetic_coupling
        * cfg.circumference
        * tffsa.spin_even_form_factor(crossed, cfg.sigma_bar)
        / np.sqrt(states[0].density * states[1].density)
    )
    assert_close("TFFSA pair-pair crossed form factor", matrix[1, 2], expected_pair_pair)

    free_cfg = tffsa.RunConfig(
        num_pairs=cfg.num_pairs,
        mass=cfg.mass,
        circumference=cfg.circumference,
        magnetic_coupling=0.0,
        sigma_bar=cfg.sigma_bar,
    )
    free_eigs = np.linalg.eigvalsh(tffsa.finite_matrix(free_cfg))
    expected_free = np.array([0.0] + [state.energy for state in states])
    if np.max(np.abs(free_eigs - expected_free)) > 1.0e-12:
        raise AssertionError("TFFSA zero-coupling spectrum does not match free energies")


def check_tffsa_spectral_flow_derivatives() -> None:
    base = tffsa.RunConfig(
        num_pairs=4,
        mass=1.0,
        circumference=7.0,
        magnetic_coupling=0.0,
        sigma_bar=1.0,
    )
    derivative = tffsa_flow.perturbation_matrix(base)
    matrix_plus = tffsa.finite_matrix(tffsa_flow.config_with_h(base, 0.125))
    matrix_minus = tffsa.finite_matrix(tffsa_flow.config_with_h(base, -0.125))
    centered_matrix_derivative = (matrix_plus - matrix_minus) / 0.25
    assert_leq(
        "TFFSA exact affine matrix derivative",
        float(np.max(np.abs(centered_matrix_derivative - derivative))),
        1.0e-12,
    )

    values, slopes, trace_error = tffsa_flow.hellmann_feynman_slopes(base, 0.015)
    assert_leq("TFFSA slope trace identity", trace_error, 1.0e-10)
    if tffsa_flow.minimum_neighbor_gap(values) <= 0.0:
        raise AssertionError("TFFSA spectral-flow check needs a simple finite spectrum")
    finite_difference = tffsa_flow.centered_difference_slopes(base, 0.015, 1.0e-5)
    assert_leq(
        "TFFSA Hellmann-Feynman finite-difference comparison",
        float(np.max(np.abs(finite_difference - slopes))),
        1.0e-6,
    )

    result = tffsa_flow.run(
        base=base,
        h_values=[-0.02, -0.01, 0.0, 0.01, 0.02],
        slope_at=0.015,
        delta=1.0e-5,
    )
    assert_leq("TFFSA spectral-flow derivative Hermiticity", result["derivative_hermiticity_error"], 1.0e-12)
    assert_leq("TFFSA spectral-flow maximum slope error", result["max_abs_slope_error"], 1.0e-6)


def check_thooft_quadratic_form_identity() -> None:
    K = 10
    m1 = 0.3
    m2 = 0.4
    gamma = 0.7
    matrix = thooft_dlcq.thooft_matrix(K, m1, m2, gamma)
    v = np.array([(-1.0) ** n * (n + 1.0) / 7.0 for n in range(K - 1)])
    left = float(v @ matrix @ v)
    xs = np.arange(1, K, dtype=float) / float(K)
    mass_part = float(np.sum((m1 * m1 / xs + m2 * m2 / (1.0 - xs)) * v * v))
    kernel_part = 0.0
    for n in range(K - 1):
        for m in range(n + 1, K - 1):
            kernel_part += gamma * K * (v[n] - v[m]) ** 2 / float((n - m) ** 2)
    assert_close("DLCQ quadratic-form identity", left, mass_part + kernel_part)
    if float(np.linalg.eigvalsh(matrix)[0]) <= 0.0:
        raise AssertionError("finite 't Hooft matrix should be positive definite")


def check_thooft_large_K_fit_algebra() -> None:
    Ks = thooft_extrapolation.parse_Ks("8, 10 12,16")
    if Ks != [8, 10, 12, 16]:
        raise AssertionError("DLCQ K parser changed its ordering convention")

    exact_values = [2.5 - 1.25 / K + 0.75 / (K * K) for K in Ks]
    exact_fit = thooft_extrapolation.fit_cutoff_sequence(
        Ks=Ks,
        values=exact_values,
        fit_order=2,
        base_exponent=1.0,
    )
    assert_close("DLCQ exact polynomial intercept", exact_fit["A_infinity"], 2.5)
    assert_leq("DLCQ exact polynomial residual", exact_fit["max_residual"], 1.0e-13)

    constant_fit = thooft_extrapolation.fit_cutoff_sequence(
        Ks=Ks,
        values=[3.0 for _ in Ks],
        fit_order=2,
        base_exponent=1.0,
    )
    assert_close("DLCQ constant intercept", constant_fit["A_infinity"], 3.0)
    assert_leq("DLCQ constant residual", constant_fit["max_residual"], 1.0e-13)

    script_result = thooft_extrapolation.run(
        Ks=[8, 10, 12],
        levels=2,
        m1=0.15,
        m2=0.15,
        gamma=0.5,
        fit_order=1,
        base_exponent=1.0,
    )
    if not script_result["positive_finite_spectra"]:
        raise AssertionError("finite large-K DLCQ diagnostic found a negative spectrum")
    for level_fit in script_result["extrapolated_levels"]:
        if not np.isfinite(level_fit["A_infinity"]):
            raise AssertionError("finite large-K DLCQ diagnostic produced a non-finite fit")


def check_residual_certificate() -> None:
    eigenvalues = np.array([1.0, 3.0, 8.0])
    matrix = np.diag(eigenvalues)
    epsilon = 0.08
    vector = np.array([(1.0 - epsilon * epsilon) ** 0.5, epsilon, 0.0])
    vector /= np.linalg.norm(vector)
    lam = float(vector @ matrix @ vector)
    residual = float(np.linalg.norm((matrix - lam * np.eye(3)) @ vector))
    distance_to_spectrum = float(np.min(np.abs(eigenvalues - lam)))
    assert_leq("residual distance to spectrum", distance_to_spectrum, residual)

    complement_gap = float(np.min(np.abs(eigenvalues[1:] - lam)))
    leakage = float(np.linalg.norm(vector[1:]))
    assert_leq("projector leakage bound", leakage, residual / complement_gap)


def check_feshbach_determinant_identity() -> None:
    matrix = np.array(
        [
            [2.0, 0.3, 0.1],
            [0.3, 4.0, -0.2],
            [0.1, -0.2, 7.0],
        ],
        dtype=float,
    )
    energy = 1.7
    p_block = matrix[:2, :2]
    q_block = matrix[2:, 2:]
    p_to_q = matrix[:2, 2:]
    q_to_p = matrix[2:, :2]
    schur = p_block - p_to_q @ np.linalg.inv(q_block - energy * np.eye(1)) @ q_to_p
    full_det = float(np.linalg.det(matrix - energy * np.eye(3)))
    factored_det = float(
        np.linalg.det(q_block - energy * np.eye(1))
        * np.linalg.det(schur - energy * np.eye(2))
    )
    assert_close("Feshbach determinant identity", full_det, factored_det)


def check_krylov_residual_and_moments() -> None:
    matrix = np.array(
        [
            [1.5, 0.4, 0.0, 0.0, 0.0],
            [0.4, 2.2, -0.3, 0.0, 0.0],
            [0.0, -0.3, 3.1, 0.5, 0.0],
            [0.0, 0.0, 0.5, 4.0, -0.2],
            [0.0, 0.0, 0.0, -0.2, 5.3],
        ],
        dtype=float,
    )
    seed = np.array([1.0, 0.2, -0.1, 0.05, 0.3], dtype=float)
    seed = seed / np.linalg.norm(seed)
    dim = 3
    basis = krylov_orthonormal_basis(matrix, seed, dim)
    compression = basis.T @ matrix @ basis
    residual_matrix = matrix @ basis - basis @ compression

    # The exact Arnoldi/Lanczos residual has support only in the final column.
    assert_leq("Krylov residual first column", float(np.linalg.norm(residual_matrix[:, 0])), 1.0e-11)
    assert_leq("Krylov residual second column", float(np.linalg.norm(residual_matrix[:, 1])), 1.0e-11)
    beta_tail = float(np.linalg.norm(residual_matrix[:, -1]))

    ritz_values, ritz_vectors = np.linalg.eigh(compression)
    for idx, theta in enumerate(ritz_values):
        y = ritz_vectors[:, idx]
        lifted = basis @ y
        full_residual = float(np.linalg.norm((matrix - theta * np.eye(matrix.shape[0])) @ lifted))
        assert_close(
            f"Krylov Ritz residual formula {idx}",
            full_residual,
            beta_tail * abs(float(y[-1])),
            tol=1.0e-11,
        )

    e1 = np.zeros(dim)
    e1[0] = 1.0
    weights = ritz_vectors[0, :] ** 2
    for power in range(2 * dim):
        exact_moment = float(seed @ np.linalg.matrix_power(matrix, power) @ seed)
        compressed_moment = float(e1 @ np.linalg.matrix_power(compression, power) @ e1)
        quadrature_moment = float(np.sum(weights * (ritz_values ** power)))
        assert_close(f"Krylov compressed moment {power}", compressed_moment, exact_moment, tol=1.0e-10)
        assert_close(f"Krylov quadrature moment {power}", quadrature_moment, exact_moment, tol=1.0e-10)


def check_variational_energy_certificates() -> None:
    matrix = np.array(
        [
            [0.8, 0.25, -0.10, 0.05],
            [0.25, 1.7, 0.30, -0.15],
            [-0.10, 0.30, 2.6, 0.20],
            [0.05, -0.15, 0.20, 4.2],
        ],
        dtype=float,
    )
    vector = np.array([1.0, 0.35, -0.4, 0.2], dtype=float)
    vector = vector / np.linalg.norm(vector)
    energy = float(vector @ matrix @ vector)
    residual = (matrix - energy * np.eye(matrix.shape[0])) @ vector
    variance = float(vector @ matrix @ matrix @ vector - energy * energy)
    assert_close("variational variance equals residual norm", variance, float(residual @ residual), tol=1.0e-12)

    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    distance = float(np.min(np.abs(eigenvalues - energy)))
    assert_leq("variational variance spectral distance", distance, float(np.sqrt(variance)))

    ground_coefficients = eigenvectors.T @ vector
    excited_weight = float(np.sum(np.abs(ground_coefficients[1:]) ** 2))
    ground_bound = (energy - float(eigenvalues[0])) / float(eigenvalues[1] - eigenvalues[0])
    assert_leq("variational ground projector leakage", excited_weight, ground_bound)

    tangent = np.array([0.2, -0.7, 0.1, 0.4], dtype=float)
    tangent = tangent - vector * float(vector @ tangent)
    tangent = tangent / np.linalg.norm(tangent)
    gradient_formula = 2.0 * float(tangent @ residual)

    def normalized_energy(t: float) -> float:
        trial = vector + t * tangent
        trial = trial / np.linalg.norm(trial)
        return float(trial @ matrix @ trial)

    step = 1.0e-6
    finite_difference = (normalized_energy(step) - normalized_energy(-step)) / (2.0 * step)
    assert_close("variational tangent-gradient formula", finite_difference, gradient_formula, tol=1.0e-8)

    nonzero_vector = vector + np.array([0.1, 0.2, 0.15, 0.05], dtype=float)
    norm2 = float(nonzero_vector @ nonzero_vector)
    local_energy = (matrix @ nonzero_vector) / nonzero_vector
    probabilities = (nonzero_vector * nonzero_vector) / norm2
    rayleigh = float(nonzero_vector @ matrix @ nonzero_vector / norm2)
    local_mean = float(np.sum(probabilities * local_energy))
    local_variance = float(np.sum(probabilities * np.abs(local_energy - rayleigh) ** 2))
    residual_variance = float(np.linalg.norm((matrix - rayleigh * np.eye(matrix.shape[0])) @ nonzero_vector) ** 2 / norm2)
    assert_close("variational local-energy mean", local_mean, rayleigh)
    assert_close("variational local-energy variance", local_variance, residual_variance)


def check_light_front_kinematic_identities() -> None:
    p_plus = Fraction(7, 5)
    p_perp = [Fraction(3, 4), Fraction(-2, 5)]
    p_perp_sq = sum(component * component for component in p_perp)
    mass_sq = Fraction(9, 10)
    p_minus = (mass_sq + p_perp_sq) / (2 * p_plus)

    mass_shell = -2 * p_plus * p_minus + p_perp_sq
    assert_equal("light-front mass shell", mass_shell, -mass_sq)
    delta_jacobian = abs(-2 * p_plus)
    assert_equal("light-front delta-function Jacobian", delta_jacobian, Fraction(14, 5))
    assert_equal("light-front one-particle measure weight", Fraction(1, delta_jacobian), Fraction(5, 14))

    q_plus = Fraction(11, 6)
    q_minus = Fraction(13, 8)
    q_perp = [Fraction(-1, 3), Fraction(5, 7)]
    dot_pq = -p_plus * q_minus - p_minus * q_plus + sum(p_i * q_i for p_i, q_i in zip(p_perp, q_perp))
    dot_qp = -q_plus * p_minus - q_minus * p_plus + sum(q_i * p_i for p_i, q_i in zip(q_perp, p_perp))
    assert_equal("light-front bilinear symmetry", dot_pq, dot_qp)

    sector_p_plus = Fraction(5, 3)
    sector_p_perp_sq = Fraction(7, 4)
    p_minus_eigenvalues = [Fraction(3, 5), Fraction(11, 10), Fraction(17, 8)]
    mass_eigenvalues = [2 * sector_p_plus * eigenvalue - sector_p_perp_sq for eigenvalue in p_minus_eigenvalues]
    expected = [Fraction(1, 4), Fraction(23, 12), Fraction(16, 3)]
    assert_equal("fixed-sector invariant-mass spectrum", mass_eigenvalues, expected)


def main() -> None:
    check_ising_bogoliubov_benchmark()
    check_phi4_hamiltonian_truncation_matrix()
    check_phi4_dlcq_matrix()
    check_tffsa_connected_spin_block()
    check_tffsa_spectral_flow_derivatives()
    check_thooft_quadratic_form_identity()
    check_thooft_large_K_fit_algebra()
    check_residual_certificate()
    check_feshbach_determinant_identity()
    check_krylov_residual_and_moments()
    check_variational_energy_certificates()
    check_light_front_kinematic_identities()
    print("All Hamiltonian-truncation and DLCQ checks passed.")


if __name__ == "__main__":
    main()
