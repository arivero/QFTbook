#!/usr/bin/env python3
"""Finite checks for Hamiltonian truncation and DLCQ benchmark algebra."""

from __future__ import annotations

from check_utils import assert_close as _assert_close
from check_utils import assert_array_close as _assert_array_close
from check_utils import assert_gt as _assert_gt
from check_utils import assert_leq as _assert_leq

import pathlib
import sys
import math
from fractions import Fraction
from itertools import product

import numpy as np


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "qft_scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import tcsa_ising_energy_benchmark as tcsa  # noqa: E402
import sine_gordon_zero_mode_truncation as sine_gordon  # noqa: E402
import sine_gordon_tcsa_vertex as sine_gordon_tcsa  # noqa: E402
import phi4_dlcq  # noqa: E402
import phi4_hamiltonian_truncation as phi4_truncation  # noqa: E402
import e8_ising_mass_ratios as e8_ratios  # noqa: E402
import tffsa_ising_spin_connected as tffsa  # noqa: E402
import tffsa_ising_spectral_flow as tffsa_flow  # noqa: E402
import thooft_dlcq  # noqa: E402
import thooft_dlcq_extrapolation as thooft_extrapolation  # noqa: E402
import benchmark_manifest_consistency as benchmark_manifest  # noqa: E402


def assert_close(name: str, actual: float, expected: float, tol: float = 1.0e-11) -> None:
    _assert_close(name, actual, expected, tol=tol)


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_leq(name: str, actual: float, bound: float, tol: float = 1.0e-12) -> None:
    _assert_leq(name, actual, bound, tol=tol)


def assert_matrix_close(name: str, actual: np.ndarray, expected: np.ndarray, tol: float = 1.0e-11) -> None:
    _assert_array_close(name, actual, expected, tol=tol)


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


def check_sine_gordon_zero_mode_selection_rules() -> None:
    cfg = sine_gordon.RunConfig(nmax=4, kappa=Fraction(3, 5), coupling=Fraction(7, 50))
    labels, free, hamiltonian = sine_gordon.hamiltonian_matrix(cfg)
    lookup = {label: idx for idx, label in enumerate(labels)}
    cosine = sine_gordon.cosine_matrix(cfg.nmax)

    assert_close("sine-Gordon <1|cos theta|0>", cosine[lookup[1], lookup[0]], 0.5)
    assert_close("sine-Gordon <-1|cos theta|0>", cosine[lookup[-1], lookup[0]], 0.5)
    assert_close("sine-Gordon <2|cos theta|0>", cosine[lookup[2], lookup[0]], 0.0)
    assert_close("sine-Gordon diagonal cosine", cosine[lookup[0], lookup[0]], 0.0)
    assert_leq(
        "sine-Gordon finite zero-mode Hermiticity",
        float(np.max(np.abs(hamiltonian - hamiltonian.T))),
        1.0e-12,
    )
    free_cfg = sine_gordon.RunConfig(nmax=cfg.nmax, kappa=cfg.kappa, coupling=0.0)
    _, free_matrix, zero_coupling = sine_gordon.hamiltonian_matrix(free_cfg)
    assert_matrix_close("sine-Gordon zero-coupling finite matrix", zero_coupling, free_matrix)

    ground = lookup[0]
    second_order = 0.0
    for idx, label in enumerate(labels):
        if idx == ground:
            continue
        second_order += hamiltonian[idx, ground] ** 2 / (free[ground, ground] - free[idx, idx])
    assert_close(
        "sine-Gordon zero-mode second-order shift",
        second_order,
        sine_gordon.second_order_ground_shift(float(cfg.kappa), float(cfg.coupling)),
    )


def check_sine_gordon_tcsa_vertex_assembly() -> None:
    cfg = sine_gordon_tcsa.RunConfig(
        momentum_max=1,
        winding_max=0,
        mode_max=1,
        level_cutoff=2,
        radius=1.0,
        alpha=0.4,
        coupling=0.2,
        spin_zero_only=False,
    )
    basis = sine_gordon_tcsa.generate_basis(cfg)
    lookup = {state: idx for idx, state in enumerate(basis)}
    vacuum = sine_gordon_tcsa.State(momentum=0, winding=0, left=(0,), right=(0,))
    shifted_vacuum = sine_gordon_tcsa.State(momentum=1, winding=0, left=(0,), right=(0,))
    left_oscillator = sine_gordon_tcsa.State(momentum=1, winding=0, left=(1,), right=(0,))
    left_right_oscillator = sine_gordon_tcsa.State(momentum=1, winding=0, left=(1,), right=(1,))

    local_vertex = sine_gordon_tcsa.cosine_vertex_matrix(cfg, basis, integrated=False)
    integrated_vertex = sine_gordon_tcsa.cosine_vertex_matrix(cfg, basis, integrated=True)

    assert_close(
        "sine-Gordon TCSA oscillator-vacuum vertex",
        integrated_vertex[lookup[shifted_vacuum], lookup[vacuum]],
        0.5,
    )
    assert_close(
        "sine-Gordon TCSA local one-oscillator vertex",
        local_vertex[lookup[left_oscillator], lookup[vacuum]],
        0.5 * cfg.alpha,
    )
    assert_close(
        "sine-Gordon TCSA integrated spin projection",
        integrated_vertex[lookup[left_oscillator], lookup[vacuum]],
        0.0,
    )
    assert_close(
        "sine-Gordon TCSA integrated two-oscillator vertex",
        integrated_vertex[lookup[left_right_oscillator], lookup[vacuum]],
        0.5 * cfg.alpha * cfg.alpha,
    )

    winding_cfg = sine_gordon_tcsa.RunConfig(
        momentum_max=1,
        winding_max=1,
        mode_max=0,
        level_cutoff=0,
        radius=1.0,
        alpha=0.4,
        coupling=0.2,
        spin_zero_only=False,
    )
    winding_basis, free, hamiltonian = sine_gordon_tcsa.hamiltonian_matrix(winding_cfg)
    vertex = sine_gordon_tcsa.cosine_vertex_matrix(winding_cfg, winding_basis, integrated=True)
    for i, bra in enumerate(winding_basis):
        for j, ket in enumerate(winding_basis):
            if bra.winding != ket.winding:
                assert_close("sine-Gordon TCSA winding conservation", vertex[i, j], 0.0)
    assert_leq(
        "sine-Gordon TCSA finite Hermiticity",
        float(np.max(np.abs(hamiltonian - hamiltonian.T))),
        1.0e-12,
    )
    zero_cfg = sine_gordon_tcsa.RunConfig(
        momentum_max=1,
        winding_max=0,
        mode_max=1,
        level_cutoff=2,
        radius=1.0,
        alpha=0.4,
        coupling=0.0,
        spin_zero_only=True,
    )
    _, free_zero, hamiltonian_zero = sine_gordon_tcsa.hamiltonian_matrix(zero_cfg)
    assert_matrix_close("sine-Gordon TCSA zero-coupling Hamiltonian", hamiltonian_zero, free_zero)


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


def check_tffsa_ns_r_spin_block() -> None:
    cfg = tffsa.RunConfig(
        num_pairs=4,
        mass=1.0,
        circumference=7.0,
        magnetic_coupling=0.02,
        sigma_bar=1.3,
        mass_sign=1,
    )
    states = tffsa.sector_basis(cfg.num_pairs, cfg.mass, cfg.circumference, cfg.mass_sign)
    matrix = tffsa.finite_matrix(cfg)
    hermiticity_error = float(np.max(np.abs(matrix - matrix.conjugate().T)))
    assert_leq("TFFSA finite block Hermiticity", hermiticity_error, 1.0e-12)

    h_zero = tffsa.finite_matrix(tffsa.RunConfig(
        num_pairs=cfg.num_pairs,
        mass=cfg.mass,
        circumference=cfg.circumference,
        magnetic_coupling=0.0,
        sigma_bar=cfg.sigma_bar,
        mass_sign=cfg.mass_sign,
    ))
    perturbation = matrix - h_zero
    same_sector_entries = [
        perturbation[i, j]
        for i, bra in enumerate(states)
        for j, ket in enumerate(states)
        if bra.sector == ket.sector
    ]
    assert_leq(
        "TFFSA spin perturbation has no same-sector entries",
        float(np.max(np.abs(same_sector_entries))),
        1.0e-12,
    )

    ns_vac_index = next(i for i, state in enumerate(states) if state.label == "NS:vac")
    r_zero_index = next(i for i, state in enumerate(states) if state.label == "R:zero")
    r_zero = states[r_zero_index]
    expected_ns_vac_to_r_zero = (
        cfg.magnetic_coupling
        * cfg.circumference
        * cfg.sigma_bar
        / np.sqrt(r_zero.density)
    )
    assert_close("TFFSA NS vacuum to R zero-mode form factor", matrix[ns_vac_index, r_zero_index], expected_ns_vac_to_r_zero)

    ns_pair_index = next(i for i, state in enumerate(states) if state.label.startswith("NS:pair"))
    r_pair_index = next(i for i, state in enumerate(states) if state.label.startswith("R:zero+pair"))
    ns_pair = states[ns_pair_index]
    r_pair = states[r_pair_index]
    crossed = [complex(theta, np.pi) for theta in ns_pair.rapidities] + [
        complex(theta) for theta in r_pair.rapidities
    ]
    expected_cross_sector_pair = (
        cfg.magnetic_coupling
        * cfg.circumference
        * tffsa.spin_sector_form_factor(crossed, cfg.sigma_bar)
        / np.sqrt(ns_pair.density * r_pair.density)
    )
    assert_close("TFFSA NS/R crossed sector form factor", matrix[ns_pair_index, r_pair_index], expected_cross_sector_pair)

    negative_mass_states = tffsa.sector_basis(
        cfg.num_pairs,
        cfg.mass,
        cfg.circumference,
        mass_sign=-1,
    )
    assert_equal(
        "positive-mass R sector uses odd parity",
        {state.parity for state in states if state.sector == "R"},
        {1},
    )
    assert_equal(
        "negative-mass R sector uses even parity",
        {state.parity for state in negative_mass_states if state.sector == "R"},
        {0},
    )

    free_cfg = tffsa.RunConfig(
        num_pairs=cfg.num_pairs,
        mass=cfg.mass,
        circumference=cfg.circumference,
        magnetic_coupling=0.0,
        sigma_bar=cfg.sigma_bar,
        mass_sign=cfg.mass_sign,
    )
    free_eigs = np.linalg.eigvalsh(tffsa.finite_matrix(free_cfg))
    expected_free = np.sort(np.array([state.energy for state in states]))
    assert_matrix_close("TFFSA zero-coupling spectrum", free_eigs, expected_free, tol=1.0e-12)


def check_tffsa_spectral_flow_derivatives() -> None:
    base = tffsa.RunConfig(
        num_pairs=4,
        mass=1.0,
        circumference=7.0,
        magnetic_coupling=0.0,
        sigma_bar=1.0,
        mass_sign=1,
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


def check_e8_ising_target_ratios() -> None:
    ratios = e8_ratios.mass_ratios()
    _assert_gt("E8 magnetic-Ising target ratio gaps", float(np.min(np.diff(ratios))), 0.0)
    assert_close("E8 mass-ratio normalization", ratios[0], 1.0)
    assert_close("E8 golden mass ratio", ratios[1], (1.0 + np.sqrt(5.0)) / 2.0)
    assert_close("E8 Coxeter eigenvalue mass ratio", ratios[2], 2.0 * np.cos(np.pi / 30.0))

    pf_check = e8_ratios.perron_frobenius_check()
    assert_close(
        "E8 adjacency largest eigenvalue",
        pf_check["largest_adjacency_eigenvalue"],
        pf_check["expected_largest_adjacency_eigenvalue"],
        tol=1.0e-13,
    )
    assert_leq("E8 PF mass-ratio check", pf_check["max_ratio_error"], 1.0e-12)


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
    _assert_gt("finite 't Hooft matrix smallest eigenvalue", float(np.linalg.eigvalsh(matrix)[0]), 0.0)


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


def check_residual_bound() -> None:
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


def check_variational_energy_bounds() -> None:
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

    rational_matrix = [
        [Fraction(1), Fraction(1, 3)],
        [Fraction(1, 3), Fraction(2)],
    ]
    rational_vector = [Fraction(1), Fraction(2)]
    rational_norm2 = sum(component * component for component in rational_vector)
    rational_probabilities = [component * component / rational_norm2 for component in rational_vector]
    rational_local_energy = [
        sum(rational_matrix[row][col] * rational_vector[col] for col in range(2)) / rational_vector[row]
        for row in range(2)
    ]
    rational_energy = sum(prob * value for prob, value in zip(rational_probabilities, rational_local_energy))
    centered_local_energy = [value - rational_energy for value in rational_local_energy]
    transition = [
        [Fraction(3, 5), Fraction(2, 5)],
        [Fraction(1, 10), Fraction(9, 10)],
    ]
    stationary = [
        sum(rational_probabilities[row] * transition[row][col] for row in range(2))
        for col in range(2)
    ]
    assert_equal("VMC Markov stationary local-energy law", stationary, rational_probabilities)

    gamma0 = sum(
        prob * centered * centered
        for prob, centered in zip(rational_probabilities, centered_local_energy)
    )
    assert_equal("VMC local-energy gamma zero", gamma0, Fraction(1, 25))
    sample_count = 5
    lag_factor = Fraction(1, 2)
    kernel_power = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
    ]
    for lag in range(sample_count):
        gamma_from_kernel = sum(
            rational_probabilities[row]
            * centered_local_energy[row]
            * kernel_power[row][col]
            * centered_local_energy[col]
            for row in range(2)
            for col in range(2)
        )
        assert_equal(f"VMC local-energy autocovariance lag {lag}", gamma_from_kernel, gamma0 * (lag_factor**lag))
        kernel_power = [
            [
                sum(kernel_power[row][middle] * transition[middle][col] for middle in range(2))
                for col in range(2)
            ]
            for row in range(2)
        ]

    variance_inflation = Fraction(1) + 2 * sum(
        (Fraction(1) - Fraction(lag, sample_count)) * (lag_factor**lag)
        for lag in range(1, sample_count)
    )
    variance_formula = gamma0 * variance_inflation / sample_count
    enumerated_mean = Fraction(0)
    enumerated_second_moment = Fraction(0)
    for path in product(range(2), repeat=sample_count):
        path_probability = rational_probabilities[path[0]]
        for index in range(sample_count - 1):
            path_probability *= transition[path[index]][path[index + 1]]
        path_mean = sum(rational_local_energy[state] for state in path) / sample_count
        enumerated_mean += path_probability * path_mean
        enumerated_second_moment += path_probability * path_mean * path_mean
    enumerated_variance = enumerated_second_moment - enumerated_mean * enumerated_mean
    assert_equal("VMC Markov sample mean expectation", enumerated_mean, rational_energy)
    assert_equal("VMC local-energy variance inflation", variance_inflation, Fraction(89, 40))
    assert_equal("VMC Markov sample mean variance", enumerated_variance, variance_formula)
    assert_equal("VMC effective sample size coordinate", Fraction(sample_count, 1) / variance_inflation, Fraction(200, 89))

    features = np.array(
        [
            [0.20, -0.10],
            [-0.35, 0.45],
            [0.55, 0.25],
            [-0.15, -0.30],
        ],
        dtype=float,
    )
    theta = np.array([0.18, -0.27], dtype=float)

    def trial(parameter: np.ndarray) -> np.ndarray:
        return np.exp(features @ parameter)

    def rayleigh_energy(parameter: np.ndarray) -> float:
        trial_vector = trial(parameter)
        return float(trial_vector @ matrix @ trial_vector / float(trial_vector @ trial_vector))

    trial_vector = trial(theta)
    norm2 = float(trial_vector @ trial_vector)
    probabilities = (trial_vector * trial_vector) / norm2
    local_energy = (matrix @ trial_vector) / trial_vector
    energy = float(np.sum(probabilities * local_energy))
    step = 1.0e-6
    for coordinate in range(features.shape[1]):
        score = features[:, coordinate]
        centered_score = score - float(np.sum(probabilities * score))
        force = 2.0 * float(np.sum(probabilities * centered_score * (local_energy - energy)))
        uncentered_force = 2.0 * float(np.sum(probabilities * score * (local_energy - energy)))
        finite_difference = (
            rayleigh_energy(theta + step * np.eye(features.shape[1])[coordinate])
            - rayleigh_energy(theta - step * np.eye(features.shape[1])[coordinate])
        ) / (2.0 * step)
        assert_close(f"variational score-force centered coordinate {coordinate}", force, finite_difference, tol=1.0e-8)
        assert_close(f"variational score-force centering coordinate {coordinate}", force, uncentered_force, tol=1.0e-12)


def check_mps_transfer_operator_correlator() -> None:
    lattice_spacing = 0.2
    mass_1 = 1.5
    mass_2 = 4.0
    q1 = math.exp(-lattice_spacing * mass_1)
    q2 = math.exp(-lattice_spacing * mass_2)
    transfer = np.diag([1.0, q1, q2])
    vacuum = np.array([1.0, 0.0, 0.0])

    single_mode_operator = np.array(
        [
            [0.0, 2.0, 0.0],
            [2.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
    )

    def connected(operator: np.ndarray, separation: int) -> float:
        expectation = float(vacuum @ operator @ vacuum)
        raw = float(vacuum @ operator @ np.linalg.matrix_power(transfer, separation) @ operator @ vacuum)
        return raw - expectation * expectation

    for separation in [1, 2, 5]:
        expected = 4.0 * (q1 ** separation)
        assert_close(f"MPS single-mode correlator n={separation}", connected(single_mode_operator, separation), expected)

    effective_mass = -math.log(connected(single_mode_operator, 4) / connected(single_mode_operator, 3)) / lattice_spacing
    assert_close("MPS single-mode effective mass", effective_mass, mass_1)

    mixed_operator = np.array(
        [
            [0.0, 2.0, 0.5],
            [2.0, 0.0, 0.0],
            [0.5, 0.0, 0.0],
        ]
    )
    for separation in [1, 3, 8]:
        mixed_mass = -math.log(connected(mixed_operator, separation + 1) / connected(mixed_operator, separation)) / lattice_spacing
        assert_leq(f"MPS mixed effective mass lower n={separation}", mass_1, mixed_mass)
        assert_leq(f"MPS mixed effective mass upper n={separation}", mixed_mass, mass_2)

    kappa = 0.6
    epsilon = kappa * lattice_spacing * lattice_spacing
    perturbed_ratio = math.exp(-lattice_spacing * mass_1) * (1.0 + epsilon)
    perturbed_mass = -math.log(perturbed_ratio) / lattice_spacing
    logarithmic_bound = abs(epsilon) / (lattice_spacing * (1.0 - abs(epsilon)))
    assert_leq("MPS logarithmic continuum-input remainder", abs(perturbed_mass - mass_1), logarithmic_bound)


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


def check_cross_method_consistency_bound() -> None:
    target = Fraction(13, 7)
    lattice_stat = Fraction(1, 50)
    lattice_remainder = Fraction(3, 100)
    lattice_matching = Fraction(1, 200)
    truncation_stat = Fraction(1, 40)
    truncation_remainder = Fraction(1, 25)
    truncation_matching = Fraction(1, 100)

    lattice_error = lattice_stat + lattice_remainder + lattice_matching
    truncation_error = truncation_stat + truncation_remainder + truncation_matching
    lattice_coordinate = target + lattice_error
    truncation_coordinate = target - truncation_error
    compatibility_bound = lattice_error + truncation_error

    assert_equal(
        "cross-method worst-case compatibility bound",
        abs(lattice_coordinate - truncation_coordinate),
        compatibility_bound,
    )

    hidden_normalization_mismatch = compatibility_bound + Fraction(1, 100)
    if hidden_normalization_mismatch <= compatibility_bound:
        raise AssertionError("hidden mismatch should violate the declared compatibility bound")


def check_benchmark_manifest_consistency() -> None:
    result = benchmark_manifest.analyze_manifest(benchmark_manifest.smoke_manifest())
    if not result["all_pairs_pass"]:
        raise AssertionError("benchmark manifest smoke data should pass its finite pairwise check")
    assert_equal("benchmark manifest method count", result["method_count"], 3)
    pair_lookup = {(entry["left"], entry["right"]): entry for entry in result["pairs"]}
    lattice_truncation = pair_lookup[("lattice-transfer-matrix", "hamiltonian-truncation")]
    assert_close(
        "benchmark manifest first pair margin",
        lattice_truncation["component_margins"][0],
        0.0044,
        tol=1.0e-12,
    )
    assert_close(
        "benchmark manifest second-component difference",
        lattice_truncation["component_differences"][1],
        0.0080,
        tol=1.0e-12,
    )
    if not lattice_truncation["normalizations_match"]:
        raise AssertionError("benchmark manifest smoke normalizations should match")
    if not lattice_truncation["envelopes_pass"]:
        raise AssertionError("benchmark manifest smoke envelopes should pass")

    failing = benchmark_manifest.smoke_manifest()
    failing["methods"][2]["coordinate"] = [1.6400, 2.0400]
    failing_result = benchmark_manifest.analyze_manifest(failing)
    if failing_result["all_pairs_pass"]:
        raise AssertionError("benchmark manifest must detect coordinates outside declared envelopes")

    normalization_failing = benchmark_manifest.smoke_manifest()
    normalization_failing["methods"][1]["normalization"] = "deliberately-incompatible"
    normalization_result = benchmark_manifest.analyze_manifest(normalization_failing)
    normalization_pairs = {
        (entry["left"], entry["right"]): entry
        for entry in normalization_result["pairs"]
    }
    mismatched_pair = normalization_pairs[("lattice-transfer-matrix", "hamiltonian-truncation")]
    if mismatched_pair["normalizations_match"]:
        raise AssertionError("benchmark manifest regression should create a normalization mismatch")
    if not mismatched_pair["envelopes_pass"]:
        raise AssertionError("normalization mismatch regression should change only the normalization label")
    if mismatched_pair["passes"]:
        raise AssertionError("normalization mismatch must fail the affected pair")
    if normalization_result["all_pairs_pass"]:
        raise AssertionError("normalization mismatch must fail the aggregate manifest result")


def main() -> None:
    check_ising_bogoliubov_benchmark()
    check_sine_gordon_zero_mode_selection_rules()
    check_sine_gordon_tcsa_vertex_assembly()
    check_phi4_hamiltonian_truncation_matrix()
    check_phi4_dlcq_matrix()
    check_tffsa_ns_r_spin_block()
    check_tffsa_spectral_flow_derivatives()
    check_e8_ising_target_ratios()
    check_thooft_quadratic_form_identity()
    check_thooft_large_K_fit_algebra()
    check_residual_bound()
    check_feshbach_determinant_identity()
    check_krylov_residual_and_moments()
    check_variational_energy_bounds()
    check_mps_transfer_operator_correlator()
    check_light_front_kinematic_identities()
    check_cross_method_consistency_bound()
    check_benchmark_manifest_consistency()
    print("All Hamiltonian-truncation and DLCQ checks passed.")


if __name__ == "__main__":
    main()
