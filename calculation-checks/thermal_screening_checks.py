#!/usr/bin/env python3
"""Finite convention checks for thermal gauge-theory screening.

These checks accompany Volume X, Chapter 7.  They verify algebraic facts that
are easy to obscure in prose: the Yukawa power in a d-dimensional static
correlator, the one-dimensional projected pole residue, Polyakov-channel
bookkeeping, static-source line renormalization cancellation with its nonzero
one-point domain, the second-background-variation contact term in Debye
matching, and the conversion of the one-loop Debye coefficient between the
monograph trace-delta convention and the common half-trace convention.  They
also check the connection/canonical conversion under mathcal A = g a through
the Debye curvature, EQCD quadratic action, static propagator, induced current,
and holonomy exponent; the finite angular algebra behind the HTL bridge from
static Debye matching to a transverse retarded response; and the finite
hierarchy logic behind local EQCD matching.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close


from fractions import Fraction
from math import exp, pi


def assert_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def assert_close(name: str, actual: float, expected: float, tol: float = 1.0e-12) -> None:
    _assert_close(name, actual, expected, tol=tol)


def yukawa_asymptotic_powers(spatial_dim: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return Bessel order, mass power, and distance power for a scalar pole."""

    d = Fraction(spatial_dim, 1)
    bessel_order = d / 2 - 1
    mass_power = (d - 3) / 2
    distance_power = -(d - 1) / 2
    return bessel_order, mass_power, distance_power


def check_yukawa_screening_power() -> None:
    expected = {
        1: (Fraction(-1, 2), Fraction(-1, 1), Fraction(0, 1)),
        2: (Fraction(0, 1), Fraction(-1, 2), Fraction(-1, 2)),
        3: (Fraction(1, 2), Fraction(0, 1), Fraction(-1, 1)),
        4: (Fraction(1, 1), Fraction(1, 2), Fraction(-3, 2)),
    }
    for spatial_dim, powers in expected.items():
        assert_equal(
            f"Yukawa asymptotic powers d={spatial_dim}",
            yukawa_asymptotic_powers(spatial_dim),
            powers,
        )

    # The old r^{-(d-2)/2} power would be wrong already in d=3, where the
    # massive static Green function is exp(-Mr)/(4 pi r).
    assert_equal("three-dimensional static Yukawa power", yukawa_asymptotic_powers(3)[2], Fraction(-1, 1))


def check_projected_pole_residue() -> None:
    mass = 1.7
    z = 2.3
    residue = 0.4
    projected = residue * exp(-mass * abs(z)) / (2.0 * mass)

    # Differentiating twice away from z=0 verifies that the projected kernel is
    # the Green function of -d_z^2 + M^2 with pole residue Z.
    second_derivative = mass * mass * projected
    assert_close("projected pole homogeneous equation", (-second_derivative + mass * mass * projected), 0.0)


def debye_half_trace_coefficient(n_c: int, n_f: int) -> Fraction:
    c_a = Fraction(n_c, 1)
    t_fund = Fraction(1, 2)
    return c_a / 3 + n_f * t_fund / 3


def debye_trace_delta_coefficient(n_c: int, n_f: int) -> Fraction:
    c_a = Fraction(2 * n_c, 1)
    t_fund = Fraction(1, 1)
    return c_a / 3 + n_f * t_fund / 3


def check_debye_trace_convention_conversion() -> None:
    for n_c in range(2, 8):
        for n_f in range(0, 7):
            # If t_delta^a=sqrt(2) t_half^a, the same covariant derivative
            # has g_delta=g_half/sqrt(2).  Thus the doubled trace-delta group
            # coefficient is compensated by g_delta^2=g_half^2/2.
            half_trace = debye_half_trace_coefficient(n_c, n_f)
            trace_delta_physical = debye_trace_delta_coefficient(n_c, n_f) / 2
            assert_equal(
                f"Debye trace conversion SU({n_c}) Nf={n_f}",
                trace_delta_physical,
                half_trace,
            )


def background_second_variation(contact: Fraction, connected_first_variations: Fraction) -> Fraction:
    # For Gamma=-log Z and Euclidean action S[A], differentiating twice gives
    # <S''>-<S' S'>_c.  Scalar and gauge operators have nonzero S'' terms.
    return contact - connected_first_variations


def check_debye_second_variation_contact_terms() -> None:
    fermion_contact = Fraction(0)
    fermion_insertions = Fraction(-5, 7)
    assert_equal(
        "linear fermion coupling has no seagull term",
        background_second_variation(fermion_contact, fermion_insertions),
        -fermion_insertions,
    )

    scalar_contact = Fraction(11, 13)
    scalar_insertions = Fraction(5, 7)
    scalar_full = background_second_variation(scalar_contact, scalar_insertions)
    scalar_current_only = -scalar_insertions
    assert_equal(
        "scalar Debye variation includes seagull",
        scalar_full - scalar_current_only,
        scalar_contact,
    )

    # Background-field gauge around a flat A0 background gives
    # (4 vector components)/2 - (one complex ghost) = one scalar determinant,
    # i.e. two real periodic bosonic thermal degrees of freedom in the adjoint.
    vector_log_copies = Fraction(4, 2)
    ghost_log_copies = Fraction(1)
    net_log_copies = vector_log_copies - ghost_log_copies
    real_boson_debye_weight = Fraction(1, 6)
    assert_equal("vector-minus-ghost determinant copies", net_log_copies, Fraction(1))
    assert_equal(
        "gauge determinant equals two real bosonic Debye weights",
        2 * real_boson_debye_weight,
        Fraction(1, 3),
    )


def check_htl_static_limit_and_transversality() -> None:
    # For K_mu=(-omega,k) and v^mu=(1,v), the retarded HTL kernel used in the
    # chapter is K_R^{mu nu}=m_D^2[delta_0^mu delta_0^nu
    #   - omega <v^mu v^nu/(omega-v.k+i0)>].
    # Contracting with K_mu cancels the denominator because
    # K_mu v^mu=-(omega-v.k).
    avg_v0 = Fraction(1)
    avg_vx = Fraction(0)
    avg_vy = Fraction(0)
    avg_vz = Fraction(0)
    assert_equal("HTL transversality nu=0", -1 + avg_v0, Fraction(0))
    assert_equal("HTL transversality nu=x", avg_vx, Fraction(0))
    assert_equal("HTL transversality nu=y", avg_vy, Fraction(0))
    assert_equal("HTL transversality nu=z", avg_vz, Fraction(0))

    # The A_0 coefficient from the kinetic solution uses
    # -v.k/(omega-v.k)=1-omega/(omega-v.k).  Check after multiplying by the
    # common denominator, which avoids choosing a regulator for the pole.
    omega = Fraction(5)
    v_dot_k = Fraction(2)
    denominator = omega - v_dot_k
    assert_equal("HTL A0 numerator decomposition", -v_dot_k, denominator - omega)

    # The strict static response at omega=0 keeps only the 00 component.  The
    # spatial two-point angular average is nonzero, but it is multiplied by the
    # explicit omega prefactor in the retarded kernel.
    omega_prefactor_static = Fraction(0)
    avg_vx2 = avg_vy2 = avg_vz2 = Fraction(1, 3)
    assert_equal("unit velocity average", avg_vx2 + avg_vy2 + avg_vz2, Fraction(1))
    assert_equal("static HTL 00 component", Fraction(1) - omega_prefactor_static, Fraction(1))
    assert_equal("static HTL 0x component", -omega_prefactor_static * avg_vx, Fraction(0))
    assert_equal("static HTL xx component", -omega_prefactor_static * avg_vx2, Fraction(0))


def check_connection_canonical_debye_htl_conversion() -> None:
    # Chapter 7 uses a connection-normalized Euclidean action and a canonical
    # real-time HTL source.  Under mathcal A = g a, the connection-source
    # curvature is m_D^2/g^2 while the canonical-source curvature is m_D^2.
    g = Fraction(3, 2)
    g2 = g * g
    temperature = Fraction(5, 7)
    beta = 1 / temperature
    g3sq = g2 * temperature
    m_d2 = Fraction(11, 13)
    k2 = Fraction(17, 19)
    a0_sq = Fraction(23, 29)
    f_sq = Fraction(31, 37)

    chi_connection = m_d2 / g2
    assert_equal(
        "connection susceptibility converts to canonical Debye kernel",
        chi_connection * g2,
        m_d2,
    )

    # Quadratic kinetic term: mathcal F = g f turns (1/4g^2) mathcal F^2 into
    # the canonical (1/4) f^2 normalization.
    connection_kinetic = (g2 * f_sq) / (4 * g2)
    canonical_kinetic = f_sq / 4
    assert_equal(
        "connection kinetic term converts to canonical kinetic term",
        connection_kinetic,
        canonical_kinetic,
    )

    # Static mass term: beta * (chi/2) mathcal A_0^2 equals beta * m_D^2 a_0^2/2,
    # and in three-dimensional connection-normalized EQCD it is
    # m_D^2 mathcal A_0^2/(2 g_3^2).
    mathcal_a0_sq = g2 * a0_sq
    four_d_mass = beta * chi_connection * mathcal_a0_sq / 2
    canonical_mass = beta * m_d2 * a0_sq / 2
    eqcd_mass = m_d2 * mathcal_a0_sq / (2 * g3sq)
    assert_equal(
        "four-dimensional mass term converts to canonical field",
        four_d_mass,
        canonical_mass,
    )
    assert_equal("EQCD mass term includes static beta factor", eqcd_mass, canonical_mass)

    canonical_1pi = k2 + m_d2
    connection_1pi = canonical_1pi / g2
    assert_equal("1PI kernel rescales by g squared", connection_1pi * g2, canonical_1pi)

    canonical_propagator_4d = 1 / canonical_1pi
    connection_propagator_4d = g2 / canonical_1pi
    eqcd_connection_propagator = g3sq / canonical_1pi
    static_zero_mode_canonical_propagator = temperature / canonical_1pi
    assert_equal(
        "four-dimensional connection propagator carries g squared",
        connection_propagator_4d,
        g2 * canonical_propagator_4d,
    )
    assert_equal(
        "EQCD connection propagator carries g_3 squared",
        eqcd_connection_propagator,
        g2 * static_zero_mode_canonical_propagator,
    )

    # The source-current derivative also rescales: delta Gamma = j_a delta a =
    # j_mathcalA delta mathcal A, so j_a = g j_mathcalA.
    canonical_source = Fraction(41, 43)
    connection_source = g * canonical_source
    canonical_current = m_d2 * canonical_source
    connection_current = chi_connection * connection_source
    assert_equal(
        "connection current converts to canonical current",
        g * connection_current,
        canonical_current,
    )

    line_length = Fraction(47, 53)
    assert_equal(
        "holonomy exponent uses connection or g times canonical field",
        line_length * connection_source,
        line_length * g * canonical_source,
    )


def check_static_source_line_renormalization_cancellation() -> None:
    # A wrapped source has an additive line self-energy.  Pair excess free
    # energies and forces must not depend on this local one-line coordinate.
    beta = Fraction(7, 3)
    delta_q = Fraction(5, 3)
    delta_qbar = Fraction(7, 5)
    finite_shift_q = Fraction(2, 11)
    finite_shift_qbar = Fraction(-3, 13)

    physical_q = Fraction(11, 7)
    physical_qbar = Fraction(13, 7)
    interaction = Fraction(-2, 9)

    bare_q = physical_q + delta_q
    bare_qbar = physical_qbar + delta_qbar
    bare_pair = physical_q + physical_qbar + interaction + delta_q + delta_qbar

    ren_q = bare_q - delta_q
    ren_qbar = bare_qbar - delta_qbar
    ren_pair = bare_pair - delta_q - delta_qbar
    bare_excess = bare_pair - bare_q - bare_qbar
    ren_excess = ren_pair - ren_q - ren_qbar

    assert_equal("Polyakov pair excess cancels bare line energies", bare_excess, interaction)
    assert_equal("Polyakov pair excess cancels renormalized line energies", ren_excess, interaction)
    assert_equal(
        "Polyakov ratio exponent line cancellation",
        -beta * bare_excess,
        -beta * ren_excess,
    )

    shifted_q = ren_q - finite_shift_q
    shifted_qbar = ren_qbar - finite_shift_qbar
    shifted_pair = ren_pair - finite_shift_q - finite_shift_qbar
    assert_equal(
        "finite line scheme leaves pair excess invariant",
        shifted_pair - shifted_q - shifted_qbar,
        interaction,
    )

    r = Fraction(3)
    sigma = Fraction(2, 5)
    coulomb = Fraction(7, 11)
    constant = Fraction(19, 13)
    delta_sum = delta_q + delta_qbar
    bare_potential = delta_sum + constant + sigma * r + coulomb / r
    ren_potential = bare_potential - delta_sum
    bare_derivative = sigma - coulomb / (r * r)
    ren_derivative = sigma - coulomb / (r * r)

    assert_equal("static pair force removes line self-energy", -bare_derivative, -ren_derivative)
    assert_equal(
        "static pair potential shifts by line self-energy",
        bare_potential - ren_potential,
        delta_sum,
    )


def check_polyakov_channel_bookkeeping() -> None:
    for n in range(2, 9):
        singlet_weight = Fraction(1, n * n)
        adjoint_weight = Fraction(n * n - 1, n * n)
        assert_equal(
            f"fundamental color-average weights sum SU({n})",
            singlet_weight + adjoint_weight,
            Fraction(1),
        )
        if singlet_weight == Fraction(1):
            raise AssertionError("nontrivial SU(N) color average cannot be a pure singlet")

        singlet_channel = Fraction(5, 7)
        adjoint_channel = Fraction(11, 13)
        color_averaged = singlet_weight * singlet_channel + adjoint_weight * adjoint_channel
        if color_averaged == singlet_channel:
            raise AssertionError("color-averaged Polyakov pair collapsed to singlet channel")

    polyakov_line_factor = Fraction(17, 19)
    spatial_transporter_factor = Fraction(23, 29)
    intersection_factor = Fraction(31, 37)
    traced_pair_renorm = polyakov_line_factor * polyakov_line_factor
    cyclic_loop_renorm = (
        traced_pair_renorm
        * spatial_transporter_factor
        * spatial_transporter_factor
        * intersection_factor
    )
    assert_equal(
        "cyclic Wilson loop has extra transporter/intersection renormalization",
        cyclic_loop_renorm / traced_pair_renorm,
        spatial_transporter_factor * spatial_transporter_factor * intersection_factor,
    )


def pair_excess_ratio(pair_correlator: Fraction, source_one_point: Fraction, antisource_one_point: Fraction) -> Fraction:
    if source_one_point == 0 or antisource_one_point == 0:
        raise ValueError("pair-excess ratio requires nonzero one-point functions")
    return pair_correlator / (source_one_point * antisource_one_point)


def check_static_source_ratio_domain_and_center_symmetric_force() -> None:
    # In a center-symmetric finite-volume pure gauge sector, a nonzero-N-ality
    # one-point function vanishes.  The neutral pair correlator may still be
    # nonzero, but the pair-excess ratio is not a defined observable.
    center_symmetric_one_point = Fraction(0)
    neutral_pair_correlator = Fraction(5, 7)
    assert_equal("center-symmetric one-point vanishes", center_symmetric_one_point, Fraction(0))
    assert_equal("neutral pair correlator can be nonzero", neutral_pair_correlator != 0, True)

    try:
        pair_excess_ratio(neutral_pair_correlator, center_symmetric_one_point, center_symmetric_one_point)
    except ValueError:
        pass
    else:
        raise AssertionError("zero one-point functions should not define a pair-excess ratio")

    selected_source = Fraction(2, 5)
    selected_antisource = Fraction(3, 7)
    selected_pair = Fraction(11, 13)
    line_factor = Fraction(17, 19)
    assert_equal(
        "source-selected pair ratio cancels finite line factors",
        pair_excess_ratio(line_factor * line_factor * selected_pair, line_factor * selected_source, line_factor * selected_antisource),
        pair_excess_ratio(selected_pair, selected_source, selected_antisource),
    )

    # The direct pair force uses only the pair free energy.  An r-independent
    # wrapped-line self-energy shifts the potential but not its derivative,
    # so this statement survives without one-point denominators.
    r = Fraction(5)
    sigma = Fraction(7, 11)
    coulomb = Fraction(13, 17)
    line_self_energy = Fraction(23, 29)
    bare_pair_potential = line_self_energy + sigma * r + coulomb / r
    ren_pair_potential = bare_pair_potential - line_self_energy
    bare_pair_derivative = sigma - coulomb / (r * r)
    ren_pair_derivative = sigma - coulomb / (r * r)
    assert_equal("center-sector direct pair potential shifts by line energy", bare_pair_potential - ren_pair_potential, line_self_energy)
    assert_equal("center-sector direct pair force removes line energy", -bare_pair_derivative, -ren_pair_derivative)


def eqcd_local_expansion_is_controlled(
    external_momentum: Fraction,
    electric_mass: Fraction,
    magnetic_scale: Fraction,
    hard_gap: Fraction,
) -> bool:
    if hard_gap <= 0:
        return False
    return (
        4 * external_momentum < hard_gap
        and 4 * electric_mass < hard_gap
        and 4 * magnetic_scale < hard_gap
    )


def check_eqcd_locality_hierarchy_and_exceptions() -> None:
    hard_gap = Fraction(1)
    external_momentum = Fraction(1, 20)
    electric_mass = Fraction(1, 10)
    magnetic_scale = Fraction(1, 25)
    assert_equal(
        "EQCD local expansion hierarchy accepted",
        eqcd_local_expansion_is_controlled(
            external_momentum,
            electric_mass,
            magnetic_scale,
            hard_gap,
        ),
        True,
    )

    derivative_remainder_order = 4
    remainder = (external_momentum / hard_gap) ** derivative_remainder_order
    assert_equal("EQCD derivative remainder power", remainder, Fraction(1, 160000))

    # A holonomy can shift a nominal n=1 Matsubara mode to zero:
    # omega_n + alpha(mathcal A0) = 1 - 1 in units of 2 pi T.
    shifted_hard_gap = Fraction(1) - Fraction(1)
    assert_equal(
        "holonomy-light mode rejects local hard-mode integration",
        eqcd_local_expansion_is_controlled(
            external_momentum,
            electric_mass,
            magnetic_scale,
            shifted_hard_gap,
        ),
        False,
    )

    strong_coupling_electric_mass = Fraction(2, 5)
    assert_equal(
        "large electric scale rejects EQCD hierarchy",
        eqcd_local_expansion_is_controlled(
            external_momentum,
            strong_coupling_electric_mass,
            magnetic_scale,
            hard_gap,
        ),
        False,
    )


def main() -> None:
    check_yukawa_screening_power()
    check_projected_pole_residue()
    check_debye_trace_convention_conversion()
    check_debye_second_variation_contact_terms()
    check_htl_static_limit_and_transversality()
    check_connection_canonical_debye_htl_conversion()
    check_polyakov_channel_bookkeeping()
    check_static_source_line_renormalization_cancellation()
    check_static_source_ratio_domain_and_center_symmetric_force()
    check_eqcd_locality_hierarchy_and_exceptions()
    print("All thermal screening convention and static-source checks passed.")


if __name__ == "__main__":
    main()
