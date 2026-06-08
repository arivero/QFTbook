#!/usr/bin/env python3
"""Finite checks for the thermal Kubo and spectral-function conventions.

Evidence contract.
Target claims: Volume X, Chapter 4 uses one retarded/source-response sign
ledger, separates commutator spectral data from full source derivatives, and
keeps the response-contact sign consistent when translating to the
conductivity kernel.  It also separates Fourier upper-half-plane retarded
variables from Laplace/Abel variables, derives the Abel static-dynamical
mismatch from the switched vector-potential source, and distinguishes
isothermal twist curvature from adiabatic Kohn curvature.
Independent construction: two-level Lehmann weights, finite retarded pole
models, a minimally coupled charged oscillator with a diamagnetic contact
term, finite Mazur projection algebra, and a two-dimensional Mori-Zwanzig
Schur-complement model.  The conductivity-sector checks separate Hermitian
dissipation from a real antisymmetric Hall block.  The Mazur/Drude checks use
an Abel-switched source response for the zero-Liouville current covariance,
an H=0 conserved-current negative control, an explicit tight-binding
periodic-twist/open-boundary comparison, an isothermal-versus-adiabatic twist
curvature comparison, a finite oscillatory negative control, and a polynomial
ultraviolet-tail control to separate source-derived Drude residues and filtered
Cesaro/Abel zero-frequency projections from unproved commutator-FDT,
pointwise, static-equilibrium, unfiltered continuum, wrong analytic-domain, or
sign-changing-filter positivity claims.
Imported assumptions: the thermal KMS condition, finite-volume linear
response, and the interpretation of real local source contacts as contact
terms outside the nonzero-frequency commutator spectral measure.
Negative controls: the wrong contact sign leaves a spurious static
conductivity kernel, real contact terms do not alter the dissipative spectral
Hermitian spectral slope, the Hall block is not accepted as a positive
entrywise real measure, the Drude sector is separated from the regular dc
slope, the commutator spectral density of an exact H=0 zero mode is not
accepted as determining the symmetrized zero atom, an oscillatory
finite-volume correlator is not accepted as having a pointwise long-time
Drude limit, an equilibrium static pure-gauge cancellation is not identified
with the Abel dynamical kernel, and a locally finite low-frequency measure
with a polynomial ultraviolet tail is not accepted as supporting unfiltered
dominated convergence; sign-changing or complex compact filters are rejected
when the proof claims a positive filtered measure.  The open-boundary
finite-size Drude atom is not accepted as the periodic twist/Kohn route: the
former vanishes at every finite size in the tight-binding check while regular
peaks collapse toward zero with increasing size.  Evaluating the Fourier
retarded transform at real epsilon, substituting isothermal curvature for
adiabatic curvature, or dropping the switched-source endpoint/contact is also
rejected.
Scope boundary: these checks do not prove hydrodynamic closure, continuum
limit exchange, or Euclidean analytic-continuation stability.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import math


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    size = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(size)) for j in range(size)] for i in range(size)]


def matadd(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    size = len(a)
    return [[a[i][j] + b[i][j] for j in range(size)] for i in range(size)]


def matcomm(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return matadd(matmul(a, b), matscale(-1.0, matmul(b, a)))


def matscale(c: complex, a: list[list[complex]]) -> list[list[complex]]:
    return [[c * a[i][j] for j in range(len(a))] for i in range(len(a))]


def adjoint(a: list[list[complex]]) -> list[list[complex]]:
    size = len(a)
    return [[a[j][i].conjugate() for j in range(size)] for i in range(size)]


def hermitian_part(a: list[list[complex]]) -> list[list[complex]]:
    return matscale(0.5, matadd(a, adjoint(a)))


def antihermitian_part(a: list[list[complex]]) -> list[list[complex]]:
    return matscale(0.5, matadd(a, matscale(-1.0, adjoint(a))))


def quadratic_form(a: list[list[complex]], vector: list[complex]) -> complex:
    return sum(
        vector[i].conjugate() * a[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def trace(a: list[list[complex]]) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def thermal_expectation(rho: list[list[complex]], a: list[list[complex]]) -> complex:
    return trace(matmul(rho, a))


IDENTITY = [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
SIGMA_X = [[0j, 1.0 + 0j], [1.0 + 0j, 0j]]
SIGMA_Z = [[1.0 + 0j, 0j], [0j, -1.0 + 0j]]


def two_level_weights(beta: float, delta: float) -> dict[str, float]:
    """Delta-function weights for A=sigma_x in a two-level system.

    The Hamiltonian has energies 0 and delta.  The dictionary records the
    coefficients multiplying 2*pi*delta(omega +/- delta).
    """

    boltzmann = math.exp(-beta * delta)
    z = 1.0 + boltzmann
    return {
        "greater_plus": 1.0 / z,
        "greater_minus": boltzmann / z,
        "less_plus": boltzmann / z,
        "less_minus": 1.0 / z,
        "rho_plus": (1.0 - boltzmann) / z,
        "rho_minus": -(1.0 - boltzmann) / z,
    }


def coth(x: float) -> float:
    return math.cosh(x) / math.sinh(x)


def check_two_level_kms_and_fdt() -> None:
    for beta, delta in ((0.7, 1.3), (2.1, 0.4), (1.0, 3.0)):
        w = two_level_weights(beta, delta)

        assert_close(
            "KMS detailed balance at positive frequency",
            w["less_plus"],
            math.exp(-beta * delta) * w["greater_plus"],
        )
        assert_close(
            "KMS detailed balance at negative frequency",
            w["less_minus"],
            math.exp(beta * delta) * w["greater_minus"],
        )

        sym_plus = 0.5 * (w["greater_plus"] + w["less_plus"])
        sym_minus = 0.5 * (w["greater_minus"] + w["less_minus"])
        assert_close(
            "FDT at positive frequency",
            sym_plus,
            0.5 * coth(0.5 * beta * delta) * w["rho_plus"],
        )
        assert_close(
            "FDT at negative frequency",
            sym_minus,
            0.5 * coth(-0.5 * beta * delta) * w["rho_minus"],
        )

        assert w["rho_plus"] > 0.0
        assert w["rho_minus"] < 0.0
        assert_close("odd spectral weights", w["rho_plus"], -w["rho_minus"])


def retarded_shear_model(omega: float, eta: float, tau: float) -> complex:
    """A causal one-pole model with Im G_R(omega) = -eta*omega + O(omega^3)."""

    return (-1j * eta * omega) / (1.0 - 1j * omega * tau)


def oscillator_paramagnetic_retarded(z: complex, charge: float, mass: float, frequency: float) -> complex:
    """Retarded commutator kernel for J_p=q p/m in a charged oscillator."""

    return charge * charge * frequency * frequency / (mass * (z * z - frequency * frequency))


def check_retarded_sign_and_transport_slope() -> None:
    eta = 0.73
    tau = 1.9
    for omega in (1.0e-4, 2.0e-4, 5.0e-4):
        gr = retarded_shear_model(omega, eta, tau)
        rho = -2.0 * gr.imag
        assert rho > 0.0
        assert_close("spectral slope gives eta", rho / (2.0 * omega), eta, tol=2.0e-6)
        assert_close("minus imaginary slope gives eta", -gr.imag / omega, eta, tol=2.0e-6)


def check_contact_term_does_not_change_spectral_slope() -> None:
    eta = 0.41
    tau = 0.6
    contact_static = 3.7
    contact_quadratic = -0.2
    omega = 3.0e-4
    nonlocal_gr = retarded_shear_model(omega, eta, tau)
    full_kernel = nonlocal_gr + contact_static + contact_quadratic * omega * omega
    assert_close(
        "real contact term leaves spectral density unchanged",
        -2.0 * full_kernel.imag,
        -2.0 * nonlocal_gr.imag,
    )
    assert_close("contact-independent transport slope", -full_kernel.imag / omega, eta, tol=2.0e-7)


def check_hall_block_is_not_positive_dissipative_measure() -> None:
    gamma = 0.73
    hall = 1.9
    sigma = [[gamma + 0j, hall + 0j], [-hall + 0j, gamma + 0j]]

    sigma_diss = hermitian_part(sigma)
    sigma_react = antihermitian_part(sigma)
    expected_diss = [[gamma + 0j, 0j], [0j, gamma + 0j]]
    expected_react = [[0j, hall + 0j], [-hall + 0j, 0j]]

    for i in range(2):
        for j in range(2):
            assert_close("Hall Hermitian dissipative projection", sigma_diss[i][j].real, expected_diss[i][j].real)
            assert_close("Hall Hermitian dissipative projection imaginary", sigma_diss[i][j].imag, 0.0)
            assert_close("Hall reactive projection", sigma_react[i][j].real, expected_react[i][j].real)
            assert_close("Hall reactive projection imaginary", sigma_react[i][j].imag, 0.0)

    real_forces = ([1.2 + 0j, -0.4 + 0j], [0.3 + 0j, 2.0 + 0j])
    complex_phasors = ([1.0 + 0.5j, -0.2 + 0.7j], [0.3 - 0.6j, 1.4 + 0.2j])
    for force in real_forces + complex_phasors:
        dissipated_power = quadratic_form(sigma_diss, list(force))
        reactive_power = quadratic_form(sigma_react, list(force))
        full_power = quadratic_form(sigma, list(force))
        assert dissipated_power.real > 0.0
        assert_close("Hall block has zero real entropy production", reactive_power.real, 0.0)
        assert_close("full real power equals Hermitian dissipative power", full_power.real, dissipated_power.real)

    entrywise_real_includes_hall = [[entry.real for entry in row] for row in sigma]
    if entrywise_real_includes_hall[0][1] == 0.0 or entrywise_real_includes_hall[1][0] == 0.0:
        raise AssertionError("entrywise real conductivity should still contain the Hall block")
    nonsymmetric_minor = entrywise_real_includes_hall[0][1] - entrywise_real_includes_hall[1][0]
    if abs(nonsymmetric_minor) <= hall:
        raise AssertionError("entrywise real Hall block was incorrectly projected out")


def check_vector_potential_response_sign() -> None:
    sigma_dc = 0.58
    tau = 1.1
    omega = 2.0e-4
    response_kernel = retarded_shear_model(omega, sigma_dc, tau)
    conductivity = -response_kernel / (1j * omega)
    assert_close("positive conductivity from -K/(i omega)", conductivity.real, sigma_dc, tol=1.0e-7)


def check_diamagnetic_contact_response_convention() -> None:
    charge = 1.3
    mass = 2.0
    frequency = 0.7
    response_contact = -(charge * charge) / mass

    static_commutator_kernel = oscillator_paramagnetic_retarded(0.0, charge, mass, frequency).real
    full_static_response = -static_commutator_kernel + response_contact
    conductivity_static_kernel = static_commutator_kernel - response_contact
    wrong_static_kernel = static_commutator_kernel + response_contact

    assert_close(
        "oscillator paramagnetic static kernel",
        static_commutator_kernel,
        -(charge * charge) / mass,
    )
    assert_close("full static vector-potential response cancels", full_static_response, 0.0)
    assert_close("conductivity static kernel cancels", conductivity_static_kernel, 0.0)
    assert_close("wrong contact sign leaves static kernel", wrong_static_kernel, 2.0 * response_contact)

    z = 0.41 + 0.08j
    nonlocal_kernel = oscillator_paramagnetic_retarded(z, charge, mass, frequency)
    full_response = -nonlocal_kernel + response_contact
    conductivity_kernel = nonlocal_kernel - response_contact
    assert_close(
        "conductivity kernel is negative full response",
        (conductivity_kernel + full_response).real,
        0.0,
    )
    assert_close(
        "conductivity kernel is negative full response imaginary part",
        (conductivity_kernel + full_response).imag,
        0.0,
    )
    assert_close(
        "conductivity kernel imaginary part is nonlocal spectral part",
        conductivity_kernel.imag,
        nonlocal_kernel.imag,
    )


def check_fourier_laplace_abel_domain_relation() -> None:
    """The Abel point is the Fourier transform at zeta=i*epsilon."""

    gamma = 0.7
    contact = -0.23

    def retarded_fourier(zeta: complex) -> complex:
        # Integral_0^infty exp(i*zeta*t) exp(-gamma*t) dt.
        return 1.0 / (gamma - 1j * zeta)

    def retarded_laplace(s_value: float) -> complex:
        return 1.0 / (gamma + s_value)

    for epsilon in (0.4, 0.2, 0.05):
        laplace_kernel = retarded_laplace(epsilon) - contact
        fourier_abel_kernel = retarded_fourier(1j * epsilon) - contact
        wrong_real_frequency_kernel = retarded_fourier(epsilon) - contact

        assert_close(
            "Laplace Abel equals Fourier at i epsilon",
            fourier_abel_kernel.real,
            laplace_kernel.real,
        )
        assert_close("Laplace Abel imaginary part", fourier_abel_kernel.imag, 0.0)
        if abs(wrong_real_frequency_kernel - laplace_kernel) < 1.0e-6:
            raise AssertionError("Fourier kernel evaluated at real epsilon was accepted as the Abel kernel")


def check_switched_source_endpoint_and_contact_are_load_bearing() -> None:
    """The Abel mismatch is derived by subtracting the final static endpoint."""

    epsilon = 0.2
    electric_field = 0.6
    isothermal_static_kernel = 0.42
    noncontact_laplace_kernel = 0.73
    response_contact = -0.11
    dynamic_abel_kernel = noncontact_laplace_kernel - response_contact

    final_vector_potential = -electric_field / epsilon
    dynamic_current_density = -dynamic_abel_kernel * final_vector_potential
    isothermal_current_density = -isothermal_static_kernel * final_vector_potential
    sigma_epsilon = (dynamic_current_density - isothermal_current_density) / electric_field

    assert_close(
        "switched source derives Abel mismatch",
        epsilon * sigma_epsilon,
        dynamic_abel_kernel - isothermal_static_kernel,
    )

    without_endpoint_subtraction = dynamic_current_density / electric_field
    wrong_without_endpoint = epsilon * without_endpoint_subtraction
    expected_mismatch = dynamic_abel_kernel - isothermal_static_kernel
    if abs(wrong_without_endpoint - expected_mismatch) < 1.0e-12:
        raise AssertionError("integration-by-parts endpoint was silently dropped")

    contact_omitted_dynamic_kernel = noncontact_laplace_kernel
    if abs(
        (contact_omitted_dynamic_kernel - isothermal_static_kernel)
        - (dynamic_abel_kernel - isothermal_static_kernel)
    ) < 1.0e-12:
        raise AssertionError("source contact omission did not change the Abel mismatch")


def check_isothermal_not_adiabatic_twist_curvature() -> None:
    """Finite-temperature Gibbs curvature includes population derivatives."""

    beta = 0.6
    level_curvature = 3.0
    current_slope = 1.1
    volume = 5.0
    probabilities = [0.5, 0.5]
    energy_slopes = [current_slope, -current_slope]
    energy_curvatures = [level_curvature, level_curvature]

    mean_slope = sum(
        weight * slope
        for weight, slope in zip(probabilities, energy_slopes, strict=True)
    )
    slope_covariance = sum(
        weight * (slope - mean_slope) ** 2
        for weight, slope in zip(probabilities, energy_slopes, strict=True)
    )
    adiabatic_curvature = sum(
        weight * curvature
        for weight, curvature in zip(probabilities, energy_curvatures, strict=True)
    ) / volume
    isothermal_curvature = adiabatic_curvature - beta * slope_covariance / volume

    assert isothermal_curvature < adiabatic_curvature
    assert_close(
        "isothermal curvature differs by diagonal-current covariance",
        adiabatic_curvature - isothermal_curvature,
        beta * slope_covariance / volume,
    )
    if abs(isothermal_curvature - adiabatic_curvature) < 1.0e-12:
        raise AssertionError("isothermal curvature was substituted for adiabatic Kohn curvature")


def check_bond_phase_total_twist_normalization() -> None:
    """Uniform bond phase A and total twist phi=L*A have different conjugates."""

    length = 8
    hopping = 1.0

    def energy_from_total_twist(mode: int, phi: float) -> float:
        momentum = 2.0 * math.pi * mode / length + phi / length
        return -2.0 * hopping * math.cos(momentum)

    def energy_from_bond_phase(mode: int, bond_phase: float) -> float:
        return energy_from_total_twist(mode, length * bond_phase)

    def current_total_twist(mode: int, phi: float) -> float:
        momentum = 2.0 * math.pi * mode / length + phi / length
        return -(2.0 * hopping / length) * math.sin(momentum)

    def current_bond_phase(mode: int, bond_phase: float) -> float:
        momentum = 2.0 * math.pi * mode / length + bond_phase
        return -2.0 * hopping * math.sin(momentum)

    mode = 1
    phi = 0.13
    bond_phase = phi / length
    assert_close(
        "bond phase and total twist parametrize the same finite spectrum",
        energy_from_bond_phase(mode, bond_phase),
        energy_from_total_twist(mode, phi),
    )
    assert_close(
        "bond-phase current is L times total-twist current",
        current_bond_phase(mode, bond_phase),
        length * current_total_twist(mode, phi),
    )

    step = 1.0e-4
    curvature_phi = (
        energy_from_total_twist(mode, step)
        - 2.0 * energy_from_total_twist(mode, 0.0)
        + energy_from_total_twist(mode, -step)
    ) / (step * step)
    curvature_bond = (
        energy_from_bond_phase(mode, step)
        - 2.0 * energy_from_bond_phase(mode, 0.0)
        + energy_from_bond_phase(mode, -step)
    ) / (step * step)
    assert_close(
        "bond-phase curvature carries L squared relative to total twist",
        curvature_bond,
        length * length * curvature_phi,
        tol=1.0e-6,
    )


def check_mazur_projection_and_drude_weight() -> None:
    beta = 0.8
    gap = 1.3
    volume = 5.0
    current_conserved_part = 0.37
    current_oscillating_part = -0.22

    weights = [math.exp(-beta * gap / 2.0), math.exp(beta * gap / 2.0)]
    partition = sum(weights)
    rho = [[weights[0] / partition, 0j], [0j, weights[1] / partition]]
    mean_sigma_z = thermal_expectation(rho, SIGMA_Z).real
    q = matadd(SIGMA_Z, matscale(-mean_sigma_z, IDENTITY))
    current = matadd(matscale(current_conserved_part, q), matscale(current_oscillating_part, SIGMA_X))

    def sym_inner(a: list[list[complex]], b: list[list[complex]]) -> float:
        anticommutator = matadd(matmul(a, b), matmul(b, a))
        return (thermal_expectation(rho, anticommutator).real) / (2.0 * volume)

    covariance = sym_inner(q, q)
    overlap = sym_inner(current, q)
    mazur_projection_norm = overlap * overlap / covariance
    expected_persistent = current_conserved_part * current_conserved_part * covariance
    assert_close("Mazur projection gives conserved current component", mazur_projection_norm, expected_persistent)

    oscillating_current = matscale(current_oscillating_part, SIGMA_X)
    oscillating_covariance = sym_inner(oscillating_current, oscillating_current)

    # Abel-switched electric-field response after the static vector-potential
    # contact has been cancelled:
    #   sigma_epsilon = beta int_0^infty exp(-epsilon t) C(t) dt.
    # The zero-Liouville component contributes beta*A0/epsilon, while the
    # finite-frequency oscillatory component contributes only an Abel-regular
    # term beta*B*epsilon/(epsilon^2+gap^2).
    residues = []
    for epsilon in (0.4, 0.2, 0.1, 0.05):
        source_conductivity = beta * (
            expected_persistent / epsilon
            + oscillating_covariance * epsilon / (epsilon * epsilon + gap * gap)
        )
        residues.append(epsilon * source_conductivity)
    target_residue = beta * expected_persistent
    assert residues[0] > residues[1] > residues[2] > target_residue
    assert_close("Abel source response gives Drude residue", residues[-1], target_residue, tol=7.0e-4)


def check_commutator_fdt_loses_exact_zero_mode() -> None:
    beta = 1.4
    volume = 3.0
    rho = [[0.5 + 0j, 0j], [0j, 0.5 + 0j]]
    conserved_current = SIGMA_Z

    sym_zero_atom = (
        thermal_expectation(
            rho,
            matadd(matmul(conserved_current, conserved_current), matmul(conserved_current, conserved_current)),
        ).real
        / (2.0 * volume)
    )
    commutator_zero_weight = thermal_expectation(
        rho,
        matadd(
            matmul(conserved_current, conserved_current),
            matscale(-1.0, matmul(conserved_current, conserved_current)),
        ),
    ).real

    assert sym_zero_atom > 0.0
    assert_close("H=0 conserved current has no commutator spectral atom", commutator_zero_weight, 0.0)

    naive_drude_from_commutator_fdt = beta * commutator_zero_weight
    source_response_drude_residue = beta * sym_zero_atom
    assert source_response_drude_residue > 0.0
    if abs(naive_drude_from_commutator_fdt - source_response_drude_residue) < 1.0e-12:
        raise AssertionError("commutator FDT incorrectly reconstructed the exact zero-mode atom")


def check_periodic_twist_and_open_boundary_drude_routes() -> None:
    beta = 1.3
    hopping = 1.0

    def thermal_weights(energies: list[float]) -> list[float]:
        shifted = [energy - min(energies) for energy in energies]
        raw = [math.exp(-beta * energy) for energy in shifted]
        total = sum(raw)
        return [weight / total for weight in raw]

    def periodic_levels(length: int, twist: float) -> list[tuple[float, float]]:
        levels = []
        for mode in range(length):
            momentum = 2.0 * math.pi * mode / length + twist / length
            energy = -2.0 * hopping * math.cos(momentum)
            current = -(2.0 * hopping / length) * math.sin(momentum)
            levels.append((energy, current))
        return levels

    def periodic_current_expectation(length: int, twist: float) -> float:
        levels = periodic_levels(length, twist)
        weights = thermal_weights([energy for energy, _current in levels])
        return sum(weight * current for weight, (_energy, current) in zip(weights, levels, strict=True))

    periodic_length = 6
    twist_step = 1.0e-4
    periodic_levels_at_zero = periodic_levels(periodic_length, 0.0)
    periodic_weights = thermal_weights([energy for energy, _current in periodic_levels_at_zero])
    periodic_mean_current = sum(
        weight * current
        for weight, (_energy, current) in zip(periodic_weights, periodic_levels_at_zero, strict=True)
    )
    periodic_zero_atom = sum(
        weight * (current - periodic_mean_current) ** 2
        for weight, (_energy, current) in zip(periodic_weights, periodic_levels_at_zero, strict=True)
    ) / periodic_length
    periodic_static_kernel = -(
        periodic_current_expectation(periodic_length, twist_step)
        - periodic_current_expectation(periodic_length, -twist_step)
    ) / (2.0 * twist_step * periodic_length)

    assert periodic_zero_atom > 0.0
    assert abs(periodic_static_kernel) > 1.0e-5

    def open_energies(length: int) -> list[float]:
        return [
            -2.0 * hopping * math.cos(math.pi * (mode + 1) / (length + 1))
            for mode in range(length)
        ]

    def open_vector(length: int, mode: int, bond_phase: float = 0.0) -> list[complex]:
        momentum = math.pi * (mode + 1) / (length + 1)
        norm = math.sqrt(2.0 / (length + 1))
        return [
            norm
            * math.sin(momentum * (site + 1))
            * complex(math.cos(bond_phase * site), math.sin(bond_phase * site))
            for site in range(length)
        ]

    def zero_matrix(size: int) -> list[list[complex]]:
        return [[0j for _col in range(size)] for _row in range(size)]

    def open_hamiltonian_matrix(length: int, bond_phase: float = 0.0) -> list[list[complex]]:
        matrix = zero_matrix(length)
        phase = complex(math.cos(bond_phase), math.sin(bond_phase))
        for site in range(length - 1):
            matrix[site + 1][site] = -hopping * phase
            matrix[site][site + 1] = -hopping * phase.conjugate()
        return matrix

    def open_current_matrix(length: int, bond_phase: float = 0.0) -> list[list[complex]]:
        matrix = zero_matrix(length)
        phase = complex(math.cos(bond_phase), math.sin(bond_phase))
        for site in range(length - 1):
            matrix[site + 1][site] = 1j * hopping * phase
            matrix[site][site + 1] = -1j * hopping * phase.conjugate()
        return matrix

    def open_contact_matrix(length: int, bond_phase: float = 0.0) -> list[list[complex]]:
        matrix = zero_matrix(length)
        phase = complex(math.cos(bond_phase), math.sin(bond_phase))
        for site in range(length - 1):
            matrix[site + 1][site] = -hopping * phase
            matrix[site][site + 1] = -hopping * phase.conjugate()
        return matrix

    def position_matrix(length: int) -> list[list[complex]]:
        matrix = zero_matrix(length)
        for site in range(length):
            matrix[site][site] = site + 0j
        return matrix

    def matrix_element(vector_l: list[complex], matrix: list[list[complex]], vector_r: list[complex]) -> complex:
        return sum(
            vector_l[row].conjugate() * matrix[row][col] * vector_r[col]
            for row in range(len(vector_l))
            for col in range(len(vector_r))
        )

    open_length = 10
    open_hamiltonian = open_hamiltonian_matrix(open_length)
    open_position = position_matrix(open_length)
    current_from_commutator = matscale(1j, matcomm(open_hamiltonian, open_position))
    direct_open_current = open_current_matrix(open_length)
    commutator_error = sum(
        abs(current_from_commutator[row][col] - direct_open_current[row][col]) ** 2
        for row in range(open_length)
        for col in range(open_length)
    )
    assert_close("open current is i[H,X]", math.sqrt(commutator_error), 0.0)

    open_weights = thermal_weights(open_energies(open_length))
    open_current = open_current_matrix(open_length)
    open_diagonal_currents = [
        matrix_element(open_vector(open_length, mode), open_current, open_vector(open_length, mode)).real
        for mode in range(open_length)
    ]
    open_zero_atom = sum(weight * current * current for weight, current in zip(open_weights, open_diagonal_currents, strict=True))
    assert_close("finite open-boundary exact zero-frequency atom vanishes", open_zero_atom, 0.0)

    def open_current_expectation(length: int, bond_phase: float) -> float:
        weights = thermal_weights(open_energies(length))
        current = open_current_matrix(length, bond_phase)
        return sum(
            weight
            * matrix_element(open_vector(length, mode, bond_phase), current, open_vector(length, mode, bond_phase)).real
            for mode, weight in enumerate(weights)
        )

    phase_step = 1.0e-5
    open_static_derivative = (
        open_current_expectation(open_length, phase_step)
        - open_current_expectation(open_length, -phase_step)
    ) / (2.0 * phase_step)
    open_contact_expectation = sum(
        weight
        * matrix_element(
            open_vector(open_length, mode),
            open_contact_matrix(open_length),
            open_vector(open_length, mode),
        ).real
        for mode, weight in enumerate(open_weights)
    )
    assert_close("open pure-gauge equilibrium current derivative vanishes", open_static_derivative, 0.0, tol=2.0e-9)
    assert abs(open_contact_expectation) > 0.1

    def lowest_open_transition(length: int) -> tuple[float, float]:
        energies = open_energies(length)
        weights = thermal_weights(energies)
        current = open_current_matrix(length)
        best_frequency = math.inf
        best_weight = 0.0
        vectors = [open_vector(length, mode) for mode in range(length)]
        for left in range(length):
            for right in range(left + 1, length):
                element = matrix_element(vectors[left], current, vectors[right])
                spectral_weight = 0.5 * (weights[left] + weights[right]) * abs(element) ** 2 / length
                if spectral_weight > 1.0e-12:
                    frequency = abs(energies[right] - energies[left])
                    if frequency < best_frequency:
                        best_frequency = frequency
                        best_weight = spectral_weight
        return best_frequency, best_weight

    open_transitions = [lowest_open_transition(length) for length in (12, 24, 48)]
    open_frequencies = [frequency for frequency, _weight in open_transitions]
    assert open_frequencies[0] > open_frequencies[1] > open_frequencies[2]
    assert open_frequencies[2] < 0.4 * open_frequencies[0]
    assert all(weight > 0.0 for _frequency, weight in open_transitions)


def check_cesaro_abel_not_pointwise_negative_control() -> None:
    constant_component = 0.31
    omega = 1.7

    def correlation(time: float) -> float:
        return constant_component + math.cos(omega * time)

    for periods in (1, 3, 11):
        time_window = 2.0 * math.pi * periods / omega
        cesaro_average = constant_component + math.sin(omega * time_window) / (omega * time_window)
        assert_close("Cesaro average over complete oscillation periods isolates zero-frequency atom", cesaro_average, constant_component)

    for epsilon in (0.2, 0.1, 0.05):
        abel_average = constant_component + epsilon * epsilon / (epsilon * epsilon + omega * omega)
        assert abel_average > constant_component
    small_epsilon = 1.0e-4
    abel_small = constant_component + small_epsilon * small_epsilon / (small_epsilon * small_epsilon + omega * omega)
    assert_close("Abel average isolates zero-frequency atom", abel_small, constant_component, tol=4.0e-9)

    maxima_subsequence = [correlation(2.0 * math.pi * n / omega) for n in (5, 17, 41)]
    minima_subsequence = [correlation((2 * n + 1) * math.pi / omega) for n in (5, 17, 41)]
    for value in maxima_subsequence:
        assert_close("oscillatory subsequence maximum persists", value, constant_component + 1.0)
    for value in minima_subsequence:
        assert_close("oscillatory subsequence minimum persists", value, constant_component - 1.0)
    if not abs(maxima_subsequence[-1] - minima_subsequence[-1]) > 1.9:
        raise AssertionError("oscillatory finite-volume correlator should not have a pointwise long-time limit")


def check_filtered_drude_rejects_uncontrolled_uv_tail() -> None:
    atom = 0.31
    low_frequency_weights = [(0.2, 0.05), (0.4, 0.07), (0.7, 0.02)]

    filtered_total_variation = sum(weight for _omega, weight in low_frequency_weights)
    assert filtered_total_variation < 0.2

    for epsilon in (0.2, 0.05, 0.01):
        filtered_abel_remainder = sum(
            weight * epsilon / complex(epsilon, omega)
            + weight * epsilon / complex(epsilon, -omega)
            for omega, weight in low_frequency_weights
        )
        assert filtered_abel_remainder.real > 0.0
        assert filtered_abel_remainder.real < 2.0 * epsilon * sum(weight / omega for omega, weight in low_frequency_weights)
    tiny_epsilon = 1.0e-5
    filtered_abel = atom + sum(
        (
            weight * tiny_epsilon / complex(tiny_epsilon, omega)
            + weight * tiny_epsilon / complex(tiny_epsilon, -omega)
        ).real
        for omega, weight in low_frequency_weights
    )
    assert_close("filtered Abel low-frequency projection isolates atom", filtered_abel, atom, tol=2.0e-5)

    def uv_dominated_convergence_majorant(cutoff: int, time_window: float) -> float:
        # The Cesaro kernel is bounded by 2/(T |omega|) away from zero.  With
        # polynomial weights n^2 at omega=n, this candidate majorant grows
        # like sum n/T and has no cutoff-independent finite bound.
        return sum((n * n) * 2.0 / (time_window * n) for n in range(1, cutoff + 1))

    majorants = [uv_dominated_convergence_majorant(cutoff, time_window=10.0) for cutoff in (10, 100, 1000)]
    assert majorants[0] < majorants[1] < majorants[2]
    if majorants[2] <= 100.0 * majorants[0]:
        raise AssertionError("polynomial UV tail should defeat an unfiltered dominated-convergence bound")

    def uv_abel_resolvent_size(cutoff: int, epsilon: float) -> float:
        return sum((n * n) * abs(epsilon / complex(epsilon, n)) for n in range(1, cutoff + 1))

    uv_sizes = [uv_abel_resolvent_size(cutoff, epsilon=0.1) for cutoff in (10, 100, 1000)]
    assert uv_sizes[0] < uv_sizes[1] < uv_sizes[2]
    if uv_sizes[2] <= 100.0 * uv_sizes[0]:
        raise AssertionError("polynomial UV tail should require smearing, cutoff, or subtraction")


def check_filtered_drude_cutoff_positivity_contract() -> None:
    spectral_weights = [(-2, 0.03), (-1, 0.05), (1, 0.05), (2, 0.03)]
    positive_cutoff = {
        -2: 0.0 + 0j,
        -1: 0.5 + 0j,
        0: 1.0 + 0j,
        1: 0.5 + 0j,
        2: 0.0 + 0j,
    }
    sign_changing_cutoff = {
        -2: 0.0 + 0j,
        -1: -0.25 + 0j,
        0: 1.0 + 0j,
        1: -0.25 + 0j,
        2: 0.0 + 0j,
    }
    complex_cutoff = {
        -2: 0.0 + 0j,
        -1: 0.5 + 0j,
        0: 1.0 + 0j,
        1: 0.5 + 0.2j,
        2: 0.0 + 0j,
    }
    overlarge_cutoff = {
        -2: 0.0 + 0j,
        -1: 1.5 + 0j,
        0: 1.0 + 0j,
        1: 1.5 + 0j,
        2: 0.0 + 0j,
    }

    def is_positive_even_real_cutoff(
        cutoff: dict[int, complex],
        tolerance: float = 1.0e-12,
    ) -> bool:
        for omega, value in cutoff.items():
            reflected = cutoff.get(-omega)
            if reflected is None:
                return False
            if abs(value.imag) > tolerance or value.real < -tolerance:
                return False
            if value.real > 1.0 + tolerance:
                return False
            if abs(value - reflected) > tolerance:
                return False
        return True

    def positive_filtered_weights(
        cutoff: dict[int, complex],
    ) -> list[tuple[int, float]]:
        if not is_positive_even_real_cutoff(cutoff):
            raise ValueError("positive-measure Drude proof needs a real nonnegative even cutoff")
        filtered = []
        for omega, weight in spectral_weights:
            if omega not in cutoff:
                raise ValueError("cutoff is not declared on the tested spectral support")
            filtered.append((omega, weight * cutoff[omega].real))
        return filtered

    filtered_weights = positive_filtered_weights(positive_cutoff)
    assert all(weight >= 0.0 for _omega, weight in filtered_weights)
    assert sum(weight for _omega, weight in filtered_weights) <= sum(
        weight for _omega, weight in spectral_weights
    )

    for bad_cutoff in (sign_changing_cutoff, complex_cutoff, overlarge_cutoff):
        try:
            positive_filtered_weights(bad_cutoff)
        except ValueError:
            pass
        else:
            raise AssertionError("bad cutoff was accepted as preserving positivity")

    signed_filtered_weights = [
        (omega, weight * sign_changing_cutoff[omega].real)
        for omega, weight in spectral_weights
    ]
    assert any(weight < 0.0 for _omega, weight in signed_filtered_weights)

    def finite_complex_total_variation(cutoff: dict[int, complex]) -> float:
        return sum(weight * abs(cutoff[omega]) for omega, weight in spectral_weights)

    complex_filtered_mass = sum(
        weight * complex_cutoff[omega]
        for omega, weight in spectral_weights
    )
    assert abs(complex_filtered_mass) <= finite_complex_total_variation(complex_cutoff)


def check_regular_drude_decomposition_for_figure() -> None:
    sigma_dc = 0.64
    tau = 1.7
    drude_weight = 0.23

    def sigma_regular(omega: float) -> float:
        return sigma_dc / (1.0 + (omega * tau) ** 2)

    for omega in (1.0e-4, 2.0e-4, 5.0e-4):
        rho_regular = 2.0 * omega * sigma_regular(omega)
        assert_close(
            "regular spectral slope gives dc conductivity",
            rho_regular / (2.0 * omega),
            sigma_dc,
            tol=5.0e-7,
        )

    for width in (0.5, 0.25, 0.125):
        # delta_width integrates to one on the real line.  Thus
        # pi*D*delta_width has total weight pi*D and height D/width at zero.
        delta_width_at_zero = 1.0 / (math.pi * width)
        spike_height = math.pi * drude_weight * delta_width_at_zero
        assert_close("Drude Lorentzian height", spike_height, drude_weight / width)
        total_weight = math.pi * drude_weight
        assert total_weight > 0.0
    assert drude_weight / 0.125 > drude_weight / 0.25 > drude_weight / 0.5


def check_mori_zwanzig_projection_identity() -> None:
    """Finite-dimensional projection identity behind the memory equation.

    Take L to be the rotation generator
        L (x, y) = (-omega y, omega x)
    and project onto the x-coordinate.  Eliminating y gives the exact
    projected equation
        x_dot(t) = -omega y0 - omega^2 int_0^t x(s) ds.
    This is the scalar version of the Kubo--Mori/Mori--Zwanzig identity in
    the chapter.
    """

    for omega, x0, y0, time in (
        (0.7, 1.2, -0.4, 0.3),
        (1.3, -0.8, 0.5, 0.9),
        (2.0, 0.6, 1.1, 0.2),
    ):
        cos = math.cos(omega * time)
        sin = math.sin(omega * time)
        x_t = x0 * cos - y0 * sin
        x_dot = -omega * x0 * sin - omega * y0 * cos

        if abs(omega) < 1.0e-14:
            integral_x = x0 * time
        else:
            integral_x = x0 * sin / omega - y0 * (1.0 - cos) / omega
        projected_rhs = -omega * y0 - omega * omega * integral_x
        assert_close("Mori-Zwanzig time-domain identity", x_dot, projected_rhs)

    for omega, z in ((0.7, 1.1), (1.3, 2.4), (2.0, 0.8)):
        laplace_cos = z / (z * z + omega * omega)
        # The projected resolvent is the Schur complement
        # [z - P L P - P L Q (z - Q L Q)^(-1) Q L P]^(-1).
        block_schur = 1.0 / (z + omega * omega / z)
        assert_close("Mori-Zwanzig Schur complement", block_schur, laplace_cos)


def main() -> None:
    check_two_level_kms_and_fdt()
    check_retarded_sign_and_transport_slope()
    check_contact_term_does_not_change_spectral_slope()
    check_hall_block_is_not_positive_dissipative_measure()
    check_vector_potential_response_sign()
    check_diamagnetic_contact_response_convention()
    check_fourier_laplace_abel_domain_relation()
    check_switched_source_endpoint_and_contact_are_load_bearing()
    check_isothermal_not_adiabatic_twist_curvature()
    check_bond_phase_total_twist_normalization()
    check_mazur_projection_and_drude_weight()
    check_commutator_fdt_loses_exact_zero_mode()
    check_periodic_twist_and_open_boundary_drude_routes()
    check_cesaro_abel_not_pointwise_negative_control()
    check_filtered_drude_rejects_uncontrolled_uv_tail()
    check_filtered_drude_cutoff_positivity_contract()
    check_regular_drude_decomposition_for_figure()
    check_mori_zwanzig_projection_identity()
    print("All thermal Kubo convention checks passed.")


if __name__ == "__main__":
    main()
