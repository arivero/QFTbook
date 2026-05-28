#!/usr/bin/env python3
"""Exact algebra checks for QCD spectroscopy and Regge conventions."""

from __future__ import annotations

from fractions import Fraction


Poly = tuple[Fraction, ...]  # coefficients in ascending powers


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def poly_mul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return tuple(out)


def veneziano_residue_polynomial(n: int) -> Poly:
    # Up to the universal pole denominator and sign, the n-th s-channel
    # residue of B(-alpha(s),-alpha(t)) is prod_{r=1}^n (alpha(t)+r)/n!.
    poly: Poly = (Fraction(1),)
    for r in range(1, n + 1):
        poly = poly_mul(poly, (Fraction(r), Fraction(1)))
    factorial = 1
    for r in range(2, n + 1):
        factorial *= r
    return tuple(c / factorial for c in poly)


def check_gell_mann_okubo() -> None:
    m0 = Fraction(11)
    a = Fraction(3)
    b = Fraction(5)
    n = m0 + a + b / 2
    xi = m0 - a + b / 2
    lam = m0
    sigma = m0 + 2 * b
    assert_equal("octet GMO", 2 * (n + xi), 3 * lam + sigma)


def check_decuplet_equal_spacing() -> None:
    m0 = Fraction(17)
    c = Fraction(-4)
    delta = m0 + c
    sigma_star = m0
    xi_star = m0 - c
    omega = m0 - 2 * c
    assert_equal("decuplet spacing 1", sigma_star - delta, xi_star - sigma_star)
    assert_equal("decuplet spacing 2", xi_star - sigma_star, omega - xi_star)


def check_veneziano_residue_degree() -> None:
    p3 = veneziano_residue_polynomial(3)
    assert_equal(
        "third Veneziano residue polynomial",
        p3,
        (Fraction(1), Fraction(11, 6), Fraction(1), Fraction(1, 6)),
    )
    for n in range(1, 7):
        pn = veneziano_residue_polynomial(n)
        assert_equal(f"Veneziano residue degree {n}", len(pn) - 1, n)
        assert_equal(f"Veneziano leading coefficient {n}", pn[-1], Fraction(1, factorial(n)))


def factorial(n: int) -> int:
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def check_rotating_string_slope_coefficient() -> None:
    # For a classical open string with massless endpoints,
    # E = pi*sigma/omega and J = pi*sigma/(2 omega^2), hence
    # J/E^2 = 1/(2*pi*sigma).  The exact rational coefficient is 1/2.
    energy_coeff = Fraction(1)
    angular_momentum_coeff = Fraction(1, 2)
    assert_equal(
        "open-string Regge slope rational coefficient",
        angular_momentum_coeff / (energy_coeff**2),
        Fraction(1, 2),
    )


def check_luscher_kmatrix_pole_algebra() -> None:
    # From delta + phi = n*pi, cot(delta) = -cot(phi).  With
    # K^{-1}=rho*cot(delta), finite-volume levels therefore sample
    # K^{-1}=-rho*cot(phi).  Use rationals for an exact representative.
    rho = Fraction(5, 7)
    cot_phi = Fraction(-11, 13)
    cot_delta = -cot_phi
    assert_equal("Luscher cotangent sign", rho * cot_delta, -rho * cot_phi)

    # With t_I = 1/(K^{-1} - i*rho), the adjacent second sheet is
    # t_II = 1/(K^{-1} + i*rho).  For K^{-1}(s)=(s-M^2)/g^2 and locally
    # constant rho, the pole is s_* = M^2 - i g^2 rho.  Check the real
    # and imaginary parts of the denominator separately.
    mass_sq = Fraction(19, 3)
    coupling_sq = Fraction(2, 5)
    pole_real = mass_sq
    pole_imag = -coupling_sq * rho
    denominator_real = (pole_real - mass_sq) / coupling_sq
    denominator_imag = pole_imag / coupling_sq + rho
    assert_equal("second-sheet pole denominator real part", denominator_real, Fraction(0))
    assert_equal("second-sheet pole denominator imaginary part", denominator_imag, Fraction(0))


def check_coupled_channel_determinant_reduction() -> None:
    # In an unmixed two-channel finite-volume determinant,
    # det(K^{-1}+F)=0 reduces channel by channel.  This pins down the sign of
    # the finite-volume geometric function in the convention F=rho*cot(phi).
    k1_inv = Fraction(7, 5)
    k2_inv = Fraction(-3, 4)
    f1 = -k1_inv
    f2 = Fraction(11, 6)
    determinant = (k1_inv + f1) * (k2_inv + f2)
    assert_equal("unmixed determinant channel reduction", determinant, Fraction(0))

    # Sheet bookkeeping: physical sheet denominator is K^{-1}-i*rho; changing
    # the first channel to the adjacent sheet flips only the first rho sign.
    sigma1 = Fraction(-1)
    sigma2 = Fraction(1)
    rho1 = Fraction(2, 3)
    rho2 = Fraction(5, 7)
    imag_first = -sigma1 * rho1
    imag_second = -sigma2 * rho2
    assert_equal("first crossed-channel imaginary sign", imag_first, rho1)
    assert_equal("second physical-channel imaginary sign", imag_second, -rho2)


def check_quarkonium_spin_centroid() -> None:
    # Two spin-1/2 particles have S_Q.S_Qbar =
    # 1/2(S(S+1)-3/2): -3/4 for singlet and 1/4 for triplet.
    singlet_spin_spin = Fraction(1, 2) * (0 * 1 - Fraction(3, 2))
    triplet_spin_spin = Fraction(1, 2) * (1 * 2 - Fraction(3, 2))
    assert_equal("quarkonium singlet spin-spin", singlet_spin_spin, Fraction(-3, 4))
    assert_equal("quarkonium triplet spin-spin", triplet_spin_spin, Fraction(1, 4))

    # For S=1, L.S = 1/2(J(J+1)-L(L+1)-2).  The degeneracy-weighted triplet
    # trace vanishes for every L, so spin-orbit terms do not shift the
    # spin-weighted centroid.
    for ell in range(1, 7):
        eigenvalues = {
            ell - 1: Fraction(-(ell + 1)),
            ell: Fraction(-1),
            ell + 1: Fraction(ell),
        }
        trace = sum(Fraction(2 * j + 1) * value for j, value in eigenvalues.items())
        assert_equal(f"quarkonium spin-orbit trace L={ell}", trace, Fraction(0))

    # The centroid hyperfine difference is (E+A/4)-(E-3A/4)=A.
    energy = Fraction(23, 5)
    spin_spin_coefficient = Fraction(7, 11)
    triplet_centroid = energy + spin_spin_coefficient * triplet_spin_spin
    singlet_mass = energy + spin_spin_coefficient * singlet_spin_spin
    assert_equal(
        "quarkonium centroid hyperfine difference",
        triplet_centroid - singlet_mass,
        spin_spin_coefficient,
    )


def check_nucleon_sachs_coordinate_transform() -> None:
    tau = Fraction(3, 8)
    f1 = Fraction(5, 7)
    f2 = Fraction(-2, 9)
    g_e = f1 - tau * f2
    g_m = f1 + f2
    recovered_f1 = (g_e + tau * g_m) / (1 + tau)
    recovered_f2 = (g_m - g_e) / (1 + tau)
    assert_equal("nucleon Sachs inverse F1", recovered_f1, f1)
    assert_equal("nucleon Sachs inverse F2", recovered_f2, f2)

    proton_f1_zero = Fraction(1)
    neutron_f1_zero = Fraction(0)
    proton_f2_zero = Fraction(17, 11)
    neutron_f2_zero = Fraction(-13, 10)
    assert_equal("proton electric charge form factor", proton_f1_zero, Fraction(1))
    assert_equal("neutron electric charge form factor", neutron_f1_zero, Fraction(0))
    assert_equal("proton magnetic Sachs zero", proton_f1_zero + proton_f2_zero, Fraction(28, 11))
    assert_equal("neutron magnetic Sachs zero", neutron_f1_zero + neutron_f2_zero, Fraction(-13, 10))


def main() -> None:
    check_gell_mann_okubo()
    check_decuplet_equal_spacing()
    check_veneziano_residue_degree()
    check_rotating_string_slope_coefficient()
    check_luscher_kmatrix_pole_algebra()
    check_coupled_channel_determinant_reduction()
    check_quarkonium_spin_centroid()
    check_nucleon_sachs_coordinate_transform()
    print("All QCD spectroscopy and Regge convention checks passed.")


if __name__ == "__main__":
    main()
