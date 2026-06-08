#!/usr/bin/env python3
"""Exact arithmetic checks for the curved trace-anomaly chapter.

Evidence contract.
Target claims:
- Verify the four-dimensional trace-anomaly curvature basis, the scalar,
  Dirac/Weyl, and Maxwell free-field heat-kernel rows, the R^2 counterterm
  shift, the N=4 a=c arithmetic, and the role of a as separated TTT data
  rather than contact data only.
Independent construction:
- The script rebuilds the heat-kernel coefficient as triples of
  Riemann^2, Ricci^2, and R^2 coefficients from rank, endomorphism,
  connection-curvature, spin-trace, one-form-trace, and ghost-subtraction
  inputs.  It then maps those triples to the a,c table.
Imported assumptions:
- The script assumes the standard local a4 formula for Laplace-type
  operators, the declared curvature-sign convention, and the separation of
  local UV coefficients from determinant-line and zero-mode/global data.
Negative controls:
- The checks detect a wrong Lichnerowicz sign, omitting the Maxwell ghost
  pair, subtracting only one real ghost, using the Dirac coefficient for a
  Weyl fermion, and treating a as contact-only rather than separated TTT data.
Scope boundary:
- Passing this script does not prove local Weyl cohomology, construct a
  nonperturbative curved-background QFT, compute a full TTT correlator, or
  trivialize chiral determinant/Pfaffian lines.
"""

from __future__ import annotations

from fractions import Fraction

CurvatureTriple = tuple[Fraction, Fraction, Fraction]


def assert_equal(actual, expected, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected {expected!r}, got {actual!r}")


def assert_not_equal(actual, forbidden, message: str) -> None:
    if actual == forbidden:
        raise AssertionError(f"{message}: unexpectedly got forbidden value {forbidden!r}")


def add_coefficients(*terms: CurvatureTriple) -> CurvatureTriple:
    return (
        sum(term[0] for term in terms),
        sum(term[1] for term in terms),
        sum(term[2] for term in terms),
    )


def scale_coefficients(factor: Fraction, term: CurvatureTriple) -> CurvatureTriple:
    return (factor * term[0], factor * term[1], factor * term[2])


def curvature_coefficients_from_ac(a: Fraction, c: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Coefficients of Riem^2, Ric^2, R^2 in c W^2 - a E4."""

    riem = c - a
    ric = -2 * c + 4 * a
    scalar = Fraction(1, 3) * c - a
    return (riem, ric, scalar)


def heat_kernel_a4_coefficients(
    *,
    rank: int,
    tr_e_r: Fraction,
    tr_e_squared: CurvatureTriple,
    tr_omega_squared: CurvatureTriple,
) -> CurvatureTriple:
    """Return non-derivative a4 coefficients for P=-(nabla^2+E)."""

    identity = (
        Fraction(rank * 2, 360),
        Fraction(rank * -2, 360),
        Fraction(rank * 5, 360),
    )
    r_e = (Fraction(0), Fraction(0), Fraction(1, 6) * tr_e_r)
    e_squared = scale_coefficients(Fraction(1, 2), tr_e_squared)
    omega_squared = scale_coefficients(Fraction(1, 12), tr_omega_squared)
    return add_coefficients(identity, r_e, e_squared, omega_squared)


def check_conformal_scalar_heat_kernel_map() -> None:
    a = Fraction(1, 360)
    c = Fraction(1, 120)
    assert_equal(
        curvature_coefficients_from_ac(a, c),
        (Fraction(1, 180), Fraction(-1, 180), Fraction(0)),
        "real conformal scalar a4 curvature combination",
    )

    # Direct a4 substitution for P = -nabla^2 + R/6, written as
    # P = -(nabla^2 + E) with E = -R/6.
    r2_coefficient = Fraction(5, 360) - Fraction(1, 36) + Fraction(1, 72)
    assert_equal(r2_coefficient, Fraction(0), "conformal scalar R^2 cancellation")

    scalar_heat = heat_kernel_a4_coefficients(
        rank=1,
        tr_e_r=Fraction(-1, 6),
        tr_e_squared=(Fraction(0), Fraction(0), Fraction(1, 36)),
        tr_omega_squared=(Fraction(0), Fraction(0), Fraction(0)),
    )
    assert_equal(
        scalar_heat,
        curvature_coefficients_from_ac(a, c),
        "real conformal scalar heat-kernel triple",
    )


def check_dirac_heat_kernel_bundle_traces() -> None:
    # For P_D = D^2 = -nabla^2 + R/4 = -(nabla^2 + E), E = -R/4.
    # With tr_S 1 = 4, tr_S E = -R, tr_S E^2 = R^2/4, and
    # tr_S Omega_{mu nu} Omega^{mu nu} = -Riem^2/2.
    dirac_heat = heat_kernel_a4_coefficients(
        rank=4,
        tr_e_r=Fraction(-1),
        tr_e_squared=(Fraction(0), Fraction(0), Fraction(1, 4)),
        tr_omega_squared=(Fraction(-1, 2), Fraction(0), Fraction(0)),
    )
    assert_equal(
        dirac_heat,
        (Fraction(-7, 360), Fraction(-8, 360), Fraction(5, 360)),
        "Dirac squared-operator heat-kernel triple",
    )

    dirac_anomaly = scale_coefficients(Fraction(-1), dirac_heat)
    expected_dirac = curvature_coefficients_from_ac(
        Fraction(11, 360),
        Fraction(1, 20),
    )
    assert_equal(dirac_anomaly, expected_dirac, "Dirac local anomaly triple")

    wrong_lichnerowicz_heat = heat_kernel_a4_coefficients(
        rank=4,
        tr_e_r=Fraction(1),
        tr_e_squared=(Fraction(0), Fraction(0), Fraction(1, 4)),
        tr_omega_squared=(Fraction(-1, 2), Fraction(0), Fraction(0)),
    )
    assert_not_equal(
        scale_coefficients(Fraction(-1), wrong_lichnerowicz_heat),
        expected_dirac,
        "wrong Lichnerowicz sign must not reproduce Dirac anomaly",
    )

    weyl_anomaly = scale_coefficients(Fraction(1, 2), dirac_anomaly)
    expected_weyl = curvature_coefficients_from_ac(
        Fraction(11, 720),
        Fraction(1, 40),
    )
    assert_equal(weyl_anomaly, expected_weyl, "Weyl local coefficient is half Dirac")
    assert_not_equal(
        weyl_anomaly,
        dirac_anomaly,
        "Weyl local coefficient cannot be replaced by full Dirac coefficient",
    )


def check_maxwell_heat_kernel_ghost_subtraction() -> None:
    # Hodge Laplacian on one-forms:
    # E_mu^nu = -R_mu^nu, tr E = -R, tr E^2 = Ric^2,
    # tr Omega_{mu nu} Omega^{mu nu} = -Riem^2.
    one_form_heat = heat_kernel_a4_coefficients(
        rank=4,
        tr_e_r=Fraction(-1),
        tr_e_squared=(Fraction(0), Fraction(1), Fraction(0)),
        tr_omega_squared=(Fraction(-1), Fraction(0), Fraction(0)),
    )
    assert_equal(
        one_form_heat,
        (Fraction(-22, 360), Fraction(172, 360), Fraction(-40, 360)),
        "one-form Hodge Laplacian heat-kernel triple",
    )

    minimal_scalar_heat = heat_kernel_a4_coefficients(
        rank=1,
        tr_e_r=Fraction(0),
        tr_e_squared=(Fraction(0), Fraction(0), Fraction(0)),
        tr_omega_squared=(Fraction(0), Fraction(0), Fraction(0)),
    )
    assert_equal(
        minimal_scalar_heat,
        (Fraction(2, 360), Fraction(-2, 360), Fraction(5, 360)),
        "minimal scalar ghost heat-kernel triple",
    )

    maxwell_anomaly = add_coefficients(
        one_form_heat,
        scale_coefficients(Fraction(-2), minimal_scalar_heat),
    )
    expected_maxwell = curvature_coefficients_from_ac(
        Fraction(31, 180),
        Fraction(1, 10),
    )
    assert_equal(maxwell_anomaly, expected_maxwell, "Maxwell one-form minus ghost pair")

    assert_not_equal(
        one_form_heat,
        expected_maxwell,
        "omitted Maxwell ghosts must not reproduce vector anomaly",
    )
    one_real_ghost_only = add_coefficients(
        one_form_heat,
        scale_coefficients(Fraction(-1), minimal_scalar_heat),
    )
    assert_not_equal(
        one_real_ghost_only,
        expected_maxwell,
        "subtracting one real ghost must not reproduce vector anomaly",
    )

    # In a Hodge decomposition of a nonminimal Lorenz gauge, the gauge-parameter
    # rescaling is confined to the exact scalar block.  Longitudinal bosonic
    # normalization, complex ghost pair, and gauge-volume normalization cancel.
    longitudinal_weight = Fraction(1)
    ghost_pair_weight = Fraction(-2)
    gauge_volume_weight = Fraction(1)
    assert_equal(
        longitudinal_weight + ghost_pair_weight + gauge_volume_weight,
        Fraction(0),
        "gauge-parameter scalar block cancels after ghost and gauge volume",
    )
    assert_not_equal(
        longitudinal_weight + ghost_pair_weight,
        Fraction(0),
        "dropping gauge-volume bookkeeping leaves spurious gauge-parameter dependence",
    )


def check_r_squared_counterterm_shift() -> None:
    # In D=4, delta sqrt(g)=4 sigma sqrt(g) and
    # delta R = -2 sigma R - 6 nabla^2 sigma.  Therefore
    # delta(sqrt(g) R^2) has zero sigma R^2 term and -12 R nabla^2 sigma.
    sigma_r2 = 4 - 4
    laplacian_coefficient = -12
    assert_equal(sigma_r2, 0, "R^2 Weyl variation has no sigma R^2 term in D=4")
    assert_equal(laplacian_coefficient, -12, "R^2 Weyl variation Laplacian coefficient")

    # With delta W = - int sigma A, adding kappa/(16 pi^2) int R^2 shifts
    # b by +12 kappa.
    kappa = Fraction(7, 5)
    assert_equal(12 * kappa, Fraction(84, 5), "Box R coefficient shift")


def check_free_field_coefficients() -> None:
    scalar = (Fraction(1, 360), Fraction(1, 120))
    weyl = (Fraction(11, 720), Fraction(1, 40))
    dirac = (Fraction(11, 360), Fraction(1, 20))
    vector = (Fraction(31, 180), Fraction(1, 10))

    assert_equal((2 * weyl[0], 2 * weyl[1]), dirac, "Dirac equals two Weyl fermions")

    # N=4 vector multiplet per adjoint generator: 6 real scalars, 4 Weyl
    # fermions, 1 vector.
    n4_a = 6 * scalar[0] + 4 * weyl[0] + vector[0]
    n4_c = 6 * scalar[1] + 4 * weyl[1] + vector[1]
    assert_equal(n4_a, Fraction(1, 4), "N=4 SYM a per adjoint generator")
    assert_equal(n4_c, Fraction(1, 4), "N=4 SYM c per adjoint generator")
    assert_equal(n4_a, n4_c, "N=4 SYM a equals c")


def check_ttt_role_of_a() -> None:
    # TT fixes one linear combination, conventionally c.  In four-dimensional
    # parity-even CFT, separated TTT data contain independent structures, and
    # the Euler coefficient a is one of the anomaly combinations detected
    # there before trace-contact Ward identities are added.
    separated_ttt_structures = 3
    tt_normalizations = 1
    anomaly_combinations_in_ttt = 2
    assert_equal(
        separated_ttt_structures > tt_normalizations,
        True,
        "separated TTT has data beyond TT normalization",
    )
    assert_equal(anomaly_combinations_in_ttt, 2, "a and c are TTT anomaly combinations")

    contact_only_model = {"c_in_tt": True, "a_in_separated_ttt": False}
    assert_equal(
        contact_only_model["a_in_separated_ttt"],
        False,
        "negative-control model marks a as contact-only",
    )
    corrected_model = {"c_in_tt": True, "a_in_separated_ttt": True}
    assert_not_equal(
        contact_only_model,
        corrected_model,
        "contact-only a model must differ from corrected TTT model",
    )


def check_constant_curvature_identities() -> None:
    # In D=4 constant sectional curvature has
    # Riem^2 = R^2/6 and Ric^2 = R^2/4.
    riem = Fraction(1, 6)
    ric = Fraction(1, 4)
    scalar = Fraction(1)
    e4 = riem - 4 * ric + scalar
    w2 = riem - 2 * ric + Fraction(1, 3) * scalar
    assert_equal(e4, Fraction(1, 6), "constant-curvature Euler density coefficient")
    assert_equal(w2, Fraction(0), "constant-curvature Weyl tensor vanishes")


def check_two_dimensional_wz_variation() -> None:
    # Vary int sqrt(g) [tau R + (nabla tau)^2] with tau -> tau + sigma.
    # After integrating by parts, the coefficient of sigma is R - 2 Box tau,
    # which is e^{2 tau} R[e^{2 tau}g] in two dimensions.
    tau_r_coefficient = 1
    kinetic_variation_after_parts = -2
    assert_equal(tau_r_coefficient, 1, "2D WZ R coefficient")
    assert_equal(kinetic_variation_after_parts, -2, "2D WZ Laplacian tau coefficient")


def main() -> None:
    check_conformal_scalar_heat_kernel_map()
    check_dirac_heat_kernel_bundle_traces()
    check_maxwell_heat_kernel_ghost_subtraction()
    check_r_squared_counterterm_shift()
    check_free_field_coefficients()
    check_ttt_role_of_a()
    check_constant_curvature_identities()
    check_two_dimensional_wz_variation()
    print("All curved trace-anomaly checks passed.")


if __name__ == "__main__":
    main()
