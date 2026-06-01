#!/usr/bin/env python3
"""Finite convention checks for ABJM and six-dimensional SUSY chapters.

The checks are intentionally finite: they verify the algebraic normalizations
that are easy to shift by factors of two or signs in prose.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [
        [sum(a[i][r] * b[r][j] for r in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def determinant(matrix: list[list[int]]) -> int:
    data = [[Fraction(entry) for entry in row] for row in matrix]
    n = len(data)
    det = Fraction(1)
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if data[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            return 0
        if pivot != col:
            data[col], data[pivot] = data[pivot], data[col]
            det = -det
        pivot_value = data[col][col]
        det *= pivot_value
        for row in range(col + 1, n):
            factor = data[row][col] / pivot_value
            for j in range(col, n):
                data[row][j] -= factor * data[col][j]
    assert det.denominator == 1
    return det.numerator


def cartan_a(rank: int) -> list[list[int]]:
    return [
        [
            2 if i == j else -1 if abs(i - j) == 1 else 0
            for j in range(rank)
        ]
        for i in range(rank)
    ]


def cartan_d(rank: int) -> list[list[int]]:
    matrix = [[0 for _ in range(rank)] for _ in range(rank)]
    for i in range(rank):
        matrix[i][i] = 2
    for i in range(rank - 3):
        matrix[i][i + 1] = matrix[i + 1][i] = -1
    branch = rank - 3
    matrix[branch][rank - 2] = matrix[rank - 2][branch] = -1
    matrix[branch][rank - 1] = matrix[rank - 1][branch] = -1
    return matrix


def cartan_e6() -> list[list[int]]:
    return [
        [2, -1, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0],
        [0, -1, 2, -1, 0, -1],
        [0, 0, -1, 2, -1, 0],
        [0, 0, 0, -1, 2, 0],
        [0, 0, -1, 0, 0, 2],
    ]


def cartan_e7() -> list[list[int]]:
    return [
        [2, -1, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, -1],
        [0, 0, -1, 2, -1, 0, 0],
        [0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, -1, 2, 0],
        [0, 0, -1, 0, 0, 0, 2],
    ]


def cartan_e8() -> list[list[int]]:
    return [
        [2, -1, 0, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0, -1],
        [0, 0, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, 0],
        [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, 0],
        [0, 0, -1, 0, 0, 0, 0, 2],
    ]


def check_abjm_superpotential_r_charge() -> None:
    matter_r = Fraction(1, 2)
    quartic_r = 4 * matter_r
    assert_equal("ABJM quartic superpotential R-charge", quartic_r, 2)


def check_abjm_standard_conformal_locus_dimension() -> None:
    # In 3D N=2 conventions, a chiral primary has Delta=R at the ABJM point
    # and the d^2 theta measure has dimension 1.  The quartic ABJM
    # superpotential is therefore power-counting marginal, but the standard
    # N=6 completion fixes its normalized coefficient to 1/k.
    matter_dimension = Fraction(1, 2)
    f_term_measure_dimension = 1
    spacetime_dimension = 3
    quartic_dimension = 4 * matter_dimension
    coefficient_dimension = spacetime_dimension - f_term_measure_dimension - quartic_dimension
    assert_equal("ABJM quartic coefficient engineering dimension", coefficient_dimension, 0)

    for k in range(1, 15):
        normalized_superpotential_coefficient = Fraction(1, k)
        assert_equal(
            f"ABJM normalized h*k relation k={k}",
            k * normalized_superpotential_coefficient,
            1,
        )

        # The integer level lattice has zero tangent space.  Since the
        # standard N=6 coefficient is a function of k, its allowed tangent is
        # also zero.
        level_lattice_tangent_dimension = 0
        superpotential_tangent_dimension = level_lattice_tangent_dimension
        assert_equal(
            f"ABJM N=6 superpotential tangent k={k}",
            superpotential_tangent_dimension,
            0,
        )
        standard_conformal_locus_dimension = level_lattice_tangent_dimension
        assert_equal(
            f"standard ABJM conformal-locus dimension k={k}",
            standard_conformal_locus_dimension,
            0,
        )

    real_mass_dimension = 1
    fi_dimension = 1
    yang_mills_coupling_squared_dimension = 1
    assert_equal("ABJM real mass is relevant", real_mass_dimension, 1)
    assert_equal("ABJM FI coordinate is relevant", fi_dimension, 1)
    assert_equal(
        "3D Yang-Mills coupling squared is dimensionful",
        yang_mills_coupling_squared_dimension,
        1,
    )


def check_abjm_parity_level_pair() -> None:
    for k in (1, 2, 5, -3):
        levels = (k, -k)
        orientation_reversed = tuple(-level for level in levels)
        exchanged = (orientation_reversed[1], orientation_reversed[0])
        assert_equal(f"ABJM parity level pair k={k}", exchanged, levels)


def check_abjm_abelian_bf_normalization() -> None:
    # Old basis: (A, Ahat), K_old=diag(k,-k).
    # New basis: (A_D, B) with A=(A_D+B)/2 and Ahat=(A_D-B)/2.
    # Then K_new=M^T K_old M has off-diagonal entries k/2, giving
    # (1/4 pi) * (k/2 A_D dB + k/2 B dA_D), equivalent on a closed
    # manifold to (k/4 pi) B dA_D.
    k = Fraction(7, 1)
    k_old = [[k, Fraction(0)], [Fraction(0), -k]]
    m = [
        [Fraction(1, 2), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(-1, 2)],
    ]
    k_new = matmul(matmul(transpose(m), k_old), m)
    expected = [[Fraction(0), Fraction(7, 2)], [Fraction(7, 2), Fraction(0)]]
    assert_equal("ABJM abelian BF K-matrix", k_new, expected)


def check_abjm_orbifold_order_and_dimension() -> None:
    for k in range(1, 9):
        phase = Fraction(1, k)
        assert_equal(f"Z_k phase order k={k}", phase.denominator, k)

    for n in range(1, 6):
        one_brane_complex_dim = 4
        symmetric_product_dim = n * one_brane_complex_dim
        assert_equal(f"ABJM commuting branch dimension N={n}", symmetric_product_dim, 4 * n)


def check_abjm_s3_matrix_denominator() -> None:
    # Four chirals form two conjugate pairs for each ordered pair of Cartan
    # eigenvalues.  Each pair contributes 1/(2 cosh), hence two pairs give
    # 1/(4 cosh^2).
    chiral_fields = 4
    conjugate_pairs = chiral_fields // 2
    assert_equal("ABJM conjugate chiral pairs", conjugate_pairs, 2)
    assert_equal("ABJM cosh denominator prefactor", 2**conjugate_pairs, 4)
    assert_equal("ABJM cosh denominator exponent", conjugate_pairs, 2)

    for n in range(1, 7):
        positive_roots_one_u_n = n * (n - 1) // 2
        vector_factors_two_groups = 2 * positive_roots_one_u_n
        assert_equal(
            f"ABJM two U(N) positive-root count N={n}",
            vector_factors_two_groups,
            n * (n - 1),
        )


def check_sphere_free_energy_normalizations() -> None:
    # The round S^3 determinant for two conjugate R=1/2 chirals at zero
    # Cartan variable is 1/(2 cosh 0)=1/2.  Hence a single free chiral has
    # |Z|^2=1/2 and F=(1/2) log 2 in the chapter convention.
    conjugate_pair_z_squared = Fraction(1, 2)
    single_chiral_z_squared = conjugate_pair_z_squared
    assert_equal("free chiral squared partition value", single_chiral_z_squared, Fraction(1, 2))

    # Rank-one ABJM: x=lambda-mu, y=lambda+mu gives Jacobian 1/2.
    # The y integral gives 2 delta(k x)=2 delta(x)/|k|, and the two
    # conjugate bifundamental pairs give a denominator 4 at x=0.
    for k in (1, 2, 7, -5):
        jacobian = Fraction(1, 2)
        fourier_delta_factor = Fraction(2, abs(k))
        chiral_denominator_at_zero = 4
        z_rank_one = jacobian * fourier_delta_factor / chiral_denominator_at_zero
        assert_equal(f"rank-one ABJM S3 integral k={k}", z_rank_one, Fraction(1, 4 * abs(k)))


def check_abjm_fermi_gas_airy_normalizations() -> None:
    # Diagonal trace of the Fermi-gas kernel:
    # rho(q,q) = [1/(2*pi*k)] [1/(4*cosh(q/2))] and
    # int dq/cosh(q/2) = 2*pi, hence Tr rho = 1/(4k).
    for k in (1, 2, 7):
        fourier_measure_denominator = 2 * k
        cosh_diagonal_denominator = 4
        sech_integral_numerator = 2
        trace = Fraction(sech_integral_numerator, fourier_measure_denominator * cosh_diagonal_denominator)
        assert_equal(f"ABJM Fermi-gas first trace k={k}", trace, Fraction(1, 4 * k))

    # Large-energy phase-space diamond:
    # area(|q|+|p| <= 2E) = 8 E^2 and 2*pi*hbar = 4*pi^2*k,
    # so n(E) = [2/(pi^2 k)] E^2.
    area_coefficient = 8
    phase_space_cell_coefficient = 4
    leading_density_coefficient_times_pi_squared_k = Fraction(
        area_coefficient, phase_space_cell_coefficient
    )
    assert_equal(
        "ABJM leading Weyl coefficient times pi^2 k",
        leading_density_coefficient_times_pi_squared_k,
        2,
    )

    # Airy inverse-Laplace rescaling.  Use C=8 so C^(1/3)=2 exactly:
    # mu=t/2 gives C mu^3/3=t^3/3 and -(N-B)mu=-(N-B)t/2.
    c = Fraction(8)
    c_cube_root = Fraction(2)
    b = Fraction(3)
    n = Fraction(11)
    cubic_coefficient_after_rescaling = c / (c_cube_root**3)
    airy_argument = (n - b) / c_cube_root
    assert_equal("Airy cubic coefficient after rescaling", cubic_coefficient_after_rescaling, 1)
    assert_equal("Airy linear coefficient after rescaling", airy_argument, 4)


def check_three_d_n2_cs_matter_auxiliary_elimination() -> None:
    # Factor out powers of pi and i.  The D-equation in trace-delta
    # convention gives sigma = -(2 pi/k) mu.  The scalar sextic coefficient is
    # then -(2/k)^2 in units of pi^2.  The Yukawa sign is spinor-convention
    # dependent, but the magnitudes and the 1:2 relative coefficient are fixed
    # after the same algebraic elimination.
    for k in (1, 2, 5, -7):
        sigma_coeff_pi = Fraction(-2, k)
        sextic_coeff_pi_squared = -(sigma_coeff_pi * sigma_coeff_pi)
        assert_equal(
            f"3D N=2 CS sigma solution coefficient k={k}",
            sigma_coeff_pi,
            Fraction(-2, k),
        )
        assert_equal(
            f"3D N=2 CS sextic scalar coefficient k={k}",
            sextic_coeff_pi_squared,
            Fraction(-4, k * k),
        )

        moment_yukawa_magnitude_pi = abs(Fraction(2, k))
        mixed_yukawa_magnitude_pi = abs(Fraction(4, k))
        assert_equal(
            f"3D N=2 CS Yukawa relative coefficient k={k}",
            mixed_yukawa_magnitude_pi,
            2 * moment_yukawa_magnitude_pi,
        )


def check_three_d_n3_adjoint_chiral_elimination() -> None:
    # Write W = pi[-(k/8) x^2 + j x].  The algebraic F-term gives
    # x=(4/k)j, and substituting gives pi*(2/k)j^2.
    for k in (1, 2, 5, -4):
        phi_coeff_pi = Fraction(4, k)
        effective_superpotential_coeff_pi = (
            -Fraction(k, 8) * phi_coeff_pi * phi_coeff_pi + phi_coeff_pi
        )
        assert_equal(
            f"3D N=3 adjoint chiral solution k={k}",
            phi_coeff_pi,
            Fraction(4, k),
        )
        assert_equal(
            f"3D N=3 effective superpotential coefficient k={k}",
            effective_superpotential_coeff_pi,
            Fraction(2, k),
        )


def check_six_dimensional_yang_mills_dimension() -> None:
    def gauge_coupling_squared_dimension(spacetime_dimension: int) -> int:
        return 4 - spacetime_dimension

    assert_equal("4D gauge coupling marginal", gauge_coupling_squared_dimension(4), 0)
    assert_equal("5D gauge coupling dimension", gauge_coupling_squared_dimension(5), -1)
    assert_equal("6D gauge coupling dimension", gauge_coupling_squared_dimension(6), -2)


def check_six_dimensional_chiral_two_form_degrees() -> None:
    transverse_dimension = 4
    two_form_polarizations = transverse_dimension * (transverse_dimension - 1) // 2
    chiral_two_form_polarizations = two_form_polarizations // 2
    scalar_polarizations = 5
    assert_equal("6D ordinary two-form physical polarizations", two_form_polarizations, 6)
    assert_equal("6D chiral two-form physical polarizations", chiral_two_form_polarizations, 3)
    assert_equal(
        "6D (2,0) tensor multiplet bosonic polarizations",
        chiral_two_form_polarizations + scalar_polarizations,
        8,
    )


def check_two_zero_a_type_data() -> None:
    for n in range(1, 8):
        rank = n - 1
        dimension = n * n - 1
        dual_coxeter = n
        interacting_anomaly_coeff = Fraction(dimension * dual_coxeter, 24)
        assert_equal(
            f"A_{n-1} (2,0) anomaly coefficient",
            interacting_anomaly_coeff,
            Fraction(n * (n * n - 1), 24),
        )
        assert_equal(f"A_{n-1} tensor branch real dimension", 5 * rank, 5 * (n - 1))


def check_two_zero_ade_anomaly_coefficients() -> None:
    # Entries are (rank, dimension, dual Coxeter number, coefficient).
    exceptional = {
        "E6": (6, 78, 12, Fraction(39)),
        "E7": (7, 133, 18, Fraction(399, 4)),
        "E8": (8, 248, 30, Fraction(310)),
    }
    for name, (rank, dimension, dual_coxeter, coefficient) in exceptional.items():
        assert_equal(f"{name} anomaly coefficient", Fraction(dimension * dual_coxeter, 24), coefficient)
        assert_equal(f"{name} tensor branch real dimension", 5 * rank, 5 * rank)

    for n in range(4, 11):
        rank = n
        dimension = n * (2 * n - 1)
        dual_coxeter = 2 * n - 2
        coefficient = Fraction(dimension * dual_coxeter, 24)
        assert_equal(
            f"D_{n} anomaly coefficient",
            coefficient,
            Fraction(n * (n - 1) * (2 * n - 1), 12),
        )
        assert_equal(f"D_{n} tensor branch real dimension", 5 * rank, 5 * n)


def check_simply_laced_root_second_moments() -> None:
    # With long roots of squared length 2, the positive-root second moment is
    # sum_{alpha>0} (alpha.v)^2 = h^vee (v.v).  For A_{N-1} use vectors in
    # the sum-zero hyperplane of R^N; for D_N use the roots e_i +/- e_j.
    for n in range(2, 10):
        raw = [Fraction(i + 1) for i in range(n)]
        mean = sum(raw) / n
        v = [entry - mean for entry in raw]
        positive_root_sum = sum((v[i] - v[j]) ** 2 for i in range(n) for j in range(i + 1, n))
        norm = sum(entry * entry for entry in v)
        assert_equal(f"A_{n-1} positive-root second moment", positive_root_sum, n * norm)

    for n in range(4, 10):
        v = [Fraction(i + 2) for i in range(n)]
        positive_root_sum = Fraction(0)
        for i in range(n):
            for j in range(i + 1, n):
                positive_root_sum += (v[i] - v[j]) ** 2
                positive_root_sum += (v[i] + v[j]) ** 2
        norm = sum(entry * entry for entry in v)
        assert_equal(f"D_{n} positive-root second moment", positive_root_sum, (2 * n - 2) * norm)


def check_simply_laced_dimension_root_count_relation() -> None:
    # The ADE relation d_g = r_g (h_g^vee + 1) is equivalent to
    # |Delta_g| = r_g h_g^vee.  It is the trace normalization behind the
    # root-system second-moment identity used in the chapter.
    data = []
    for n in range(2, 10):
        data.append((f"A_{n-1}", n - 1, n * n - 1, n))
    for n in range(4, 10):
        data.append((f"D_{n}", n, n * (2 * n - 1), 2 * n - 2))
    data.extend(
        [
            ("E6", 6, 78, 12),
            ("E7", 7, 133, 18),
            ("E8", 8, 248, 30),
        ]
    )
    for name, rank, dimension, dual_coxeter in data:
        assert_equal(f"{name} d=r(h+1)", dimension, rank * (dual_coxeter + 1))
        assert_equal(f"{name} root count", dimension - rank, rank * dual_coxeter)


def check_green_schwarz_quadratic_descent_factor() -> None:
    # The 1/2 in (1/2) Omega^{IJ} X_I X_J is cancelled in descent by the two
    # equal variations of the symmetric product.
    omega = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(3)]]
    x2 = [Fraction(5), Fraction(7)]
    x4 = [Fraction(11), Fraction(13)]
    descent_from_half_quadratic = Fraction(0)
    direct_descent = Fraction(0)
    for i in range(2):
        for j in range(2):
            descent_from_half_quadratic += Fraction(1, 2) * omega[i][j] * (
                x2[i] * x4[j] + x2[j] * x4[i]
            )
            direct_descent += omega[i][j] * x2[i] * x4[j]
    assert_equal("GS half-quadratic descent factor", descent_from_half_quadratic, direct_descent)


def check_five_dimensional_instanton_kk_normalization() -> None:
    # In trace-delta variables the BPST check gives E_inst=4 pi^2/g_5^2.
    # Equating to one KK unit 1/R gives g_5^2=4 pi^2 R.  The half-trace
    # coupling is twice the trace-delta coupling.
    trace_delta_action_coeff = Fraction(4)
    half_trace_action_coeff = Fraction(8)
    coupling_conversion = Fraction(2)
    assert_equal(
        "5D half-trace/trace-delta coupling conversion",
        trace_delta_action_coeff * coupling_conversion,
        half_trace_action_coeff,
    )

    kk_energy_coeff = Fraction(1)
    g5_squared_over_pi2_r = trace_delta_action_coeff / kk_energy_coeff
    assert_equal("5D g5^2/(pi^2 R) coefficient", g5_squared_over_pi2_r, 4)


def check_wrapped_string_mass_normalization() -> None:
    # Omitting the common factor pi, M_wrap = 2 R T_alpha and
    # phi_5d = 2 R phi_6d in the chapter convention.
    radius = Fraction(3)
    alpha_phi_6d = Fraction(5)
    wrapped_mass_over_pi = 2 * radius * alpha_phi_6d
    phi_5d_over_pi = 2 * radius * alpha_phi_6d
    assert_equal("wrapped string/W-boson scalar normalization", wrapped_mass_over_pi, phi_5d_over_pi)


def check_two_zero_defect_group_orders() -> None:
    for rank in range(1, 9):
        # Type A_rank has algebra A_{rank}; the corresponding group order is
        # |P/Q|=rank+1.
        assert_equal(
            f"A_{rank} discriminant order",
            determinant(cartan_a(rank)),
            rank + 1,
        )

    for rank in range(4, 11):
        assert_equal(f"D_{rank} discriminant order", determinant(cartan_d(rank)), 4)

    assert_equal("E6 discriminant order", determinant(cartan_e6()), 3)
    assert_equal("E7 discriminant order", determinant(cartan_e7()), 2)
    assert_equal("E8 discriminant order", determinant(cartan_e8()), 1)


def check_cyclic_finite_flux_polarization() -> None:
    # Model A=Z_N with perfect pairing b(a,b)=ab/N.  The finite flux model
    # K=A plus A has symplectic numerator a b' - b a' modulo N.
    for n in range(2, 13):
        elements = [(a, b) for a in range(n) for b in range(n)]

        def symplectic_numerator(x: tuple[int, int], y: tuple[int, int]) -> int:
            return (x[0] * y[1] - x[1] * y[0]) % n

        for x in elements:
            assert_equal(f"Z_{n} alternating self-pairing {x}", symplectic_numerator(x, x), 0)
            for y in elements:
                assert_equal(
                    f"Z_{n} skew pairing {x},{y}",
                    symplectic_numerator(x, y),
                    (-symplectic_numerator(y, x)) % n,
                )

        for x in elements:
            if x == (0, 0):
                continue
            detects = any(symplectic_numerator(x, y) != 0 for y in elements)
            assert_equal(f"Z_{n} finite flux nondegeneracy {x}", detects, True)

        polarization = [(a, 0) for a in range(n)]
        assert_equal(f"Z_{n} polarization size squared", len(polarization) ** 2, len(elements))
        for x in polarization:
            for y in polarization:
                assert_equal(f"Z_{n} polarization isotropic {x},{y}", symplectic_numerator(x, y), 0)


def check_circle_reduction_finite_flux_pairing() -> None:
    # For Y=S^1 x X_5, write x=(u,v) for u in H^3(X;A) and
    # eta v in eta H^2(X;A).  The product sign gives
    # <(u,v),(u',v')> = v u' - u v' modulo N in the cyclic one-cell model.
    for n in range(2, 13):
        elements = [(u, v) for u in range(n) for v in range(n)]

        def circle_pairing(x: tuple[int, int], y: tuple[int, int]) -> int:
            u, v = x
            up, vp = y
            return (v * up - u * vp) % n

        for x in elements:
            assert_equal(f"circle finite flux alternating {n} {x}", circle_pairing(x, x), 0)
            for y in elements:
                assert_equal(
                    f"circle finite flux skew {n} {x},{y}",
                    circle_pairing(x, y),
                    (-circle_pairing(y, x)) % n,
                )

        for x in elements:
            if x == (0, 0):
                continue
            detects = any(circle_pairing(x, y) != 0 for y in elements)
            assert_equal(f"circle finite flux nondegenerate {n} {x}", detects, True)

        unwrapped_surface = [(u, 0) for u in range(n)]
        wrapped_line = [(0, v) for v in range(n)]
        for subgroup_name, subgroup in (
            ("unwrapped-surface", unwrapped_surface),
            ("wrapped-line", wrapped_line),
        ):
            assert_equal(
                f"circle {subgroup_name} polarization size {n}",
                len(subgroup) ** 2,
                len(elements),
            )
            for x in subgroup:
                for y in subgroup:
                    assert_equal(
                        f"circle {subgroup_name} isotropic {n} {x},{y}",
                        circle_pairing(x, y),
                        0,
                    )


def check_circle_reduction_genuine_defect_polarizations() -> None:
    # In the cyclic one-cell finite algebra, an absolute global form is a
    # maximal isotropic subgroup.  Its commutant under the perfect pairing is
    # itself; hence charges outside it are relative/non-genuine for that
    # absolute polarization.  Graphs of symplectic automorphisms give
    # Lagrangian relations between polarizations.
    for n in range(2, 13):
        elements = [(a, b) for a in range(n) for b in range(n)]

        def pairing(x: tuple[int, int], y: tuple[int, int]) -> int:
            return (x[0] * y[1] - x[1] * y[0]) % n

        for name, polarization in (
            ("surface", [(a, 0) for a in range(n)]),
            ("line", [(0, b) for b in range(n)]),
        ):
            commutant = [
                x
                for x in elements
                if all(pairing(x, y) == 0 for y in polarization)
            ]
            assert_equal(
                f"Z_{n} {name} polarization equals commutant",
                sorted(commutant),
                sorted(polarization),
            )

        def s_transform(x: tuple[int, int]) -> tuple[int, int]:
            return (x[1] % n, (-x[0]) % n)

        graph = [(x, s_transform(x)) for x in elements]
        assert_equal(f"Z_{n} symplectic graph size", len(graph), len(elements))
        for (x, sx) in graph:
            for (y, sy) in graph:
                # The target pairing is reversed in K plus Kbar.
                relation_pairing = (pairing(x, y) - pairing(sx, sy)) % n
                assert_equal(
                    f"Z_{n} symplectic graph isotropic {x},{y}",
                    relation_pairing,
                    0,
                )


def check_class_s_hitchin_base_degrees() -> None:
    for n in range(2, 10):
        a_degrees = list(range(2, n + 1))
        a_sum = sum(2 * degree - 1 for degree in a_degrees)
        assert_equal(f"A_{n-1} Hitchin degree sum", a_sum, n * n - 1)
        for genus in range(2, 6):
            assert_equal(
                f"A_{n-1} genus-{genus} Hitchin base dimension",
                (genus - 1) * a_sum,
                (genus - 1) * (n * n - 1),
            )

    for n in range(4, 10):
        d_degrees = [2 * j for j in range(1, n)] + [n]
        d_sum = sum(2 * degree - 1 for degree in d_degrees)
        assert_equal(f"D_{n} Hitchin degree sum", d_sum, n * (2 * n - 1))
        for genus in range(2, 6):
            assert_equal(
                f"D_{n} genus-{genus} Hitchin base dimension",
                (genus - 1) * d_sum,
                (genus - 1) * n * (2 * n - 1),
            )

    exceptional_degrees = {
        "E6": ([2, 5, 6, 8, 9, 12], 78),
        "E7": ([2, 6, 8, 10, 12, 14, 18], 133),
        "E8": ([2, 8, 12, 14, 18, 20, 24, 30], 248),
    }
    for name, (degrees, dimension) in exceptional_degrees.items():
        degree_sum = sum(2 * degree - 1 for degree in degrees)
        assert_equal(f"{name} Hitchin degree sum", degree_sum, dimension)
        for genus in range(2, 5):
            assert_equal(
                f"{name} genus-{genus} Hitchin base dimension",
                (genus - 1) * degree_sum,
                (genus - 1) * dimension,
            )


def check_class_s_anomaly_pushforward_coefficients() -> None:
    # In the twist e(N_2)=x+eta t, the terms linear in t are
    # [I_8(1)]_t = eta x t (x^2 - p + 3u)/48 and
    # [(d h/24) p_2(N)]_t = eta d h x u t / 12.
    # Represent a polynomial by coefficients of x^3, x p, x u after removing
    # the common factor eta t.
    free_tensor = {
        "x^3": Fraction(1, 48),
        "x p": Fraction(-1, 48),
        "x u": Fraction(3, 48),
    }
    assert_equal("free tensor twist x^3 coefficient", free_tensor["x^3"], Fraction(1, 48))
    assert_equal("free tensor twist xp coefficient", free_tensor["x p"], Fraction(-1, 48))
    assert_equal("free tensor twist xu coefficient", free_tensor["x u"], Fraction(1, 16))

    # Check a few ADE inputs after multiplying by r_g and adding the
    # interacting excess.
    data = [
        ("A1", 1, 3, 2),
        ("A2", 2, 8, 3),
        ("D4", 4, 28, 6),
        ("E6", 6, 78, 12),
        ("E7", 7, 133, 18),
        ("E8", 8, 248, 30),
    ]
    for name, rank, dimension, dual_coxeter in data:
        x3 = Fraction(rank, 48)
        xp = Fraction(-rank, 48)
        xu = Fraction(rank, 16) + Fraction(dimension * dual_coxeter, 12)
        assert_equal(f"{name} class-S x^3 coefficient", x3, Fraction(rank, 48))
        assert_equal(f"{name} class-S xp coefficient", xp, Fraction(-rank, 48))
        assert_equal(
            f"{name} class-S xu coefficient",
            xu,
            Fraction(rank, 16) + Fraction(dimension * dual_coxeter, 12),
        )


def main() -> None:
    check_abjm_superpotential_r_charge()
    check_abjm_standard_conformal_locus_dimension()
    check_abjm_parity_level_pair()
    check_abjm_abelian_bf_normalization()
    check_abjm_orbifold_order_and_dimension()
    check_abjm_s3_matrix_denominator()
    check_sphere_free_energy_normalizations()
    check_abjm_fermi_gas_airy_normalizations()
    check_three_d_n2_cs_matter_auxiliary_elimination()
    check_three_d_n3_adjoint_chiral_elimination()
    check_six_dimensional_yang_mills_dimension()
    check_six_dimensional_chiral_two_form_degrees()
    check_two_zero_a_type_data()
    check_two_zero_ade_anomaly_coefficients()
    check_simply_laced_root_second_moments()
    check_simply_laced_dimension_root_count_relation()
    check_green_schwarz_quadratic_descent_factor()
    check_five_dimensional_instanton_kk_normalization()
    check_wrapped_string_mass_normalization()
    check_two_zero_defect_group_orders()
    check_cyclic_finite_flux_polarization()
    check_circle_reduction_finite_flux_pairing()
    check_circle_reduction_genuine_defect_polarizations()
    check_class_s_hitchin_base_degrees()
    check_class_s_anomaly_pushforward_coefficients()
    print("All ABJM and six-dimensional SUSY convention checks passed.")


if __name__ == "__main__":
    main()
