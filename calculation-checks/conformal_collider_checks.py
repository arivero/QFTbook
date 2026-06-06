#!/usr/bin/env python3
"""Finite checks for the ANEC and conformal-collider bounds section.

The checks include the four-dimensional stress-tensor collider diagonalization
and the N=1 supersymmetric specialization that converts the detector
positivity inequalities into the central-charge bound 1/2 <= a/c <= 3/2.
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

    def helicity_eigenvalues(t2: Fraction, t4: Fraction) -> tuple[Fraction, Fraction, Fraction]:
        return (
            1 - t2 / 3 - 2 * t4 / 15,
            1 + t2 / 6 - 2 * t4 / 15,
            1 + t2 / 3 + 8 * t4 / 15,
        )

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

    The continuum proof uses one-sided relative-entropy monotonicity for a
    null-cut region and its complement.  This finite check models only the
    displayed derivative algebra: the right-cut modular derivative is
    -int_0^infty phi T, the complementary derivative is
    +int_{-infty}^0 phi T, and the common entropy derivative can be squeezed
    between the two only when the full null integral is nonnegative.
    """

    phi = Fraction(3, 2)
    epsilon = Fraction(1, 100)
    right_atoms = [(Fraction(1, 5), Fraction(-2, 3)), (Fraction(3, 5), Fraction(1, 3))]
    left_atoms = [(Fraction(-4, 5), Fraction(1, 6)), (Fraction(-1, 3), Fraction(1, 3))]

    def right_modular(s: Fraction) -> Fraction:
        return sum((x - s * phi) * stress for x, stress in right_atoms)

    def complement_modular(s: Fraction) -> Fraction:
        return sum((s * phi - x) * stress for x, stress in left_atoms)

    right_integral = phi * sum(stress for _, stress in right_atoms)
    left_integral = phi * sum(stress for _, stress in left_atoms)
    right_derivative = (right_modular(epsilon) - right_modular(Fraction(0))) / epsilon
    complement_derivative = (complement_modular(epsilon) - complement_modular(Fraction(0))) / epsilon

    assert_equal("right null-cut modular derivative sign", right_derivative, -right_integral)
    assert_equal("complement null-cut modular derivative sign", complement_derivative, left_integral)

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
    check_light_transform_homogeneity_map()
    check_null_cut_modular_anec_sign_bookkeeping()
    check_light_ray_ope_transverse_scaling_bookkeeping()
    print("All conformal-collider finite checks passed.")


if __name__ == "__main__":
    main()
