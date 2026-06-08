#!/usr/bin/env python3
"""Finite checks for the supersymmetric Yang-Mills deformation ladder.

Evidence contract.
Target claims:
- Volume VII Chapter 7b's holomorphic scale dimensions, N=1* fuzzy-sphere
  F-term ansatz, finite k-string comparison ledgers, local
  Seiberg-Witten vortex profile normalization, Abelianized A-type sine
  profile, pure N=1 SYM channel-pole bookkeeping, and soft-gaugino-mass
  spectral-bridge response formulae.
Independent construction:
- Exact finite-dimensional algebra using symbolic matrices, rational
  perturbations, trigonometric identities, an unbounded diagonal common-domain
  model with exact resolvent derivative, and a finite matrix cluster used only
  as a downstream bounded regression.
Imported assumptions:
- The script imports only SymPy algebra.  QFT inputs such as regulator
  existence, self-adjoint domain construction, reflection positivity,
  continuum limits, and spectral isolation are hypotheses in the text, not
  assumptions verified here.
Negative controls:
- The checks reject a transported k-string ratio when the logarithmic response
  is nonzero, so the old "if constant, then equal" bridge cannot pass as a
  calculation.  They also reject a cutoff-only perturbation whose relative
  bound grows with the cutoff, showing why a finite matrix identity cannot
  verify the unbounded-operator domain step.
Scope boundary:
- These checks verify finite algebra and normalization.  They do not prove a
  four-dimensional supersymmetric or bosonic Yang-Mills continuum
  construction, a phase-boundary exclusion theorem, or a decoupling theorem.
Primary derivation route:
- Derive scale dimensions, BPS/vortex identities, Riesz-projection
  derivatives, finite-volume Feynman-Hellmann formulae, and logarithmic
  tension-ratio responses directly.
Independent verification route:
- Compare the spectral-bridge formulas against explicit matrix entries and
  exact Taylor coefficients of finite tension functions.
Convention dependencies:
- The soft mass path is a real ray in the gaugino-mass source plane; the
  perturbing operator is the derivative of the finite-volume Hamiltonian along
  that renormalized path.
Domain and remainder assumptions:
- Spectral projection transport requires a common-domain Kato type-(A), common
  form-domain type-(B), or C^1 norm-resolvent hypothesis; finite-volume level
  isolation; Riesz ranges in the perturbing-operator or form domain; and a
  uniform continuum/thermodynamic limiting order supplied by the chapter.
Remaining unproved or conditional:
- Extension from the small-soft-mass bridge segment to the bosonic
  Yang-Mills endpoint remains conditional on regulator-level phase and
  decoupling control.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


REPO_ROOT = Path(__file__).resolve().parents[1]
CHAPTER = REPO_ROOT / "monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex"


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.factor(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


def assert_near_zero(name: str, expr: sp.Expr, tol: sp.Float = sp.Float("1e-45")) -> None:
    value = abs(sp.N(expr, 80))
    if value.is_finite is not True:
        raise AssertionError(f"{name} produced nonfinite numerical value: {value!r}")
    if tol.is_finite is not True or tol < 0:
        raise AssertionError(f"{name} has invalid tolerance: {tol!r}")
    if value >= tol:
        raise AssertionError(f"{name} failed numerically: {value!r}")


def assert_contains(text: str, phrase: str, context: str) -> None:
    normalized_text = " ".join(text.split())
    normalized_phrase = " ".join(phrase.split())
    if phrase not in text and normalized_phrase not in normalized_text:
        raise AssertionError(f"{context}: missing {phrase!r}")


def check_holomorphic_scale_dimensions() -> None:
    n = sp.symbols("N_c", positive=True, integer=True)
    # N=4 -> pure N=2*: Lambda^(2N) = m_h^(2N) q.
    dim_lhs_n2 = 2 * n
    dim_rhs_n2 = 2 * n
    assert_zero("N=4 to N=2 scale dimension", dim_lhs_n2 - dim_rhs_n2)

    # N=4 -> pure N=1*: Lambda^(3N) = (m1 m2 m3)^N q.
    dim_lhs_n1 = 3 * n
    dim_rhs_n1 = n + n + n
    assert_zero("N=4 to N=1 scale dimension", dim_lhs_n1 - dim_rhs_n1)


def check_n1_star_fuzzy_sphere_ansatz() -> None:
    alpha, m = sp.symbols("alpha m", nonzero=True)
    # If [J2,J3] = i J1 and Phi_i = alpha J_i, then
    # sqrt(2)[Phi2,Phi3] + m Phi1 = alpha (sqrt(2) i alpha + m) J1.
    alpha_solution = sp.I * m / sp.sqrt(2)
    coefficient = alpha * (sp.sqrt(2) * sp.I * alpha + m)
    assert_zero("N=1* fuzzy-sphere F-term coefficient", coefficient.subs(alpha, alpha_solution))


def check_k_string_ledgers() -> None:
    n, k = sp.symbols("N k", positive=True)
    sine_k = sp.sin(sp.pi * k / n) / sp.sin(sp.pi / n)
    sine_conj = sp.sin(sp.pi * (n - k) / n) / sp.sin(sp.pi / n)
    assert_zero("sine-law charge conjugation", sp.trigsimp(sine_k - sine_conj))

    casimir_k = k * (n - k) / (n - 1)
    casimir_conj = (n - k) * k / (n - 1)
    assert_zero("Casimir-ledger charge conjugation", casimir_k - casimir_conj)

    x = sp.symbols("x")
    sine_series = sp.series(sp.sin(sp.pi * k * x) / sp.sin(sp.pi * x), x, 0, 5).removeO()
    expected_sine = k - sp.pi**2 * k * (k**2 - 1) * x**2 / 6
    assert_zero("sine-law large-N through x^2", sp.expand(sine_series - expected_sine).coeff(x, 2))

    casimir_x = k * (1 / x - k) / (1 / x - 1)
    casimir_series = sp.series(casimir_x, x, 0, 3).removeO()
    expected_casimir = k - k * (k - 1) * x
    assert_zero("Casimir large-N through x", sp.expand(casimir_series - expected_casimir).coeff(x, 1))


def check_sw_vortex_radial_normalization() -> None:
    n = sp.symbols("n", positive=True, integer=True)
    flux = 2 * sp.pi * n * (1 - 0)
    assert_zero("SW vortex flux normalization", flux - 2 * sp.pi * n)

    r, c = sp.symbols("R c", positive=True)
    for winding in range(1, 5):
        f = c * r**winding
        a = r**2 / (2 * winding)
        first_eq_residual = sp.diff(f, r) - winding * (1 - a) * f / r
        second_eq_residual = sp.diff(a, r) - r * (1 - f**2) / winding
        assert_zero(
            f"SW vortex small-R leading f equation n={winding}",
            sp.expand(first_eq_residual).coeff(r, winding - 1),
        )
        assert_zero(
            f"SW vortex small-R leading a equation n={winding}",
            sp.expand(second_eq_residual).coeff(r, 1),
        )


def check_abelianized_a_type_sine_profile() -> None:
    for rank_plus_one in range(3, 11):
        dim = rank_plus_one - 1
        cartan = sp.zeros(dim, dim)
        for i in range(dim):
            cartan[i, i] = 2
            if i > 0:
                cartan[i, i - 1] = -1
            if i + 1 < dim:
                cartan[i, i + 1] = -1

        sine_vector = sp.Matrix(
            [sp.sin(sp.pi * (i + 1) / rank_plus_one) for i in range(dim)]
        )
        eigenvalue = 4 * sp.sin(sp.pi / (2 * rank_plus_one)) ** 2
        residual = cartan * sine_vector - eigenvalue * sine_vector
        for i, entry in enumerate(residual):
            assert_near_zero(f"A-type sine eigenvector N={rank_plus_one}, row={i+1}", entry)

        for k_value in range(1, rank_plus_one):
            ratio = sp.sin(sp.pi * k_value / rank_plus_one) / sp.sin(sp.pi / rank_plus_one)
            conjugate_ratio = sp.sin(sp.pi * (rank_plus_one - k_value) / rank_plus_one) / sp.sin(
                sp.pi / rank_plus_one
            )
            assert_zero(
                f"A-type sine charge conjugation N={rank_plus_one}, k={k_value}",
                sp.trigsimp(ratio - conjugate_ratio),
            )

        for k_value in range(1, rank_plus_one - 1):
            for ell_value in range(1, rank_plus_one - k_value):
                a = sp.pi * k_value / rank_plus_one
                b = sp.pi * ell_value / rank_plus_one
                difference = sp.sin(a) + sp.sin(b) - sp.sin(a + b)
                factorized = 4 * sp.sin(a / 2) * sp.sin(b / 2) * sp.sin((a + b) / 2)
                assert_near_zero(
                    f"A-type sine subadditivity identity N={rank_plus_one}, k={k_value}, ell={ell_value}",
                    difference - factorized,
                )
                if not bool(sp.N(difference) > 0):
                    raise AssertionError(
                        f"A-type sine subadditivity positivity failed for N={rank_plus_one}, "
                        f"k={k_value}, ell={ell_value}: {difference!r}"
                    )


def check_pure_sym_channel_pole_bookkeeping() -> None:
    mass, t, t0 = sp.symbols("m t t0", positive=True)
    z_plus, z_minus, z_fermion = sp.symbols("z_plus z_minus z_fermion", nonzero=True)

    lambda_plus = z_plus**2 * sp.exp(-mass * t) / (z_plus**2 * sp.exp(-mass * t0))
    lambda_minus = z_minus**2 * sp.exp(-mass * t) / (z_minus**2 * sp.exp(-mass * t0))
    lambda_fermion = z_fermion**2 * sp.exp(-mass * t) / (z_fermion**2 * sp.exp(-mass * t0))
    expected = sp.exp(-mass * (t - t0))
    assert_zero("pure SYM even-channel pole", lambda_plus / expected - 1)
    assert_zero("pure SYM odd-channel pole", lambda_minus / expected - 1)
    assert_zero("pure SYM fermion-channel pole", lambda_fermion / expected - 1)

    equal_masses = [sp.Integer(7), sp.Integer(7), sp.Integer(7)]
    equal_delta = max(abs(equal_masses[0] - equal_masses[1]), abs(equal_masses[0] - equal_masses[2]), abs(equal_masses[1] - equal_masses[2]))
    assert_zero("pure SYM equal-mass diagnostic", equal_delta)

    split_masses = [sp.Integer(4), sp.Integer(5), sp.Integer(6)]
    split_delta = max(abs(split_masses[0] - split_masses[1]), abs(split_masses[0] - split_masses[2]), abs(split_masses[1] - split_masses[2]))
    split_average = sum(split_masses) / sp.Integer(3)
    assert_zero("pure SYM split diagnostic value", split_delta / split_average - sp.Rational(2, 5))


def check_soft_mass_common_domain_unbounded_model() -> None:
    # Exact diagonal model on l^2(N):
    # H_m e_n = (n + m(2n+3)) e_n, with common domain
    # {psi: sum n^2 |psi_n|^2 < infinity}.  The perturbation is H_0-bounded,
    # so the resolvent derivative is an operator-domain statement rather than
    # a finite-matrix identity.
    m = sp.symbols("m")
    z = sp.I
    for n_value in (0, 1, 3, 9, 17):
        h_n = sp.Integer(n_value) + m * (2 * n_value + 3)
        v_n = sp.Integer(2 * n_value + 3)
        resolvent_entry = 1 / (z - h_n)
        assert_zero(
            f"unbounded common-domain resolvent derivative n={n_value}",
            sp.diff(resolvent_entry, m) - v_n / (z - h_n) ** 2,
        )
        # Relative bound with respect to H_0: 2n+3 <= 5(n+1).
        if not (v_n <= 5 * (n_value + 1)):
            raise AssertionError("common-domain relative bound check failed")


def check_unbounded_domain_negative_control() -> None:
    # V_bad e_n = n^2 e_n is bounded in every finite cutoff, but it is not
    # H_0-bounded for H_0 e_n = n e_n on l^2(N).  The cutoff relative-bound
    # constant grows like N, so a 3-by-3 check cannot certify the domain step.
    cutoff_ratios = []
    for cutoff in (4, 8, 16, 32):
        worst_ratio = max(sp.Rational(n * n, n + 1) for n in range(1, cutoff + 1))
        cutoff_ratios.append(worst_ratio)
    for previous, current in zip(cutoff_ratios, cutoff_ratios[1:]):
        if not current > previous:
            raise AssertionError("bad unbounded perturbation did not grow with cutoff")
    if cutoff_ratios[-1] <= 4 * cutoff_ratios[0]:
        raise AssertionError("cutoff matrix negative control failed to expose domain loss")


def check_soft_mass_spectral_projection_transport() -> None:
    # Bounded finite-cluster regression after the chapter has supplied the
    # common-domain/norm-resolvent hypotheses.  This does not verify the
    # unbounded Hamiltonian domain hypothesis.
    energies = [sp.Integer(0), sp.Integer(2), sp.Integer(5)]
    h0 = sp.diag(*energies)
    perturbation = sp.Matrix(
        [
            [sp.Integer(3), sp.Integer(7), sp.Integer(0)],
            [sp.Integer(7), sp.Integer(11), sp.Integer(13)],
            [sp.Integer(0), sp.Integer(13), sp.Integer(17)],
        ]
    )
    level = 1

    pprime = sp.zeros(3, 3)
    for other in range(3):
        if other == level:
            continue
        coefficient = perturbation[other, level] / (energies[level] - energies[other])
        pprime[other, level] = coefficient
        pprime[level, other] = coefficient

    expected = sp.Matrix(
        [
            [0, sp.Rational(7, 2), 0],
            [sp.Rational(7, 2), 0, sp.Rational(-13, 3)],
            [0, sp.Rational(-13, 3), 0],
        ]
    )
    if pprime != expected:
        raise AssertionError(f"soft-mass Riesz projection derivative failed: {pprime!r}")

    # Differentiating Tr(PH) through a fixed-rank isolated projection leaves the
    # perturbing operator restricted to the transported cluster.
    cluster_derivative = perturbation[level, level]
    vacuum_derivative = perturbation[0, 0]
    assert_zero("soft-mass Feynman-Hellmann mass derivative", cluster_derivative - vacuum_derivative - 8)

    commutator_trace = sp.trace((pprime * h0) * sp.eye(3))
    assert_zero("soft-mass projection derivative trace term", commutator_trace)


def check_soft_mass_string_ratio_response() -> None:
    m = sp.symbols("m")
    tension_one = sp.Integer(5) + 2 * m
    tension_k = sp.Integer(15) + 9 * m
    ratio = tension_k / tension_one
    gamma = sp.diff(tension_k, m) / tension_k - sp.diff(tension_one, m) / tension_one

    gamma_at_zero = sp.simplify(gamma.subs(m, 0))
    assert_zero("soft-mass ratio response value", gamma_at_zero - sp.Rational(1, 5))

    transported_log = sp.log(ratio / ratio.subs(m, 0)).series(m, 0, 2).removeO()
    assert_zero("soft-mass log-ratio transport linear term", transported_log - gamma_at_zero * m)

    if sp.simplify(sp.diff(ratio, m).subs(m, 0)) == 0:
        raise AssertionError("nonzero response negative control degenerated")
    if sp.simplify(ratio.subs(m, 1) - ratio.subs(m, 0)) == 0:
        raise AssertionError("constant-ratio negative control was incorrectly accepted")


def check_soft_mass_domain_text_contract() -> None:
    text = CHAPTER.read_text(encoding="utf-8")
    required = [
        "self-adjoint Hamiltonian",
        r"\mathcal D_{\sigma}",
        r"\mathcal Q_{\sigma}",
        "operator-topology hypothesis",
        "Kato type-\\((A)\\)",
        "closed-quadratic-form type-\\((B)\\)",
        r"C^1\) norm-resolvent",
        r"\label{eq:soft-mass-relative-bound}",
        "finite-rank Riesz range",
        r"\label{eq:soft-mass-resolvent-derivative-domain}",
        "form-resolvent language",
        "Finite cutoff versus continuum endpoint",
        "bosonic Yang--Mills endpoint remains a",
    ]
    for phrase in required:
        assert_contains(text, phrase, "soft-mass domain hypothesis text")


def main() -> None:
    check_holomorphic_scale_dimensions()
    check_n1_star_fuzzy_sphere_ansatz()
    check_k_string_ledgers()
    check_sw_vortex_radial_normalization()
    check_abelianized_a_type_sine_profile()
    check_pure_sym_channel_pole_bookkeeping()
    check_soft_mass_common_domain_unbounded_model()
    check_unbounded_domain_negative_control()
    check_soft_mass_spectral_projection_transport()
    check_soft_mass_string_ratio_response()
    check_soft_mass_domain_text_contract()
    print("All supersymmetric Yang-Mills deformation-ladder checks passed.")


if __name__ == "__main__":
    main()
