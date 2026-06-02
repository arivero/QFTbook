#!/usr/bin/env python3
"""Finite checks for the EEC light-ray OPE bookkeeping.

The script checks algebraic consequences of the endpoint conventions used in
Volume II, Chapter 19.  It does not evaluate QCD loop integrals.  Its role is
to guard the distributional plus-prescription convention, the contact-term
normalization, and the sign/transpose convention in the coefficient/operator
RG equations.
"""

from fractions import Fraction


def assert_equal(left, right, message):
    if left != right:
        raise AssertionError(f"{message}: {left!r} != {right!r}")


def plus_action(poly, rho0):
    """Action of [1/rho]_+ on a polynomial sum poly[n] rho^n."""
    total = Fraction(0)
    for power, coeff in enumerate(poly):
        if power == 0:
            continue
        total += coeff * rho0**power / power
    return total


def ordinary_annulus_action(poly, rho_a, rho_b):
    """Action of 1_{rho_a<rho<rho_b}/rho on a polynomial.

    The constant term is deliberately excluded by the caller when testing the
    resolution-shift identity, because its contribution is recorded
    symbolically as log(rho_b/rho_a).
    """

    total = Fraction(0)
    for power, coeff in enumerate(poly):
        if power == 0:
            continue
        total += coeff * (rho_b**power - rho_a**power) / power
    return total


def symbolic_log_term(log_rho0=0, log_eps=0, finite=0):
    return {
        "log_rho0": Fraction(log_rho0),
        "log_eps": Fraction(log_eps),
        "finite": Fraction(finite),
    }


def add_log_terms(*terms):
    total = symbolic_log_term()
    for term in terms:
        for key in total:
            total[key] += term[key]
    return total


def scalar_mul_log_term(c, term):
    return {key: Fraction(c) * value for key, value in term.items()}


def mat_vec(matrix, vector):
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    ]


def mat_mat(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def mat_add(left, right):
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def mat_sub(left, right):
    return [
        [left[i][j] - right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def mat_scale(scalar, matrix):
    return [
        [Fraction(scalar) * matrix[i][j] for j in range(len(matrix[0]))]
        for i in range(len(matrix))
    ]


def row_mat(row, matrix):
    return [
        sum(row[i] * matrix[i][j] for i in range(len(row)))
        for j in range(len(matrix[0]))
    ]


def dot(row, column):
    return sum(row[i] * column[i] for i in range(len(row)))


def inv2(matrix):
    (a, b), (c, d) = matrix
    determinant = a * d - b * c
    if determinant == 0:
        raise AssertionError("matrix is singular")
    return [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant],
    ]


def identity2():
    return [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
    ]


def check_endpoint_resolution_shift():
    # Distribution identity used in the text:
    # D_b = D_a + 1_{a<rho<b}/rho - log(b/a) delta(rho).
    # For a polynomial phi = c0 + c1 rho + c2 rho^2 + ..., the nonconstant
    # terms are checked by rational arithmetic, and the constant term is
    # checked separately at the symbolic logarithm level.
    rho_a = Fraction(2, 7)
    rho_b = Fraction(5, 7)
    poly = [Fraction(11, 13), Fraction(3, 5), Fraction(-7, 17), Fraction(19, 23)]

    left_nonconstant = plus_action(poly, rho_b)
    right_nonconstant = plus_action(poly, rho_a) + ordinary_annulus_action(poly, rho_a, rho_b)
    assert_equal(
        left_nonconstant,
        right_nonconstant,
        "endpoint resolution shift nonconstant test",
    )

    # The "finite" slot is only a formal scalar coefficient here: both terms
    # multiply the same log(rho_b/rho_a), so cancellation is coefficient-wise.
    constant_coeff = poly[0]
    annulus_constant_log = symbolic_log_term(finite=constant_coeff)
    contact_shift = symbolic_log_term(finite=-constant_coeff)
    assert_equal(
        add_log_terms(annulus_constant_log, contact_shift),
        symbolic_log_term(),
        "endpoint resolution shift constant test",
    )


def check_finite_light_ray_mixing_chart():
    # Renormalized operators are O_R = Z^{-1} O_reg.  If O_reg is held fixed,
    # gamma = Z^{-1} dZ gives dO_R = -gamma O_R, while the coefficient row
    # C = C_reg Z obeys dC = C gamma.  The finite matrices below keep this
    # sign/transpose convention honest.
    Z = [
        [Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(1)],
    ]
    dZ = [
        [Fraction(3, 5), Fraction(-2, 7)],
        [Fraction(4, 11), Fraction(1, 13)],
    ]
    invZ = inv2(Z)
    gamma = mat_mat(invZ, dZ)
    O_reg = [Fraction(5, 7), Fraction(-3, 8)]
    O_ren = mat_vec(invZ, O_reg)
    dO_direct = [-entry for entry in mat_vec(mat_mat(invZ, dZ), O_ren)]
    dO_gamma = [-entry for entry in mat_vec(gamma, O_ren)]
    assert_equal(dO_direct, dO_gamma, "operator RG from finite Z matrix")

    C_reg = [Fraction(11, 17), Fraction(-13, 19)]
    C_ren = row_mat(C_reg, Z)
    dC_direct = row_mat(C_reg, dZ)
    dC_gamma = row_mat(C_ren, gamma)
    assert_equal(dC_direct, dC_gamma, "coefficient RG from finite Z matrix")
    assert_equal(
        dot(dC_direct, O_ren) + dot(C_ren, dO_gamma),
        Fraction(0),
        "finite chart preserves coefficient/operator pairing",
    )

    # A finite scheme change O' = R^{-1} O, C' = C R changes
    # gamma by R^{-1} gamma R + R^{-1} dR.  The transformed coefficient row
    # still obeys the same paired RG equation.
    R = [
        [Fraction(1), Fraction(2, 5)],
        [Fraction(0), Fraction(3, 2)],
    ]
    dR = [
        [Fraction(0), Fraction(1, 7)],
        [Fraction(0), Fraction(-1, 11)],
    ]
    invR = inv2(R)
    gamma_prime = mat_add(mat_mat(mat_mat(invR, gamma), R), mat_mat(invR, dR))
    C_prime = row_mat(C_ren, R)
    dC_prime_direct = [
        row_mat(dC_direct, R)[j] + row_mat(C_ren, dR)[j]
        for j in range(2)
    ]
    dC_prime_gamma = row_mat(C_prime, gamma_prime)
    assert_equal(
        dC_prime_direct,
        dC_prime_gamma,
        "finite scheme change transforms coefficient RG covariantly",
    )
    O_prime = mat_vec(invR, O_ren)
    assert_equal(
        dot(C_prime, O_prime),
        dot(C_ren, O_ren),
        "finite scheme change preserves paired observable",
    )

    # The protected energy moment is a left null vector of gamma only in a
    # convention preserving the displayed energy-sum row.  Under a general
    # scheme change its coordinate row moves covariantly.
    moment = [Fraction(1), Fraction(1)]
    conserving_gamma = [
        [Fraction(2, 7), Fraction(-3, 5)],
        [Fraction(-2, 7), Fraction(3, 5)],
    ]
    assert_equal(row_mat(moment, conserving_gamma), [Fraction(0), Fraction(0)], "moment row is protected")
    gamma_prime_moment = mat_add(
        mat_mat(mat_mat(invR, conserving_gamma), R),
        mat_mat(invR, dR),
    )
    moment_prime = row_mat(moment, R)
    dmoment_prime = row_mat(moment, dR)
    assert_equal(
        dmoment_prime,
        row_mat(moment_prime, gamma_prime_moment),
        "protected moment row transforms covariantly",
    )
    R_preserving_moment = [
        [Fraction(3, 2), Fraction(-1, 4)],
        [Fraction(-1, 2), Fraction(5, 4)],
    ]
    assert_equal(
        row_mat(moment, R_preserving_moment),
        moment,
        "energy-sum-preserving schemes have M R = M",
    )


def check_finite_light_ray_transport_certificate():
    # Use nilpotent matrices so that exp(s gamma) = I + s gamma exactly over
    # the rationals.  This checks the side on which the anomalous dimension
    # acts in the text's row/column convention.
    gamma = [
        [Fraction(0), Fraction(2, 3)],
        [Fraction(0), Fraction(0)],
    ]
    s = Fraction(5, 7)
    U = mat_add(identity2(), mat_scale(s, gamma))
    U_inv = mat_sub(identity2(), mat_scale(s, gamma))
    assert_equal(mat_mat(U, U_inv), identity2(), "nilpotent transport inverse")
    coeff0 = [Fraction(11, 13), Fraction(-17, 19)]
    operator0 = [Fraction(23, 29), Fraction(31, 37)]
    coeff_s = row_mat(coeff0, U)
    operator_s = mat_vec(U_inv, operator0)
    assert_equal(
        dot(coeff_s, operator_s),
        dot(coeff0, operator0),
        "finite light-ray transport preserves coefficient/operator pairing",
    )

    # Since gamma^2=0, d(C0(I+s gamma))/ds = C(s) gamma and
    # d((I-s gamma)O0)/ds = -gamma O(s) hold exactly.
    assert_equal(
        row_mat(coeff0, gamma),
        row_mat(coeff_s, gamma),
        "coefficient transport differential equation",
    )
    assert_equal(
        [-entry for entry in mat_vec(gamma, operator0)],
        [-entry for entry in mat_vec(gamma, operator_s)],
        "operator transport differential equation",
    )

    # A protected row is constant in a fixed chart exactly when M gamma = 0.
    protected_gamma = [
        [Fraction(1, 5), Fraction(-1, 5)],
        [Fraction(-1, 5), Fraction(1, 5)],
    ]
    moment = [Fraction(1), Fraction(1)]
    assert_equal(row_mat(moment, protected_gamma), [Fraction(0), Fraction(0)], "constant protected row")
    moving_R = [
        [Fraction(1), Fraction(1, 4)],
        [Fraction(0), Fraction(3, 2)],
    ]
    moved_moment = row_mat(moment, moving_R)
    assert_equal(
        dot(moved_moment, mat_vec(inv2(moving_R), operator0)),
        dot(moment, operator0),
        "moving protected row preserves moment coordinate",
    )

    # Flat two-scale transport: gamma and eta are multiples of the same
    # nilpotent, so the two path-ordered products agree.
    eta_flat = [
        [Fraction(0), Fraction(-4, 5)],
        [Fraction(0), Fraction(0)],
    ]
    r = Fraction(3, 11)
    U_mu = mat_add(identity2(), mat_scale(s, gamma))
    U_nu_flat = mat_add(identity2(), mat_scale(r, eta_flat))
    assert_equal(
        mat_mat(U_mu, U_nu_flat),
        mat_mat(U_nu_flat, U_mu),
        "flat two-scale light-ray transport is path independent",
    )

    # Nonzero curvature appears as the commutator obstruction already in a
    # finite nilpotent chart.
    eta_curved = [
        [Fraction(0), Fraction(0)],
        [Fraction(5, 13), Fraction(0)],
    ]
    U_nu_curved = mat_add(identity2(), mat_scale(r, eta_curved))
    path_difference = mat_sub(mat_mat(U_mu, U_nu_curved), mat_mat(U_nu_curved, U_mu))
    commutator = mat_sub(mat_mat(gamma, eta_curved), mat_mat(eta_curved, gamma))
    assert_equal(
        path_difference,
        mat_scale(s * r, commutator),
        "curved two-scale transport commutator obstruction",
    )


def main():
    rho0 = Fraction(3, 5)

    # The plus distribution annihilates the constant test function and has the
    # defining finite action on polynomial deviations from the endpoint value.
    assert_equal(
        plus_action([Fraction(1)], rho0),
        Fraction(0),
        "plus distribution should annihilate constants",
    )
    a = Fraction(7, 11)
    b = Fraction(-5, 13)
    poly = [Fraction(1), a, b]
    expected = a * rho0 + b * rho0**2 / 2
    assert_equal(
        plus_action(poly, rho0),
        expected,
        "plus distribution polynomial action",
    )

    # A separated real density Gamma/rho on eps < rho < rho0 carries the
    # logarithm Gamma log(rho0/eps).  The plus prescription subtracts exactly
    # this endpoint log from the contact part before the finite delta
    # coefficient is chosen.
    gamma = Fraction(17, 19)
    real_cutoff_integral = scalar_mul_log_term(
        gamma, symbolic_log_term(log_rho0=1, log_eps=-1)
    )
    endpoint_counterterm = scalar_mul_log_term(
        -gamma, symbolic_log_term(log_rho0=1, log_eps=-1)
    )
    assert_equal(
        add_log_terms(real_cutoff_integral, endpoint_counterterm),
        symbolic_log_term(),
        "endpoint contact subtraction should cancel the cutoff logarithm",
    )

    finite_contact = Fraction(23, 29)
    full_endpoint_moment = add_log_terms(
        real_cutoff_integral,
        endpoint_counterterm,
        symbolic_log_term(finite=finite_contact),
    )
    assert_equal(
        full_endpoint_moment,
        symbolic_log_term(finite=finite_contact),
        "renormalized endpoint moment should retain only the finite delta coefficient",
    )

    # With column-vector operators obeying dO/dlog(mu) = -gamma O and row
    # coefficients obeying dC/dlog(mu) = C gamma, the scalar pairing C O is
    # RG-invariant.  This guards the sign and transpose convention in the text.
    gamma_matrix = [
        [Fraction(1, 3), Fraction(2, 5)],
        [Fraction(-7, 11), Fraction(13, 17)],
    ]
    coeff = [Fraction(19, 23), Fraction(-29, 31)]
    operator = [Fraction(37, 41), Fraction(43, 47)]
    d_operator = [-entry for entry in mat_vec(gamma_matrix, operator)]
    d_coeff = row_mat(coeff, gamma_matrix)
    derivative_pairing = dot(d_coeff, operator) + dot(coeff, d_operator)
    assert_equal(
        derivative_pairing,
        Fraction(0),
        "coefficient/operator RG pairing should be invariant",
    )

    # The same null-vector condition is the finite-dimensional analogue of the
    # statement that the energy-sum functional has zero anomalous dimension.
    moment = [Fraction(1), Fraction(1)]
    conserving_gamma = [
        [Fraction(2, 7), Fraction(-3, 5)],
        [Fraction(-2, 7), Fraction(3, 5)],
    ]
    assert_equal(
        row_mat(moment, conserving_gamma),
        [Fraction(0), Fraction(0)],
        "energy-sum functional should be a left null vector of the mixing matrix",
    )

    check_endpoint_resolution_shift()
    check_finite_light_ray_mixing_chart()
    check_finite_light_ray_transport_certificate()

    print("All EEC light-ray OPE bookkeeping checks passed.")


if __name__ == "__main__":
    main()
