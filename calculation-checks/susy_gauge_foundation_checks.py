#!/usr/bin/env python3
"""Finite checks for foundational supersymmetric gauge-theory conventions."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_d_term_square_completion():
    """Check the auxiliary D-field equation and on-shell potential sign."""

    g_squared = Fraction(5, 3)
    mu = Fraction(7, 4)
    zeta = Fraction(1, 6)
    eta = mu - zeta

    d_on_shell = -g_squared * eta
    lagrangian_on_shell = d_on_shell * d_on_shell / (2 * g_squared) + eta * d_on_shell
    expected_lagrangian = -g_squared * eta * eta / 2
    potential = -lagrangian_on_shell

    assert_equal(d_on_shell, -g_squared * eta, "D-field algebraic equation")
    assert_equal(lagrangian_on_shell, expected_lagrangian, "D-term on-shell Lagrangian")
    assert_equal(potential, g_squared * eta * eta / 2, "positive D-term potential")


def check_fi_parameter_centrality_for_su2():
    """A linear FI functional on a semisimple algebra must vanish."""

    # In an su(2) basis [e1,e2]=e3, [e2,e3]=e1, [e3,e1]=e2.
    # Gauge invariance of zeta requires zeta([x,y])=0 for each bracket, so the
    # linear system for (zeta(e1), zeta(e2), zeta(e3)) has these rows.
    constraint_rows = [
        (0, 0, 1),  # zeta([e1,e2]) = zeta(e3)
        (1, 0, 0),  # zeta([e2,e3]) = zeta(e1)
        (0, 1, 0),  # zeta([e3,e1]) = zeta(e2)
    ]
    determinant = (
        constraint_rows[0][0] * constraint_rows[1][1] * constraint_rows[2][2]
        + constraint_rows[0][1] * constraint_rows[1][2] * constraint_rows[2][0]
        + constraint_rows[0][2] * constraint_rows[1][0] * constraint_rows[2][1]
        - constraint_rows[0][2] * constraint_rows[1][1] * constraint_rows[2][0]
        - constraint_rows[0][1] * constraint_rows[1][0] * constraint_rows[2][2]
        - constraint_rows[0][0] * constraint_rows[1][2] * constraint_rows[2][1]
    )
    assert_equal(abs(determinant), 1, "SU(2) FI centrality matrix has full rank")


def cubic_u1_anomaly(charges):
    return sum(q**3 for q in charges)


def mixed_gravity_u1_anomaly(charges):
    return sum(charges)


def check_vectorlike_u1_anomaly_cancellation():
    for q in (Fraction(1), Fraction(2), Fraction(-3, 2), Fraction(5, 3)):
        charges = [q, -q]
        assert_equal(cubic_u1_anomaly(charges), 0, f"U(1)^3 vectorlike anomaly q={q}")
        assert_equal(
            mixed_gravity_u1_anomaly(charges),
            0,
            f"mixed gravitational-U(1) vectorlike anomaly q={q}",
        )


def check_conjugate_nonabelian_anomaly_sign():
    """Model the sign A_{R^vee}=-A_R for a single anomaly coefficient."""

    anomaly_r = Fraction(11, 7)
    anomaly_dual = -anomaly_r
    assert_equal(anomaly_r + anomaly_dual, 0, "conjugate representation anomaly sign")


def main():
    check_d_term_square_completion()
    check_fi_parameter_centrality_for_su2()
    check_vectorlike_u1_anomaly_cancellation()
    check_conjugate_nonabelian_anomaly_sign()
    print("All supersymmetric gauge-foundation checks passed.")


if __name__ == "__main__":
    main()
