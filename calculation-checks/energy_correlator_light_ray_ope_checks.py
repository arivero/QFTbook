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


def row_mat(row, matrix):
    return [
        sum(row[i] * matrix[i][j] for i in range(len(row)))
        for j in range(len(matrix[0]))
    ]


def dot(row, column):
    return sum(row[i] * column[i] for i in range(len(row)))


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

    print("All EEC light-ray OPE bookkeeping checks passed.")


if __name__ == "__main__":
    main()
