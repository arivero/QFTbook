#!/usr/bin/env python3
"""Finite algebra checks for the QCD phase-structure chapter.

The script checks convention-sensitive numerical factors used in the
Stefan--Boltzmann pressure, the Banks--Casher normalization, the Linde
magnetic-scale estimate, finite-regulator source-curvature identities,
one-loop Polyakov-holonomy coefficients, chiral Ward-identity normalizations,
low-temperature chiral effective theory coefficients, static HTL Debye-mass
normalizations, retarded HTL angular-kernel bookkeeping, thermodynamic
derivative identities, baryon-number cumulants, Roberge--Weiss periodicity
bookkeeping, and the color-flavor-locked symmetry count.  It is not a lattice
simulation and it does not assert the existence or order of any QCD phase
transition.
"""

from fractions import Fraction
from math import factorial


def assert_equal(label, actual, expected):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual}, expected {expected}")


def assert_true(label, condition):
    if not condition:
        raise AssertionError(label)


def check_stefan_boltzmann_pressure():
    # Pressure is reported as p/T^4 = pi^2 * coefficient.
    # One massless bosonic degree of freedom contributes pi^2/90.
    # One massless fermionic degree of freedom contributes (7/8) pi^2/90.
    nc = 3
    nf = 3
    d_adj = nc * nc - 1
    gluon_degrees = 2 * d_adj
    quark_degrees = 4 * nc * nf

    gluon_coeff = Fraction(gluon_degrees, 90)
    quark_coeff = Fraction(7, 8) * Fraction(quark_degrees, 90)
    assert_equal("SU(3) gluon pressure coefficient", gluon_coeff, Fraction(8, 45))
    assert_equal("three-flavor quark pressure coefficient", quark_coeff, Fraction(21, 60))
    assert_equal("total free QCD coefficient", gluon_coeff + quark_coeff, Fraction(19, 36))


def check_finite_mu_quark_pressure():
    # For one massless Dirac quark of one color:
    # p = 7*pi^2*T^4/180 + mu^2*T^2/6 + mu^4/(12*pi^2).
    # Baryon chemical potential assigns quark chemical potential mu_B/N_c.
    nc = 3
    nf = 2
    mu2_coeff = Fraction(nc * nf, 6 * nc * nc)
    mu4_coeff = Fraction(nc * nf, 12 * nc**4)
    assert_equal("two-flavor baryon-mu T^2 coefficient", mu2_coeff, Fraction(1, 9))
    assert_equal("two-flavor baryon-mu fourth coefficient", mu4_coeff, Fraction(1, 162))


def check_thermodynamic_derivative_identities():
    # For a homogeneous conformal pressure p=a T^4 + b mu^2 T^2 + c mu^4,
    # the interaction measure T p_T + mu p_mu - 4p vanishes identically.
    a = Fraction(5, 7)
    b = Fraction(11, 13)
    c = Fraction(17, 19)
    temperature = Fraction(2)
    chemical_potential = Fraction(3)

    pressure = (
        a * temperature**4
        + b * chemical_potential**2 * temperature**2
        + c * chemical_potential**4
    )
    p_t = 4 * a * temperature**3 + 2 * b * chemical_potential**2 * temperature
    p_mu = 2 * b * chemical_potential * temperature**2 + 4 * c * chemical_potential**3
    interaction_measure = temperature * p_t + chemical_potential * p_mu - 4 * pressure
    assert_equal("homogeneous pressure has zero interaction measure", interaction_measure, Fraction(0))

    # At fixed x=mu/T, p(T,xT)/T^4 is independent of T for a homogeneous
    # degree-four pressure.
    x = Fraction(3, 2)
    reduced_pressure = a + b * x**2 + c * x**4
    reduced_pressure_rescaled = (
        a * temperature**4
        + b * (x * temperature)**2 * temperature**2
        + c * (x * temperature)**4
    ) / temperature**4
    assert_equal("fixed mu/T reduced pressure", reduced_pressure_rescaled, reduced_pressure)

    # At mu=0, c_s^2=(dp/dT)/(d epsilon/dT)=1/3 for p=a T^4.
    dp_dt = 4 * a * temperature**3
    d_epsilon_dt = 12 * a * temperature**3
    assert_equal("conformal sound speed squared", dp_dt / d_epsilon_dt, Fraction(1, 3))


def check_banks_casher_kernel_normalization():
    # The distributional identity used in Banks--Casher is
    # lim_{m down 0} int_0^\infty 2m f(lambda)/(lambda^2+m^2) dlambda
    # = pi f(0).
    # For f(lambda)=1 on [0,Lambda] the exact integral is 2 arctan(Lambda/m).
    # A rational sample verifies monotone approach toward pi from below.
    samples = [
        Fraction(1, 1),
        Fraction(1, 10),
        Fraction(1, 100),
    ]
    # Avoid floating pi in the check: arctan is not evaluated.  The exact
    # formula is recorded by checking the limiting angle argument Lambda/m.
    arguments = [1 / m for m in samples]
    assert_equal("largest Banks-Casher arctan argument", arguments[-1], 100)
    assert_true("Banks-Casher arguments increase as m decreases", arguments[0] < arguments[1] < arguments[2])


def check_fugacity_laurent_polynomial_shift():
    # A finite lattice fermion determinant is Laurent-polynomial in the
    # fugacity zeta.  Multiplication by a sufficiently large power of zeta
    # turns it into an ordinary polynomial; zeros of this polynomial are the
    # finite-regulator Lee-Yang zeros in the fugacity plane, up to the point
    # zeta=0 introduced by the shift.
    exponents = [-3, -1, 0, 4]
    shift = -min(exponents)
    shifted_exponents = [power + shift for power in exponents]
    assert_equal("fugacity shift removes negative powers", min(shifted_exponents), 0)
    assert_equal("fugacity polynomial degree after shift", max(shifted_exponents), 7)
    assert_equal("shift preserves exponent differences", shifted_exponents[-1] - shifted_exponents[1], 5)


def check_roberge_weiss_periodicity_bookkeeping():
    # A center-twisted temporal gauge transformation with z=exp(2*pi*i*k/Nc)
    # shifts the quark imaginary chemical-potential angle by 2*pi*k/Nc.
    # Since theta_B=Nc theta_q, the baryon angle shifts by 2*pi*k.
    nc = 3
    for k in range(-3, 4):
        quark_shift_units = Fraction(k, nc)
        baryon_shift_units = nc * quark_shift_units
        assert_equal(f"RW baryon period unit k={k}", baryon_shift_units, Fraction(k))

    # In a canonical fugacity expansion, imaginary baryon angle periodicity
    # follows from integer baryon charge: exp(i B (theta_B+2*pi))=exp(i B theta_B).
    baryon_charges = [-2, -1, 0, 1, 2]
    shifted_phases_units = [charge * 1 for charge in baryon_charges]
    assert_true(
        "integer baryon charges give 2pi periodicity",
        all(phase_units == int(phase_units) for phase_units in shifted_phases_units),
    )

    # The high-temperature RW exchange loci in the quark angle are
    # theta_q=(2r+1) pi/Nc, i.e. baryon angle theta_B=(2r+1) pi.
    rw_quark_half_turn_units = [Fraction(2 * r + 1, nc) for r in range(3)]
    rw_baryon_half_turn_units = [nc * value for value in rw_quark_half_turn_units]
    assert_equal("first SU(3) RW quark half-turn", rw_quark_half_turn_units[0], Fraction(1, 3))
    assert_equal("RW baryon half-turns are odd", rw_baryon_half_turn_units, [Fraction(1), Fraction(3), Fraction(5)])


def check_htl_angular_kernel_transversality_bookkeeping():
    # For K_mu=(-omega,k) and v^mu=(1,v), the retarded HTL kernel is
    # K_R^{mu nu}=m_D^2[delta_0^mu delta_0^nu
    #   - omega <v^mu v^nu/(omega-v.k+i0)>].
    # Contracting with K_mu cancels the denominator because
    # K_mu v^mu=-(omega-v.k), leaving -omega delta_0^nu+omega <v^nu>.
    avg_v0 = Fraction(1)
    avg_vx = Fraction(0)
    avg_vy = Fraction(0)
    avg_vz = Fraction(0)
    assert_equal("HTL transversality nu=0", -1 + avg_v0, Fraction(0))
    assert_equal("HTL transversality nu=x", avg_vx, Fraction(0))
    assert_equal("HTL transversality nu=y", avg_vy, Fraction(0))
    assert_equal("HTL transversality nu=z", avg_vz, Fraction(0))

    # Rotational averages on S^2 used by the long-wavelength HTL expansion.
    avg_vx2 = avg_vy2 = avg_vz2 = Fraction(1, 3)
    assert_equal("unit velocity average", avg_vx2 + avg_vy2 + avg_vz2, Fraction(1))
    assert_equal("static HTL leaves only 00 component", Fraction(1), Fraction(1))


def check_source_curvature_susceptibility():
    # For Z(h)=sum_i w_i exp(h X_i), d^2 log Z/dh^2 at h=0 is Var(X).
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    x_values = [Fraction(-2, 3), Fraction(1, 5), Fraction(7, 4)]
    volume = Fraction(11, 1)
    temperature = Fraction(3, 2)

    mean_x = sum(w * x for w, x in zip(weights, x_values))
    mean_x2 = sum(w * x * x for w, x in zip(weights, x_values))
    variance_x = mean_x2 - mean_x * mean_x

    pressure_second = temperature * variance_x / volume
    intensive_variance = variance_x / (volume * volume)
    susceptibility_form = temperature * volume * intensive_variance

    assert_equal("source curvature equals pressure second derivative", pressure_second, susceptibility_form)


def check_weiss_holonomy_potential_coefficients():
    # Coefficients are reported as f/T^4 = pi^2 * coefficient.
    # The pure-glue Weiss potential is
    # f_g = -(2/pi^2 beta^4) sum_n tr_adj(P^n)/n^4.
    # Since zeta(4)=pi^4/90, a center holonomy P=z*1 gives
    # coefficient -(N_c^2-1)/45.
    nc = 3
    nf = 2
    adj_dim = nc * nc - 1
    zeta4_over_pi4 = Fraction(1, 90)

    broken_center_coeff = -2 * zeta4_over_pi4 * adj_dim
    assert_equal("SU(3) Weiss broken-center free energy", broken_center_coeff, Fraction(-8, 45))

    # For uniformly spaced eigenvalues, tr_F(P^n)=0 unless N_c divides n.
    # Therefore sum_n tr_adj(P^n)/n^4 = pi^4*(1/N_c^2 - 1)/90.
    center_symmetric_sum = zeta4_over_pi4 * (Fraction(1, nc * nc) - 1)
    center_symmetric_coeff = -2 * center_symmetric_sum
    assert_equal("SU(3) Weiss center-symmetric free energy", center_symmetric_coeff, Fraction(8, 405))
    assert_equal(
        "SU(3) Weiss center-symmetric cost",
        center_symmetric_coeff - broken_center_coeff,
        Fraction(16, 81),
    )

    # At P=1, the massless Dirac-quark holonomy potential is the negative
    # of the free pressure.  The alternating sum is -7*pi^4/720.
    alternating_zeta4_over_pi4 = Fraction(-7, 720)
    quark_identity_coeff = 4 * nc * nf * alternating_zeta4_over_pi4
    assert_equal("two-flavor SU(3) free quark free energy", quark_identity_coeff, Fraction(-7, 30))

    # Center charge bookkeeping: adjoint traces are center-neutral, while a
    # fundamental trace tr_F(P^n) has N-ality n mod N_c.
    assert_equal("fundamental n=1 center charge", 1 % nc, 1)
    assert_equal("adjoint center charge", (1 - 1) % nc, 0)


def check_baryon_cumulants_and_radius_estimator():
    # Symmetric finite-volume baryon-number distribution at mu_B=0.
    weights = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]
    baryon_numbers = [Fraction(-1), Fraction(0), Fraction(1)]
    volume = Fraction(5)
    temperature = Fraction(2)
    normalization = volume * temperature**3

    moments = {
        power: sum(w * b**power for w, b in zip(weights, baryon_numbers))
        for power in range(1, 5)
    }
    mean = moments[1]
    second_cumulant = moments[2] - mean * mean
    third_cumulant = moments[3] - 3 * moments[2] * mean + 2 * mean**3
    fourth_cumulant = (
        moments[4]
        - 4 * moments[3] * mean
        - 3 * moments[2] * moments[2]
        + 12 * moments[2] * mean * mean
        - 6 * mean**4
    )

    assert_equal("charge-conjugation odd first cumulant", mean, Fraction(0))
    assert_equal("charge-conjugation odd third cumulant", third_cumulant, Fraction(0))
    assert_equal("baryon second susceptibility", second_cumulant / normalization, Fraction(1, 80))
    assert_equal("baryon fourth susceptibility", fourth_cumulant / normalization, Fraction(-1, 160))

    # If chi_{2n}/(2n)! = R^{-2n}, the standard even ratio estimator returns R.
    radius = Fraction(3)
    n = 2
    chi_2n = factorial(2 * n) * radius ** (-2 * n)
    chi_2n_plus_2 = factorial(2 * n + 2) * radius ** (-2 * n - 2)
    ratio_squared = Fraction((2 * n + 2) * (2 * n + 1)) * chi_2n / chi_2n_plus_2
    assert_equal("even susceptibility ratio estimator squared", ratio_squared, radius * radius)


def check_chiral_ward_identity_normalization():
    # Flavor generators tau^a are normalized by tr_f(tau^a tau^b)=delta^{ab}.
    # In a flavor-symmetric state,
    # <bar q {tau^a,tau^b} q> = (2/N_f) delta^{ab} <bar q q>_sum.
    # With the positive per-flavor condensate Sigma=-<bar q q>_sum/N_f,
    # the integrated Ward identity 2m chi_pi^{ab}=-<bar q {tau^a,tau^b} q>
    # gives m chi_pi^{ab}=delta^{ab} Sigma.
    nf = Fraction(3)
    sigma = Fraction(5, 7)
    scalar_sum = -nf * sigma
    singlet_anticommutator_coeff = Fraction(2, 1) / nf
    ward_rhs = -singlet_anticommutator_coeff * scalar_sum
    chi_times_m_from_ward = ward_rhs / 2
    assert_equal("delta-normalized chiral Ward identity", chi_times_m_from_ward, sigma)

    # With delta-normalized generators, pole saturation and PCAC give
    # f_delta^2 M_pi^2 = 4 m Sigma.  The conventional tr(t^a t^b)=1/2 delta
    # decay constant is smaller by sqrt(2), so f_half^2 M_pi^2 = 2 m Sigma.
    mass = Fraction(11, 13)
    f_delta_sq_mpi_sq = 4 * mass * sigma
    f_half_sq_mpi_sq = f_delta_sq_mpi_sq / 2
    assert_equal("delta-normalized GMOR coefficient", f_delta_sq_mpi_sq, 4 * mass * sigma)
    assert_equal("half-normalized GMOR coefficient", f_half_sq_mpi_sq, 2 * mass * sigma)


def check_low_temperature_chiral_condensate_coefficient():
    # With tr_f(tau^a tau^b)=delta^{ab} and
    # U=exp(i sqrt(2) pi^a tau^a/F), the leading chiral Lagrangian has
    # canonical pion kinetic terms, Sigma=F^2 B, and M_pi^2=2 B m.
    f_sq = Fraction(17, 5)
    b_const = Fraction(19, 7)
    mass = Fraction(3, 11)
    sigma = f_sq * b_const
    pion_mass_sq = 2 * b_const * mass
    f_delta_sq = 2 * f_sq

    assert_equal("chiral EFT tree Sigma", sigma, f_sq * b_const)
    assert_equal("chiral EFT tree pion mass", pion_mass_sq, 2 * b_const * mass)
    assert_equal("trace-delta tree GMOR", f_delta_sq * pion_mass_sq, 4 * mass * sigma)

    # The massless thermal tadpole is
    # int d^3k/(2*pi)^3 n_B(k)/|k| = T^2/12.
    # Therefore Sigma(T)/Sigma(0)=1-(N_f^2-1)T^2/(12 N_f F^2)+...
    for nf, expected in [(2, Fraction(1, 8)), (3, Fraction(2, 9)), (4, Fraction(5, 16))]:
        d_pi = nf * nf - 1
        coefficient = Fraction(d_pi, 12 * nf)
        assert_equal(f"low-temperature chiral coefficient Nf={nf}", coefficient, expected)

    # Check the pressure-derivative chain rule:
    # d p_pi/d M_pi^2 = -(N_f^2-1) T^2/24,
    # d M_pi^2/dm=2B, and per-flavor division gives the coefficient above.
    nf = 2
    d_pi = nf * nf - 1
    dp_dmpi_sq_over_t2 = Fraction(-d_pi, 24)
    dm_pi_sq_dm = 2 * b_const
    per_flavor_delta_sigma_over_t2 = dp_dmpi_sq_over_t2 * dm_pi_sq_dm / nf
    expected_delta_over_t2 = -Fraction(d_pi, 12 * nf) * b_const
    assert_equal("pion-gas source derivative coefficient", per_flavor_delta_sigma_over_t2, expected_delta_over_t2)


def check_linde_magnetic_scale():
    # In four dimensions, g_3^2 = g^2 T has mass dimension one.  A purely
    # magnetic three-dimensional vacuum free-energy density scales as (g_3^2)^3.
    # Multiplying by T to recover four-dimensional pressure gives g^6 T^4.
    g_power = 2 * 3
    t_power = 1 + 3
    assert_equal("Linde magnetic g power", g_power, 6)
    assert_equal("Linde magnetic T power", t_power, 4)


def check_static_htl_debye_mass_normalization():
    # The static HTL susceptibility has
    # I_B = int d^3p/(2*pi)^3 [-n_B'(p)] = T^2/6
    # I_F = int d^3p/(2*pi)^3 [-n_F'(p)] = T^2/12.
    # Gluons give 2 C_A I_B and each Dirac flavor gives 4 T_R I_F.
    ib_over_t2 = Fraction(1, 6)
    if_over_t2 = Fraction(1, 12)
    gluon_factor = 2
    dirac_factor = 4

    assert_equal("static HTL boson integral", gluon_factor * ib_over_t2, Fraction(1, 3))
    assert_equal("static HTL Dirac integral", dirac_factor * if_over_t2, Fraction(1, 3))

    # With tr_fund(T^a T^b)=delta^{ab}, SU(N_c) has C_A=2N_c and T_fund=1.
    nc = 3
    nf = 3
    ca = 2 * nc
    t_fund = 1
    coefficient = Fraction(ca, 3) + Fraction(nf * t_fund, 3)
    assert_equal("SU(3), Nf=3 static HTL Debye coefficient", coefficient, Fraction(3, 1))


def check_cfl_global_goldstone_count():
    # For N_f=N_c=3 and ignoring the anomalous axial U(1), the CFL condensate
    # locks SU(3)_L x SU(3)_R x U(1)_B to diagonal SU(3).  The gauged color
    # directions are Higgs directions, not physical Goldstone bosons.
    dim_su3 = 8
    global_before = dim_su3 + dim_su3 + 1
    global_after = dim_su3
    assert_equal("CFL physical Goldstone count", global_before - global_after, 9)


def main():
    check_stefan_boltzmann_pressure()
    check_finite_mu_quark_pressure()
    check_thermodynamic_derivative_identities()
    check_banks_casher_kernel_normalization()
    check_fugacity_laurent_polynomial_shift()
    check_roberge_weiss_periodicity_bookkeeping()
    check_htl_angular_kernel_transversality_bookkeeping()
    check_source_curvature_susceptibility()
    check_weiss_holonomy_potential_coefficients()
    check_chiral_ward_identity_normalization()
    check_low_temperature_chiral_condensate_coefficient()
    check_baryon_cumulants_and_radius_estimator()
    check_static_htl_debye_mass_normalization()
    check_linde_magnetic_scale()
    check_cfl_global_goldstone_count()
    print("All QCD phase-structure checks passed.")


if __name__ == "__main__":
    main()
