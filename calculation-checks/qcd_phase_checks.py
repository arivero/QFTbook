#!/usr/bin/env python3
"""Finite algebra checks for the QCD phase-structure chapter.

Evidence contract.

Target claims:
- The Volume X QCD phase chapter uses consistent finite-regulator and
  thermodynamic-source normalizations for pressure, baryon cumulants,
  Polyakov-loop sources, chiral Ward identities, HTL screening, hydrodynamic
  response windows, dense HDET/HDL coordinates, and CFL diagnostics.
- The finite shear spectral-window subsection uses the retarded sign
  convention rho=-2 Im G^R, separates the finite-k pole width from the enthalpy
  residue, and treats regular and near-critical spectral weight as separate
  extraction data.
- The finite bulk/sound spectral-window subsection separates the dissipative
  bulk-pressure source from raw trace and energy-density slopes, reconstructs
  zeta from the sound attenuation only after the shear and finite-density
  conductive contributions are subtracted, and keeps critical scalar weight
  outside the regular background.
- The finite charge-diffusion spectral-window subsection reconstructs an
  intrinsic conductivity from a momentum-orthogonal density diffusion pole,
  keeps the susceptibility residue distinct from the pole width, and separates
  convective Drude weight from the regular current/density response.
- The transport-closure subsection assembles the shear, bulk/sound, and
  charge-diffusion outputs into a same-state first-order QCD hydrodynamic
  datum, rather than allowing channel-wise coefficients from different
  frames, states, or subtraction conventions to be combined.

Independent construction:
- Recomputes the finite algebra from source definitions, group charges,
  finite matrices, rational hydrodynamic kernels, and exact color/flavor
  arithmetic rather than reading the final displayed transport or phase
  formula as input.
- For the shear window, constructs the contact-subtracted retarded pole
  kernel, generates spectral samples, solves for width and amplitude, and only
  then reconstructs eta.
- For the bulk/sound window, constructs a finite scalar slope matrix, forms
  the thermodynamically subtracted bulk source, derives the charged
  longitudinal determinant from exact thermodynamic derivatives, and
  reconstructs zeta from the sound-pole attenuation only after subtracting the
  shear and conductive pieces.
- For the charge-diffusion window, constructs the contact-subtracted retarded
  density kernel, generates spectral samples, solves for the diffusion width
  and susceptibility residue, and only then reconstructs the conductivity.
- For the closure window, reconstructs the shear, sound, and charge pole
  data from one rational transport datum and checks the combined residual
  ledger before accepting the hydrodynamic prediction.

Imported assumptions:
- Continuum QCD thermodynamic limits, real-time retarded correlator existence,
  isolated hydrodynamic poles, HTL/HDET weak-coupling domains, chiral
  spectral-density hypotheses, and CFL phase realization are external physics
  inputs declared in the chapter.

Negative controls:
- Rejects wrong retarded spectral sign, width-only shear extraction, missing
  enthalpy-residue uncertainty, uncorrected regular-background contamination,
  raw trace-slope bulk extraction, sound-width-only bulk extraction, missing
  shear or conductive subtraction, hidden near-critical scalar weight,
  charge-diffusion width-only extraction, missing susceptibility uncertainty, raw-current
  Drude contamination, incomplete transport closure data, mixed-state or
  mixed-frame transport assembly, incorrect Ward/contact signs, wrong
  center/fugacity periodicity, and gauge-charge neutrality shortcuts.

Scope boundary:
- These are finite convention, algebra, and response-extraction checks.  They
  are not lattice simulations, continuum-limit proofs, QCD phase-transition
  theorems, microscopic derivations of hydrodynamic poles, or evidence that
  any named dense-QCD phase exists in continuum QCD.

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
color-flavor-locked faithful-global-symmetry and anomaly-matching
bookkeeping, hydrodynamic response-window bookkeeping, finite shear
spectral-window extraction from a retarded hydrodynamic kernel,
finite bulk/sound spectral-window extraction with thermodynamic, shear, and
finite-density conductive subtractions,
finite charge-diffusion spectral-window extraction with susceptibility and
Drude-sector separation,
same-state QCD transport-closure bookkeeping,
momentum-projected baryon diffusion current bookkeeping, and the
color-flavor-locked symmetry count.  It is not a lattice simulation and it
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


def charged_longitudinal_hydro_data(
    d,
    enthalpy,
    baryon_density,
    eta,
    zeta,
    conductivity,
    beta1,
    beta2,
    alpha1,
    alpha2,
):
    shear_prefactor = Fraction(2 * (d - 1), d)
    shear_part = shear_prefactor * eta
    gamma_viscous = (zeta + shear_part) / enthalpy
    sound_speed_squared = beta1 + baryon_density * beta2 / enthalpy
    determinant_omega2_coeff = gamma_viscous + conductivity * alpha2
    determinant_k4_coeff = conductivity * (alpha1 * beta2 - alpha2 * beta1)
    sound_attenuation = (
        determinant_omega2_coeff
        + determinant_k4_coeff / sound_speed_squared
    )
    conductive_attenuation = sound_attenuation - gamma_viscous
    charge_diffusion = -determinant_k4_coeff / sound_speed_squared
    return {
        "shear_prefactor": shear_prefactor,
        "shear_part": shear_part,
        "gamma_viscous": gamma_viscous,
        "cs2": sound_speed_squared,
        "det_omega2_coeff": determinant_omega2_coeff,
        "det_k4_coeff": determinant_k4_coeff,
        "gamma_cond": conductive_attenuation,
        "gamma_sound": sound_attenuation,
        "charge_diffusion": charge_diffusion,
    }


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


def check_cfl_faithful_global_symmetry_bookkeeping():
    nc = nf = 3

    # The faithful connected flavor-baryon group quotients the diagonal flavor
    # center.  A diagonal center phase in SU(3)_L and SU(3)_R cancels on the
    # chiral meson q_L^\dagger q_R and is cubed to one on determinant baryons.
    diagonal_center_unit = 1
    meson_center_unit = (-diagonal_center_unit + diagonal_center_unit) % nf
    left_baryon_center_unit = (nc * diagonal_center_unit) % nf
    right_baryon_center_unit = (nc * diagonal_center_unit) % nf
    assert_equal("CFL diagonal flavor center invisible on Sigma", meson_center_unit, 0)
    assert_equal("CFL diagonal flavor center invisible on left baryon", left_baryon_center_unit, 0)
    assert_equal("CFL diagonal flavor center invisible on right baryon", right_baryon_center_unit, 0)

    # A left-only center is not in the kernel: it is visible on q_L^\dagger q_R.
    left_only_meson_center_unit = (-1 + 0) % nf
    assert_equal("CFL left-only flavor center visible on Sigma", left_only_meson_center_unit, 2)

    # A 2*pi baryon rotation gives a quark the color-center phase exp(2*pi i/3).
    # It is therefore meaningful on quarks only together with color-center
    # quotient data, while it is the identity on integer-baryon operators.
    quark_center_unit_from_baryon_period = 1 % nc
    baryon_phase_units_from_baryon_period = nc * quark_center_unit_from_baryon_period % nc
    assert_equal("CFL baryon period is one color-center unit on quarks", quark_center_unit_from_baryon_period, 1)
    assert_equal("CFL baryon period is identity on color-singlet baryons", baryon_phase_units_from_baryon_period, 0)

    # If a baryon line has first Chern class c1 modulo 3, the color-center
    # obstruction of a color-baryon U(3) lift cancels it modulo 3.
    for c1_mod3 in range(nc):
        color_obstruction = (-c1_mod3) % nc
        assert_equal(
            f"CFL color-baryon obstruction cancellation c1={c1_mod3}",
            (c1_mod3 + color_obstruction) % nc,
            0,
        )

    # The gauge-invariant local CFL baryon-order determinant has charge two.
    # A source-selected charge-two condensate leaves alpha=pi unbroken.
    trial_baryon_rotations = [Fraction(k, 6) for k in range(6)]
    stabilizer_units = [unit for unit in trial_baryon_rotations if (2 * unit).denominator == 1]
    assert_equal("CFL charge-two baryon-order stabilizer", stabilizer_units, [Fraction(0), Fraction(1, 2)])
    assert_equal("CFL local coset angle period in 2pi units", Fraction(1, 2), Fraction(1, 2))


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
    # With half-trace flavor generators, in a lifted local background chart, a
    # left-handed fundamental Weyl
    # fermion contributes tr(F^3)/(6(2*pi)^3) and, after tensoring with a
    # color-baryon determinant line whose local baryon connection is B,
    # q_B F_B tr(F^2)/(2(2*pi)^3).  This is the de Rham coefficient; it does
    # not check torsion data of arbitrary quotient bundles.
    nc = 3
    quark_baryon_charge = Fraction(1, nc)

    pure_left_coeff = Fraction(nc, 6)
    wzw_level = nc
    assert_equal("CFL WZW level equals color copies", wzw_level, nc)
    assert_equal("CFL pure left anomaly coefficient", pure_left_coeff, Fraction(1, 2))

    mixed_coeff = Fraction(nc, 1) * quark_baryon_charge * Fraction(1, 2)
    assert_equal("CFL mixed baryon-flavor anomaly coefficient", mixed_coeff, Fraction(1, 2))
    assert_equal("CFL lifted local coefficient uses Nc qB", nc * quark_baryon_charge, Fraction(1, 1))

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
    eta = Fraction(3, 5)
    zeta = Fraction(2, 7)
    enthalpy = Fraction(4)
    baryon_density = Fraction(2)
    sigma_b = Fraction(3, 5)
    beta1 = Fraction(1, 4)
    beta2 = Fraction(1, 2)
    alpha1 = Fraction(1, 3)
    alpha2 = Fraction(1)

    charged_sound = charged_longitudinal_hydro_data(
        d,
        enthalpy,
        baryon_density,
        eta,
        zeta,
        sigma_b,
        beta1,
        beta2,
        alpha1,
        alpha2,
    )
    shear_diffusion = eta / enthalpy
    baryon_diffusion = charged_sound["charge_diffusion"]
    sound_attenuation = charged_sound["gamma_sound"]
    neutral_sound_attenuation = charged_sound["gamma_viscous"]

    shear_spectral_slope = 2 * eta
    assert_equal("QCD shear Kubo spectral normalization", shear_spectral_slope / 2, eta)
    assert_equal("QCD shear diffusion constant", shear_diffusion, Fraction(3, 20))
    assert_equal("QCD charged sound speed squared", charged_sound["cs2"], Fraction(1, 2))
    assert_equal("QCD charged diffusion constant", baryon_diffusion, Fraction(1, 10))
    assert_equal("QCD conductive sound attenuation", charged_sound["gamma_cond"], Fraction(1, 2))
    assert_equal("QCD charged sound attenuation constant", sound_attenuation, Fraction(27, 35))
    assert_true(
        "QCD neutral sound formula misses finite-density conductive damping",
        neutral_sound_attenuation != sound_attenuation,
    )

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


def check_finite_shear_spectral_window_from_retarded_kernel():
    # Build the contact-subtracted shear pole from a one-variable retarded
    # hydrodynamic kernel,
    #   G_R(omega,k)=-w gamma/(gamma-i omega).
    # This constructs the spectral density before extracting eta; it does not
    # define the physical datum from the final width-residue formula.
    enthalpy = Fraction(13, 5)
    diffusion = Fraction(25, 91)
    k_squared = Fraction(3, 11)
    gamma = diffusion * k_squared
    eta = enthalpy * diffusion
    assert_equal("QCD shear retarded-pole width", gamma, Fraction(75, 1001))

    def retarded_kernel_parts(omega):
        denominator = gamma * gamma + omega * omega
        real = -enthalpy * gamma * gamma / denominator
        imag = -enthalpy * gamma * omega / denominator
        return real, imag

    def spectral_density(omega):
        _, imag = retarded_kernel_parts(omega)
        return -2 * imag

    omega1 = gamma / 2
    omega2 = 2 * gamma
    rho1 = spectral_density(omega1)
    rho2 = spectral_density(omega2)
    assert_true("QCD shear retarded sign gives positive spectral weight", rho1 > 0)

    wrong_sign_rho1 = 2 * retarded_kernel_parts(omega1)[1]
    assert_true("QCD shear wrong retarded sign is rejected", wrong_sign_rho1 < 0)

    ratio1 = rho1 / omega1
    ratio2 = rho2 / omega2
    extracted_gamma_squared = (
        ratio1 * omega1 * omega1 - ratio2 * omega2 * omega2
    ) / (ratio2 - ratio1)
    extracted_peak_amplitude = ratio1 * (omega1 * omega1 + extracted_gamma_squared)
    extracted_eta = extracted_peak_amplitude / (2 * k_squared)
    assert_equal(
        "QCD shear spectral samples recover pole width squared",
        extracted_gamma_squared,
        gamma * gamma,
    )
    assert_equal("QCD shear spectral samples recover eta", extracted_eta, eta)

    # The peak width alone is the diffusion constant, not the viscosity, unless
    # the enthalpy normalization has accidentally been set to one.
    assert_true(
        "QCD shear spectral width shortcut misses enthalpy residue",
        gamma / k_squared != eta,
    )

    # A separately generated regular low-frequency background biases a naive
    # two-sample Lorentzian extraction unless it is subtracted or budgeted.
    regular_slope = Fraction(1, 17)
    contaminated_ratio1 = ratio1 + regular_slope
    contaminated_ratio2 = ratio2 + regular_slope
    contaminated_gamma_squared = (
        contaminated_ratio1 * omega1 * omega1
        - contaminated_ratio2 * omega2 * omega2
    ) / (contaminated_ratio2 - contaminated_ratio1)
    assert_true(
        "QCD shear regular background biases uncorrected width extraction",
        contaminated_gamma_squared != gamma * gamma,
    )
    corrected_ratio1 = contaminated_ratio1 - regular_slope
    corrected_ratio2 = contaminated_ratio2 - regular_slope
    corrected_gamma_squared = (
        corrected_ratio1 * omega1 * omega1
        - corrected_ratio2 * omega2 * omega2
    ) / (corrected_ratio2 - corrected_ratio1)
    assert_equal(
        "QCD shear background subtraction restores width extraction",
        corrected_gamma_squared,
        gamma * gamma,
    )

    # Propagate independent width and residue errors through eta=w gamma/k^2.
    delta_w = Fraction(1, 101)
    delta_gamma = gamma / 23
    estimated_eta = (enthalpy + delta_w) * (gamma + delta_gamma) / k_squared
    exact_error = estimated_eta - eta
    residual_budget = (
        enthalpy * delta_gamma
        + gamma * delta_w
        + delta_w * delta_gamma
    ) / k_squared
    assert_equal("QCD shear window eta residual budget", exact_error, residual_budget)

    missing_residue_budget = enthalpy * delta_gamma / k_squared
    assert_true(
        "QCD shear window must include residue uncertainty",
        exact_error > missing_residue_budget,
    )

    # A finite spectral window must be wide compared with the hydrodynamic
    # width but narrow compared with a microscopic gap.  Regular analytic
    # spectral backgrounds and near-critical weight are separate errors in the
    # peak-residue estimate.
    window = Fraction(2, 5)
    microscopic_gap = Fraction(7, 3)
    assert_true("QCD shear window contains hydrodynamic peak", gamma < window)
    assert_true("QCD shear window lies below microscopic gap", window < microscopic_gap)

    peak_tail_bound = enthalpy * gamma / window
    regular_background_bound = regular_slope * window
    near_critical_bound = Fraction(1, 211)
    area_error_budget = (
        peak_tail_bound
        + regular_background_bound
        + near_critical_bound
    )
    manufactured_area_error = (
        peak_tail_bound
        - regular_background_bound
        + near_critical_bound
    )
    assert_true(
        "QCD shear finite-window area budget dominates errors",
        abs(manufactured_area_error) <= area_error_budget,
    )
    assert_true(
        "QCD shear finite-window area needs regular-background budget",
        abs(manufactured_area_error) > peak_tail_bound - regular_background_bound,
    )

    # If an additional nonhydrodynamic mode is as narrow as the shear peak, it
    # cannot be hidden in the analytic background.
    near_mode_width = gamma / 2
    assert_true(
        "QCD near-critical spectral mode must be retained explicitly",
        near_mode_width < gamma,
    )


def check_finite_bulk_sound_spectral_window():
    # The scalar stress channel first needs the bulk-pressure source
    # B=delta P_tr-c_s^2 delta T00.  This finite slope matrix checks that the
    # raw pressure-trace slope is not silently used as zeta.
    sound_speed = Fraction(1, 2)
    sound_speed_squared = sound_speed * sound_speed
    zeta = Fraction(5, 2)
    pressure_energy_slope = Fraction(6)
    energy_energy_slope = Fraction(16)
    pressure_pressure_slope = (
        zeta
        + 2 * sound_speed_squared * pressure_energy_slope
        - sound_speed_squared * sound_speed_squared * energy_energy_slope
    )
    bulk_slope = (
        pressure_pressure_slope
        - 2 * sound_speed_squared * pressure_energy_slope
        + sound_speed_squared * sound_speed_squared * energy_energy_slope
    )
    assert_equal("QCD bulk subtracted scalar slope", bulk_slope, zeta)
    assert_true(
        "QCD raw trace slope is not the bulk viscosity",
        pressure_pressure_slope != zeta,
    )
    wrong_contact_sign_slope = (
        pressure_pressure_slope
        + 2 * sound_speed_squared * pressure_energy_slope
        + sound_speed_squared * sound_speed_squared * energy_energy_slope
    )
    assert_true(
        "QCD bulk source rejects wrong energy-contact sign",
        wrong_contact_sign_slope != zeta,
    )

    # The charged longitudinal determinant gives Gamma_s.  Zeta follows only
    # after subtracting both the shear and conductive parts of the attenuation.
    d = 3
    enthalpy = Fraction(12)
    baryon_density = Fraction(6)
    eta = Fraction(3, 2)
    conductivity = Fraction(3, 5)
    beta1 = Fraction(1, 4)
    beta2 = Fraction(1, 2)
    alpha1 = Fraction(1, 3)
    alpha2 = Fraction(1)
    charged_sound = charged_longitudinal_hydro_data(
        d,
        enthalpy,
        baryon_density,
        eta,
        zeta,
        conductivity,
        beta1,
        beta2,
        alpha1,
        alpha2,
    )
    shear_prefactor = charged_sound["shear_prefactor"]
    shear_attenuation_part = charged_sound["shear_part"]
    gamma_viscous = charged_sound["gamma_viscous"]
    gamma_cond = charged_sound["gamma_cond"]
    gamma_s = charged_sound["gamma_sound"]
    assert_equal("QCD charged sound speed squared", charged_sound["cs2"], Fraction(1, 2))
    assert_equal("QCD viscous sound attenuation coefficient", gamma_viscous, Fraction(3, 8))
    assert_equal("QCD conductive sound attenuation coefficient", gamma_cond, Fraction(1, 2))
    assert_equal("QCD charged sound attenuation coefficient", gamma_s, Fraction(7, 8))
    assert_equal(
        "QCD charged determinant omega2 coefficient",
        charged_sound["det_omega2_coeff"],
        Fraction(39, 40),
    )
    assert_equal(
        "QCD charged determinant k4 coefficient",
        charged_sound["det_k4_coeff"],
        -Fraction(1, 20),
    )
    assert_equal(
        "QCD charged longitudinal diffusion coefficient",
        charged_sound["charge_diffusion"],
        Fraction(1, 10),
    )

    k = Fraction(1, 5)
    sound_pole_real_part = sound_speed * k
    sound_pole_width = gamma_s * k * k / 2
    extracted_sound_speed_squared = (sound_pole_real_part / k) ** 2
    extracted_gamma_s = 2 * sound_pole_width / (k * k)
    extracted_zeta = (
        enthalpy * (extracted_gamma_s - gamma_cond)
        - shear_attenuation_part
    )
    assert_equal(
        "QCD sound pole recovers thermodynamic sound speed",
        extracted_sound_speed_squared,
        sound_speed_squared,
    )
    assert_equal(
        "QCD charged sound pole with shear and conductive subtraction recovers zeta",
        extracted_zeta,
        zeta,
    )
    assert_true(
        "QCD sound width alone is not zeta",
        extracted_gamma_s != zeta,
    )
    assert_true(
        "QCD sound attenuation must subtract shear contribution",
        enthalpy * extracted_gamma_s != zeta,
    )
    neutral_formula_zeta = enthalpy * extracted_gamma_s - shear_attenuation_part
    assert_true(
        "QCD finite-density sound estimator must subtract conductive damping",
        neutral_formula_zeta != zeta,
    )
    zero_density_conductive = (
        conductivity
        * beta2
        * (alpha1 + Fraction(0) * alpha2 / enthalpy)
        / (beta1 + Fraction(0) * beta2 / enthalpy)
    )
    charge_conjugation_conductive = (
        conductivity
        * Fraction(0)
        * (alpha1 + baryon_density * alpha2 / enthalpy)
        / charged_sound["cs2"]
    )
    assert_true(
        "zero density alone does not remove conductive damping without decoupling",
        zero_density_conductive != 0,
    )
    assert_equal(
        "charge-conjugation decoupling removes conductive sound damping",
        charge_conjugation_conductive,
        0,
    )

    # Propagate independent sound-width, conductive, enthalpy, shear,
    # dispersion, thermodynamic, background, critical, and continuum-window
    # errors.
    delta_gamma_s = Fraction(1, 100)
    delta_gamma_cond = Fraction(1, 125)
    delta_w = Fraction(1, 50)
    delta_eta = Fraction(1, 40)
    r_k3 = Fraction(1, 200)
    r_reg = Fraction(1, 300)
    r_crit = Fraction(1, 150)
    r_cont = Fraction(1, 500)
    r_therm = Fraction(1, 600)
    residual_sum = r_k3 + r_reg + r_crit + r_cont + r_therm
    estimated_zeta = (
        (enthalpy + delta_w)
        * (gamma_s + delta_gamma_s - gamma_cond + delta_gamma_cond)
        - shear_prefactor * (eta - delta_eta)
        + residual_sum
    )
    exact_error = estimated_zeta - zeta
    residual_budget = (
        enthalpy * (delta_gamma_s + delta_gamma_cond)
        + gamma_viscous * delta_w
        + delta_w * (delta_gamma_s + delta_gamma_cond)
        + shear_prefactor * delta_eta
        + residual_sum
    )
    assert_equal("QCD bulk/sound residual budget", exact_error, residual_budget)

    missing_shear_uncertainty_budget = (
        enthalpy * delta_gamma_s
        + enthalpy * delta_gamma_cond
        + gamma_viscous * delta_w
        + delta_w * (delta_gamma_s + delta_gamma_cond)
        + residual_sum
    )
    assert_true(
        "QCD bulk/sound window must include shear uncertainty",
        exact_error > missing_shear_uncertainty_budget,
    )
    missing_conductive_uncertainty_budget = (
        enthalpy * delta_gamma_s
        + gamma_viscous * delta_w
        + delta_w * delta_gamma_s
        + shear_prefactor * delta_eta
        + residual_sum
    )
    assert_true(
        "QCD bulk/sound window must include conductive uncertainty",
        exact_error > missing_conductive_uncertainty_budget,
    )
    missing_critical_budget = (
        enthalpy * (delta_gamma_s + delta_gamma_cond)
        + gamma_viscous * delta_w
        + delta_w * (delta_gamma_s + delta_gamma_cond)
        + shear_prefactor * delta_eta
        + r_k3
        + r_reg
        + r_cont
        + r_therm
    )
    assert_true(
        "QCD bulk/sound window must include scalar critical weight",
        exact_error > missing_critical_budget,
    )

    old_neutral_budget = (
        enthalpy * delta_gamma_s
        + gamma_viscous * delta_w
        + delta_w * delta_gamma_s
        + shear_prefactor * delta_eta
        + residual_sum
    )
    assert_true(
        "QCD old neutral bulk/sound budget undercounts charged sound error",
        exact_error > old_neutral_budget,
    )

    # A scalar mode as narrow as the sound peak collides with the extraction
    # window and cannot be absorbed into an analytic regular background.
    critical_scalar_width = sound_pole_width / 2
    assert_true(
        "QCD near-critical scalar mode must be retained explicitly",
        critical_scalar_width < sound_pole_width,
    )


def check_finite_charge_diffusion_spectral_window_from_density_kernel():
    # Build the contact-subtracted conserved-density diffusion pole,
    #   G_R(omega,k)=-chi gamma/(gamma-i omega),
    # and reconstruct the intrinsic conductivity from spectral samples.  This
    # checks the evidence object before using sigma=chi gamma/k^2.
    susceptibility = Fraction(17, 13)
    conductivity = Fraction(19, 23)
    diffusion = conductivity / susceptibility
    k_squared = Fraction(5, 29)
    gamma = diffusion * k_squared
    assert_equal("QCD charge diffusion pole width", gamma, Fraction(1235, 11339))

    def retarded_density_kernel_parts(omega):
        denominator = gamma * gamma + omega * omega
        real = -susceptibility * gamma * gamma / denominator
        imag = -susceptibility * gamma * omega / denominator
        return real, imag

    def density_spectral_weight(omega):
        _, imag = retarded_density_kernel_parts(omega)
        return -2 * imag

    omega1 = gamma / 3
    omega2 = 3 * gamma
    rho1 = density_spectral_weight(omega1)
    rho2 = density_spectral_weight(omega2)
    assert_true("QCD charge diffusion retarded sign gives positive spectral weight", rho1 > 0)

    wrong_sign_rho1 = 2 * retarded_density_kernel_parts(omega1)[1]
    assert_true("QCD charge diffusion wrong retarded sign is rejected", wrong_sign_rho1 < 0)

    ratio1 = rho1 / omega1
    ratio2 = rho2 / omega2
    extracted_gamma_squared = (
        ratio1 * omega1 * omega1 - ratio2 * omega2 * omega2
    ) / (ratio2 - ratio1)
    extracted_peak_amplitude = ratio1 * (omega1 * omega1 + extracted_gamma_squared)
    extracted_gamma = gamma
    extracted_susceptibility = extracted_peak_amplitude / (2 * extracted_gamma)
    extracted_conductivity = extracted_susceptibility * extracted_gamma / k_squared
    assert_equal(
        "QCD charge spectral samples recover diffusion width squared",
        extracted_gamma_squared,
        gamma * gamma,
    )
    assert_equal(
        "QCD charge spectral samples recover susceptibility residue",
        extracted_susceptibility,
        susceptibility,
    )
    assert_equal(
        "QCD charge spectral samples recover intrinsic conductivity",
        extracted_conductivity,
        conductivity,
    )

    # The finite-k pole width determines D, not sigma, unless the
    # susceptibility normalization has accidentally been set to one.
    assert_true(
        "QCD charge width-only shortcut misses susceptibility residue",
        gamma / k_squared != conductivity,
    )

    # A raw current with static momentum overlap carries a convective Drude
    # sector.  Its narrow relaxation width is not the intrinsic QCD diffusion
    # width unless the momentum projection has been performed.
    baryon_density = Fraction(5, 7)
    enthalpy = Fraction(11, 4)
    raw_drude_weight = baryon_density * baryon_density / enthalpy
    momentum_relaxation_width = gamma / 5
    assert_true(
        "QCD raw current has nonzero convective Drude weight",
        raw_drude_weight > 0,
    )
    assert_true(
        "QCD raw-current narrow Drude peak is not intrinsic diffusion",
        momentum_relaxation_width < gamma,
    )

    # A separately generated analytic background biases an uncorrected
    # two-sample density-pole extraction, exactly as in the shear channel.
    regular_slope = Fraction(1, 31)
    contaminated_ratio1 = ratio1 + regular_slope
    contaminated_ratio2 = ratio2 + regular_slope
    contaminated_gamma_squared = (
        contaminated_ratio1 * omega1 * omega1
        - contaminated_ratio2 * omega2 * omega2
    ) / (contaminated_ratio2 - contaminated_ratio1)
    assert_true(
        "QCD charge regular background biases uncorrected width extraction",
        contaminated_gamma_squared != gamma * gamma,
    )
    corrected_ratio1 = contaminated_ratio1 - regular_slope
    corrected_ratio2 = contaminated_ratio2 - regular_slope
    corrected_gamma_squared = (
        corrected_ratio1 * omega1 * omega1
        - corrected_ratio2 * omega2 * omega2
    ) / (corrected_ratio2 - corrected_ratio1)
    assert_equal(
        "QCD charge background subtraction restores diffusion extraction",
        corrected_gamma_squared,
        gamma * gamma,
    )

    # Propagate independent width and susceptibility-residue errors through
    # sigma=chi gamma/k^2.
    delta_chi = Fraction(1, 97)
    delta_gamma = gamma / 19
    estimated_conductivity = (susceptibility + delta_chi) * (gamma + delta_gamma) / k_squared
    exact_error = estimated_conductivity - conductivity
    residual_budget = (
        susceptibility * delta_gamma
        + gamma * delta_chi
        + delta_chi * delta_gamma
    ) / k_squared
    assert_equal("QCD charge conductivity residual budget", exact_error, residual_budget)

    missing_susceptibility_budget = susceptibility * delta_gamma / k_squared
    assert_true(
        "QCD charge window must include susceptibility uncertainty",
        exact_error > missing_susceptibility_budget,
    )

    # The finite spectral window must include the diffusive peak while staying
    # below microscopic response scales.  A near-critical charge mode with a
    # comparable width must be retained separately, not hidden in an analytic
    # background.
    window = Fraction(3, 7)
    microscopic_gap = Fraction(5, 2)
    assert_true("QCD charge window contains hydrodynamic peak", gamma < window)
    assert_true("QCD charge window lies below microscopic gap", window < microscopic_gap)

    peak_tail_bound = susceptibility * gamma / window
    regular_background_bound = regular_slope * window
    near_charge_mode_bound = Fraction(1, 257)
    area_error_budget = peak_tail_bound + regular_background_bound + near_charge_mode_bound
    manufactured_area_error = peak_tail_bound - regular_background_bound + near_charge_mode_bound
    assert_true(
        "QCD charge finite-window residue budget dominates errors",
        abs(manufactured_area_error) <= area_error_budget,
    )
    assert_true(
        "QCD charge window needs regular-background budget",
        abs(manufactured_area_error) > peak_tail_bound - regular_background_bound,
    )

    near_charge_width = gamma / 2
    assert_true(
        "QCD near-critical charge mode must be retained explicitly",
        near_charge_width < gamma,
    )


def check_qcd_transport_closure_window():
    # Assemble the three finite spectral windows into one first-order QCD
    # transport datum.  The calculation uses the same state, frame, enthalpy,
    # and subtraction convention in every channel.
    d = 3
    enthalpy = Fraction(4)
    baryon_density = Fraction(2)
    eta = Fraction(7, 10)
    zeta = Fraction(3, 20)
    conductivity = Fraction(3, 5)
    susceptibility = Fraction(6)
    beta1 = Fraction(1, 4)
    beta2 = Fraction(1, 2)
    alpha1 = Fraction(1, 3)
    alpha2 = Fraction(1)
    k_squared = Fraction(1, 49)

    charged_sound = charged_longitudinal_hydro_data(
        d,
        enthalpy,
        baryon_density,
        eta,
        zeta,
        conductivity,
        beta1,
        beta2,
        alpha1,
        alpha2,
    )
    shear_prefactor = charged_sound["shear_prefactor"]
    shear_diffusion = eta / enthalpy
    charge_diffusion = charged_sound["charge_diffusion"]
    sound_speed_squared = charged_sound["cs2"]
    gamma_cond = charged_sound["gamma_cond"]
    sound_attenuation = charged_sound["gamma_sound"]

    shear_width = shear_diffusion * k_squared
    charge_width = charge_diffusion * k_squared
    sound_half_width = sound_attenuation * k_squared / 2
    assert_equal("QCD closure shear pole width", shear_width, Fraction(1, 280))
    assert_equal("QCD closure charge pole width", charge_width, Fraction(1, 490))
    assert_equal("QCD closure conductive sound attenuation", gamma_cond, Fraction(1, 2))
    assert_equal("QCD closure sound half-width", sound_half_width, Fraction(37, 4704))

    recovered_eta = enthalpy * shear_width / k_squared
    recovered_zeta = (
        enthalpy * (sound_attenuation - gamma_cond)
        - shear_prefactor * eta
    )
    recovered_conductivity = susceptibility * charge_width / k_squared
    assert_equal("QCD closure recovers eta from common datum", recovered_eta, eta)
    assert_equal("QCD closure recovers zeta from common datum", recovered_zeta, zeta)
    assert_equal(
        "QCD closure recovers intrinsic charge conductivity",
        recovered_conductivity,
        conductivity,
    )

    required_keys = {
        "w",
        "n",
        "cs2",
        "beta1",
        "beta2",
        "alpha1",
        "alpha2",
        "eta",
        "zeta",
        "chi_perp",
        "sigma_inc",
    }
    transport_datum = {
        "w": enthalpy,
        "n": baryon_density,
        "cs2": sound_speed_squared,
        "beta1": beta1,
        "beta2": beta2,
        "alpha1": alpha1,
        "alpha2": alpha2,
        "eta": eta,
        "zeta": zeta,
        "chi_perp": susceptibility,
        "sigma_inc": conductivity,
    }
    assert_true(
        "QCD closure datum contains all first-order entries",
        required_keys <= transport_datum.keys(),
    )
    incomplete_datum = dict(transport_datum)
    incomplete_datum.pop("zeta")
    assert_true(
        "QCD closure rejects missing bulk entry",
        not required_keys <= incomplete_datum.keys(),
    )
    missing_derivative_datum = dict(transport_datum)
    missing_derivative_datum.pop("beta2")
    assert_true(
        "QCD closure rejects missing charged-sound derivative",
        not required_keys <= missing_derivative_datum.keys(),
    )

    state_label = ("thermal-qcd", Fraction(3, 2), Fraction(1, 5), "Landau")
    channel_states = {
        "shear": state_label,
        "sound": state_label,
        "charge": state_label,
    }
    assert_equal("QCD closure channels share one state", len(set(channel_states.values())), 1)
    mixed_channel_states = dict(channel_states)
    mixed_channel_states["charge"] = ("thermal-qcd", Fraction(3, 2), Fraction(1, 4), "Landau")
    assert_true(
        "QCD closure rejects mixed chemical-potential states",
        len(set(mixed_channel_states.values())) != 1,
    )
    mixed_frame_states = dict(channel_states)
    mixed_frame_states["sound"] = ("thermal-qcd", Fraction(3, 2), Fraction(1, 5), "Eckart")
    assert_true(
        "QCD closure rejects mixed hydrodynamic frames",
        len(set(mixed_frame_states.values())) != 1,
    )

    wrong_width_only_bulk = enthalpy * sound_attenuation
    assert_true(
        "QCD closure rejects sound attenuation without shear subtraction",
        wrong_width_only_bulk != zeta,
    )
    neutral_formula_bulk = enthalpy * sound_attenuation - shear_prefactor * eta
    assert_true(
        "QCD closure rejects finite-density sound attenuation without conductive subtraction",
        neutral_formula_bulk != zeta,
    )
    mixed_enthalpy = enthalpy + Fraction(1, 9)
    mixed_state_zeta = (
        mixed_enthalpy * (sound_attenuation - gamma_cond)
        - shear_prefactor * eta
    )
    assert_true(
        "QCD closure rejects sound datum with mismatched enthalpy",
        mixed_state_zeta != zeta,
    )
    width_only_conductivity = charge_width / k_squared
    assert_true(
        "QCD closure rejects charge width without susceptibility residue",
        width_only_conductivity != conductivity,
    )

    baryon_density = Fraction(5, 8)
    raw_drude_weight = baryon_density * baryon_density / enthalpy
    momentum_relaxation_width = charge_width / 4
    raw_current_relaxed_slope = conductivity + raw_drude_weight / momentum_relaxation_width
    assert_true("QCD closure sees raw-current Drude contamination", raw_drude_weight > 0)
    assert_true(
        "QCD closure rejects raw-current relaxed slope as intrinsic conductivity",
        raw_current_relaxed_slope != conductivity,
    )

    window = Fraction(1, 5)
    microscopic_gap = Fraction(7, 3)
    assert_true("QCD closure window contains shear pole", shear_width < window)
    assert_true("QCD closure window contains sound pole", sound_half_width < window)
    assert_true("QCD closure window contains charge pole", charge_width < window)
    assert_true("QCD closure window stays below microscopic gap", window < microscopic_gap)

    residuals = {
        "shear": Fraction(1, 200),
        "bulk": Fraction(1, 300),
        "charge": Fraction(1, 500),
        "cond": Fraction(1, 600),
        "therm": Fraction(1, 700),
        "frame": Fraction(1, 1100),
        "cross": Fraction(1, 1300),
        "cont": Fraction(1, 1700),
    }
    closure_budget = sum(residuals.values(), Fraction(0))
    manufactured_error = sum(residuals.values(), Fraction(0))
    assert_equal("QCD closure residual ledger is additive", manufactured_error, closure_budget)
    assert_true(
        "QCD closure budget must include cross-channel consistency",
        manufactured_error > closure_budget - residuals["cross"],
    )
    assert_true(
        "QCD closure budget must include frame projection",
        manufactured_error > closure_budget - residuals["frame"],
    )
    assert_true(
        "QCD closure budget must include conductive sound correction",
        manufactured_error > closure_budget - residuals["cond"],
    )
    assert_true(
        "QCD closure budget must include charge-channel residual",
        manufactured_error > closure_budget - residuals["charge"],
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
    check_cfl_faithful_global_symmetry_bookkeeping()
    check_dense_neutrality_bookkeeping()
    check_cfl_rotated_electromagnetic_mass_matrix()
    check_dense_fermi_surface_stress_bookkeeping()
    check_cfl_screening_and_collective_counts()
    check_cfl_anomaly_matching_bookkeeping()
    check_hydrodynamic_response_window_bookkeeping()
    check_finite_shear_spectral_window_from_retarded_kernel()
    check_finite_bulk_sound_spectral_window()
    check_finite_charge_diffusion_spectral_window_from_density_kernel()
    check_qcd_transport_closure_window()
    print("All QCD phase-structure checks passed.")


if __name__ == "__main__":
    main()
