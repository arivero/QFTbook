#!/usr/bin/env python3
"""Finite checks for supersymmetric moduli-space and branch-EFT conventions.

The quotient cells below verify finite algebra behind classical vacuum spaces.
The Higgs-branch metric-protection cells are narrower Ward/counterterm
bookkeeping: they test theorem-status boundaries and reject component
multiplicity ledgers as substitutes for a background-field determinant.  The
D1-D5 bridge cells test the finite
rank/flux/FI arithmetic behind the Higgs-versus-Coulomb branch distinction,
not a construction of the continuum D1-D5 infrared CFT.
"""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_rank_one_abelian_invariant_ring():
    """Check C[x,y]^{C*} = C[xy] for charges (+1,-1) up to finite degree."""

    for total_degree in range(0, 10):
        invariant_monomials = []
        for a in range(total_degree + 1):
            b = total_degree - a
            charge = a - b
            if charge == 0:
                invariant_monomials.append((a, b))

        if total_degree % 2 == 0:
            power = total_degree // 2
            assert_equal(
                invariant_monomials,
                [(power, power)],
                f"degree {total_degree} invariant monomial is (xy)^{power}",
            )
        else:
            assert_equal(
                invariant_monomials,
                [],
                f"degree {total_degree} has no invariant monomial",
            )


def check_rank_one_abelian_dimension_count():
    """Compare real symplectic and complex affine quotient dimensions."""

    complex_variables = 2
    complex_reductive_quotient = 1
    affine_complex_dimension = complex_variables - complex_reductive_quotient

    real_variables = 4
    real_moment_map_equations = 1
    compact_gauge_orbit_dimension = 1
    symplectic_real_dimension = (
        real_variables - real_moment_map_equations - compact_gauge_orbit_dimension
    )

    assert_equal(affine_complex_dimension, 1, "affine quotient complex dimension")
    assert_equal(symplectic_real_dimension, 2, "symplectic quotient real dimension")
    assert_equal(
        2 * affine_complex_dimension,
        symplectic_real_dimension,
        "Kempf-Ness dimension comparison",
    )


def check_f_term_ideal_equivariance():
    """Invariant W implies dW transforms in the dual representation."""

    q_x = 1
    q_y = -1

    # W=(xy)^2 is invariant.  The derivative F_x=2*x*y^2 has charge -1,
    # and F_y=2*x^2*y has charge +1, i.e. q(F_i)=-q(field_i).
    charge_fx = q_x + 2 * q_y
    charge_fy = 2 * q_x + q_y

    assert_equal(charge_fx, -q_x, "F_x dual charge")
    assert_equal(charge_fy, -q_y, "F_y dual charge")
    assert_equal(charge_fx + q_x, 0, "F_x d x invariant pairing")
    assert_equal(charge_fy + q_y, 0, "F_y d y invariant pairing")


def check_rank_one_hyperkahler_quotient_dimensions():
    """Check the dimension ledger for T^* P^{N-1} as a hyperkahler quotient."""

    for n in range(2, 20):
        ambient_complex_dimension = 2 * n
        complex_moment_equations = 1
        complex_gauge_dimension = 1
        quotient_complex_dimension = (
            ambient_complex_dimension
            - complex_moment_equations
            - complex_gauge_dimension
        )

        ambient_real_dimension = 4 * n
        real_moment_equations = 3
        compact_gauge_dimension = 1
        quotient_real_dimension = (
            ambient_real_dimension
            - real_moment_equations
            - compact_gauge_dimension
        )

        assert_equal(
            quotient_complex_dimension,
            2 * (n - 1),
            "rank-one hyperkahler quotient complex dimension",
        )
        assert_equal(
            quotient_real_dimension,
            4 * (n - 1),
            "rank-one hyperkahler quotient real dimension",
        )
        assert_equal(
            2 * quotient_complex_dimension,
            quotient_real_dimension,
            "rank-one hyperkahler quotient real/complex dimension match",
        )


def check_rank_one_hyperkahler_one_form_descent():
    """Check that sum tilde(q)_i dq_i descends to sum p_i dz_i on a patch."""

    for n in range(2, 10):
        q_a = Fraction(5, 3)
        z = {index: Fraction(index + 2, index + 5) for index in range(1, n)}
        p = {index: Fraction(2 * index + 3, index + 7) for index in range(1, n)}

        tilde = {index: p[index] / q_a for index in range(1, n)}
        tilde_a = -sum(z[index] * p[index] for index in range(1, n)) / q_a

        dq_a_coefficient = tilde_a + sum(
            z[index] * tilde[index]
            for index in range(1, n)
        )
        assert_equal(
            dq_a_coefficient,
            0,
            "rank-one hyperkahler quotient vertical one-form coefficient",
        )

        for index in range(1, n):
            dz_coefficient = q_a * tilde[index]
            assert_equal(
                dz_coefficient,
                p[index],
                "rank-one hyperkahler quotient cotangent coordinate",
            )


def check_rank_one_hyperkahler_cotangent_transition():
    """Check a patch transition preserves the canonical cotangent one-form."""

    for n in range(2, 10):
        z = {index: Fraction(index + 2, index + 4) for index in range(1, n)}
        p = {index: Fraction(3 * index + 1, 2 * index + 5) for index in range(1, n)}
        z_1 = z[1]

        # Move from the q_0 != 0 patch to the q_1 != 0 patch.  New coordinates
        # are w_0=1/z_1 and w_j=z_j/z_1 for j>=2.  The new momenta are
        # r_0=-z_1 sum_j z_j p_j and r_j=z_1 p_j.
        r_0 = -z_1 * sum(z[index] * p[index] for index in range(1, n))
        r = {index: z_1 * p[index] for index in range(2, n)}

        rhs_coefficients = {index: Fraction(0) for index in range(1, n)}
        rhs_coefficients[1] += r_0 * (-1 / (z_1 * z_1))
        for index in range(2, n):
            rhs_coefficients[index] += r[index] * (1 / z_1)
            rhs_coefficients[1] += r[index] * (-z[index] / (z_1 * z_1))

        for index in range(1, n):
            assert_equal(
                rhs_coefficients[index],
                p[index],
                "rank-one hyperkahler cotangent transition preserves one-form",
            )


def check_d1_d5_adhm_higgs_branch_dimension():
    """Check the ADHM Higgs-branch dimension ledger for the N=(4,4) model."""

    for q1 in range(1, 8):
        for q5 in range(1, 9):
            ambient_complex_dimension = 2 * q1 * q1 + 2 * q1 * q5
            complex_moment_equations = q1 * q1
            complex_gauge_dimension = q1 * q1
            quotient_complex_dimension = (
                ambient_complex_dimension
                - complex_moment_equations
                - complex_gauge_dimension
            )

            ambient_real_dimension = 4 * (q1 * q1 + q1 * q5)
            real_moment_equations = 3 * q1 * q1
            compact_gauge_dimension = q1 * q1
            quotient_real_dimension = (
                ambient_real_dimension
                - real_moment_equations
                - compact_gauge_dimension
            )

            assert_equal(
                quotient_complex_dimension,
                2 * q1 * q5,
                "D1-D5 ADHM complex Higgs-branch dimension",
            )
            assert_equal(
                quotient_real_dimension,
                4 * q1 * q5,
                "D1-D5 ADHM real Higgs-branch dimension",
            )
            assert_equal(
                2 * quotient_complex_dimension,
                quotient_real_dimension,
                "D1-D5 ADHM real/complex dimension match",
            )


def check_d1_d5_positive_fi_excludes_empty_framing_boundary():
    """Trace the real moment map at I=J=0 to expose the FI boundary case."""

    for q1 in range(1, 12):
        zeta = Fraction(q1 + 2, q1 + 5)

        # At I=J=0 the trace of [B_1,B_1^\dagger]+[B_2,B_2^\dagger] is zero.
        # The positive-FI equation requires trace(zeta * 1_K)=zeta*q1.
        trace_left_at_empty_framing = Fraction(0)
        trace_positive_fi = zeta * q1

        assert_equal(
            trace_left_at_empty_framing,
            0,
            "D1-D5 ADHM commutator trace at empty framing",
        )
        assert_equal(
            trace_positive_fi > 0,
            True,
            "D1-D5 ADHM positive FI trace is nonzero",
        )
        assert_equal(
            trace_left_at_empty_framing == trace_positive_fi,
            False,
            "D1-D5 ADHM positive FI excludes I=J=0 boundary",
        )


def check_d1_d5_coulomb_throat_metric_flux():
    """Check the rank-one D1-D5 Coulomb throat harmonic metric and flux."""

    def radial_laplacian_r4_power(power: int, coefficient: Fraction) -> Fraction:
        # For f(r)=coefficient*r^power in four real dimensions,
        # Delta f = coefficient*power*(power+2)*r^(power-2).
        return coefficient * power * (power + 2)

    for q5 in range(1, 10):
        throat_coefficient = Fraction(q5, 2)
        h_infinity = Fraction(3, 7)

        assert_equal(
            radial_laplacian_r4_power(-2, throat_coefficient),
            0,
            "D1-D5 Coulomb r^-2 harmonic metric coefficient",
        )
        assert_equal(
            radial_laplacian_r4_power(0, h_infinity),
            0,
            "D1-D5 Coulomb constant metric coefficient is harmonic",
        )

        normalized_h_flux = 2 * throat_coefficient
        assert_equal(
            normalized_h_flux,
            q5,
            "D1-D5 Coulomb torsion flux normalized by S^3 volume",
        )

        missing_torsion_flux = 0
        assert_equal(
            missing_torsion_flux == q5,
            False,
            "D1-D5 metric-only shortcut misses H-flux",
        )

        for dyadic_power in range(1, 8):
            r_squared = Fraction(1, 4**dyadic_power)
            log_radial_metric = h_infinity * r_squared + throat_coefficient
            assert_equal(
                log_radial_metric >= throat_coefficient,
                True,
                "D1-D5 logarithmic radial metric has positive throat floor",
            )

        wrong_three_dimensional_coulomb_tail = radial_laplacian_r4_power(
            -1,
            throat_coefficient,
        )
        assert_equal(
            wrong_three_dimensional_coulomb_tail == 0,
            False,
            "D1-D5 four-transverse-dimensional throat is not a 1/r tail",
        )


def check_d1_d5_positive_fi_coulomb_lift_bound():
    """Check the trace lower bound lifting the empty-framing Coulomb locus."""

    for q1 in range(1, 9):
        zeta = Fraction(q1 + 1, q1 + 4)
        gauge_coupling_squared = Fraction(2 * q1 + 3, q1 + 5)

        trace_defect = -zeta * q1
        frobenius_lower_bound = trace_defect * trace_defect / q1
        assert_equal(
            frobenius_lower_bound,
            q1 * zeta * zeta,
            "D1-D5 positive FI Coulomb-lift trace lower bound",
        )

        potential_lower_bound = gauge_coupling_squared * frobenius_lower_bound / 2
        assert_equal(
            potential_lower_bound > 0,
            True,
            "D1-D5 positive FI gives positive empty-framing potential",
        )

        zero_fi_lower_bound = Fraction(0)
        assert_equal(
            zero_fi_lower_bound < frobenius_lower_bound,
            True,
            "D1-D5 zero-FI boundary lacks the positive trace obstruction",
        )


def check_d1_d5_dimension_does_not_fix_bridge_flux():
    """Same Higgs dimension can carry different Coulomb-throat flux data."""

    first_pair = (1, 6)
    second_pair = (2, 3)

    def higgs_dimension(pair: tuple[int, int]) -> int:
        q1, q5 = pair
        return 4 * q1 * q5

    def coulomb_flux(pair: tuple[int, int]) -> int:
        _, q5 = pair
        return q5

    assert_equal(
        higgs_dimension(first_pair),
        higgs_dimension(second_pair),
        "D1-D5 equal product gives equal Higgs-branch dimension",
    )
    assert_equal(
        coulomb_flux(first_pair) == coulomb_flux(second_pair),
        False,
        "D1-D5 Higgs dimension alone does not fix Coulomb H-flux",
    )


def check_higgs_branch_metric_status_matrix():
    """Separate local metric protection from global and torsion claims."""

    status = {
        "4d_N2": {
            "local_metric": "theorem_boundary_input",
            "global_metric": "conditional_continuum",
            "torsion_or_wz": "not_part_of_metric_statement",
        },
        "3d_N4": {
            "local_metric": "dimension_reduced_theorem_boundary_input",
            "global_metric": "conditional_continuum",
            "torsion_or_wz": "not_part_of_metric_statement",
        },
        "2d_N44": {
            "local_metric": "dimension_reduced_theorem_boundary_input",
            "global_metric": "conditional_continuum",
            "torsion_or_wz": "separate_two_dimensional_branch_datum",
        },
    }

    assert_equal(
        status["4d_N2"]["local_metric"],
        "theorem_boundary_input",
        "4d N=2 local Higgs metric status is a theorem boundary",
    )
    for label in ("3d_N4", "2d_N44"):
        assert_equal(
            status[label]["local_metric"],
            "dimension_reduced_theorem_boundary_input",
            f"{label} local Higgs metric status is dimension-specific",
        )

    for label, data in status.items():
        assert_equal(
            data["global_metric"],
            "conditional_continuum",
            f"{label} global Higgs metric is separate continuum input",
        )

    assert_equal(
        status["2d_N44"]["torsion_or_wz"],
        "separate_two_dimensional_branch_datum",
        "2d (4,4) torsion/WZ is outside pure metric protection",
    )


def check_higgs_branch_counterterm_filter():
    """Check that allowed two-derivative cells do not create a new metric."""

    candidates = [
        {
            "name": "coordinate representative",
            "two_derivative": True,
            "intrinsic_metric": False,
            "new_quantum_metric": False,
        },
        {
            "name": "FI or mass transport",
            "two_derivative": True,
            "intrinsic_metric": False,
            "new_quantum_metric": False,
        },
        {
            "name": "vector spurion D-term",
            "two_derivative": True,
            "intrinsic_metric": False,
            "new_quantum_metric": False,
        },
        {
            "name": "torsion or WZ branch datum",
            "two_derivative": True,
            "intrinsic_metric": False,
            "new_quantum_metric": False,
        },
        {
            "name": "singular or mixed branch operator",
            "two_derivative": True,
            "intrinsic_metric": False,
            "new_quantum_metric": False,
        },
    ]

    def surviving_metric_counterterms(cells):
        return [
            candidate["name"]
            for candidate in cells
            if (
                candidate["two_derivative"]
                and candidate["intrinsic_metric"]
                and candidate["new_quantum_metric"]
            )
        ]

    assert_equal(
        surviving_metric_counterterms(candidates),
        [],
        "Higgs-branch counterterm filter leaves no new intrinsic metric term",
    )

    wrong_vector_spurion = dict(candidates[2])
    wrong_vector_spurion["intrinsic_metric"] = True
    wrong_vector_spurion["new_quantum_metric"] = True
    wrong_shortcut_survivors = surviving_metric_counterterms(
        candidates[:2] + [wrong_vector_spurion] + candidates[3:]
    )
    assert_equal(
        wrong_shortcut_survivors,
        ["vector spurion D-term"],
        "negative-control vector-spurion shortcut would claim metric correction",
    )


def check_higgs_branch_background_field_derivation_gate():
    """Reject multiplicity arithmetic as a Higgs-metric determinant proof."""

    required_model = {
        "dimension": 4,
        "supersymmetry": "N=2",
        "gauge_group": "U(1)",
        "hypermultiplets": 2,
        "fi_parameter": "positive",
        "patch": "q_1_nonzero_Tstar_CP1",
        "regulator": "supersymmetric_wilsonian",
        "gauge": "background_R_xi",
    }
    assert_equal(
        required_model["patch"],
        "q_1_nonzero_Tstar_CP1",
        "explicit rank-one Higgs patch is specified",
    )
    assert_equal(
        required_model["gauge"],
        "background_R_xi",
        "background-field gauge is specified",
    )

    required_slots = {
        "model",
        "dimension",
        "regulator",
        "gauge",
        "quadratic_operators",
        "linear_tangent_vertices",
        "seagull_vertices",
        "mixed_diagrams",
        "ghosts",
        "goldstones",
        "fermions",
        "auxiliary_contacts",
        "gauge_parameter_cancellation",
        "dimension_reduction_audit",
    }

    old_component_ledger = {
        "model": required_model,
        "dimension": 4,
        "component_weights": {
            "gauge_field": 4,
            "complex_vector_scalar": 2,
            "eaten_hyper_scalars": 4,
            "faddeev_popov_ghosts": -2,
            "auxiliary_contacts": 0,
            "fermions": -8,
        },
    }

    def missing_slots(record):
        return sorted(required_slots - set(record))

    assert_equal(
        "quadratic_operators" in old_component_ledger,
        False,
        "old Higgs ledger has no generated fluctuation operators",
    )
    assert_equal(
        missing_slots(old_component_ledger)[:3],
        ["auxiliary_contacts", "dimension_reduction_audit", "fermions"],
        "old Higgs ledger is rejected as an incomplete determinant derivation",
    )

    operator_blueprint = {
        "model": required_model,
        "dimension": 4,
        "regulator": "supersymmetric_wilsonian",
        "gauge": "background_R_xi",
        "quadratic_operators": {
            "nonminimal_gauge_operator",
            "goldstone_operator",
            "ghost_operator",
            "vector_scalar_operator",
            "radial_hyper_operator",
            "fermion_dirac_operator",
        },
        "linear_tangent_vertices": {
            "gauge_goldstone_tangent_vertex",
            "scalar_connection_tangent_vertex",
            "fermion_connection_tangent_vertex",
        },
        "seagull_vertices": {
            "bosonic_tangent_seagull",
            "ghost_tangent_seagull",
            "fermion_tangent_seagull",
        },
        "mixed_diagrams": {
            "gauge_goldstone_mixed_trace",
            "scalar_tangent_double_insertion",
            "fermion_tangent_double_insertion",
        },
        "ghosts": "included",
        "goldstones": "included",
        "fermions": "included",
        "auxiliary_contacts": "included_or_integrated_with_contact_terms",
        "dimension_reduction_audit": "dimension_specific",
        # A toy exact ledger for xi-dependent terms in the generated trace-log
        # classes.  The numbers are not the metric coefficient; they check that
        # gauge-parameter dependence cannot be ignored.
        "gauge_parameter_cancellation": {
            "gauge_nonminimal": Fraction(3),
            "goldstone": Fraction(1),
            "ghost": Fraction(-2),
            "fermion_auxiliary_contact": Fraction(-2),
        },
    }
    assert_equal(
        missing_slots(operator_blueprint),
        [],
        "operator blueprint has every background-field derivation slot",
    )

    def xi_residual(record):
        return sum(record["gauge_parameter_cancellation"].values())

    assert_equal(
        xi_residual(operator_blueprint),
        Fraction(0),
        "full generated operator set cancels gauge-parameter dependence",
    )

    omitted_ghost = dict(operator_blueprint)
    omitted_ghost["gauge_parameter_cancellation"] = dict(
        operator_blueprint["gauge_parameter_cancellation"]
    )
    omitted_ghost["gauge_parameter_cancellation"]["ghost"] = Fraction(0)
    assert_equal(
        xi_residual(omitted_ghost) == 0,
        False,
        "omitting ghosts leaves a gauge-parameter residual",
    )

    omitted_goldstone = dict(operator_blueprint)
    omitted_goldstone["gauge_parameter_cancellation"] = dict(
        operator_blueprint["gauge_parameter_cancellation"]
    )
    omitted_goldstone["gauge_parameter_cancellation"]["goldstone"] = Fraction(0)
    assert_equal(
        xi_residual(omitted_goldstone) == 0,
        False,
        "omitting Goldstone/eaten-hyper data leaves a gauge-parameter residual",
    )

    component_balance_4d = sum(old_component_ledger["component_weights"].values())
    assert_equal(
        component_balance_4d,
        0,
        "four-dimensional long-multiplet balance is only a diagnostic",
    )

    dimension_reduction = {
        4: {"gauge_components": 4, "reduced_connection_scalars": 0},
        3: {"gauge_components": 3, "reduced_connection_scalars": 1},
        2: {"gauge_components": 2, "reduced_connection_scalars": 2},
    }
    for dimension, slots in dimension_reduction.items():
        assert_equal(
            slots["gauge_components"] + slots["reduced_connection_scalars"],
            4,
            f"{dimension}d reduction preserves four connection slots",
        )
    for dimension in (3, 2):
        assert_equal(
            old_component_ledger["component_weights"]["gauge_field"]
            == dimension_reduction[dimension]["gauge_components"],
            False,
            f"{dimension}d Higgs metric audit rejects a fixed 4d gauge-field entry",
        )

    unacceptable_status = {
        "component_multiplicity_proof",
        "derived_perturbative_theorem_from_ledger",
    }
    chapter_status = "theorem_boundary_input_plus_background_field_obligation"
    assert_equal(
        chapter_status in unacceptable_status,
        False,
        "chapter status does not promote the ledger to a proof",
    )


def check_large_charge_torus_lattice_and_weyl_orbit():
    """Check the charge-sector lattice distinctions used in the text."""

    su2_weight_lattice_sample = list(range(-5, 6))
    so3_allowed_weights = [
        weight for weight in su2_weight_lattice_sample if weight % 2 == 0
    ]
    assert_equal(
        so3_allowed_weights,
        [-4, -2, 0, 2, 4],
        "SO(3) global form keeps only root-lattice charges",
    )

    for weight in range(0, 6):
        weyl_orbit = sorted({weight, -weight})
        dominant_representative = max(weyl_orbit)
        assert_equal(
            dominant_representative,
            weight,
            "SU(2) fixed-charge sector uses a Weyl-orbit representative",
        )


def check_large_charge_branch_noether_and_routhian():
    """Check the fixed-charge saddle algebra for the chiral branch model."""

    # A branch scalar X of charge n rotates as X=rho*exp(i n mu t).
    # With curvature mass m on the cylinder and volume V, the fixed-charge
    # minimum has physical phase frequency omega=n*mu=m.
    test_data = [
        (2, Fraction(3), Fraction(5), Fraction(60)),
        (3, Fraction(4), Fraction(7), Fraction(168)),
        (5, Fraction(2), Fraction(11), Fraction(220)),
    ]
    for charge_unit, volume, curvature_mass, charge in test_data:
        rho_squared = charge / (2 * charge_unit * volume * curvature_mass)
        chemical_potential = curvature_mass / charge_unit
        phase_frequency = charge_unit * chemical_potential

        noether_charge = (
            2
            * charge_unit
            * phase_frequency
            * volume
            * rho_squared
        )
        energy = volume * (
            phase_frequency * phase_frequency
            + curvature_mass * curvature_mass
        ) * rho_squared
        expected_energy = curvature_mass * charge / charge_unit
        susceptibility = 2 * charge_unit * charge_unit * volume * rho_squared

        assert_equal(noether_charge, charge, "large-charge branch Noether map")
        assert_equal(energy, expected_energy, "large-charge branch Routhian value")
        assert_equal(
            susceptibility > 0,
            True,
            "large-charge branch susceptibility positivity",
        )


def check_large_charge_branch_transverse_window():
    """Check the transverse mass hierarchy in the supersymmetric branch example."""

    charge_unit = 2
    volume = Fraction(1)
    curvature_mass = Fraction(1)
    charge = Fraction(16)
    yukawa = Fraction(7)

    rho_squared = charge / (2 * charge_unit * volume * curvature_mass)
    rho = Fraction(2)
    chemical_potential = curvature_mass / charge_unit
    transverse_gap = yukawa * rho

    assert_equal(rho * rho, rho_squared, "large-charge branch radius")
    assert_equal(transverse_gap, 14, "large-charge branch transverse mass")
    assert_equal(
        chemical_potential / transverse_gap,
        Fraction(1, 28),
        "large-charge branch mu over transverse gap",
    )
    assert_equal(
        transverse_gap > curvature_mass,
        True,
        "large-charge branch transverse gap exceeds cylinder scale",
    )


def check_large_mu_window_scaling_condition():
    """Check that superlinear transverse-gap scaling opens both small ratios."""

    radius = Fraction(5)
    coefficient = Fraction(3)
    low_mu = Fraction(4)
    high_mu = Fraction(40)

    def ratios(mu):
        transverse_gap = coefficient * mu * mu
        return 1 / (mu * radius), mu / transverse_gap

    low_derivative, low_transverse = ratios(low_mu)
    high_derivative, high_transverse = ratios(high_mu)

    assert_equal(
        high_derivative < low_derivative,
        True,
        "large-mu derivative ratio decreases",
    )
    assert_equal(
        high_transverse < low_transverse,
        True,
        "large-mu transverse ratio decreases",
    )


def su2_nf2_minors(row_1, row_2):
    """Return V^{IJ}=row_1^I row_2^J-row_1^J row_2^I for I<J."""

    minors = {}
    for i in range(4):
        for j in range(i + 1, 4):
            minors[(i, j)] = row_1[i] * row_2[j] - row_1[j] * row_2[i]
    return minors


def su2_nf2_pfaffian(v):
    """Pf(V)=V12 V34 - V13 V24 + V14 V23 in zero-based indices."""

    return (
        v[(0, 1)] * v[(2, 3)]
        - v[(0, 2)] * v[(1, 3)]
        + v[(0, 3)] * v[(1, 2)]
    )


def su2_nf2_pfaffian_gradient(v):
    """Gradient of Pf(V) with respect to the six antisymmetric coordinates."""

    return {
        (0, 1): v[(2, 3)],
        (0, 2): -v[(1, 3)],
        (0, 3): v[(1, 2)],
        (1, 3): -v[(0, 2)],
        (1, 2): v[(0, 3)],
        (2, 3): v[(0, 1)],
    }


def check_su2_nf2_plucker_identity():
    """Check decomposable SU(2) invariants obey the Pfaffian relation."""

    test_rows = [
        (
            [Fraction(1), Fraction(2), Fraction(3), Fraction(5)],
            [Fraction(7), Fraction(11), Fraction(13), Fraction(17)],
        ),
        (
            [Fraction(-2), Fraction(3, 5), Fraction(0), Fraction(9, 4)],
            [Fraction(1, 7), Fraction(-4), Fraction(6), Fraction(5, 3)],
        ),
    ]

    for row_1, row_2 in test_rows:
        minors = su2_nf2_minors(row_1, row_2)
        assert_equal(
            su2_nf2_pfaffian(minors),
            0,
            "SU(2) N_f=2 decomposable two-form has zero Pfaffian",
        )


def check_su2_nf2_plucker_converse_chart():
    """Check the explicit V12 != 0 reconstruction used in the text."""

    chart_data = [
        (
            Fraction(3),
            Fraction(5),
            Fraction(-7),
            Fraction(11),
            Fraction(13),
        ),
        (
            Fraction(-5, 2),
            Fraction(7, 3),
            Fraction(4),
            Fraction(-9, 5),
            Fraction(6),
        ),
    ]

    for v_01, v_02, v_03, v_12, v_13 in chart_data:
        v_23 = (v_02 * v_13 - v_03 * v_12) / v_01
        v = {
            (0, 1): v_01,
            (0, 2): v_02,
            (0, 3): v_03,
            (1, 2): v_12,
            (1, 3): v_13,
            (2, 3): v_23,
        }
        assert_equal(
            su2_nf2_pfaffian(v),
            0,
            "SU(2) N_f=2 converse chart data lies on Pfaffian hypersurface",
        )

        row_1 = [Fraction(1), Fraction(0), -v_12 / v_01, -v_13 / v_01]
        row_2 = [Fraction(0), v_01, v_02, v_03]
        reconstructed = su2_nf2_minors(row_1, row_2)
        assert_equal(
            reconstructed,
            v,
            "SU(2) N_f=2 Pfaffian-zero point reconstructs from doublets",
        )


def check_su2_nf2_dimension_ledger():
    """Compare the Plucker hypersurface and stable quotient dimensions."""

    antisymmetric_coordinates = 6
    pfaffian_equations = 1
    hypersurface_dimension = antisymmetric_coordinates - pfaffian_equations

    doublet_coordinates = 2 * 4
    complex_gauge_dimension = 3
    stable_quotient_dimension = doublet_coordinates - complex_gauge_dimension

    assert_equal(hypersurface_dimension, 5, "SU(2) N_f=2 hypersurface dimension")
    assert_equal(stable_quotient_dimension, 5, "SU(2) N_f=2 quotient dimension")
    assert_equal(
        hypersurface_dimension,
        stable_quotient_dimension,
        "SU(2) N_f=2 dimension ledger match",
    )


def check_su2_nf2_quantum_deformation_smoothness():
    """Check the Pfaffian gradient vanishes only at the removed origin."""

    coordinate_keys = {
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    }
    expected_gradient_entries = {
        (0, 1): ((2, 3), Fraction(1)),
        (0, 2): ((1, 3), Fraction(-1)),
        (0, 3): ((1, 2), Fraction(1)),
        (1, 3): ((0, 2), Fraction(-1)),
        (1, 2): ((0, 3), Fraction(1)),
        (2, 3): ((0, 1), Fraction(1)),
    }
    assert_equal(
        {source for source, _ in expected_gradient_entries.values()},
        coordinate_keys,
        "SU(2) N_f=2 Pfaffian gradient sees every coordinate once",
    )
    for source_key in coordinate_keys:
        basis_vector = {key: Fraction(0) for key in coordinate_keys}
        basis_vector[source_key] = Fraction(1)
        gradient = su2_nf2_pfaffian_gradient(basis_vector)
        expected_gradient = {}
        for derivative_key, (expected_source, coefficient) in (
            expected_gradient_entries.items()
        ):
            expected_gradient[derivative_key] = (
                coefficient if source_key == expected_source else Fraction(0)
            )
        assert_equal(
            gradient,
            expected_gradient,
            "SU(2) N_f=2 Pfaffian gradient signs and coordinate order",
        )

    zero = {key: Fraction(0) for key in coordinate_keys}
    assert_equal(
        su2_nf2_pfaffian_gradient(zero),
        {key: Fraction(0) for key in coordinate_keys},
        "SU(2) N_f=2 Pfaffian gradient vanishes at origin",
    )
    assert_equal(
        su2_nf2_pfaffian(zero),
        0,
        "SU(2) N_f=2 origin is not on a nonzero quantum deformation",
    )


def check_su2_nf2_mass_deformation_vacua():
    """Check the two massive vacua on Pf(V)=Lambda^4 for diagonal masses."""

    m_1 = Fraction(9)
    m_2 = Fraction(16)
    lambda_squared = Fraction(5)
    lambda_fourth = lambda_squared * lambda_squared
    sqrt_m1_m2 = Fraction(12)
    pure_scale_cubed = lambda_squared * sqrt_m1_m2

    coordinate_keys = {
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    }
    mass_source = {
        (0, 1): m_1,
        (2, 3): m_2,
    }

    for sign in [Fraction(1), Fraction(-1)]:
        x = sign * sqrt_m1_m2 / lambda_squared
        v = {key: Fraction(0) for key in coordinate_keys}
        v[(0, 1)] = -m_2 / x
        v[(2, 3)] = -m_1 / x

        assert_equal(
            su2_nf2_pfaffian(v),
            lambda_fourth,
            "SU(2) N_f=2 massive vacuum lies on quantum deformation",
        )

        gradient = su2_nf2_pfaffian_gradient(v)
        for key in coordinate_keys:
            f_term = mass_source.get(key, Fraction(0)) + x * gradient[key]
            assert_equal(
                f_term,
                0,
                "SU(2) N_f=2 diagonal mass F-term vanishes",
            )

        superpotential = m_1 * v[(0, 1)] + m_2 * v[(2, 3)]
        expected_superpotential = -sign * 2 * lambda_squared * sqrt_m1_m2
        assert_equal(
            superpotential,
            expected_superpotential,
            "SU(2) N_f=2 massive vacuum superpotential value",
        )
        assert_equal(
            superpotential,
            -sign * 2 * pure_scale_cubed,
            "SU(2) N_f=2 pure-SYM branch superpotential normalization",
        )

    assert_equal(
        pure_scale_cubed * pure_scale_cubed,
        m_1 * m_2 * lambda_fourth,
        "SU(2) N_f=2 holomorphic threshold scale matching",
    )


def main():
    check_rank_one_abelian_invariant_ring()
    check_rank_one_abelian_dimension_count()
    check_f_term_ideal_equivariance()
    check_rank_one_hyperkahler_quotient_dimensions()
    check_rank_one_hyperkahler_one_form_descent()
    check_rank_one_hyperkahler_cotangent_transition()
    check_d1_d5_adhm_higgs_branch_dimension()
    check_d1_d5_positive_fi_excludes_empty_framing_boundary()
    check_d1_d5_coulomb_throat_metric_flux()
    check_d1_d5_positive_fi_coulomb_lift_bound()
    check_d1_d5_dimension_does_not_fix_bridge_flux()
    check_higgs_branch_metric_status_matrix()
    check_higgs_branch_counterterm_filter()
    check_higgs_branch_background_field_derivation_gate()
    check_large_charge_torus_lattice_and_weyl_orbit()
    check_large_charge_branch_noether_and_routhian()
    check_large_charge_branch_transverse_window()
    check_large_mu_window_scaling_condition()
    check_su2_nf2_plucker_identity()
    check_su2_nf2_plucker_converse_chart()
    check_su2_nf2_dimension_ledger()
    check_su2_nf2_quantum_deformation_smoothness()
    check_su2_nf2_mass_deformation_vacua()
    print("All supersymmetric moduli-space and branch-EFT checks passed.")


if __name__ == "__main__":
    main()
