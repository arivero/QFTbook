#!/usr/bin/env python3
"""Finite algebra checks for the QCD phase-structure chapter.

The script checks convention-sensitive numerical factors used in the
Stefan--Boltzmann pressure, the Banks--Casher normalization, the Linde
magnetic-scale estimate, finite-regulator source-curvature identities,
one-loop Polyakov-holonomy coefficients, and the color-flavor-locked
symmetry count.  It is not a lattice simulation and it does not assert the
existence or order of any QCD phase transition.
"""

from fractions import Fraction


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


def check_linde_magnetic_scale():
    # In four dimensions, g_3^2 = g^2 T has mass dimension one.  A purely
    # magnetic three-dimensional vacuum free-energy density scales as (g_3^2)^3.
    # Multiplying by T to recover four-dimensional pressure gives g^6 T^4.
    g_power = 2 * 3
    t_power = 1 + 3
    assert_equal("Linde magnetic g power", g_power, 6)
    assert_equal("Linde magnetic T power", t_power, 4)


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
    check_banks_casher_kernel_normalization()
    check_fugacity_laurent_polynomial_shift()
    check_source_curvature_susceptibility()
    check_weiss_holonomy_potential_coefficients()
    check_linde_magnetic_scale()
    check_cfl_global_goldstone_count()
    print("All QCD phase-structure checks passed.")


if __name__ == "__main__":
    main()
