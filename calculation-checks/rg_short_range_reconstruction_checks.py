#!/usr/bin/env python3
"""Exact finite checks for ordinary short-range scalar RG reconstruction.

Volume XI, Chapter 7 defines the block-spin reconstruction datum for an
ordinary short-range scalar lattice model.  These checks verify the finite
normalization and exponent bookkeeping used there: block kernels preserve
constant fields up to the declared field scaling, block-constant test
functions keep the distribution pairing invariant, adjoint source blocking
has the forced L^D pullback factor and the stated smooth-test sampling
error, independent-site covariances scale with the expected block exponent,
the reconstruction bound has the displayed geometric form, and an auxiliary
RG theorem transfers to
the short-range target only when the one-step intertwining defects remain
controlled after stable or relevant RG amplification.  The observable-germ
checks verify that finite-window agreement is a projective, seminorm-level
estimate rather than a substitute for full universality, and that
QFT-strength observable germs must include reflection-positivity Gram
windows rather than only a visible finite list of correlator coordinates.
The polymer checks verify the exact finite arithmetic behind the one-step
contraction budget: linear irrelevant gain, a finite pair-overlap majorant
for the quadratic circle product, and a finite local-coordinate extraction
defect.
The multiscale polymer checks verify the forced-recursion sum that turns the
one-step budget into a scale-uniform smallness condition.
The finite-range covariance check verifies the block-diagonal characteristic
function factorization behind independent fluctuation integrations on
separated polymers.
The localization checks verify the finite Taylor-remainder arithmetic and
canonical local-monomial scaling exponents used to decide whether an omitted
coordinate has an actual irrelevant gain.
The large-field regulator check verifies the exact determinant and exponent
bookkeeping for finite Gaussian stability of a quadratic regulator under
fluctuation integration.
The source-window check verifies the finite Taylor-source extraction rule
used to decide which connected correlator windows are actually controlled by
a source-extended polymer RG chart.
The finite source-window-to-cumulant check verifies the Cauchy estimate and
restriction compatibility that turn holomorphic finite source windows into
actual cumulant distribution windows.
The source-chart-to-window check verifies the Lipschitz estimate that turns
source-extended RG-coordinate convergence, including the normalizing
coordinate and finite-step remainder, into holomorphic source-window
convergence on one fixed polydisc.
The source-stable trajectory check verifies the finite-depth arithmetic that
combines source-stable contraction, source-local relevant-coordinate
amplification, polymer-tail control, and normalizing/remainder errors before
Cauchy extraction of a source window is allowed.
The finite-volume source-window check verifies the cluster-tail-to-cumulant
Cauchy bound needed before finite-volume source windows can be used as
thermodynamic Schwinger data.
The stable-chart observable-window bound check verifies the finite RG estimate
bound that decomposes a universality comparison into relevant mismatch,
stable-coordinate contraction, accumulated one-step defects, and source-tail
or normalization errors.
The auxiliary projective-window transfer check verifies the finite
observable-germ estimate that combines auxiliary-window convergence,
auxiliary-to-target observable defects, short-range orbit-transfer defects,
and normalization mismatch.
The C1 stable-graph check verifies the differentiated Lyapunov--Perron
equation for a finite one-dimensional nonlinear RG map whose stable graph can
be summed exactly.
The quantitative tuning check verifies the finite-dimensional contraction
constants that turn a transverse microscopic parameter chart into an actual
solution of the relevant-coordinate tuning equation inside a declared ball.
The projective distribution-window check verifies the finite arithmetic
behind compatibility of restriction maps and a uniform seminorm bound,
the two inputs that let finite test-function windows extend to a tempered
distribution.
The cofinal finite-window assembly check verifies the diagonal schedule and
uniform seminorm arithmetic needed when the limiting distribution is obtained
from regulated finite-window functionals, rather than supplied in advance.
The finite OS-positivity bound checks verify both the Gram-window error
bound used when projective observable-germ convergence is strong enough to
feed Osterwalder--Schrader reconstruction and the family-size obstruction:
fixed entrywise tolerance cannot prove positivity on a directed family of
windows unless it scales with the window size or is replaced by an operator
norm estimate.
The reflection-positive block-spin pullback check verifies the finite matrix
compression mechanism by which a reflection-compatible block-spin map sends a
fine reflection-positive Gram form to a coarse one.
The positive-time translation check verifies the finite Gram-window
equicontinuity bound that turns translated positive-time test vectors into a
strongly continuous OS time semigroup after taking the continuum limit.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def pow_int(base, exponent):
    if exponent >= 0:
        return base**exponent
    return Fraction(1, base ** (-exponent))


def product(values):
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def uniform_block_kernel(dimension, scale):
    volume = scale**dimension
    return [Fraction(1, volume) for _ in range(volume)]


def check_block_kernel_constant_field_scaling():
    dimension = 4
    scale = 2
    delta_phi = 1
    constant = Fraction(7, 3)
    q = uniform_block_kernel(dimension, scale)
    assert_equal("block-kernel normalization", sum(q), Fraction(1))
    blocked = pow_int(scale, delta_phi) * sum(weight * constant for weight in q)
    assert_equal(
        "constant field block scaling",
        blocked,
        pow_int(scale, delta_phi) * constant,
    )


def check_distribution_pairing_for_block_constant_tests():
    # Fine lattice spacing is set to a_k=1 for exact arithmetic.  One coarse
    # block then has spacing a_{k-1}=L.  For a test function constant on the
    # block, a^{D-Delta} sum f phi is preserved by the block-spin definition.
    dimension = 4
    scale = 2
    delta_phi = 1
    fine_spacing = Fraction(1)
    coarse_spacing = Fraction(scale)
    field_values = [Fraction(i + 1) for i in range(scale**dimension)]
    test_value = Fraction(5, 7)
    q = uniform_block_kernel(dimension, scale)

    fine_pairing = (
        fine_spacing ** (dimension - delta_phi)
        * test_value
        * sum(field_values)
    )
    blocked_field = pow_int(scale, delta_phi) * sum(
        weight * value for weight, value in zip(q, field_values)
    )
    coarse_pairing = (
        coarse_spacing ** (dimension - delta_phi)
        * test_value
        * blocked_field
    )
    assert_equal("block-constant distribution pairing", coarse_pairing, fine_pairing)


def check_adjoint_source_blocking_identity_and_smooth_error():
    dimension = 2
    scale = 2
    delta_phi = 1
    fine_spacing = Fraction(3, 11)
    coarse_spacing = scale * fine_spacing
    field_values = [Fraction(5, 7), Fraction(-2, 9), Fraction(11, 13), Fraction(3, 8)]
    source_value = Fraction(7, 5)
    q = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 8)]
    assert_equal("nonuniform block-kernel normalization", sum(q), Fraction(1))

    blocked_field = pow_int(scale, delta_phi) * sum(
        weight * value for weight, value in zip(q, field_values)
    )
    coarse_pairing = (
        coarse_spacing ** (dimension - delta_phi)
        * source_value
        * blocked_field
    )
    pulled_source = [
        pow_int(scale, dimension) * weight * source_value
        for weight in q
    ]
    fine_pairing = (
        fine_spacing ** (dimension - delta_phi)
        * sum(source * value for source, value in zip(pulled_source, field_values))
    )
    assert_equal("adjoint source blocking identity", coarse_pairing, fine_pairing)

    smooth_dimension = 1
    smooth_scale = 3
    smooth_fine_spacing = Fraction(1, 5)
    smooth_coarse_spacing = smooth_scale * smooth_fine_spacing
    beta = Fraction(7, 11)
    coarse_sites = [Fraction(0), smooth_coarse_spacing]
    block_offsets = [0, 1, 2]
    l1_sampling_error = (
        smooth_fine_spacing ** smooth_dimension
        * sum(
            beta * smooth_fine_spacing * r
            for _y in coarse_sites
            for r in block_offsets
        )
    )
    constant_c = Fraction(
        sum(block_offsets),
        smooth_scale ** (smooth_dimension + 1),
    )
    coarse_volume = smooth_coarse_spacing ** smooth_dimension * len(coarse_sites)
    expected_bound = constant_c * beta * smooth_coarse_spacing * coarse_volume
    assert_equal("adjoint source smooth-test error bound", l1_sampling_error, expected_bound)


def check_independent_covariance_scaling():
    dimension = 4
    scale = 2
    delta_phi = 1
    variance = Fraction(11, 5)
    q = uniform_block_kernel(dimension, scale)
    covariance_of_block_average = pow_int(scale, 2 * delta_phi) * sum(
        weight * weight * variance for weight in q
    )
    expected = variance * pow_int(scale, 2 * delta_phi - dimension)
    assert_equal("independent-site block covariance scaling", covariance_of_block_average, expected)
    assert_equal("canonical D=4 free-field covariance factor", expected / variance, Fraction(1, 4))


def check_geometric_reconstruction_bound():
    c_b = Fraction(5, 2)
    c0 = Fraction(3, 7)
    theta = Fraction(1, 3)
    eps0 = Fraction(2, 5)
    sigma = Fraction(1, 4)
    for step in range(6):
        chart_distance = c0 * theta**step
        discretization_error = eps0 * sigma**step
        bound = c_b * chart_distance + discretization_error
        expected = c_b * c0 * theta**step + eps0 * sigma**step
        assert_equal(f"geometric reconstruction bound step {step}", bound, expected)
        if step:
            previous = c_b * c0 * theta ** (step - 1) + eps0 * sigma ** (step - 1)
            assert_true(f"bound decreases at step {step}", bound < previous)


def check_correction_to_scaling_bookkeeping():
    scale = 2
    omega_1 = 1
    omega_2 = 2
    fixed_observable = Fraction(13, 17)
    correction_1 = Fraction(11, 3)
    correction_2 = Fraction(-5, 4)
    amplitude_1 = Fraction(7, 5)
    amplitude_2 = Fraction(-2, 9)

    def power_decay(omega, step):
        return Fraction(1, scale ** (omega * step))

    def observable(step):
        return (
            fixed_observable
            + amplitude_1 * power_decay(omega_1, step) * correction_1
            + amplitude_2 * power_decay(omega_2, step) * correction_2
        )

    for step in range(1, 6):
        leading_scaled_error = scale**step * (observable(step) - fixed_observable)
        expected = amplitude_1 * correction_1 + amplitude_2 * correction_2 * power_decay(1, step)
        assert_equal(f"leading correction extraction step {step}", leading_scaled_error, expected)

    for step in range(1, 5):
        subtracted_now = observable(step) - fixed_observable - amplitude_1 * power_decay(omega_1, step) * correction_1
        subtracted_next = observable(step + 1) - fixed_observable - amplitude_1 * power_decay(omega_1, step + 1) * correction_1
        assert_equal(
            f"subleading correction ratio step {step}",
            subtracted_next,
            power_decay(omega_2, 1) * subtracted_now,
        )

    other_amplitude_1 = Fraction(-3, 8)
    other_amplitude_2 = Fraction(5, 11)

    def other_observable(step):
        return (
            fixed_observable
            + other_amplitude_1 * power_decay(omega_1, step) * correction_1
            + other_amplitude_2 * power_decay(omega_2, step) * correction_2
        )

    for step in range(1, 5):
        difference = observable(step) - other_observable(step)
        leading_difference = (
            (amplitude_1 - other_amplitude_1) * power_decay(omega_1, step) * correction_1
        )
        after_leading_subtraction = difference - leading_difference
        expected_subleading = (
            (amplitude_2 - other_amplitude_2) * power_decay(omega_2, step) * correction_2
        )
        assert_equal(
            f"same limit but regulator-dependent correction amplitudes step {step}",
            after_leading_subtraction,
            expected_subleading,
        )


def check_auxiliary_transfer_telescoping_bound():
    theta = Fraction(2, 3)
    q = Fraction(1, 5)
    c = Fraction(3, 7)

    for steps in range(1, 8):
        defects = [c * q**j for j in range(steps)]
        orbit_error = Fraction(0)
        for defect in defects:
            orbit_error = theta * orbit_error + defect

        telescoping = sum(
            theta ** (steps - 1 - j) * defects[j] for j in range(steps)
        )
        closed_form = c * (theta**steps - q**steps) / (theta - q)

        assert_equal(f"auxiliary transfer recurrence step {steps}", orbit_error, telescoping)
        assert_equal(f"auxiliary transfer geometric sum step {steps}", telescoping, closed_form)

    equal_rate = Fraction(1, 4)
    c_equal = Fraction(5, 6)
    for steps in range(1, 7):
        defects = [c_equal * equal_rate**j for j in range(steps)]
        telescoping = sum(
            equal_rate ** (steps - 1 - j) * defects[j] for j in range(steps)
        )
        assert_equal(
            f"auxiliary transfer equal-rate sum step {steps}",
            telescoping,
            c_equal * steps * equal_rate ** (steps - 1),
        )


def check_auxiliary_projective_window_transfer_estimate():
    amplification_factors = [Fraction(2, 3), Fraction(1, 2), Fraction(3, 5)]
    defect_bounds = [Fraction(1, 10), Fraction(1, 20), Fraction(1, 40)]
    steps = len(defect_bounds)

    orbit_bound = sum(
        defect_bounds[j]
        * product(amplification_factors[ell] for ell in range(j + 1, steps))
        for j in range(steps)
    )
    assert_equal("auxiliary projective-window orbit bound", orbit_bound, Fraction(17, 200))

    # Signed defects can cancel in the actual orbit; the estimate uses the
    # absolute defect bounds and therefore remains valid without relying on
    # cancellation.
    signed_defects = [Fraction(1, 10), Fraction(-1, 20), Fraction(1, 40)]
    orbit_error = Fraction(0)
    for factor, defect in zip(amplification_factors, signed_defects):
        orbit_error = factor * orbit_error + defect
    assert_equal("auxiliary projective-window actual orbit error", orbit_error, Fraction(1, 40))
    assert_true("actual orbit error below absolute-defect bound", abs(orbit_error) <= orbit_bound)

    window_lipschitz = Fraction(4)
    auxiliary_window_error = Fraction(1, 100)
    observable_comparison_defect = Fraction(1, 80)
    normalization_mismatch = Fraction(1, 200)

    projective_window_bound = (
        normalization_mismatch
        + auxiliary_window_error
        + observable_comparison_defect
        + window_lipschitz * orbit_bound
    )
    assert_equal("auxiliary projective-window transfer bound", projective_window_bound, Fraction(147, 400))

    actual_window_error = (
        normalization_mismatch
        + auxiliary_window_error
        + observable_comparison_defect
        + window_lipschitz * abs(orbit_error)
    )
    assert_equal("auxiliary projective-window actual finite error", actual_window_error, Fraction(51, 400))
    assert_true(
        "auxiliary projective-window estimate bounds finite error",
        actual_window_error <= projective_window_bound,
    )

    # If the one-step target defects do not decay after amplification, the
    # projective transfer estimate cannot prove convergence of the target
    # observable germ.
    constant_defect = Fraction(1, 30)
    theta = Fraction(2, 3)
    nondecaying_bound = sum(theta ** (steps - 1 - j) * constant_defect for j in range(steps))
    assert_equal("auxiliary projective-window nondecaying defect floor", nondecaying_bound, Fraction(19, 270))
    assert_true("nondecaying defect floor remains positive", nondecaying_bound > 0)


def check_relevant_direction_tuning_amplification():
    lam = Fraction(3)
    rho = Fraction(5, 7)
    for depth in range(1, 6):
        tuned_initial = rho / lam**depth
        amplified = lam**depth * tuned_initial
        assert_equal(f"relevant tuning depth {depth}", amplified, rho)

    initial = Fraction(1, 11)
    errors = [Fraction(1, 3), Fraction(-1, 9), Fraction(1, 27), Fraction(-1, 81)]
    coordinate = initial
    for error in errors:
        coordinate = lam * coordinate + error
    expected = lam ** len(errors) * initial + sum(
        lam ** (len(errors) - 1 - j) * errors[j] for j in range(len(errors))
    )
    assert_equal("relevant direction affine amplification", coordinate, expected)


def check_quantitative_microscopic_tuning_contraction():
    # Exact one-dimensional model for the quantitative tuning estimate.
    # F(x)=2x-1/5+x^2/3, A=F'(0)=2, rho=1/5.  The Newton map with frozen
    # inverse A^{-1} is T(x)=x-A^{-1}F(x)=1/10-x^2/6.
    rho = Fraction(1, 5)
    residual = Fraction(1, 5)
    inverse_norm = Fraction(1, 2)
    derivative_variation_constant = Fraction(2, 3) * rho
    kappa = inverse_norm * derivative_variation_constant
    assert_equal("quantitative tuning normalized residual", inverse_norm * residual, rho / 2)
    assert_equal("quantitative tuning contraction constant", kappa, Fraction(1, 15))
    assert_true("quantitative tuning contraction below half", kappa < Fraction(1, 2))

    map_radius_bound = inverse_norm * residual + kappa * rho
    assert_equal("quantitative tuning ball map bound", map_radius_bound, Fraction(17, 150))
    assert_true("quantitative tuning maps ball into itself", map_radius_bound <= rho)

    # Directly check the contraction estimate for two rational points in the
    # declared ball.
    x = Fraction(1, 7)
    y = Fraction(-1, 9)
    tx = Fraction(1, 10) - x * x / 6
    ty = Fraction(1, 10) - y * y / 6
    lipschitz_bound = kappa * abs(x - y)
    assert_true("quantitative tuning sample contraction", abs(tx - ty) <= lipschitz_bound)

    # A larger residual violates the displayed sufficient condition and the
    # frozen Newton map no longer maps the declared ball into itself at the
    # base point.
    bad_residual = Fraction(3, 5)
    assert_true("large residual violates tuning smallness", inverse_norm * bad_residual > rho / 2)
    bad_t0 = inverse_norm * bad_residual
    assert_true("large residual leaves declared tuning ball", bad_t0 > rho)


def check_c1_stable_graph_derivative_equation():
    # One-dimensional nonlinear RG map:
    #   u_{n+1} = A u_n + c s_n^2,   s_{n+1} = B s_n.
    # The Lyapunov--Perron stable graph is
    #   h(s) = -sum_{j>=0} A^{-(j+1)} c (B^j s)^2
    #        = -c s^2/(A-B^2).
    # Differentiating the Lyapunov--Perron equation gives
    #   Dh(s)v = -sum_{j>=0} A^{-(j+1)} 2c (B^j s)(B^j v),
    # which must equal -2c s v/(A-B^2).
    unstable_eigenvalue = Fraction(2)
    stable_eigenvalue = Fraction(1, 3)
    nonlinear_coefficient = Fraction(5)
    stable_coordinate = Fraction(1, 7)
    stable_tangent = Fraction(3, 11)
    denominator = unstable_eigenvalue - stable_eigenvalue**2

    graph_value = -nonlinear_coefficient * stable_coordinate**2 / denominator
    graph_derivative = (
        -2
        * nonlinear_coefficient
        * stable_coordinate
        * stable_tangent
        / denominator
    )
    assert_equal("C1 stable graph closed form", graph_value, Fraction(-45, 833))
    assert_equal("C1 stable graph derivative closed form", graph_derivative, Fraction(-270, 1309))

    lp_derivative_sum = (
        -2
        * nonlinear_coefficient
        * stable_coordinate
        * stable_tangent
        / unstable_eigenvalue
        / (1 - stable_eigenvalue**2 / unstable_eigenvalue)
    )
    assert_equal(
        "C1 differentiated Lyapunov-Perron sum",
        lp_derivative_sum,
        graph_derivative,
    )

    zero_graph_derivative = (
        -2
        * nonlinear_coefficient
        * Fraction(0)
        * stable_tangent
        / denominator
    )
    assert_equal("C1 stable graph tangent to stable subspace", zero_graph_derivative, Fraction(0))


def check_observable_germ_finite_window_estimate():
    # Three finite observation windows form a projective chain
    # gamma -> beta -> alpha.  The exact numbers model normalized finite lists
    # of observables; the check is the projective compatibility and the
    # finite-window triangle estimate used in the chapter.
    gamma_data = {
        "alpha": Fraction(5, 7),
        "beta_extra": Fraction(-2, 3),
        "gamma_extra": Fraction(11, 13),
    }
    beta_projection = {
        "alpha": gamma_data["alpha"],
        "beta_extra": gamma_data["beta_extra"],
    }
    alpha_projection = {"alpha": gamma_data["alpha"]}

    assert_equal("project gamma to beta", beta_projection["alpha"], gamma_data["alpha"])
    assert_equal("project beta to alpha", alpha_projection["alpha"], beta_projection["alpha"])
    assert_equal("direct gamma to alpha", alpha_projection["alpha"], gamma_data["alpha"])

    fixed_alpha = Fraction(17, 19)
    fixed_beta = Fraction(-4, 9)
    fixed_gamma = Fraction(7, 11)
    error_i = {
        "alpha": Fraction(1, 100),
        "beta": Fraction(1, 80),
        "gamma": Fraction(1, 70),
    }
    error_j = {
        "alpha": Fraction(1, 90),
        "beta": Fraction(1, 75),
        "gamma": Fraction(1, 60),
    }
    rec_i = {
        "alpha": fixed_alpha + error_i["alpha"],
        "beta": fixed_beta - error_i["beta"],
        "gamma": fixed_gamma + error_i["gamma"],
    }
    rec_j = {
        "alpha": fixed_alpha - error_j["alpha"],
        "beta": fixed_beta + error_j["beta"],
        "gamma": fixed_gamma - error_j["gamma"],
    }

    for key in ("alpha", "beta", "gamma"):
        lhs = abs(rec_i[key] - rec_j[key])
        rhs = error_i[key] + error_j[key]
        assert_equal(f"finite-window universality estimate {key}", lhs, rhs)

    hidden_window_error = Fraction(1, 7)
    declared_finite_bound = error_i["alpha"] + error_j["alpha"]
    assert_true(
        "uncontrolled window remains outside finite estimate",
        hidden_window_error > declared_finite_bound,
    )


def check_projective_distribution_window_extension():
    # A projective family of distribution windows must be compatible under
    # restriction, and the finite values must obey a single seminorm bound.
    # This finite vector-space model is the exact arithmetic counterpart of the
    # Schwartz-window extension lemma in the chapter.
    window_e1 = [Fraction(2), Fraction(-1)]
    window_e2 = window_e1 + [Fraction(3, 5)]
    window_e3 = window_e2 + [Fraction(7, 4)]

    assert_equal("project E3 to E2", window_e3[:3], window_e2)
    assert_equal("project E2 to E1", window_e2[:2], window_e1)
    assert_equal("direct project E3 to E1", window_e3[:2], window_e1)

    test_coefficients = [
        Fraction(1, 3),
        Fraction(-2),
        Fraction(5, 7),
        Fraction(-4, 9),
    ]
    induced_value = sum(
        coefficient * value
        for coefficient, value in zip(test_coefficients, window_e3)
    )
    assert_equal("projective extension value", induced_value, Fraction(146, 63))

    model_qr = sum(abs(coefficient) for coefficient in test_coefficients)
    seminorm_constant = max(abs(value) for value in window_e3)
    assert_equal("finite model Schwartz seminorm", model_qr, Fraction(220, 63))
    assert_equal("finite distribution seminorm constant", seminorm_constant, Fraction(2))
    assert_true(
        "finite distribution seminorm bound",
        abs(induced_value) <= seminorm_constant * model_qr,
    )

    bad_window_e3 = window_e2[:2] + [Fraction(4, 5), window_e3[3]]
    restriction_defect = bad_window_e3[2] - window_e2[2]
    assert_equal(
        "incompatible projective restriction defect",
        restriction_defect,
        Fraction(1, 5),
    )

    declared_uniform_constant = Fraction(5)
    large_tail_values = [Fraction(1), Fraction(-2), Fraction(3), Fraction(8)]
    assert_true(
        "declared uniform seminorm bound detects large tail",
        abs(large_tail_values[-1]) > declared_uniform_constant,
    )


def check_cofinal_finite_window_assembly():
    # Model nested finite windows E_N = span(e_1,...,e_N) with
    # q(f)=sum_i |f_i|.  Regulated scale k controls windows N <= N_k.
    # The coefficient of e_i is a_i + 1/(k+i+1), so every fixed window is
    # Cauchy and the limit coefficient is a_i.
    def coefficient(index: int, scale: int) -> Fraction:
        return Fraction(1, index + 1) + Fraction(1, scale + index + 1)

    def limiting_coefficient(index: int) -> Fraction:
        return Fraction(1, index + 1)

    def window_value(
        window_size: int,
        scale: int,
        vector: tuple[Fraction, ...],
    ) -> Fraction:
        if len(vector) != window_size:
            raise AssertionError("window vector has the wrong dimension")
        return sum(
            coefficient(i + 1, scale) * vector[i]
            for i in range(window_size)
        )

    scale = 8
    large_window_vector = (Fraction(2), Fraction(-1), Fraction(3))
    restricted_vector = large_window_vector[:2]
    assert_equal(
        "cofinal window restriction compatibility",
        window_value(3, scale, restricted_vector + (Fraction(0),)),
        window_value(2, scale, restricted_vector),
    )

    # The l1-dual norm of a finite window is the maximum absolute coefficient.
    for scale in (4, 8, 16):
        dual_norm = max(coefficient(i, scale) for i in range(1, 6))
        assert_true("cofinal assembly uniform seminorm bound", dual_norm <= 1)

    # A diagonal choice k_j=2^j controls all windows N <= j with error at most
    # 2^{-j} in the l1-dual norm.
    for stage in (3, 4, 5):
        diagonal_scale = 2**stage
        for window_size in range(1, stage + 1):
            error = max(
                abs(coefficient(i, diagonal_scale) - limiting_coefficient(i))
                for i in range(1, window_size + 1)
            )
            assert_true(
                "cofinal diagonal window error",
                error <= Fraction(1, 2**stage),
            )

    # The limiting window is compatible and bounded by the same seminorm.
    limiting_vector = (Fraction(2), Fraction(-1), Fraction(3), Fraction(4))
    limiting_value = sum(
        limiting_coefficient(i + 1) * limiting_vector[i]
        for i in range(4)
    )
    q_norm = sum(abs(component) for component in limiting_vector)
    assert_equal("cofinal limiting window value", limiting_value, Fraction(133, 60))
    assert_true(
        "cofinal limiting functional bounded by q",
        abs(limiting_value) <= q_norm,
    )

    # If the number of controlled windows is bounded, the dense-union
    # requirement fails: e_3 is never seen when N_k <= 2.
    bounded_window_counts = [2, 2, 2, 2]
    assert_true("noncofinal window schedule detected", max(bounded_window_counts) < 3)


def check_qft_strength_observable_germ_windows():
    # A visible one-coordinate window can agree while an undeclared
    # reflection-positivity Gram window fails.  This finite check models the
    # chapter's point that equality of a local QFT requires the whole
    # OS/Wightman reconstruction germ, not only a finite observable list.
    visible_two_point = Fraction(2)
    positive_gram = [
        [visible_two_point, Fraction(1)],
        [Fraction(1), Fraction(3)],
    ]
    positive_det = (
        positive_gram[0][0] * positive_gram[1][1]
        - positive_gram[0][1] ** 2
    )
    assert_equal(
        "project Gram to visible two-point",
        positive_gram[0][0],
        visible_two_point,
    )
    assert_true("declared OS Gram determinant positive", positive_det > 0)

    hidden_bad_gram = [
        [visible_two_point, Fraction(3)],
        [Fraction(3), Fraction(1)],
    ]
    hidden_bad_det = (
        hidden_bad_gram[0][0] * hidden_bad_gram[1][1]
        - hidden_bad_gram[0][1] ** 2
    )
    assert_equal(
        "hidden bad Gram has same visible coordinate",
        hidden_bad_gram[0][0],
        visible_two_point,
    )
    assert_true("hidden bad OS Gram determinant negative", hidden_bad_det < 0)

    error_i = Fraction(1, 100)
    error_j = Fraction(1, 120)
    rec_i_visible = visible_two_point + error_i
    rec_j_visible = visible_two_point - error_j
    finite_visible_bound = abs(rec_i_visible - rec_j_visible)
    assert_equal(
        "visible finite-window bound",
        finite_visible_bound,
        error_i + error_j,
    )
    assert_true(
        "visible bound does not detect hidden positivity failure",
        hidden_bad_det < 0 and finite_visible_bound < 1,
    )


def check_reflection_positive_block_spin_pullback():
    # Fine positive-time polynomial basis: 1, phi_1, phi_2.
    # A reflection-compatible coarse field Phi=a phi_1+b phi_2 gives the
    # coarse positive-time basis 1, Phi by pullback.  Hence the coarse Gram
    # matrix is B^T G_fine B and remains positive whenever G_fine is positive.
    fine_gram = [
        [Fraction(2), Fraction(1, 3), Fraction(-1, 4)],
        [Fraction(1, 3), Fraction(3), Fraction(1, 2)],
        [Fraction(-1, 4), Fraction(1, 2), Fraction(5)],
    ]
    block_weights = [Fraction(2, 5), Fraction(3, 5)]
    pullback_matrix = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), block_weights[0]],
        [Fraction(0), block_weights[1]],
    ]

    def matmul(left, right):
        rows = len(left)
        cols = len(right[0])
        mid = len(right)
        return [
            [
                sum(left[i][k] * right[k][j] for k in range(mid))
                for j in range(cols)
            ]
            for i in range(rows)
        ]

    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]

    coarse_gram = matmul(transpose(pullback_matrix), matmul(fine_gram, pullback_matrix))
    expected = [
        [Fraction(2), Fraction(-1, 60)],
        [Fraction(-1, 60), Fraction(63, 25)],
    ]
    assert_equal("reflection-positive block-spin compressed Gram", coarse_gram, expected)

    fine_principal_one = [fine_gram[i][i] for i in range(3)]
    assert_true("fine Gram diagonal positive", all(value > 0 for value in fine_principal_one))
    fine_minor_12 = fine_gram[0][0] * fine_gram[1][1] - fine_gram[0][1] ** 2
    fine_minor_13 = fine_gram[0][0] * fine_gram[2][2] - fine_gram[0][2] ** 2
    fine_minor_23 = fine_gram[1][1] * fine_gram[2][2] - fine_gram[1][2] ** 2
    fine_det = (
        fine_gram[0][0]
        * (fine_gram[1][1] * fine_gram[2][2] - fine_gram[1][2] * fine_gram[2][1])
        - fine_gram[0][1]
        * (fine_gram[1][0] * fine_gram[2][2] - fine_gram[1][2] * fine_gram[2][0])
        + fine_gram[0][2]
        * (fine_gram[1][0] * fine_gram[2][1] - fine_gram[1][1] * fine_gram[2][0])
    )
    assert_true("fine Gram two-by-two minors positive", fine_minor_12 > 0 and fine_minor_13 > 0 and fine_minor_23 > 0)
    assert_true("fine Gram determinant positive", fine_det > 0)

    coarse_det = coarse_gram[0][0] * coarse_gram[1][1] - coarse_gram[0][1] ** 2
    assert_equal("reflection-positive block-spin coarse determinant", coarse_det, Fraction(18143, 3600))
    assert_true("coarse Gram determinant positive", coarse_det > 0)

    # The compression statement is the finite matrix version of pulling a
    # coarse positive-time polynomial back to the fine positive-time algebra.
    coarse_coefficients = [Fraction(7, 11), Fraction(-5, 13)]
    pulled_fine_coefficients = [
        sum(pullback_matrix[i][j] * coarse_coefficients[j] for j in range(2))
        for i in range(3)
    ]

    def quadratic_form(matrix, vector):
        return sum(
            vector[i] * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        )

    coarse_value = quadratic_form(coarse_gram, coarse_coefficients)
    pulled_value = quadratic_form(fine_gram, pulled_fine_coefficients)
    assert_equal("reflection-positive pullback quadratic form", coarse_value, pulled_value)
    assert_true("reflection-positive pullback value nonnegative", coarse_value >= 0)


def check_finite_os_positivity_bound():
    # Finite OS positivity is a Gram-matrix condition.  If a regulated Gram
    # matrix G_k has lower bound ell and the limiting Gram matrix differs
    # entrywise by at most epsilon, then
    #   c^* G_* c >= (ell - m epsilon) ||c||_2^2
    # for an m-by-m window.  This check verifies the exact finite arithmetic.
    dimension = 3
    ell = Fraction(1)
    epsilon = Fraction(1, 10)
    regulated_gram = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(3, 2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(2)],
    ]
    limiting_gram = [
        [regulated_gram[i][j] - epsilon for j in range(dimension)]
        for i in range(dimension)
    ]

    lower_bound = ell - dimension * epsilon
    assert_equal("finite OS lower bound", lower_bound, Fraction(7, 10))

    vector = [Fraction(2), Fraction(-1), Fraction(3)]

    def quadratic_form(matrix, vec):
        total = Fraction(0)
        for i, row in enumerate(matrix):
            for j, entry in enumerate(row):
                total += vec[i] * entry * vec[j]
        return total

    norm_squared = sum(component * component for component in vector)
    regulated_value = quadratic_form(regulated_gram, vector)
    limiting_value = quadratic_form(limiting_gram, vector)
    l1_square = sum(abs(component) for component in vector) ** 2
    entrywise_error_bound = epsilon * l1_square

    assert_equal("finite OS regulated quadratic form", regulated_value, Fraction(47, 2))
    assert_equal("finite OS limiting quadratic form", limiting_value, Fraction(219, 10))
    assert_equal("finite OS entrywise error bound", entrywise_error_bound, Fraction(18, 5))
    assert_true(
        "finite OS quadratic-form difference below entrywise bound",
        abs(limiting_value - regulated_value) <= entrywise_error_bound,
    )
    assert_true(
        "finite OS bound gives positive lower bound",
        limiting_value >= lower_bound * norm_squared,
    )

    # The same concrete limiting matrix is positive by principal minors.  This
    # is not the proof used in the chapter, but it protects the example from
    # accidentally choosing an indefinite window.
    principal_one = [limiting_gram[i][i] for i in range(dimension)]
    assert_true("finite OS one-by-one principal minors positive", all(value > 0 for value in principal_one))
    for i in range(dimension):
        for j in range(i + 1, dimension):
            minor = (
                limiting_gram[i][i] * limiting_gram[j][j]
                - limiting_gram[i][j] * limiting_gram[j][i]
            )
            assert_true(f"finite OS two-by-two principal minor {i}{j} positive", minor > 0)
    determinant = (
        limiting_gram[0][0]
        * (limiting_gram[1][1] * limiting_gram[2][2] - limiting_gram[1][2] * limiting_gram[2][1])
        - limiting_gram[0][1]
        * (limiting_gram[1][0] * limiting_gram[2][2] - limiting_gram[1][2] * limiting_gram[2][0])
        + limiting_gram[0][2]
        * (limiting_gram[1][0] * limiting_gram[2][1] - limiting_gram[1][1] * limiting_gram[2][0])
    )
    assert_equal("finite OS limiting Gram determinant", determinant, Fraction(47, 20))
    assert_true("finite OS limiting Gram determinant positive", determinant > 0)


def check_finite_os_positivity_family_size_obstruction():
    # The entrywise estimate in the chapter is sharp for an all-ones
    # perturbation.  With G_k = ell I_m and G_* = ell I_m - epsilon J_m, the
    # vector (1,...,1) has quadratic form m (ell - m epsilon).  Thus a fixed
    # entrywise tolerance cannot be promoted to a directed OS positivity theorem
    # as the finite positive-time test family grows.
    ell = Fraction(1, 2)
    epsilon = Fraction(1, 10)

    def all_ones_direction_value(dimension):
        norm_squared = Fraction(dimension)
        value = dimension * ell - dimension * dimension * epsilon
        entrywise_lower = (ell - dimension * epsilon) * norm_squared
        assert_equal(
            f"all-ones perturbation saturates m epsilon loss m={dimension}",
            value,
            entrywise_lower,
        )
        return value

    assert_true("entrywise OS bound positive for m=4", all_ones_direction_value(4) > 0)
    assert_equal("entrywise OS bound exactly zero for m=5", all_ones_direction_value(5), Fraction(0))
    assert_true("entrywise OS bound fails for m=6", all_ones_direction_value(6) < 0)

    # An operator-norm estimate has a different scaling.  A diagonal error of
    # size epsilon has ||G_* - G_k||_{2->2}=epsilon, so the lower bound is
    # ell-epsilon, independently of the number of vectors in the window.
    dimension = 6
    norm_squared = Fraction(dimension)
    operator_norm_lower = (ell - epsilon) * norm_squared
    diagonal_error_value = dimension * (ell - epsilon)
    assert_equal("operator-norm OS lower bound", operator_norm_lower, Fraction(12, 5))
    assert_equal("diagonal perturbation realizes operator bound", diagonal_error_value, operator_norm_lower)
    assert_true("operator-norm OS lower bound positive", operator_norm_lower > 0)


def check_positive_time_translation_window_bound():
    # The chapter's OS semigroup-continuity input is a bound on the
    # positive-time Gram norm of tau_t F - F.  This finite check keeps the
    # support margin, modulus of continuity, limiting Gram-window bound, and
    # dense-domain extension arithmetic separate.
    support_margin = Fraction(3, 2)
    time_s = Fraction(1, 4)
    time_t = Fraction(1, 3)
    assert_true("positive-time translation support margin", time_s + time_t < support_margin / 2)
    assert_equal("translation semigroup parameter addition", time_s + time_t, Fraction(7, 12))

    modulus_constant = Fraction(3)
    small_time = Fraction(1, 5)
    half_time = small_time / 2
    omega_small = modulus_constant * small_time**2
    omega_half = modulus_constant * half_time**2
    assert_equal("translation modulus at t", omega_small, Fraction(3, 25))
    assert_equal("translation modulus at t/2", omega_half, Fraction(3, 100))
    assert_equal("quadratic translation modulus scaling", 4 * omega_half, omega_small)

    regulator_errors = [Fraction(1, 10), Fraction(1, 20), Fraction(1, 40)]
    finite_bounds = [omega_small + error for error in regulator_errors]
    assert_equal("first regulated translation Gram bound", finite_bounds[0], Fraction(11, 50))
    assert_true("regulated translation bounds decrease", finite_bounds[2] < finite_bounds[1] < finite_bounds[0])
    assert_true("limiting translation bound below finite bounds", all(omega_small < bound for bound in finite_bounds))

    # If a dense positive-time vector v is approximated by u with OS norm
    # alpha, and the translated dense vector obeys beta, a contraction
    # semigroup gives ||T_t v - v|| <= beta + 2 alpha.  This is the finite
    # extension estimate behind passing continuity from a dense domain to the
    # OS Hilbert-space closure.
    dense_approximation_error = Fraction(1, 20)
    dense_vector_translation_bound = omega_half
    closure_bound = dense_vector_translation_bound + 2 * dense_approximation_error
    assert_equal("positive-time dense-domain extension bound", closure_bound, Fraction(13, 100))
    assert_true("dense-domain extension keeps continuity small", closure_bound < Fraction(1, 5))


def check_stable_chart_observable_window_bound():
    theta = Fraction(1, 2)
    initial_stable_mismatch = Fraction(1, 5)
    one_step_defects = [
        Fraction(1, 100),
        Fraction(1, 200),
        Fraction(1, 400),
        Fraction(1, 800),
    ]
    stable_mismatch = initial_stable_mismatch
    for defect in one_step_defects:
        stable_mismatch = theta * stable_mismatch + defect

    steps = len(one_step_defects)
    propagated_stable_bound = (
        theta**steps * initial_stable_mismatch
        + sum(
            theta ** (steps - 1 - index) * defect
            for index, defect in enumerate(one_step_defects)
        )
    )
    assert_equal(
        "stable-chart propagated mismatch",
        stable_mismatch,
        Fraction(7, 400),
    )
    assert_equal(
        "stable-chart stable recurrence bound",
        stable_mismatch,
        propagated_stable_bound,
    )

    relevant_lipschitz = Fraction(2)
    stable_lipschitz = Fraction(3)
    relevant_mismatch = Fraction(1, 100)
    source_tail_error = Fraction(1, 400)
    normalization_error = Fraction(1, 800)
    total_declared_tail = source_tail_error + normalization_error

    window_bound = (
        relevant_lipschitz * relevant_mismatch
        + stable_lipschitz * propagated_stable_bound
        + total_declared_tail
    )
    assert_equal("stable-chart observable-window bound", window_bound, Fraction(61, 800))

    actual_window_difference = (
        relevant_lipschitz * relevant_mismatch
        + stable_lipschitz * stable_mismatch
        + source_tail_error
    )
    assert_equal(
        "stable-chart actual finite-window difference",
        actual_window_difference,
        Fraction(60, 800),
    )
    assert_true(
        "stable-chart bound controls finite-window difference",
        actual_window_difference <= window_bound,
    )

    exactly_tuned_bound = (
        stable_lipschitz * propagated_stable_bound
        + total_declared_tail
    )
    assert_equal("stable-chart exact tuning removes relevant term", exactly_tuned_bound, Fraction(45, 800))
    assert_true("stable-chart tuned bound is sharper", exactly_tuned_bound < window_bound)


def check_polymer_contraction_budget():
    # The chapter's polymer datum gives
    #   x_{k+1} <= q x_k + B x_k^2 + epsilon.
    # This exact rational test is deliberately finite: it verifies the
    # contraction-budget arithmetic, not any model-specific analytic estimate
    # for q, B, epsilon, or the large-field norm.
    linear_gain = Fraction(2, 5)
    quadratic_constant = Fraction(7, 4)
    radius = Fraction(1, 10)
    extraction_defect = Fraction(1, 200)

    theta = (
        linear_gain
        + quadratic_constant * radius
        + extraction_defect / radius
    )
    assert_equal("polymer contraction margin", theta, Fraction(5, 8))
    assert_true("polymer contraction margin below one", theta < 1)

    boundary_next = (
        linear_gain * radius
        + quadratic_constant * radius * radius
        + extraction_defect
    )
    assert_equal("polymer boundary image", boundary_next, theta * radius)
    assert_true("polymer ball maps strictly inside itself", boundary_next < radius)

    x = radius
    for step in range(1, 7):
        x_next = linear_gain * x + quadratic_constant * x * x + extraction_defect
        assert_true(f"polymer recurrence remains inside radius step {step}", x_next <= radius)
        if x >= boundary_next:
            assert_true(f"polymer recurrence decreases before fixed cell step {step}", x_next <= x)
        x = x_next

    # A finite overlap/combinatorial constant controls the quadratic
    # circle-product estimate ||K_1 circ K_2|| <= B_pol ||K_1|| ||K_2||.
    overlap_constant = Fraction(6)
    norm_1 = Fraction(1, 30)
    norm_2 = Fraction(1, 20)
    product_bound = overlap_constant * norm_1 * norm_2
    assert_equal("polymer circle-product quadratic bound", product_bound, Fraction(1, 100))


def check_polymer_pair_overlap_majorant():
    # Finite one-dimensional shadow of the pair-overlap constant
    # C_a^circ.  Polymers are connected intervals in a five-block line.
    # Two intervals are incompatible when they overlap or are adjacent, so
    # their reblocked hull is still controlled by a local counting constant.
    block_count = 5
    omega = Fraction(1, 4)  # exact stand-in for exp(-a)
    intervals = [
        (left, right)
        for left in range(block_count)
        for right in range(left, block_count)
    ]

    def length(interval):
        return interval[1] - interval[0] + 1

    def incompatible(first, second):
        return not (first[1] + 1 < second[0] or second[1] + 1 < first[0])

    def hull(first, second):
        return (min(first[0], second[0]), max(first[1], second[1]))

    block_sums = []
    for block in range(block_count):
        total = Fraction(0)
        for first in intervals:
            for second in intervals:
                if not incompatible(first, second):
                    continue
                joined = hull(first, second)
                if joined[0] <= block <= joined[1]:
                    total += omega ** (length(first) + length(second))
        block_sums.append(total)

    expected = [
        Fraction(421281, 1048576),
        Fraction(763825, 1048576),
        Fraction(866481, 1048576),
        Fraction(763825, 1048576),
        Fraction(421281, 1048576),
    ]
    assert_equal("polymer pair-overlap block sums", block_sums, expected)
    pair_majorant = max(block_sums)
    assert_equal("polymer pair-overlap majorant", pair_majorant, Fraction(866481, 1048576))

    regulator_constant = Fraction(3, 2)
    norm_1 = Fraction(1, 10)
    norm_2 = Fraction(1, 7)
    admissible_b_pol = regulator_constant * pair_majorant
    product_bound = admissible_b_pol * norm_1 * norm_2
    assert_equal(
        "polymer pair-overlap circle-product bound",
        product_bound,
        Fraction(371349, 20971520),
    )


def check_polymer_multiscale_forcing_budget():
    theta = Fraction(2, 5)
    sigma = Fraction(1, 3)
    forcing_size = Fraction(1, 100)
    initial = Fraction(1, 20)

    for steps in range(1, 8):
        x = initial
        for j in range(steps):
            x = theta * x + forcing_size * sigma**j
        expected = theta**steps * initial + forcing_size * sum(
            theta ** (steps - 1 - j) * sigma**j for j in range(steps)
        )
        closed_form = (
            theta**steps * initial
            + forcing_size * (theta**steps - sigma**steps) / (theta - sigma)
        )
        assert_equal(f"polymer multiscale forcing recurrence {steps}", x, expected)
        assert_equal(f"polymer multiscale geometric forcing {steps}", x, closed_form)

    equal_rate = Fraction(1, 4)
    equal_forcing = Fraction(3, 200)
    for steps in range(1, 7):
        forcing_sum = sum(
            equal_rate ** (steps - 1 - j) * equal_forcing * equal_rate**j
            for j in range(steps)
        )
        assert_equal(
            f"polymer equal-rate forcing sum {steps}",
            forcing_sum,
            equal_forcing * steps * equal_rate ** (steps - 1),
        )

    uniform_forcing = Fraction(1, 500)
    radius = Fraction(1, 10)
    invariant_budget = initial + uniform_forcing / (1 - theta)
    assert_true("polymer uniform-forcing invariant budget below radius", invariant_budget <= radius)
    x = initial
    for steps in range(1, 10):
        x = theta * x + uniform_forcing
        bound = theta**steps * initial + uniform_forcing * (1 - theta**steps) / (1 - theta)
        assert_equal(f"polymer uniform-forcing bound {steps}", x, bound)
        assert_true(f"polymer uniform-forcing orbit stays in radius {steps}", x <= radius)


def check_finite_range_gaussian_factorization():
    # Four finite field coordinates are split as A={0,1}, B={2,3}.  The
    # covariance has nontrivial internal correlations in A and B but vanishing
    # cross block.  The Gaussian characteristic exponent therefore splits
    # exactly into its A and B parts.  This is the finite arithmetic model of
    # the chapter's separated-polymer fluctuation factorization.
    gamma = [
        [Fraction(5), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(3), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(7), Fraction(2)],
        [Fraction(0), Fraction(0), Fraction(2), Fraction(4)],
    ]
    vector = [Fraction(1, 2), Fraction(-3, 5), Fraction(2, 7), Fraction(5, 11)]

    def quadratic_form(matrix, vec):
        total = Fraction(0)
        for i, row in enumerate(matrix):
            for j, entry in enumerate(row):
                total += vec[i] * entry * vec[j]
        return total

    full = quadratic_form(gamma, vector)
    a_block = quadratic_form(
        [row[:2] for row in gamma[:2]],
        vector[:2],
    )
    b_block = quadratic_form(
        [row[2:] for row in gamma[2:]],
        vector[2:],
    )
    assert_equal("finite-range characteristic exponent splits", full, a_block + b_block)

    # Turning on one cross covariance records exactly the mixed term that
    # prevents factorization.  The coefficient is 2 t_0 Gamma_{02} t_2 in the
    # symmetric quadratic form.
    gamma_with_tail = [row[:] for row in gamma]
    cross = Fraction(3, 13)
    gamma_with_tail[0][2] = cross
    gamma_with_tail[2][0] = cross
    full_with_tail = quadratic_form(gamma_with_tail, vector)
    mixed_term = 2 * vector[0] * cross * vector[2]
    assert_equal(
        "cross covariance creates mixed characteristic term",
        full_with_tail,
        a_block + b_block + mixed_term,
    )
    assert_true("mixed term is nonzero when covariance tail remains", mixed_term != 0)


def check_localization_taylor_remainder_bound():
    # Scalar finite-dimensional shadow of the Taylor-localization estimate.
    # F(t)=3-2t+5t^2-7t^3+11t^4 is localized through degree two.
    # On |t|<=r, sup |F'''(t)| <= 6*7 + 24*11*r, so the integral Taylor
    # remainder gives |R_2(t)| <= M_3 r^3/6 at |t|=r.
    r = Fraction(1, 5)
    c0 = Fraction(3)
    c1 = Fraction(-2)
    c2 = Fraction(5)
    c3 = Fraction(-7)
    c4 = Fraction(11)

    value = c0 + c1 * r + c2 * r**2 + c3 * r**3 + c4 * r**4
    localized = c0 + c1 * r + c2 * r**2
    remainder = abs(value - localized)
    direct_abs_sum = abs(c3) * r**3 + abs(c4) * r**4
    derivative_bound = 6 * abs(c3) + 24 * abs(c4) * r
    taylor_bound = derivative_bound * r**3 / 6

    assert_equal("Taylor localization direct omitted-coordinate sum", direct_abs_sum, Fraction(46, 625))
    assert_true("Taylor localization exact remainder below direct abs sum", remainder <= direct_abs_sum)
    assert_equal("Taylor localization derivative bound", derivative_bound, Fraction(474, 5))
    assert_equal("Taylor localization integral remainder bound", taylor_bound, Fraction(79, 625))
    assert_true("Taylor localization remainder below derivative bound", remainder <= taylor_bound)


def check_localization_scaling_exponents():
    def exponent(dimension, delta_phi, fields, differences):
        return dimension - fields * delta_phi - differences

    # Canonical D=4 scalar bookkeeping: phi^4 and (partial phi)^2 are
    # marginal, while phi^6 and four-derivative quadratic terms are
    # irrelevant by two powers of the block scale.
    d4 = Fraction(4)
    delta4 = Fraction(1)
    assert_equal("D4 mass exponent", exponent(d4, delta4, 2, 0), Fraction(2))
    assert_equal("D4 quartic exponent", exponent(d4, delta4, 4, 0), Fraction(0))
    assert_equal("D4 kinetic exponent", exponent(d4, delta4, 2, 2), Fraction(0))
    assert_equal("D4 phi6 exponent", exponent(d4, delta4, 6, 0), Fraction(-2))
    assert_equal("D4 four-derivative quadratic exponent", exponent(d4, delta4, 2, 4), Fraction(-2))
    first_omitted_gap_d4 = min(
        -exponent(d4, delta4, 6, 0),
        -exponent(d4, delta4, 2, 4),
    )
    assert_equal("D4 first omitted canonical localization gap", first_omitted_gap_d4, Fraction(2))
    assert_true("D4 omitted canonical coordinates are contractive", first_omitted_gap_d4 > 0)

    # Canonical D=3 scalar bookkeeping: phi^6 is marginal by engineering
    # power counting.  Discarding it into the irrelevant polymer activity
    # therefore requires an interacting fixed-point/scaling-field theorem or
    # a separate localization estimate, not the canonical ledger alone.
    d3 = Fraction(3)
    delta3 = Fraction(1, 2)
    assert_equal("D3 mass exponent", exponent(d3, delta3, 2, 0), Fraction(2))
    assert_equal("D3 quartic exponent", exponent(d3, delta3, 4, 0), Fraction(1))
    assert_equal("D3 phi6 exponent", exponent(d3, delta3, 6, 0), Fraction(0))
    assert_equal("D3 phi8 exponent", exponent(d3, delta3, 8, 0), Fraction(-1))
    first_omitted_gap_d3_if_phi6_omitted = -exponent(d3, delta3, 6, 0)
    assert_equal(
        "D3 no canonical irrelevant gain if phi6 is omitted",
        first_omitted_gap_d3_if_phi6_omitted,
        Fraction(0),
    )
    assert_true("D3 omitted phi6 is not canonically contractive", first_omitted_gap_d3_if_phi6_omitted <= 0)


def check_large_field_gaussian_regulator_bound():
    # Diagonal finite covariance with eigenvalues 1/3 and 1/5, regulator
    # coefficient kappa=1/4, and background field (2,-3).  The exact
    # Gaussian identity in the chapter has determinant factor
    # prod_i (1-2 kappa lambda_i)^(-1/2) and exponent
    # sum_i kappa phi_i^2/(1-2 kappa lambda_i).  The bound replaces each
    # eigenvalue by lambda_max.
    kappa = Fraction(1, 4)
    eigenvalues = [Fraction(1, 3), Fraction(1, 5)]
    phi = [Fraction(2), Fraction(-3)]

    denominators = [1 - 2 * kappa * lam for lam in eigenvalues]
    assert_equal("large-field regulator first denominator", denominators[0], Fraction(5, 6))
    assert_equal("large-field regulator second denominator", denominators[1], Fraction(9, 10))

    prefactor_squared = Fraction(1)
    for denominator in denominators:
        prefactor_squared *= Fraction(1, denominator)
    assert_equal("large-field regulator determinant prefactor squared", prefactor_squared, Fraction(4, 3))

    exact_exponent = sum(
        kappa * component**2 / denominator
        for component, denominator in zip(phi, denominators)
    )
    lambda_max = max(eigenvalues)
    norm_squared = sum(component**2 for component in phi)
    bound_exponent = kappa * norm_squared / (1 - 2 * kappa * lambda_max)
    assert_equal("large-field regulator exact exponent", exact_exponent, Fraction(37, 10))
    assert_equal("large-field regulator bound exponent", bound_exponent, Fraction(39, 10))
    assert_true("large-field regulator spectral bound dominates exact exponent", exact_exponent <= bound_exponent)

    # One-dimensional completing-square bookkeeping for lambda=1/3,
    # kappa=1/4, phi=2.  This verifies the shifted Gaussian coefficient and
    # the constant term before multiplying over coordinates.
    lam = Fraction(1, 3)
    background = Fraction(2)
    alpha = Fraction(1, 2 * lam) - kappa
    shift = kappa * background / alpha
    square_completion_constant = kappa * background**2 + (kappa * background) ** 2 / alpha
    exact_one_dimensional_exponent = kappa * background**2 / (1 - 2 * kappa * lam)
    assert_equal("large-field regulator square coefficient", alpha, Fraction(5, 4))
    assert_equal("large-field regulator square shift", shift, Fraction(2, 5))
    assert_equal(
        "large-field regulator completing-square constant",
        square_completion_constant,
        Fraction(6, 5),
    )
    assert_equal(
        "large-field regulator one-dimensional exponent",
        exact_one_dimensional_exponent,
        square_completion_constant,
    )


def check_source_window_extraction_error():
    def factorial(n):
        value = 1
        for integer in range(2, n + 1):
            value *= integer
        return value

    def multi_factorial(beta):
        value = 1
        for component in beta:
            value *= factorial(component)
        return value

    def total_degree(beta):
        return sum(beta)

    def derivative_at_origin(coefficients, beta):
        return multi_factorial(beta) * coefficients.get(beta, Fraction(0))

    coefficients = {
        (0, 0): Fraction(1),
        (1, 0): Fraction(2),
        (0, 1): Fraction(-3),
        (2, 0): Fraction(5),
        (1, 1): Fraction(-7),
        (0, 2): Fraction(11),
        (3, 0): Fraction(13),
        (2, 1): Fraction(-17),
        (0, 3): Fraction(19),
    }

    retained_degree_two = {
        beta: coefficient
        for beta, coefficient in coefficients.items()
        if total_degree(beta) <= 2
    }
    tail_degree_two = {
        beta: coefficients.get(beta, Fraction(0)) - retained_degree_two.get(beta, Fraction(0))
        for beta in coefficients
    }

    for beta in [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]:
        assert_equal(
            f"source extraction retained derivative {beta}",
            derivative_at_origin(tail_degree_two, beta),
            Fraction(0),
        )

    third_beta = (2, 1)
    omitted_third_derivative = derivative_at_origin(tail_degree_two, third_beta)
    assert_equal("source extraction omitted third derivative", omitted_third_derivative, Fraction(-34))

    retained_degree_three = {
        beta: coefficient
        for beta, coefficient in coefficients.items()
        if total_degree(beta) <= 3
    }
    tail_degree_three = {
        beta: coefficients.get(beta, Fraction(0)) - retained_degree_three.get(beta, Fraction(0))
        for beta in coefficients
    }
    assert_equal(
        "source extraction degree-three chart controls third derivative",
        derivative_at_origin(tail_degree_three, third_beta),
        Fraction(0),
    )

    radii = (Fraction(2), Fraction(3))
    majorant = sum(
        abs(coefficient) * radii[0] ** beta[0] * radii[1] ** beta[1]
        for beta, coefficient in coefficients.items()
    )
    rho_beta = radii[0] ** third_beta[0] * radii[1] ** third_beta[1]
    cauchy_bound = multi_factorial(third_beta) * majorant / rho_beta
    assert_equal("source extraction Cauchy majorant", majorant, Fraction(996))
    assert_equal("source extraction Cauchy bound", cauchy_bound, Fraction(166))
    assert_true("source omitted derivative below Cauchy bound", abs(omitted_third_derivative) <= cauchy_bound)

    propagation_norms = [Fraction(1, 2), Fraction(2, 3), Fraction(1, 4)]
    source_tail_norms = [Fraction(7), Fraction(5), Fraction(11)]
    retained_source_degrees = [2, 1, 3]
    scale_factor = multi_factorial(third_beta) / rho_beta
    propagated_bound = sum(
        propagation * scale_factor * tail_norm
        for propagation, tail_norm, retained_degree in zip(
            propagation_norms,
            source_tail_norms,
            retained_source_degrees,
        )
        if retained_degree < total_degree(third_beta)
    )
    assert_equal("source propagated Cauchy-tail bound", propagated_bound, Fraction(41, 36))

    actual_tail_derivatives = [Fraction(1, 3), Fraction(-1, 4), Fraction(0)]
    actual_window_error = sum(
        propagation * derivative
        for propagation, derivative in zip(propagation_norms, actual_tail_derivatives)
    )
    assert_equal("source propagated example cancellation", actual_window_error, Fraction(0))
    assert_true("source propagated example below bound", abs(actual_window_error) <= propagated_bound)


def check_finite_source_window_to_cumulant_distribution_bound():
    def factorial(n):
        value = 1
        for integer in range(2, n + 1):
            value *= integer
        return value

    def multi_factorial(beta):
        value = 1
        for component in beta:
            value *= factorial(component)
        return value

    radii = (Fraction(2), Fraction(3), Fraction(5))
    beta = (1, 2, 0)
    epsilon = Fraction(1, 240)
    rho_beta = product(radius ** exponent for radius, exponent in zip(radii, beta))
    cauchy_bound = multi_factorial(beta) * epsilon / rho_beta
    assert_equal("finite source-window rho beta", rho_beta, Fraction(18))
    assert_equal("finite source-window cumulant Cauchy bound", cauchy_bound, Fraction(1, 2160))

    # Model a compatible pair E subset F.  The coefficient of z_1 z_2^2 in
    # W_F restricts to the same coefficient in W_E, so the extracted cumulant
    # derivative is independent of which containing source window is used.
    coefficient_e = Fraction(1, 5000)
    coefficient_f = coefficient_e
    cumulant_e = multi_factorial(beta) * coefficient_e
    cumulant_f = multi_factorial(beta) * coefficient_f
    assert_equal("finite source-window restriction derivative", cumulant_f, cumulant_e)
    assert_true("finite source-window derivative below Cauchy bound", abs(cumulant_e) <= cauchy_bound)

    # If a larger window changes the restricted coefficient, compatibility
    # fails before any distributional extension can be claimed.
    bad_coefficient_f = Fraction(1, 4000)
    bad_cumulant_f = multi_factorial(beta) * bad_coefficient_f
    assert_true("finite source-window restriction defect detected", bad_cumulant_f != cumulant_e)

    # Uniform Schwartz-seminorm boundedness is a separate requirement from the
    # Cauchy extraction.  This finite arithmetic models the bound
    # |S(f_1,f_2)| <= C q(f_1 tensor f_2) and a failed declared constant.
    cumulant_value = Fraction(7, 9)
    seminorm_value = Fraction(5, 6)
    good_constant = Fraction(2)
    bad_constant = Fraction(1, 2)
    assert_true(
        "finite source-window Schwartz bound holds",
        abs(cumulant_value) <= good_constant * seminorm_value,
    )
    assert_true(
        "finite source-window Schwartz bound failure detected",
        abs(cumulant_value) > bad_constant * seminorm_value,
    )


def check_source_chart_to_holomorphic_window_bound():
    def factorial(n):
        value = 1
        for integer in range(2, n + 1):
            value *= integer
        return value

    def multi_factorial(beta):
        value = 1
        for component in beta:
            value *= factorial(component)
        return value

    normalizing_defect = Fraction(1, 100)
    local_coordinate_defect = Fraction(1, 50)
    polymer_tail_defect = Fraction(1, 75)
    finite_step_remainder = Fraction(1, 200)
    chart_lipschitz = Fraction(3)
    window_bound = (
        normalizing_defect
        + chart_lipschitz * (local_coordinate_defect + polymer_tail_defect)
        + finite_step_remainder
    )
    assert_equal("source chart to holomorphic window bound", window_bound, Fraction(23, 200))

    radii = (Fraction(2), Fraction(4))
    beta = (2, 1)
    rho_beta = product(radius ** exponent for radius, exponent in zip(radii, beta))
    derivative_bound = multi_factorial(beta) * window_bound / rho_beta
    assert_equal("source chart to window rho beta", rho_beta, Fraction(16))
    assert_equal("source chart induced cumulant bound", derivative_bound, Fraction(23, 1600))

    actual_derivative_difference = Fraction(1, 100)
    assert_true(
        "source chart induced cumulant difference controlled",
        actual_derivative_difference <= derivative_bound,
    )

    # A shrinking source radius can destroy the derivative estimate even when
    # the uniform source-functional error itself tends to zero.
    shrinking_radius = Fraction(1, 10)
    shrinking_error = Fraction(1, 100)
    fixed_radius_bound = shrinking_error / Fraction(2)
    shrinking_radius_bound = shrinking_error / shrinking_radius
    assert_true(
        "shrinking source radius weakens Cauchy derivative control",
        shrinking_radius_bound > fixed_radius_bound,
    )


def check_source_stable_trajectory_window_bound():
    theta = Fraction(1, 2)
    stable_initial = Fraction(1, 5)
    stable_defects = [Fraction(1, 100), Fraction(1, 200), Fraction(1, 400)]
    steps = len(stable_defects)
    stable_bound = (
        theta**steps * stable_initial
        + sum(
            theta ** (steps - 1 - index) * defect
            for index, defect in enumerate(stable_defects)
        )
    )
    assert_equal("source-stable trajectory bound", stable_bound, Fraction(13, 400))

    unstable_eigenvalue = Fraction(3)
    unstable_initial = Fraction(1, 1000)
    unstable_defects = [Fraction(1, 3000), Fraction(1, 9000), Fraction(1, 27000)]
    unstable_bound = (
        unstable_eigenvalue**steps * unstable_initial
        + sum(
            unstable_eigenvalue ** (steps - 1 - index) * defect
            for index, defect in enumerate(unstable_defects)
        )
    )
    assert_equal("source-unstable finite-depth amplification", unstable_bound, Fraction(41, 1350))

    chart_lipschitz = Fraction(2)
    normalizing_defect = Fraction(1, 500)
    polymer_tail_defect = Fraction(1, 300)
    finite_step_remainder = Fraction(1, 600)
    source_window_bound = (
        normalizing_defect
        + chart_lipschitz * (stable_bound + unstable_bound + polymer_tail_defect)
        + finite_step_remainder
    )
    assert_equal("source-stable chart to window bound", source_window_bound, Fraction(1837, 13500))

    actual_window_difference = Fraction(1, 10)
    assert_true(
        "source-stable chart controls sample window difference",
        actual_window_difference <= source_window_bound,
    )

    bad_unstable_initial = Fraction(1, 100)
    bad_unstable_amplification = unstable_eigenvalue**steps * bad_unstable_initial
    assert_equal("source-unstable mistuning amplification", bad_unstable_amplification, Fraction(27, 100))
    assert_true(
        "source-unstable mistuning exceeds controlled window bound",
        bad_unstable_amplification > source_window_bound,
    )


def check_finite_volume_source_window_cluster_tail():
    def factorial(n):
        value = 1
        for integer in range(2, n + 1):
            value *= integer
        return value

    def multi_factorial(beta):
        value = 1
        for component in beta:
            value *= factorial(component)
        return value

    radii = (Fraction(2), Fraction(2))
    beta = (1, 1)
    amplitude = Fraction(3)
    decay = Fraction(1, 2)
    boundary_distance = 3
    tail_bound = amplitude * decay**boundary_distance
    rho_beta = product(radius ** exponent for radius, exponent in zip(radii, beta))
    derivative_bound = multi_factorial(beta) * tail_bound / rho_beta
    assert_equal("finite-volume source-window tail bound", tail_bound, Fraction(3, 8))
    assert_equal("finite-volume source-window Cauchy derivative bound", derivative_bound, Fraction(3, 32))

    actual_derivative_difference = Fraction(1, 40)
    assert_true(
        "finite-volume source-window derivative below boundary tail",
        abs(actual_derivative_difference) <= derivative_bound,
    )

    later_distance = 5
    later_derivative_bound = (
        multi_factorial(beta)
        * amplitude
        * decay**later_distance
        / rho_beta
    )
    assert_true(
        "finite-volume source-window tail decreases with boundary distance",
        later_derivative_bound < derivative_bound,
    )

    # Two cofinal exhaustions are compared through a common larger volume.
    # The finite Cauchy bound is the sum of the two boundary tails, not an
    # assumption that the two finite volumes are nested.
    first_distance = 4
    second_distance = 6
    cofinal_bound = (
        multi_factorial(beta)
        * amplitude
        * (decay**first_distance + decay**second_distance)
        / rho_beta
    )
    assert_equal("finite-volume cofinal exhaustion comparison", cofinal_bound, Fraction(15, 256))
    exhaustion_difference = Fraction(1, 100)
    assert_true(
        "finite-volume cofinal comparison controls difference",
        exhaustion_difference <= cofinal_bound,
    )


def main():
    check_block_kernel_constant_field_scaling()
    check_distribution_pairing_for_block_constant_tests()
    check_adjoint_source_blocking_identity_and_smooth_error()
    check_independent_covariance_scaling()
    check_geometric_reconstruction_bound()
    check_correction_to_scaling_bookkeeping()
    check_auxiliary_transfer_telescoping_bound()
    check_auxiliary_projective_window_transfer_estimate()
    check_relevant_direction_tuning_amplification()
    check_quantitative_microscopic_tuning_contraction()
    check_c1_stable_graph_derivative_equation()
    check_observable_germ_finite_window_estimate()
    check_projective_distribution_window_extension()
    check_cofinal_finite_window_assembly()
    check_qft_strength_observable_germ_windows()
    check_reflection_positive_block_spin_pullback()
    check_finite_os_positivity_bound()
    check_finite_os_positivity_family_size_obstruction()
    check_positive_time_translation_window_bound()
    check_stable_chart_observable_window_bound()
    check_polymer_contraction_budget()
    check_polymer_pair_overlap_majorant()
    check_polymer_multiscale_forcing_budget()
    check_finite_range_gaussian_factorization()
    check_localization_taylor_remainder_bound()
    check_localization_scaling_exponents()
    check_large_field_gaussian_regulator_bound()
    check_source_window_extraction_error()
    check_finite_source_window_to_cumulant_distribution_bound()
    check_source_chart_to_holomorphic_window_bound()
    check_source_stable_trajectory_window_bound()
    check_finite_volume_source_window_cluster_tail()
    print("All short-range scalar RG reconstruction checks passed.")


if __name__ == "__main__":
    main()
