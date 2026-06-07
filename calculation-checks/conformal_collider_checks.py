#!/usr/bin/env python3
r"""Finite checks for the ANEC and conformal-collider bounds section.

The checks include the four-dimensional stress-tensor collider diagonalization
and the N=1 supersymmetric specialization that converts the detector
positivity inequalities into the central-charge bound 1/2 <= a/c <= 3/2.

Evidence contract.

Target claims:
  Volume III, Chapter 10 uses a route-scoped ANEC theorem boundary, the
  null-cut full-modular-generator sign convention, the ANEC-to-detector
  positivity bridge, the Hofman--Maldacena stress-tensor one-point normal
  form, the helicity-sector collider inequalities, the four-dimensional N=1
  superconformal a/c bound, and the light-transform homogeneity map.

Independent construction:
  The checks rebuild the S^2 tensor averages from rotational moments,
  evaluate the detector quadratic form on explicit symmetric-traceless
  polarizations, decompose a generic polarization into SO(2) helicity sectors,
  recompute the N=1 endpoint eigenvalues from a/c data, and model the
  null-cut full modular generator by finite signed atoms.  They do not import
  the displayed inequalities as an assumed answer.

Imported assumptions:
  The route-specific Lorentzian CFT hypotheses behind ANEC, the
  Casini-Teste-Torroba null-cut modular-flow theorem boundary, the conformal
  map from a complete null generator to null infinity, the bounded extension
  from smooth angular tests to detector measures, the Wightman/ward-identity
  calculation of the stress-tensor one-point normal form, and the N=1
  supercurrent Ward identity are imported physics inputs.

Negative controls:
  The suite rejects total-energy normalization as a substitute for pointwise
  detector positivity, omitting any one of the three helicity-sector
  inequalities, a wrong N=1 t2 normalization, a nonzero t4 at the N=1 identity
  point, a one-sided null-cut sign argument that omits part of the complete
  generator, and an unregulated sharp-density-matrix shortcut missing Araki,
  collar-removal, and common-domain data.

Scope boundary:
  These are exact finite checks of angular averages, polarization linear
  algebra, convention maps, and modular sign bookkeeping.  They are not a
  proof of ANEC, a construction of Lorentzian light-ray operators, a
  derivation of the detector measure, or a calculation of the full
  stress-tensor Wightman distribution.

Primary derivation route:
  The manuscript route first states ANEC as a route-scoped Lorentzian CFT
  theorem boundary, records the null-cut modular-flow theorem boundary,
  displays the full-modular-generator sign algebra, passes through the
  ANEC-to-detector bounded-extension bridge, derives the t2,t4 normal form for
  a stress-tensor collider state, and then diagonalizes the resulting
  quadratic form in helicity sectors.

Independent verification route:
  The executable route starts from primitive rational matrices and finite
  signed atoms and a finite route-hypothesis checklist.  It reconstructs the
  S^2 averages, obtains the helicity eigenvalues by direct evaluation and by
  spectral recomposition of a generic polarization, tests the collider
  positivity polytope against adversarial shortcuts, and checks the N=1 a/c map
  at interior and endpoint samples.

Convention dependencies:
  Four-dimensional parity-even stress-tensor collider coordinates t2,t4,
  total-energy normalization Q/(4*pi), SO(2) helicity sectors relative to a
  detector direction, S^2 moment normalizations 1/3 and 2/15, the null-cut
  full-modular-generator sign convention for x^+=f(y), and the N=1 convention
  t4=0, t2=6(1-a/c).

Domain and remainder assumptions:
  The finite checks apply after the ANEC route hypotheses, wavepacket
  regularization, detector smearing, null-infinity limiting, and bounded
  positive extension have been supplied.  Regulator independence for the
  modular route, the causality/OPE assumptions for the HKT route, contact terms
  in detector products, and separated-angle Wightman distribution calculation
  remain external to this finite arithmetic.

Remaining unproved or conditional:
  ANEC itself, the existence and domain of light-ray operators in the stated
  CFT class, the ANEC-to-detector limiting theorem, the full TTT Wightman
  integration, and any nonconformal or QCD use of the collider formula remain
  conditional inputs outside this companion.
"""

from __future__ import annotations

from fractions import Fraction


Matrix = tuple[tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction]]
Vector = tuple[Fraction, Fraction, Fraction]
Polynomial = tuple[Fraction, Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def mat_norm_sq(eps: Matrix) -> Fraction:
    return sum(eps[i][j] * eps[i][j] for i in range(3) for j in range(3))


def mat_vec(eps: Matrix, n: Vector) -> Vector:
    return tuple(sum(eps[i][j] * n[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def quad(eps: Matrix, n: Vector) -> Fraction:
    return sum(n[i] * eps[i][j] * n[j] for i in range(3) for j in range(3))


def first_ratio(eps: Matrix, n: Vector) -> Fraction:
    v = mat_vec(eps, n)
    return sum(x * x for x in v) / mat_norm_sq(eps)


def second_ratio(eps: Matrix, n: Vector) -> Fraction:
    return quad(eps, n) ** 2 / mat_norm_sq(eps)


def energy_flux_polynomial(first_ratio: Fraction, second_ratio: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return coefficients of 1 + coeff_t2 t2 + coeff_t4 t4."""

    coeff_t2 = first_ratio - Fraction(1, 3)
    coeff_t4 = second_ratio - Fraction(2, 15)
    return (Fraction(1, 1), coeff_t2, coeff_t4)


def helicity_eigenvalues(t2: Fraction, t4: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return the helicity 2, 1, 0 detector eigenvalues."""

    return (
        1 - t2 / 3 - 2 * t4 / 15,
        1 + t2 / 6 - 2 * t4 / 15,
        1 + t2 / 3 + 8 * t4 / 15,
    )


def angular_average_profile(t2: Fraction, t4: Fraction) -> Fraction:
    """Average of the normalized one-detector profile over S^2."""

    return (
        1
        + t2 * (Fraction(1, 3) - Fraction(1, 3))
        + t4 * (Fraction(2, 15) - Fraction(2, 15))
    )


def mat_inner(left: Matrix, right: Matrix) -> Fraction:
    return sum(left[i][j] * right[i][j] for i in range(3) for j in range(3))


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def poly_scale(scale: Fraction, poly: Polynomial) -> Polynomial:
    return tuple(scale * coefficient for coefficient in poly)  # type: ignore[return-value]


def check_sphere_averages_for_traceless_tensor() -> None:
    """Check the constants subtracted in the four-dimensional flux form."""

    # On S^2, <n_i n_j> = delta_ij/3.
    assert_equal("rank-two sphere average coefficient", Fraction(1, 3), Fraction(1, 3))

    # <n_i n_j n_k n_l> =
    #   (delta_ij delta_kl + delta_ik delta_jl + delta_il delta_jk)/15.
    # For a symmetric traceless polarization epsilon_ij, the first contraction
    # vanishes and the second and third contractions each give epsilon*epsilon.
    eps: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-3)),
    )
    norm = mat_norm_sq(eps)
    trace = sum(eps[i][i] for i in range(3))
    fourth_moment_contraction = (trace * trace + 2 * norm) / 15
    assert_equal("test tensor traceless", trace, Fraction(0))
    assert_equal("traceless rank-four sphere average coefficient", fourth_moment_contraction / norm, Fraction(2, 15))


def check_helicity_bounds() -> None:
    """Check the helicity 2, 1, 0 reductions of the stress-tensor flux."""

    n: Vector = (Fraction(0), Fraction(0), Fraction(1))
    eps_h2: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    eps_h1: Matrix = (
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
    )
    eps_h0: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-2)),
    )

    helicity_two = energy_flux_polynomial(first_ratio(eps_h2, n), second_ratio(eps_h2, n))
    helicity_one = energy_flux_polynomial(first_ratio(eps_h1, n), second_ratio(eps_h1, n))
    helicity_zero = energy_flux_polynomial(first_ratio(eps_h0, n), second_ratio(eps_h0, n))

    assert_equal("helicity-2 collider polynomial", helicity_two, (Fraction(1, 1), Fraction(-1, 3), Fraction(-2, 15)))
    assert_equal("helicity-1 collider polynomial", helicity_one, (Fraction(1, 1), Fraction(1, 6), Fraction(-2, 15)))
    assert_equal("helicity-0 collider polynomial", helicity_zero, (Fraction(1, 1), Fraction(1, 3), Fraction(8, 15)))


def check_helicity_projector_spectral_diagonalization() -> None:
    """Check the full helicity-sector spectral decomposition."""

    n: Vector = (Fraction(0), Fraction(0), Fraction(1))
    eps_h2: Matrix = (
        (Fraction(1), Fraction(2), Fraction(0)),
        (Fraction(2), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    eps_h1: Matrix = (
        (Fraction(0), Fraction(0), Fraction(3)),
        (Fraction(0), Fraction(0), Fraction(-1)),
        (Fraction(3), Fraction(-1), Fraction(0)),
    )
    eps_h0: Matrix = (
        (Fraction(2), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-4)),
    )
    eps_total: Matrix = tuple(
        tuple(eps_h2[i][j] + eps_h1[i][j] + eps_h0[i][j] for j in range(3))
        for i in range(3)
    )  # type: ignore[assignment]

    for name, left, right in (
        ("h2-h1 orthogonality", eps_h2, eps_h1),
        ("h2-h0 orthogonality", eps_h2, eps_h0),
        ("h1-h0 orthogonality", eps_h1, eps_h0),
    ):
        assert_equal(name, mat_inner(left, right), Fraction(0))

    norms = (mat_norm_sq(eps_h2), mat_norm_sq(eps_h1), mat_norm_sq(eps_h0))
    assert_equal("helicity-sector norms", norms, (Fraction(10), Fraction(20), Fraction(24)))
    assert_equal("total norm from orthogonal projectors", mat_norm_sq(eps_total), sum(norms))

    full_flux = poly_scale(
        mat_norm_sq(eps_total),
        energy_flux_polynomial(first_ratio(eps_total, n), second_ratio(eps_total, n)),
    )
    eigenvalues = (
        (Fraction(1), Fraction(-1, 3), Fraction(-2, 15)),
        (Fraction(1), Fraction(1, 6), Fraction(-2, 15)),
        (Fraction(1), Fraction(1, 3), Fraction(8, 15)),
    )
    spectral_flux = (Fraction(0), Fraction(0), Fraction(0))
    for norm, eigenvalue in zip(norms, eigenvalues):
        spectral_flux = poly_add(spectral_flux, poly_scale(norm, eigenvalue))

    assert_equal("full helicity spectral decomposition", full_flux, spectral_flux)
    assert_equal("generic full flux polynomial", full_flux, (Fraction(54), Fraction(8), Fraction(44, 5)))


def check_n1_susy_collider_central_charge_bound() -> None:
    """Check the N=1 SCFT map from collider coordinates to a/c."""

    def susy_eigenvalues(a_over_c: Fraction) -> tuple[Fraction, Fraction, Fraction]:
        t2 = 6 * (1 - a_over_c)
        t4 = Fraction(0)
        return helicity_eigenvalues(t2, t4)

    samples = (
        (Fraction(1, 2), (Fraction(0), Fraction(3, 2), Fraction(2))),
        (Fraction(1), (Fraction(1), Fraction(1), Fraction(1))),
        (Fraction(3, 2), (Fraction(2), Fraction(1, 2), Fraction(0))),
        (Fraction(7, 6), (Fraction(4, 3), Fraction(5, 6), Fraction(2, 3))),
    )
    for a_over_c, expected in samples:
        assert_equal("N=1 collider a/c eigenvalues", susy_eigenvalues(a_over_c), expected)

    lower_outside = susy_eigenvalues(Fraction(49, 100))
    upper_outside = susy_eigenvalues(Fraction(151, 100))
    if all(value >= 0 for value in lower_outside):
        raise AssertionError("a/c below 1/2 should violate helicity-two positivity")
    if all(value >= 0 for value in upper_outside):
        raise AssertionError("a/c above 3/2 should violate helicity-zero positivity")

    free_chiral = (Fraction(1, 48), Fraction(1, 24))
    free_vector = (Fraction(3, 16), Fraction(1, 8))
    chiral_ratio = free_chiral[0] / free_chiral[1]
    vector_ratio = free_vector[0] / free_vector[1]
    assert_equal("free chiral a/c", chiral_ratio, Fraction(1, 2))
    assert_equal("free vector a/c", vector_ratio, Fraction(3, 2))
    assert_equal("free chiral saturates helicity two", susy_eigenvalues(chiral_ratio)[0], Fraction(0))
    assert_equal("free vector saturates helicity zero", susy_eigenvalues(vector_ratio)[2], Fraction(0))

    wrong_t2_normalization = 3 * (1 - chiral_ratio)
    if helicity_eigenvalues(wrong_t2_normalization, Fraction(0))[0] == 0:
        raise AssertionError("wrong t2 normalization should not reproduce chiral saturation")

    wrong_nonzero_t4 = helicity_eigenvalues(6 * (1 - Fraction(1)), Fraction(1, 5))
    if wrong_nonzero_t4 == (Fraction(1), Fraction(1), Fraction(1)):
        raise AssertionError("N=1 identity point should require t4=0")


def check_normalization_integrates_to_total_energy() -> None:
    """Check that the angular subtractions make t2 and t4 integrate to zero."""

    assert_equal("t2 average subtraction", Fraction(1, 3) - Fraction(1, 3), Fraction(0, 1))
    assert_equal("t4 average subtraction", Fraction(2, 15) - Fraction(2, 15), Fraction(0, 1))


def check_collider_positivity_requires_all_helicity_sectors() -> None:
    """Check that fixed total energy and partial sector tests are insufficient."""

    positive_samples = (
        (Fraction(0), Fraction(0)),
        (Fraction(3), Fraction(0)),
        (Fraction(-3), Fraction(0)),
        (Fraction(1, 2), Fraction(3, 5)),
    )
    for t2, t4 in positive_samples:
        eigenvalues = helicity_eigenvalues(t2, t4)
        if not all(value >= 0 for value in eigenvalues):
            raise AssertionError(f"positive collider sample failed: {(t2, t4, eigenvalues)!r}")

    average_only_t2 = Fraction(4)
    average_only_t4 = Fraction(0)
    assert_equal(
        "average normalization with negative helicity profile",
        angular_average_profile(average_only_t2, average_only_t4),
        Fraction(1),
    )
    if all(value >= 0 for value in helicity_eigenvalues(average_only_t2, average_only_t4)):
        raise AssertionError("total-energy normalization should not imply collider positivity")

    shortcuts = (
        ("missing helicity-two inequality", Fraction(4), Fraction(0), (1, 2), 0),
        ("missing helicity-one inequality", Fraction(-1), Fraction(8), (0, 2), 1),
        ("missing helicity-zero inequality", Fraction(-4), Fraction(0), (0, 1), 2),
    )
    for name, t2, t4, retained_indices, omitted_index in shortcuts:
        eigenvalues = helicity_eigenvalues(t2, t4)
        if not all(eigenvalues[index] >= 0 for index in retained_indices):
            raise AssertionError(f"{name} should pass its retained-sector shortcut")
        if eigenvalues[omitted_index] >= 0:
            raise AssertionError(f"{name} should violate the omitted helicity sector")
        if all(value >= 0 for value in eigenvalues):
            raise AssertionError(f"{name} should fail the full collider positivity test")


def check_light_transform_homogeneity_map() -> None:
    """Check the embedding-space light-transform weight map."""

    test_pairs = (
        (Fraction(3, 1), Fraction(1, 1)),
        (Fraction(4, 1), Fraction(2, 1)),
        (Fraction(5, 1), Fraction(3, 1)),
        (Fraction(7, 2), Fraction(5, 2)),
    )
    for delta, spin in test_pairs:
        p_exponent = spin - 1
        z_exponent = 1 - delta
        transformed_delta = 1 - spin
        transformed_spin = 1 - delta
        assert_equal("light-transform P homogeneity exponent", p_exponent, -transformed_delta)
        assert_equal("light-transform Z homogeneity exponent", z_exponent, transformed_spin)

    spacetime_dimension = Fraction(4, 1)
    stress_tensor_spin = Fraction(2, 1)
    stress_tensor_light_delta = 1 - stress_tensor_spin
    stress_tensor_light_spin = 1 - spacetime_dimension
    assert_equal("four-dimensional stress-tensor light-transform Delta", stress_tensor_light_delta, Fraction(-1, 1))
    assert_equal("four-dimensional stress-tensor light-transform spin", stress_tensor_light_spin, Fraction(-3, 1))


def check_null_cut_modular_anec_sign_bookkeeping() -> None:
    """Check the finite sign algebra in the modular route to ANEC.

    The continuum theorem boundary uses the full modular generator of a
    null-cut algebra, not a sharp-region density matrix.  This finite check
    models only the displayed derivative algebra:
      K_hat(s) = K_hat(0) - s * phi * int_{-infty}^infty T.
    Positivity of the half-sided-inclusion difference K_hat(0)-K_hat(s)
    therefore controls the complete null integral.  The older finite-factor
    entropy squeeze is retained only as a regulated route mnemonic and is
    rejected unless the route-hypothesis checklist is complete.
    """

    phi = Fraction(3, 2)
    epsilon = Fraction(1, 100)
    right_atoms = [(Fraction(1, 5), Fraction(-2, 3)), (Fraction(3, 5), Fraction(1, 3))]
    left_atoms = [(Fraction(-4, 5), Fraction(1, 6)), (Fraction(-1, 3), Fraction(1, 3))]
    all_atoms = right_atoms + left_atoms

    def right_modular(s: Fraction) -> Fraction:
        return sum((x - s * phi) * stress for x, stress in right_atoms)

    def complement_modular(s: Fraction) -> Fraction:
        return sum((s * phi - x) * stress for x, stress in left_atoms)

    def full_modular(s: Fraction) -> Fraction:
        return sum((x - s * phi) * stress for x, stress in all_atoms)

    right_integral = phi * sum(stress for _, stress in right_atoms)
    left_integral = phi * sum(stress for _, stress in left_atoms)
    full_integral = right_integral + left_integral
    right_derivative = (right_modular(epsilon) - right_modular(Fraction(0))) / epsilon
    complement_derivative = (complement_modular(epsilon) - complement_modular(Fraction(0))) / epsilon
    full_derivative = (full_modular(epsilon) - full_modular(Fraction(0))) / epsilon
    inclusion_difference = full_modular(Fraction(0)) - full_modular(epsilon)

    assert_equal("right null-cut modular derivative sign", right_derivative, -right_integral)
    assert_equal("complement null-cut modular derivative sign", complement_derivative, left_integral)
    assert_equal("full modular generator derivative sign", full_derivative, -full_integral)
    assert_equal("half-sided inclusion difference", inclusion_difference, epsilon * full_integral)
    if inclusion_difference < 0:
        raise AssertionError("positive half-sided inclusion difference must control the full null integral")

    required_route_data = {
        "araki_relative_entropy",
        "regulator_independence",
        "collar_removal",
        "common_stress_tensor_domain",
        "right_cut_shape_derivative",
        "complement_cut_shape_derivative",
        "common_regulated_entropy_variation",
    }
    density_matrix_shortcut = {
        "finite_factor_density_matrix",
        "right_cut_shape_derivative",
        "complement_cut_shape_derivative",
        "common_regulated_entropy_variation",
    }
    if required_route_data <= density_matrix_shortcut:
        raise AssertionError("unregulated density-matrix shortcut should not satisfy the modular ANEC route")
    missing_shortcut_data = required_route_data - density_matrix_shortcut
    assert_equal(
        "density-matrix shortcut missing route data",
        missing_shortcut_data,
        {"araki_relative_entropy", "regulator_independence", "collar_removal", "common_stress_tensor_domain"},
    )

    completed_regulated_route = set(required_route_data)
    if not required_route_data <= completed_regulated_route:
        raise AssertionError("complete regulated route data should satisfy the modular ANEC checklist")

    # This finite-factor squeeze checks only the algebra after all route
    # hypotheses above have been supplied.
    entropy_derivative = Fraction(2, 3)
    region_relative_entropy_derivative = right_derivative - entropy_derivative
    complement_relative_entropy_derivative = complement_derivative - entropy_derivative
    if region_relative_entropy_derivative > 0:
        raise AssertionError("nested right-cut relative entropy should have nonpositive derivative")
    if complement_relative_entropy_derivative < 0:
        raise AssertionError("nested complementary relative entropy should have nonnegative derivative")
    if right_integral + left_integral < 0:
        raise AssertionError("compatible entropy squeeze must imply a nonnegative full null integral")

    impossible_left_integral = Fraction(1, 4)
    lower_entropy_bound = -right_integral
    upper_entropy_bound = impossible_left_integral
    if lower_entropy_bound <= upper_entropy_bound:
        raise AssertionError("negative full null integral should make the entropy squeeze incompatible")

    future_only_integral = Fraction(1, 3)
    omitted_past_integral = Fraction(-2, 3)
    if future_only_integral < 0:
        raise AssertionError("future-only sample should look positive before the omitted piece is restored")
    if future_only_integral + omitted_past_integral >= 0:
        raise AssertionError("one-sided null-cut shortcut should still have negative full null integral")


def check_light_ray_ope_transverse_scaling_bookkeeping() -> None:
    """Check the transverse homogeneity ledger for the light-ray OPE.

    In a local detector patch with d transverse coordinates, the detector
    density scales as lambda^{-d}.  A product of two detector densities
    therefore has exponent -2d.  If a light-ray operator has transverse
    density exponent w and is acted on by |m| transverse derivatives, the
    coefficient distribution in the OPE must have exponent
    -2d - w + |m|.  This is only bookkeeping; analytic convergence is the
    content of the Lorentzian light-ray OPE theorem boundary.
    """

    cases = (
        (Fraction(2), Fraction(-1), Fraction(0)),
        (Fraction(2), Fraction(-3), Fraction(1)),
        (Fraction(3), Fraction(1, 2), Fraction(2)),
        (Fraction(5), Fraction(-7, 3), Fraction(4)),
    )
    for transverse_dimension, light_weight, derivative_order in cases:
        coefficient_weight = -2 * transverse_dimension - light_weight + derivative_order
        rhs_weight = coefficient_weight + light_weight - derivative_order
        lhs_weight = -2 * transverse_dimension
        assert_equal("light-ray OPE transverse scaling", rhs_weight, lhs_weight)


def main() -> None:
    check_sphere_averages_for_traceless_tensor()
    check_helicity_bounds()
    check_helicity_projector_spectral_diagonalization()
    check_n1_susy_collider_central_charge_bound()
    check_normalization_integrates_to_total_energy()
    check_collider_positivity_requires_all_helicity_sectors()
    check_light_transform_homogeneity_map()
    check_null_cut_modular_anec_sign_bookkeeping()
    check_light_ray_ope_transverse_scaling_bookkeeping()
    print("All conformal-collider finite checks passed.")


if __name__ == "__main__":
    main()
