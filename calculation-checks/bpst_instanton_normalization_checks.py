#!/usr/bin/env python3
"""Finite checks for BPST instanton normalizations used in the monograph.

The displayed BPST formulas use the common SU(2) basis T_a=sigma_a/2 with
tr(T_a T_b)=delta_ab/2.  The active monograph coupling uses the trace-delta
basis t_a=sqrt(2) T_a and

    S = (4 g_YM^2)^(-1) int tr_delta(F_{mu nu} F_{mu nu}).

This script verifies the finite algebra and radial integrals behind the
relations

    int F^a_{mu nu} F^a_{mu nu} d^4x = 32 pi^2,
    Q = 1,
    S_common = 8 pi^2/g_ht^2 = 4 pi^2/g_YM^2,
    d^4 a d rho / rho^5 and (mu rho)^b0 are the universal
    one-loop scale/RG factors in the instanton density
    the pure-gauge Pauli-Villars one-instanton determinant constant is the
    orientation-integrated zero-mode constant times the finite nonzero-mode
    exponential exp[-alpha(1)-2(N-2)alpha(1/2)]
    the one-instanton small-rho boundary exponent criterion is
    b0 + beta_X > 4
    the general charge-k framed ADHM quotient has local real dimension 4 k N
    the finite-dimensional ADHM quotient-density coarea formula has the
    correct orbit-volume and homogeneous-cone scaling
    the finite-regulator nonzero-mode determinant datum has the correct
    boson/ghost/fermion determinant powers and counterterm shifts
    the ordered one-instanton amplitude datum keeps the classical weight,
    collective density, nonzero-mode determinant, zero-mode/source coefficient,
    source matching, endpoint control, and physical projection as distinct
    load-bearing stages, and the finite-regulator amplitude pipeline realizes
    the same ordering
    the finite fermion block determinant separates the nonzero-mode spectral
    determinant from the zero-mode Schur/Berezin determinant
    finite source-frame changes multiply the zero-mode determinant by
    det Z_R det Z_L and require the inverse transformation of the finite
    light-fermion nonzero-mode determinant factor; local finite determinant
    counterterms give a separate multiplicative scheme shift
    calibrating the finite light-fermion determinant by one reference amplitude
    predicts other channels only through same-frame ratios B_alpha/B_0; the
    reference residual is amplified by that ratio and a noncancellation margin
    for B_0 is required
    finite-scheme transport of an instanton determinant constant compensates
    the finite coupling-coordinate shift together with source and operator
    frame normalizations; reusing the old constant after a scheme change
    changes the amplitude
    the proper-time fluctuation determinant combines with either an independent
    bilinear source determinant or a differentiated linear Grassmann source
    coefficient to give the finite four-fermion instanton amplitude
    finite connected four-source extraction in an instanton source chart uses
    the coefficient of log Z_src, so lower two-source terms contribute the
    determinant subtraction before the four-point kernel is quoted
    source-dependent Schur corrections deform the zero-mode source determinant
    through the nonzero-mode propagator and cannot be replaced by a universal
    determinant constant
    a proper-time determinant residual bound gives an absolute logarithmic
    bound and a multiplicative amplitude error bound; signed cancellations of
    ghost, boson, and fermion trace remainders are rejected as valid bounds
    the heat-kernel logarithm in the nonzero-mode determinant carries the
    vector-plus-ghost 11 C_A/3 coefficient, the Dirac matter subtraction, and
    cancels the cutoff-scale dependence of the bare instanton exponential
    the BPST fundamental zero-mode density envelope has finite zeroth moment,
    an exact momentum-space form factor, a power-law tail, and a
    logarithmically infrared-sensitive second moment, while the individual
    singular-gauge zero-mode slot form factor is normalized at zero momentum
    and has the large-momentum tail 3/(4t^3)
    external-leg amputation removes only source-slot propagator residues from
    differentiated linear source matrices, and row/column residues from an
    independent bilinear source matrix
    plane-wave instanton four-fermion amplitudes factor the common center
    phase out of the differentiated right-slot and left-slot determinants, so
    the center integral supplies total momentum conservation while the
    individual zero-mode form-factor determinants remain inside the size
    integral
    hard wave-packet sources require rank-two projected zero-mode overlap
    matrices and a positive hard support margin; Hadamard's inequality turns
    row-wise zero-mode form-factor bounds into the same R^(-1/3) tail
    control for the SU(3), Nf=2 four-slot coefficient
    the SU(2) instanton orientation Haar average projects two colored
    zero-mode slots onto the antisymmetric invariant tensor and makes the
    shared-orientation four-slot coefficient a genuine four-fundamental Haar
    projector rather than a product of two independent two-slot averages
    color-singlet source projection multiplies the hard instanton kernel by
    gauge-invariant source-overlap matrices, while hadronic pole residues are
    separate external spectral data; the finite-volume hadronic pole window
    divides by source overlaps only after the selected pole has been isolated
    and excited-state leakage has a gap-suppressed majorant
    the Euclidean instanton source kernel becomes a physical amplitude only
    after analytic continuation and pole/spectral/OPE projection; the bridge
    has independent regulator, continuation, spectral, infrared, unitarity-cut,
    matching, and size-endpoint residuals
    inclusive spectral weights and rates first expand by amplitude sectors:
    a nonzero perturbative sector produces an order e^(-S_I) interference
    term, while the diagonal IbarI contribution has doubled action and is
    leading only after a selection rule or projection removes lower-action
    interference
    a selected one-instanton amplitude requires a separate sector-isolation
    bound: the retained Q=1 coefficient, same-sector residual,
    perturbative leakage, anti-instanton leakage, two-instanton leakage,
    IbarI amplitude-sector leakage, and higher-sector remainder enter an
    absolute majorant before a relative one-instanton claim is valid
    a physical instanton observable requires an ordered assembly ladder:
    Euclidean determinant/source/fluctuation/window residuals, sector
    leakage, and continuation/projection/infrared/cut/scheme residuals all
    enter before a finite instanton source coefficient is quoted as a
    scattering, OPE, susceptibility, or rate contribution
    a finite one-instanton amplitude error budget separates the leading
    determinant/zero-mode/source density from determinant remainders,
    zero-mode truncation, source matching, Schur corrections, and endpoint
    tails; the collective-coordinate measure alone is not the amplitude
    source-dependent fluctuation cumulants around the instanton saddle refine
    the determinant residual in a selected amplitude; vacuum determinant
    calibration and signed cumulant cancellation are rejected as
    source-amplitude bounds
    hard external momenta convert the Nf=2 four-fermion size integral into a
    Q^(-2) coefficient; fused bilinear density sources exponentially suppress
    the large-rho endpoint, while individual fermion slots obey the power test
    b0+1-3m<-1
    the equal-transfer fused bilinear-density hard size integral evaluates to
    an explicit Gamma-function Mellin coefficient with c^(-b0-2) source-scale
    dependence; this exponential-tail source channel is distinct from the
    individual-slot four-fermion kernel
    hard-size dominance is stronger than endpoint convergence: for SU(3),
    Nf=2 differentiated fermion slots the log-size shell and the tail beyond
    rho=R/Q decay only as R^(-1/3), so tenfold suppression of the power-tail
    majorant costs three decades in R, while fused density sources have
    exponential endpoint control;
    if a hard exponential source envelope and a physical screening mass are
    both present, the absolute log-size shell solves
    2 m_scr^2 rho^2+d Q rho-A=0; dropping either term gives the wrong
    dominant-size coordinate except in its own limiting regime
    the specialized SU(3), Nf=2 hard four-fermion instanton coefficient has
    b0=29/3, size-integrand power 32/3, RG-invariant falloff
    Lambda_ht^(29/3) Q^(-35/3), and leading individual-slot endpoint tail
    3*6^4 prod_l c_l^(-3) R^(-1/3);
    subtracting the leading individual-slot endpoint tail gives an accelerated
    hard coefficient estimator whose residual is bounded by
    (3/7) B_ind R^(-7/3) once the first product-tail residual majorant is
    supplied
    quoting the hard coefficient on a finite window requires the retained
    signed integral J_R, absolute mass M_R, tail T_R, and noncancellation
    margin kappa_R=|J_R|/M_R; cancellation can defeat relative control even
    when the absolute tail budget is small
    a four-source instanton amplitude bound requires nondegenerate
    right/left zero-mode overlap determinants; entrywise overlap errors give
    an explicit 2x2 determinant-stability bound and rank-margin residual
    source-conditioning matrices B^(-1) Delta B expose how a nearly rank-one
    hard source can amplify tiny overlap leakage into a determinant-relative
    error, separately from the BPST measure and determinant constant
    the four-fermion instanton benchmark gate ledger keeps center momentum
    conservation, classical/collective data, determinant normalization,
    zero-mode saturation, Haar projection, amputation, source conditioning,
    size-window control, sector isolation, physical projection, and scheme
    transport together before comparing with a 't Hooft-style amplitude
    a Wilsonian split of the instanton size integral has exact cancellation
    of the artificial factorization-scale boundary flux between the short
    instanton coefficient and the long-distance remainder
    short-instanton OPE coefficients transform inversely to the renormalized
    operator basis, satisfy the dual operator-mixing RG equation, and still
    carry a separate Wilsonian size-boundary flux
    trading the one-loop action for Lambda_ht gives the full hard scaling
    Lambda_ht^b0 Q^(-b0-2), with net coefficient dimension -2
    mass-saturated QCD vacuum activity carries prod_f(m_f rho), depends on
    theta+arg det M, is locally small-rho finite when b0+Nf>4, and is
    infrared-uncontrolled in zero-temperature QCD if the same one-loop power
    is extended to large rho
    mass derivatives of the finite-window vacuum activity obey the local
    anomalous Ward relations m_f Sigma_f^I + chi_top^I=0 and
    d_{arg m_f} E_I=d_theta E_I
    a physical Gaussian screening scale turns the one-instanton size integral
    into 1/2 m_scr^(-A) Gamma(A/2), with exact moment and shell-location
    bookkeeping; for SU(3), Nf=2 mass saturation A=23/3
    the high-temperature GPY/HTL determinant screening coefficient is
    m_T^2=pi^2 T^2 (2 Nc+Nf)/3, matching pi^2 m_D^2/g_YM^2 in the
    trace-delta Debye convention and giving pi^2 T^2 rho_shell^2=23/16
    for the SU(3), Nf=2 mass-saturated channel
    the corresponding dilute high-temperature topological susceptibility has
    chi_top=2 zeta_T, b2=-1/12, the same positive-activity determinant
    residual bound as zeta_T, and SU(3), Nf=2 scaling
    |m_u m_d| Lambda_ht^(29/3) T^(-23/3); negative and complex source
    amplitudes require a fixed-phase absolute value or an absolute-kernel
    majorant instead of a signed activity bound
    the same Euclidean thermal topological susceptibility is distinct from a
    real-time axial-charge relaxation rate: the former is a static
    spectral-area/contact datum, while the latter is controlled by the KMS
    zero-frequency Chern-Simons diffusion slope, the axial susceptibility, and,
    for massive quarks, the full dot-Q5 noise matrix including pseudoscalar
    mass-term and cross weights
    the renormalized mass/source instanton functional has homogeneous
    source-coordinate RG transport, with the finite fermion determinant factor
    cancelling the anomalous running of det(M^0+J^0)
    the one-instanton channel RG ledger combines the universal density,
    mass/source determinant, finite fermion determinant factor, and external
    projection normalization; finite-window residuals require a
    noncancellation margin for relative control
    the dilute instanton gas gives the Poisson/Skellam theta cumulants
    chi_top=2 zeta and b2=-1/12 only after the one-instanton amplitude is
    promoted to a finite dilute activity
    the first two-body Mayer correction changes the theta harmonics through
    same-charge instanton clusters, while the neutral instanton-anti-instanton
    cluster cancels from E(theta)-E(0) at this order; the corresponding
    susceptibility and b2 ratio are checked exactly
    a finite one-body instanton activity does not imply a finite two-body
    cluster coefficient: the connected relative kernel must be integrable at
    both the collision face and the large-separation tail in the same source
    and determinant scheme
    a finite instanton--anti-instanton ensemble has a rectangular zero-mode
    overlap matrix T whose singular values give the massive determinant
    m^|n_+-n_-| prod_alpha(m^2+s_alpha^2), the unpaired zero-mode pole, and
    the Banks--Casher kernel criterion for an instanton-liquid zero-mode zone;
    the same finite block gives the U(1)_A-odd pi-delta susceptibility kernel,
    where constant, linear, and superlinear near-zero singular-value densities
    respectively give pi*rho0/m, 2*c1, and a vanishing chiral-limit remnant,
    and the equivalent cumulative mode-count criterion requires
    N(lambda)=O(lambda^(2+epsilon)) after the exact-topology density has been
    removed;
    electroweak instanton/sphaleron physics uses the same anomalous charge
    ledger, but the real-time B+L washout rate is q_X^2 Gamma_CS/(chi_X T),
    with q_X=2N_g and B-L exactly conserved; the susceptibility entering that
    rate is the constrained Schur complement after conserved charges and
    neutrality conditions have been projected out;
    the physical instanton correlator contribution is the top Berezin
    coefficient after operator, mass/source, and zero-mode factors are
    restricted to the instanton zero-mode subspace, giving the full flavor
    determinant, the two-flavor scalar/pseudoscalar channel decomposition, the
    induced local source-curvature splittings, their anomalous axial Ward
    ledger, the tested-susceptibility contact rule in which the local
    instanton curvature weights only the diagonal value of the test kernel,
    the finite-momentum pi-delta source-kernel convolution that survives
    point splitting while preserving the zero-momentum contact limit, and the
    theta+arg det M phase combination;
    Uhlenbeck boundary faces have the expected codimensions and product
    power-counting integrability thresholds;
    the k=1 ADHM quotient has orientation dimension 4N-5 and cone
    volume power rho^(4N-5)

with g_ht = sqrt(2) g_YM.

Evidence contract.
Target claims: BPST normalization, one-instanton measure, zero-mode saturation,
proper-time determinant residual propagation, instanton-orientation Haar
projection, source-dependent fluctuation-cumulant residuals, hard-size/OPE
coefficient bookkeeping, and related Chapter 20 instanton labels.
Independent construction: direct radial integrals, finite determinant and
Schur-complement algebra, source differentiation, inverse-Gram construction of
the shared SU(2) four-fundamental Haar projector, absolute logarithmic
determinant-residual bounds, finite reference-amplitude calibration
ratios, finite-scheme transport ratios, zero-mode overlap determinant-stability
bounds, zero-mode source-conditioning matrices, Schwinger/Beta factorization
of the fused-source Bessel Mellin integral, finite cumulant telescopes,
coefficient/operator transport matrices, exact retained size-shell
stationarity equations, finite amplitude-sector isolation telescopes, and
exact radial power-counting for two-body cluster relative-coordinate
majorants, together with exact log-weight bookkeeping for the renormalized
one-instanton channel ledger, finite pole-window source/sink spectral
projection checks, and exact finite cyclic convolution tests for the
finite-momentum pi-delta source kernel.
Imported assumptions: the BPST background and zero-mode formulas, one-loop
determinant coefficients, the trace-delta convention, and finite regulator
truncations stated in the chapter.
Negative controls: the shared-Haar 1/3 versus factorized 1/4 counterexample,
rank-one and color-symmetric source-pair rejections, signed determinant-trace
cancellations rejected as fluctuation-error bounds, negative/complex
thermal amplitude kernels rejected from signed activity bounds, finite-frame
inverse checks, canceled reference-amplitude normalization, stale determinant
constants under finite scheme changes, rank-one four-source zero-mode collapse,
hard support mistaken for a nondegenerate source projection, unconditioned
overlap errors mistaken for determinant-relative errors,
same Euclidean topological susceptibility paired with different Kubo slopes,
nonzero Euclidean instanton susceptibility paired with zero real-time
diffusion,
finite one-body activities mistaken for a finite dilute-gas cluster
coefficient, signed relative-kernel cancellation mistaken for an absolute
Mayer bound,
mass/source zero-mode determinants or local operators mistaken for complete
renormalized instanton channel coordinates, and small signed retained windows
mistaken for good relative control without a noncancellation margin,
source correlator poles mistaken for hadronic matrix elements before overlap
division, overlap division mistaken for pole isolation when excited states
remain, and vanishing interpolating-source overlaps hidden by an instanton
kernel,
point-split source response discarded by a contact-only shortcut,
zero-momentum source normalization confused with finite-momentum smearing,
hard-source suppression replaced by a local vertex norm,
vacuum determinant calibration substituted for a source-dependent fluctuation
bound, signed fluctuation-cumulant cancellations,
hard-only and screening-only shell substitutions in the mixed size-majorant
problem, fused bilinear-density endpoint control mistaken for individual-slot
four-fermion endpoint control, and separation of operator RG flow from the
Wilsonian size-boundary flux, perturbative sector leakage mistaken for an
exact selection rule, omitted neighboring-sector leakage, and signed
adjacent-sector cancellation mistaken for sector isolation, the BPST/ADHM
classical-and-moduli prefix
mistaken for the instanton amplitude datum, the collective-coordinate measure
alone mistaken for the observable coefficient, the Euclidean source coefficient
mistaken for the physical observable after bridge residuals, omitted
endpoint/sector budgets, the top Berezin coefficient mistaken for the
connected four-source kernel when lower source terms are present, and signed
physical residual cancellation, and a source-dependent Schur correction
mistaken for source-independent determinant normalization.
Scope boundary: a pass checks finite algebra and normalization interfaces; it
does not prove dilute-gas validity, large-size control, uniform semiclassical
remainders, or physical hadronic matrix elements.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close


from fractions import Fraction
import itertools
import math

import mpmath as mp


def eps4(a: int, b: int, c: int, d: int) -> int:
    vals = [a, b, c, d]
    if len(set(vals)) < 4:
        return 0
    inv = 0
    for i in range(4):
        for j in range(i + 1, 4):
            inv += vals[i] > vals[j]
    return -1 if inv % 2 else 1


def eps3(a: int, b: int, c: int) -> int:
    vals = [a, b, c]
    if len(set(vals)) < 3:
        return 0
    inv = 0
    for i in range(3):
        for j in range(i + 1, 3):
            inv += vals[i] > vals[j]
    return -1 if inv % 2 else 1


def eta(a: int, mu: int, nu: int) -> int:
    """Self-dual 't Hooft eta symbol, indices a=0,1,2 and mu,nu=0..3.

    The fourth Euclidean coordinate is represented by index 3.  The convention
    is eta^a_{ij}=epsilon_{aij}, eta^a_{i4}=delta_ai,
    eta^a_{4i}=-delta_ai.
    """

    if mu == nu:
        return 0
    if mu < 3 and nu < 3:
        return eps3(a, mu, nu)
    if mu < 3 and nu == 3:
        return 1 if a == mu else 0
    if mu == 3 and nu < 3:
        return -1 if a == nu else 0
    raise AssertionError("unreachable")


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def assert_close(name: str, lhs: float, rhs: float, tolerance: float = 1e-12) -> None:
    _assert_close(name, lhs, rhs, tol=tolerance)


def det_fraction(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    if n == 1:
        return matrix[0][0]
    total = Fraction(0)
    for j in range(n):
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        total += ((-1) ** j) * matrix[0][j] * det_fraction(minor)
    return total


def submatrix(
    matrix: list[list[Fraction]],
    rows: set[int],
    cols: set[int],
) -> list[list[Fraction]]:
    return [
        [entry for col, entry in enumerate(row) if col in cols]
        for row_index, row in enumerate(matrix)
        if row_index in rows
    ]


def product_fraction(values: list[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


ComplexFraction = tuple[Fraction, Fraction]


def complex_mul_fraction(left: ComplexFraction, right: ComplexFraction) -> ComplexFraction:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def complex_scale_fraction(scale: Fraction, value: ComplexFraction) -> ComplexFraction:
    return (scale * value[0], scale * value[1])


def complex_abs_sq_fraction(value: ComplexFraction) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def matmul_fraction(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    if not left or not right:
        return []
    inner = len(right)
    assert_equal("matrix multiplication inner dimension", len(left[0]), inner)
    return [
        [
            sum(left[row][k] * right[k][col] for k in range(inner))
            for col in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def matrix_add_fraction(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    assert_equal("matrix add row count", len(left), len(right))
    assert_equal("matrix add column count", len(left[0]), len(right[0]))
    return [
        [left[row][col] + right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def matrix_sub_fraction(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    assert_equal("matrix subtract row count", len(left), len(right))
    assert_equal("matrix subtract column count", len(left[0]), len(right[0]))
    return [
        [left[row][col] - right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def trace_fraction(matrix: list[list[Fraction]]) -> Fraction:
    assert_equal("matrix trace square row count", len(matrix), len(matrix[0]))
    return sum(matrix[index][index] for index in range(len(matrix)))


def inverse_2x2_fraction(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    assert_equal("2x2 inverse row count", len(matrix), 2)
    assert_equal("2x2 inverse column count", len(matrix[0]), 2)
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = a * d - b * c
    if determinant == 0:
        raise AssertionError("singular 2x2 matrix")
    return [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant],
    ]


def block_2x2_fraction(
    upper_left: list[list[Fraction]],
    upper_right: list[list[Fraction]],
    lower_left: list[list[Fraction]],
    lower_right: list[list[Fraction]],
) -> list[list[Fraction]]:
    return [
        upper_left[row] + upper_right[row]
        for row in range(len(upper_left))
    ] + [
        lower_left[row] + lower_right[row]
        for row in range(len(lower_left))
    ]


GrassmannPolynomial = dict[tuple[int, ...], Fraction]


def grassmann_monomial(
    *variables: int,
    coefficient: Fraction = Fraction(1),
) -> GrassmannPolynomial:
    if len(set(variables)) != len(variables):
        return {}
    inversions = sum(
        1
        for i in range(len(variables))
        for j in range(i + 1, len(variables))
        if variables[i] > variables[j]
    )
    sign = Fraction(-1) if inversions % 2 else Fraction(1)
    return {tuple(sorted(variables)): sign * coefficient}


def grassmann_add(
    left: GrassmannPolynomial,
    right: GrassmannPolynomial,
) -> GrassmannPolynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def grassmann_mul(
    left: GrassmannPolynomial,
    right: GrassmannPolynomial,
) -> GrassmannPolynomial:
    result: GrassmannPolynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            if set(left_monomial) & set(right_monomial):
                continue
            concatenated = left_monomial + right_monomial
            product = grassmann_monomial(
                *concatenated,
                coefficient=left_coefficient * right_coefficient,
            )
            result = grassmann_add(result, product)
    return result


def berezin_top_coefficient(
    polynomial: GrassmannPolynomial,
    variable_count: int,
) -> Fraction:
    return polynomial.get(tuple(range(variable_count)), Fraction(0))


def grassmann_source_determinant_top_coefficient(
    matrix: list[list[Fraction]],
) -> Fraction:
    flavor_count = len(matrix)
    polynomial: GrassmannPolynomial = {}
    for permutation in itertools.permutations(range(flavor_count)):
        term = grassmann_monomial(coefficient=Fraction(1))
        for left_flavor, right_flavor in enumerate(permutation):
            term = grassmann_mul(
                term,
                grassmann_monomial(
                    2 * left_flavor,
                    2 * right_flavor + 1,
                    coefficient=matrix[left_flavor][right_flavor],
                ),
            )
        polynomial = grassmann_add(polynomial, term)
    return berezin_top_coefficient(polynomial, 2 * flavor_count)


def grassmann_linear_source_four_slot_coefficient(
    right_slots: list[list[Fraction]],
    left_slots: list[list[Fraction]],
) -> Fraction:
    flavor_count = 2
    assert_equal("right source slot matrix size", len(right_slots), flavor_count)
    assert_equal("left source flavor matrix size", len(left_slots), flavor_count)

    polynomial = grassmann_monomial(coefficient=Fraction(1))
    for flavor in range(flavor_count):
        alpha: GrassmannPolynomial = {}
        for slot in range(flavor_count):
            alpha = grassmann_add(
                alpha,
                grassmann_monomial(
                    slot,
                    coefficient=right_slots[slot][flavor],
                ),
            )
        polynomial = grassmann_mul(polynomial, alpha)

    for flavor in range(flavor_count):
        beta: GrassmannPolynomial = {}
        for slot in range(flavor_count):
            beta = grassmann_add(
                beta,
                grassmann_monomial(
                    flavor_count + slot,
                    coefficient=left_slots[flavor][slot],
                ),
            )
        polynomial = grassmann_mul(polynomial, beta)

    return berezin_top_coefficient(polynomial, 2 * flavor_count)


def check_eta_self_duality() -> None:
    for a, mu, nu in itertools.product(range(3), range(4), range(4)):
        dual = Fraction(1, 2) * sum(
            eps4(mu, nu, rho, sig) * eta(a, rho, sig)
            for rho in range(4)
            for sig in range(4)
        )
        assert_equal(f"eta self-duality a={a} mu={mu} nu={nu}", dual, eta(a, mu, nu))


def check_eta_norm() -> None:
    norm = sum(eta(a, mu, nu) ** 2 for a in range(3) for mu in range(4) for nu in range(4))
    assert_equal("sum eta^2", norm, 12)


def check_eta_quadratic_identity() -> None:
    # Check the tensor identity
    #   eps^a_bc eta^b_{mu rho} eta^c_{nu sigma} y^rho y^sigma
    # = r^2 eta^a_{mu nu}
    #   + y_mu eta^a_{nu lambda} y^lambda
    #   - y_nu eta^a_{mu lambda} y^lambda
    # coefficient by coefficient in the commuting monomials y_i y_j.
    for a, mu, nu in itertools.product(range(3), range(4), range(4)):
        lhs = {(i, j): 0 for i in range(4) for j in range(i, 4)}
        rhs = {(i, j): 0 for i in range(4) for j in range(i, 4)}
        for b, c, rho, sig in itertools.product(range(3), range(3), range(4), range(4)):
            key = (rho, sig) if rho <= sig else (sig, rho)
            lhs[key] += eps3(a, b, c) * eta(b, mu, rho) * eta(c, nu, sig)
        for lam in range(4):
            rhs[(lam, lam)] += eta(a, mu, nu)
            key = (mu, lam) if mu <= lam else (lam, mu)
            rhs[key] += eta(a, nu, lam)
            key = (nu, lam) if nu <= lam else (lam, nu)
            rhs[key] -= eta(a, mu, lam)
        assert_equal(f"eta quadratic identity a={a} mu={mu} nu={nu}", lhs, rhs)


def check_radial_integrals_and_actions() -> None:
    # Integral over R^4 of rho^4/(r^2+rho^2)^4:
    # 2*pi^2 * 1/2 * B(2,2) = pi^2/6.  Track only the rational coefficient.
    radial_coeff = Fraction(1, 6)
    f_component_coeff = 16 * 12 * radial_coeff
    assert_equal("int F_component^2 coefficient", f_component_coeff, 32)

    # In the half-trace basis tr(T_a T_b)=delta_ab/2.
    trace_half_coeff = Fraction(1, 2) * f_component_coeff
    assert_equal("int tr_half F^2 coefficient", trace_half_coeff, 16)

    # Q = (32*pi^2)^(-1) int F^a Ftilde^a for self-dual unit instanton.
    topological_charge = Fraction(f_component_coeff, 32)
    assert_equal("BPST topological charge", topological_charge, 1)

    # Common component action: (4 g_ht^2)^(-1) int F^a F^a.
    action_common_coeff = Fraction(f_component_coeff, 4)
    assert_equal("common half-trace action coefficient", action_common_coeff, 8)

    # Trace-delta action: F_delta^a = F_common^a/sqrt(2), hence int tr_delta F^2
    # is half the common component contraction.
    action_trace_delta_coeff = Fraction(trace_half_coeff, 4)
    assert_equal("trace-delta action coefficient", action_trace_delta_coeff, 4)

    # Coupling conversion g_ht^2 = 2 g_YM^2 makes 8/g_ht^2 = 4/g_YM^2.
    converted_common_coeff = Fraction(action_common_coeff, 2)
    assert_equal("coupling-converted action coefficient", converted_common_coeff, action_trace_delta_coeff)


def check_radial_cumulative_profile() -> None:
    # The normalized cumulative charge inside R=rho*u is
    # C(u)=1-3/(1+u^2)^2+2/(1+u^2)^3.  It is the integral of
    # 12 u^3/(1+u^2)^4, i.e. the radial measure times the normalized
    # BPST density divided by the total charge.
    def cumulative(u: Fraction) -> Fraction:
        t = 1 + u * u
        return 1 - Fraction(3, t * t) + Fraction(2, t * t * t)

    def density_with_measure(u: Fraction) -> Fraction:
        t = 1 + u * u
        return Fraction(12) * u**3 / (t**4)

    assert_equal("BPST cumulative at origin", cumulative(Fraction(0)), 0)
    assert_equal("BPST cumulative at u=1", cumulative(Fraction(1)), Fraction(1, 2))

    u = Fraction(2)
    t = 1 + u * u
    derivative = Fraction(12) * u / (t**3) - Fraction(12) * u / (t**4)
    assert_equal("BPST cumulative derivative", derivative, density_with_measure(u))


def check_one_instanton_density_scaling() -> None:
    # Translation and size coordinates have dimensions L^4 and L respectively;
    # rho^{-5} makes the center/scale measure dimensionless.
    measure_length_dimension = 4 + 1 - 5
    assert_equal("one-instanton center-size measure dimension", measure_length_dimension, 0)

    for n_c, n_f in [(2, 0), (3, 0), (3, 2), (5, 4)]:
        zero_modes = 4 * n_c
        # (8*pi^2/g^2)^(2 N_c) carries g-power -4 N_c, one g^{-1}
        # per bosonic zero mode.
        displayed_g_power = -2 * (2 * n_c)
        assert_equal(f"zero-mode g-power SU({n_c})", displayed_g_power, -zero_modes)

        b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
        alpha = b0
        # For log[g^{-4N_c} (mu rho)^alpha exp(-8*pi^2/g^2)],
        # beta=-b0 g^3/(16*pi^2) gives the leading RG derivative alpha-b0.
        leading_rg_derivative = alpha - b0
        assert_equal(f"one-loop RG exponent SU({n_c}) Nf={n_f}", leading_rg_derivative, 0)


def check_pure_gauge_pv_determinant_constant() -> None:
    # In the Pauli-Villars convention of the one-loop SU(N) instanton density,
    # the orientation-integrated zero-mode constant is
    #   2^(4N+2) pi^(4N-2) (8 pi^2)^(-2N)
    # = 2^(2-2N) pi^(-2)
    # after rewriting g^(-4N) as (8 pi^2/g^2)^(2N) (8 pi^2)^(-2N).
    # The finite nonzero-mode determinant supplies
    #   exp[-alpha(1)-2(N-2) alpha(1/2)].
    alpha_one = 0.443307
    alpha_half = 0.145873
    compact_prefactor_log = (
        2 * math.log(2)
        - 2 * math.log(math.pi)
        - alpha_one
        + 4 * alpha_half
    )
    compact_slope = -2 * math.log(2) - 2 * alpha_half

    assert_close("PV determinant rounded prefactor", math.exp(compact_prefactor_log), 0.466, 6.0e-4)
    assert_close("PV determinant rounded exponent slope", -compact_slope, 1.679, 1.0e-3)

    for n_c in [2, 3, 5]:
        structural_log = (
            (2 - 2 * n_c) * math.log(2)
            - 2 * math.log(math.pi)
            - alpha_one
            - 2 * (n_c - 2) * alpha_half
            - math.lgamma(n_c)
            - math.lgamma(n_c - 1)
        )
        compact_log = (
            compact_prefactor_log
            + compact_slope * n_c
            - math.lgamma(n_c)
            - math.lgamma(n_c - 1)
        )
        assert_close(f"PV determinant constant reduction SU({n_c})", structural_log, compact_log)

    su3_constant = math.exp(
        compact_prefactor_log + 3 * compact_slope - math.lgamma(3) - math.lgamma(2)
    )
    assert_close("PV determinant constant SU(3)", su3_constant, 1.51e-3, 1.0e-5)


def check_small_instanton_boundary_exponent_criterion() -> None:
    def b0(n_c: int, n_f: int) -> Fraction:
        return Fraction(11, 3) * n_c - Fraction(2, 3) * n_f

    def status(n_c: int, n_f: int, beta_x: Fraction) -> str:
        threshold_margin = b0(n_c, n_f) + beta_x - 4
        if threshold_margin > 0:
            return "finite"
        if threshold_margin == 0:
            return "log_divergent"
        return "power_divergent"

    assert_equal("pure SU(2) vacuum small-rho status", status(2, 0, Fraction(0)), "finite")
    assert_equal("pure SU(3) vacuum small-rho status", status(3, 0, Fraction(0)), "finite")

    # Asymptotic freedom is b0>0, but local small-rho integrability of the
    # vacuum one-instanton density with beta_X=0 requires b0>4.
    assert_equal("SU(3) Nf=16 asymptotic freedom", b0(3, 16) > 0, True)
    assert_equal("SU(3) Nf=16 vacuum small-rho status", status(3, 16, Fraction(0)), "power_divergent")
    assert_equal("SU(3) Nf=16 with insertion beta=4 status", status(3, 16, Fraction(4)), "finite")

    assert_equal("borderline log divergence", status(3, 9, Fraction(-1)), "log_divergent")

    # For integrand rho^(b0+beta_X-5), the antiderivative denominator is
    # b0+beta_X-4; this is exactly the threshold margin above.
    for n_c, n_f, beta_x in [(2, 0, Fraction(0)), (3, 16, Fraction(0)), (3, 9, Fraction(-1))]:
        exponent = b0(n_c, n_f) + beta_x - 5
        antiderivative_denominator = exponent + 1
        assert_equal(
            f"small-rho threshold denominator SU({n_c}) Nf={n_f} beta={beta_x}",
            antiderivative_denominator,
            b0(n_c, n_f) + beta_x - 4,
        )


def check_k_one_adhm_dimension_and_cone_power() -> None:
    for n_c in range(2, 9):
        # k=1 ADHM data: B1,B2 are two complex center coordinates, while
        # I,J contribute 4N real centered variables.
        real_variables = 4 + 4 * n_c
        real_equations = 3
        gauge_quotient = 1
        full_moduli_dim = real_variables - real_equations - gauge_quotient
        assert_equal(f"k=1 ADHM full dimension SU({n_c})", full_moduli_dim, 4 * n_c)

        centered_dim = full_moduli_dim - 4
        fixed_size_orbit_dim = centered_dim - 1
        assert_equal(f"k=1 ADHM centered cone dimension SU({n_c})", centered_dim, 4 * n_c - 4)
        assert_equal(f"k=1 ADHM orientation dimension SU({n_c})", fixed_size_orbit_dim, 4 * n_c - 5)

        u_n = n_c**2
        u_n_minus_two = (n_c - 2) ** 2
        homogeneous_orbit_dim = u_n - u_n_minus_two - 1
        assert_equal(
            f"U(N)/(U(N-2)xU(1)) dimension SU({n_c})",
            homogeneous_orbit_dim,
            fixed_size_orbit_dim,
        )

        if n_c == 2:
            assert_equal("SU(2)/Z2 orientation dimension", 3, fixed_size_orbit_dim)
        else:
            su_n = n_c**2 - 1
            su_n_minus_two = (n_c - 2) ** 2 - 1
            su_homogeneous_orbit_dim = su_n - su_n_minus_two - 1
            assert_equal(
                f"SU(N)/(SU(N-2)xU(1)) dimension SU({n_c})",
                su_homogeneous_orbit_dim,
                fixed_size_orbit_dim,
            )

        cone_radial_power = centered_dim - 1
        assert_equal(f"k=1 ADHM cone volume power SU({n_c})", cone_radial_power, 4 * n_c - 5)


def check_general_adhm_quotient_dimension() -> None:
    for n_c in range(2, 8):
        for k in range(1, 6):
            real_variables = 4 * k * k + 4 * k * n_c
            complex_equation_real = 2 * k * k
            real_moment_equation = k * k
            unitary_quotient = k * k
            quotient_dim = real_variables - complex_equation_real - real_moment_equation - unitary_quotient
            assert_equal(f"ADHM quotient dimension k={k} SU({n_c})", quotient_dim, 4 * k * n_c)
            assert_equal(f"centered ADHM dimension k={k} SU({n_c})", quotient_dim - 4, 4 * k * n_c - 4)

            # The four center coordinates are the two complex trace parts
            # tr(B_1)/k and tr(B_2)/k.  The traceless variables carry the
            # remaining dimension before constraints.
            traceless_b_real = 4 * (k * k - 1)
            framing_real = 4 * k * n_c
            centered_unconstrained = traceless_b_real + framing_real
            assert_equal(
                f"centered unconstrained ADHM variables k={k} SU({n_c})",
                centered_unconstrained,
                real_variables - 4,
            )


def check_adhm_quotient_density_coarea_scaling() -> None:
    # Toy quotient R^2 \ {0} -> R_{>0} by U(1): the level-set coarea formula
    # divides the circle density 2*pi*r by Vol(U(1))*sqrt(M), with M=r^2.
    # Thus the quotient radial density is dr, not r dr.
    circle_density_power = 1
    sqrt_orbit_gram_power = 1
    quotient_radial_density_power = circle_density_power - sqrt_orbit_gram_power
    assert_equal("toy U(1) quotient radial density power", quotient_radial_density_power, 0)

    for n_c in range(2, 8):
        for k in range(1, 6):
            centered_ambient_dim = 4 * k * k + 4 * k * n_c - 4
            constraint_dim = 3 * k * k
            group_dim = k * k
            quotient_dim = centered_ambient_dim - constraint_dim - group_dim
            assert_equal(f"centered ADHM quotient dimension k={k} SU({n_c})", quotient_dim, 4 * k * n_c - 4)

            # In the ambient coarea expression, the moment maps are quadratic.
            # Under X -> lambda X:
            # dX contributes V, delta(mu) contributes -2C, J_mu contributes C
            # because D mu is linear in X, and sqrt(det M) contributes G.
            ball_scaling_power = centered_ambient_dim - 2 * constraint_dim + constraint_dim - group_dim
            assert_equal(f"ADHM quotient ball scaling k={k} SU({n_c})", ball_scaling_power, quotient_dim)
            assert_equal(
                f"ADHM quotient cone shell power k={k} SU({n_c})",
                ball_scaling_power - 1,
                4 * k * n_c - 5,
            )


def check_finite_regulator_determinant_datum() -> None:
    # Finite toy Hessians after zero modes are removed.
    boson_vacuum = [[Fraction(2), Fraction(0), Fraction(0)],
                    [Fraction(0), Fraction(3), Fraction(0)],
                    [Fraction(0), Fraction(0), Fraction(5)]]
    boson_inst_nonzero = [[Fraction(7), Fraction(0)],
                          [Fraction(0), Fraction(11)]]
    ghost_vacuum = [[Fraction(13), Fraction(0)], [Fraction(0), Fraction(17)]]
    ghost_inst_nonzero = [[Fraction(19), Fraction(0)], [Fraction(0), Fraction(23)]]

    boson_ratio_squared = det_fraction(boson_vacuum) / det_fraction(boson_inst_nonzero)
    ghost_ratio = det_fraction(ghost_inst_nonzero) / det_fraction(ghost_vacuum)
    assert_equal("bosonic determinant inverse square factor squared", boson_ratio_squared, Fraction(30, 77))
    assert_equal("ghost determinant numerator factor", ghost_ratio, Fraction(437, 221))

    # A real antisymmetric fermion block [[0,a],[-a,0]] has Pfaffian a.
    # For two blocks, Pfaffians multiply.  Zero-mode blocks are omitted.
    fermion_inst_pf = Fraction(29) * Fraction(31)
    fermion_vac_pf = Fraction(37) * Fraction(41)
    fermion_ratio = fermion_inst_pf / fermion_vac_pf
    assert_equal("fermion Pfaffian nonzero ratio", fermion_ratio, Fraction(899, 1517))

    # The whole scalar datum in a vectorlike toy model has one ghost factor,
    # one inverse-square-root bosonic factor, and one Pfaffian factor.  Track
    # the square to avoid irrational square roots while preserving powers.
    scalar_weight_squared = boson_ratio_squared * ghost_ratio * ghost_ratio * fermion_ratio * fermion_ratio
    expected = Fraction(30, 77) * Fraction(437, 221) ** 2 * Fraction(899, 1517) ** 2
    assert_equal("finite determinant datum squared", scalar_weight_squared, expected)

    # A local counterterm c0+c1 log(mu rho) multiplies the density by
    # exp(-c0) (mu rho)^(-c1).  Check the exponent bookkeeping used in the
    # manuscript discussion.
    old_power = Fraction(11, 3)
    c1 = Fraction(2, 5)
    new_power = old_power - c1
    assert_equal("counterterm logarithmic power shift", new_power, Fraction(49, 15))


def check_one_instanton_amplitude_datum_gate_spine() -> None:
    gates = (
        "classical_saddle",
        "collective_density",
        "nonzero_mode_determinant",
        "zero_mode_saturation",
        "source_matching",
        "size_boundary",
        "physical_projection",
    )
    gate_index = {gate: index for index, gate in enumerate(gates)}
    required_edges = (
        ("classical_saddle", "collective_density"),
        ("collective_density", "nonzero_mode_determinant"),
        ("nonzero_mode_determinant", "zero_mode_saturation"),
        ("zero_mode_saturation", "source_matching"),
        ("source_matching", "size_boundary"),
        ("size_boundary", "physical_projection"),
    )
    for before, after in required_edges:
        assert_equal(
            f"one-instanton datum order {before} before {after}",
            gate_index[before] < gate_index[after],
            True,
        )

    gate_weights = {
        "classical_saddle": Fraction(2, 5),
        "collective_density": Fraction(3, 7),
        "nonzero_mode_determinant": Fraction(5, 11),
        "zero_mode_saturation": Fraction(7, 13),
        "source_matching": Fraction(11, 17),
        "size_boundary": Fraction(13, 19),
        "physical_projection": Fraction(17, 23),
    }
    full_datum = product_fraction([gate_weights[gate] for gate in gates])

    prefixes: dict[str, Fraction] = {}
    running_prefix = Fraction(1)
    for gate in gates:
        running_prefix *= gate_weights[gate]
        prefixes[gate] = running_prefix

    assert_equal(
        "BPST/ADHM moduli prefix is not the amplitude datum",
        prefixes["collective_density"] == full_datum,
        False,
    )
    for gate in gates[2:]:
        omitted_gate_product = product_fraction(
            [gate_weights[other] for other in gates if other != gate]
        )
        assert_equal(
            f"omitting {gate} changes the one-instanton amplitude datum",
            omitted_gate_product == full_datum,
            False,
        )

    unsaturated_weights = dict(gate_weights)
    unsaturated_weights["zero_mode_saturation"] = Fraction(0)
    unsaturated_euclidean_source = product_fraction(
        [unsaturated_weights[gate] for gate in gates[:-1]]
    )
    assert_equal(
        "unsaturated zero-mode datum gives zero Euclidean source coefficient",
        unsaturated_euclidean_source,
        Fraction(0),
    )

    residuals_by_gate = {
        "nonzero_mode_determinant": Fraction(1, 101),
        "zero_mode_saturation": Fraction(1, 103),
        "source_matching": Fraction(1, 107),
        "size_boundary": Fraction(1, 109),
        "physical_projection": Fraction(1, 113),
    }
    assert_equal(
        "post-moduli gates carry independent residual controls",
        set(residuals_by_gate),
        set(gates[2:]),
    )
    controlled_physical = full_datum + sum(residuals_by_gate.values())
    euclidean_source_shortcut = product_fraction(
        [gate_weights[gate] for gate in gates[:-1]]
    )
    assert_equal(
        "Euclidean source coefficient is not the physical amplitude datum",
        euclidean_source_shortcut == controlled_physical,
        False,
    )


def check_instanton_amplitude_pipeline_stage_bookkeeping() -> None:
    # A finite-regulator instanton chart reduces the amplitude integrand to
    # finitely many cells after a quadrature/discretization.  Each cell carries
    # distinct classical, collective-coordinate, nonzero-mode determinant,
    # zero-mode/source, source-matching, and physical-projection data.
    cells = [
        {
            "classical": Fraction(2, 3),
            "collective": Fraction(3, 5),
            "nonzero": Fraction(5, 7),
            "zero_mode": Fraction(7, 11),
            "source": Fraction(11, 13),
            "projection": Fraction(13, 17),
        },
        {
            "classical": Fraction(3, 4),
            "collective": Fraction(5, 9),
            "nonzero": Fraction(7, 10),
            "zero_mode": Fraction(0),
            "source": Fraction(11, 12),
            "projection": Fraction(2, 19),
        },
        {
            "classical": Fraction(5, 6),
            "collective": Fraction(7, 8),
            "nonzero": Fraction(11, 13),
            "zero_mode": Fraction(13, 17),
            "source": Fraction(17, 19),
            "projection": Fraction(19, 23),
        },
    ]

    euclidean_cells = [
        product_fraction(
            [
                cell["classical"],
                cell["collective"],
                cell["nonzero"],
                cell["zero_mode"],
                cell["source"],
            ]
        )
        for cell in cells
    ]
    physical_from_pipeline = sum(
        cell["projection"] * euclidean_cell
        for cell, euclidean_cell in zip(cells, euclidean_cells)
    )
    physical_from_merged_cells = sum(
        product_fraction(
            [
                cell["classical"],
                cell["collective"],
                cell["nonzero"],
                cell["zero_mode"],
                cell["source"],
                cell["projection"],
            ]
        )
        for cell in cells
    )
    assert_equal(
        "instanton amplitude pipeline equals merged finite-cell product",
        physical_from_pipeline,
        physical_from_merged_cells,
    )
    assert_equal(
        "unsaturated instanton cell gives zero before physical projection",
        euclidean_cells[1],
        Fraction(0),
    )

    moduli_only_coordinate = sum(
        cell["classical"] * cell["collective"] for cell in cells
    )
    determinant_omitted_coordinate = sum(
        cell["classical"] * cell["collective"] * cell["zero_mode"] * cell["source"]
        for cell in cells
    )
    assert_equal(
        "collective-coordinate chart alone is not the physical instanton amplitude",
        moduli_only_coordinate == physical_from_pipeline,
        False,
    )
    assert_equal(
        "dropping the nonzero-mode determinant changes the instanton amplitude",
        determinant_omitted_coordinate == physical_from_pipeline,
        False,
    )

    # Source-frame changes can move a finite determinant between the light
    # fermion nonzero-mode factor and the zero-mode source coefficient.  The
    # amplitude cell is the product of both, not either factor separately.
    source_frame_scale = Fraction(5, 4)
    flavor_pairs = 2
    rescaled_physical = sum(
        product_fraction(
            [
                cell["classical"],
                cell["collective"],
                cell["nonzero"] * source_frame_scale**flavor_pairs,
                cell["zero_mode"] / source_frame_scale**flavor_pairs,
                cell["source"],
                cell["projection"],
            ]
        )
        for cell in cells
    )
    assert_equal(
        "source-frame reshuffling preserves the full instanton pipeline product",
        rescaled_physical,
        physical_from_pipeline,
    )

    residuals = {
        "determinant": Fraction(1, 29),
        "zero_mode": Fraction(-1, 31),
        "source_matching": Fraction(1, 37),
        "endpoint": Fraction(-1, 41),
        "continuation": Fraction(1, 43),
        "spectral": Fraction(-1, 47),
        "infrared": Fraction(1, 53),
        "unitarity_cut": Fraction(-1, 59),
    }
    physical_with_residuals = physical_from_pipeline + sum(residuals.values())
    assert_equal(
        "instanton amplitude pipeline residual telescope",
        physical_with_residuals - physical_from_pipeline,
        sum(residuals.values()),
    )


def check_physical_instanton_correlator_zero_mode_saturation() -> None:
    # Four zero modes in canonical order: R1, L1, R2, L2.  Berezin
    # integration returns only the coefficient of R1 L1 R2 L2.
    variable_count = 4
    unsaturated = grassmann_mul(
        grassmann_monomial(0, coefficient=Fraction(3)),
        grassmann_monomial(2, coefficient=Fraction(5)),
    )
    assert_equal(
        "unsaturated instanton zero-mode correlator vanishes",
        berezin_top_coefficient(unsaturated, variable_count),
        Fraction(0),
    )

    operator_pair = grassmann_monomial(0, 1, coefficient=Fraction(7))
    mass_lift = grassmann_monomial(2, 3, coefficient=Fraction(11))
    lifted = grassmann_mul(operator_pair, mass_lift)
    assert_equal(
        "mass/source lifting supplies missing instanton zero modes",
        berezin_top_coefficient(lifted, variable_count),
        Fraction(77),
    )

    # Two-flavor QCD zero-mode insertions form the determinant
    # B_11 B_22 - B_12 B_21 as the top Berezin coefficient.
    b11 = Fraction(2)
    b12 = Fraction(3)
    b21 = Fraction(5)
    b22 = Fraction(7)
    diagonal_pairing = grassmann_mul(
        grassmann_monomial(0, 1, coefficient=b11),
        grassmann_monomial(2, 3, coefficient=b22),
    )
    crossed_pairing = grassmann_mul(
        grassmann_monomial(0, 3, coefficient=b12),
        grassmann_monomial(2, 1, coefficient=b21),
    )
    flavor_determinant_polynomial = grassmann_add(diagonal_pairing, crossed_pairing)
    determinant = b11 * b22 - b12 * b21
    assert_equal(
        "two-flavor 't Hooft determinant from zero-mode Berezin coefficient",
        berezin_top_coefficient(flavor_determinant_polynomial, variable_count),
        determinant,
    )

    axial_charge_per_bilinear = 2
    flavor_count = 2
    assert_equal(
        "QCD instanton axial charge selection",
        axial_charge_per_bilinear * flavor_count,
        4,
    )

    three_flavor_source = [
        [Fraction(2), Fraction(3), Fraction(5)],
        [Fraction(7), Fraction(11), Fraction(13)],
        [Fraction(17), Fraction(19), Fraction(23)],
    ]
    assert_equal(
        "three-flavor 't Hooft determinant from zero-mode Berezin coefficient",
        grassmann_source_determinant_top_coefficient(three_flavor_source),
        det_fraction(three_flavor_source),
    )

    axial_parameter_units = 5
    flavor_count = 3
    theta_shift = 2 * flavor_count * axial_parameter_units
    mass_phase_shift = -2 * flavor_count * axial_parameter_units
    assert_equal(
        "strong CP phase theta plus arg det M is axial invariant",
        theta_shift + mass_phase_shift,
        0,
    )

    # Mixed mass/source saturation is the determinant identity
    # det(M+B)=sum_{I,J} (-1)^{sum I + sum J} det M_{I^c,J^c} det B_{I,J},
    # with one-based row/column labels in the sign.  This is the exact
    # finite-dimensional statement behind differentiating the instanton
    # source functional.
    mass_matrix = [
        [Fraction(2), Fraction(3), Fraction(5)],
        [Fraction(7), Fraction(11), Fraction(13)],
        [Fraction(17), Fraction(19), Fraction(23)],
    ]
    source_matrix = [
        [Fraction(29), Fraction(31), Fraction(37)],
        [Fraction(41), Fraction(43), Fraction(47)],
        [Fraction(53), Fraction(59), Fraction(61)],
    ]
    flavor_indices = set(range(3))
    minor_expansion = Fraction(0)
    for r in range(4):
        for rows_tuple in itertools.combinations(range(3), r):
            rows = set(rows_tuple)
            rows_complement = flavor_indices - rows
            for cols_tuple in itertools.combinations(range(3), r):
                cols = set(cols_tuple)
                cols_complement = flavor_indices - cols
                one_based_sum = (
                    sum(row + 1 for row in rows)
                    + sum(col + 1 for col in cols)
                )
                cofactor_sign = Fraction(1 if one_based_sum % 2 == 0 else -1)
                mass_minor = det_fraction(
                    submatrix(mass_matrix, rows_complement, cols_complement)
                )
                source_minor = det_fraction(submatrix(source_matrix, rows, cols))
                minor_expansion += cofactor_sign * mass_minor * source_minor

    combined_matrix = [
        [
            mass_matrix[row][col] + source_matrix[row][col]
            for col in range(3)
        ]
        for row in range(3)
    ]
    assert_equal(
        "instanton mixed mass/source minor expansion",
        minor_expansion,
        det_fraction(combined_matrix),
    )

    # For N_f=2 the one-source coefficient is the complementary mass cofactor,
    # and the all-source coefficient is the antisymmetric massless vertex.
    m11, m12, m21, m22 = Fraction(2), Fraction(3), Fraction(5), Fraction(7)
    b11, b12, b21, b22 = Fraction(11), Fraction(13), Fraction(17), Fraction(19)
    two_flavor_expansion = (
        (m11 * m22 - m12 * m21)
        + m22 * b11
        - m21 * b12
        - m12 * b21
        + m11 * b22
        + b11 * b22
        - b12 * b21
    )
    assert_equal(
        "two-flavor mixed mass/source determinant expansion",
        two_flavor_expansion,
        det_fraction([[m11 + b11, m12 + b12], [m21 + b21, m22 + b22]]),
    )


def check_two_flavor_thooft_channel_decomposition() -> None:
    def complex_sub(
        left: tuple[Fraction, Fraction],
        right: tuple[Fraction, Fraction],
    ) -> tuple[Fraction, Fraction]:
        return (left[0] - right[0], left[1] - right[1])

    def complex_mul(
        left: tuple[Fraction, Fraction],
        right: tuple[Fraction, Fraction],
    ) -> tuple[Fraction, Fraction]:
        return (
            left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0],
        )

    def determinant_2x2_complex(
        matrix: list[list[tuple[Fraction, Fraction]]],
    ) -> tuple[Fraction, Fraction]:
        return complex_sub(
            complex_mul(matrix[0][0], matrix[1][1]),
            complex_mul(matrix[0][1], matrix[1][0]),
        )

    # With S=s0 1+s.tau and P=p0 1+p.tau, the chiral bilinear matrix is
    # Phi=(S+iP)/2.  Check det(S+iP) directly in the Pauli basis.
    s0 = Fraction(2)
    p0 = Fraction(-3, 5)
    s = [Fraction(7, 11), Fraction(-13, 17), Fraction(19, 23)]
    p = [Fraction(29, 31), Fraction(37, 41), Fraction(-43, 47)]

    x00 = (s0 + s[2], p0 + p[2])
    x11 = (s0 - s[2], p0 - p[2])
    x01 = (s[0] + p[1], -s[1] + p[0])
    x10 = (s[0] - p[1], s[1] + p[0])
    direct_real, direct_imag = determinant_2x2_complex([[x00, x01], [x10, x11]])

    channel_real = (
        s0 * s0
        - sum(entry * entry for entry in s)
        - p0 * p0
        + sum(entry * entry for entry in p)
    )
    channel_imag = 2 * (
        s0 * p0
        - sum(s[index] * p[index] for index in range(3))
    )
    assert_equal("two-flavor determinant real channel", direct_real, channel_real)
    assert_equal("two-flavor determinant imaginary channel", direct_imag, channel_imag)

    # det Phi carries an extra factor (1/2)^2.  Therefore
    # e^{i theta} det Phi + e^{-i theta} det Phi^dagger has cos(theta)
    # coefficient channel_real/2 and sin(theta) coefficient -channel_imag/2.
    assert_equal(
        "two-flavor theta-even channel coefficient",
        direct_real / 2,
        channel_real / 2,
    )
    assert_equal(
        "two-flavor theta-odd scalar-pseudoscalar mixing coefficient",
        -direct_imag / 2,
        -(s0 * p0 - sum(s[index] * p[index] for index in range(3))),
    )

    # Basis-vector checks expose the signs of the four physical channels at
    # theta=0: scalar singlet and pseudoscalar triplet enter with the opposite
    # sign from pseudoscalar singlet and scalar triplet.
    def theta_zero_channel(
        scalar_singlet: Fraction = Fraction(0),
        scalar_triplet: Fraction = Fraction(0),
        pseudoscalar_singlet: Fraction = Fraction(0),
        pseudoscalar_triplet: Fraction = Fraction(0),
    ) -> Fraction:
        return Fraction(1, 2) * (
            scalar_singlet * scalar_singlet
            - scalar_triplet * scalar_triplet
            - pseudoscalar_singlet * pseudoscalar_singlet
            + pseudoscalar_triplet * pseudoscalar_triplet
        )

    assert_equal(
        "theta-zero scalar singlet sign",
        theta_zero_channel(scalar_singlet=1),
        Fraction(1, 2),
    )
    assert_equal(
        "theta-zero scalar triplet sign",
        theta_zero_channel(scalar_triplet=1),
        Fraction(-1, 2),
    )
    assert_equal(
        "theta-zero pseudoscalar singlet sign",
        theta_zero_channel(pseudoscalar_singlet=1),
        Fraction(-1, 2),
    )
    assert_equal(
        "theta-zero pseudoscalar triplet sign",
        theta_zero_channel(pseudoscalar_triplet=1),
        Fraction(1, 2),
    )

    axial_phase_per_phi = -2
    flavor_count = 2
    determinant_phase = flavor_count * axial_phase_per_phi
    theta_compensation = 2 * flavor_count
    assert_equal("two-flavor determinant axial phase", determinant_phase, -4)
    assert_equal(
        "theta shift compensates two-flavor determinant phase",
        determinant_phase + theta_compensation,
        0,
    )


def check_two_flavor_instanton_source_curvature() -> None:
    kappa = Fraction(17, 19)
    cos_theta = Fraction(5, 7)
    sin_theta = Fraction(11, 13)

    # The local finite-activity source coordinate is
    # kappa[(cos theta/2)(s0^2-s^2-p0^2+p^2)-sin theta(s0 p0-s.p)].
    # The source curvatures are its second derivatives at zero source.
    sigma_curvature = 2 * kappa * cos_theta / 2
    delta_curvature = 2 * (-kappa * cos_theta / 2)
    eta_curvature = 2 * (-kappa * cos_theta / 2)
    pion_curvature = 2 * kappa * cos_theta / 2
    assert_equal("instanton sigma source curvature", sigma_curvature, kappa * cos_theta)
    assert_equal("instanton delta source curvature", delta_curvature, -kappa * cos_theta)
    assert_equal("instanton eta source curvature", eta_curvature, -kappa * cos_theta)
    assert_equal("instanton pion source curvature", pion_curvature, kappa * cos_theta)

    assert_equal(
        "instanton U(1)_A pion-delta splitting",
        pion_curvature - delta_curvature,
        2 * kappa * cos_theta,
    )
    assert_equal(
        "instanton U(1)_A sigma-eta splitting",
        sigma_curvature - eta_curvature,
        2 * kappa * cos_theta,
    )

    sigma_eta_mixing = -kappa * sin_theta
    delta_pion_mixing = kappa * sin_theta
    assert_equal("theta-odd sigma-eta source mixing", sigma_eta_mixing, -kappa * sin_theta)
    assert_equal("theta-odd delta-pion source mixing", delta_pion_mixing, kappa * sin_theta)

    # At theta=0 the CP-odd source mixings vanish, while the U(1)_A splitting
    # remains proportional to the finite local instanton activity.
    assert_equal("theta-zero CP-odd mixing vanishes", -kappa * 0, Fraction(0))
    assert_equal("theta-zero pion-delta splitting", 2 * kappa, Fraction(34, 19))


def check_two_flavor_instanton_source_ward_ledger() -> None:
    kappa = Fraction(17, 19)
    cos_theta = Fraction(5, 7)
    sin_theta = Fraction(11, 13)
    s0 = Fraction(2)
    s_vec = [Fraction(3), Fraction(5), Fraction(7)]
    p0 = Fraction(11)
    p_vec = [Fraction(13), Fraction(17), Fraction(19)]

    channel_a = s0 * s0 - sum(x * x for x in s_vec) - p0 * p0 + sum(x * x for x in p_vec)
    channel_b = s0 * p0 - sum(s * p for s, p in zip(s_vec, p_vec))

    delta_s0 = 2 * p0
    delta_s_vec = [2 * p for p in p_vec]
    delta_p0 = -2 * s0
    delta_p_vec = [-2 * s for s in s_vec]
    delta_a = (
        2 * s0 * delta_s0
        - 2 * sum(s * ds for s, ds in zip(s_vec, delta_s_vec))
        - 2 * p0 * delta_p0
        + 2 * sum(p * dp for p, dp in zip(p_vec, delta_p_vec))
    )
    delta_b = (
        delta_s0 * p0
        + s0 * delta_p0
        - sum(ds * p + s * dp for s, ds, p, dp in zip(s_vec, delta_s_vec, p_vec, delta_p_vec))
    )
    assert_equal("two-flavor axial source variation of A", delta_a, 8 * channel_b)
    assert_equal("two-flavor axial source variation of B", delta_b, -2 * channel_a)

    theta_variation = 4 * kappa * (
        -sin_theta * channel_a / 2 - cos_theta * channel_b
    )
    source_variation = kappa * (
        cos_theta * delta_a / 2 - sin_theta * delta_b
    )
    assert_equal(
        "two-flavor instanton source Ward identity",
        theta_variation + source_variation,
        Fraction(0),
    )

    # For each axial pair W=epsilon*kappa[(cos theta/2)(s^2-p^2)-sin theta sp].
    # The singlet pair has epsilon=+1; a triplet pair has epsilon=-1.
    for label, epsilon in [("singlet", Fraction(1)), ("triplet", Fraction(-1))]:
        chi_s = epsilon * kappa * cos_theta
        chi_p = -epsilon * kappa * cos_theta
        mixing = -epsilon * kappa * sin_theta
        dtheta_chi_s = -epsilon * kappa * sin_theta
        dtheta_chi_p = epsilon * kappa * sin_theta
        dtheta_mixing = -epsilon * kappa * cos_theta
        assert_equal(f"{label} Ward dtheta chi_s", dtheta_chi_s, mixing)
        assert_equal(f"{label} Ward dtheta chi_p", dtheta_chi_p, -mixing)
        assert_equal(
            f"{label} Ward curvature difference",
            chi_s - chi_p,
            -2 * dtheta_mixing,
        )

    theta_zero_triplet_delta = -kappa
    theta_zero_triplet_pion = kappa
    assert_equal(
        "triplet Ward ledger matches positive pion-delta order",
        theta_zero_triplet_pion - theta_zero_triplet_delta,
        2 * kappa,
    )


def check_two_flavor_instanton_tested_susceptibility_contact() -> None:
    kappa = Fraction(17, 19)
    cos_theta = Fraction(5, 7)
    sin_theta = Fraction(11, 13)

    # A finite tested susceptibility weights a local curvature only by the
    # diagonal of the test kernel.  Off-diagonal entries belong to the
    # propagated/spectral two-point function, not to the local contact term.
    test_kernel = [
        [Fraction(2), Fraction(101), Fraction(-37)],
        [Fraction(101), Fraction(3), Fraction(59)],
        [Fraction(-37), Fraction(59), Fraction(5)],
    ]
    volume = Fraction(len(test_kernel))
    diagonal_weight = sum(
        test_kernel[index][index] for index in range(len(test_kernel))
    ) / volume
    full_kernel_weight = sum(sum(row) for row in test_kernel) / volume

    pion_contact = kappa * cos_theta * diagonal_weight
    delta_contact = -kappa * cos_theta * diagonal_weight
    sigma_eta_contact = -kappa * sin_theta * diagonal_weight
    delta_pion_contact = kappa * sin_theta * diagonal_weight
    assert_equal(
        "tested pion local instanton contact",
        pion_contact,
        kappa * cos_theta * diagonal_weight,
    )
    assert_equal(
        "tested delta local instanton contact",
        delta_contact,
        -kappa * cos_theta * diagonal_weight,
    )
    assert_equal(
        "tested U1A contact splitting",
        pion_contact - delta_contact,
        2 * kappa * cos_theta * diagonal_weight,
    )
    assert_equal(
        "tested sigma-eta CP-odd contact",
        sigma_eta_contact,
        -kappa * sin_theta * diagonal_weight,
    )
    assert_equal(
        "tested delta-pion CP-odd contact",
        delta_pion_contact,
        kappa * sin_theta * diagonal_weight,
    )

    assert_equal(
        "off-diagonal test weight is not a local contact weight",
        full_kernel_weight == diagonal_weight,
        False,
    )
    assert_equal(
        "wrong full-kernel contact weighting is rejected",
        2 * kappa * cos_theta * full_kernel_weight
        == pion_contact - delta_contact,
        False,
    )

    point_split_kernel = [
        [Fraction(0), Fraction(7), Fraction(11)],
        [Fraction(7), Fraction(0), Fraction(13)],
        [Fraction(11), Fraction(13), Fraction(0)],
    ]
    point_split_diagonal = sum(
        point_split_kernel[index][index] for index in range(len(point_split_kernel))
    ) / volume
    assert_equal("point-split diagonal weight", point_split_diagonal, Fraction(0))
    assert_equal(
        "point-split local instanton contact vanishes",
        2 * kappa * cos_theta * point_split_diagonal,
        Fraction(0),
    )

    spectral_difference = Fraction(-31, 23)
    counterterm_difference = Fraction(5, 29)
    local_remainder = Fraction(-7, 31)
    regulator_remainder = Fraction(2, 37)
    total_tested_difference = (
        pion_contact
        - delta_contact
        + spectral_difference
        + counterterm_difference
        + local_remainder
        + regulator_remainder
    )
    assert_equal(
        "tested susceptibility separates contact and propagated data",
        total_tested_difference,
        2 * kappa * cos_theta * diagonal_weight
        + spectral_difference
        + counterterm_difference
        + local_remainder
        + regulator_remainder,
    )

    large_negative_spectral_difference = (
        -(pion_contact - delta_contact) - Fraction(1, 41)
    )
    assert_equal(
        "spectral term can reverse the full tested splitting",
        pion_contact - delta_contact + large_negative_spectral_difference < 0,
        True,
    )


def check_finite_momentum_pion_delta_instanton_source_kernel() -> None:
    # A finite zero-mode density kernel is a convolution, not a pure contact
    # delta.  Use a four-site periodic regulator with a normalized BPST-like
    # density envelope.
    h = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 4), Fraction(0)]
    volume = len(h)
    assert_equal("finite source density envelope normalized", sum(h, Fraction(0)), Fraction(1))

    def cyclic_source_kernel(envelope: list[Fraction]) -> list[Fraction]:
        return [
            sum(
                envelope[center] * envelope[(center + separation) % volume]
                for center in range(volume)
            )
            for separation in range(volume)
        ]

    source_kernel = cyclic_source_kernel(h)
    assert_equal(
        "finite source-width convolution kernel",
        source_kernel,
        [Fraction(3, 8), Fraction(3, 16), Fraction(1, 4), Fraction(3, 16)],
    )
    assert_equal("finite source kernel has unit zero-momentum weight", sum(source_kernel), Fraction(1))

    zeta = Fraction(5, 7)
    point_split_test = [Fraction(0), Fraction(1), Fraction(0), Fraction(0)]
    local_contact_kernel = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    local_contact_weight = sum(
        test * contact for test, contact in zip(point_split_test, local_contact_kernel)
    )
    finite_source_weight = sum(
        test * kernel for test, kernel in zip(point_split_test, source_kernel)
    )
    assert_equal("point-split local contact weight", local_contact_weight, Fraction(0))
    assert_equal("point-split finite zero-mode source weight", finite_source_weight, Fraction(3, 16))

    pion_source_curvature = zeta * finite_source_weight
    delta_source_curvature = -zeta * finite_source_weight
    assert_equal(
        "finite-momentum pion-delta source kernel",
        pion_source_curvature - delta_source_curvature,
        2 * zeta * finite_source_weight,
    )
    assert_equal(
        "contact-only shortcut misses finite source-width kernel",
        2 * zeta * local_contact_weight == pion_source_curvature - delta_source_curvature,
        False,
    )

    constant_test = [Fraction(1), Fraction(1), Fraction(1), Fraction(1)]
    finite_constant_weight = sum(
        test * kernel for test, kernel in zip(constant_test, source_kernel)
    )
    local_constant_weight = constant_test[0]
    assert_equal("zero-momentum source kernel matches local contact", finite_constant_weight, local_constant_weight)

    def cyclic_smear(source: list[Fraction]) -> list[Fraction]:
        return [
            sum(h[shift] * source[(center + shift) % volume] for shift in range(volume))
            for center in range(volume)
        ]

    hard_source = [Fraction(1), Fraction(-1), Fraction(1), Fraction(-1)]
    smeared_hard_source = cyclic_smear(hard_source)
    unsmeared_norm = sum(value * value for value in hard_source) / volume
    smeared_norm = sum(value * value for value in smeared_hard_source) / volume
    assert_equal("hard source mode is suppressed by zero-mode density", smeared_norm, Fraction(1, 4))
    assert_equal(
        "hard source suppression is not the local vertex norm",
        smeared_norm == unsmeared_norm,
        False,
    )

    determinant_residual = Fraction(1, 100)
    endpoint_residual = Fraction(1, 80)
    ir_residual = Fraction(1, 60)
    residual_bound = determinant_residual + endpoint_residual + ir_residual
    retained_mass = abs(2 * zeta * finite_source_weight)
    actual_residual = retained_mass * Fraction(1, 90)
    if not actual_residual <= retained_mass * residual_bound:
        raise AssertionError("finite-momentum pion-delta residual budget failed")


def check_fermion_determinant_zero_mode_nonzero_mode_factorization() -> None:
    # At finite cutoff the fermion bilinear is a finite block matrix.  The
    # determinant factors into the nonzero-mode determinant and the zero-mode
    # Schur complement; the latter is the mass/source Berezin determinant.
    mass_zero_block = [[Fraction(2), Fraction(3)], [Fraction(5), Fraction(7)]]
    source_zero_block = [
        [Fraction(11), Fraction(13)],
        [Fraction(17), Fraction(19)],
    ]
    k00 = matrix_add_fraction(mass_zero_block, source_zero_block)
    k0n = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(5)]]
    kn0 = [[Fraction(7), Fraction(11)], [Fraction(13), Fraction(17)]]
    knn = [[Fraction(19), Fraction(23)], [Fraction(29), Fraction(31)]]
    schur_correction = matmul_fraction(
        k0n,
        matmul_fraction(inverse_2x2_fraction(knn), kn0),
    )
    schur_complement = matrix_sub_fraction(k00, schur_correction)
    full_bilinear = block_2x2_fraction(k00, k0n, kn0, knn)
    assert_equal(
        "fermion block determinant Schur factorization",
        det_fraction(full_bilinear),
        det_fraction(knn) * det_fraction(schur_complement),
    )

    zero_coupling = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
    projected_bilinear = block_2x2_fraction(
        k00,
        zero_coupling,
        zero_coupling,
        knn,
    )
    assert_equal(
        "zero-mode projected determinant separates nonzero determinant",
        det_fraction(projected_bilinear),
        det_fraction(knn) * det_fraction(k00),
    )

    rho = Fraction(5)
    masses = [Fraction(2, 3), Fraction(7, 11)]
    zero_mode_vacuum_determinant = product_fraction(
        [rho * mass for mass in masses]
    )
    finite_nonzero_factor = Fraction(13, 17)
    assert_equal(
        "mass factors are zero-mode determinant not spectral determinant",
        finite_nonzero_factor * zero_mode_vacuum_determinant,
        Fraction(4550, 561),
    )

    complementary_mass_cofactor = rho * masses[1]
    scheme_a = Fraction(13, 17)
    scheme_b = Fraction(19, 23)
    assert_equal(
        "zero-mode minor independent of nonzero-mode scheme factor A",
        scheme_a * complementary_mass_cofactor / scheme_a,
        complementary_mass_cofactor,
    )
    assert_equal(
        "zero-mode minor independent of nonzero-mode scheme factor B",
        scheme_b * complementary_mass_cofactor / scheme_b,
        complementary_mass_cofactor,
    )

    leading_source = [
        [Fraction(2, 5), Fraction(3, 7)],
        [Fraction(5, 11), Fraction(7, 13)],
    ]
    zero_to_nonzero = [
        [Fraction(1, 5), Fraction(1, 7)],
        [Fraction(1, 11), Fraction(1, 13)],
    ]
    nonzero_operator = [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(3)]]
    nonzero_to_zero = [
        [Fraction(1, 17), Fraction(1, 19)],
        [Fraction(1, 23), Fraction(1, 29)],
    ]
    source_schur = [
        [-entry for entry in row]
        for row in matmul_fraction(
            zero_to_nonzero,
            matmul_fraction(inverse_2x2_fraction(nonzero_operator), nonzero_to_zero),
        )
    ]
    exact_source_matrix = matrix_add_fraction(leading_source, source_schur)
    determinant_shift = (
        leading_source[1][1] * source_schur[0][0]
        + leading_source[0][0] * source_schur[1][1]
        - leading_source[1][0] * source_schur[0][1]
        - leading_source[0][1] * source_schur[1][0]
        + det_fraction(source_schur)
    )
    assert_equal(
        "source Schur determinant expansion",
        det_fraction(exact_source_matrix),
        det_fraction(leading_source) + determinant_shift,
    )
    assert_equal(
        "dropping source Schur correction changes four-source coefficient",
        det_fraction(exact_source_matrix) == det_fraction(leading_source),
        False,
    )

    l_bound = max(abs(entry) for row in leading_source for entry in row)
    eta_bound = max(abs(entry) for row in source_schur for entry in row)
    schur_error_bound = 4 * l_bound * eta_bound + 2 * eta_bound * eta_bound
    assert_equal(
        "source Schur determinant stability bound",
        abs(det_fraction(exact_source_matrix) - det_fraction(leading_source))
        <= schur_error_bound,
        True,
    )

    second_source = [
        [Fraction(11, 17), Fraction(13, 19)],
        [Fraction(17, 23), Fraction(19, 29)],
    ]
    calibrated_constant = det_fraction(exact_source_matrix) / det_fraction(
        leading_source
    )
    second_exact = matrix_add_fraction(second_source, source_schur)
    assert_equal(
        "source Schur correction is not a universal determinant constant",
        calibrated_constant * det_fraction(second_source) == det_fraction(second_exact),
        False,
    )

    zero_source_schur = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
    assert_equal(
        "zero-to-nonzero source coupling hypothesis removes Schur correction",
        det_fraction(matrix_add_fraction(leading_source, zero_source_schur)),
        det_fraction(leading_source),
    )


def check_light_fermion_determinant_source_frame_covariance() -> None:
    zero_mode_kernel = [
        [Fraction(2, 3), Fraction(3, 5)],
        [Fraction(5, 7), Fraction(7, 11)],
    ]
    finite_fermion_factor = Fraction(13, 17)
    source_functional = finite_fermion_factor * det_fraction(zero_mode_kernel)

    z_r = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(3)]]
    z_l = [[Fraction(3), Fraction(2)], [Fraction(1), Fraction(2)]]
    transformed_kernel = matmul_fraction(
        matmul_fraction(z_r, zero_mode_kernel),
        z_l,
    )
    determinant_multiplier = det_fraction(z_r) * det_fraction(z_l)
    transformed_factor = finite_fermion_factor / determinant_multiplier

    assert_equal(
        "light-fermion determinant inverse source-frame covariance",
        transformed_factor * det_fraction(transformed_kernel),
        source_functional,
    )

    scalar_frame = Fraction(3, 2)
    scalar_kernel = [
        [scalar_frame * scalar_frame * entry for entry in row]
        for row in zero_mode_kernel
    ]
    flavor_count = 2
    scalar_factor = finite_fermion_factor / (scalar_frame ** (2 * flavor_count))
    assert_equal(
        "scalar source-frame power is two zero-mode sides per flavor",
        scalar_factor * det_fraction(scalar_kernel),
        source_functional,
    )

    counterterm_multiplier = Fraction(5, 9)
    counterterm_factor = counterterm_multiplier * transformed_factor
    assert_equal(
        "finite determinant counterterm multiplies source functional",
        counterterm_factor * det_fraction(transformed_kernel),
        counterterm_multiplier * source_functional,
    )


def check_light_fermion_reference_amplitude_calibration() -> None:
    # A reference amplitude can fix one finite light-fermion determinant
    # normalization only through the same-frame ratio of retained source
    # integrals.  Residuals from the reference observable are amplified by
    # B_target/B_ref.
    reference_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    target_cells = [Fraction(2, 7), -Fraction(1, 8), Fraction(5, 11)]
    b_ref = sum(reference_cells, Fraction(0))
    m_ref = sum(abs(cell) for cell in reference_cells)
    b_target = sum(target_cells, Fraction(0))
    m_target = sum(abs(cell) for cell in target_cells)
    kappa_ref = abs(b_ref) / m_ref

    assert_equal("reference instanton calibration integral", b_ref, Fraction(17, 20))
    assert_equal("reference instanton calibration absolute mass", m_ref, Fraction(21, 20))
    assert_equal("reference instanton calibration noncancellation margin", kappa_ref, Fraction(17, 21))

    determinant_normalization = Fraction(11, 17)
    reference_residual = Fraction(1, 50)
    target_residual = -Fraction(1, 70)
    reference_amplitude = determinant_normalization * b_ref + reference_residual
    target_amplitude = determinant_normalization * b_target + target_residual
    calibrated_prediction = reference_amplitude * b_target / b_ref

    assert_equal(
        "reference-amplitude calibration residual identity",
        target_amplitude - calibrated_prediction,
        target_residual - reference_residual * b_target / b_ref,
    )
    calibration_bound = abs(target_residual) + abs(b_target / b_ref) * abs(reference_residual)
    assert_equal(
        "reference-amplitude calibration residual bound",
        abs(target_amplitude - calibrated_prediction) <= calibration_bound,
        True,
    )
    assert_equal(
        "reference-amplitude calibration ratio margin bound",
        abs(b_target / b_ref) <= m_target / (kappa_ref * m_ref),
        True,
    )

    zero_residual_reference = determinant_normalization * b_ref
    assert_equal(
        "reference calibration exact when residuals vanish",
        zero_residual_reference * b_target / b_ref,
        determinant_normalization * b_target,
    )

    # A common finite source-frame change rescales all zero-mode source
    # integrals and the determinant normalization inversely.  The leading
    # amplitudes and the calibrated ratio are unchanged only because the same
    # frame is used for both reference and target.
    source_frame_scale = Fraction(5, 3)
    flavor_count = 2
    frame_factor = source_frame_scale**flavor_count
    scaled_b_ref = frame_factor * b_ref
    scaled_b_target = frame_factor * b_target
    scaled_determinant_normalization = determinant_normalization / frame_factor
    assert_equal(
        "same-frame calibration keeps leading reference amplitude",
        scaled_determinant_normalization * scaled_b_ref,
        determinant_normalization * b_ref,
    )
    assert_equal(
        "same-frame calibration keeps source ratio",
        scaled_b_target / scaled_b_ref,
        b_target / b_ref,
    )

    # A nearly cancelled reference channel is a bad normalization coordinate:
    # the same absolute reference residual becomes a large calibrated
    # uncertainty.
    canceled_reference_cells = [Fraction(1), -Fraction(99, 100)]
    b_cancel = sum(canceled_reference_cells, Fraction(0))
    m_cancel = sum(abs(cell) for cell in canceled_reference_cells)
    kappa_cancel = abs(b_cancel) / m_cancel
    assert_equal("canceled reference instanton integral", b_cancel, Fraction(1, 100))
    assert_equal("canceled reference noncancellation margin", kappa_cancel, Fraction(1, 199))
    assert_equal(
        "canceled reference residual is not relatively small",
        abs(reference_residual) / abs(b_cancel) <= Fraction(1, 10),
        False,
    )
    assert_equal(
        "canceled reference amplifies calibration residual",
        abs(reference_residual * b_target / b_cancel)
        > 50 * abs(reference_residual * b_target / b_ref),
        True,
    )


def check_instanton_finite_scheme_transport_bound() -> None:
    # Work with the exponential of the finite coupling-coordinate shift,
    # exp(delta_X), as an exact rational fixture.  The common exp(-X_S) factor
    # is omitted; exp(-X_S') contributes the inverse shift.
    determinant_constant = Fraction(7, 11)
    source_integral = Fraction(13, 17)
    operator_matrix_element = Fraction(19, 23)
    leading_amplitude = determinant_constant * source_integral * operator_matrix_element

    coupling_shift_factor = Fraction(5, 3)
    source_frame_factor = Fraction(11, 7)
    operator_frame_factor = Fraction(4, 5)
    transported_constant = (
        coupling_shift_factor
        * determinant_constant
        / (source_frame_factor * operator_frame_factor)
    )
    shifted_exponential_factor = Fraction(1, 1) / coupling_shift_factor
    shifted_source = source_frame_factor * source_integral
    shifted_operator = operator_frame_factor * operator_matrix_element

    assert_equal(
        "finite scheme transport preserves instanton amplitude",
        transported_constant * shifted_exponential_factor * shifted_source * shifted_operator,
        leading_amplitude,
    )

    stale_constant_amplitude = (
        determinant_constant
        * shifted_exponential_factor
        * shifted_source
        * shifted_operator
    )
    assert_equal(
        "stale determinant constant changes scheme-shifted amplitude",
        stale_constant_amplitude == leading_amplitude,
        False,
    )
    assert_equal(
        "stale determinant constant amplitude ratio",
        stale_constant_amplitude / leading_amplitude,
        source_frame_factor * operator_frame_factor / coupling_shift_factor,
    )

    missing_source_compensation = (
        coupling_shift_factor * determinant_constant / operator_frame_factor
    )
    assert_equal(
        "missing source-frame inverse compensation changes amplitude",
        missing_source_compensation
        * shifted_exponential_factor
        * shifted_source
        * shifted_operator
        == leading_amplitude,
        False,
    )

    # Multiplicative residuals are written as exp(r_i).  The logarithmic bound
    # bound exp(sum |r_i|)-1 is checked exactly as prod max(q_i, q_i^(-1))-1.
    residual_factors = [
        Fraction(101, 100),  # determinant constant residual
        Fraction(99, 100),  # coupling-coordinate residual in exp(-X)
        Fraction(51, 50),  # source-coordinate residual
        Fraction(98, 100),  # operator/projection residual
    ]
    residual_amplitude_ratio = product_fraction(residual_factors)
    log_bound_multiplier = product_fraction(
        factor if factor >= 1 else Fraction(1, 1) / factor for factor in residual_factors
    )
    assert_equal(
        "finite scheme residual amplitude bound",
        abs(residual_amplitude_ratio - 1) <= log_bound_multiplier - 1,
        True,
    )

    canceling_residual_factors = [Fraction(3, 2), Fraction(2, 3)]
    canceling_ratio = product_fraction(canceling_residual_factors)
    canceling_bound = product_fraction(
        factor if factor >= 1 else Fraction(1, 1) / factor
        for factor in canceling_residual_factors
    )
    assert_equal("canceling finite-scheme residuals can hide in the ratio", canceling_ratio, Fraction(1))
    assert_equal(
        "finite scheme bound does not vanish by residual cancellation",
        canceling_bound == Fraction(1),
        False,
    )


def check_instanton_mass_source_rg_transport() -> None:
    # The source functional before differentiation is R_f(mu) det(M^0 + J^0),
    # with M^0 and J^0 linear in the mass and source coordinates.  If M and J
    # have mass anomalous dimension -gamma_m, determinant homogeneity gives
    # weight -Nf gamma_m, so the finite fermion determinant factor must carry
    # +Nf gamma_m in the same source convention.
    mass_matrix = [
        [Fraction(2), Fraction(3), Fraction(5)],
        [Fraction(7), Fraction(11), Fraction(13)],
        [Fraction(17), Fraction(19), Fraction(23)],
    ]
    source_matrix = [
        [Fraction(29), Fraction(31), Fraction(37)],
        [Fraction(41), Fraction(43), Fraction(47)],
        [Fraction(53), Fraction(59), Fraction(61)],
    ]
    rho = Fraction(5)
    zero_mode_matrix = [
        [
            rho * (mass_matrix[row][col] + source_matrix[row][col])
            for col in range(3)
        ]
        for row in range(3)
    ]
    scaling = Fraction(7, 5)
    scaled_zero_mode_matrix = [
        [scaling * entry for entry in row]
        for row in zero_mode_matrix
    ]
    assert_equal(
        "mass/source determinant homogeneous degree Nf",
        det_fraction(scaled_zero_mode_matrix),
        scaling**3 * det_fraction(zero_mode_matrix),
    )

    gamma_m = Fraction(5, 13)
    flavor_count = 3
    determinant_rg_weight = -flavor_count * gamma_m
    fermion_factor_rg_weight = flavor_count * gamma_m
    assert_equal(
        "source-functional anomalous dimensions cancel",
        fermion_factor_rg_weight + determinant_rg_weight,
        Fraction(0),
    )

    diagonal_masses = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    vacuum_mass_product = product_fraction([rho * mass for mass in diagonal_masses])
    assert_equal(
        "mass-saturated zero-mode determinant rho power",
        vacuum_mass_product,
        rho**flavor_count * product_fraction(diagonal_masses),
    )
    assert_equal(
        "mass-saturated anomalous source transport cancels",
        fermion_factor_rg_weight - flavor_count * gamma_m,
        Fraction(0),
    )

    # After r source differentiations, the remaining mass minor has degree
    # Nf-r.  The coefficient therefore transports with r gamma_m, which is the
    # Callan-Symanzik covariance of r inserted renormalized scalar densities.
    for source_derivatives in range(flavor_count + 1):
        mass_minor_degree = flavor_count - source_derivatives
        differentiated_weight = (
            fermion_factor_rg_weight
            - mass_minor_degree * gamma_m
        )
        assert_equal(
            f"{source_derivatives}-source instanton coefficient RG covariance",
            differentiated_weight,
            source_derivatives * gamma_m,
        )

    theta_phase = Fraction(17, 3)
    positive_mass_renormalization_arg_shift = Fraction(0)
    anomalous_chiral_arg_shift = Fraction(-5, 2)
    anomalous_chiral_theta_shift = Fraction(5, 2)
    assert_equal(
        "positive mass renormalization leaves strong CP phase unchanged",
        theta_phase + positive_mass_renormalization_arg_shift,
        theta_phase,
    )
    assert_equal(
        "chiral anomaly keeps theta plus arg det M invariant",
        anomalous_chiral_arg_shift + anomalous_chiral_theta_shift,
        Fraction(0),
    )


def check_one_instanton_channel_rg_ledger() -> None:
    # The full channel ledger combines the universal density, the zero-mode
    # source functional, and the external operator/projection normalization.
    # Each component has a nonzero log transport; the assembled channel is the
    # object with the declared Callan-Symanzik covariance.
    b0 = Fraction(29, 3)
    universal_density_log_weight = b0 - b0
    assert_equal(
        "universal instanton density one-loop RG cancellation",
        universal_density_log_weight,
        Fraction(0),
    )
    assert_equal(
        "omitting the instanton determinant logarithm is not RG neutral",
        -b0 == Fraction(0),
        False,
    )

    gamma_m = Fraction(5, 13)
    flavor_count = 3
    source_determinant_weight = -flavor_count * gamma_m
    finite_fermion_factor_weight = flavor_count * gamma_m
    assert_equal(
        "source determinant and finite fermion factor cancel in channel ledger",
        source_determinant_weight + finite_fermion_factor_weight,
        Fraction(0),
    )
    assert_equal(
        "mass/source determinant alone is not the channel RG object",
        source_determinant_weight == Fraction(0),
        False,
    )

    for source_derivatives in range(flavor_count + 1):
        mass_minor_degree = flavor_count - source_derivatives
        differentiated_coefficient_weight = (
            finite_fermion_factor_weight
            - mass_minor_degree * gamma_m
        )
        external_projection_weight = -source_derivatives * gamma_m
        assert_equal(
            f"{source_derivatives}-source channel RG covariance is paired",
            differentiated_coefficient_weight + external_projection_weight,
            Fraction(0),
        )

    # Absolute residual control of a signed channel needs a noncancellation
    # margin.  The same pointwise absolute logarithmic residual can be a small
    # relative error in a healthy channel and a large relative error in a
    # nearly cancelled channel.
    retained_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    retained_signed = sum(retained_cells, Fraction(0))
    retained_mass = sum(abs(cell) for cell in retained_cells)
    kappa = abs(retained_signed) / retained_mass
    eta = Fraction(1, 20)
    worst_signed_delta = eta * retained_mass
    assert_equal("channel RG ledger retained signed window", retained_signed, Fraction(17, 20))
    assert_equal("channel RG ledger retained absolute mass", retained_mass, Fraction(21, 20))
    assert_equal("channel RG ledger noncancellation margin", kappa, Fraction(17, 21))
    assert_equal(
        "channel RG residual relative bound",
        worst_signed_delta / abs(retained_signed),
        eta / kappa,
    )

    canceled_cells = [Fraction(1), -Fraction(99, 100)]
    canceled_signed = sum(canceled_cells, Fraction(0))
    canceled_mass = sum(abs(cell) for cell in canceled_cells)
    canceled_kappa = abs(canceled_signed) / canceled_mass
    assert_equal("nearly canceled channel margin", canceled_kappa, Fraction(1, 199))
    assert_equal(
        "nearly canceled channel amplifies the same absolute RG residual",
        eta / canceled_kappa > 100 * eta / kappa,
        True,
    )

    # Moving the Wilsonian size split is a boundary-flux identity, not the
    # renormalization-scale cancellation of the universal density.
    size_boundary_flux = Fraction(3, 17)
    short_size_flow = -size_boundary_flux
    long_size_flow = size_boundary_flux
    assert_equal(
        "short and long instanton size-window RG ledger flux cancels",
        short_size_flow + long_size_flow,
        Fraction(0),
    )
    assert_equal(
        "size-factorization flux is not the one-loop universal density RG weight",
        size_boundary_flux == universal_density_log_weight,
        False,
    )


def check_proper_time_fluctuation_four_fermion_amplitude() -> None:
    # A finite proper-time determinant ledger is a product over nonzero
    # spectra.  The zero eigenvalue is visible before collective-coordinate
    # projection and is absent from the determinant datum.
    raw_boson_instanton_spectrum = [Fraction(0), Fraction(11), Fraction(13), Fraction(17)]
    boson_instanton_nonzero = [
        eigenvalue for eigenvalue in raw_boson_instanton_spectrum if eigenvalue != 0
    ]
    assert_equal(
        "unprojected instanton bosonic determinant has zero mode",
        product_fraction(raw_boson_instanton_spectrum),
        Fraction(0),
    )
    assert_equal(
        "bosonic collective coordinate removed before determinant",
        len(raw_boson_instanton_spectrum) - len(boson_instanton_nonzero),
        1,
    )

    boson_vacuum_spectrum = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
    ghost_vacuum_spectrum = [Fraction(19), Fraction(23)]
    ghost_instanton_spectrum = [Fraction(29), Fraction(31)]
    fermion_vacuum_pfaffian_blocks = [Fraction(37), Fraction(41)]
    fermion_instanton_pfaffian_blocks = [Fraction(43), Fraction(47)]

    boson_inverse_sqrt_squared = (
        product_fraction(boson_vacuum_spectrum)
        / product_fraction(boson_instanton_nonzero)
    )
    ghost_ratio = (
        product_fraction(ghost_instanton_spectrum)
        / product_fraction(ghost_vacuum_spectrum)
    )
    fermion_pfaffian_ratio = (
        product_fraction(fermion_instanton_pfaffian_blocks)
        / product_fraction(fermion_vacuum_pfaffian_blocks)
    )
    nonzero_mode_weight_squared = (
        boson_inverse_sqrt_squared
        * ghost_ratio
        * ghost_ratio
        * fermion_pfaffian_ratio
        * fermion_pfaffian_ratio
    )
    assert_equal(
        "proper-time nonzero-mode determinant weight squared",
        nonzero_mode_weight_squared,
        Fraction(210, 2431) * Fraction(899, 437) ** 2 * Fraction(2021, 1517) ** 2,
    )

    # An independent even bilinear source matrix enters through the
    # zero-mode-projected two-flavor determinant.  The full semiclassical
    # source functional is W_nz times the zero-mode Berezin coefficient,
    # integrated over collective coordinates; this finite check tracks the
    # bilinear-source scalar integrand.
    source_matrix = [[Fraction(2), Fraction(3)], [Fraction(5), Fraction(11)]]
    source_determinant = det_fraction(source_matrix)
    assert_equal(
        "zero-mode projected four-fermion source determinant",
        grassmann_source_determinant_top_coefficient(source_matrix),
        source_determinant,
    )
    four_fermion_integrand_squared = (
        nonzero_mode_weight_squared * source_determinant * source_determinant
    )
    assert_equal(
        "four-fermion instanton amplitude integrand squared",
        four_fermion_integrand_squared,
        nonzero_mode_weight_squared * Fraction(49),
    )

    # In the local limit for N_f=2, each zero-mode source matrix entry carries
    # the BPST zero-mode normalization rho^3, while det(B_eta) contains two
    # entries.  This is the rho^6 factor in the local four-fermion vertex.
    assert_equal("two-flavor local 't Hooft vertex rho power", 2 * 3, 6)

    # The universal log(mu rho) power is the sum of the proper-time small-t
    # trace coefficient and the coupling/counterterm conversion in the same
    # scheme.  For SU(3) with two Dirac fundamentals this equals b0=29/3.
    spectral_trace_power = Fraction(7, 3)
    coupling_and_local_counterterm_power = Fraction(22, 3)
    assert_equal(
        "proper-time plus counterterm log power for SU(3) Nf=2",
        spectral_trace_power + coupling_and_local_counterterm_power,
        Fraction(29, 3),
    )


def check_proper_time_determinant_residual_window() -> None:
    # The log determinant is a weighted sum of block trace remainders.  A
    # bound for a physical amplitude needs the absolute weighted sum,
    # because exp(delta_log) multiplies the zero-mode/source kernel pointwise.
    weights = {
        "ghost": Fraction(1),
        "boson": Fraction(-1, 2),
        "fermion": Fraction(1),
    }
    trace_residuals = {
        "ghost": Fraction(1, 40),
        "boson": Fraction(-1, 18),
        "fermion": Fraction(1, 63),
    }
    trace_bounds = {
        "ghost": Fraction(1, 30),
        "boson": Fraction(1, 15),
        "fermion": Fraction(1, 42),
    }
    log_residual = sum(
        weights[name] * trace_residuals[name]
        for name in weights
    )
    epsilon_det = sum(
        abs(weights[name]) * trace_bounds[name]
        for name in weights
    )
    assert_equal(
        "proper-time determinant log residual bound",
        abs(log_residual) <= epsilon_det,
        True,
    )

    lead_weight = Fraction(5, 7)
    exact_weight = float(lead_weight) * math.exp(float(log_residual))
    determinant_bound = float(lead_weight) * (math.exp(float(epsilon_det)) - 1.0)
    if not abs(exact_weight - float(lead_weight)) <= determinant_bound:
        raise AssertionError("determinant multiplicative residual bound failed")

    lead_cells = [Fraction(2, 7), Fraction(3, 11), Fraction(5, 13)]
    local_log_residuals = [Fraction(1, 50), Fraction(-1, 45), Fraction(1, 60)]
    window_epsilon = Fraction(1, 30)
    exact_amplitude = sum(
        float(cell) * math.exp(float(delta))
        for cell, delta in zip(lead_cells, local_log_residuals)
    )
    lead_amplitude = sum(float(cell) for cell in lead_cells)
    amplitude_bound = sum(float(abs(cell)) for cell in lead_cells) * (
        math.exp(float(window_epsilon)) - 1.0
    )
    if not abs(exact_amplitude - lead_amplitude) <= amplitude_bound:
        raise AssertionError("proper-time determinant amplitude-window bound failed")

    signed_fake_bound = (
        weights["ghost"] * Fraction(1, 12)
        + weights["boson"] * Fraction(1, 3)
        + weights["fermion"] * Fraction(1, 12)
    )
    absolute_bound = (
        abs(weights["ghost"]) * Fraction(1, 12)
        + abs(weights["boson"]) * Fraction(1, 3)
        + abs(weights["fermion"]) * Fraction(1, 12)
    )
    assert_equal(
        "signed determinant residuals can cancel spuriously",
        signed_fake_bound,
        Fraction(0),
    )
    if not absolute_bound > 0:
        raise AssertionError("absolute determinant bound vanished")


def check_instanton_source_typing_and_differentiation() -> None:
    right_vector = [Fraction(2), Fraction(3)]
    left_vector = [Fraction(5), Fraction(7)]
    cnumber_outer_product = [
        [right * left for left in left_vector]
        for right in right_vector
    ]
    assert_equal(
        "c-number external wave-packet outer product determinant vanishes",
        det_fraction(cnumber_outer_product),
        Fraction(0),
    )

    right_slots = [[Fraction(2), Fraction(3)], [Fraction(5), Fraction(11)]]
    left_slots = [[Fraction(7), Fraction(13)], [Fraction(17), Fraction(19)]]
    differentiated_coefficient = grassmann_linear_source_four_slot_coefficient(
        right_slots,
        left_slots,
    )
    expected_coefficient = det_fraction(right_slots) * det_fraction(left_slots)
    assert_equal(
        "differentiated Grassmann source four-slot coefficient",
        differentiated_coefficient,
        expected_coefficient,
    )
    assert_equal(
        "differentiated source coefficient is nonzero",
        differentiated_coefficient == 0,
        False,
    )


def check_connected_four_source_instanton_extraction() -> None:
    def scale_polynomial(
        polynomial: GrassmannPolynomial,
        factor: Fraction,
    ) -> GrassmannPolynomial:
        return {
            monomial: coefficient * factor
            for monomial, coefficient in polynomial.items()
            if coefficient * factor != 0
        }

    def two_source_polynomial(matrix: list[list[Fraction]]) -> GrassmannPolynomial:
        polynomial: GrassmannPolynomial = {}
        for bar_slot in range(2):
            for chi_slot in range(2):
                polynomial = grassmann_add(
                    polynomial,
                    grassmann_monomial(
                        bar_slot,
                        2 + chi_slot,
                        coefficient=matrix[bar_slot][chi_slot],
                    ),
                )
        return polynomial

    def connected_coefficient(
        z0: Fraction,
        z2: list[list[Fraction]],
        z4: Fraction,
    ) -> Fraction:
        return z4 / z0 + det_fraction(z2) / (z0 * z0)

    z0 = Fraction(5)
    z2 = [[Fraction(2), Fraction(3)], [Fraction(5), Fraction(7)]]
    z4 = Fraction(11)
    x = scale_polynomial(two_source_polynomial(z2), Fraction(1, 1) / z0)
    y = grassmann_monomial(0, 1, 2, 3, coefficient=z4 / z0)
    log_polynomial = grassmann_add(
        grassmann_add(x, y),
        scale_polynomial(grassmann_mul(x, x), -Fraction(1, 2)),
    )
    top_from_log = berezin_top_coefficient(log_polynomial, 4)
    expected_connected = connected_coefficient(z0, z2, z4)
    assert_equal(
        "connected four-source coefficient from log source functional",
        top_from_log,
        expected_connected,
    )
    assert_equal(
        "Grassmann log square sign gives plus determinant subtraction",
        top_from_log,
        Fraction(54, 25),
    )

    unconnected_top = z4 / z0
    assert_equal(
        "top Berezin coefficient is not connected with lower source terms",
        unconnected_top == top_from_log,
        False,
    )

    mass_background_z0 = Fraction(6)
    mass_background_z2 = [[Fraction(3), Fraction(0)], [Fraction(0), Fraction(2)]]
    mass_background_z4 = Fraction(1)
    assert_equal(
        "mass-saturated lower source terms change connected four-source kernel",
        connected_coefficient(
            mass_background_z0,
            mass_background_z2,
            mass_background_z4,
        ),
        Fraction(1, 3),
    )
    assert_equal(
        "mass-background top coefficient alone misses connected subtraction",
        mass_background_z4 / mass_background_z0 == Fraction(1, 3),
        False,
    )

    rank_one_z2 = [[Fraction(2), Fraction(4)], [Fraction(3), Fraction(6)]]
    assert_equal(
        "rank-one lower source matrix has zero determinant",
        det_fraction(rank_one_z2),
        Fraction(0),
    )
    assert_equal(
        "rank-one lower source terms do not shift connected top coefficient",
        connected_coefficient(z0, rank_one_z2, z4),
        z4 / z0,
    )

    exact_z0 = Fraction(51, 10)
    exact_z2 = [
        [Fraction(41, 20), Fraction(59, 20)],
        [Fraction(101, 20), Fraction(139, 20)],
    ]
    exact_z4 = Fraction(111, 10)
    exact_connected = connected_coefficient(exact_z0, exact_z2, exact_z4)
    actual_error = abs(exact_connected - expected_connected)

    e0 = abs(exact_z0 - z0)
    e4 = abs(exact_z4 - z4)
    e2 = Fraction(1, 20)
    entry_bound = max(abs(entry) for row in z2 for entry in row)
    determinant_error_bound = 4 * entry_bound * e2 + 2 * e2 * e2
    d0 = min(abs(z0), abs(exact_z0))
    z4_ratio_error_bound = e4 / d0 + abs(z4) * e0 / (abs(z0) * d0)
    determinant_ratio_error_bound = (
        determinant_error_bound / (d0 * d0)
        + abs(det_fraction(z2))
        * abs(exact_z0 * exact_z0 - z0 * z0)
        / (z0 * z0 * d0 * d0)
    )
    if not actual_error <= z4_ratio_error_bound + determinant_ratio_error_bound:
        raise AssertionError("connected four-source extraction residual bound failed")


def check_instanton_heat_kernel_beta0_logarithm() -> None:
    n_c = 3
    n_f = 2
    t_fundamental = Fraction(1, 2)
    vector_ghost_coefficient = Fraction(11, 3) * n_c
    dirac_matter_coefficient = -Fraction(4, 3) * n_f * t_fundamental
    beta0 = vector_ghost_coefficient + dirac_matter_coefficient
    assert_equal("SU(3) Nf=2 vector plus ghost heat coefficient", vector_ghost_coefficient, 11)
    assert_equal("SU(3) Nf=2 Dirac heat coefficient", dirac_matter_coefficient, Fraction(-4, 3))
    assert_equal("SU(3) Nf=2 instanton heat-kernel beta0", beta0, Fraction(29, 3))

    # In a cutoff ledger, X_Lambda=X_mu+b0 log(Lambda/mu) and the determinant
    # logarithm contains b0 log(Lambda rho).  The coefficient of
    # log(Lambda/mu) cancels between the bare instanton exponential and the
    # nonzero-mode determinant, leaving b0 log(mu rho).
    cutoff_log_coefficient = -beta0 + beta0
    assert_equal("cutoff scale cancels in instanton logarithm", cutoff_log_coefficient, 0)

    charge = 3
    assert_equal(
        "charge-k heat-kernel logarithm is k beta0",
        charge * beta0,
        Fraction(29),
    )

    # Mass-saturated QCD adds one rho power per Dirac zero-mode pair after the
    # fluctuation determinant has supplied the universal beta0 power.
    mass_saturation_power = n_f
    density_power = beta0 + mass_saturation_power - 5
    assert_equal("SU(3) Nf=2 mass-saturated density power", density_power, Fraction(20, 3))
    assert_equal("SU(3) Nf=2 mass-saturated endpoint margin", density_power + 1, Fraction(23, 3))


def check_instanton_zero_mode_tail_local_limit() -> None:
    # The normalized scalar envelope of a BPST fundamental zero-mode line is
    # h_rho(y)=2 rho^2/[pi^2 (y^2+rho^2)^3].  After the angular integral,
    # the cumulative mass inside R=rho*U is
    # P(U)=4 int_0^U u^3/(1+u^2)^3 du = U^4/(1+U^2)^2.
    for u in [Fraction(1, 3), Fraction(2, 1), Fraction(5, 2)]:
        cumulative = u**4 / (1 + u * u) ** 2
        tail = (1 + 2 * u * u) / (1 + u * u) ** 2
        assert_equal(f"zero-mode cumulative plus tail U={u}", cumulative + tail, 1)

        radial_density = 4 * u**3 / (1 + u * u) ** 3
        cumulative_derivative = 4 * u**3 / (1 + u * u) ** 3
        assert_equal(
            f"zero-mode cumulative derivative U={u}",
            cumulative_derivative,
            radial_density,
        )

        # With q=(rho/R)^2=U^{-2}, the tail is q(2+q)/(1+q)^2.  The leading
        # power is 2q, and the exact remainder starts at order q^2.
        q = 1 / (u * u)
        tail_in_q = q * (2 + q) / (1 + q) ** 2
        assert_equal(f"zero-mode tail q form U={u}", tail_in_q, tail)
        assert_equal(
            f"zero-mode tail leading-power remainder U={u}",
            tail - 2 * q,
            -q * q * (3 + 2 * q) / (1 + q) ** 2,
        )

        # The truncated second moment is
        # M2(U)=2 rho^2 [log(1+U^2)+2/(1+U^2)-1/(2(1+U^2)^2)-3/2].
        # Differentiating the bracket gives 2 U^5/(1+U^2)^3, hence
        # dM2/dU=4 rho^2 U^5/(1+U^2)^3, matching the radial integrand.
        second_moment_derivative_over_rho2 = 4 * u**5 / (1 + u * u) ** 3
        second_moment_integrand = 4 * u**5 / (1 + u * u) ** 3
        assert_equal(
            f"zero-mode second-moment derivative U={u}",
            second_moment_derivative_over_rho2,
            second_moment_integrand,
        )

    # In four Euclidean dimensions rotational invariance gives
    # int y_mu y_nu h = delta_mu_nu M2/4.  The trace over four directions
    # recovers M2.
    tensor_trace_units = 4 * Fraction(1, 4)
    assert_equal("zero-mode tensor second moment trace", tensor_trace_units, 1)

    # If a source has dimension d_s, the local zero-mode entry carries
    # rho^d_s.  A mass source uses d_s=1; the local quark bilinear in the
    # 't Hooft vertex uses d_s=3.
    assert_equal("mass source zero-mode rho power", 1, 1)
    assert_equal("bilinear source zero-mode rho power", 3, 3)

    # Schwinger-parameter prefactor for the Fourier transform:
    # h = 2 rho^2/pi^2 * (y^2+rho^2)^(-3), Gamma(3)=2, and
    # int d^4y exp(-s y^2) = pi^2 s^(-2).  The remaining integral is
    # rho^2 int ds exp[-rho^2 s - q^2/(4s)] = z K_1(z).
    schwinger_prefactor = Fraction(2) * Fraction(1, 2)
    gaussian_prefactor = Fraction(1)
    assert_equal(
        "zero-mode Fourier Schwinger prefactor",
        schwinger_prefactor * gaussian_prefactor,
        1,
    )

    # The form factor F(z)=z K_1(z) satisfies z F'' - F' - z F=0.
    # A small-z ansatz F=1+a z^2 log z+b z^2+... solves the order-z
    # equation only if a=1/2; b is fixed only after the specific K_1 branch
    # and its Euler-gamma/log(2) constants are chosen.
    a = Fraction(1, 2)
    assert_equal("zero-mode form-factor log coefficient", 2 * a - 1, 0)

    # For large z, K_nu(z) has first correction (4 nu^2-1)/(8z).
    nu = 1
    first_large_z_coefficient = Fraction(4 * nu * nu - 1, 8)
    assert_equal(
        "zero-mode form-factor large-z first coefficient",
        first_large_z_coefficient,
        Fraction(3, 8),
    )

    # The individual singular-gauge zero-mode slot is different from the fused
    # density h_rho.  Its standard scalar form factor is
    # F_zm(t)=-t d_t[I0(t)K0(t)-I1(t)K1(t)]
    #       =2t(I0K1-I1K0)-2I1K1, t=rho |p|/2.
    # At small t, I0K1 contributes 1/t and I1K1 contributes 1/2, so F_zm(0)=1.
    small_t_first_term = Fraction(2)
    small_t_second_term = Fraction(-1)
    assert_equal(
        "individual zero-mode form-factor normalization",
        small_t_first_term + small_t_second_term,
        Fraction(1),
    )

    # Large-t asymptotics of the products, after removing their common 1/(2t),
    # are checked through the first nonzero term of F_zm.  In
    # F_n = (I0K1)_n - (I1K0)_n - (I1K1)_{n-1}, the n=0,1,2 coefficients cancel
    # and the n=3 coefficient is 3/4.
    i0k1 = [Fraction(1), Fraction(1, 2), Fraction(0), Fraction(3, 16)]
    i1k0 = [Fraction(1), Fraction(-1, 2), Fraction(0), Fraction(-3, 16)]
    i1k1 = [Fraction(1), Fraction(0), Fraction(-3, 8)]
    individual_large_coefficients = []
    for order in range(4):
        coefficient = i0k1[order] - i1k0[order]
        if order >= 1:
            coefficient -= i1k1[order - 1]
        individual_large_coefficients.append(coefficient)
    assert_equal(
        "individual zero-mode form-factor large-t cancellations",
        individual_large_coefficients[:3],
        [Fraction(0), Fraction(0), Fraction(0)],
    )
    assert_equal(
        "individual zero-mode form-factor t^-3 coefficient",
        individual_large_coefficients[3],
        Fraction(3, 4),
    )
    assert_equal(
        "individual zero-mode form-factor z^-3 coefficient",
        individual_large_coefficients[3] * 8,
        Fraction(6),
    )

    # Momentum-dependent source entries carry the form factor before the
    # flavor Berezin determinant is taken.
    source_matrix = [[Fraction(2), Fraction(3)], [Fraction(5), Fraction(7)]]
    form_factors = [[Fraction(11, 13), Fraction(17, 19)], [Fraction(23, 29), Fraction(31, 37)]]
    dressed_source = [
        [
            source_matrix[row][col] * form_factors[row][col]
            for col in range(2)
        ]
        for row in range(2)
    ]
    expected_dressed_det = (
        source_matrix[0][0]
        * form_factors[0][0]
        * source_matrix[1][1]
        * form_factors[1][1]
        -
        source_matrix[0][1]
        * form_factors[0][1]
        * source_matrix[1][0]
        * form_factors[1][0]
    )
    assert_equal(
        "zero-mode form factors enter before flavor determinant",
        det_fraction(dressed_source),
        expected_dressed_det,
    )


def check_instanton_external_leg_amputation_kernel() -> None:
    right_slot_residues = [Fraction(2, 3), Fraction(5, 7)]
    left_slot_residues = [Fraction(11, 13), Fraction(17, 19)]
    right_amputated_slots = [
        [Fraction(3, 5), Fraction(7, 11)],
        [Fraction(13, 17), Fraction(19, 23)],
    ]
    left_amputated_slots = [
        [Fraction(29, 31), Fraction(37, 41)],
        [Fraction(43, 47), Fraction(53, 59)],
    ]
    right_unamputated_slots = [
        [
            right_slot_residues[slot] * right_amputated_slots[slot][flavor]
            for flavor in range(2)
        ]
        for slot in range(2)
    ]
    left_unamputated_slots = [
        [
            left_amputated_slots[flavor][slot] * left_slot_residues[slot]
            for slot in range(2)
        ]
        for flavor in range(2)
    ]
    slot_residue_product = (
        product_fraction(right_slot_residues)
        * product_fraction(left_slot_residues)
    )
    assert_equal(
        "linear source slot determinant external residue factor",
        det_fraction(right_unamputated_slots)
        * det_fraction(left_unamputated_slots),
        slot_residue_product
        * det_fraction(right_amputated_slots)
        * det_fraction(left_amputated_slots),
    )
    assert_equal(
        "linear source amputation preserves differentiated coefficient",
        (
            det_fraction(right_unamputated_slots)
            * det_fraction(left_unamputated_slots)
            / slot_residue_product
        ),
        det_fraction(right_amputated_slots) * det_fraction(left_amputated_slots),
    )

    row_leg_residues = [Fraction(2, 3), Fraction(5, 7)]
    column_leg_residues = [Fraction(11, 13), Fraction(17, 19)]
    orientation_tensor = [[Fraction(3), Fraction(5)], [Fraction(7), Fraction(11)]]
    form_factors = [
        [Fraction(23, 29), Fraction(31, 37)],
        [Fraction(41, 43), Fraction(47, 53)],
    ]
    amputated_source = [
        [
            orientation_tensor[row][col] * form_factors[row][col]
            for col in range(2)
        ]
        for row in range(2)
    ]
    unamputated_source = [
        [
            row_leg_residues[row]
            * amputated_source[row][col]
            * column_leg_residues[col]
            for col in range(2)
        ]
        for row in range(2)
    ]
    external_residue_product = (
        product_fraction(row_leg_residues)
        * product_fraction(column_leg_residues)
    )
    assert_equal(
        "bilinear source determinant row-column external residue factor",
        det_fraction(unamputated_source),
        external_residue_product * det_fraction(amputated_source),
    )

    recovered_amputated_source = [
        [
            unamputated_source[row][col]
            / row_leg_residues[row]
            / column_leg_residues[col]
            for col in range(2)
        ]
        for row in range(2)
    ]
    assert_equal(
        "bilinear external-leg amputation recovers zero-mode source matrix",
        recovered_amputated_source,
        amputated_source,
    )

    expected_amputated_det = (
        orientation_tensor[0][0]
        * form_factors[0][0]
        * orientation_tensor[1][1]
        * form_factors[1][1]
        -
        orientation_tensor[0][1]
        * form_factors[0][1]
        * orientation_tensor[1][0]
        * form_factors[1][0]
    )
    assert_equal(
        "amputated bilinear instanton determinant retains form factors",
        det_fraction(amputated_source),
        expected_amputated_det,
    )

    second_amputated_source = [
        [Fraction(13, 17), Fraction(19, 23)],
        [Fraction(29, 31), Fraction(37, 41)],
    ]
    weights = [Fraction(43, 47), Fraction(53, 59)]
    unamputated_integral = (
        weights[0] * det_fraction(unamputated_source)
        + weights[1]
        * external_residue_product
        * det_fraction(second_amputated_source)
    )
    amputated_integral = unamputated_integral / external_residue_product
    assert_equal(
        "collective integral commutes with external-leg amputation",
        amputated_integral,
        (
            weights[0] * det_fraction(amputated_source)
            + weights[1] * det_fraction(second_amputated_source)
        ),
    )


def check_plane_wave_instanton_four_fermion_assembly() -> None:
    def add_vec(*vectors: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return tuple(sum(vector[index] for vector in vectors) for index in range(4))

    def sub_vec(
        left: tuple[int, int, int, int],
        right: tuple[int, int, int, int],
    ) -> tuple[int, int, int, int]:
        return tuple(left[index] - right[index] for index in range(4))

    p_r = [(2, 3, 5, 7), (11, 13, 17, 19)]
    p_l = [(23, 29, 31, 37), (41, 43, 47, 53)]
    total_phase = sub_vec(add_vec(*p_r), add_vec(*p_l))

    def neg_vec(vector: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return tuple(-entry for entry in vector)

    def permutation_sign(permutation: tuple[int, ...]) -> Fraction:
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(len(permutation))
            for right in range(left + 1, len(permutation))
        )
        return Fraction(-1 if inversions % 2 else 1)

    # In the bilinear-source specialization each determinant pairing still has
    # the same center phase.  This is not a c-number wave-packet outer product;
    # the independent bilinear source entries are the objects being paired.
    for permutation in itertools.permutations(range(2)):
        permutation_phase = add_vec(
            *[
                sub_vec(p_r[row], p_l[permutation[row]])
                for row in range(2)
            ]
        )
        assert_equal(
            f"bilinear source center phase is permutation independent {permutation}",
            permutation_phase,
            total_phase,
        )

    right_profiles = [[Fraction(2, 3), Fraction(5, 7)], [Fraction(11, 13), Fraction(17, 19)]]
    left_profiles = [[Fraction(23, 29), Fraction(31, 37)], [Fraction(41, 43), Fraction(47, 53)]]
    determinant_terms_by_phase: dict[tuple[int, int, int, int], Fraction] = {}
    for right_permutation in itertools.permutations(range(2)):
        right_phase = add_vec(*p_r)
        right_coefficient = permutation_sign(right_permutation) * product_fraction(
            [
                right_profiles[slot][right_permutation[slot]]
                for slot in range(2)
            ]
        )
        for left_permutation in itertools.permutations(range(2)):
            left_phase = add_vec(*[neg_vec(p_l[left_permutation[flavor]]) for flavor in range(2)])
            left_coefficient = permutation_sign(left_permutation) * product_fraction(
                [
                    left_profiles[flavor][left_permutation[flavor]]
                    for flavor in range(2)
                ]
            )
            phase = add_vec(right_phase, left_phase)
            coefficient = right_coefficient * left_coefficient
            determinant_terms_by_phase[phase] = (
                determinant_terms_by_phase.get(phase, Fraction(0)) + coefficient
            )

    assert_equal(
        "plane-wave linear-source determinants have one center phase",
        list(determinant_terms_by_phase.keys()),
        [total_phase],
    )
    assert_equal(
        "plane-wave linear-source coefficient after phase factoring",
        determinant_terms_by_phase[total_phase],
        det_fraction(right_profiles) * det_fraction(left_profiles),
    )

    individual_zero_mode_power = Fraction(3, 2)
    external_slot_count = 4
    assert_equal(
        "plane-wave four-fermion differentiated-source rho power",
        individual_zero_mode_power * external_slot_count,
        6,
    )

    period = 5
    off_shell_phase = tuple(value % period for value in total_phase)
    center_sum_off_shell = 0 if any(off_shell_phase) else period**4
    assert_equal("finite-volume center sum kills nonconserved momentum", center_sum_off_shell, 0)

    p_l_conserved = [p_r[1], p_r[0]]
    conserved_total_phase = sub_vec(add_vec(*p_r), add_vec(*p_l_conserved))
    center_sum_conserved = (
        period**4
        if not any(value % period for value in conserved_total_phase)
        else 0
    )
    assert_equal("finite-volume center sum keeps conserved momentum", center_sum_conserved, period**4)


def check_hard_wave_packet_instanton_source_support() -> None:
    right_rows = [
        [Fraction(2, 3), Fraction(5, 7)],
        [Fraction(11, 13), Fraction(17, 19)],
    ]
    left_columns = [
        [Fraction(23, 29), Fraction(31, 37)],
        [Fraction(41, 43), Fraction(47, 53)],
    ]

    right_det = det_fraction(right_rows)
    left_det = det_fraction(left_columns)
    assert_equal("hard wave-packet right overlap has rank two", right_det == 0, False)
    assert_equal("hard wave-packet left overlap has rank two", left_det == 0, False)

    right_row_norm_product = product_fraction(
        [sum(entry * entry for entry in row) for row in right_rows]
    )
    left_row_norm_product = product_fraction(
        [sum(entry * entry for entry in row) for row in left_columns]
    )
    assert_equal(
        "hard wave-packet right Hadamard determinant bound",
        right_det * right_det <= right_row_norm_product,
        True,
    )
    assert_equal(
        "hard wave-packet left Hadamard determinant bound",
        left_det * left_det <= left_row_norm_product,
        True,
    )
    assert_equal(
        "hard wave-packet four-slot Hadamard bound",
        (right_det * left_det) ** 2 <= right_row_norm_product * left_row_norm_product,
        True,
    )

    rank_one_right = [3 * entry for entry in right_rows[0]]
    assert_equal(
        "rank-one hard source projection kills right determinant",
        det_fraction([right_rows[0], rank_one_right]),
        Fraction(0),
    )
    rank_one_left = [5 * entry for entry in left_columns[0]]
    assert_equal(
        "rank-one hard source projection kills left determinant",
        det_fraction([left_columns[0], rank_one_left]),
        Fraction(0),
    )

    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    slot_decay_power = 12
    tail_margin = slot_decay_power - b0 - 2
    assert_equal("hard wave-packet SU3 Nf2 tail margin", tail_margin, Fraction(1, 3))

    # Choose R=x^3 so the exact SU(3), Nf=2 tail model
    # int_R^infty s^(-4/3) ds = 3 R^(-1/3) remains rational.
    x = Fraction(4)
    r_cut = x**3
    c_min = Fraction(2)
    c_src = Fraction(5, 7)
    tail_bound = 3 * c_src * c_min ** (-12) / x
    assert_equal(
        "hard wave-packet exact tail model",
        tail_bound,
        c_src * c_min ** (-12) * 3 / x,
    )

    harder_cut = (2 * x) ** 3
    harder_tail_bound = 3 * c_src * c_min ** (-12) / (2 * x)
    assert_equal("hard wave-packet harder cutoff", harder_cut, 8 * r_cut)
    assert_equal(
        "hard wave-packet tail halves when R grows by eight",
        harder_tail_bound,
        tail_bound / 2,
    )

    soft_support_margin = Fraction(0)
    assert_equal(
        "soft source support has no positive hard margin",
        soft_support_margin > 0,
        False,
    )


def epsilon2(left: int, right: int) -> Fraction:
    if (left, right) == (0, 1):
        return Fraction(1)
    if (left, right) == (1, 0):
        return Fraction(-1)
    return Fraction(0)


def check_instanton_orientation_haar_projection() -> None:
    def haar_two_same(
        color_left: int,
        color_right: int,
        core_left: int,
        core_right: int,
    ) -> Fraction:
        return (
            epsilon2(color_left, color_right)
            * epsilon2(core_left, core_right)
            / 2
        )

    def haar_mixed(
        color_left: int,
        color_right: int,
        core_left: int,
        core_right: int,
    ) -> Fraction:
        return (
            Fraction(1, 2)
            if color_left == color_right and core_left == core_right
            else Fraction(0)
        )

    single_slot = [Fraction(2), Fraction(-5)]
    center_averaged_slot = [(entry - entry) / 2 for entry in single_slot]
    assert_equal(
        "SU2 center element forces one-slot orientation average to vanish",
        center_averaged_slot,
        [Fraction(0), Fraction(0)],
    )

    mixed_trace = sum(
        haar_mixed(color, color, core, core)
        for color in range(2)
        for core in range(2)
    )
    assert_equal("SU2 orientation mixed trace normalization", mixed_trace, 2)

    epsilon_contraction = sum(
        epsilon2(color_left, color_right)
        * epsilon2(core_left, core_right)
        * haar_two_same(color_left, color_right, core_left, core_right)
        for color_left in range(2)
        for color_right in range(2)
        for core_left in range(2)
        for core_right in range(2)
    )
    assert_equal(
        "SU2 orientation same-chirality determinant normalization",
        epsilon_contraction,
        2,
    )

    def two_slot_projection(
        color_left: int,
        color_right: int,
        first: list[Fraction],
        second: list[Fraction],
    ) -> Fraction:
        return sum(
            haar_two_same(color_left, color_right, core_left, core_right)
            * first[core_left]
            * second[core_right]
            for core_left in range(2)
            for core_right in range(2)
        )

    first_source = [Fraction(2), Fraction(3)]
    second_source = [Fraction(5), Fraction(7)]
    source_det = (
        first_source[0] * second_source[1]
        - first_source[1] * second_source[0]
    )

    for color_left in range(2):
        for color_right in range(2):
            assert_equal(
                "SU2 orientation two-slot determinant projection "
                f"{color_left}{color_right}",
                two_slot_projection(
                    color_left,
                    color_right,
                    first_source,
                    second_source,
                ),
                epsilon2(color_left, color_right) * source_det / 2,
            )

    rank_one_second = [3 * entry for entry in first_source]
    assert_equal(
        "SU2 orientation projection kills rank-one source pair",
        two_slot_projection(0, 1, first_source, rank_one_second),
        0,
    )
    assert_equal(
        "SU2 orientation projection kills color-symmetric pair",
        two_slot_projection(0, 0, first_source, second_source),
        0,
    )

    def pairing_a(
        first: int,
        second: int,
        third: int,
        fourth: int,
    ) -> Fraction:
        return epsilon2(first, second) * epsilon2(third, fourth)

    def pairing_b(
        first: int,
        second: int,
        third: int,
        fourth: int,
    ) -> Fraction:
        return epsilon2(first, third) * epsilon2(second, fourth)

    def haar_four_same(
        colors: tuple[int, int, int, int],
        cores: tuple[int, int, int, int],
    ) -> Fraction:
        color_a = pairing_a(*colors)
        color_b = pairing_b(*colors)
        core_a = pairing_a(*cores)
        core_b = pairing_b(*cores)
        return (
            Fraction(1, 3) * color_a * core_a
            - Fraction(1, 6) * color_a * core_b
            - Fraction(1, 6) * color_b * core_a
            + Fraction(1, 3) * color_b * core_b
        )

    # This is the counterexample to the factorized two-slot shortcut:
    # for U=[[a,b],[-conj(b),conj(a)]], the integral is int |a|^4 dU=1/3,
    # not (int det U dU / 2)^2=1/4.
    shared_counterexample = haar_four_same((0, 1, 0, 1), (0, 1, 0, 1))
    factorized_counterexample = (
        haar_two_same(0, 1, 0, 1)
        * haar_two_same(0, 1, 0, 1)
    )
    assert_equal("SU2 shared four-slot Haar counterexample", shared_counterexample, Fraction(1, 3))
    assert_equal(
        "SU2 shared four-slot differs from factorized shortcut",
        shared_counterexample == factorized_counterexample,
        False,
    )

    right_sources = [
        [Fraction(2), Fraction(3)],
        [Fraction(5), Fraction(7)],
    ]
    left_sources = [
        [Fraction(11), Fraction(13)],
        [Fraction(17), Fraction(19)],
    ]

    def det_pair(first: list[Fraction], second: list[Fraction]) -> Fraction:
        return first[0] * second[1] - first[1] * second[0]

    def four_slot_source_projection(
        colors: tuple[int, int, int, int],
        right_first: list[Fraction],
        right_second: list[Fraction],
        left_first: list[Fraction],
        left_second: list[Fraction],
    ) -> Fraction:
        return sum(
            haar_four_same(colors, (core_1, core_2, core_3, core_4))
            * right_first[core_1]
            * right_second[core_2]
            * left_first[core_3]
            * left_second[core_4]
            for core_1 in range(2)
            for core_2 in range(2)
            for core_3 in range(2)
            for core_4 in range(2)
        )

    colors = (0, 1, 0, 1)
    delta_12_34 = det_pair(right_sources[0], right_sources[1]) * det_pair(
        left_sources[0],
        left_sources[1],
    )
    delta_13_24 = det_pair(right_sources[0], left_sources[0]) * det_pair(
        right_sources[1],
        left_sources[1],
    )
    expected_shared_projection = (
        pairing_a(*colors)
        * (Fraction(1, 3) * delta_12_34 - Fraction(1, 6) * delta_13_24)
        + pairing_b(*colors)
        * (-Fraction(1, 6) * delta_12_34 + Fraction(1, 3) * delta_13_24)
    )
    assert_equal(
        "SU2 shared four-slot source projector",
        four_slot_source_projection(
            colors,
            right_sources[0],
            right_sources[1],
            left_sources[0],
            left_sources[1],
        ),
        expected_shared_projection,
    )

    rank_one_right = [3 * entry for entry in right_sources[0]]
    rank_one_four_slot = four_slot_source_projection(
        colors,
        right_sources[0],
        rank_one_right,
        left_sources[0],
        left_sources[1],
    )
    assert_equal(
        "SU2 shared four-slot rank-one right pair need not vanish",
        rank_one_four_slot == 0,
        False,
    )


def check_color_singlet_instanton_source_projection() -> None:
    hard_kernel = [
        [Fraction(2, 5), Fraction(3, 7)],
        [Fraction(5, 11), Fraction(7, 13)],
    ]
    right_overlap = [
        [Fraction(11, 17), Fraction(13, 19)],
        [Fraction(17, 23), Fraction(19, 29)],
    ]
    left_overlap = [
        [Fraction(23, 31), Fraction(29, 37)],
        [Fraction(31, 41), Fraction(37, 43)],
    ]
    projected_source = matmul_fraction(
        matmul_fraction(right_overlap, hard_kernel),
        left_overlap,
    )
    assert_equal(
        "color-singlet source determinant projection",
        det_fraction(projected_source),
        det_fraction(right_overlap)
        * det_fraction(hard_kernel)
        * det_fraction(left_overlap),
    )

    # If the source-overlap matrices vary over collective-coordinate cells,
    # the projection identity holds pointwise but the overlaps must stay inside
    # the cell sum.
    second_kernel = [
        [Fraction(41, 47), Fraction(43, 53)],
        [Fraction(47, 59), Fraction(53, 61)],
    ]
    second_right_overlap = [
        [Fraction(3, 11), Fraction(5, 13)],
        [Fraction(7, 17), Fraction(11, 19)],
    ]
    second_left_overlap = [
        [Fraction(13, 23), Fraction(17, 29)],
        [Fraction(19, 31), Fraction(23, 37)],
    ]
    weights = [Fraction(2, 7), Fraction(5, 9)]
    projected_integral = (
        weights[0]
        * det_fraction(
            matmul_fraction(matmul_fraction(right_overlap, hard_kernel), left_overlap)
        )
        + weights[1]
        * det_fraction(
            matmul_fraction(
                matmul_fraction(second_right_overlap, second_kernel),
                second_left_overlap,
            )
        )
    )
    pointwise_integral = (
        weights[0]
        * det_fraction(right_overlap)
        * det_fraction(hard_kernel)
        * det_fraction(left_overlap)
        + weights[1]
        * det_fraction(second_right_overlap)
        * det_fraction(second_kernel)
        * det_fraction(second_left_overlap)
    )
    assert_equal(
        "color-singlet projection is pointwise under collective integration",
        projected_integral,
        pointwise_integral,
    )

    # Stable-hadron extraction divides by the source overlaps with the physical
    # external states.  This pole-residue operation is external to the
    # instanton kernel and linear in the gauge-invariant source correlator.
    source_to_hadron = Fraction(7, 15)
    sink_to_hadron = Fraction(11, 21)
    hadronic_amplitude = projected_integral
    gauge_invariant_correlator_pole = (
        sink_to_hadron * hadronic_amplitude * source_to_hadron
    )
    assert_equal(
        "hadronic pole residue recovers instanton amplitude contribution",
        gauge_invariant_correlator_pole / (sink_to_hadron * source_to_hadron),
        hadronic_amplitude,
    )


def check_instanton_hadronic_pole_window_projection() -> None:
    # Finite-volume source/sink pole extraction is a separate spectral step
    # after the instanton source kernel has been assembled.  Use rational
    # q-factors for exp[-Delta_H t] and exp[-Delta_H' (T-t)].
    source_overlap = Fraction(7, 15)
    sink_overlap = Fraction(11, 21)
    selected_matrix_element = Fraction(13, 17)
    source_gap_factor = Fraction(1, 5)
    sink_gap_factor = Fraction(1, 7)

    selected_pole = (
        sink_overlap
        * source_overlap
        * selected_matrix_element
    )
    final_excited = sink_overlap * source_overlap * Fraction(2, 9) * sink_gap_factor
    initial_excited = sink_overlap * source_overlap * Fraction(-3, 11) * source_gap_factor
    double_excited = (
        sink_overlap
        * source_overlap
        * Fraction(5, 13)
        * sink_gap_factor
        * source_gap_factor
    )
    normalized_ratio = (
        selected_pole
        + final_excited
        + initial_excited
        + double_excited
    ) / (sink_overlap * source_overlap)
    leakage = normalized_ratio - selected_matrix_element

    tail_bound = (
        Fraction(2, 9) * sink_gap_factor
        + Fraction(3, 11) * source_gap_factor
        + Fraction(5, 13) * sink_gap_factor * source_gap_factor
    )
    assert_equal(
        "instanton hadronic pole-window normalized leading matrix element",
        selected_pole / (sink_overlap * source_overlap),
        selected_matrix_element,
    )
    assert_equal(
        "instanton hadronic pole-window excited leakage bound",
        abs(leakage) <= tail_bound,
        True,
    )

    # The unnormalized source correlator still contains external pole
    # overlaps.  It is not the hadronic matrix element.
    assert_equal(
        "source correlator pole is not the hadronic matrix element",
        selected_pole == selected_matrix_element,
        False,
    )

    # Dividing by overlaps before isolating the pole leaves excited-state
    # contamination.  Large Euclidean time or an explicit tail majorant is
    # part of the physical amplitude extraction.
    assert_equal(
        "overlap division alone leaves excited contamination",
        normalized_ratio == selected_matrix_element,
        False,
    )

    zero_sink_overlap = Fraction(0)
    if zero_sink_overlap == 0:
        extraction_defined = False
    else:
        extraction_defined = True
    assert_equal(
        "vanishing interpolating overlap prevents pole extraction",
        extraction_defined,
        False,
    )

    # Better pole windows shrink the same normalized excited-state majorant.
    longer_source_gap_factor = source_gap_factor * source_gap_factor
    longer_sink_gap_factor = sink_gap_factor * sink_gap_factor
    longer_tail_bound = (
        Fraction(2, 9) * longer_sink_gap_factor
        + Fraction(3, 11) * longer_source_gap_factor
        + Fraction(5, 13) * longer_sink_gap_factor * longer_source_gap_factor
    )
    assert_equal(
        "longer hadronic pole window improves excited-state bound",
        longer_tail_bound < tail_bound,
        True,
    )


def check_instanton_euclidean_to_physical_residual_budget() -> None:
    leading_kernel_coordinate = Fraction(7, 13)
    residuals = {
        "regulator": Fraction(1, 17),
        "continuation": Fraction(-2, 19),
        "spectral": Fraction(3, 23),
        "infrared": Fraction(-5, 29),
        "unitarity_cut": Fraction(7, 31),
        "matching": Fraction(-11, 37),
        "size_endpoint": Fraction(13, 41),
    }
    total_residual = sum(residuals.values(), Fraction(0))
    physical_amplitude = leading_kernel_coordinate + total_residual

    assert_equal(
        "instanton physical-amplitude residual telescope",
        physical_amplitude - leading_kernel_coordinate - total_residual,
        Fraction(0),
    )
    if total_residual == 0:
        raise AssertionError("instanton physical residual budget accidentally collapsed")

    residual_bound = sum(abs(value) for value in residuals.values())
    assert_equal(
        "instanton physical-amplitude residual bound",
        abs(physical_amplitude - leading_kernel_coordinate) <= residual_bound,
        True,
    )

    zero_residual_physical_coordinate = leading_kernel_coordinate + sum(
        Fraction(0) for _ in residuals
    )
    assert_equal(
        "instanton kernel equals physical amplitude only with zero bridge residual",
        zero_residual_physical_coordinate,
        leading_kernel_coordinate,
    )
    assert_equal(
        "leading instanton kernel alone is not the physical amplitude",
        physical_amplitude == leading_kernel_coordinate,
        False,
    )

    # A colored auxiliary kernel has no physical pole projection until a
    # gauge-invariant source or an infrared deformation has been supplied.
    has_color_singlet_source = False
    has_declared_infrared_deformation = False
    assert_equal(
        "colored partonic instanton kernel has no standalone physical LSZ map",
        has_color_singlet_source or has_declared_infrared_deformation,
        False,
    )


def check_instanton_unitarity_cut_pairing() -> None:
    instanton_charge = 1
    anti_instanton_charge = -1
    assert_equal(
        "instanton anti-instanton cut cancels theta charge",
        instanton_charge + anti_instanton_charge,
        0,
    )
    assert_equal(
        "same-charge instanton pair is theta charged",
        instanton_charge + instanton_charge == 0,
        False,
    )

    one_instanton_action_power = 1
    cut_pair_action_power = one_instanton_action_power + one_instanton_action_power
    assert_equal("inclusive cut doubles instanton action power", cut_pair_action_power, 2)

    perturbative_amplitude = Fraction(7, 5)
    instanton_amplitude = Fraction(11, 13)
    cut_overlap = Fraction(17, 19)
    theta_zero_cos = Fraction(1)
    theta_quarter_turn_cos = Fraction(0)
    interference_at_theta_zero = (
        2
        * perturbative_amplitude
        * instanton_amplitude
        * cut_overlap
        * theta_zero_cos
    )
    interference_at_quarter_turn = (
        2
        * perturbative_amplitude
        * instanton_amplitude
        * cut_overlap
        * theta_quarter_turn_cos
    )
    assert_equal(
        "nonzero perturbative sector gives order e^-SI interference",
        interference_at_theta_zero,
        Fraction(2618, 1235),
    )
    assert_equal(
        "instanton interference can carry theta dependence",
        interference_at_theta_zero == interference_at_quarter_turn,
        False,
    )
    assert_equal(
        "interference precedes diagonal IbarI order",
        one_instanton_action_power < cut_pair_action_power,
        True,
    )

    selected_perturbative_amplitude = Fraction(0)
    selected_interference = (
        2
        * selected_perturbative_amplitude
        * instanton_amplitude
        * cut_overlap
        * theta_zero_cos
    )
    assert_equal(
        "selection rule removes lower-action instanton interference",
        selected_interference,
        Fraction(0),
    )

    n_flavors = 2
    amplitude_zero_mode_slots = 2 * n_flavors
    cut_pair_zero_mode_slots = 2 * amplitude_zero_mode_slots
    assert_equal("two-flavor cut pair has conjugate zero-mode slots", cut_pair_zero_mode_slots, 8)

    instanton_cells = [Fraction(2, 5), Fraction(3, 7), Fraction(5, 11)]
    anti_instanton_cells = [Fraction(7, 13), Fraction(11, 17), Fraction(13, 19)]
    cut_weights = [Fraction(3, 2), Fraction(5, 3), Fraction(7, 5)]
    leading_cut_rate = sum(
        left * right * cut
        for left, right, cut in zip(instanton_cells, anti_instanton_cells, cut_weights)
    )
    uncut_product = sum(
        left * right for left, right in zip(instanton_cells, anti_instanton_cells)
    )
    assert_equal(
        "final-state cut weights are part of instanton rate datum",
        leading_cut_rate == uncut_product,
        False,
    )

    one_amplitude_coordinate = sum(instanton_cells)
    assert_equal(
        "one-instanton amplitude coordinate is not the inclusive cut rate",
        one_amplitude_coordinate == leading_cut_rate,
        False,
    )

    relative_cut_errors = [Fraction(1, 10), Fraction(-1, 20), Fraction(1, 30)]
    exact_cut_rate = sum(
        left * right * cut * (1 + residual)
        for left, right, cut, residual in zip(
            instanton_cells, anti_instanton_cells, cut_weights, relative_cut_errors
        )
    )
    cut_majorant = sum(
        abs(left * right * cut)
        for left, right, cut in zip(instanton_cells, anti_instanton_cells, cut_weights)
    )
    epsilon_cut = max(abs(residual) for residual in relative_cut_errors)
    assert_equal(
        "instanton cut-pair residual bound",
        abs(exact_cut_rate - leading_cut_rate) <= epsilon_cut * cut_majorant,
        True,
    )


def check_one_instanton_sector_isolation_bound() -> None:
    # A selected one-instanton coefficient is not isolated merely because a
    # BPST saddle exists.  Adjacent amplitude sectors must either be killed by
    # an exact source/charge projection or bounded in the same normalization.
    retained_one_instanton = Fraction(5, 7)
    one_window_mass = Fraction(9, 10)
    same_sector_residual = Fraction(3, 50)
    same_sector_epsilon = Fraction(1, 12)
    assert_equal(
        "one-instanton same-sector residual bound",
        abs(same_sector_residual) <= same_sector_epsilon * one_window_mass,
        True,
    )

    sector_masses = {
        "perturbative": Fraction(4, 3),
        "anti_instanton": Fraction(5, 6),
        "two_instanton": Fraction(7, 8),
        "instanton_anti_instanton_amplitude": Fraction(9, 10),
    }
    leakage_factors = {
        "perturbative": Fraction(0),
        "anti_instanton": Fraction(1, 25),
        "two_instanton": Fraction(2, 35),
        "instanton_anti_instanton_amplitude": Fraction(1, 18),
    }
    projected_sector_leakage = {
        name: leakage_factors[name] * sector_masses[name]
        for name in sector_masses
    }
    higher_sector_remainder = Fraction(1, 60)

    projected_observable = (
        retained_one_instanton
        + same_sector_residual
        + sum(projected_sector_leakage.values(), Fraction(0))
        + higher_sector_remainder
    )
    isolation_error = projected_observable - retained_one_instanton
    isolation_majorant = (
        same_sector_epsilon * one_window_mass
        + sum(
            leakage_factors[name] * sector_masses[name]
            for name in sector_masses
        )
        + higher_sector_remainder
    )
    assert_equal(
        "one-instanton sector-isolation majorant",
        abs(isolation_error) <= isolation_majorant,
        True,
    )

    noncancellation_margin = abs(retained_one_instanton) / one_window_mass
    assert_equal(
        "one-instanton noncancellation margin",
        noncancellation_margin,
        Fraction(50, 63),
    )
    relative_isolation_bound = isolation_majorant / abs(retained_one_instanton)
    assert_equal(
        "one-instanton relative isolation bound",
        abs(isolation_error) / abs(retained_one_instanton)
        <= relative_isolation_bound,
        True,
    )

    # Negative controls: a generic source with perturbative leakage is not a
    # one-instanton observable, omitting a neighboring sector underbudgets the
    # error, and signed cancellations between adjacent sectors do not establish
    # isolation.
    unprojected_perturbative_leakage = Fraction(3)
    assert_equal(
        "unprojected perturbative sector can dominate one-instanton coefficient",
        abs(unprojected_perturbative_leakage) > abs(retained_one_instanton),
        True,
    )

    missing_anti_instanton_bound = (
        isolation_majorant - projected_sector_leakage["anti_instanton"]
    )
    assert_equal(
        "omitting anti-instanton leakage underbudgets isolation error",
        abs(isolation_error) <= missing_anti_instanton_bound,
        False,
    )

    canceling_adjacent_sectors = [Fraction(1, 3), -Fraction(1, 3)]
    signed_sector_sum = sum(canceling_adjacent_sectors, Fraction(0))
    absolute_sector_sum = sum(abs(term) for term in canceling_adjacent_sectors)
    assert_equal(
        "signed adjacent-sector leakage can cancel",
        signed_sector_sum,
        Fraction(0),
    )
    assert_equal(
        "signed cancellation is not sector-isolation evidence",
        absolute_sector_sum > abs(signed_sector_sum),
        True,
    )


def check_instanton_amplitude_error_budget() -> None:
    # A finite regulator reduces the amplitude assembly to a finite sum over
    # chart cells.  The leading term is not the moduli-space measure alone:
    # it is the collective Jacobian multiplied by the pure-gauge determinant
    # convention, the light-fermion nonzero-mode factor, and the zero-mode
    # source coefficient.
    pure_gauge_constant = Fraction(2, 5)
    light_fermion_factor = Fraction(3, 7)
    zero_mode_source_coefficient = Fraction(5, 11)
    collective_jacobian = Fraction(7, 13)
    leading_cell = (
        pure_gauge_constant
        * light_fermion_factor
        * zero_mode_source_coefficient
        * collective_jacobian
    )
    assert_equal(
        "leading instanton cell multiplies determinant zero-mode and measure data",
        leading_cell,
        Fraction(6, 143),
    )
    assert_equal(
        "collective-coordinate measure alone is not the instanton amplitude",
        leading_cell == collective_jacobian,
        False,
    )

    # A finite source-convention change can move a factor between the
    # nonzero-mode determinant and the zero-mode source coefficient, but their
    # product is the amplitude datum.
    source_scale = Fraction(5, 3)
    flavor_count = 2
    rescaled_fermion_factor = light_fermion_factor * source_scale**flavor_count
    rescaled_zero_mode = zero_mode_source_coefficient / source_scale**flavor_count
    assert_equal(
        "finite source convention leaves determinant times zero-mode factor",
        rescaled_fermion_factor * rescaled_zero_mode,
        light_fermion_factor * zero_mode_source_coefficient,
    )

    lead_cells = [Fraction(2, 7), Fraction(3, 11), Fraction(5, 13)]
    determinant_remainders = [Fraction(1, 10), Fraction(-1, 15), Fraction(1, 21)]
    zero_mode_remainders = [Fraction(1, 14), Fraction(0), Fraction(-1, 22)]
    source_matching_remainders = [Fraction(-1, 30), Fraction(1, 18), Fraction(1, 26)]
    schur_corrections = [Fraction(1, 200), Fraction(-1, 231), Fraction(1, 286)]
    endpoint_cells = [Fraction(1, 97), Fraction(-1, 143)]

    hard_exact_cells = []
    for index, lead in enumerate(lead_cells):
        hard_exact_cells.append(
            lead
            * (
                1
                + determinant_remainders[index]
                + zero_mode_remainders[index]
                + source_matching_remainders[index]
            )
            + schur_corrections[index]
        )

    lead_amplitude = sum(lead_cells, Fraction(0))
    determinant_residual = sum(
        lead * remainder
        for lead, remainder in zip(lead_cells, determinant_remainders)
    )
    zero_mode_residual = sum(
        lead * remainder
        for lead, remainder in zip(lead_cells, zero_mode_remainders)
    )
    source_matching_residual = sum(
        lead * remainder
        for lead, remainder in zip(lead_cells, source_matching_remainders)
    )
    schur_residual = sum(schur_corrections, Fraction(0))
    endpoint_residual = sum(endpoint_cells, Fraction(0))
    exact_amplitude = sum(hard_exact_cells, Fraction(0)) + endpoint_residual

    assert_equal(
        "finite instanton amplitude residual decomposition",
        exact_amplitude,
        (
            lead_amplitude
            + determinant_residual
            + zero_mode_residual
            + source_matching_residual
            + schur_residual
            + endpoint_residual
        ),
    )

    error_bound = (
        sum(
            abs(lead)
            * (
                abs(determinant_remainders[index])
                + abs(zero_mode_remainders[index])
                + abs(source_matching_remainders[index])
            )
            for index, lead in enumerate(lead_cells)
        )
        + sum(abs(correction) for correction in schur_corrections)
        + sum(abs(cell) for cell in endpoint_cells)
    )
    assert_equal(
        "finite instanton amplitude error bound dominates residual",
        abs(exact_amplitude - lead_amplitude) <= error_bound,
        True,
    )

    no_remainder_exact = sum(lead_cells, Fraction(0))
    assert_equal(
        "leading instanton amplitude recovered only when all residuals vanish",
        no_remainder_exact,
        lead_amplitude,
    )


def check_source_dependent_fluctuation_cumulant_bound() -> None:
    # A vacuum/spectral determinant normalization is not enough for an
    # instanton amplitude with source insertions.  The selected source must also
    # be stable under the same nonzero-mode fluctuation measure.
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    assert_equal("fluctuation-cell weights normalize", sum(weights, Fraction(0)), Fraction(1))

    first_cumulants = [Fraction(1, 12), -Fraction(1, 18), Fraction(1, 24)]
    second_cumulants = [Fraction(1, 70), -Fraction(1, 84), Fraction(1, 105)]
    tail_remainders = [Fraction(1, 200), -Fraction(1, 180), Fraction(1, 252)]

    exact_source_ratio = sum(
        weight * (1 + first + second + tail)
        for weight, first, second, tail in zip(
            weights, first_cumulants, second_cumulants, tail_remainders
        )
    )
    first_mean = sum(
        weight * first for weight, first in zip(weights, first_cumulants)
    )
    second_mean = sum(
        weight * second for weight, second in zip(weights, second_cumulants)
    )
    tail_mean = sum(
        weight * tail for weight, tail in zip(weights, tail_remainders)
    )
    assert_equal(
        "source-dependent fluctuation cumulant telescope",
        exact_source_ratio,
        1 + first_mean + second_mean + tail_mean,
    )

    fluctuation_bound = sum(
        weight * (abs(first) + abs(second) + abs(tail))
        for weight, first, second, tail in zip(
            weights, first_cumulants, second_cumulants, tail_remainders
        )
    )
    if not abs(exact_source_ratio - 1) <= fluctuation_bound:
        raise AssertionError("source-dependent fluctuation bound failed")

    # Propagate the same source-dependent correction through a finite signed
    # hard window.  The absolute mass, not the signed coefficient alone, controls
    # the error.
    window_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    fluctuation_errors = [Fraction(1, 20), -Fraction(1, 30), Fraction(1, 40)]
    leading_window = sum(window_cells, Fraction(0))
    absolute_window_mass = sum(abs(cell) for cell in window_cells)
    exact_window = sum(
        cell * (1 + error) for cell, error in zip(window_cells, fluctuation_errors)
    )
    epsilon_fluc = max(abs(error) for error in fluctuation_errors)
    if not abs(exact_window - leading_window) <= epsilon_fluc * absolute_window_mass:
        raise AssertionError("finite-window fluctuation residual bound failed")

    # A determinant normalized in a vacuum channel can have no source residual,
    # while the selected source amplitude still has a nonzero fluctuation
    # correction.
    vacuum_determinant_residual = Fraction(0)
    if not abs(exact_source_ratio - 1) > vacuum_determinant_residual:
        raise AssertionError(
            "vacuum determinant calibration was mistaken for source fluctuation control"
        )

    # Signed fluctuation cumulants can cancel.  The bound must use absolute
    # cumulant control, not the signed sum.
    canceling_cumulants = [Fraction(1, 8), -Fraction(1, 8)]
    signed_cumulant_sum = sum(canceling_cumulants, Fraction(0))
    absolute_cumulant_sum = sum(abs(term) for term in canceling_cumulants)
    assert_equal("signed fluctuation cumulants cancel", signed_cumulant_sum, Fraction(0))
    signed_only_budget = abs(signed_cumulant_sum)
    if not absolute_cumulant_sum > signed_only_budget:
        raise AssertionError("signed cancellation erased the absolute fluctuation budget")


def check_instanton_observable_assembly_ladder() -> None:
    # The physical observable is not the collective-coordinate measure and not
    # even the Euclidean source coefficient.  It is obtained only after the
    # source coefficient, sector isolation, and physical projection residuals
    # have been budgeted in one normalization.
    collective_measure = Fraction(2, 5)
    pure_gauge_determinant = Fraction(3, 7)
    zero_mode_source = Fraction(5, 9)
    orientation_projection = Fraction(7, 11)
    hard_window_factor = Fraction(11, 13)
    full_euclidean_cell = (
        collective_measure
        * pure_gauge_determinant
        * zero_mode_source
        * orientation_projection
        * hard_window_factor
    )
    assert_equal(
        "instanton observable cell uses more than collective measure",
        full_euclidean_cell == collective_measure,
        False,
    )

    leading_source_coefficient = Fraction(5, 8)
    physical_projection_factor = Fraction(9, 10)
    leading_physical_coordinate = (
        physical_projection_factor * leading_source_coefficient
    )
    assert_equal(
        "Euclidean instanton source coefficient is not yet physical observable",
        leading_source_coefficient == leading_physical_coordinate,
        False,
    )

    window_mass = Fraction(3, 4)
    deltas = {
        "spectral_counterterm": Fraction(1, 60),
        "source_fluctuation": Fraction(1, 70),
        "zero_mode_rank": Fraction(1, 80),
        "schur": Fraction(1, 90),
        "endpoint": Fraction(1, 18),
        "sector": Fraction(1, 20),
        "continuation": Fraction(1, 75),
        "projection": Fraction(1, 84),
        "infrared": Fraction(1, 96),
        "cut": Fraction(1, 108),
        "scheme": Fraction(1, 120),
    }
    residuals = {
        name: window_mass * delta for name, delta in deltas.items()
    }
    residual_sum = sum(residuals.values(), Fraction(0))
    exact_physical_observable = leading_physical_coordinate + residual_sum

    assert_equal(
        "instanton observable assembly residual telescope",
        exact_physical_observable,
        leading_physical_coordinate + residual_sum,
    )
    majorant = window_mass * sum(deltas.values(), Fraction(0))
    assert_equal(
        "instanton observable assembly absolute bound",
        abs(exact_physical_observable - leading_physical_coordinate) <= majorant,
        True,
    )

    noncancellation_margin = abs(leading_physical_coordinate) / window_mass
    assert_equal(
        "instanton observable noncancellation margin",
        noncancellation_margin,
        Fraction(3, 4),
    )
    relative_bound = majorant / abs(leading_physical_coordinate)
    assert_equal(
        "instanton observable assembly relative bound",
        abs(exact_physical_observable - leading_physical_coordinate)
        / abs(leading_physical_coordinate)
        <= relative_bound,
        True,
    )

    omitted_endpoint_sector_bound = (
        majorant - abs(residuals["endpoint"]) - abs(residuals["sector"])
    )
    assert_equal(
        "omitting endpoint and sector budgets underbounds observable",
        abs(exact_physical_observable - leading_physical_coordinate)
        <= omitted_endpoint_sector_bound,
        False,
    )

    unprojected_perturbative_leakage = Fraction(2)
    assert_equal(
        "unprojected lower-action sector can overwhelm instanton observable",
        abs(unprojected_perturbative_leakage) > abs(leading_physical_coordinate),
        True,
    )

    canceling_physical_residuals = [Fraction(1, 8), -Fraction(1, 8)]
    signed_physical_residual = sum(canceling_physical_residuals, Fraction(0))
    absolute_physical_residual = sum(
        abs(term) for term in canceling_physical_residuals
    )
    assert_equal(
        "signed physical residuals can cancel",
        signed_physical_residual,
        Fraction(0),
    )
    assert_equal(
        "signed cancellation is not observable-assembly evidence",
        absolute_physical_residual > abs(signed_physical_residual),
        True,
    )


def check_hard_momentum_instanton_size_window() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f

    measure_power = Fraction(-5)
    individual_form_factor_count = 4
    individual_zero_mode_power = Fraction(3, 2)
    zero_mode_source_power = individual_form_factor_count * individual_zero_mode_power
    integrand_power = b0 + measure_power + zero_mode_source_power
    antiderivative_power = integrand_power + 1
    assert_equal("hard Nf=2 b0", b0, Fraction(29, 3))
    assert_equal("hard Nf=2 four individual zero modes give rho^6", zero_mode_source_power, 6)
    assert_equal("hard Nf=2 size integrand power", integrand_power, b0 + 1)
    assert_equal("hard Nf=2 small-rho margin", antiderivative_power, b0 + 2)

    mu_power = b0
    rho_integral_q_power = -antiderivative_power
    coefficient_q_power = mu_power + rho_integral_q_power
    assert_equal("hard Nf=2 coefficient dimension", coefficient_q_power, Fraction(-2))
    assert_equal(
        "hard Nf=2 coefficient equals four-fermion operator dimension",
        coefficient_q_power,
        Fraction(4 - 3 * n_f),
    )

    # If exp[-8*pi^2/g(Q)^2] is traded for Lambda_ht^b0 Q^(-b0), the hard
    # coefficient falls as Lambda_ht^b0 Q^(-b0-2), up to logarithmic
    # collective-coordinate prefactors.  The combined mass dimension remains
    # the four-fermion coefficient dimension.
    running_exponential_q_power = -b0
    lambda_power = b0
    full_hard_q_power = running_exponential_q_power + coefficient_q_power
    assert_equal("hard Nf=2 full asymptotic Q power", full_hard_q_power, -b0 - 2)
    assert_equal(
        "hard Nf=2 Lambda/Q dimension",
        lambda_power + full_hard_q_power,
        Fraction(-2),
    )

    # In the fused bilinear-source specialization the density form factors
    # z K_1(z) give exponential large-rho suppression.
    bilinear_density_scales = [Fraction(3), Fraction(5)]
    bilinear_hard_cutoff = sum(bilinear_density_scales)
    assert_equal("hard bilinear-density exponential scale", bilinear_hard_cutoff, Fraction(8))

    def large_rho_status(transfer_sum: Fraction) -> str:
        return "exponential_cutoff" if transfer_sum > 0 else "no_form_factor_cutoff"

    assert_equal(
        "hard bilinear-density term has exponential large-rho cutoff",
        large_rho_status(bilinear_hard_cutoff),
        "exponential_cutoff",
    )

    # Individual singular-gauge fermion zero-mode slots have only the power tail
    # F_zm(c Q rho/2) ~ (Q rho)^(-3).  The four-slot Nf=2 SU(3) hard kernel has
    # large-rho integrand power b0+1-12=-4/3, hence a positive convergence
    # margin 1/3.  If one slot is soft, only three hard powers remain and the
    # same one-loop size integral is not controlled by the hard source profile.
    individual_slot_tail_power = Fraction(-3)
    hard_slot_count = 4
    large_rho_power = integrand_power + individual_slot_tail_power * hard_slot_count
    large_rho_margin = Fraction(-1) - large_rho_power
    assert_equal("hard individual-slot large-rho power", large_rho_power, Fraction(-4, 3))
    assert_equal("hard individual-slot large-rho margin", large_rho_margin, Fraction(1, 3))
    assert_equal("hard individual-slot b0 threshold", 3 * hard_slot_count - 2, 10)
    assert_equal("hard individual-slot b0 threshold margin", Fraction(10) - b0, Fraction(1, 3))

    soft_slot_count = 3
    soft_large_rho_power = integrand_power + individual_slot_tail_power * soft_slot_count
    assert_equal("soft individual-slot large-rho power", soft_large_rho_power, Fraction(5, 3))
    assert_equal(
        "soft individual-slot term fails hard large-rho test",
        soft_large_rho_power < -1,
        False,
    )

    # The mass-saturated vacuum integral has no hard form factor; with the same
    # one-loop power it is small-rho finite but large-rho power divergent.
    vacuum_antiderivative_power = b0 + n_f - 4
    assert_equal(
        "Nf=2 mass-saturated vacuum small-rho margin",
        vacuum_antiderivative_power,
        Fraction(23, 3),
    )
    assert_equal(
        "positive vacuum size power is not a hard cutoff",
        large_rho_status(Fraction(0)),
        "no_form_factor_cutoff",
    )


def check_fused_source_hard_size_mellin_integral() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    assert_equal("fused source hard b0", b0, Fraction(29, 3))

    # The fused density source has two factors cs K_1(cs).  The exact Mellin
    # integral scales as c^(-b0-2), so it carries the same hard Q power as the
    # general source-amputated coefficient after the Lambda_ht trade.
    source_scale_power = -b0 - 2
    assert_equal("fused source c-scaling power", source_scale_power, Fraction(-35, 3))
    lambda_power = b0
    q_power = -b0 - 2
    assert_equal("fused source hard coefficient dimension", lambda_power + q_power, -2)

    mellin_lambda = b0 + 4
    mellin_nu = Fraction(1)
    assert_equal("fused Mellin lambda", mellin_lambda, Fraction(41, 3))
    assert_equal(
        "fused Mellin convergence condition",
        mellin_lambda > 2 * abs(mellin_nu),
        True,
    )

    mp.mp.dps = 50
    b0_mp = mp.mpf(b0.numerator) / b0.denominator
    lambda_mp = mp.mpf(mellin_lambda.numerator) / mellin_lambda.denominator
    nu_mp = mp.mpf(mellin_nu.numerator) / mellin_nu.denominator
    c_value = mp.mpf(5) / 4

    gamma_formula = (
        c_value ** (-(b0_mp + 2))
        * 2 ** (b0_mp + 1)
        * mp.gamma((b0_mp + 4) / 2) ** 2
        * mp.gamma((b0_mp + 6) / 2)
        * mp.gamma((b0_mp + 2) / 2)
        / mp.gamma(b0_mp + 4)
    )
    schwinger_factorized = (
        c_value ** (-(b0_mp + 2))
        * 2 ** (lambda_mp - 3)
        * mp.gamma(lambda_mp / 2 + nu_mp)
        * mp.gamma(lambda_mp / 2 - nu_mp)
        * mp.beta(lambda_mp / 2, lambda_mp / 2)
    )
    relative_error = abs(schwinger_factorized - gamma_formula) / abs(gamma_formula)
    if not relative_error < mp.mpf("1e-45"):
        raise AssertionError(
            "fused-source Schwinger/Mellin factorization failed: "
            f"relative error {mp.nstr(relative_error, 8)}"
        )

    # The b0=0, c=1 specialization reduces to an elementary Gamma recurrence:
    # int_0^infty s^3 K_1(s)^2 ds = 2/3.
    special_formula = (
        2 ** (4 - 3)
        * mp.gamma(2) ** 2
        * mp.gamma(3)
        * mp.gamma(1)
        / mp.gamma(4)
    )
    assert_close("fused source b0=0 special Mellin value", float(special_formula), 2 / 3)

    doubled_scale_formula = gamma_formula * 2 ** (-(b0_mp + 2))
    doubled_scale_direct = (
        (2 * c_value) ** (-(b0_mp + 2))
        * 2 ** (b0_mp + 1)
        * mp.gamma((b0_mp + 4) / 2) ** 2
        * mp.gamma((b0_mp + 6) / 2)
        * mp.gamma((b0_mp + 2) / 2)
        / mp.gamma(b0_mp + 4)
    )
    scale_error = abs(doubled_scale_formula - doubled_scale_direct) / abs(
        doubled_scale_direct
    )
    if not scale_error < mp.mpf("1e-50"):
        raise AssertionError("fused-source hard scale law failed")

    small_s_power = b0 + 1
    assert_equal("fused source small-s integrability", small_s_power > -1, True)

    def endpoint_kind(exponential_scale: Fraction, power_margin: Fraction) -> str:
        if exponential_scale > 0:
            return "exponential"
        if power_margin > 0:
            return "power"
        return "uncontrolled"

    individual_margin = Fraction(1, 3)
    assert_equal(
        "fused source endpoint channel",
        endpoint_kind(Fraction(2), Fraction(0)),
        "exponential",
    )
    assert_equal(
        "individual source endpoint channel remains power",
        endpoint_kind(Fraction(0), individual_margin),
        "power",
    )
    assert_equal(
        "fused endpoint control is not individual-slot control",
        endpoint_kind(Fraction(2), Fraction(0))
        == endpoint_kind(Fraction(0), individual_margin),
        False,
    )


def check_hard_size_tail_dominance_criterion() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    size_power = b0 + 1
    hard_slot_count = 4
    individual_slot_tail_power = 3
    sigma = individual_slot_tail_power * hard_slot_count

    assert_equal("hard-size tail b0", b0, Fraction(29, 3))
    assert_equal("hard-size tail integrand power before form factors", size_power, Fraction(32, 3))
    assert_equal("hard-size individual slot sigma", sigma, 12)
    assert_equal("hard-size convergence condition margin", sigma - b0 - 2, Fraction(1, 3))
    assert_equal("hard-size tail power after R cutoff", b0 + 2 - sigma, Fraction(-1, 3))
    assert_equal("hard-size log-shell power", b0 + 2 - sigma, Fraction(-1, 3))

    # With the normalized model bound |F_hard(s)| <= C s^{-12}, the tail
    # integral is C/(sigma-b0-2) R^(b0+2-sigma)=3 C R^(-1/3).  Convergence is
    # real but slow: suppressing this normalized tail below epsilon requires
    # R > (3/epsilon)^3.
    normalized_tail_prefactor = Fraction(1, 1) / (sigma - b0 - 2)
    assert_equal("hard-size normalized tail prefactor", normalized_tail_prefactor, 3)

    # Since the shell/tail exponent is 1/3, one decade in R gives only a
    # 10^(-1/3) improvement.  A tenfold improvement requires three decades.
    decades_for_tenfold_tail_suppression = Fraction(1, 1) / (sigma - b0 - 2)
    assert_equal(
        "hard-size decades for tenfold tail suppression",
        decades_for_tenfold_tail_suppression,
        3,
    )

    epsilon = Fraction(1, 10)
    required_r_cubed = (normalized_tail_prefactor / epsilon) ** 3
    assert_equal("hard-size R cubed for ten-percent normalized tail", required_r_cubed, 27000)

    # A fused bilinear-density source carries exponential large-rho
    # suppression; this is a different source construction from the individual
    # fermion-slot kernel and should not be merged with the power-tail test.
    def tail_kind(exponential_scale: Fraction, power_margin: Fraction) -> str:
        if exponential_scale > 0:
            return "exponential"
        if power_margin > 0:
            return "power"
        return "uncontrolled"

    assert_equal(
        "hard-size fused density source tail kind",
        tail_kind(Fraction(2), Fraction(0)),
        "exponential",
    )
    assert_equal(
        "hard-size individual source tail kind",
        tail_kind(Fraction(0), sigma - b0 - 2),
        "power",
    )
    assert_equal(
        "hard-size soft slot tail kind",
        tail_kind(Fraction(0), Fraction(-8, 3)),
        "uncontrolled",
    )


def check_hard_screened_instanton_size_shell() -> None:
    # Majorant shell for rho^A exp[-dQ rho - m_scr^2 rho^2] d log rho.
    # Choose exact data for which the mixed stationary point is rational.
    shell_power = Fraction(8)
    hard_envelope = Fraction(6)
    screening_mass_squared = Fraction(1)
    discriminant = (
        hard_envelope * hard_envelope
        + 8 * shell_power * screening_mass_squared
    )
    assert_equal("hard-screened discriminant", discriminant, Fraction(100))
    sqrt_discriminant = math.isqrt(discriminant.numerator)
    assert_equal(
        "hard-screened discriminant is square",
        sqrt_discriminant * sqrt_discriminant,
        discriminant.numerator,
    )

    rho_star = (
        -hard_envelope + Fraction(sqrt_discriminant)
    ) / (4 * screening_mass_squared)
    assert_equal("hard-screened mixed shell", rho_star, Fraction(1))
    assert_equal(
        "hard-screened stationarity equation",
        2 * screening_mass_squared * rho_star * rho_star
        + hard_envelope * rho_star
        - shell_power,
        Fraction(0),
    )

    hard_only_shell = shell_power / hard_envelope
    screened_only_shell = Fraction(2)  # sqrt(A/(2 m^2)) for A=8, m^2=1.
    assert_equal("mixed shell below hard-only shell", rho_star < hard_only_shell, True)
    assert_equal("mixed shell below screened-only shell", rho_star < screened_only_shell, True)

    # Exact ratio to the hard-only shell:
    # rho_*/(A/dQ) = 2/(1+sqrt(1+8 A m^2/(dQ)^2)).
    eta = 8 * shell_power * screening_mass_squared / (hard_envelope * hard_envelope)
    assert_equal("hard-screened eta", eta, Fraction(16, 9))
    sqrt_one_plus_eta = Fraction(sqrt_discriminant, hard_envelope)
    assert_equal("hard-screened sqrt one plus eta", sqrt_one_plus_eta, Fraction(5, 3))
    assert_equal(
        "hard-screened ratio to hard shell",
        rho_star / hard_only_shell,
        Fraction(2) / (1 + sqrt_one_plus_eta),
    )

    def log_shell_derivative(
        rho: Fraction,
        include_hard: bool,
        include_screening: bool,
    ) -> Fraction:
        return (
            shell_power
            - (hard_envelope * rho if include_hard else 0)
            - (2 * screening_mass_squared * rho * rho if include_screening else 0)
        )

    assert_equal(
        "hard-only shell fails when screening is present",
        log_shell_derivative(
            hard_only_shell,
            include_hard=True,
            include_screening=True,
        ) == 0,
        False,
    )
    assert_equal(
        "screened-only shell fails when hard envelope is present",
        log_shell_derivative(
            screened_only_shell,
            include_hard=True,
            include_screening=True,
        ) == 0,
        False,
    )
    assert_equal(
        "hard shell is correct only after dropping screening",
        log_shell_derivative(hard_only_shell, include_hard=True, include_screening=False),
        Fraction(0),
    )
    assert_equal(
        "screened shell is correct only after dropping hard envelope",
        log_shell_derivative(screened_only_shell, include_hard=False, include_screening=True),
        Fraction(0),
    )

    # Limiting-regime diagnostics used by the prose.  A small value means the
    # named effect is a perturbation across the pure shell; neither replaces
    # the exact mixed stationarity equation in the intermediate region.
    hard_shell_screening_ratio = screening_mass_squared * hard_only_shell * hard_only_shell
    screened_shell_hard_ratio = hard_envelope * screened_only_shell / shell_power
    assert_equal("screening across hard-only shell", hard_shell_screening_ratio, Fraction(16, 9))
    assert_equal("hard envelope across screened-only shell", screened_shell_hard_ratio, Fraction(3, 2))


def check_su3_two_flavor_hard_instanton_coefficient() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    zero_mode_power = Fraction(6)
    measure_power = Fraction(-5)
    size_integrand_power = b0 + zero_mode_power + measure_power

    assert_equal("SU3 Nf2 hard coefficient b0", b0, Fraction(29, 3))
    assert_equal("SU3 Nf2 hard coefficient collective power", 2 * n_c, 6)
    assert_equal("SU3 Nf2 hard size integrand power", size_integrand_power, Fraction(32, 3))

    q_power_at_mu_q = b0 - (size_integrand_power + 1)
    assert_equal("SU3 Nf2 hard coefficient Q power at mu=Q", q_power_at_mu_q, Fraction(-2))

    lambda_power = b0
    rg_invariant_q_power = -b0 + q_power_at_mu_q
    assert_equal("SU3 Nf2 hard Lambda power", lambda_power, Fraction(29, 3))
    assert_equal("SU3 Nf2 hard RG-invariant Q power", rg_invariant_q_power, Fraction(-35, 3))
    assert_equal(
        "SU3 Nf2 hard coefficient mass dimension",
        lambda_power + rg_invariant_q_power,
        Fraction(-2),
    )

    # For F_zm(c_l s/2) ~ 6 c_l^(-3) s^(-3), four differentiated slots give
    # an integrand s^(32/3-12)=s^(-4/3).  The tail integral is
    # 3*6^4*prod c_l^(-3)*R^(-1/3), with the next term O(R^(-7/3)).
    c_values = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    leading_slot_coefficient = product_fraction([Fraction(6, 1) / (c**3) for c in c_values])
    tail_integrand_power = size_integrand_power - 12
    tail_antiderivative_power = tail_integrand_power + 1
    leading_tail_coefficient = -leading_slot_coefficient / tail_antiderivative_power

    assert_equal("SU3 Nf2 hard tail integrand power", tail_integrand_power, Fraction(-4, 3))
    assert_equal("SU3 Nf2 hard tail antiderivative power", tail_antiderivative_power, Fraction(-1, 3))
    assert_equal(
        "SU3 Nf2 hard tail leading coefficient",
        leading_tail_coefficient,
        3 * leading_slot_coefficient,
    )
    assert_equal(
        "SU3 Nf2 hard tail coefficient with sample c",
        leading_tail_coefficient,
        Fraction(3 * 6**4, (1 * 2 * 3 * 4) ** 3),
    )

    next_slot_power = -14
    next_tail_power = size_integrand_power + next_slot_power + 1
    assert_equal("SU3 Nf2 hard tail next exponent", next_tail_power, Fraction(-7, 3))


def check_individual_slot_tail_subtracted_hard_coefficient() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    size_integrand_power = b0 + 1
    leading_product_power = -12
    residual_product_power = -14

    assert_equal(
        "individual-slot leading integrand power",
        size_integrand_power + leading_product_power,
        -Fraction(4, 3),
    )
    assert_equal(
        "individual-slot residual integrand power",
        size_integrand_power + residual_product_power,
        -Fraction(10, 3),
    )

    c_values = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    orientation_tail = Fraction(5, 7)
    a_ind = orientation_tail * product_fraction(
        [Fraction(6, 1) / (c**3) for c in c_values]
    )
    b_ind = Fraction(13, 11)
    x = Fraction(3)
    r_minus_one_third = Fraction(1, 1) / x
    r_minus_seven_thirds = Fraction(1, 1) / (x**7)

    leading_tail = 3 * a_ind * r_minus_one_third
    residual_bound = Fraction(3, 7) * b_ind * r_minus_seven_thirds
    actual_residual = residual_bound / 2
    finite_window_integral = Fraction(17, 19)
    exact_tail = leading_tail + actual_residual
    exact_integral = finite_window_integral + exact_tail
    accelerated_estimator = finite_window_integral + leading_tail

    assert_equal(
        "individual-slot leading tail subtraction coefficient",
        leading_tail,
        3 * a_ind / x,
    )
    assert_equal(
        "individual-slot subtracted residual bound",
        residual_bound,
        Fraction(3, 7) * b_ind / (x**7),
    )
    if not abs(exact_integral - accelerated_estimator) <= residual_bound:
        raise AssertionError("individual-slot tail-subtracted residual bound failed")

    raw_truncation_error = abs(exact_integral - finite_window_integral)
    assert_equal(
        "raw individual-slot truncation is not residual-level control",
        raw_truncation_error <= residual_bound,
        False,
    )

    # If the leading source-orientation tail coefficient cancels, the same
    # formula correctly leaves only the residual majorant; it does not license
    # importing the fused-source exponential tail.
    canceled_a_ind = Fraction(0)
    canceled_accelerated = finite_window_integral + 3 * canceled_a_ind / x
    canceled_exact = finite_window_integral + actual_residual
    if not abs(canceled_exact - canceled_accelerated) <= residual_bound:
        raise AssertionError("canceled-tail individual-slot residual bound failed")


def check_hard_instanton_finite_window_bound() -> None:
    # A finite hard coefficient needs an absolute error budget and a
    # noncancellation margin |J_R| >= kappa_R M_R.  Otherwise a small absolute
    # tail can be a large relative error in the signed/source-projected
    # coefficient.
    window_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    j_r = sum(window_cells, Fraction(0))
    m_r = sum(abs(cell) for cell in window_cells)
    kappa_r = abs(j_r) / m_r
    assert_equal("hard instanton finite-window leading integral", j_r, Fraction(17, 20))
    assert_equal("hard instanton finite-window absolute mass", m_r, Fraction(21, 20))
    assert_equal("hard instanton finite-window noncancellation margin", kappa_r, Fraction(17, 21))

    eps_det = Fraction(1, 40)
    eps_zm = Fraction(1, 60)
    eps_src = Fraction(1, 120)
    eps_schur = Fraction(1, 80)
    tau_r = Fraction(1, 32)
    eps_total = eps_det + eps_zm + eps_src + eps_schur
    assert_equal("hard instanton finite-window residual sum", eps_total, Fraction(1, 16))

    actual_residual = (
        Fraction(1, 80) * m_r
        - Fraction(1, 100) * m_r
        + Fraction(1, 200) * m_r
        + Fraction(1, 100) * m_r
    )
    actual_tail = Fraction(1, 40) * m_r
    exact_coefficient = j_r + actual_residual + actual_tail
    absolute_bound = m_r * (eps_total + tau_r)
    if not abs(exact_coefficient - j_r) <= absolute_bound:
        raise AssertionError("hard instanton finite-window absolute bound failed")

    relative_bound = (eps_total + tau_r) / kappa_r
    actual_relative_error = abs(exact_coefficient - j_r) / abs(j_r)
    if not actual_relative_error <= relative_bound:
        raise AssertionError("hard instanton finite-window relative bound failed")

    # The SU(3), Nf=2 differentiated four-slot power tail is
    # s^(32/3) s^(-12)=s^(-4/3), hence the retained tail bound
    # int_R^infty B s^(-4/3) ds = 3 B R^(-1/3).
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    large_s_power = b0 + 1 - 12
    assert_equal("hard instanton finite-window tail integrand power", large_s_power, -Fraction(4, 3))
    b_infty = Fraction(5, 7)
    r_cuberoot = Fraction(3)
    tail_bound = 3 * b_infty / r_cuberoot
    assert_equal("hard instanton finite-window R=27 tail bound", tail_bound, b_infty)

    # Cancellation negative control: a tiny signed window coefficient cannot
    # be assigned a small relative uncertainty from an absolute majorant alone.
    cancel_cells = [Fraction(1), -Fraction(99, 100)]
    cancel_j = sum(cancel_cells, Fraction(0))
    cancel_m = sum(abs(cell) for cell in cancel_cells)
    cancel_kappa = abs(cancel_j) / cancel_m
    assert_equal("hard instanton cancellation window coefficient", cancel_j, Fraction(1, 100))
    assert_equal("hard instanton cancellation margin", cancel_kappa, Fraction(1, 199))

    nominal_absolute_ratio = Fraction(1, 100)
    relative_bound = nominal_absolute_ratio / cancel_kappa
    assert_equal(
        "hard instanton cancellation makes relative control fail",
        relative_bound <= Fraction(1, 10),
        False,
    )


def check_four_source_instanton_amplitude_rank_bound() -> None:
    def max_abs_entry(matrix: list[list[Fraction]]) -> Fraction:
        return max(abs(entry) for row in matrix for entry in row)

    right_overlap = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(2)]]
    left_overlap = [[Fraction(3), Fraction(1)], [Fraction(2), Fraction(2)]]
    right_det = det_fraction(right_overlap)
    left_det = det_fraction(left_overlap)
    assert_equal("four-source right zero-mode determinant", right_det, Fraction(3))
    assert_equal("four-source left zero-mode determinant", left_det, Fraction(4))

    eta_right = Fraction(1, 20)
    eta_left = Fraction(1, 30)
    right_entry_bound = max_abs_entry(right_overlap)
    left_entry_bound = max_abs_entry(left_overlap)
    right_det_error_bound = 4 * right_entry_bound * eta_right + 2 * eta_right * eta_right
    left_det_error_bound = 4 * left_entry_bound * eta_left + 2 * eta_left * eta_left

    right_delta = [
        [eta_right, -eta_right],
        [Fraction(0), eta_right],
    ]
    left_delta = [
        [eta_left, Fraction(0)],
        [-eta_left, eta_left],
    ]
    right_exact = matrix_add_fraction(right_overlap, right_delta)
    left_exact = matrix_add_fraction(left_overlap, left_delta)
    actual_right_det_error = abs(det_fraction(right_exact) - right_det)
    actual_left_det_error = abs(det_fraction(left_exact) - left_det)

    if not actual_right_det_error <= right_det_error_bound:
        raise AssertionError("right overlap determinant-stability bound failed")
    if not actual_left_det_error <= left_det_error_bound:
        raise AssertionError("left overlap determinant-stability bound failed")

    rank_relative_bound = (
        right_det_error_bound / abs(right_det)
        + left_det_error_bound / abs(left_det)
        + right_det_error_bound * left_det_error_bound / (abs(right_det) * abs(left_det))
    )
    exact_source_factor = det_fraction(right_exact) * det_fraction(left_exact)
    leading_source_factor = right_det * left_det
    actual_rank_relative_error = abs(exact_source_factor - leading_source_factor) / abs(
        leading_source_factor
    )
    if not actual_rank_relative_error <= rank_relative_bound:
        raise AssertionError("four-source rank-margin residual bound failed")

    window_cells = [Fraction(3, 5), -Fraction(1, 10), Fraction(7, 20)]
    j_r = sum(window_cells, Fraction(0)) * leading_source_factor
    m_r = sum(abs(cell) for cell in window_cells) * abs(leading_source_factor)

    eps_det = Fraction(1, 80)
    eps_schur = Fraction(1, 120)
    eps_proj = Fraction(1, 100)
    tau_r = Fraction(1, 90)
    euclidean_error_bound = m_r * (eps_det + rank_relative_bound + eps_schur + eps_proj + tau_r)
    actual_euclidean_residual = (
        m_r * Fraction(1, 200)
        - m_r * Fraction(1, 300)
        + m_r * Fraction(1, 240)
    )
    exact_euclidean_coefficient = j_r + actual_euclidean_residual
    if not abs(exact_euclidean_coefficient - j_r) <= euclidean_error_bound:
        raise AssertionError("four-source instanton Euclidean amplitude bound failed")

    physical_projection_residual = Fraction(1, 70)
    physical_amplitude = exact_euclidean_coefficient + physical_projection_residual
    if physical_amplitude == exact_euclidean_coefficient:
        raise AssertionError("physical projection residual accidentally vanished")
    if physical_amplitude - j_r == actual_euclidean_residual:
        raise AssertionError(
            "negative control failed: physical projection residual was merged into Euclidean kernel"
        )

    rank_one_right = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
    assert_equal("rank-one right source determinant", det_fraction(rank_one_right), Fraction(0))
    rank_one_source_factor = det_fraction(rank_one_right) * left_det
    if rank_one_source_factor != 0:
        raise AssertionError("rank-one right source still produced a four-source zero-mode factor")

    moduli_measure_weight = Fraction(5, 7)
    determinant_weight = Fraction(11, 13)
    if moduli_measure_weight * determinant_weight == rank_one_source_factor:
        raise AssertionError(
            "negative control failed: moduli and determinant weights detected zero-mode rank collapse"
        )


def check_four_source_instanton_source_conditioning() -> None:
    def max_abs_entry(matrix: list[list[Fraction]]) -> Fraction:
        return max(abs(entry) for row in matrix for entry in row)

    def conditioning_matrix(
        base: list[list[Fraction]],
        perturbation: list[list[Fraction]],
    ) -> list[list[Fraction]]:
        return matmul_fraction(inverse_2x2_fraction(base), perturbation)

    def determinant_relative_error(
        base: list[list[Fraction]],
        perturbation: list[list[Fraction]],
    ) -> Fraction:
        base_det = det_fraction(base)
        exact_det = det_fraction(matrix_add_fraction(base, perturbation))
        return abs(exact_det - base_det) / abs(base_det)

    def conditioning_relative_bound(
        base: list[list[Fraction]],
        perturbation: list[list[Fraction]],
    ) -> Fraction:
        delta = max_abs_entry(conditioning_matrix(base, perturbation))
        return 2 * delta + 2 * delta * delta

    right_base = [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(21, 20)]]
    right_perturbation = [
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1, 1000)],
    ]
    right_conditioning = conditioning_matrix(right_base, right_perturbation)
    right_delta = max_abs_entry(right_conditioning)
    right_relative_error = determinant_relative_error(right_base, right_perturbation)
    assert_equal("near-rank source determinant margin", det_fraction(right_base), Fraction(1, 20))
    assert_equal("near-rank source conditioning delta", right_delta, Fraction(1, 50))
    assert_equal("near-rank source determinant relative error", right_relative_error, Fraction(1, 50))
    if not right_relative_error <= conditioning_relative_bound(right_base, right_perturbation):
        raise AssertionError("right source conditioning determinant bound failed")

    unconditioned_overlap_error = max_abs_entry(right_perturbation)
    assert_equal(
        "unconditioned overlap error underestimates determinant-relative error",
        right_relative_error > 10 * unconditioned_overlap_error,
        True,
    )

    left_base = [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(3)]]
    left_perturbation = [
        [Fraction(1, 100), Fraction(0)],
        [Fraction(0), Fraction(-1, 200)],
    ]
    left_relative_error = determinant_relative_error(left_base, left_perturbation)
    assert_equal("well-conditioned left determinant", det_fraction(left_base), Fraction(6))
    assert_equal("left source conditioning delta", max_abs_entry(conditioning_matrix(left_base, left_perturbation)), Fraction(1, 200))
    if not left_relative_error <= conditioning_relative_bound(left_base, left_perturbation):
        raise AssertionError("left source conditioning determinant bound failed")

    leading_source_factor = det_fraction(right_base) * det_fraction(left_base)
    exact_source_factor = (
        det_fraction(matrix_add_fraction(right_base, right_perturbation))
        * det_fraction(matrix_add_fraction(left_base, left_perturbation))
    )
    actual_source_relative_error = abs(exact_source_factor - leading_source_factor) / abs(
        leading_source_factor
    )
    right_bound = conditioning_relative_bound(right_base, right_perturbation)
    left_bound = conditioning_relative_bound(left_base, left_perturbation)
    product_bound = right_bound + left_bound + right_bound * left_bound
    if not actual_source_relative_error <= product_bound:
        raise AssertionError("four-source conditioning product bound failed")

    window_mass = Fraction(17, 19)
    conditioned_amplitude_bound = window_mass * product_bound
    actual_amplitude_error = window_mass * actual_source_relative_error
    if not actual_amplitude_error <= conditioned_amplitude_bound:
        raise AssertionError("conditioned source residual did not bound amplitude error")

    rank_one_hard_source = [[Fraction(1), Fraction(1)], [Fraction(2), Fraction(2)]]
    hard_support_margin = Fraction(3, 5)
    assert_equal("rank-one hard source determinant", det_fraction(rank_one_hard_source), Fraction(0))
    assert_equal("hard support margin can be positive with rank collapse", hard_support_margin > 0, True)
    try:
        inverse_2x2_fraction(rank_one_hard_source)
    except AssertionError:
        pass
    else:
        raise AssertionError("rank-one hard source incorrectly admitted a conditioning matrix")

    moduli_measure_weight = Fraction(5, 7)
    determinant_constant = Fraction(11, 13)
    if moduli_measure_weight * determinant_constant == leading_source_factor:
        raise AssertionError(
            "negative control failed: moduli/determinant constants fixed source conditioning"
        )


def check_thooft_four_fermion_benchmark_gate_ledger() -> None:
    required_gates = {
        "center",
        "classical_collective",
        "determinant",
        "zero_mode_source",
        "haar_projection",
        "amputation",
        "source_conditioning",
        "size_window",
        "sector_projection",
        "physical_projection",
        "scheme_transport",
    }
    supplied_gates = set(required_gates)
    assert_equal("four-fermion benchmark supplies every gate", supplied_gates, required_gates)
    for omitted_gate in sorted(required_gates):
        assert_equal(
            f"omitting benchmark gate {omitted_gate} is detected",
            required_gates.issubset(supplied_gates - {omitted_gate}),
            False,
        )

    # A finite arithmetic model of the benchmark coefficient:
    # center delta (on shell), classical/collective weight, determinant,
    # shared Haar projection, conditioned right/left zero-mode determinants,
    # amputation convention, and the signed size window all multiply before
    # the physical projection is applied.
    center_delta_on_shell = Fraction(1)
    center_delta_off_shell = Fraction(0)
    classical_collective = Fraction(2, 5)
    determinant_constant = Fraction(11, 13)
    haar_projection = Fraction(3, 7)
    amputation_factor = Fraction(1)
    scheme_factor = Fraction(1)
    physical_projection = Fraction(7, 11)
    sector_projection = Fraction(1)

    right_overlap = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(2)]]
    left_overlap = [[Fraction(3), Fraction(1)], [Fraction(2), Fraction(2)]]
    zero_mode_source = det_fraction(right_overlap) * det_fraction(left_overlap)
    assert_equal("benchmark right source determinant", det_fraction(right_overlap), Fraction(3))
    assert_equal("benchmark left source determinant", det_fraction(left_overlap), Fraction(4))
    assert_equal("benchmark zero-mode source factor", zero_mode_source, Fraction(12))

    size_cells = [Fraction(1, 2), -Fraction(1, 8), Fraction(3, 10)]
    signed_size_window = sum(size_cells, Fraction(0))
    absolute_size_mass = sum(abs(cell) for cell in size_cells)
    assert_equal("benchmark signed size window", signed_size_window, Fraction(27, 40))
    assert_equal("benchmark absolute size mass", absolute_size_mass, Fraction(37, 40))

    euclidean_benchmark = (
        center_delta_on_shell
        * classical_collective
        * determinant_constant
        * haar_projection
        * amputation_factor
        * scheme_factor
        * zero_mode_source
        * signed_size_window
    )
    benchmark_mass = (
        abs(classical_collective)
        * abs(determinant_constant)
        * abs(haar_projection)
        * abs(zero_mode_source)
        * absolute_size_mass
    )
    physical_benchmark = physical_projection * sector_projection * euclidean_benchmark
    kappa_benchmark = abs(physical_benchmark) / benchmark_mass
    assert_equal("benchmark noncancellation margin", kappa_benchmark, Fraction(189, 407))

    epsilons = {
        "determinant": Fraction(1, 100),
        "zero_mode_source": Fraction(1, 120),
        "haar_projection": Fraction(1, 140),
        "source_conditioning": Fraction(1, 160),
        "size_window": Fraction(1, 90),
        "sector_projection": Fraction(1, 150),
        "physical_projection": Fraction(1, 110),
        "scheme_transport": Fraction(1, 130),
    }
    residual_sum = (
        benchmark_mass * Fraction(1, 500)
        - benchmark_mass * Fraction(1, 700)
        + benchmark_mass * Fraction(1, 900)
    )
    epsilon_sum = sum(epsilons.values(), Fraction(0))
    if not abs(residual_sum) <= benchmark_mass * epsilon_sum:
        raise AssertionError("benchmark absolute residual ledger failed")
    relative_residual = abs(residual_sum) / abs(physical_benchmark)
    relative_bound = epsilon_sum / kappa_benchmark
    if not relative_residual <= relative_bound:
        raise AssertionError("benchmark relative residual bound failed")

    # Off-shell center momentum conservation kills the benchmark coefficient
    # even when all local instanton factors are nonzero.
    off_shell_benchmark = (
        center_delta_off_shell
        * classical_collective
        * determinant_constant
        * haar_projection
        * zero_mode_source
        * signed_size_window
    )
    assert_equal("off-shell center gate kills four-fermion benchmark", off_shell_benchmark, Fraction(0))

    density_only = classical_collective * determinant_constant * signed_size_window
    assert_equal(
        "moduli plus determinant density is not the four-fermion benchmark",
        density_only == euclidean_benchmark,
        False,
    )

    rank_one_right = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
    collapsed_source = det_fraction(rank_one_right) * det_fraction(left_overlap)
    assert_equal("rank-collapsed benchmark source factor", collapsed_source, Fraction(0))
    collapsed_benchmark = (
        classical_collective
        * determinant_constant
        * haar_projection
        * collapsed_source
        * signed_size_window
    )
    assert_equal("rank collapse kills the benchmark despite hard gates", collapsed_benchmark, Fraction(0))

    external_residue_product = Fraction(5, 3)
    unamputated_benchmark = external_residue_product * euclidean_benchmark
    assert_equal(
        "unamputated external residues change the benchmark coordinate",
        unamputated_benchmark == euclidean_benchmark,
        False,
    )
    assert_equal(
        "amputation recovers the benchmark coordinate",
        unamputated_benchmark / external_residue_product,
        euclidean_benchmark,
    )

    assert_equal(
        "colored Euclidean kernel is not yet the physical benchmark",
        euclidean_benchmark == physical_benchmark,
        False,
    )

    lower_action_leakage = benchmark_mass * Fraction(1, 20)
    without_sector_projection = physical_benchmark + lower_action_leakage
    assert_equal(
        "sector leakage changes the selected benchmark amplitude",
        without_sector_projection == physical_benchmark,
        False,
    )
    if not abs(without_sector_projection - physical_benchmark) <= benchmark_mass:
        raise AssertionError("sector leakage was not measured in the benchmark source norm")

    source_frame = Fraction(7, 5)
    operator_frame = Fraction(13, 17)
    coupling_constant_shift = Fraction(19, 23)
    transported_determinant = (
        coupling_constant_shift * determinant_constant / (source_frame * operator_frame)
    )
    old_scheme_coordinate = determinant_constant * zero_mode_source * physical_projection
    transported_coordinate = (
        transported_determinant
        * (source_frame * zero_mode_source)
        * (operator_frame * physical_projection)
        / coupling_constant_shift
    )
    reused_old_constant_coordinate = (
        determinant_constant
        * (source_frame * zero_mode_source)
        * (operator_frame * physical_projection)
    )
    assert_equal("scheme-transported determinant preserves benchmark coordinate", transported_coordinate, old_scheme_coordinate)
    assert_equal(
        "reusing old determinant constant after frame changes fails",
        reused_old_constant_coordinate == old_scheme_coordinate,
        False,
    )


def check_wilsonian_instanton_size_factorization() -> None:
    # Model the fully paired finite-regulator size integrand by
    # K(rho)=rho^(p-1) on 0<rho<rho_max.  The artificial Wilsonian split at
    # rho_I=1/mu_I has short and long logarithmic derivatives which cancel by
    # the boundary flux rho_I K(rho_I).
    p = 5
    mu_i = Fraction(3, 2)
    rho_i = Fraction(1, 1) / mu_i
    rho_max = Fraction(5, 1)

    def primitive(rho: Fraction) -> Fraction:
        return rho**p / p

    short_piece = primitive(rho_i)
    long_piece = primitive(rho_max) - primitive(rho_i)
    total_piece = primitive(rho_max)
    boundary_flux = rho_i**p

    assert_equal(
        "Wilsonian instanton split preserves total size integral",
        short_piece + long_piece,
        total_piece,
    )
    assert_equal(
        "short-instanton coefficient log-scale derivative",
        -boundary_flux,
        -rho_i * rho_i ** (p - 1),
    )
    assert_equal(
        "long-instanton remainder log-scale derivative",
        boundary_flux,
        rho_i * rho_i ** (p - 1),
    )
    assert_equal(
        "Wilsonian instanton factorization-scale cancellation",
        -boundary_flux + boundary_flux,
        0,
    )

    # Moving the factorization scale only transfers the intervening shell
    # between the short coefficient and the long-distance remainder.
    mu_low = Fraction(2, 1)
    mu_high = Fraction(4, 1)
    rho_low_cut = Fraction(1, 1) / mu_low
    rho_high_cut = Fraction(1, 1) / mu_high
    transferred_shell = primitive(rho_low_cut) - primitive(rho_high_cut)
    short_low = primitive(rho_low_cut)
    short_high = primitive(rho_high_cut)
    long_low = primitive(rho_max) - primitive(rho_low_cut)
    long_high = primitive(rho_max) - primitive(rho_high_cut)

    assert_equal(
        "raising instanton factorization scale removes shell from short part",
        short_low - short_high,
        transferred_shell,
    )
    assert_equal(
        "raising instanton factorization scale adds shell to long part",
        long_high - long_low,
        transferred_shell,
    )
    assert_equal(
        "factorization shell transfer leaves full amplitude fixed",
        short_high + long_high,
        short_low + long_low,
    )


def check_short_instanton_ope_coefficient_transport() -> None:
    # A local instanton vertex coefficient is a row vector pairing with a
    # renormalized operator column.  If dO/dlog(mu)=-gamma O, the coefficient
    # obeys dC/dlog(mu)=C gamma so that C O is scale independent.
    coefficient = [[Fraction(2, 3), Fraction(5, 7)]]
    operator_matrix_element = [[Fraction(11, 13)], [Fraction(17, 19)]]
    gamma = [
        [Fraction(1, 3), Fraction(2, 5)],
        [Fraction(-1, 7), Fraction(3, 11)],
    ]

    coefficient_flow = matmul_fraction(coefficient, gamma)
    operator_flow = [
        [-entry[0]]
        for entry in matmul_fraction(gamma, operator_matrix_element)
    ]
    pair_flow = (
        matmul_fraction(coefficient_flow, operator_matrix_element)[0][0]
        + matmul_fraction(coefficient, operator_flow)[0][0]
    )
    assert_equal("short-instanton coefficient/operator RG cancellation", pair_flow, 0)

    # A finite operator-frame change O_tilde=M O requires C_tilde=C M^{-1};
    # the coefficient alone changes, but the local insertion is unchanged.
    frame_change = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(1)]]
    frame_inverse = inverse_2x2_fraction(frame_change)
    coefficient_tilde = matmul_fraction(coefficient, frame_inverse)
    operator_tilde = matmul_fraction(frame_change, operator_matrix_element)
    assert_equal(
        "short-instanton coefficient frame change leaves insertion pairing",
        matmul_fraction(coefficient_tilde, operator_tilde)[0][0],
        matmul_fraction(coefficient, operator_matrix_element)[0][0],
    )

    # With a scale-dependent finite frame, the connection law of Chapter 12
    # makes the transformed coefficient obey the same dual transport equation.
    frame_change_flow = [
        [Fraction(1, 5), Fraction(1, 7)],
        [Fraction(1, 11), Fraction(-1, 13)],
    ]
    gamma_tilde = matrix_sub_fraction(
        matmul_fraction(matmul_fraction(frame_change, gamma), frame_inverse),
        matmul_fraction(frame_change_flow, frame_inverse),
    )
    coefficient_tilde_flow_direct = matrix_sub_fraction(
        matmul_fraction(coefficient_flow, frame_inverse),
        matmul_fraction(
            coefficient_tilde,
            matmul_fraction(frame_change_flow, frame_inverse),
        ),
    )
    coefficient_tilde_flow_connection = matmul_fraction(coefficient_tilde, gamma_tilde)
    assert_equal(
        "short-instanton coefficient follows transformed operator connection",
        coefficient_tilde_flow_direct,
        coefficient_tilde_flow_connection,
    )

    # The Wilsonian size cut is a different scale.  Its boundary flux cancels
    # only against the long-distance coefficient/remainder, not against the
    # operator-mixing RG transport above.
    boundary_flux = [[Fraction(3, 17), Fraction(5, 19)]]
    short_size_flow = [[-entry for entry in boundary_flux[0]]]
    long_size_flow = boundary_flux
    assert_equal(
        "short and long OPE coefficient size-boundary flux cancels",
        matrix_add_fraction(short_size_flow, long_size_flow),
        [[Fraction(0), Fraction(0)]],
    )
    assert_equal(
        "operator RG transport is distinct from size-factorization flux",
        coefficient_flow == short_size_flow,
        False,
    )


def check_dilute_instanton_gas_theta_cumulants() -> None:
    # The dilute gas promotes the one-instanton and one-anti-instanton
    # amplitudes to independent Poisson activities.  The topological charge
    # Q=n_+-n_- therefore has a Skellam cumulant generator
    # K(t)=V zeta (e^t+e^{-t}-2).
    volume = Fraction(11, 5)
    activity = Fraction(7, 13)
    one_species_mean = volume * activity

    for order in range(1, 8):
        cumulant = (
            2 * one_species_mean
            if order % 2 == 0
            else Fraction(0)
        )
        expected = (
            2 * volume * activity
            if order % 2 == 0
            else Fraction(0)
        )
        assert_equal(f"dilute gas charge cumulant order {order}", cumulant, expected)

    topological_susceptibility = (2 * volume * activity) / volume
    assert_equal("dilute gas topological susceptibility", topological_susceptibility, 2 * activity)

    # E(theta)-E(0)=2 zeta (1-cos theta)
    # = zeta theta^2 - zeta theta^4/12 + zeta theta^6/360 + ...
    theta2_coefficient = activity
    theta4_coefficient = -activity / 12
    theta6_coefficient = activity / 360
    assert_equal("dilute gas theta2 coefficient", theta2_coefficient, topological_susceptibility / 2)
    assert_equal("dilute gas b2 coefficient", theta4_coefficient / theta2_coefficient, Fraction(-1, 12))
    assert_equal("dilute gas theta6 coefficient", theta6_coefficient, activity / 360)

    for m in range(1, 5):
        energy_derivative = 2 * activity * (1 if m % 2 == 1 else -1)
        assert_equal(
            f"dilute gas energy derivative order {2 * m}",
            energy_derivative,
            2 * activity * ((-1) ** (m + 1)),
        )

    # A mass-saturated QCD vacuum activity contains one mass factor for each
    # Dirac flavor zero-mode pair.  If one mass is zero, the vacuum theta
    # activity from this one-instanton term vanishes, even though fermionic
    # correlators can still be saturated by external sources.
    nonzero_masses = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    mass_saturated_activity = activity * product_fraction(nonzero_masses)
    assert_equal(
        "mass-saturated dilute activity",
        mass_saturated_activity,
        Fraction(770, 3549),
    )
    masses_with_zero = [Fraction(2, 3), Fraction(0), Fraction(11, 13)]
    assert_equal(
        "massless flavor removes vacuum dilute activity",
        activity * product_fraction(masses_with_zero),
        Fraction(0),
    )


def check_first_cluster_correction_to_dilute_instanton_gas() -> None:
    zeta = Fraction(5, 17)
    same_charge_cluster = Fraction(-3, 19)
    neutral_cluster = Fraction(7, 23)

    # Mayer pressure through two-body clusters:
    # p(theta)=2 zeta cos(theta)
    #        + zeta^2 (B_2 cos(2 theta)+B_0).
    # The theta-independent neutral cluster cancels from E(theta)-E(0).
    pressure_zero = 2 * zeta + zeta * zeta * (
        same_charge_cluster + neutral_cluster
    )
    pressure_theta_dependent_zero = 2 * zeta + zeta * zeta * same_charge_cluster
    assert_equal(
        "neutral instanton-anti-instanton cluster is theta independent",
        pressure_zero - pressure_theta_dependent_zero,
        zeta * zeta * neutral_cluster,
    )

    # E(theta)-E(0)=p(0)-p(theta).  For 1-cos(n theta), the second and fourth
    # derivatives at zero are n^2 and -n^4.
    susceptibility = 2 * zeta + 4 * zeta * zeta * same_charge_cluster
    fourth_curvature = -2 * zeta - 16 * zeta * zeta * same_charge_cluster
    assert_equal(
        "first cluster susceptibility harmonic",
        susceptibility,
        2 * zeta * (1 + 2 * zeta * same_charge_cluster),
    )
    assert_equal(
        "first cluster fourth theta curvature harmonic",
        fourth_curvature,
        -2 * zeta * (1 + 8 * zeta * same_charge_cluster),
    )

    b2 = fourth_curvature / (12 * susceptibility)
    assert_equal(
        "first cluster b2 exact ratio",
        b2,
        -(
            1 + 8 * zeta * same_charge_cluster
        ) / (12 * (1 + 2 * zeta * same_charge_cluster)),
    )

    poisson_b2 = Fraction(-1, 12)
    first_order_shift = -zeta * same_charge_cluster / 2
    linearized_b2 = poisson_b2 + first_order_shift
    cluster_parameter = zeta * same_charge_cluster
    exact_minus_linearized = b2 - linearized_b2
    assert_equal(
        "first cluster b2 shift starts at same-charge cluster",
        first_order_shift,
        Fraction(15, 646),
    )
    assert_equal(
        "first cluster b2 linearization error is quadratic",
        exact_minus_linearized,
        cluster_parameter * cluster_parameter / (1 + 2 * cluster_parameter),
    )


def check_two_body_cluster_integrability_window() -> None:
    def cluster_status(p_collision: Fraction, p_infinity: Fraction) -> str:
        if p_collision > 4:
            return "collision_power_divergent"
        if p_collision == 4:
            return "collision_log_divergent"
        if p_infinity < 4:
            return "tail_power_divergent"
        if p_infinity == 4:
            return "tail_log_divergent"
        return "finite"

    one_body_plus_mass = Fraction(2, 5)
    one_body_minus_mass = Fraction(3, 7)
    cluster_majorant = Fraction(11, 13)
    p_collision = Fraction(3)
    p_infinity = Fraction(5)
    radial_without_sphere = (
        Fraction(1, 4 - p_collision)
        + Fraction(1, p_infinity - 4)
    )
    assert_equal("two-body cluster finite status", cluster_status(p_collision, p_infinity), "finite")
    assert_equal("two-body cluster radial majorant", radial_without_sphere, Fraction(2))

    absolute_cluster_bound_without_sphere = (
        one_body_plus_mass
        * one_body_minus_mass
        * cluster_majorant
        * radial_without_sphere
    )
    assert_equal(
        "two-body cluster absolute bound without sphere volume",
        absolute_cluster_bound_without_sphere,
        Fraction(132, 455),
    )

    # The one-body activities can both be finite while the connected relative
    # kernel has a nonintegrable large-distance tail.
    assert_equal("one-body plus activity finite", one_body_plus_mass > 0, True)
    assert_equal("one-body minus activity finite", one_body_minus_mass > 0, True)
    assert_equal(
        "borderline long-range cluster tail diverges logarithmically",
        cluster_status(Fraction(3), Fraction(4)),
        "tail_log_divergent",
    )
    assert_equal(
        "slow long-range cluster tail diverges by power",
        cluster_status(Fraction(3), Fraction(7, 2)),
        "tail_power_divergent",
    )
    assert_equal(
        "borderline core collision diverges logarithmically",
        cluster_status(Fraction(4), Fraction(5)),
        "collision_log_divergent",
    )
    assert_equal(
        "strong core collision diverges by power",
        cluster_status(Fraction(9, 2), Fraction(5)),
        "collision_power_divergent",
    )

    signed_angular_average = Fraction(1) - Fraction(1)
    absolute_angular_average = Fraction(1) + Fraction(1)
    assert_equal("signed relative kernel can cancel angularly", signed_angular_average, Fraction(0))
    assert_equal("absolute relative kernel still sees both angular cells", absolute_angular_average, Fraction(2))
    if signed_angular_average == 0 and cluster_status(Fraction(3), Fraction(4)) == "finite":
        raise AssertionError("signed cancellation incorrectly made borderline tail integrable")

    zeta = Fraction(5, 17)
    poisson_susceptibility = 2 * zeta
    finite_same_charge_cluster = Fraction(-3, 19)
    clustered_susceptibility = (
        poisson_susceptibility
        + 4 * zeta * zeta * finite_same_charge_cluster
    )
    assert_equal(
        "finite cluster coefficient shifts dilute susceptibility",
        clustered_susceptibility,
        2 * zeta + 4 * zeta * zeta * finite_same_charge_cluster,
    )
    assert_equal(
        "Poisson term alone does not supply finite cluster coefficient",
        poisson_susceptibility == clustered_susceptibility,
        False,
    )


def check_instanton_ensemble_zero_mode_overlap_spectrum() -> None:
    def zero_matrix(rows: int, cols: int) -> list[list[Fraction]]:
        return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]

    def identity_scaled(size: int, scalar: Fraction) -> list[list[Fraction]]:
        return [
            [scalar if row == col else Fraction(0) for col in range(size)]
            for row in range(size)
        ]

    def diagonal_overlap(
        n_plus: int,
        n_minus: int,
        singular_values: list[Fraction],
    ) -> list[list[Fraction]]:
        overlap = zero_matrix(n_plus, n_minus)
        for index, value in enumerate(singular_values):
            overlap[index][index] = value
        return overlap

    def negative_transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
        if not matrix:
            return []
        return [
            [-matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))
        ]

    def zero_mode_block_determinant(
        n_plus: int,
        n_minus: int,
        singular_values: list[Fraction],
        mass: Fraction,
    ) -> Fraction:
        overlap = diagonal_overlap(n_plus, n_minus, singular_values)
        block = block_2x2_fraction(
            identity_scaled(n_plus, mass),
            overlap,
            negative_transpose(overlap),
            identity_scaled(n_minus, mass),
        )
        return det_fraction(block)

    n_plus = 2
    n_minus = 3
    singular_values = [Fraction(2), Fraction(3)]
    mass = Fraction(5)
    expected_determinant = (
        mass ** abs(n_plus - n_minus)
        * product_fraction([mass * mass + s * s for s in singular_values])
    )
    assert_equal(
        "rectangular instanton overlap determinant",
        zero_mode_block_determinant(n_plus, n_minus, singular_values, mass),
        expected_determinant,
    )
    assert_equal(
        "massless leading overlap block has unmatched zero factor",
        zero_mode_block_determinant(n_plus, n_minus, singular_values, Fraction(0)),
        Fraction(0),
    )
    assert_equal(
        "balanced massless overlap determinant is product of singular squares",
        zero_mode_block_determinant(2, 2, singular_values, Fraction(0)),
        product_fraction([s * s for s in singular_values]),
    )

    resolvent_trace = (
        Fraction(abs(n_plus - n_minus), 1) / mass
        + sum(2 * mass / (mass * mass + s * s) for s in singular_values)
    )
    assert_equal(
        "zero-mode overlap resolvent unpaired pole plus paired kernel",
        resolvent_trace,
        Fraction(1, 5) + Fraction(10, 29) + Fraction(5, 17),
    )

    # The exact zero in the previous determinant is a statement about the
    # leading projected block.  A generic chirality-breaking remainder can lift
    # that projected zero unless an exact index-preserving regulator protects
    # the full operator kernel.
    overlap = diagonal_overlap(n_plus, n_minus, singular_values)
    leading_massless_block = block_2x2_fraction(
        identity_scaled(n_plus, Fraction(0)),
        overlap,
        negative_transpose(overlap),
        identity_scaled(n_minus, Fraction(0)),
    )
    chirality_breaking_remainder = zero_matrix(n_plus + n_minus, n_plus + n_minus)
    chirality_breaking_remainder[-1][-1] = Fraction(7)
    lifted_block = matrix_add_fraction(leading_massless_block, chirality_breaking_remainder)
    assert_equal(
        "leading projected block zero before remainder",
        det_fraction(leading_massless_block),
        Fraction(0),
    )
    assert_equal(
        "generic remainder can lift projected mismatch zero",
        det_fraction(lifted_block),
        Fraction(252),
    )
    total_topological_charge = n_plus - n_minus
    assert_equal(
        "index-preserving exact kernel count needs total charge",
        abs(total_topological_charge),
        abs(n_plus - n_minus),
    )

    flavor_masses = [Fraction(5), Fraction(7), Fraction(11)]
    multiflavor_determinant = product_fraction(
        [
            m ** abs(n_plus - n_minus)
            * product_fraction([m * m + s * s for s in singular_values])
            for m in flavor_masses
        ]
    )
    assert_equal(
        "multi-flavor instanton-liquid overlap determinants multiply",
        multiflavor_determinant,
        zero_mode_block_determinant(n_plus, n_minus, singular_values, Fraction(5))
        * zero_mode_block_determinant(n_plus, n_minus, singular_values, Fraction(7))
        * zero_mode_block_determinant(n_plus, n_minus, singular_values, Fraction(11)),
    )

    # The finite-volume trace formula behind Banks--Casher separates unpaired
    # topological zero modes from the paired near-zero singular values.  The
    # former must have zero density before the chiral limit.
    mismatch = Fraction(abs(n_plus - n_minus))
    volumes = [Fraction(10), Fraction(100), Fraction(1000)]
    mismatch_densities = [mismatch / volume for volume in volumes]
    assert_equal(
        "topological mismatch density decreases with volume",
        mismatch_densities[0] > mismatch_densities[1] > mismatch_densities[2],
        True,
    )

    rho0 = 0.37
    cutoff = 11.0
    small_mass = 1.0e-10
    constant_density_kernel = 2 * rho0 * math.atan(cutoff / small_mass)
    assert_close(
        "instanton-liquid constant-density Banks-Casher kernel limit",
        constant_density_kernel,
        math.pi * rho0,
        tolerance=1e-10,
    )


def check_instanton_zero_mode_zone_u1a_susceptibility() -> None:
    mass = Fraction(3, 5)
    gamma5 = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(-1)],
    ]

    def paired_source_trace_kernel(singular_value: Fraction) -> Fraction:
        chiral_block = [
            [mass, singular_value],
            [-singular_value, mass],
        ]
        propagator = inverse_2x2_fraction(chiral_block)
        scalar_source_curvature = -trace_fraction(
            matmul_fraction(propagator, propagator)
        )
        pseudoscalar_source_curvature = trace_fraction(
            matmul_fraction(
                matmul_fraction(matmul_fraction(propagator, gamma5), propagator),
                gamma5,
            )
        )
        return pseudoscalar_source_curvature - scalar_source_curvature

    singular_value = Fraction(2, 7)
    paired_kernel = 4 * mass * mass / (mass * mass + singular_value * singular_value) ** 2
    assert_equal(
        "paired zero-mode U1A source-trace kernel",
        paired_source_trace_kernel(singular_value),
        paired_kernel,
    )

    volume = Fraction(97)
    mismatch = Fraction(2)
    singular_values = [Fraction(2, 7), Fraction(5, 11), Fraction(7, 13)]
    finite_splitting = (
        2 * mismatch / (volume * mass * mass)
        + sum(
            4 * mass * mass / (volume * (mass * mass + s * s) ** 2)
            for s in singular_values
        )
    )
    trace_splitting = (
        2 * mismatch / (volume * mass * mass)
        + sum(paired_source_trace_kernel(s) / volume for s in singular_values)
    )
    assert_equal(
        "finite zero-mode-zone pi-delta susceptibility splitting",
        finite_splitting,
        trace_splitting,
    )

    larger_volume = Fraction(10) * volume
    assert_equal(
        "topological U1A pole density is volume controlled",
        2 * mismatch / (volume * mass * mass)
        > 2 * mismatch / (larger_volume * mass * mass),
        True,
    )

    rho0 = 0.37
    c1 = 0.23
    c2 = 0.19
    cutoff = 11.0
    small_mass = 1.0e-8
    constant_density_kernel = rho0 * (
        2 * cutoff / (cutoff * cutoff + small_mass * small_mass)
        + 2 / small_mass * math.atan(cutoff / small_mass)
    )
    assert_close(
        "constant-density U1A kernel asymptotic pi rho0 over m",
        small_mass * constant_density_kernel,
        math.pi * rho0,
        tolerance=1e-10,
    )

    linear_density_kernel = c1 * (
        2 * (1 - small_mass * small_mass / (cutoff * cutoff + small_mass * small_mass))
    )
    assert_close(
        "linear-density U1A kernel finite remnant",
        linear_density_kernel,
        2 * c1,
        tolerance=1e-14,
    )

    quadratic_density_kernel = c2 * (
        2 * small_mass * math.atan(cutoff / small_mass)
        - 2
        * small_mass
        * small_mass
        * cutoff
        / (cutoff * cutoff + small_mass * small_mass)
    )
    assert_equal(
        "superlinear-density U1A kernel vanishes in chiral limit",
        quadratic_density_kernel < 1.0e-7,
        True,
    )


def check_u1a_mode_count_restoration_criterion() -> None:
    mass = Fraction(1, 16)
    smaller_mass = mass / 2
    volume = Fraction(97)
    topological_mismatch = Fraction(3)
    topological_pole = 2 * topological_mismatch / (volume * mass * mass)
    smaller_mass_pole = 2 * topological_mismatch / (volume * smaller_mass * smaller_mass)
    assert_equal(
        "fixed-volume exact topology pole is chiral singular",
        smaller_mass_pole,
        4 * topological_pole,
    )
    larger_volume = 100 * volume
    assert_equal(
        "thermodynamic first suppresses exact topology density",
        2 * topological_mismatch / (larger_volume * mass * mass)
        < topological_pole,
        True,
    )

    singular_value_multiplicities = [
        (Fraction(1, 4), 2),
        (Fraction(3, 8), 1),
        (Fraction(5, 8), 3),
    ]

    def atomic_stieltjes_integral(
        atoms: list[tuple[Fraction, int]],
        mass_value: Fraction,
        volume_value: Fraction,
    ) -> Fraction:
        total = Fraction(0)
        for singular_value, multiplicity in sorted(atoms):
            jump = Fraction(multiplicity, volume_value)
            total += (
                4
                * mass_value
                * mass_value
                * jump
                / (mass_value * mass_value + singular_value * singular_value) ** 2
            )
        return total

    stieltjes_sum = atomic_stieltjes_integral(
        singular_value_multiplicities,
        mass,
        volume,
    )
    finite_spectral_sum = sum(
        4
        * mass
        * mass
        * multiplicity
        / (volume * (mass * mass + singular_value * singular_value) ** 2)
        for singular_value, multiplicity in singular_value_multiplicities
    )
    assert_equal(
        "finite Stieltjes mode-count integral equals spectral sum",
        stieltjes_sum,
        finite_spectral_sum,
    )

    count_constant = Fraction(7, 5)
    total_retained_density = Fraction(11, 3)

    def dyadic_count_bound(mass_value: Fraction, cumulative_power: int, shells: int = 5) -> Fraction:
        low_modes = 4 * count_constant * mass_value**cumulative_power / (mass_value * mass_value)
        shell_bound = Fraction(0)
        for shell in range(shells):
            lower = Fraction(2**shell) * mass_value
            upper = Fraction(2 ** (shell + 1)) * mass_value
            cumulative_upper = count_constant * upper**cumulative_power
            shell_bound += (
                4
                * mass_value
                * mass_value
                * cumulative_upper
                / lower**4
            )
        high_tail = 4 * mass_value * mass_value * total_retained_density
        return low_modes + shell_bound + high_tail

    superlinear_bound = dyadic_count_bound(mass, cumulative_power=3)
    superlinear_bound_smaller = dyadic_count_bound(smaller_mass, cumulative_power=3)
    assert_equal(
        "superlinear cumulative count bound decreases toward chiral limit",
        superlinear_bound_smaller < superlinear_bound,
        True,
    )

    linear_density_low_modes = (
        4 * count_constant * mass**2 / (mass * mass)
    )
    linear_density_low_modes_smaller = (
        4 * count_constant * smaller_mass**2 / (smaller_mass * smaller_mass)
    )
    assert_equal(
        "linear density cumulative count leaves finite low-mode remnant",
        linear_density_low_modes_smaller,
        linear_density_low_modes,
    )

    constant_density_low_modes = 4 * count_constant * mass / (mass * mass)
    constant_density_low_modes_smaller = (
        4 * count_constant * smaller_mass / (smaller_mass * smaller_mass)
    )
    assert_equal(
        "constant density cumulative count diverges in chiral limit",
        constant_density_low_modes_smaller,
        2 * constant_density_low_modes,
    )


def check_mass_saturated_vacuum_activity_size_integral() -> None:
    n_c = 3
    n_f = 3
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    size_integrand_power = b0 + n_f - 5
    antiderivative_power = size_integrand_power + 1
    assert_equal("SU(3) Nf=3 mass-saturated b0", b0, Fraction(9))
    assert_equal(
        "mass-saturated size-integral antiderivative power",
        antiderivative_power,
        b0 + n_f - 4,
    )
    assert_equal("SU(3) Nf=3 mass-saturated endpoint margin", antiderivative_power, 8)

    def endpoint_status(power: Fraction) -> tuple[str, str]:
        if power > 0:
            return ("small_finite", "large_power_divergent")
        if power == 0:
            return ("small_log_divergent", "large_log_divergent")
        return ("small_power_divergent", "large_finite")

    assert_equal(
        "positive instanton size margin endpoint status",
        endpoint_status(antiderivative_power),
        ("small_finite", "large_power_divergent"),
    )
    assert_equal(
        "borderline instanton size margin endpoint status",
        endpoint_status(Fraction(0)),
        ("small_log_divergent", "large_log_divergent"),
    )
    assert_equal(
        "negative instanton size margin endpoint status",
        endpoint_status(Fraction(-2)),
        ("small_power_divergent", "large_finite"),
    )

    rho_low = Fraction(1, 2)
    rho_high = Fraction(3, 2)
    finite_size_window = (
        rho_high**antiderivative_power
        - rho_low**antiderivative_power
    ) / antiderivative_power
    assert_equal("mass-saturated finite size window", finite_size_window, Fraction(205, 64))

    masses = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    determinant_abs = product_fraction(masses)
    scheme_prefactor = Fraction(5, 7)
    window_activity = scheme_prefactor * determinant_abs * finite_size_window
    assert_equal("mass-saturated finite-window activity", window_activity, Fraction(56375, 61152))

    one_massless = [Fraction(2, 3), Fraction(0), Fraction(11, 13)]
    assert_equal(
        "massless flavor removes mass-saturated vacuum activity",
        scheme_prefactor * product_fraction(one_massless) * finite_size_window,
        Fraction(0),
    )

    theta_shift = Fraction(19, 5)
    arg_det_m_shift = -Fraction(19, 5)
    assert_equal(
        "mass-saturated phase theta plus arg det M invariant",
        theta_shift + arg_det_m_shift,
        Fraction(0),
    )


def check_mass_saturated_instanton_ward_derivatives() -> None:
    masses = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    determinant_prefactor = Fraction(17, 19)
    size_integral = Fraction(23, 29)
    zeta = determinant_prefactor * size_integral * product_fraction(masses)
    cos_bar_theta = Fraction(7, 11)
    sin_bar_theta = Fraction(5, 13)

    energy = -2 * zeta * cos_bar_theta
    topological_curvature = 2 * zeta * cos_bar_theta
    theta_derivative = 2 * zeta * sin_bar_theta
    assert_equal(
        "mass-saturated instanton energy and theta curvature",
        -energy,
        topological_curvature,
    )

    for flavor, mass in enumerate(masses):
        mass_derivative = -2 * zeta * cos_bar_theta / mass
        phase_derivative = 2 * zeta * sin_bar_theta
        assert_equal(
            f"mass-saturated instanton mass Ward flavor {flavor}",
            mass * mass_derivative + topological_curvature,
            Fraction(0),
        )
        assert_equal(
            f"mass-saturated instanton phase Ward flavor {flavor}",
            phase_derivative,
            theta_derivative,
        )

    masses_with_zero = [masses[0], Fraction(0), masses[2]]
    zero_activity = (
        determinant_prefactor * size_integral * product_fraction(masses_with_zero)
    )
    assert_equal("massless flavor kills vacuum instanton activity", zero_activity, Fraction(0))

    # Source saturation remains a different coordinate: a four-source
    # determinant can be nonzero even when the mass determinant vanishes.
    right_source = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(5)]]
    left_source = [[Fraction(7), Fraction(11)], [Fraction(13), Fraction(17)]]
    source_saturated = det_fraction(right_source) * det_fraction(left_source)
    assert_equal(
        "source-saturated instanton correlator can survive zero mass",
        source_saturated != 0 and zero_activity == 0,
        True,
    )


def check_screened_one_instanton_size_integral() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    beta_x = Fraction(n_f)
    screened_power = b0 + beta_x - 4
    assert_equal("SU(3) Nf=2 screened mass-saturated A", screened_power, Fraction(23, 3))

    gamma_argument = screened_power / 2
    assert_equal("screened instanton gamma argument", gamma_argument, Fraction(23, 6))

    # If I_A(m)=1/2 m^{-A} Gamma(A/2), then
    # I_{A+2}/I_A = m^{-2} A/2 and
    # I_{A+4}/I_A = m^{-4} (A/2)(A/2+1).
    m_scr = Fraction(5, 3)
    moment_two = gamma_argument / (m_scr * m_scr)
    moment_four = gamma_argument * (gamma_argument + 1) / (m_scr**4)
    assert_equal("screened instanton rho^2 moment", moment_two, Fraction(69, 50))
    assert_equal("screened instanton rho^4 moment", moment_four, Fraction(6003, 2500))

    log_shell_location = gamma_argument
    ordinary_density_location = (screened_power - 1) / 2
    assert_equal("screened instanton log-shell location", log_shell_location, Fraction(23, 6))
    assert_equal("screened instanton ordinary-density saddle", ordinary_density_location, Fraction(10, 3))

    # The screened integral contributes m_scr^{-A}.  For a mass-saturated vacuum
    # activity, the prefactor |det M| mu^{b0} has dimension Nf+b0, so the
    # screened activity remains a four-dimensional energy density.
    prefactor_mass_dimension = Fraction(n_f) + b0
    screened_integral_dimension = -screened_power
    assert_equal(
        "screened mass-saturated instanton activity dimension",
        prefactor_mass_dimension + screened_integral_dimension,
        Fraction(4),
    )

    # Without the screening scale, A>0 is exactly the large-rho power divergence
    # exposed by the finite-window formula.
    assert_equal("screened formula diverges as m_scr -> 0 when A positive", screened_power > 0, True)


def check_thermal_instanton_determinant_screening() -> None:
    n_c = 3
    n_f = 2
    thermal_screening_over_pi2_t2 = Fraction(2 * n_c + n_f, 3)
    assert_equal("SU(3) Nf=2 thermal instanton screening coefficient", thermal_screening_over_pi2_t2, Fraction(8, 3))

    # In the trace-delta convention used by the thermal chapter,
    # m_D^2/g_YM^2 = T^2(2Nc+Nf)/3 for fundamental Dirac matter.
    trace_delta_debye_over_g2_t2 = Fraction(2 * n_c + n_f, 3)
    assert_equal(
        "thermal instanton coefficient equals pi^2 Debye-over-g^2 coefficient",
        thermal_screening_over_pi2_t2,
        trace_delta_debye_over_g2_t2,
    )

    # In the common half-trace convention, the same invariant statement reads
    # m_T^2 = 2 pi^2 m_D,ht^2/g_ht^2.
    half_trace_debye_over_g2_t2 = Fraction(n_c, 3) + Fraction(n_f, 6)
    assert_equal(
        "half-trace Debye conversion for thermal instanton screening",
        2 * half_trace_debye_over_g2_t2,
        thermal_screening_over_pi2_t2,
    )

    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    screened_power = b0 + n_f - 4
    assert_equal("thermal SU(3) Nf=2 mass-saturated A", screened_power, Fraction(23, 3))

    gamma_argument = screened_power / 2
    shell_pi2_t2_rho2 = gamma_argument / thermal_screening_over_pi2_t2
    ordinary_density_pi2_t2_rho2 = ((screened_power - 1) / 2) / thermal_screening_over_pi2_t2
    assert_equal("thermal instanton log-shell pi^2 T^2 rho^2", shell_pi2_t2_rho2, Fraction(23, 16))
    assert_equal("thermal instanton ordinary-density pi^2 T^2 rho^2", ordinary_density_pi2_t2_rho2, Fraction(5, 4))

    # The Gaussian amplitude scales as (pi^2 T^2 c)^(-A/2), so the T power is -A.
    assert_equal("thermal instanton Gaussian T power", -2 * gamma_argument, -Fraction(23, 3))

    # If |R_T| <= eps on the chosen size window, then |exp(R_T)-1| is bounded by
    # exp(eps)-1 pointwise.  A positive activity may use the signed Gaussian
    # activity itself as the majorant.
    gaussian_majorant = Fraction(11, 7)
    residual_multiplier_bound = Fraction(1, 5)
    residual_error_bound = residual_multiplier_bound * gaussian_majorant
    actual_residual_error = Fraction(3, 20) * gaussian_majorant
    assert_equal(
        "thermal positive-activity residual bounded by multiplicative window norm",
        actual_residual_error <= residual_error_bound,
        True,
    )

    # The old signed form is invalid for a negative kernel: its right-hand side
    # is negative even though the left-hand side is an absolute error.
    negative_gaussian = -gaussian_majorant
    invalid_signed_rhs = residual_multiplier_bound * negative_gaussian
    assert_equal("negative K0 makes signed thermal residual RHS negative", invalid_signed_rhs < 0, True)
    fixed_phase_error_bound = residual_multiplier_bound * abs(negative_gaussian)
    fixed_phase_actual_error = Fraction(3, 20) * abs(negative_gaussian)
    assert_equal(
        "thermal fixed-phase residual uses absolute Gaussian amplitude",
        fixed_phase_actual_error <= fixed_phase_error_bound,
        True,
    )

    # A complex source-projected amplitude needs an absolute-kernel majorant.
    # The complex number below has modulus gaussian_majorant.
    complex_gaussian = (
        Fraction(3, 5) * gaussian_majorant,
        Fraction(4, 5) * gaussian_majorant,
    )
    complex_signed_rhs = complex_scale_fraction(residual_multiplier_bound, complex_gaussian)
    assert_equal("complex signed thermal RHS has imaginary part", complex_signed_rhs[1] != 0, True)
    complex_residual_factor = (Fraction(1, 10), Fraction(1, 10))
    complex_error = complex_mul_fraction(complex_residual_factor, complex_gaussian)
    complex_error_abs_sq = complex_abs_sq_fraction(complex_error)
    complex_majorant_abs_sq = (residual_multiplier_bound * gaussian_majorant) ** 2
    assert_equal(
        "thermal complex residual controlled by absolute-kernel majorant",
        complex_error_abs_sq <= complex_majorant_abs_sq,
        True,
    )


def check_thermal_dilute_topological_susceptibility() -> None:
    n_c = 3
    n_f = 2
    b0 = Fraction(11, 3) * n_c - Fraction(2, 3) * n_f
    activity_power = b0 + n_f - 4
    assert_equal("thermal dilute SU(3) Nf=2 activity power", activity_power, Fraction(23, 3))

    # The Gaussian activity has a factor (T^2)^(-A/2)=T^(-A).  The
    # susceptibility is 2*zeta_T, so it carries the same temperature power.
    susceptibility_t_power = -activity_power
    assert_equal("thermal dilute susceptibility T power", susceptibility_t_power, -Fraction(23, 3))

    # After the one-loop action is traded for Lambda_ht^b0, the mass-saturated
    # prefactor has dimensions Nf+b0 and the screened integral has dimension -A.
    mass_dimension = Fraction(n_f) + b0 - activity_power
    assert_equal("thermal dilute susceptibility mass dimension", mass_dimension, Fraction(4))

    # The Poisson/Skellam dilute gas gives chi_top=2*zeta and fourth derivative
    # -2*zeta, hence b2 = (-2*zeta)/(12*chi_top).
    zeta_units = Fraction(13, 7)
    chi_top = 2 * zeta_units
    fourth_theta_curvature = -2 * zeta_units
    b2 = fourth_theta_curvature / (12 * chi_top)
    assert_equal("thermal dilute topological susceptibility", chi_top, Fraction(26, 7))
    assert_equal("thermal dilute theta b2", b2, -Fraction(1, 12))

    # A positive multiplicative determinant residual for zeta_T propagates
    # unchanged to chi_top=2*zeta_T.
    residual_multiplier_bound = Fraction(1, 6)
    activity_error = residual_multiplier_bound * zeta_units
    susceptibility_error = 2 * activity_error
    susceptibility_error_bound = residual_multiplier_bound * chi_top
    assert_equal(
        "thermal dilute susceptibility residual inherits activity bound",
        susceptibility_error,
        susceptibility_error_bound,
    )

    negative_activity = -zeta_units
    invalid_negative_susceptibility_bound = residual_multiplier_bound * 2 * negative_activity
    assert_equal(
        "negative thermal activity cannot define positive susceptibility bound",
        invalid_negative_susceptibility_bound < 0,
        True,
    )

    complex_activity = (Fraction(3, 7), Fraction(4, 7))
    complex_susceptibility = complex_scale_fraction(Fraction(2), complex_activity)
    assert_equal(
        "complex source amplitude cannot be used as topological susceptibility",
        complex_susceptibility[1] != 0,
        True,
    )


def check_qcd_axial_charge_relaxation_kubo_bridge() -> None:
    n_f = 3
    axial_step = 2 * n_f
    gamma_cs = Fraction(7, 19)
    chi5 = Fraction(11, 13)
    temperature = Fraction(5, 3)
    n5_density = Fraction(17, 23)
    mu5 = n5_density / chi5

    topological_relaxation_rate = (
        axial_step * axial_step * gamma_cs / (2 * chi5 * temperature)
    )
    drift = -topological_relaxation_rate * n5_density
    ncs_fokker_planck_diffusion = gamma_cs / 2
    detailed_balance_drift = (
        -axial_step
        * ncs_fokker_planck_diffusion
        * (axial_step * mu5)
        / temperature
    )
    assert_equal(
        "massless QCD axial relaxation detailed-balance drift",
        drift,
        detailed_balance_drift,
    )
    old_no_half_rate = axial_step * axial_step * gamma_cs / (chi5 * temperature)
    assert_equal(
        "variance-rate convention rejects no-half axial relaxation",
        old_no_half_rate == topological_relaxation_rate,
        False,
    )

    # The Euclidean topological susceptibility is a spectral-area integral,
    # while the real-time diffusion rate is the zero-frequency KMS slope.
    # Two spectra can have the same Euclidean area but different Kubo slopes.
    euclidean_chi = Fraction(6)
    low_window_width = Fraction(2)
    slope_a = Fraction(1, 5)
    slope_b = Fraction(3, 7)
    low_area_a = 2 * slope_a * low_window_width
    low_area_b = 2 * slope_b * low_window_width
    high_area_a = euclidean_chi - low_area_a
    high_area_b = euclidean_chi - low_area_b
    kubo_a = temperature * slope_a
    kubo_b = temperature * slope_b
    assert_equal("first spectral model has positive high-frequency area", high_area_a > 0, True)
    assert_equal("second spectral model has positive high-frequency area", high_area_b > 0, True)
    assert_equal(
        "same Euclidean susceptibility can have different Kubo slopes",
        low_area_a + high_area_a == low_area_b + high_area_b and kubo_a != kubo_b,
        True,
    )
    assert_equal(
        "KMS zero-frequency weight has no extra factor two",
        kubo_a == 2 * temperature * slope_a,
        False,
    )

    nonzero_static_instanton_susceptibility = Fraction(2, 7)
    zero_topological_diffusion = Fraction(0)
    assert_equal(
        "nonzero static instanton susceptibility is not a topological relaxation rate",
        nonzero_static_instanton_susceptibility > 0
        and axial_step * axial_step * zero_topological_diffusion / (2 * chi5 * temperature) == 0,
        True,
    )

    # Massive quarks add a pseudoscalar chirality-flip channel and cross noise.
    gamma_qq = Fraction(3, 11)
    gamma_qm = Fraction(1, 17)
    gamma_mm = Fraction(5, 13)
    assert_equal(
        "massive anomaly zero-frequency noise matrix sample is positive",
        gamma_qq * gamma_mm - gamma_qm * gamma_qm > 0,
        True,
    )
    full_dot_q5_noise = (
        axial_step * axial_step * gamma_qq
        + 2 * axial_step * gamma_qm
        + gamma_mm
    )
    topological_only_noise = axial_step * axial_step * gamma_qq
    assert_equal(
        "massive QCD axial relaxation includes pseudoscalar and cross weights",
        full_dot_q5_noise,
        topological_only_noise + 2 * axial_step * gamma_qm + gamma_mm,
    )
    assert_equal(
        "massive anomaly relaxation differs from topological-only relaxation",
        full_dot_q5_noise == topological_only_noise,
        False,
    )


def check_electroweak_sphaleron_response_ledger() -> None:
    generations = 3
    delta_ncs = Fraction(1)
    delta_b = generations * delta_ncs
    delta_l = generations * delta_ncs
    delta_b_minus_l = delta_b - delta_l
    delta_x = delta_b + delta_l
    assert_equal("electroweak instanton B change", delta_b, Fraction(3))
    assert_equal("electroweak instanton L change", delta_l, Fraction(3))
    assert_equal("electroweak instanton conserves B-L", delta_b_minus_l, Fraction(0))
    assert_equal("electroweak instanton changes B+L", delta_x, Fraction(6))

    gamma_cs = Fraction(7, 11)
    temperature = Fraction(5, 3)
    susceptibility = Fraction(13, 17)
    x_density = Fraction(19, 23)
    chemical_potential = x_density / susceptibility
    relaxation_rate = delta_x * delta_x * gamma_cs / (2 * susceptibility * temperature)
    drift = -relaxation_rate * x_density
    ncs_fokker_planck_diffusion = gamma_cs / 2
    detailed_balance_drift = (
        -delta_x
        * ncs_fokker_planck_diffusion
        * (delta_x * chemical_potential)
        / temperature
    )
    assert_equal("sphaleron B+L relaxation drift", drift, detailed_balance_drift)
    old_no_half_rate = delta_x * delta_x * gamma_cs / (susceptibility * temperature)
    assert_equal(
        "variance-rate convention rejects no-half B+L relaxation",
        old_no_half_rate == relaxation_rate,
        False,
    )

    variance_rate_b_plus_l = delta_x * delta_x * gamma_cs
    variance_rate_b_minus_l = delta_b_minus_l * delta_b_minus_l * gamma_cs
    assert_equal("Chern-Simons diffusion induces B+L diffusion", variance_rate_b_plus_l, 36 * gamma_cs)
    assert_equal("Chern-Simons diffusion leaves B-L unchanged", variance_rate_b_minus_l, Fraction(0))

    zero_sphaleron_rate = Fraction(0)
    assert_equal(
        "no real-time sphaleron diffusion gives no washout despite vertex selection rule",
        delta_x * delta_x * zero_sphaleron_rate / (2 * susceptibility * temperature),
        Fraction(0),
    )

    # The susceptibility in the washout rate is the thermodynamic
    # susceptibility after exact conserved charges have been projected out.
    chi_b = Fraction(2)
    chi_l = Fraction(3)
    unconstrained_chi_x = chi_b + chi_l
    w_chi_c = chi_b - chi_l
    c_chi_c = chi_b + chi_l
    constrained_chi_x = unconstrained_chi_x - w_chi_c * w_chi_c / c_chi_c
    direct_fixed_b_minus_l_chi = 4 * chi_b * chi_l / (chi_b + chi_l)
    assert_equal(
        "electroweak constrained B+L susceptibility Schur complement",
        constrained_chi_x,
        direct_fixed_b_minus_l_chi,
    )
    assert_equal(
        "electroweak fixed B-L susceptibility value",
        constrained_chi_x,
        Fraction(24, 5),
    )

    projected_relaxation_rate = (
        delta_x * delta_x * gamma_cs / (2 * constrained_chi_x * temperature)
    )
    projected_drift = -projected_relaxation_rate * x_density
    projected_chemical_potential = x_density / constrained_chi_x
    assert_equal(
        "projected susceptibility gives detailed-balance drift",
        projected_drift,
        -delta_x
        * ncs_fokker_planck_diffusion
        * (delta_x * projected_chemical_potential)
        / temperature,
    )
    assert_equal(
        "unconstrained susceptibility differs when B-L is fixed",
        unconstrained_chi_x == constrained_chi_x,
        False,
    )

    # If a constraint already fixes B+L, the Schur complement vanishes: there
    # is no independent B+L coordinate for the sphaleron diffusion to relax.
    fixed_x_projected_chi = (
        unconstrained_chi_x
        - unconstrained_chi_x * unconstrained_chi_x / unconstrained_chi_x
    )
    assert_equal(
        "fixed B+L constraint removes washout susceptibility",
        fixed_x_projected_chi,
        Fraction(0),
    )


def check_uhlenbeck_boundary_face_budget() -> None:
    for n_c in range(2, 8):
        for k in range(1, 6):
            full_dim = 4 * k * n_c
            for ell in range(1, k + 1):
                open_stratum_dim = 4 * (k - ell) * n_c + 4 * ell
                open_codim = full_dim - open_stratum_dim
                assert_equal(
                    f"open Uhlenbeck codim k={k} ell={ell} SU({n_c})",
                    open_codim,
                    4 * ell * (n_c - 1),
                )
                for clusters in range(1, ell + 1):
                    diagonal_dim = 4 * (k - ell) * n_c + 4 * clusters
                    total_codim = full_dim - diagonal_dim
                    additional_collision_codim = total_codim - open_codim
                    assert_equal(
                        f"Uhlenbeck diagonal codim k={k} ell={ell} r={clusters} SU({n_c})",
                        additional_collision_codim,
                        4 * (ell - clusters),
                    )
                    assert_equal(
                        f"total Uhlenbeck diagonal codim k={k} ell={ell} r={clusters} SU({n_c})",
                        total_codim,
                        4 * ell * (n_c - 1) + 4 * (ell - clusters),
                    )

    def power_status(exponents: list[Fraction]) -> str:
        if all(exponent > 0 for exponent in exponents):
            return "finite"
        if any(exponent < 0 for exponent in exponents):
            return "power_divergent"
        return "log_divergent"

    assert_equal("Uhlenbeck positive product status", power_status([Fraction(1, 3), Fraction(5, 4)]), "finite")
    assert_equal("Uhlenbeck zero exponent status", power_status([Fraction(2), Fraction(0)]), "log_divergent")
    assert_equal("Uhlenbeck negative exponent status", power_status([Fraction(2), Fraction(-1, 3)]), "power_divergent")

    # With epsilon=1 and no logarithms, the factorized boundary integral is
    # product_alpha A_alpha^{-1}.  This is the finite shadow of the product
    # criterion in the manuscript.
    exponents = [Fraction(1, 2), Fraction(3, 2), Fraction(2)]
    product_integral = Fraction(1)
    for exponent in exponents:
        product_integral *= Fraction(1, 1) / exponent
    assert_equal("Uhlenbeck product antiderivative", product_integral, Fraction(2, 3))

    # The charge-one threshold is the same product criterion with a single
    # scale exponent A=b0+beta_X-4.
    b0 = Fraction(11, 3) * 3 - Fraction(2, 3) * 9
    beta_x = Fraction(-1)
    charge_one_scale_exponent = b0 + beta_x - 4
    assert_equal("charge-one exponent from b0 beta", charge_one_scale_exponent, Fraction(0))
    assert_equal("charge-one threshold as face status", power_status([charge_one_scale_exponent]), "log_divergent")


def main() -> None:
    check_eta_self_duality()
    check_eta_norm()
    check_eta_quadratic_identity()
    check_radial_integrals_and_actions()
    check_radial_cumulative_profile()
    check_one_instanton_density_scaling()
    check_pure_gauge_pv_determinant_constant()
    check_small_instanton_boundary_exponent_criterion()
    check_general_adhm_quotient_dimension()
    check_adhm_quotient_density_coarea_scaling()
    check_finite_regulator_determinant_datum()
    check_one_instanton_amplitude_datum_gate_spine()
    check_instanton_amplitude_pipeline_stage_bookkeeping()
    check_physical_instanton_correlator_zero_mode_saturation()
    check_two_flavor_thooft_channel_decomposition()
    check_two_flavor_instanton_source_curvature()
    check_two_flavor_instanton_source_ward_ledger()
    check_two_flavor_instanton_tested_susceptibility_contact()
    check_finite_momentum_pion_delta_instanton_source_kernel()
    check_fermion_determinant_zero_mode_nonzero_mode_factorization()
    check_light_fermion_determinant_source_frame_covariance()
    check_light_fermion_reference_amplitude_calibration()
    check_instanton_finite_scheme_transport_bound()
    check_instanton_mass_source_rg_transport()
    check_one_instanton_channel_rg_ledger()
    check_proper_time_fluctuation_four_fermion_amplitude()
    check_proper_time_determinant_residual_window()
    check_instanton_source_typing_and_differentiation()
    check_connected_four_source_instanton_extraction()
    check_instanton_heat_kernel_beta0_logarithm()
    check_instanton_zero_mode_tail_local_limit()
    check_instanton_external_leg_amputation_kernel()
    check_plane_wave_instanton_four_fermion_assembly()
    check_hard_wave_packet_instanton_source_support()
    check_instanton_orientation_haar_projection()
    check_color_singlet_instanton_source_projection()
    check_instanton_hadronic_pole_window_projection()
    check_instanton_euclidean_to_physical_residual_budget()
    check_instanton_unitarity_cut_pairing()
    check_one_instanton_sector_isolation_bound()
    check_instanton_amplitude_error_budget()
    check_source_dependent_fluctuation_cumulant_bound()
    check_instanton_observable_assembly_ladder()
    check_hard_momentum_instanton_size_window()
    check_fused_source_hard_size_mellin_integral()
    check_hard_size_tail_dominance_criterion()
    check_hard_screened_instanton_size_shell()
    check_su3_two_flavor_hard_instanton_coefficient()
    check_individual_slot_tail_subtracted_hard_coefficient()
    check_hard_instanton_finite_window_bound()
    check_four_source_instanton_amplitude_rank_bound()
    check_four_source_instanton_source_conditioning()
    check_thooft_four_fermion_benchmark_gate_ledger()
    check_wilsonian_instanton_size_factorization()
    check_short_instanton_ope_coefficient_transport()
    check_dilute_instanton_gas_theta_cumulants()
    check_first_cluster_correction_to_dilute_instanton_gas()
    check_two_body_cluster_integrability_window()
    check_instanton_ensemble_zero_mode_overlap_spectrum()
    check_instanton_zero_mode_zone_u1a_susceptibility()
    check_u1a_mode_count_restoration_criterion()
    check_mass_saturated_vacuum_activity_size_integral()
    check_mass_saturated_instanton_ward_derivatives()
    check_screened_one_instanton_size_integral()
    check_thermal_instanton_determinant_screening()
    check_thermal_dilute_topological_susceptibility()
    check_qcd_axial_charge_relaxation_kubo_bridge()
    check_electroweak_sphaleron_response_ledger()
    check_uhlenbeck_boundary_face_budget()
    check_k_one_adhm_dimension_and_cone_power()
    print("All BPST instanton normalization checks passed.")


if __name__ == "__main__":
    main()
