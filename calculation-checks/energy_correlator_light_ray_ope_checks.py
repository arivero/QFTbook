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


def l1(vector):
    return sum(abs(entry) for entry in vector)


def linfty(vector):
    return max(abs(entry) for entry in vector)


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


def zero_matrix(rows, cols):
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


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


def check_finite_light_ray_transport_flatness():
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

    # The full flatness equation contains derivative terms, not only a
    # commutator.  In the affine chart gamma(t,r)=r A and eta(t,r)=t A the
    # derivative terms cancel exactly: partial_t eta - partial_r gamma = 0.
    A = [
        [Fraction(0), Fraction(7, 17)],
        [Fraction(0), Fraction(0)],
    ]
    affine_flat_curvature = mat_sub(A, A)
    assert_equal(
        affine_flat_curvature,
        [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]],
        "affine derivative terms cancel in flat light-ray chart",
    )

    # With different derivative matrices the curvature already appears at the
    # base point before any commutator term contributes.  This guards the sign
    # in partial_t eta - partial_r gamma.
    B = [
        [Fraction(0), Fraction(0)],
        [Fraction(11, 19), Fraction(0)],
    ]
    affine_base_curvature = mat_sub(B, A)
    assert_equal(
        affine_base_curvature,
        [
            [Fraction(0), Fraction(-7, 17)],
            [Fraction(11, 19), Fraction(0)],
        ],
        "affine derivative curvature has the displayed sign",
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


def check_cusp_log_flatness_chart():
    # Minimal cusp-log chart used in the text.  In the convention
    # d_t O = -gamma O, d_r O = -eta O, a UV anomalous dimension with
    # gamma_cusp(t,r)=Gamma(t) r A is flat only when the rapidity anomalous
    # dimension contains eta_cusp(t)=G(t) A with G'(t)=Gamma(t).
    A = [
        [Fraction(0), Fraction(5, 11)],
        [Fraction(0), Fraction(0)],
    ]
    t = Fraction(7, 13)
    gamma_value = Fraction(3, 5) + Fraction(2, 7) * t
    d_gamma_dr = mat_scale(gamma_value, A)
    d_eta_dt = mat_scale(gamma_value, A)
    curvature = mat_sub(d_eta_dt, d_gamma_dr)
    assert_equal(
        curvature,
        [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]],
        "cusp-log rapidity chart satisfies derivative flatness",
    )

    wrong_sign_d_eta_dt = mat_scale(-gamma_value, A)
    wrong_sign_curvature = mat_sub(wrong_sign_d_eta_dt, d_gamma_dr)
    assert_equal(
        wrong_sign_curvature,
        mat_scale(-2 * gamma_value, A),
        "opposite rapidity sign gives cusp curvature obstruction",
    )


def check_projected_curvature_and_scheme_covariance():
    # If the full light-ray connection is flat but a finite chart keeps only a
    # subspace L, the retained curvature is generated by the omitted Q channels:
    # F_LL^trunc = eta_LQ gamma_QL - gamma_LQ eta_QL.
    gamma = [
        [Fraction(0), Fraction(0), Fraction(2, 5)],
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(3, 7), Fraction(-5, 11), Fraction(0)],
    ]
    eta = [
        [Fraction(0), Fraction(0), Fraction(-7, 13)],
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(11, 17), Fraction(13, 19), Fraction(0)],
    ]
    commutator = mat_sub(mat_mat(gamma, eta), mat_mat(eta, gamma))

    # Force full flatness at the base point by choosing derivative matrices
    # d_t eta - d_r gamma = -[gamma, eta].
    d_eta_dt = zero_matrix(3, 3)
    d_gamma_dr = commutator
    full_curvature = mat_add(mat_sub(d_eta_dt, d_gamma_dr), commutator)
    assert_equal(full_curvature, zero_matrix(3, 3), "full light-ray connection is flat")

    gamma_ll = [[gamma[i][j] for j in range(2)] for i in range(2)]
    eta_ll = [[eta[i][j] for j in range(2)] for i in range(2)]
    d_eta_ll = [[d_eta_dt[i][j] for j in range(2)] for i in range(2)]
    d_gamma_ll = [[d_gamma_dr[i][j] for j in range(2)] for i in range(2)]
    truncated_curvature = mat_add(
        mat_sub(d_eta_ll, d_gamma_ll),
        mat_sub(mat_mat(gamma_ll, eta_ll), mat_mat(eta_ll, gamma_ll)),
    )

    gamma_lq = [[gamma[i][2]] for i in range(2)]
    gamma_ql = [[gamma[2][j] for j in range(2)]]
    eta_lq = [[eta[i][2]] for i in range(2)]
    eta_ql = [[eta[2][j] for j in range(2)]]
    omitted_channel = mat_sub(mat_mat(eta_lq, gamma_ql), mat_mat(gamma_lq, eta_ql))
    assert_equal(
        truncated_curvature,
        omitted_channel,
        "projected curvature equals omitted light-ray channel term",
    )

    # Check the two-scale finite-scheme covariance with scale-dependent R at a
    # single base point:
    # gamma' = R^{-1} gamma R + R^{-1} R_t,
    # eta' = R^{-1} eta R + R^{-1} R_r,
    # F' = R^{-1} F R.
    gamma2 = [
        [Fraction(1, 3), Fraction(2, 7)],
        [Fraction(-5, 11), Fraction(3, 13)],
    ]
    eta2 = [
        [Fraction(4, 17), Fraction(-1, 5)],
        [Fraction(7, 19), Fraction(-2, 23)],
    ]
    d_gamma_dr2 = [
        [Fraction(2, 29), Fraction(-3, 31)],
        [Fraction(5, 37), Fraction(7, 41)],
    ]
    d_eta_dt2 = [
        [Fraction(-11, 43), Fraction(13, 47)],
        [Fraction(17, 53), Fraction(-19, 59)],
    ]
    curvature2 = mat_add(
        mat_sub(d_eta_dt2, d_gamma_dr2),
        mat_sub(mat_mat(gamma2, eta2), mat_mat(eta2, gamma2)),
    )

    R = [
        [Fraction(5, 3), Fraction(1, 4)],
        [Fraction(-2, 5), Fraction(7, 6)],
    ]
    Rt = [
        [Fraction(1, 11), Fraction(-2, 13)],
        [Fraction(3, 17), Fraction(5, 19)],
    ]
    Rr = [
        [Fraction(-7, 23), Fraction(11, 29)],
        [Fraction(13, 31), Fraction(-17, 37)],
    ]
    Rtr = [
        [Fraction(19, 41), Fraction(-23, 43)],
        [Fraction(29, 47), Fraction(31, 53)],
    ]
    Rinv = inv2(R)
    Rinv_t = mat_scale(-1, mat_mat(mat_mat(Rinv, Rt), Rinv))
    Rinv_r = mat_scale(-1, mat_mat(mat_mat(Rinv, Rr), Rinv))

    gamma_prime = mat_add(mat_mat(mat_mat(Rinv, gamma2), R), mat_mat(Rinv, Rt))
    eta_prime = mat_add(mat_mat(mat_mat(Rinv, eta2), R), mat_mat(Rinv, Rr))

    d_gamma_prime_dr = mat_add(
        mat_add(
            mat_add(
                mat_mat(mat_mat(Rinv_r, gamma2), R),
                mat_mat(mat_mat(Rinv, d_gamma_dr2), R),
            ),
            mat_mat(mat_mat(Rinv, gamma2), Rr),
        ),
        mat_add(mat_mat(Rinv_r, Rt), mat_mat(Rinv, Rtr)),
    )
    d_eta_prime_dt = mat_add(
        mat_add(
            mat_add(
                mat_mat(mat_mat(Rinv_t, eta2), R),
                mat_mat(mat_mat(Rinv, d_eta_dt2), R),
            ),
            mat_mat(mat_mat(Rinv, eta2), Rt),
        ),
        mat_add(mat_mat(Rinv_t, Rr), mat_mat(Rinv, Rtr)),
    )
    curvature_prime = mat_add(
        mat_sub(d_eta_prime_dt, d_gamma_prime_dr),
        mat_sub(mat_mat(gamma_prime, eta_prime), mat_mat(eta_prime, gamma_prime)),
    )
    expected_prime = mat_mat(mat_mat(Rinv, curvature2), R)
    assert_equal(
        curvature_prime,
        expected_prime,
        "two-scale light-ray curvature transforms covariantly",
    )


def check_endpoint_observable_transport_budget():
    # The finite endpoint chart in the text has
    # V(phi;t)=C_L(phi;t) O_L(t)+K_L(phi;t).  The anomalous-dimension pieces
    # cancel between the coefficient row and the operator column, while a
    # moving endpoint-extension row D_L cancels only against the compensating
    # contact derivative dK=-D_L O_L.  Residuals are the only surviving scale
    # derivative of the detector-test functional.
    gamma = [
        [Fraction(2, 7), Fraction(-1, 5)],
        [Fraction(3, 11), Fraction(4, 13)],
    ]
    coeff = [Fraction(5, 17), Fraction(-7, 19)]
    operator = [Fraction(11, 23), Fraction(13, 29)]
    endpoint_shift = [Fraction(-3, 31), Fraction(2, 37)]

    residual_coeff = [Fraction(1, 41), Fraction(-2, 43)]
    residual_operator = [Fraction(3, 47), Fraction(-5, 53)]
    residual_contact = Fraction(7, 59)

    d_coeff = [
        row_mat(coeff, gamma)[i] + endpoint_shift[i] + residual_coeff[i]
        for i in range(2)
    ]
    d_operator = [
        -mat_vec(gamma, operator)[i] + residual_operator[i]
        for i in range(2)
    ]
    d_contact = -dot(endpoint_shift, operator) + residual_contact

    derivative = dot(d_coeff, operator) + dot(coeff, d_operator) + d_contact
    expected = (
        dot(residual_coeff, operator)
        + dot(coeff, residual_operator)
        + residual_contact
    )
    assert_equal(
        derivative,
        expected,
        "endpoint observable transport leaves only declared residuals",
    )

    # With zero residuals, both anomalous-dimension transport and endpoint
    # contact reshuffling cancel exactly.
    exact_d_coeff = [
        row_mat(coeff, gamma)[i] + endpoint_shift[i]
        for i in range(2)
    ]
    exact_d_operator = [-entry for entry in mat_vec(gamma, operator)]
    exact_d_contact = -dot(endpoint_shift, operator)
    assert_equal(
        dot(exact_d_coeff, operator)
        + dot(coeff, exact_d_operator)
        + exact_d_contact,
        Fraction(0),
        "exact finite endpoint chart is scale independent",
    )

    # The wrong contact sign changes the observable by twice the endpoint
    # extension row paired with the operator column.
    wrong_contact = dot(endpoint_shift, operator)
    wrong_derivative = (
        dot(exact_d_coeff, operator)
        + dot(coeff, exact_d_operator)
        + wrong_contact
    )
    assert_equal(
        wrong_derivative,
        2 * dot(endpoint_shift, operator),
        "wrong endpoint contact sign produces the predicted defect",
    )

    # The text's finite norm budget is checked with the l1/linfty dual pair.
    bound = (
        l1(residual_coeff) * linfty(operator)
        + l1(coeff) * linfty(residual_operator)
        + abs(residual_contact)
    )
    if abs(derivative) > bound:
        raise AssertionError(
            f"endpoint observable residual bound failed: {abs(derivative)!r} > {bound!r}"
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
    check_finite_light_ray_transport_flatness()
    check_cusp_log_flatness_chart()
    check_projected_curvature_and_scheme_covariance()
    check_endpoint_observable_transport_budget()

    print("All EEC light-ray OPE and endpoint transport bookkeeping checks passed.")


if __name__ == "__main__":
    main()
