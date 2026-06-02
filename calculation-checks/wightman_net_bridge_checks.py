#!/usr/bin/env python3
"""Finite checks for the Wightman-to-local-net comparison discussion.

The script verifies only the bounded finite-dimensional algebra used as a
diagnostic in Volume IV, Chapter 3.  It does not assert any general
Wightman-to-AQFT theorem.
"""

from __future__ import annotations

from fractions import Fraction

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
MatrixAny = tuple[tuple[Fraction, ...], ...]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def add(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] + b[0][0], a[0][1] + b[0][1]),
        (a[1][0] + b[1][0], a[1][1] + b[1][1]),
    )


def sub(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] - b[0][0], a[0][1] - b[0][1]),
        (a[1][0] - b[1][0], a[1][1] - b[1][1]),
    )


def scale(c: Fraction, a: Matrix) -> Matrix:
    return ((c * a[0][0], c * a[0][1]), (c * a[1][0], c * a[1][1]))


def comm(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def assert_eq(got: Matrix, expected: Matrix, msg: str) -> None:
    if got != expected:
        raise AssertionError(f"{msg}: got {got}, expected {expected}")


def matmul_any(a: MatrixAny, b: MatrixAny) -> MatrixAny:
    rows = len(a)
    middle = len(b)
    cols = len(b[0])
    return tuple(
        tuple(sum(a[i][r] * b[r][j] for r in range(middle)) for j in range(cols))
        for i in range(rows)
    )


def add_any(a: MatrixAny, b: MatrixAny) -> MatrixAny:
    return tuple(
        tuple(x + y for x, y in zip(row_a, row_b))
        for row_a, row_b in zip(a, b)
    )


def sub_any(a: MatrixAny, b: MatrixAny) -> MatrixAny:
    return tuple(
        tuple(x - y for x, y in zip(row_a, row_b))
        for row_a, row_b in zip(a, b)
    )


def scale_any(c: Fraction, a: MatrixAny) -> MatrixAny:
    return tuple(tuple(c * x for x in row) for row in a)


def kron(a: MatrixAny, b: MatrixAny) -> MatrixAny:
    return tuple(
        tuple(a_i_j * b_row_entry for a_i_j in a_row for b_row_entry in b_row)
        for a_row in a
        for b_row in b
    )


def conjugate_by_involution(unitary: MatrixAny, a: MatrixAny) -> MatrixAny:
    return matmul_any(matmul_any(unitary, a), unitary)


def comm_any(a: MatrixAny, b: MatrixAny) -> MatrixAny:
    return sub_any(matmul_any(a, b), matmul_any(b, a))


def assert_eq_any(got: MatrixAny, expected: MatrixAny, msg: str) -> None:
    if got != expected:
        raise AssertionError(f"{msg}: got {got}, expected {expected}")


def off_diagonal_entries(a: MatrixAny) -> list[Fraction]:
    return [a[i][j] for i in range(len(a)) for j in range(len(a)) if i != j]


def zero_matrix(n: int) -> MatrixAny:
    return tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))


def diagonal_matrix(values: list[Fraction]) -> MatrixAny:
    return tuple(
        tuple(value if i == j else Fraction(0) for j, value in enumerate(values))
        for i, value in enumerate(values)
    )


def diagonal_spectral_projection(values: list[Fraction], eigenvalue: Fraction) -> MatrixAny:
    return diagonal_matrix([
        Fraction(1) if value == eigenvalue else Fraction(0)
        for value in values
    ])


zero: Matrix = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
one: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
parity: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))
odd_field: Matrix = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0)))

half = Fraction(1, 2)
proj_plus = scale(half, add(one, odd_field))
proj_minus = scale(half, sub(one, odd_field))
even_plus = scale(half, add(one, parity))
even_minus = scale(half, sub(one, parity))


def average_over_z2(a: Matrix) -> Matrix:
    """Conditional expectation onto the fixed-point algebra."""
    return scale(half, add(a, matmul(matmul(parity, a), parity)))


def average_over_diagonal_z2(a: MatrixAny) -> MatrixAny:
    """Conditional expectation for the diagonal parity action on two regions."""
    diagonal_parity = kron(parity, parity)
    return scale_any(half, add_any(a, conjugate_by_involution(diagonal_parity, a)))


def span_coefficients(a: Matrix) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return coefficients in the basis 1, P, X, PX."""
    px = matmul(parity, odd_field)
    # For [[a,b],[c,d]], coefficients are
    # alpha+beta=a, alpha-beta=d, gamma+delta=b, gamma-delta=-c.
    alpha = half * (a[0][0] + a[1][1])
    beta = half * (a[0][0] - a[1][1])
    gamma = half * (a[0][1] + a[1][0])
    delta = half * (a[0][1] - a[1][0])
    reconstructed = add(add(scale(alpha, one), scale(beta, parity)),
                        add(scale(gamma, odd_field), scale(delta, px)))
    assert_eq(reconstructed, a, "basis reconstruction")
    return alpha, beta, gamma, delta


def check_finite_analytic_strong_locality_model() -> None:
    """Finite-dimensional shadow of the analytic-vector strong-locality lemma."""

    a_values = [Fraction(-1), Fraction(0), Fraction(0), Fraction(2)]
    b_values = [Fraction(3), Fraction(5), Fraction(7), Fraction(7)]
    a = diagonal_matrix(a_values)
    b = diagonal_matrix(b_values)
    assert_eq_any(comm_any(a, b), zero_matrix(4), "commuting finite self-adjoint generators")
    for a_eigenvalue in set(a_values):
        for b_eigenvalue in set(b_values):
            p_a = diagonal_spectral_projection(a_values, a_eigenvalue)
            p_b = diagonal_spectral_projection(b_values, b_eigenvalue)
            assert_eq_any(
                comm_any(p_a, p_b),
                zero_matrix(4),
                "commuting finite generators have commuting spectral projections",
            )


def check_scalar_shift_does_not_change_generated_spectral_algebra() -> None:
    """Finite model for shifting a self-adjoint local field by a c-number."""

    values = [Fraction(-2), Fraction(1), Fraction(3), Fraction(3)]
    shift = Fraction(5)
    shifted_values = [value + shift for value in values]
    for value in set(values):
        original_projection = diagonal_spectral_projection(values, value)
        shifted_projection = diagonal_spectral_projection(shifted_values, value + shift)
        assert_eq_any(
            shifted_projection,
            original_projection,
            "c-number field shift relabels spectral projections without changing the algebra",
        )


def check_schwinger_observable_coordinate_reduction() -> None:
    """Finite shadow of the Schwinger-model local observable-net reduction."""

    # Two scalar local coordinates separate four diagonal atoms.  This is the
    # finite analogue of saying that the massive scalar coordinates generate
    # the local Weyl algebra after functional calculus.
    phi_0_values = [Fraction(-1), Fraction(0), Fraction(2), Fraction(2)]
    phi_1_values = [Fraction(0), Fraction(1), Fraction(-1), Fraction(3)]
    scalar_pairs = list(zip(phi_0_values, phi_1_values))
    if len(set(scalar_pairs)) != len(scalar_pairs):
        raise AssertionError("scalar coordinates should separate the finite atoms")

    identity4 = diagonal_matrix([Fraction(1)] * 4)
    phi_0 = diagonal_matrix(phi_0_values)
    phi_1 = diagonal_matrix(phi_1_values)

    # E = a phi + c 1 with a nonzero.  Spectral projections are relabelled,
    # not changed.  This is the exact finite version of the c-number theta
    # shift and nonzero Schwinger mass coefficient in the local net.
    charge = Fraction(3)
    scale_factor = -charge
    theta_shift = Fraction(5, 7)
    electric_0_values = [scale_factor * value + theta_shift for value in phi_0_values]
    for value in set(phi_0_values):
        phi_projection = diagonal_spectral_projection(phi_0_values, value)
        electric_projection = diagonal_spectral_projection(
            electric_0_values,
            scale_factor * value + theta_shift,
        )
        assert_eq_any(
            electric_projection,
            phi_projection,
            "Schwinger electric coordinate relabels scalar spectral projections",
        )

    # Current smearings are derivative pullbacks of the same scalar
    # coordinate.  In the finite shadow they are linear combinations of the
    # scalar coordinates, hence stay in the diagonal observable algebra and
    # commute with every scalar spectral projection.
    current_0 = phi_1
    current_1 = scale_any(Fraction(-1), phi_0)
    for current in (current_0, current_1):
        if any(entry != 0 for entry in off_diagonal_entries(current)):
            raise AssertionError("Schwinger current coordinate should stay in the scalar observable algebra")
        for value in set(phi_0_values):
            projection = diagonal_spectral_projection(phi_0_values, value)
            assert_eq_any(
                comm_any(current, projection),
                zero_matrix(4),
                "Schwinger current coordinate commutes with scalar spectral projections",
            )

    # A finite Gauss-law relation: derivative(E) + e J^0 = 0.  The constants
    # are modelled rationally; the point is that this is a relation among the
    # same scalar coordinates, not a new local generator.
    derivative_phi = phi_1
    derivative_electric = scale_any(scale_factor, derivative_phi)
    gauss_combination = add_any(derivative_electric, scale_any(charge, current_0))
    assert_eq_any(gauss_combination, zero_matrix(4), "finite Schwinger Gauss-law coordinate relation")

    # A sector-changing or line-dressed charged operator is not an element of
    # the diagonal electric/current observable algebra in this local model.
    line_shift: MatrixAny = (
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    )
    if all(entry == 0 for entry in off_diagonal_entries(line_shift)):
        raise AssertionError("line-dressed finite operator should be off diagonal")
    if comm_any(line_shift, phi_0) == zero_matrix(4):
        raise AssertionError("line-dressed finite operator should not commute with the electric coordinate")

    # Closed flux functions, by contrast, are bounded functions of the same
    # electric coordinate and hence remain diagonal.
    closed_flux_function = add_any(scale_any(Fraction(2), identity4), scale_any(Fraction(-1), phi_0))
    if any(entry != 0 for entry in off_diagonal_entries(closed_flux_function)):
        raise AssertionError("closed flux function should stay inside the electric-field algebra")


def check_finite_affiliation_commutant_criterion() -> None:
    """Finite shadow of affiliation through commutant invariance."""

    diagonal_values = [Fraction(-1), Fraction(2)]
    affiliated_generator = diagonal_matrix(diagonal_values)
    affiliated_projection = diagonal_spectral_projection(diagonal_values, Fraction(-1))
    parity_as_commutant_unitary: MatrixAny = parity
    assert_eq_any(
        comm_any(affiliated_projection, parity_as_commutant_unitary),
        zero_matrix(2),
        "affiliated spectral projection commutes with the commutant",
    )
    assert_eq_any(
        comm_any(affiliated_generator, parity_as_commutant_unitary),
        zero_matrix(2),
        "affiliated generator preserves the commutant graph in finite dimension",
    )

    nonaffiliated_projection: MatrixAny = proj_plus
    if comm_any(nonaffiliated_projection, parity_as_commutant_unitary) == zero_matrix(2):
        raise AssertionError("odd-field spectral projection should not be affiliated with the diagonal algebra")
    if comm_any(odd_field, parity) == zero:
        raise AssertionError("odd-field generator should not commute with the diagonal commutant unitary")


def check_affiliation_does_not_imply_generation() -> None:
    """Finite diagonal model: affiliated coordinates may generate a proper subnet."""

    # In the full diagonal algebra D_3, T=diag(0,0,1) is affiliated because
    # its spectral projections are diagonal.  Its spectral partition is
    # nevertheless too coarse to recover the two minimal projections in the
    # degenerate zero eigenspace.
    t_values = [Fraction(0), Fraction(0), Fraction(1)]
    p_zero_t = diagonal_spectral_projection(t_values, Fraction(0))
    p_one_t = diagonal_spectral_projection(t_values, Fraction(1))
    minimal_0 = diagonal_matrix([Fraction(1), Fraction(0), Fraction(0)])
    minimal_1 = diagonal_matrix([Fraction(0), Fraction(1), Fraction(0)])
    minimal_2 = diagonal_matrix([Fraction(0), Fraction(0), Fraction(1)])

    assert_eq_any(add_any(p_zero_t, p_one_t), diagonal_matrix([Fraction(1)] * 3), "coarse spectral projections sum to one")
    assert_eq_any(p_one_t, minimal_2, "nondegenerate eigenvalue gives one minimal projection")
    assert_eq_any(
        p_zero_t,
        add_any(minimal_0, minimal_1),
        "degenerate eigenvalue gives a block projection",
    )

    # The algebra generated by T consists of a I + b T, hence all diagonal
    # entries in the first two slots are equal.  The first minimal projection
    # violates that equality and is therefore not generated by T alone.
    t_generated_samples = [
        add_any(scale_any(a, diagonal_matrix([Fraction(1)] * 3)), scale_any(b, diagonal_matrix(t_values)))
        for a in (Fraction(0), Fraction(2), Fraction(-1, 3))
        for b in (Fraction(0), Fraction(5), Fraction(7, 2))
    ]
    for sample in t_generated_samples:
        if sample[0][0] != sample[1][1]:
            raise AssertionError("T-generated diagonal algebra should not split the zero eigenspace")
    if minimal_0[0][0] == minimal_0[1][1]:
        raise AssertionError("minimal projection should split the degenerate eigenspace")

    # Adding S=diag(0,1,0) refines the spectral partition.  Its projection at
    # eigenvalue one is the second minimal projection, and the remaining first
    # minimal projection is obtained by subtraction from the identity.
    s_values = [Fraction(0), Fraction(1), Fraction(0)]
    p_one_s = diagonal_spectral_projection(s_values, Fraction(1))
    recovered_minimal_0 = sub_any(
        diagonal_matrix([Fraction(1)] * 3),
        add_any(p_one_s, p_one_t),
    )
    assert_eq_any(p_one_s, minimal_1, "second coordinate recovers second minimal projection")
    assert_eq_any(recovered_minimal_0, minimal_0, "two coordinates recover the remaining minimal projection")


def check_finite_generated_additivity_and_covariance() -> None:
    """Finite shadow of the Trotter/functional-calculus additivity bridge."""

    local_a = scale(Fraction(3), parity)
    local_b = scale(Fraction(4), odd_field)
    summed_generator = add(local_a, local_b)

    if comm(local_a, local_b) == zero:
        raise AssertionError(
            "additivity diagnostic should use noncommuting local coordinates"
        )

    # The eigenvalues of 3 Z + 4 X are +/-5, so the spectral projections are
    # exact rational polynomials in the summed generator.  This is the
    # finite-dimensional analogue of applying functional calculus after the
    # closure/Trotter step has placed the summed generator in the algebra
    # generated by the smaller local algebras.
    p_plus_sum = scale(
        Fraction(1, 2),
        add(one, scale(Fraction(1, 5), summed_generator)),
    )
    p_minus_sum = scale(
        Fraction(1, 2),
        sub(one, scale(Fraction(1, 5), summed_generator)),
    )
    assert_eq(
        matmul(p_plus_sum, p_plus_sum),
        p_plus_sum,
        "summed-generator P_+ idempotent",
    )
    assert_eq(
        matmul(p_minus_sum, p_minus_sum),
        p_minus_sum,
        "summed-generator P_- idempotent",
    )
    assert_eq(
        add(p_plus_sum, p_minus_sum),
        one,
        "summed-generator projections sum to one",
    )
    assert_eq(scale(Fraction(5), sub(p_plus_sum, p_minus_sum)),
              summed_generator,
              "summed generator recovered from its spectral projections")

    coeffs = span_coefficients(p_plus_sum)
    if coeffs[3] != 0:
        raise AssertionError(
            "summed-generator projection should lie in algebra generated by the two local generators"
        )

    # Covariance of closures implies covariance of all spectral projections.
    transformed_generator = add(local_a, scale(Fraction(-4), odd_field))
    transformed_projection = scale(
        Fraction(1, 2),
        add(one, scale(Fraction(1, 5), transformed_generator)),
    )
    conjugated_projection = matmul(matmul(parity, p_plus_sum), parity)
    assert_eq(conjugated_projection,
              transformed_projection,
              "symmetry conjugation transports spectral projections")


def main() -> None:
    check_finite_analytic_strong_locality_model()
    check_scalar_shift_does_not_change_generated_spectral_algebra()
    check_schwinger_observable_coordinate_reduction()
    check_finite_affiliation_commutant_criterion()
    check_affiliation_does_not_imply_generation()
    check_finite_generated_additivity_and_covariance()

    assert_eq(matmul(parity, parity), one, "parity squares to one")
    assert_eq(matmul(odd_field, odd_field), one, "odd field squares to one")
    assert_eq(matmul(matmul(parity, odd_field), parity),
              scale(Fraction(-1), odd_field),
              "odd field changes sign under parity")

    assert_eq(matmul(proj_plus, proj_plus), proj_plus, "P_+^X idempotent")
    assert_eq(matmul(proj_minus, proj_minus), proj_minus, "P_-^X idempotent")
    assert_eq(add(proj_plus, proj_minus), one, "odd spectral projections sum to one")

    assert_eq(matmul(matmul(parity, proj_plus), parity), proj_minus,
              "parity exchanges odd-field spectral projections")
    assert_eq(average_over_z2(odd_field), zero, "conditional expectation kills odd field")
    assert_eq(average_over_z2(parity), parity, "conditional expectation preserves even field")
    assert_eq(average_over_z2(proj_plus), scale(half, one),
              "odd spectral projection is not an observable projection")

    # The fixed-point algebra consists of the diagonal span of 1 and parity.
    for observable in (one, parity, even_plus, even_minus):
        coeffs = span_coefficients(observable)
        if coeffs[2] != 0 or coeffs[3] != 0:
            raise AssertionError("fixed-point observable has odd component")

    # Adding the odd-field spectral projections recovers the odd generator and
    # hence the full two-by-two field algebra once the even parity operator is
    # also present.
    recovered_x = sub(proj_plus, proj_minus)
    assert_eq(recovered_x, odd_field, "odd field recovered from spectral projections")
    px = matmul(parity, odd_field)
    basis = (one, parity, odd_field, px)
    for b in basis:
        span_coefficients(b)

    # Strong locality is a spectral-projection statement.  Commuting
    # self-adjoint generators have commuting projections; the odd and parity
    # generators do not.
    assert_eq(comm(even_plus, even_minus), zero, "even spectral projections commute")
    if comm(proj_plus, even_plus) == zero:
        raise AssertionError("noncommuting field/observable projections incorrectly commute")

    # Fixed points are local von Neumann subalgebras, but additivity of the
    # observable subnet is not automatic.  With a diagonal Z_2 action on two
    # finite field algebras, X_1 and X_2 are odd local coordinates, whereas
    # X_1 X_2 is globally invariant.  It is not in the algebra generated by the
    # two separate local fixed-point algebras, which is diagonal in this model.
    one4 = kron(one, one)
    p1 = kron(parity, one)
    p2 = kron(one, parity)
    x1 = kron(odd_field, one)
    x2 = kron(one, odd_field)
    diagonal_parity = kron(parity, parity)
    neutral_pair = matmul_any(x1, x2)
    assert_eq_any(
        matmul_any(diagonal_parity, diagonal_parity),
        one4,
        "diagonal parity squares to one",
    )
    assert_eq_any(
        average_over_diagonal_z2(x1),
        zero_matrix(4),
        "diagonal expectation kills first odd field",
    )
    assert_eq_any(
        average_over_diagonal_z2(x2),
        zero_matrix(4),
        "diagonal expectation kills second odd field",
    )
    assert_eq_any(average_over_diagonal_z2(neutral_pair), neutral_pair,
                  "neutral pair is globally invariant")

    local_observable_generators = (one4, p1, p2, matmul_any(p1, p2))
    for generator in local_observable_generators:
        if any(entry != 0 for entry in off_diagonal_entries(generator)):
            raise AssertionError("local fixed-point generated algebra should be diagonal")
    if all(entry == 0 for entry in off_diagonal_entries(neutral_pair)):
        raise AssertionError("neutral bilocal composite should not be diagonal")

    fixed_b = add_any(one4, p1)
    fixed_c = add_any(one4, p2)
    sample = add_any(x1, neutral_pair)
    bimodule_left = average_over_diagonal_z2(
        matmul_any(matmul_any(fixed_b, sample), fixed_c)
    )
    bimodule_right = matmul_any(
        matmul_any(fixed_b, average_over_diagonal_z2(sample)),
        fixed_c,
    )
    assert_eq_any(bimodule_left, bimodule_right, "fixed-point expectation bimodule identity")

    # Haag duality is exactly the step from exterior commutation to membership
    # in the assigned local algebra.  In this finite diagnostic, take the
    # assigned algebra of the first region to be span{1, Z_1} and the
    # complement algebra to be span{1, Z_2}.  The operator X_1 commutes with
    # the complement, hence lies in the dual algebra R(O')', but it is not in
    # the assigned first-region algebra because that algebra is diagonal.
    assert_eq_any(comm_any(x1, p2), zero_matrix(4), "X_1 commutes with exterior Z_2")
    if all(entry == 0 for entry in off_diagonal_entries(x1)):
        raise AssertionError("X_1 should not belong to the diagonal assigned local algebra")

    print("All Wightman-to-net bridge finite-algebra checks passed.")


if __name__ == "__main__":
    main()
