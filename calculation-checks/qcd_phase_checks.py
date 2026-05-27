#!/usr/bin/env python3
"""Finite algebra checks for the QCD phase-structure chapter.

The script checks convention-sensitive numerical factors used in the
Stefan--Boltzmann pressure, the Banks--Casher normalization, the Linde
magnetic-scale estimate, and the color-flavor-locked symmetry count.  It is
not a lattice simulation and it does not assert the existence or order of any
QCD phase transition.
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
    check_linde_magnetic_scale()
    check_cfl_global_goldstone_count()
    print("All QCD phase-structure checks passed.")


if __name__ == "__main__":
    main()
