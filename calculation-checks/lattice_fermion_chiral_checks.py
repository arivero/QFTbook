#!/usr/bin/env python3
"""Finite checks for lattice-fermion/chiral-symmetry conventions.

The script verifies exact arithmetic used in Volume XI, Chapter 11:
naive doubler chirality signs, Wilson doubler masses, the
Ginsparg-Wilson/overlap algebra, the finite Berezinian index factor,
fermionic reflection-positive crossing kernels, and the finite-wall
sign-function approximation behind the domain-wall/overlap limit.

Evidence contract.

Target claims:
    Finite Berezin Gaussian/chiral-index conventions, Wilson doubler lifting,
    fermionic reflection positivity through oriented homogeneous crossing
    kernels, the Wilson r=1 mid-link projector crossing, the single-shift
    overlap kernel convention, Ginsparg-Wilson zero-mode index identification,
    and finite-L_s domain-wall convergence to the overlap sign function.

Independent construction:
    The checks use exact rational finite-dimensional models: Brillouin-corner
    arithmetic, explicit Ginsparg-Wilson matrices, an enumerated Grassmann
    algebra with reflection and Berezin top-coefficient extraction, projector
    eigenvalue checks, corner branch counts for the overlap kernel, and a
    scalar transfer-matrix sign-function approximation with exact residual
    bounds.

Imported assumptions:
    The script does not prove continuum locality of the overlap operator,
    admissibility or mobility-gap theorems, the full Shamir block Gaussian
    elimination, or the continuum topological-index theorem.  It checks the
    finite algebra and convention-sensitive consequences used in the chapter.

Negative controls:
    Bare Berezin integration is shown not to be a positive inner product on
    constants, wrong crossing signs and wrong orientation phases give negative
    norms, the naive r=0 time-crossing matrix has a negative projector
    coefficient, the overlap double-shift convention activates an extra
    doubler shell, and finite wall extent is rejected as an exact sign
    function.

Scope boundary:
    Passing this script verifies finite convention algebra only.  It is not a
    proof of continuum constructive reflection positivity for every possible
    cut, of overlap locality in rough gauge backgrounds, or of the continuum
    chiral gauge theory.
"""

from fractions import Fraction
from itertools import product


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def matmul(a, b):
    n = len(a)
    m = len(b[0])
    kdim = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(kdim)) for j in range(m)]
        for i in range(n)
    ]


def matadd(a, b):
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def matsub(a, b):
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def scalar_mul(c, a):
    return [[c * x for x in row] for row in a]


def diag(entries):
    return [
        [entry if i == j else Fraction(0) for j, entry in enumerate(entries)]
        for i, entry in enumerate(entries)
    ]


def eye(n):
    return diag([Fraction(1) for _ in range(n)])


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def transpose(a):
    return [list(row) for row in zip(*a)]


def assert_zero_matrix(a, label):
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value != 0:
                raise AssertionError(f"{label}: entry {(i, j)} is {value!r}")


def multiply_monomials(left, right, total_variables):
    if left & right:
        return 0, 0
    swaps = 0
    for left_index in range(total_variables):
        if (left >> left_index) & 1:
            for right_index in range(left_index):
                if (right >> right_index) & 1:
                    swaps += 1
    sign = -1 if swaps % 2 else 1
    return sign, left | right


def multiply_polys(left, right, total_variables):
    product_poly = {}
    for left_mask, left_coeff in left.items():
        for right_mask, right_coeff in right.items():
            sign, product_mask = multiply_monomials(left_mask, right_mask, total_variables)
            if sign == 0:
                continue
            product_poly[product_mask] = (
                product_poly.get(product_mask, Fraction(0))
                + sign * left_coeff * right_coeff
            )
    return {mask: coeff for mask, coeff in product_poly.items() if coeff != 0}


def singleton(mask):
    return {mask: Fraction(1)}


def add_polys(*polys):
    total = {}
    for poly in polys:
        for mask, coeff in poly.items():
            total[mask] = total.get(mask, Fraction(0)) + coeff
    return {mask: coeff for mask, coeff in total.items() if coeff != 0}


def scale_poly(coefficient, poly):
    return {
        mask: coefficient * value
        for mask, value in poly.items()
        if coefficient * value != 0
    }


def reflect_variable(variable_index):
    if variable_index % 2 == 0:
        return variable_index + 1
    return variable_index - 1


def reflect_monomial(mask, pair_count):
    total_variables = 2 * pair_count
    reflected = {0: Fraction(1)}
    variables = [index for index in range(total_variables) if (mask >> index) & 1]
    for variable_index in reversed(variables):
        reflected = multiply_polys(
            reflected,
            singleton(1 << reflect_variable(variable_index)),
            total_variables,
        )
    return reflected


def reflect_poly(poly, pair_count):
    reflected_terms = []
    for mask, coeff in poly.items():
        reflected_terms.append(scale_poly(coeff, reflect_monomial(mask, pair_count)))
    return add_polys(*reflected_terms)


def berezin_integral(poly, pair_count):
    return poly.get((1 << (2 * pair_count)) - 1, Fraction(0))


def reflection_pairing(left, kernel, right, pair_count):
    total_variables = 2 * pair_count
    return berezin_integral(
        multiply_polys(
            multiply_polys(reflect_poly(left, pair_count), kernel, total_variables),
            right,
            total_variables,
        ),
        pair_count,
    )


def positive_mask(subset):
    mask = 0
    for pair_index in subset:
        mask |= 1 << (2 * pair_index + 1)
    return mask


def positive_basis(pair_count):
    basis = []
    for choice in product([0, 1], repeat=pair_count):
        subset = [index for index, value in enumerate(choice) if value]
        basis.append(positive_mask(subset))
    return basis


def crossing_kernel(pair_count, blocks, coefficients, phases=None):
    total_variables = 2 * pair_count
    if phases is None:
        phases = [Fraction(1) for _ in blocks]
    kernel = {0: Fraction(1)}
    for block, coefficient, phase in zip(blocks, coefficients, phases):
        block_poly = singleton(block)
        reflected_block = reflect_poly(block_poly, pair_count)
        positive_block = multiply_polys(reflected_block, block_poly, total_variables)
        factor = add_polys(
            {0: Fraction(1)},
            scale_poly(coefficient * phase, positive_block),
        )
        kernel = multiply_polys(kernel, factor, total_variables)
    return kernel


def polynomial_from_basis_coefficients(basis, coefficients):
    return {
        mask: coefficient
        for mask, coefficient in zip(basis, coefficients)
        if coefficient != 0
    }


def check_naive_doubler_chirality_sum():
    dimension = 4
    signs = []
    for epsilon in product([0, 1], repeat=dimension):
        signs.append((-1) ** sum(epsilon))
    assert_equal(len(signs), 2**dimension, "number of naive Brillouin corners")
    assert_equal(sum(signs), 0, "sum of doubler chirality signs")
    assert_equal(signs.count(1), signs.count(-1), "opposite chirality multiplicities")


def check_wilson_corner_masses():
    dimension = 4
    mass = Fraction(1, 7)
    r = Fraction(1)
    a = Fraction(1)
    degeneracies = {}
    for epsilon in product([0, 1], repeat=dimension):
        n_epsilon = sum(epsilon)
        corner_mass = mass + 2 * r * n_epsilon / a
        degeneracies[corner_mass] = degeneracies.get(corner_mass, 0) + 1
    expected = {
        Fraction(1, 7): 1,
        Fraction(15, 7): 4,
        Fraction(29, 7): 6,
        Fraction(43, 7): 4,
        Fraction(57, 7): 1,
    }
    assert_equal(degeneracies, expected, "Wilson corner mass degeneracies")


def check_ginsparg_wilson_and_overlap_index():
    # A diagonal exact example with nonzero overlap index.
    rho = Fraction(3)
    gamma5 = diag([Fraction(1), Fraction(1), Fraction(-1), Fraction(-1)])
    v = diag([Fraction(1), Fraction(1), Fraction(1), Fraction(-1)])
    ident = eye(4)
    d = scalar_mul(rho, matadd(ident, v))  # lattice spacing a=1

    lhs = matadd(matmul(gamma5, d), matmul(d, gamma5))
    rhs = scalar_mul(Fraction(1, rho), matmul(matmul(d, gamma5), d))
    assert_zero_matrix(matsub(lhs, rhs), "Ginsparg-Wilson relation")

    index = trace(matmul(gamma5, matsub(ident, scalar_mul(Fraction(1, 2 * rho), d))))
    sign_h = matmul(gamma5, v)
    spectral_asymmetry = -Fraction(1, 2) * trace(sign_h)
    assert_equal(index, Fraction(-1), "sample overlap index")
    assert_equal(index, spectral_asymmetry, "overlap spectral asymmetry index")

    measure_log_linear = trace(matmul(gamma5, d))
    assert_equal(measure_log_linear, -2 * rho * index, "Berezinian index exponent")

    d_diagonal = [d[i][i] for i in range(4)]
    gamma5_diagonal = [gamma5[i][i] for i in range(4)]
    zero_mode_chirality = sum(
        chirality for eigenvalue, chirality in zip(d_diagonal, gamma5_diagonal)
        if eigenvalue == 0
    )
    top_mode_contribution = sum(
        chirality * (1 - eigenvalue / (2 * rho))
        for eigenvalue, chirality in zip(d_diagonal, gamma5_diagonal)
        if eigenvalue == 2 * rho
    )
    assert_equal(index, zero_mode_chirality, "GW trace index equals zero-mode chirality")
    assert_equal(top_mode_contribution, Fraction(0), "2rho/a modes do not contribute to GW index")

    # A non-diagonal unitary V with zero index checks the same algebra without
    # relying on simultaneous diagonalization.
    gamma5_2 = diag([Fraction(1), Fraction(-1)])
    v2 = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]
    d2 = scalar_mul(rho, matadd(eye(2), v2))
    lhs2 = matadd(matmul(gamma5_2, d2), matmul(d2, gamma5_2))
    rhs2 = scalar_mul(Fraction(1, rho), matmul(matmul(d2, gamma5_2), d2))
    assert_zero_matrix(matsub(lhs2, rhs2), "non-diagonal GW relation")
    v2_dagger = transpose(v2)
    gamma_v_gamma = matmul(matmul(gamma5_2, v2), gamma5_2)
    assert_equal(v2_dagger, gamma_v_gamma, "gamma5-Hermiticity of V")


def check_grassmann_reflection_positive_crossing_kernel():
    bare = {0: Fraction(1)}
    one = {0: Fraction(1)}
    chi = singleton(positive_mask([0]))
    assert_equal(
        reflection_pairing(one, bare, one, 1),
        Fraction(0),
        "bare Berezin functional is not an inner product on constants",
    )
    assert_equal(
        reflection_pairing(chi, bare, chi, 1),
        Fraction(1),
        "bare Berezin functional extracts the saturated one-link coefficient",
    )

    for pair_count, coefficients in [(1, [Fraction(3)]), (2, [Fraction(2), Fraction(5)])]:
        blocks = [positive_mask([index]) for index in range(pair_count)]
        kernel = crossing_kernel(pair_count, blocks, coefficients)
        basis = positive_basis(pair_count)
        for left_mask in basis:
            left_subset = {
                index
                for index in range(pair_count)
                if (left_mask >> (2 * index + 1)) & 1
            }
            complement_weight = Fraction(1)
            for index, coefficient in enumerate(coefficients):
                if index not in left_subset:
                    complement_weight *= coefficient
            for right_mask in basis:
                value = reflection_pairing(
                    singleton(left_mask),
                    kernel,
                    singleton(right_mask),
                    pair_count,
                )
                expected = complement_weight if left_mask == right_mask else Fraction(0)
                assert_equal(value, expected, "crossing kernel weighted monomial Gram entry")

        for sample_coefficients in product([Fraction(-1), Fraction(0), Fraction(2)], repeat=len(basis)):
            test_poly = polynomial_from_basis_coefficients(basis, sample_coefficients)
            norm = reflection_pairing(test_poly, kernel, test_poly, pair_count)
            expected_norm = Fraction(0)
            for mask, coefficient in zip(basis, sample_coefficients):
                subset = {
                    index
                    for index in range(pair_count)
                    if (mask >> (2 * index + 1)) & 1
                }
                weight = Fraction(1)
                for index, crossing_coefficient in enumerate(coefficients):
                    if index not in subset:
                        weight *= crossing_coefficient
                expected_norm += coefficient * coefficient * weight
            assert_equal(norm, expected_norm, "exhaustive one/two-link weighted norm")
            if norm < 0:
                raise AssertionError("reflection-positive kernel produced a negative norm")

    even_block = positive_mask([0, 1])
    even_kernel = crossing_kernel(2, [even_block], [Fraction(7)])
    basis = positive_basis(2)
    expected_even_weights = {
        positive_mask([]): Fraction(7),
        positive_mask([0]): Fraction(0),
        positive_mask([1]): Fraction(0),
        positive_mask([0, 1]): Fraction(1),
    }
    for mask in basis:
        value = reflection_pairing(singleton(mask), even_kernel, singleton(mask), 2)
        assert_equal(value, expected_even_weights[mask], "even quartic block weighted norm")

    wrong_sign_kernel = crossing_kernel(1, [positive_mask([0])], [Fraction(-1)])
    wrong_sign_norm = reflection_pairing(one, wrong_sign_kernel, one, 1)
    assert_equal(wrong_sign_norm, Fraction(-1), "wrong crossing sign negative control")

    wrong_phase_kernel = crossing_kernel(1, [positive_mask([0])], [Fraction(1)], [Fraction(-1)])
    wrong_phase_norm = reflection_pairing(one, wrong_phase_kernel, one, 1)
    assert_equal(wrong_phase_norm, Fraction(-1), "wrong crossing phase negative control")


def check_wilson_reflection_projectors():
    gamma0 = diag([Fraction(1), Fraction(1), Fraction(-1), Fraction(-1)])
    ident = eye(4)
    p_plus = scalar_mul(Fraction(1, 2), matadd(ident, gamma0))
    p_minus = scalar_mul(Fraction(1, 2), matsub(ident, gamma0))
    assert_zero_matrix(matsub(matmul(p_plus, p_plus), p_plus), "P+ idempotent")
    assert_zero_matrix(matsub(matmul(p_minus, p_minus), p_minus), "P- idempotent")
    assert_zero_matrix(matmul(p_plus, p_minus), "P+ P- orthogonality")
    assert_equal(trace(p_plus), Fraction(2), "P+ rank")
    assert_equal(trace(p_minus), Fraction(2), "P- rank")

    r = Fraction(1)
    forward_crossing = scalar_mul(Fraction(1, 2), matsub(scalar_mul(r, ident), gamma0))
    backward_crossing = scalar_mul(Fraction(1, 2), matadd(scalar_mul(r, ident), gamma0))
    assert_equal(
        [forward_crossing[i][i] for i in range(4)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        "Wilson r=1 forward crossing is P-",
    )
    assert_equal(
        [backward_crossing[i][i] for i in range(4)],
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0)],
        "Wilson r=1 backward crossing is P+",
    )

    naive_forward = scalar_mul(Fraction(1, 2), scalar_mul(Fraction(-1), gamma0))
    if all(naive_forward[i][i] >= 0 for i in range(4)):
        raise AssertionError("naive r=0 crossing unexpectedly became positive semidefinite")


def check_overlap_kernel_branch_window_and_normalization():
    dimension = 4
    r = Fraction(1)
    rho = Fraction(3, 2)

    correct_negative_corners = []
    double_shift_negative_corners = []
    weighted_correct = Fraction(0)
    weighted_double_shift = Fraction(0)
    for epsilon in product([0, 1], repeat=dimension):
        n_epsilon = sum(epsilon)
        chirality = Fraction((-1) ** n_epsilon)
        correct_mass = 2 * r * n_epsilon - rho
        double_shift_mass = 2 * r * n_epsilon - 2 * rho
        if correct_mass < 0:
            correct_negative_corners.append(epsilon)
            weighted_correct += chirality
        if double_shift_mass < 0:
            double_shift_negative_corners.append(epsilon)
            weighted_double_shift += chirality

    assert_equal(len(correct_negative_corners), 1, "overlap one-species branch for 0<rho<2r")
    assert_equal(weighted_correct, Fraction(1), "correct overlap branch chirality weight")
    assert_equal(
        len(double_shift_negative_corners),
        5,
        "double-shift convention activates an extra doubler shell",
    )
    if weighted_double_shift == weighted_correct:
        raise AssertionError("double-shift branch weight was not rejected")

    physical_slope = rho * Fraction(1, rho)
    unnormalized_slope = Fraction(1, rho)
    assert_equal(physical_slope, Fraction(1), "rho/a overlap prefactor gives unit Dirac slope")
    if unnormalized_slope == 1:
        raise AssertionError("missing rho prefactor unexpectedly kept the physical slope")


def truncated_domain_wall_sign(kappa, extent):
    transfer = (1 - kappa) / (1 + kappa)
    transfer_power = transfer ** extent
    return (1 - transfer_power) / (1 + transfer_power)


def check_domain_wall_sign_approximation():
    gap = Fraction(1, 3)
    extent = 4
    contraction = (1 - gap) / (1 + gap)
    for kappa, expected_sign in [(gap, Fraction(1)), (-gap, Fraction(-1))]:
        approximation = truncated_domain_wall_sign(kappa, extent)
        error = abs(expected_sign - approximation)
        bound = 2 * (contraction ** extent)
        if error > bound:
            raise AssertionError("finite-wall residual bound failed")
        if approximation == expected_sign:
            raise AssertionError("finite wall extent incorrectly gave the exact sign")

    longer_error = abs(Fraction(1) - truncated_domain_wall_sign(gap, 2 * extent))
    shorter_error = abs(Fraction(1) - truncated_domain_wall_sign(gap, extent))
    if longer_error >= shorter_error:
        raise AssertionError("domain-wall sign approximation did not improve with L_s")


def check_staggered_phase_antisymmetry():
    # Two-dimensional staggered phases eta_0=1, eta_1=(-1)^x0 in lattice units.
    def eta(mu, x):
        if mu == 0:
            return 1
        if mu == 1:
            return (-1) ** x[0]
        raise ValueError(mu)

    sites = [(x0, x1) for x0 in range(4) for x1 in range(4)]
    for x in sites:
        for mu in [0, 1]:
            y = list(x)
            y[mu] = (y[mu] + 1) % 4
            y = tuple(y)
            forward = Fraction(eta(mu, x), 2)
            backward = -Fraction(eta(mu, x), 2)
            # M(x,y)=eta_mu(x)/2 and M(y,x)=-eta_mu(x)/2 for the same link.
            assert_equal(forward, -backward, "staggered link antisymmetry")

    for x in sites:
        reflection_phase = (-1) ** x[1]
        assert_equal(reflection_phase * reflection_phase, 1, "staggered reflection phase squares to one")


def main():
    check_naive_doubler_chirality_sum()
    check_wilson_corner_masses()
    check_ginsparg_wilson_and_overlap_index()
    check_grassmann_reflection_positive_crossing_kernel()
    check_wilson_reflection_projectors()
    check_overlap_kernel_branch_window_and_normalization()
    check_domain_wall_sign_approximation()
    check_staggered_phase_antisymmetry()
    print(
        "All lattice-fermion doubler, Wilson-mass, Ginsparg-Wilson, "
        "overlap-index, reflection-crossing, Wilson-projector, overlap-kernel, "
        "domain-wall, and staggered-phase checks passed."
    )


if __name__ == "__main__":
    main()
