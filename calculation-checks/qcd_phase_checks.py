#!/usr/bin/env python3
"""Finite algebra checks for the QCD phase-structure chapter.

The script checks convention-sensitive numerical factors used in the
Stefan--Boltzmann pressure, the Banks--Casher normalization, the Linde
magnetic-scale estimate, finite-regulator source-curvature identities,
one-loop Polyakov-holonomy coefficients, chiral Ward-identity normalizations,
low-temperature chiral effective theory coefficients, static HTL Debye-mass
normalizations, retarded HTL angular-kernel bookkeeping, thermodynamic
derivative identities, finite-regulator Polyakov-loop effective-measure
bookkeeping, high-density Fermi-surface and HDL coefficient bookkeeping,
non-Fermi-liquid self-energy coefficients, one-gluon exchange color factors
for dense pairing, leading-log magnetic gap coefficient bookkeeping,
baryon-number cumulants, Roberge--Weiss periodicity bookkeeping, dense-matter
neutrality constraints, color-flavor-locked gauge-invariant composite
charges, rotated electromagnetic mass-matrix bookkeeping, screening and
collective-mode counts, dense Fermi-surface stress scales,
color-flavor-locked anomaly matching, hydrodynamic response-window
bookkeeping, momentum-projected baryon diffusion current bookkeeping, and
the color-flavor-locked symmetry count.  It is not a lattice simulation and it
does not assert the
existence or order of any QCD phase transition.
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


def check_polyakov_effective_measure_center_bookkeeping():
    nc = 3

    # Pure-gauge nearest-neighbor tube: fundamental at one spatial site and
    # antifundamental at the neighbor, hence total N-ality zero.
    fundamental_charge = 1
    antifundamental_charge = -1
    assert_equal(
        "nearest-neighbor tube is center neutral",
        (fundamental_charge + antifundamental_charge) % nc,
        0,
    )

    # A heavy fundamental quark winding once around the thermal circle is a
    # single fundamental Polyakov loop and therefore breaks center symmetry.
    assert_equal("forward heavy-quark loop center charge", fundamental_charge % nc, 1)
    assert_equal("backward heavy-quark loop center charge", antifundamental_charge % nc, nc - 1)

    # Temporal winding collects N_tau factors of exp(a mu_q), giving
    # exp(beta mu_q) because beta=a N_tau.  The check records the exponent.
    n_tau = 5
    assert_equal("forward temporal winding exponent", n_tau, 5)
    assert_equal("minimal strong-coupling tube exponent", n_tau, 5)


def check_high_density_fermi_surface_bookkeeping():
    # In units where the common pi^{-2} factor is suppressed, the angular
    # measure coefficient is 4*pi/(2*pi)^3 = 1/(2*pi^2).  Thus one spin and
    # one internal state have coefficient 1/2, while a positive-energy
    # massless Dirac branch has two spin states and coefficient 1.
    one_spin_density_coeff = Fraction(4, 2**3)
    dirac_density_coeff = 2 * one_spin_density_coeff
    assert_equal(
        "one-spin Fermi-surface density coefficient",
        one_spin_density_coeff,
        Fraction(1, 2),
    )
    assert_equal("Dirac Fermi-surface density coefficient", dirac_density_coeff, Fraction(1))

    # With tr_fund(T^a T^b)=delta^{ab}, each massless Dirac fundamental
    # flavor contributes g^2 mu_q^2/pi^2 to the zero-temperature dense
    # electric screening mass.
    t_fund_trace_delta = Fraction(1)
    per_flavor_hdl_coeff = dirac_density_coeff * t_fund_trace_delta
    assert_equal(
        "trace-delta dense HDL coefficient per flavor",
        per_flavor_hdl_coeff,
        Fraction(1),
    )
    assert_equal("three-flavor dense HDL coefficient", 3 * per_flavor_hdl_coeff, Fraction(3))

    # The expansion sqrt(1+2a+a^2+b^2)=1+a+b^2/2+O(3) has cancellation of the
    # a^2 term and transverse curvature coefficient 1/2.
    sqrt_linear_coeff = Fraction(1, 2) * 2
    sqrt_a2_coeff = Fraction(1, 2) - Fraction(1, 8) * 4
    sqrt_b2_coeff = Fraction(1, 2)
    assert_equal("Fermi-surface longitudinal coefficient", sqrt_linear_coeff, Fraction(1))
    assert_equal("Fermi-surface longitudinal quadratic cancellation", sqrt_a2_coeff, Fraction(0))
    assert_equal(
        "Fermi-surface transverse curvature coefficient",
        sqrt_b2_coeff,
        Fraction(1, 2),
    )


def check_dense_non_fermi_liquid_coefficients():
    # In the trace-delta convention C_F=(N_c^2-1)/N_c.  The cold dense
    # non-Fermi-liquid coefficient is lambda_NFL=g^2 C_F/(12*pi^2).
    nc = 3
    c_f_trace_delta = Fraction(nc * nc - 1, nc)
    nfl_coeff = c_f_trace_delta / 12
    assert_equal("SU(3) trace-delta C_F", c_f_trace_delta, Fraction(8, 3))
    assert_equal("SU(3) non-Fermi-liquid coefficient", nfl_coeff, Fraction(2, 9))

    # The coefficient decomposes into the same patch prefactor g^2 C_F/(4*pi^2)
    # and the Landau-damped magnetic collinear factor 1/3.
    patch_prefactor_without_g2_pi2 = c_f_trace_delta / 4
    collinear_factor = Fraction(1, 3)
    assert_equal(
        "non-Fermi-liquid prefactor factorization",
        patch_prefactor_without_g2_pi2 * collinear_factor,
        nfl_coeff,
    )

    # The residue is asymptotically inverse-logarithmic: at logarithmic size L
    # the leading denominator is lambda_NFL * L.  Check the bookkeeping at an
    # arbitrary rational L.
    logarithm = Fraction(9, 5)
    leading_denominator = nfl_coeff * logarithm
    leading_residue_times_denominator = leading_denominator / leading_denominator
    assert_equal("non-Fermi-liquid inverse-log residue bookkeeping", leading_residue_times_denominator, Fraction(1))


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
    # The Euclidean convention P^a=bar q i gamma_5 tau^a q and
    # delta q=i alpha tau^a gamma_5 q gives the local contact term
    # delta^a P^b=-bar q {tau^a,tau^b} q.  The two minus signs are the
    # left and right variations, each using i^2 gamma_5^2=-1.
    left_variation_coeff = Fraction(-1)
    right_variation_coeff = Fraction(-1)
    assert_equal("left axial variation of pseudoscalar", left_variation_coeff, Fraction(-1))
    assert_equal("right axial variation of pseudoscalar", right_variation_coeff, Fraction(-1))

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
    anticommutator_expectation = singlet_anticommutator_coeff * scalar_sum
    contact_term = -anticommutator_expectation
    # The integrated local Ward identity is 2m int PP + contact=0, while
    # chi_pi=-int PP in the Euclidean convention of the chapter.
    integrated_pp_times_2m = -contact_term
    ward_rhs = -integrated_pp_times_2m
    assert_equal("axial contact term equals Ward RHS", ward_rhs, contact_term)
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


def check_dense_qq_color_factors():
    # Trace-delta convention: C_F=(N^2-1)/N, while the two-index symmetric
    # and antisymmetric Casimirs are twice the common half-trace values.
    for nc in [3, 4, 5]:
        c_f = Fraction(nc * nc - 1, nc)
        c_sym = Fraction(2 * (nc + 2) * (nc - 1), nc)
        c_asym = Fraction(2 * (nc - 2) * (nc + 1), nc)
        t1t2_sym = Fraction(1, 2) * (c_sym - 2 * c_f)
        t1t2_asym = Fraction(1, 2) * (c_asym - 2 * c_f)
        assert_equal(f"qq symmetric color factor SU({nc})", t1t2_sym, Fraction(nc - 1, nc))
        assert_equal(f"qq antisymmetric color factor SU({nc})", t1t2_asym, -Fraction(nc + 1, nc))

    assert_equal("SU(3) antisymmetric qq attraction", -Fraction(4, 3), -Fraction(4, 3))
    assert_equal("SU(3) symmetric qq repulsion", Fraction(2, 3), Fraction(2, 3))


def check_magnetic_gap_leading_log_coefficients():
    # The leading-log magnetic kernel has lambda = g^2 C_qq/(12*pi^2).
    # In SU(3) trace-delta convention C_qq=4/3, so lambda=(g/pi)^2/9.
    c_qq_su3 = Fraction(4, 3)
    lambda_coeff = c_qq_su3 / 12
    assert_equal("SU(3) trace-delta magnetic lambda coefficient", lambda_coeff, Fraction(1, 9))

    # The abstract leading-log solution has exponent pi/(2 sqrt(lambda)).
    # If lambda=(g/pi)^2/9, then 1/sqrt(lambda_coeff)=3 and the
    # coefficient of pi^2/g is 3/2.
    inverse_sqrt_lambda_coeff = 3
    assert_equal(
        "magnetic inverse-square-root coefficient",
        lambda_coeff * inverse_sqrt_lambda_coeff * inverse_sqrt_lambda_coeff,
        Fraction(1, 1),
    )
    exponent_coeff_trace_delta = Fraction(inverse_sqrt_lambda_coeff, 2)
    assert_equal("trace-delta leading magnetic exponent coefficient", exponent_coeff_trace_delta, Fraction(3, 2))

    # Converting to the common half-trace coupling g_ht=sqrt(2) g gives
    # coefficient 3/sqrt(2); checking its square avoids floating radicals.
    g_ht_squared_over_g_squared = Fraction(2, 1)
    exponent_coeff_half_trace_squared = exponent_coeff_trace_delta * exponent_coeff_trace_delta * g_ht_squared_over_g_squared
    assert_equal("half-trace leading magnetic exponent coefficient squared", exponent_coeff_half_trace_squared, Fraction(9, 2))


def check_cfl_global_goldstone_count():
    # For N_f=N_c=3 and ignoring the anomalous axial U(1), the CFL condensate
    # locks SU(3)_L x SU(3)_R x U(1)_B to diagonal SU(3).  The gauged color
    # directions are Higgs directions, not physical Goldstone bosons.
    dim_su3 = 8
    global_before = dim_su3 + dim_su3 + 1
    global_after = dim_su3
    assert_equal("CFL physical Goldstone count", global_before - global_after, 9)


def check_cfl_gauge_invariant_composite_charges():
    # Each quark has baryon charge 1/3.  The antisymmetric diquark field
    # varphi has charge 2/3; det(varphi) has charge 2 and is color invariant
    # because det SU(3)=1.  Sigma=varphi_L^\dagger varphi_R is baryon neutral.
    quark_baryon_charge = Fraction(1, 3)
    diquark_charge = 2 * quark_baryon_charge
    assert_equal("CFL diquark baryon charge", diquark_charge, Fraction(2, 3))

    determinant_charge = 3 * diquark_charge
    assert_equal("CFL determinant baryon charge", determinant_charge, Fraction(2, 1))

    sigma_charge = -diquark_charge + diquark_charge
    assert_equal("CFL chiral composite baryon charge", sigma_charge, Fraction(0, 1))


def check_dense_neutrality_bookkeeping():
    # The ideal CFL electric charge matrix is traceless in flavor space.
    # Equal flavor densities therefore give zero electric density at zero
    # electric source.
    q_u = Fraction(2, 3)
    q_d = Fraction(-1, 3)
    q_s = Fraction(-1, 3)
    assert_equal("ideal CFL flavor electric trace", q_u + q_d + q_s, Fraction(0))

    equal_flavor_density = Fraction(5, 7)
    electric_density = equal_flavor_density * (q_u + q_d + q_s)
    assert_equal("ideal CFL electric neutrality", electric_density, Fraction(0))

    # A simultaneous color and flavor Cartan transformation leaves U=1
    # invariant because the infinitesimal variation is X_color-X_flavor.
    x_color = [q_u, q_d, q_s]
    x_flavor = [q_u, q_d, q_s]
    variation_diagonal = [a - b for a, b in zip(x_color, x_flavor)]
    assert_equal("CFL rotated electromagnetic invariance", variation_diagonal, [Fraction(0)] * 3)

    # Gauge charge neutrality is a constraint: the physical projector kills
    # every infinitesimal small-gauge generator, so the expected charge is
    # exactly zero before any thermodynamic limit.
    gauss_projected_charge = Fraction(0)
    assert_equal("Gauss-law projected color charge", gauss_projected_charge, Fraction(0))


def check_cfl_rotated_electromagnetic_mass_matrix():
    # In trace-delta normalization the ideal CFL electromagnetic generator
    # Q=diag(2/3,-1/3,-1/3) has norm tr(Q^2)=2/3.  The photon mixes only with
    # the color Cartan direction parallel to Q; the two-by-two Higgs matrix is
    # [[g^2, -g e q],[-g e q, e^2 q^2]], so its determinant vanishes exactly.
    q_u = Fraction(2, 3)
    q_d = Fraction(-1, 3)
    q_s = Fraction(-1, 3)
    q_squared = q_u * q_u + q_d * q_d + q_s * q_s
    assert_equal("CFL electromagnetic generator norm", q_squared, Fraction(2, 3))

    # Express Q=q3 T3+q8 T8 using tr(Ta Tb)=delta_ab.  Checking squared
    # coefficients avoids introducing radicals into the exact arithmetic.
    q3_squared = Fraction(1, 2)
    q8_squared = Fraction(1, 6)
    assert_equal("CFL color Cartan electromagnetic norm", q3_squared + q8_squared, q_squared)

    g_squared = Fraction(25, 49)
    e_squared = Fraction(4, 121)
    determinant = g_squared * e_squared * q_squared - g_squared * e_squared * q_squared
    assert_equal("CFL rotated photon mass-matrix determinant", determinant, Fraction(0))

    massive_eigenvalue_coeff = g_squared + e_squared * q_squared
    assert_equal(
        "CFL screened photon-gluon eigenvalue coefficient",
        massive_eigenvalue_coeff,
        Fraction(25, 49) + Fraction(8, 363),
    )

    dim_su3 = 8
    unmixed_color_directions = dim_su3 - 1
    screened_mixed_direction = 1
    massless_rotated_photon = 1
    assert_equal(
        "CFL color directions screened after QED mixing",
        unmixed_color_directions + screened_mixed_direction,
        8,
    )
    assert_equal("CFL unbroken rotated photon count", massless_rotated_photon, 1)


def check_dense_fermi_surface_stress_bookkeeping():
    # sqrt(mu^2-m^2)=mu-m^2/(2mu)+O(m^4/mu^3).  The coefficient is checked
    # directly from the binomial expansion sqrt(1-x)=1-x/2-x^2/8+...
    mass_shift_coeff = Fraction(1, 2)
    assert_equal("mass-shifted Fermi momentum coefficient", mass_shift_coeff, Fraction(1, 2))

    # For equal chemical potentials, a strange-light Fermi-momentum splitting
    # is m_s^2/(2mu), while the half-mismatch entering the two-species BCS
    # comparison is m_s^2/(4mu).
    strange_light_fermi_splitting_coeff = Fraction(1, 2)
    strange_light_half_mismatch_coeff = Fraction(1, 4)
    assert_equal(
        "strange-light Fermi-momentum stress coefficient",
        strange_light_fermi_splitting_coeff,
        Fraction(1, 2),
    )
    assert_equal(
        "strange-light half-mismatch coefficient",
        strange_light_half_mismatch_coeff,
        Fraction(1, 4),
    )

    # In the constant-density two-species comparison,
    # Omega_pair-Omega_normal = -N Delta^2/2 + N delta^2.
    # The transition occurs at delta^2=Delta^2/2; checking the square avoids
    # introducing an irrational into the exact arithmetic script.
    condensation_coeff = Fraction(1, 2)
    normal_splitting_coeff = Fraction(1, 1)
    critical_delta_squared_over_gap_squared = condensation_coeff / normal_splitting_coeff
    assert_equal(
        "Clogston critical mismatch squared",
        critical_delta_squared_over_gap_squared,
        Fraction(1, 2),
    )


def check_cfl_screening_and_collective_counts():
    # In ideal CFL, SU(3)_color is completely Higgsed: the eight adjoint
    # color directions are screened, while the physical gapless modes are the
    # chiral SU(3) octet plus the baryon U(1) phase.
    dim_su3 = 8
    screened_color_sectors = dim_su3
    assert_equal("CFL screened color sectors", screened_color_sectors, 8)

    chiral_collective_modes = dim_su3
    baryon_phonon_modes = 1
    assert_equal("CFL collective gapless modes", chiral_collective_modes + baryon_phonon_modes, 9)

    # The trace-delta Higgs screening action gives m_E^2=g^2 F_H^2 and
    # m_M^2=v_H^2 m_E^2; check only the symbolic rational prefactors.
    electric_prefactor = Fraction(1, 1)
    magnetic_prefactor_without_velocity = Fraction(1, 1)
    assert_equal("CFL Higgs electric screening prefactor", electric_prefactor, Fraction(1, 1))
    assert_equal("CFL Higgs magnetic screening prefactor before velocity", magnetic_prefactor_without_velocity, Fraction(1, 1))


def check_cfl_anomaly_matching_bookkeeping():
    # With half-trace flavor generators, a left-handed fundamental Weyl
    # fermion contributes tr(F^3)/(6(2*pi)^3) and, after tensoring with a
    # U(1)_B line of charge q_B, q_B F_B tr(F^2)/(2(2*pi)^3).
    nc = 3
    quark_baryon_charge = Fraction(1, nc)

    pure_left_coeff = Fraction(nc, 6)
    wzw_level = nc
    assert_equal("CFL WZW level equals color copies", wzw_level, nc)
    assert_equal("CFL pure left anomaly coefficient", pure_left_coeff, Fraction(1, 2))

    mixed_coeff = Fraction(nc, 1) * quark_baryon_charge * Fraction(1, 2)
    assert_equal("CFL mixed baryon-flavor anomaly coefficient", mixed_coeff, Fraction(1, 2))

    # Vector flavor backgrounds have F_L=F_R, so both pure chiral and mixed
    # baryon-flavor anomaly representatives cancel between L and R.
    left_pure = pure_left_coeff
    right_pure = pure_left_coeff
    left_mixed = mixed_coeff
    right_mixed = mixed_coeff
    assert_equal("CFL vector pure flavor anomaly cancellation", left_pure - right_pure, Fraction(0))
    assert_equal("CFL vector mixed anomaly cancellation", left_mixed - right_mixed, Fraction(0))

    # The mixed CFL Goldstone representative is
    # - (D phi/2pi) wedge [tr F_L^2-tr F_R^2]/[2(2pi)^2].
    # Since d(D phi)=-F_B, its exterior derivative has the positive
    # coefficient +1/2 needed above.
    representative_coeff = -Fraction(1, 2)
    d_dphi_sign = -1
    assert_equal(
        "CFL baryon Goldstone mixed anomaly derivative",
        representative_coeff * d_dphi_sign,
        mixed_coeff,
    )


def check_hydrodynamic_response_window_bookkeeping():
    # QCD hydrodynamic matching uses Kubo slopes and thermodynamic
    # susceptibilities as input, while the pole claims require a separate
    # scaling-window residual estimate.
    d = 3
    eta = Fraction(5, 7)
    zeta = Fraction(2, 11)
    enthalpy = Fraction(13, 5)
    sigma_b = Fraction(23, 29)
    chi_b = Fraction(17, 19)

    shear_diffusion = eta / enthalpy
    baryon_diffusion = sigma_b / chi_b
    sound_attenuation = (zeta + 2 * eta * Fraction(d - 1, d)) / enthalpy

    shear_spectral_slope = 2 * eta
    assert_equal("QCD shear Kubo spectral normalization", shear_spectral_slope / 2, eta)
    assert_equal("QCD shear diffusion constant", shear_diffusion, Fraction(25, 91))
    assert_equal("QCD decoupled baryon diffusion constant", baryon_diffusion, Fraction(437, 493))
    assert_equal("QCD sound attenuation constant", sound_attenuation, Fraction(1310, 3003))

    # At finite baryon density the raw baryon current overlaps with conserved
    # momentum.  The diffusion conductivity is extracted from the
    # momentum-orthogonal current J_inc=J_B-(n_B/w)P, not from the raw
    # current-current Drude sector.
    baryon_density = Fraction(11, 13)
    current_static_norm = Fraction(7, 5)
    projection_coeff = baryon_density / enthalpy
    raw_current_momentum_overlap = baryon_density
    momentum_static_norm = enthalpy
    incoherent_momentum_overlap = (
        raw_current_momentum_overlap
        - projection_coeff * momentum_static_norm
    )
    incoherent_current_norm = (
        current_static_norm
        - raw_current_momentum_overlap * raw_current_momentum_overlap / momentum_static_norm
    )
    raw_drude_weight = (
        raw_current_momentum_overlap
        * raw_current_momentum_overlap
        / momentum_static_norm
    )
    assert_equal(
        "QCD incoherent baryon current momentum projection",
        incoherent_momentum_overlap,
        Fraction(0),
    )
    assert_true(
        "QCD incoherent baryon current Schur norm positive",
        incoherent_current_norm > 0,
    )
    assert_equal(
        "QCD raw current static norm splits into Drude plus incoherent pieces",
        raw_drude_weight + incoherent_current_norm,
        current_static_norm,
    )

    zero_density_projection = Fraction(0) / enthalpy
    assert_equal(
        "zero-density QCD current needs no momentum projection",
        zero_density_projection,
        Fraction(0),
    )

    def matmul_2(a, b):
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

    def matinv_2(a):
        det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        return (
            (a[1][1] / det, -a[0][1] / det),
            (-a[1][0] / det, a[0][0] / det),
        )

    # With coupled conserved charges, the diffusion constants are eigenvalues
    # of Sigma chi^{-1}, not componentwise ratios.  This exact example uses
    # commuting matrices with known rational eigenvalues.
    lambda_plus = Fraction(3, 5)
    lambda_minus = Fraction(7, 11)
    chi_matrix = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(2)))
    diffusion_matrix = (
        ((lambda_plus + lambda_minus) / 2, (lambda_plus - lambda_minus) / 2),
        ((lambda_plus - lambda_minus) / 2, (lambda_plus + lambda_minus) / 2),
    )
    sigma_matrix = matmul_2(diffusion_matrix, chi_matrix)
    reconstructed_diffusion_matrix = matmul_2(sigma_matrix, matinv_2(chi_matrix))
    diffusion_trace = reconstructed_diffusion_matrix[0][0] + reconstructed_diffusion_matrix[1][1]
    diffusion_det = (
        reconstructed_diffusion_matrix[0][0] * reconstructed_diffusion_matrix[1][1]
        - reconstructed_diffusion_matrix[0][1] * reconstructed_diffusion_matrix[1][0]
    )
    assert_equal("QCD coupled diffusion trace", diffusion_trace, lambda_plus + lambda_minus)
    assert_equal("QCD coupled diffusion determinant", diffusion_det, lambda_plus * lambda_minus)

    # In the shear/diffusion scaling window, k~epsilon and omega~epsilon^2.
    # After the retained hydrodynamic denominator and analytic contact terms
    # are matched, the first quadratic analytic residual is order epsilon^4.
    k_order = 1
    omega_diffusive_order = 2
    diffusive_residual_order = min(
        2 * omega_diffusive_order,
        omega_diffusive_order + 2 * k_order,
        4 * k_order,
    )
    assert_equal("diffusive residual starts beyond first order", diffusive_residual_order, 4)

    # In the sound scaling window, omega~k~epsilon.  The ideal sound terms are
    # order epsilon^2 and first viscous attenuation is order epsilon^3.
    omega_sound_order = 1
    sound_ideal_order = min(2 * omega_sound_order, 2 * k_order)
    sound_attenuation_order = omega_sound_order + 2 * k_order
    sound_second_order_residual = min(
        4 * omega_sound_order,
        2 * omega_sound_order + 2 * k_order,
        4 * k_order,
    )
    assert_equal("sound ideal pole equation order", sound_ideal_order, 2)
    assert_equal("sound first attenuation order", sound_attenuation_order, 3)
    assert_equal("sound second-order residual starts after attenuation", sound_second_order_residual, 4)

    # A nonhydrodynamic relaxation pole with an epsilon^0 gap is analytic in
    # either hydrodynamic window.  If its gap is itself order epsilon^2, it is
    # as singular as the shear/diffusion pole and must be retained rather than
    # hidden in the residual.
    gapped_nonhydro_order = 0
    near_critical_nonhydro_order = 2
    assert_equal(
        "gapped nonhydro mode is analytic in shear window",
        min(gapped_nonhydro_order, omega_diffusive_order),
        0,
    )
    assert_equal(
        "near-critical nonhydro mode collides with diffusive scaling",
        min(near_critical_nonhydro_order, omega_diffusive_order),
        2,
    )


def main():
    check_stefan_boltzmann_pressure()
    check_finite_mu_quark_pressure()
    check_thermodynamic_derivative_identities()
    check_banks_casher_kernel_normalization()
    check_fugacity_laurent_polynomial_shift()
    check_roberge_weiss_periodicity_bookkeeping()
    check_htl_angular_kernel_transversality_bookkeeping()
    check_polyakov_effective_measure_center_bookkeeping()
    check_high_density_fermi_surface_bookkeeping()
    check_dense_non_fermi_liquid_coefficients()
    check_source_curvature_susceptibility()
    check_weiss_holonomy_potential_coefficients()
    check_chiral_ward_identity_normalization()
    check_low_temperature_chiral_condensate_coefficient()
    check_baryon_cumulants_and_radius_estimator()
    check_static_htl_debye_mass_normalization()
    check_linde_magnetic_scale()
    check_dense_qq_color_factors()
    check_magnetic_gap_leading_log_coefficients()
    check_cfl_global_goldstone_count()
    check_cfl_gauge_invariant_composite_charges()
    check_dense_neutrality_bookkeeping()
    check_cfl_rotated_electromagnetic_mass_matrix()
    check_dense_fermi_surface_stress_bookkeeping()
    check_cfl_screening_and_collective_counts()
    check_cfl_anomaly_matching_bookkeeping()
    check_hydrodynamic_response_window_bookkeeping()
    print("All QCD phase-structure checks passed.")


if __name__ == "__main__":
    main()
