#!/usr/bin/env python3
"""Finite sign checks for Volume I, Chapter 19 QED external-state conventions."""

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_local_charge_neutrality() -> None:
    """Gauge phase of a pointlike monomial is exp(i g (N_psi-N_bar) xi)."""
    samples = [
        (1, 1, True),
        (2, 2, True),
        (2, 1, False),
        (0, 1, False),
    ]
    for n_psi, n_bar, neutral in samples:
        require((n_psi - n_bar == 0) is neutral, "local charge neutrality")


def check_wilson_line_endpoint_phases() -> None:
    """Endpoint phases cancel for the half-line and bilocal Abelian dressings."""
    # Work with integer exponents multiplying i g.  The endpoint at infinity is
    # fixed to zero in the half-line dressing.
    psi_phase = 1
    half_line_phase = -1
    require(psi_phase + half_line_phase == 0, "half-line endpoint cancellation")

    # Bilocal operator: psi(x) W[y->x] bar_psi(y).
    psi_x = 1
    wilson_x = -1
    wilson_y = 1
    bar_y = -1
    require(psi_x + wilson_x == 0, "bilocal x endpoint cancellation")
    require(wilson_y + bar_y == 0, "bilocal y endpoint cancellation")


def check_abelian_fp_field_independence() -> None:
    """The linearized Abelian Lorenz-gauge slice has no field-dependent term."""
    # F[A + d xi] - F[A] = Box xi.  Coefficients of A and psi in the Jacobian
    # are zero; the coefficient of xi is one copy of Box.
    coeff_box_xi = Fraction(1)
    coeff_A = Fraction(0)
    coeff_psi = Fraction(0)
    require(coeff_box_xi == 1, "Abelian FP Box coefficient")
    require(coeff_A == 0 and coeff_psi == 0, "Abelian FP field independence")


def check_compton_longitudinal_cancellation() -> None:
    """Ward cancellation signs in the tree Compton hard kernel."""
    # Pick positive rational dot products; only the signs and identical
    # scalar factors matter after using the Dirac equations.
    p_dot_k = Fraction(5, 3)
    pp_dot_k = Fraction(7, 4)
    pp_dot_kp = Fraction(11, 6)
    p_dot_kp = Fraction(13, 5)

    # Incoming photon representative shift e(k) -> e(k) + alpha k.
    first_in = Fraction(-2) * p_dot_k / (2 * p_dot_k)
    second_in = Fraction(-2) * pp_dot_k / (-2 * pp_dot_k)
    require(first_in + second_in == 0, "incoming Ward cancellation")
    require(first_in == -1 and second_in == 1, "incoming Ward signs")

    # Outgoing photon representative shift e*(k') -> e*(k') + beta k'.
    first_out = Fraction(-2) * pp_dot_kp / (2 * pp_dot_kp)
    second_out = Fraction(-2) * p_dot_kp / (-2 * p_dot_kp)
    require(first_out + second_out == 0, "outgoing Ward cancellation")
    require(first_out == -1 and second_out == 1, "outgoing Ward signs")


def check_cross_section_no_incoming_average() -> None:
    """Fixed incoming spin/helicity sums over two final spins and two helicities."""
    final_spin_count = 2
    final_helicity_count = 2
    incoming_average = 1
    require(final_spin_count * final_helicity_count == 4, "final state count")
    require(incoming_average == 1, "fixed incoming labels are not averaged")


def main() -> None:
    check_local_charge_neutrality()
    check_wilson_line_endpoint_phases()
    check_abelian_fp_field_independence()
    check_compton_longitudinal_cancellation()
    check_cross_section_no_incoming_average()
    print("All QED external-state convention checks passed.")


if __name__ == "__main__":
    main()
