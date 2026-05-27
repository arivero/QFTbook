#!/usr/bin/env python3
"""Finite algebra checks for supersymmetric moduli-space quotient conventions."""


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_rank_one_abelian_invariant_ring():
    """Check C[x,y]^{C*} = C[xy] for charges (+1,-1) up to finite degree."""

    for total_degree in range(0, 10):
        invariant_monomials = []
        for a in range(total_degree + 1):
            b = total_degree - a
            charge = a - b
            if charge == 0:
                invariant_monomials.append((a, b))

        if total_degree % 2 == 0:
            power = total_degree // 2
            assert_equal(
                invariant_monomials,
                [(power, power)],
                f"degree {total_degree} invariant monomial is (xy)^{power}",
            )
        else:
            assert_equal(
                invariant_monomials,
                [],
                f"degree {total_degree} has no invariant monomial",
            )


def check_rank_one_abelian_dimension_count():
    """Compare real symplectic and complex affine quotient dimensions."""

    complex_variables = 2
    complex_reductive_quotient = 1
    affine_complex_dimension = complex_variables - complex_reductive_quotient

    real_variables = 4
    real_moment_map_equations = 1
    compact_gauge_orbit_dimension = 1
    symplectic_real_dimension = (
        real_variables - real_moment_map_equations - compact_gauge_orbit_dimension
    )

    assert_equal(affine_complex_dimension, 1, "affine quotient complex dimension")
    assert_equal(symplectic_real_dimension, 2, "symplectic quotient real dimension")
    assert_equal(
        2 * affine_complex_dimension,
        symplectic_real_dimension,
        "Kempf-Ness dimension comparison",
    )


def check_f_term_ideal_equivariance():
    """Invariant W implies dW transforms in the dual representation."""

    q_x = 1
    q_y = -1

    # W=(xy)^2 is invariant.  The derivative F_x=2*x*y^2 has charge -1,
    # and F_y=2*x^2*y has charge +1, i.e. q(F_i)=-q(field_i).
    charge_fx = q_x + 2 * q_y
    charge_fy = 2 * q_x + q_y

    assert_equal(charge_fx, -q_x, "F_x dual charge")
    assert_equal(charge_fy, -q_y, "F_y dual charge")
    assert_equal(charge_fx + q_x, 0, "F_x d x invariant pairing")
    assert_equal(charge_fy + q_y, 0, "F_y d y invariant pairing")


def main():
    check_rank_one_abelian_invariant_ring()
    check_rank_one_abelian_dimension_count()
    check_f_term_ideal_equivariance()
    print("All supersymmetric moduli-space quotient checks passed.")


if __name__ == "__main__":
    main()
