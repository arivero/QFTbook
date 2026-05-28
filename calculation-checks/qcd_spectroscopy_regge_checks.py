#!/usr/bin/env python3
"""Exact algebra checks for QCD spectroscopy and Regge conventions."""

from __future__ import annotations

from fractions import Fraction


Poly = tuple[Fraction, ...]  # coefficients in ascending powers
Matrix = tuple[tuple[Fraction, ...], ...]


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def poly_mul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return tuple(out)


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols))
        for i in range(rows)
    )


def mat_transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def mat_inv_2(a: Matrix) -> Matrix:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


def trace_2(a: Matrix) -> Fraction:
    return a[0][0] + a[1][1]


def det_2(a: Matrix) -> Fraction:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def identity_matrix(n: int) -> Matrix:
    return tuple(
        tuple(Fraction(1) if i == j else Fraction(0) for j in range(n))
        for i in range(n)
    )


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


def check_pseudoscalar_baryon_partial_waves() -> None:
    def allowed_j_and_parity(orbital_l: int) -> tuple[tuple[Fraction, ...], int]:
        if orbital_l == 0:
            spins = (Fraction(1, 2),)
        else:
            spins = (Fraction(orbital_l) - Fraction(1, 2), Fraction(orbital_l) + Fraction(1, 2))
        parity = -1 if orbital_l % 2 == 0 else 1
        return spins, parity

    assert_equal("S-wave pseudoscalar-baryon J", allowed_j_and_parity(0)[0], (Fraction(1, 2),))
    assert_equal("S-wave pseudoscalar-baryon parity", allowed_j_and_parity(0)[1], -1)
    assert_equal(
        "P-wave pseudoscalar-baryon J",
        allowed_j_and_parity(1)[0],
        (Fraction(1, 2), Fraction(3, 2)),
    )
    assert_equal("P-wave pseudoscalar-baryon parity", allowed_j_and_parity(1)[1], 1)
    assert_equal(
        "D-wave pseudoscalar-baryon J",
        allowed_j_and_parity(2)[0],
        (Fraction(3, 2), Fraction(5, 2)),
    )
    assert_equal("D-wave pseudoscalar-baryon parity", allowed_j_and_parity(2)[1], -1)


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


def check_triple_regge_exponents_and_eikonal_poisson() -> None:
    alpha_i = Fraction(4, 3)
    alpha_j = Fraction(5, 4)
    alpha_k = Fraction(7, 6)
    gap_exponent = alpha_i + alpha_j - 2
    missing_mass_exponent = alpha_k - 1
    assert_equal("triple-Regge rapidity-gap exponent", gap_exponent, Fraction(7, 12))
    assert_equal("triple-Regge missing-mass exponent", missing_mass_exponent, Fraction(1, 6))

    delta = Fraction(1, 9)
    slope_t = Fraction(-2, 15)
    alpha_p_t = 1 + delta + slope_t
    assert_equal("triple-Pomeron gap exponent", 2 * alpha_p_t - 2, 2 * (delta + slope_t))

    # For a one-channel absorptive eikonal, the probabilities
    # P_n=e^{-Omega} Omega^n/n! sum to one.  Equivalently, every positive
    # coefficient in the formal product e^{-Omega} e^{Omega} vanishes.
    for degree in range(1, 8):
        coefficient = sum(
            Fraction((-1) ** k, factorial(k) * factorial(degree - k))
            for k in range(degree + 1)
        )
        assert_equal(f"eikonal Poisson normalization coefficient {degree}", coefficient, Fraction(0))


def falling_factorial(n: int, r: int) -> int:
    if n < r:
        return 0
    out = 1
    for k in range(r):
        out *= n - k
    return out


def check_reggeon_diffusion_and_agk_moments() -> None:
    # The free Reggeon quadratic datum gives exp[(Delta-alpha' q^2)Y].
    # With t=-q^2 the trajectory exponent is alpha(t)-1=Delta+alpha' t.
    delta = Fraction(2, 9)
    alpha_prime = Fraction(5, 13)
    momentum_sq = Fraction(7, 11)
    t = -momentum_sq
    transverse_exponent = delta - alpha_prime * momentum_sq
    trajectory_exponent = delta + alpha_prime * t
    assert_equal("free Reggeon trajectory exponent", transverse_exponent, trajectory_exponent)

    # Eikonal AGK-type cancellation: the coefficient of Omega^m in the r-th
    # factorial moment of P_n=e^{-Omega} Omega^n/n! is delta_{m,r}.
    for r in range(1, 6):
        for m in range(0, 10):
            coefficient = sum(
                Fraction(
                    falling_factorial(n, r) * ((-1) ** (m - n)),
                    factorial(n) * factorial(m - n),
                )
                for n in range(0, m + 1)
            )
            expected = Fraction(1) if m == r else Fraction(0)
            assert_equal(f"eikonal AGK factorial moment r={r}, m={m}", coefficient, expected)


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


def check_swave_luscher_zeta_normalization() -> None:
    # The S-wave formula is q*cot(delta)=Z00/pi^(3/2).  Stripping the common
    # displayed pi factor, the exact rational statement is q*cot(delta)=Z00.
    q = Fraction(3, 5)
    zeta = Fraction(7, 11)
    cot_delta_rational = zeta / q
    assert_equal("S-wave zeta q cot(delta)", q * cot_delta_rational, zeta)

    # With delta+phi=n*pi, cot(delta)=-cot(phi).  The monograph convention is
    # cot(phi)=-Z00/(pi^(3/2) q), again checked after removing the common
    # irrational pi factor.
    cot_phi_rational = -zeta / q
    assert_equal("S-wave phase-function sign", cot_delta_rational, -cot_phi_rational)

    # Since k=2*pi*q/L, the same formula gives
    # k*cot(delta)=2*Z00/(sqrt(pi)*L).  The rational coefficient is 2/L.
    length = Fraction(13, 4)
    kcot_rational = Fraction(2) * zeta / length
    assert_equal("S-wave k cot(delta) zeta coefficient", kcot_rational, Fraction(2, 1) * zeta / length)


def check_pipi_crossing_and_roy_subtractions() -> None:
    # The isospin amplitudes T=(T0,T1,T2) are obtained from
    # A=(A(s,t,u), A(t,s,u), A(u,t,s)) by T=M A.  Crossing matrices are
    # C=M P M^{-1}; the exact rational entries are convention-sensitive.
    m: Matrix = (
        (Fraction(3), Fraction(1), Fraction(1)),
        (Fraction(0), Fraction(1), -Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(1)),
    )
    m_inv: Matrix = (
        (Fraction(1, 3), Fraction(0), -Fraction(1, 3)),
        (Fraction(0), Fraction(1, 2), Fraction(1, 2)),
        (Fraction(0), -Fraction(1, 2), Fraction(1, 2)),
    )
    p_st: Matrix = (
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    p_su: Matrix = (
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
    )
    c_st_expected: Matrix = (
        (Fraction(1, 3), Fraction(1), Fraction(5, 3)),
        (Fraction(1, 3), Fraction(1, 2), -Fraction(5, 6)),
        (Fraction(1, 3), -Fraction(1, 2), Fraction(1, 6)),
    )
    c_su_expected: Matrix = (
        (Fraction(1, 3), -Fraction(1), Fraction(5, 3)),
        (-Fraction(1, 3), Fraction(1, 2), Fraction(5, 6)),
        (Fraction(1, 3), Fraction(1, 2), Fraction(1, 6)),
    )
    c_st = mat_mul(mat_mul(m, p_st), m_inv)
    c_su = mat_mul(mat_mul(m, p_su), m_inv)
    assert_equal("pi-pi s-t crossing matrix", c_st, c_st_expected)
    assert_equal("pi-pi s-u crossing matrix", c_su, c_su_expected)
    assert_equal("pi-pi crossing involution st", mat_mul(c_st, c_st), identity_matrix(3))
    assert_equal("pi-pi crossing involution su", mat_mul(c_su, c_su), identity_matrix(3))

    # Roy subtraction polynomials in the monograph convention:
    # k00=a00+x/12*(2a00-5a02), k11=x/72*(2a00-5a02),
    # k02=a02-x/24*(2a00-5a02), where x=(s-4m_pi^2)/m_pi^2.
    a00 = Fraction(7, 5)
    a02 = -Fraction(2, 9)
    x = Fraction(11, 13)
    combo = 2 * a00 - 5 * a02
    k00 = a00 + x * combo / 12
    k11 = x * combo / 72
    k02 = a02 - x * combo / 24
    assert_equal("Roy subtraction threshold k00", a00 + Fraction(0) * combo / 12, a00)
    assert_equal("Roy subtraction threshold k02", a02 - Fraction(0) * combo / 24, a02)
    assert_equal("Roy subtraction threshold k11", Fraction(0) * combo / 72, Fraction(0))
    assert_equal("Roy subtraction slope ratio 00/11", (combo / 12) / (combo / 72), Fraction(6))
    assert_equal("Roy subtraction slope ratio 02/11", (-combo / 24) / (combo / 72), -Fraction(3))
    assert_equal("Roy subtraction finite x relation", k00 - a00, Fraction(6) * k11)
    assert_equal("Roy subtraction finite x relation 02", k02 - a02, -Fraction(3) * k11)


def check_roy_steiner_unequal_mass_kinematics() -> None:
    # Elastic A(m1)+B(m2)->A(m1)+B(m2) kinematics:
    # k_s^2=lambda(s,m1^2,m2^2)/(4s),
    # t=-2 k_s^2(1-z), u=2(m1^2+m2^2)-s-t.
    m1_sq = Fraction(4)
    m2_sq = Fraction(9)
    s = Fraction(49)
    z = Fraction(3, 7)
    s_plus = Fraction(25)
    s_minus = Fraction(1)
    k_sq = (s - s_plus) * (s - s_minus) / (4 * s)
    t = -2 * k_sq * (1 - z)
    u = 2 * (m1_sq + m2_sq) - s - t
    assert_equal("unequal-mass Mandelstam sum", s + t + u, 2 * (m1_sq + m2_sq))
    assert_equal("forward unequal-mass t", -2 * k_sq * (1 - Fraction(1)), Fraction(0))
    assert_equal("backward unequal-mass t", -2 * k_sq * (1 - Fraction(-1)), -4 * k_sq)

    # Partial-wave normalization in the monograph convention:
    # T(z)=16*pi sum_l (2l+1) P_l(z) f_l, so the inverse coefficient
    # (1/(32*pi)) int_{-1}^1 P_l T dz recovers f_l.  After stripping pi,
    # the rational coefficient is (1/32)*16*(2/(2l+1))*(2l+1)=1.
    for ell in range(0, 6):
        inverse_coefficient = Fraction(1, 32) * 16 * Fraction(2, 2 * ell + 1) * (2 * ell + 1)
        assert_equal(f"unequal-mass partial-wave inverse ell={ell}", inverse_coefficient, Fraction(1))


def check_gevp_basis_covariance() -> None:
    c0: Matrix = (
        (Fraction(5), Fraction(1)),
        (Fraction(1), Fraction(3)),
    )
    ct: Matrix = (
        (Fraction(7, 2), Fraction(2, 3)),
        (Fraction(2, 3), Fraction(11, 5)),
    )
    r: Matrix = (
        (Fraction(2), Fraction(-1)),
        (Fraction(1), Fraction(1)),
    )
    rt = mat_transpose(r)
    c0_prime = mat_mul(mat_mul(r, c0), rt)
    ct_prime = mat_mul(mat_mul(r, ct), rt)
    gevp_matrix = mat_mul(mat_inv_2(c0), ct)
    gevp_matrix_prime = mat_mul(mat_inv_2(c0_prime), ct_prime)

    # Generalized eigenvalues of (Ct,C0) are the eigenvalues of C0^{-1}Ct.
    # Under C -> R C R^T this matrix is similar to the original one, so the
    # 2x2 characteristic polynomial, represented by trace and determinant, is
    # invariant.
    assert_equal("GEVP trace basis covariance", trace_2(gevp_matrix_prime), trace_2(gevp_matrix))
    assert_equal("GEVP determinant basis covariance", det_2(gevp_matrix_prime), det_2(gevp_matrix))


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


def check_stable_current_three_point_ratio() -> None:
    # Exact finite-dimensional model of the transfer-matrix extraction:
    # C3_leading = Z_out Z_in exp_out exp_in M, and the fitted overlap/energy
    # denominator removes only the external propagation and source overlap.
    z_in = Fraction(5, 3)
    z_out = Fraction(-7, 4)
    matrix_element = Fraction(11, 6)
    exp_in = Fraction(2, 5)
    exp_out = Fraction(3, 7)
    leading_three_point = z_out * z_in * exp_out * exp_in * matrix_element
    leading_denominator = z_out * z_in * exp_out * exp_in
    assert_equal(
        "stable-current leading three-point ratio",
        leading_three_point / leading_denominator,
        matrix_element,
    )

    # Excited-state terms in the sink and source channels remain proportional
    # to the corresponding suppression factors exp(-Delta_out(t-tau)) and
    # exp(-Delta_in tau) after the same division.
    sink_overlap = Fraction(13, 10)
    source_overlap = Fraction(-17, 12)
    sink_current = Fraction(19, 8)
    source_current = Fraction(-23, 9)
    sink_suppression = Fraction(1, 29)
    source_suppression = Fraction(1, 31)
    numerator = (
        leading_three_point
        + sink_overlap * z_in * exp_out * sink_suppression * exp_in * sink_current
        + z_out * source_overlap * exp_out * exp_in * source_suppression * source_current
    )
    ratio = numerator / leading_denominator
    expected_ratio = (
        matrix_element
        + (sink_overlap / z_out) * sink_suppression * sink_current
        + (source_overlap / z_in) * source_suppression * source_current
    )
    assert_equal("stable-current excited-state bookkeeping", ratio, expected_ratio)


def check_forward_compton_baldin_prefactor() -> None:
    # In the convention Im f(omega)=omega sigma(omega)/(4*pi), the
    # once-subtracted even dispersion relation gives the omega^2 coefficient
    # (2/pi) int Im f(omega')/omega'^3.  The rational part of the prefactor is
    # therefore 2*(1/4)=1/2, with the two displayed pi factors giving
    # 1/(2*pi^2).
    dispersion_rational = Fraction(2)
    optical_rational = Fraction(1, 4)
    assert_equal(
        "Baldin rational prefactor",
        dispersion_rational * optical_rational,
        Fraction(1, 2),
    )

    # A finite spectral measure model: the coefficient obtained by expanding
    # the dispersion kernel equals the Baldin sum over cross-section atoms.
    atoms = [(Fraction(3, 5), Fraction(2, 7)), (Fraction(11, 6), Fraction(5, 13))]
    dispersion_coeff_rational = sum(
        dispersion_rational * optical_rational * sigma / (omega**2)
        for omega, sigma in atoms
    )
    baldin_rational = Fraction(1, 2) * sum(sigma / (omega**2) for omega, sigma in atoms)
    assert_equal("Baldin finite-atom expansion", dispersion_coeff_rational, baldin_rational)


def check_forward_spin_gdh_prefactor() -> None:
    # In the convention Im g(omega)=omega DeltaSigma(omega)/(8*pi), the odd
    # dispersion relation gives the coefficient of omega as
    # (2/pi) int Im g(omega')/omega'^2.  The rational part is 2*(1/8)=1/4,
    # with the displayed pi factors giving 1/(4*pi^2).
    dispersion_rational = Fraction(2)
    optical_rational = Fraction(1, 8)
    assert_equal(
        "GDH rational dispersion prefactor",
        dispersion_rational * optical_rational,
        Fraction(1, 4),
    )

    # Comparing a_1 omega with a_1=-e^2 kappa^2/(8*pi M^2) gives
    # int DeltaSigma/omega = 4*pi^2*a_1
    # = -pi*e^2*kappa^2/(2 M^2).  This checks the rational coefficient and
    # the sign for DeltaSigma=sigma_{1/2}-sigma_{3/2}.
    low_energy_rational = -Fraction(1, 8)
    integral_rational = Fraction(4) * low_energy_rational
    assert_equal(
        "GDH low-energy rational coefficient",
        integral_rational,
        -Fraction(1, 2),
    )

    # The omega^3 coefficient has the same dispersion/optical rational
    # prefactor but two additional powers of omega' in the denominator.
    atoms = [(Fraction(4, 7), Fraction(-3, 11)), (Fraction(9, 5), Fraction(8, 13))]
    dispersion_coeff_rational = sum(
        dispersion_rational * optical_rational * delta_sigma / (omega**3)
        for omega, delta_sigma in atoms
    )
    gamma0_rational = Fraction(1, 4) * sum(
        delta_sigma / (omega**3) for omega, delta_sigma in atoms
    )
    assert_equal(
        "forward spin polarizability finite-atom expansion",
        dispersion_coeff_rational,
        gamma0_rational,
    )


def main() -> None:
    check_gell_mann_okubo()
    check_decuplet_equal_spacing()
    check_pseudoscalar_baryon_partial_waves()
    check_veneziano_residue_degree()
    check_rotating_string_slope_coefficient()
    check_triple_regge_exponents_and_eikonal_poisson()
    check_reggeon_diffusion_and_agk_moments()
    check_luscher_kmatrix_pole_algebra()
    check_swave_luscher_zeta_normalization()
    check_pipi_crossing_and_roy_subtractions()
    check_roy_steiner_unequal_mass_kinematics()
    check_gevp_basis_covariance()
    check_coupled_channel_determinant_reduction()
    check_quarkonium_spin_centroid()
    check_nucleon_sachs_coordinate_transform()
    check_stable_current_three_point_ratio()
    check_forward_compton_baldin_prefactor()
    check_forward_spin_gdh_prefactor()
    print("All QCD spectroscopy and Regge convention checks passed.")


if __name__ == "__main__":
    main()
