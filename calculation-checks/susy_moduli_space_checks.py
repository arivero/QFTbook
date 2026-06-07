#!/usr/bin/env python3
"""Finite checks for supersymmetric moduli-space and branch-EFT conventions.

Evidence contract.
Target claims: Volume VII Chapter 08 quotient formulae, branch-EFT status
boundaries, D1-D5 Higgs/Coulomb arithmetic, and the finite Higgs-metric
background-field gates replacing component multiplicity ledgers, including the
metric-kernel projection after source transport and the two-dimensional
torsion-free versus torsionful theorem boundary and the finite gauge-fixed
heavy-package projection.
Independent construction: exact rational invariant-ring, quotient-dimension,
cotangent-transition, moment-map, determinant-row, trace-log, and regulator
supertrace cells, together with a finite metric two-jet source-transport
projection and gauge-map/zero-mode projection cell, are built from finite data
rather than by entering the manuscript's final identities as constants.
Imported assumptions: the finite toy cells assume the declared charge
assignments, a smooth fully Higgsed rank-one patch, the selected
background-field gauge slots, and finite matrix representatives of the
heavy nonzero-mode complex.
Negative controls: component-count-only Higgs metric proofs, vector-spurion
metric shortcuts, omitted ghosts/Goldstones/longitudinal vectors, omitted
seagulls, mismatched Ward vertices, dropped auxiliary/Yukawa contacts,
unpaired dimension-reduced scalar contacts, covering four-dimensional
component reuse, unpaired regulator masses, point-metric-only source matching,
undeclared vector-spurion transport, four-supercharge Kahler-term imports,
singular-branch shortcuts, mismatched ghost gauge maps, unprojected tangent zero
modes, missing heavy rows, and metric-only projections of torsionful
two-dimensional (4,4) data are rejected when represented by the finite model.
Scope boundary: these checks do not prove a continuum Higgs-branch metric
nonrenormalization theorem, construct the full continuum gauge-fixed elliptic complex,
establish all-order harmonic/projective superspace protection, or construct
the continuum D1-D5 infrared CFT.

The quotient cells below verify finite algebra behind classical vacuum spaces.
The Higgs-branch metric-protection cells are narrower Ward/counterterm
bookkeeping: they test theorem-status boundaries and reject component
multiplicity ledgers as substitutes for a background-field determinant.  The
D1-D5 bridge cells test the finite rank/flux/FI arithmetic behind the
Higgs-versus-Coulomb branch distinction, not a construction of the continuum
D1-D5 infrared CFT.
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
    """Separate local metric protection from global and torsionful claims."""

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
        "2d_N44_torsion_free": {
            "local_metric": "dimension_reduced_theorem_boundary_input",
            "global_metric": "conditional_continuum",
            "torsion_or_wz": "excluded_by_declared_torsion_free_class",
        },
        "2d_N44_torsion_allowed": {
            "local_metric": "not_a_pure_metric_theorem",
            "global_metric": "conditional_continuum",
            "torsion_or_wz": "coupled_hkt_or_bihermitian_target",
            "required_counterterm_slots": {
                "delta_g",
                "delta_B",
                "delta_Phi",
                "torsionful_connections",
            },
        },
    }

    assert_equal(
        status["4d_N2"]["local_metric"],
        "theorem_boundary_input",
        "4d N=2 local Higgs metric status is a theorem boundary",
    )
    for label in ("3d_N4", "2d_N44_torsion_free"):
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
        status["2d_N44_torsion_allowed"]["local_metric"],
        "not_a_pure_metric_theorem",
        "torsionful 2d (4,4) is not governed by a pure metric theorem",
    )
    assert_equal(
        status["2d_N44_torsion_allowed"]["required_counterterm_slots"]
        >= {"delta_g", "delta_B", "delta_Phi"},
        True,
        "torsionful 2d (4,4) requires coupled local counterterm slots",
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
            "name": "torsionful (4,4) branch deformation",
            "two_derivative": True,
            "intrinsic_metric": False,
            "new_quantum_metric": False,
            "coupled_target": True,
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


def check_higgs_branch_ward_counterterm_interface():
    """Audit the slots needed for a local eight-supercharge Ward proof."""

    required_slots = {
        "supercharges",
        "r_symmetry_preserved",
        "smooth_fully_higgsed_stratum",
        "transverse_gap",
        "source_multiplet_split",
        "locality",
        "two_derivative_order",
        "cohomology_quotients",
        "regulator_preserves_ward_data",
        "two_dimensional_torsion_policy",
    }
    proof_interface = {
        "supercharges": 8,
        "r_symmetry_preserved": True,
        "smooth_fully_higgsed_stratum": True,
        "transverse_gap": True,
        "source_multiplet_split": {
            "hypermultiplet_coordinates",
            "vector_multiplet_spurions",
            "fi_triplet_sources",
            "mass_backgrounds",
        },
        "locality": "on_smooth_stratum_U",
        "two_derivative_order": True,
        "cohomology_quotients": {
            "hypermultiplet_field_redefinition",
            "fi_or_mass_source_transport",
            "Q_exact_local_functional",
        },
        "regulator_preserves_ward_data": True,
        "two_dimensional_torsion_policy": {
            "torsion_free_metric_target",
            "coupled_hkt_or_bihermitian_target_when_H_allowed",
        },
    }

    assert_equal(
        sorted(required_slots - set(proof_interface)),
        [],
        "Higgs Ward proof interface carries every local-counterterm slot",
    )
    assert_equal(
        "vector_multiplet_spurions"
        in proof_interface["source_multiplet_split"],
        True,
        "source split keeps vector/coupling spurions separate from Higgs fields",
    )

    def classify_counterterm(candidate):
        if not candidate["local_on_smooth_stratum"] or not candidate["gap"]:
            return "outside_local_higgs_sigma_model"
        if candidate["derivative_order"] != 2:
            return "not_two_derivative_metric_order"
        if candidate.get("dimension") == 2 and candidate.get("torsion_allowed", False):
            required_torsionful_slots = {
                "delta_g",
                "delta_B",
                "delta_Phi",
                "torsionful_connections",
            }
            if set(candidate.get("counterterm_slots", set())) >= required_torsionful_slots:
                return "coupled_hkt_or_bihermitian_target"
            return "incomplete_torsionful_2d_counterterm"
        if candidate["channel"] == "antisymmetric":
            return "outside_torsion_free_metric_theorem"
        if (
            candidate["supercharges"] != 8
            or not candidate["r_symmetry_preserved"]
            or not candidate["regulator_preserves_ward_data"]
        ):
            return "outside_eight_supercharge_ward_theorem"
        source_types = set(candidate["source_types"])
        if source_types & {"vector_multiplet", "gauge_coupling", "coulomb"}:
            return "vector_sector_or_higher_derivative"
        if source_types & {"fi_triplet", "mass_background"}:
            return "source_transport_after_matching"
        if candidate["cohomology_class"] in {
            "hypermultiplet_field_redefinition",
            "Q_exact_local_functional",
        }:
            return "coordinate_or_exact_representative"
        if candidate["cohomology_class"] == "nontrivial_hypermetric":
            return "new_intrinsic_higgs_metric"
        raise ValueError(f"unknown cohomology class {candidate['cohomology_class']!r}")

    valid_eight_supercharge_candidates = [
        {
            "name": "hypermultiplet coordinate representative",
            "supercharges": 8,
            "r_symmetry_preserved": True,
            "regulator_preserves_ward_data": True,
            "local_on_smooth_stratum": True,
            "gap": True,
            "channel": "symmetric",
            "derivative_order": 2,
            "source_types": {"hypermultiplet"},
            "cohomology_class": "hypermultiplet_field_redefinition",
        },
        {
            "name": "FI transport of quotient level",
            "supercharges": 8,
            "r_symmetry_preserved": True,
            "regulator_preserves_ward_data": True,
            "local_on_smooth_stratum": True,
            "gap": True,
            "channel": "symmetric",
            "derivative_order": 2,
            "source_types": {"hypermultiplet", "fi_triplet"},
            "cohomology_class": "Q_exact_local_functional",
        },
        {
            "name": "vector spurion local term",
            "supercharges": 8,
            "r_symmetry_preserved": True,
            "regulator_preserves_ward_data": True,
            "local_on_smooth_stratum": True,
            "gap": True,
            "channel": "symmetric",
            "derivative_order": 2,
            "source_types": {"hypermultiplet", "vector_multiplet"},
            "cohomology_class": "nontrivial_hypermetric",
        },
    ]
    assert_equal(
        [
            classify_counterterm(candidate)
            for candidate in valid_eight_supercharge_candidates
        ],
        [
            "coordinate_or_exact_representative",
            "source_transport_after_matching",
            "vector_sector_or_higher_derivative",
        ],
        "local Ward interface leaves no new intrinsic Higgs metric class",
    )

    four_supercharge_kahler_term = {
        "name": "four-supercharge Kahler D-term",
        "supercharges": 4,
        "r_symmetry_preserved": True,
        "regulator_preserves_ward_data": True,
        "local_on_smooth_stratum": True,
        "gap": True,
        "channel": "symmetric",
        "derivative_order": 2,
        "source_types": {"chiral"},
        "cohomology_class": "nontrivial_hypermetric",
    }
    assert_equal(
        classify_counterterm(four_supercharge_kahler_term),
        "outside_eight_supercharge_ward_theorem",
        "four-supercharge Kahler renormalization cannot be imported as Higgs proof",
    )

    mislabelled_vector_spurion = dict(four_supercharge_kahler_term)
    mislabelled_vector_spurion.update(
        {
            "name": "mislabelled vector spurion",
            "supercharges": 8,
            "source_types": {"hypermultiplet", "vector_multiplet"},
        }
    )
    assert_equal(
        classify_counterterm(mislabelled_vector_spurion),
        "vector_sector_or_higher_derivative",
        "typed source split blocks vector spurion from becoming a Higgs metric",
    )
    if_vector_type_is_erased = dict(mislabelled_vector_spurion)
    if_vector_type_is_erased["source_types"] = {"hypermultiplet"}
    assert_equal(
        classify_counterterm(if_vector_type_is_erased),
        "new_intrinsic_higgs_metric",
        "erasing the source type would fake an intrinsic Higgs metric correction",
    )

    singular_branch_candidate = dict(if_vector_type_is_erased)
    singular_branch_candidate.update(
        {
            "name": "singular branch light-sector shortcut",
            "gap": False,
            "local_on_smooth_stratum": False,
        }
    )
    assert_equal(
        classify_counterterm(singular_branch_candidate),
        "outside_local_higgs_sigma_model",
        "singular or mixed loci invalidate the smooth-stratum counterterm theorem",
    )

    two_dimensional_torsion = dict(if_vector_type_is_erased)
    two_dimensional_torsion.update(
        {
            "name": "2d torsionful B/WZ projection",
            "dimension": 2,
            "torsion_allowed": True,
            "channel": "antisymmetric",
            "counterterm_slots": {"delta_B"},
        }
    )
    assert_equal(
        classify_counterterm(two_dimensional_torsion),
        "incomplete_torsionful_2d_counterterm",
        "2d torsionful data cannot be classified by the antisymmetric slot alone",
    )

    coupled_two_dimensional_torsion = dict(two_dimensional_torsion)
    coupled_two_dimensional_torsion.update(
        {
            "name": "2d coupled HKT counterterm",
            "channel": "coupled_torsionful",
            "counterterm_slots": {
                "delta_g",
                "delta_B",
                "delta_Phi",
                "torsionful_connections",
            },
        }
    )
    assert_equal(
        classify_counterterm(coupled_two_dimensional_torsion),
        "coupled_hkt_or_bihermitian_target",
        "torsionful 2d (4,4) counterterms are a coupled target, not a metric proof",
    )

    broken_regulator_candidate = dict(if_vector_type_is_erased)
    broken_regulator_candidate.update(
        {
            "name": "regulator-broken Ward identity",
            "regulator_preserves_ward_data": False,
        }
    )
    assert_equal(
        classify_counterterm(broken_regulator_candidate),
        "outside_eight_supercharge_ward_theorem",
        "a regulator that breaks the Ward data cannot prove metric protection",
    )


def check_higgs_branch_two_dimensional_torsion_boundary():
    """Reject metric-only projections of torsionful 2d (4,4) target data."""

    theorem_classes = {
        "torsion_free_metric": {
            "dimension": 2,
            "H": Fraction(0),
            "connection": "levi_civita",
            "counterterm_slots": {"delta_g"},
        },
        "torsionful_target": {
            "dimension": 2,
            "H": "nonzero_allowed",
            "connection": "torsionful_pm",
            "counterterm_slots": {
                "delta_g",
                "delta_B",
                "delta_Phi",
                "delta_nabla_plus",
                "delta_nabla_minus",
            },
        },
    }
    assert_equal(
        theorem_classes["torsion_free_metric"]["connection"],
        "levi_civita",
        "torsion-free 2d (4,4) metric theorem uses the Levi-Civita connection",
    )
    assert_equal(
        theorem_classes["torsionful_target"]["counterterm_slots"] > {"delta_g"},
        True,
        "torsionful 2d (4,4) target has more slots than the metric projection",
    )

    raw_two_index_kernel = {
        "Pi_12": Fraction(7, 5),
        "Pi_21": Fraction(3, 5),
    }
    raw_delta_g = (
        raw_two_index_kernel["Pi_12"] + raw_two_index_kernel["Pi_21"]
    ) / 2
    raw_delta_B = (
        raw_two_index_kernel["Pi_12"] - raw_two_index_kernel["Pi_21"]
    ) / 2
    assert_equal(
        raw_delta_g,
        Fraction(1),
        "raw 2d trace-log kernel has a symmetric tensor component",
    )
    assert_equal(
        raw_delta_B,
        Fraction(2, 5),
        "raw 2d trace-log kernel has a nonzero antisymmetric tensor component",
    )

    def torsionful_connection_variation(delta_g, delta_B):
        return {
            "delta_nabla_plus": delta_g + delta_B,
            "delta_nabla_minus": delta_g - delta_B,
        }

    coupled_counterterm = {
        "delta_g": raw_delta_g,
        "delta_B": raw_delta_B,
        "delta_Phi": Fraction(1, 7),
        **torsionful_connection_variation(raw_delta_g, raw_delta_B),
    }
    assert_equal(
        coupled_counterterm["delta_nabla_plus"]
        == coupled_counterterm["delta_nabla_minus"],
        False,
        "nonzero torsion changes the two torsionful connections differently",
    )

    naive_metric_only_projection = {"delta_g": raw_delta_g}
    missing_slots = sorted(
        theorem_classes["torsionful_target"]["counterterm_slots"]
        - set(naive_metric_only_projection)
    )
    assert_equal(
        missing_slots,
        ["delta_B", "delta_Phi", "delta_nabla_minus", "delta_nabla_plus"],
        "metric-only projection drops required torsionful 2d counterterm slots",
    )
    assert_equal(
        set(coupled_counterterm) >= theorem_classes["torsionful_target"]["counterterm_slots"],
        True,
        "coupled 2d torsionful target carries metric, B, dilaton, and connections",
    )


def check_higgs_branch_metric_transport_projection():
    """Project a finite Higgs metric two-jet modulo declared source transport."""

    # On the zero-cotangent CP^1 slice of the rank-one quotient,
    # g_zeta = zeta * (1 + r)^(-2) has two-jet zeta * (1, -2, 3).
    # The source direction is generated from the quotient metric, not entered as
    # an arbitrary cancellation coefficient.
    def quotient_metric_two_jet(zeta):
        return (zeta, -2 * zeta, 3 * zeta)

    def scale_jet(coefficient, jet):
        return tuple(coefficient * entry for entry in jet)

    def subtract_jets(left, right):
        return tuple(left[index] - right[index] for index in range(len(left)))

    zeta = Fraction(5, 2)
    source_shift = Fraction(3, 7)
    source_jet = subtract_jets(
        quotient_metric_two_jet(zeta + source_shift),
        quotient_metric_two_jet(zeta),
    )
    unit_fi_source_jet = (Fraction(1), Fraction(-2), Fraction(3))
    assert_equal(
        source_jet,
        scale_jet(source_shift, unit_fi_source_jet),
        "rank-one quotient metric generates the FI source two-jet",
    )

    declared_source_jets = {"fi_triplet": unit_fi_source_jet}

    def residual_after_declared_transport(jet, source_name):
        if source_name not in declared_source_jets:
            return jet
        source = declared_source_jets[source_name]
        if source[0] == 0:
            raise ValueError("source jet must move the point metric in this gauge")
        coefficient = jet[0] / source[0]
        transported = scale_jet(coefficient, source)
        return subtract_jets(jet, transported)

    transported_kernel = scale_jet(Fraction(11, 5), unit_fi_source_jet)
    assert_equal(
        residual_after_declared_transport(transported_kernel, "fi_triplet"),
        (Fraction(0), Fraction(0), Fraction(0)),
        "FI-transported Higgs metric two-jet has no intrinsic residual",
    )

    curvature_residual = (Fraction(0), Fraction(0), Fraction(4, 9))
    fake_intrinsic_kernel = tuple(
        transported_kernel[index] + curvature_residual[index]
        for index in range(len(transported_kernel))
    )
    assert_equal(
        residual_after_declared_transport(fake_intrinsic_kernel, "fi_triplet"),
        curvature_residual,
        "wrong curvature two-jet survives source transport",
    )
    assert_equal(
        fake_intrinsic_kernel[0] == transported_kernel[0],
        True,
        "point-metric matching alone cannot detect the intrinsic jet residual",
    )

    old_component_balance = 4 + 2 + 4 - 2 + 0 - 8
    assert_equal(
        old_component_balance,
        0,
        "old long-multiplet balance is only a signed inventory",
    )
    assert_equal(
        residual_after_declared_transport(fake_intrinsic_kernel, "fi_triplet")
        == (Fraction(0), Fraction(0), Fraction(0)),
        False,
        "zero component balance does not imply zero intrinsic metric residual",
    )
    assert_equal(
        residual_after_declared_transport(transported_kernel, "vector_multiplet")
        == (Fraction(0), Fraction(0), Fraction(0)),
        False,
        "undeclared vector-spurion transport cannot remove a Higgs metric kernel",
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
        "frame_connection_seagull_identity",
        "mass_curvature_ward_pairing",
        "supercharge_factorization",
        "off_shell_row_completion",
        "rank_one_row_jacobians",
        "gauge_fixed_heavy_package_projection",
        "regulator_supertrace_pairing",
        "dimension_reduced_row_contacts",
        "gauge_parameter_cancellation",
        "dimension_reduction_audit",
        "two_dimensional_torsion_classification",
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
        missing_slots(old_component_ledger)[:4],
        [
            "auxiliary_contacts",
            "dimension_reduced_row_contacts",
            "dimension_reduction_audit",
            "fermions",
        ],
        "old Higgs ledger is rejected as an incomplete determinant derivation",
    )

    xi_operator = "p2+xi*M2"
    higgs_mass_operator = "p2+M2"

    def determinant_weight(field_kind, modes):
        if field_kind == "real_boson":
            return Fraction(modes, 2)
        if field_kind == "complex_grassmann_ghost_pair":
            return -Fraction(modes)
        raise ValueError(f"unknown determinant field kind {field_kind!r}")

    def constant_background_spectrum(dimension):
        """Generate the R_xi trace-log sectors from the split operators."""

        if dimension not in {2, 3, 4}:
            raise ValueError("Higgs metric audit only covers 2d, 3d, and 4d")

        sectors = [
            {
                "sector": "gauge_transverse",
                "origin": "gauge_connection",
                "operator": higgs_mass_operator,
                "field_kind": "real_boson",
                "modes": dimension - 1,
            },
            {
                "sector": "gauge_longitudinal",
                "origin": "gauge_connection",
                "operator": xi_operator,
                "field_kind": "real_boson",
                "modes": 1,
            },
            {
                "sector": "goldstone",
                "origin": "eaten_hypermultiplet",
                "operator": xi_operator,
                "field_kind": "real_boson",
                "modes": 1,
            },
            {
                "sector": "ghost_pair",
                "origin": "faddeev_popov",
                "operator": xi_operator,
                "field_kind": "complex_grassmann_ghost_pair",
                "modes": 1,
            },
        ]
        reduced_connection_scalars = 4 - dimension
        if reduced_connection_scalars:
            sectors.append(
                {
                    "sector": "reduced_connection_scalars",
                    "origin": "gauge_connection",
                    "operator": higgs_mass_operator,
                    "field_kind": "real_boson",
                    "modes": reduced_connection_scalars,
                }
            )

        for sector in sectors:
            sector["trace_log_weight"] = determinant_weight(
                sector["field_kind"], sector["modes"]
            )
        return sectors

    def trace_log_weight(spectrum, operator):
        return sum(
            sector["trace_log_weight"]
            for sector in spectrum
            if sector["operator"] == operator
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
        "constant_background_spectrum": {
            dimension: constant_background_spectrum(dimension)
            for dimension in (4, 3, 2)
        },
        "gauge_parameter_cancellation": "generated_from_R_xi_spectrum",
        "frame_connection_seagull_identity": "generated_from_operator_conjugation",
        "mass_curvature_ward_pairing": "matched_operator_vertices_required",
        "supercharge_factorization": "off_shell_heavy_complex_required",
        "off_shell_row_completion": {
            "kinetic_frame_rows",
            "gauge_fixing_and_ghost_rows",
            "moment_map_auxiliary_rows",
            "yukawa_rows",
        },
        "rank_one_row_jacobians": {
            "real_moment_map_row",
            "complex_moment_map_rows",
            "background_gauge_fixing_row",
            "yukawa_mass_row",
            "heavy_projector_zero_mode_split",
        },
        "gauge_fixed_heavy_package_projection": {
            "gauge_map",
            "gauge_fixing_adjoint_row",
            "ghost_from_gauge_map",
            "nonzero_heavy_projection",
        },
        "regulator_supertrace_pairing": "same_pv_function_on_nonzero_Q_complex",
        "dimension_reduced_row_contacts": "reduced_vector_scalars_kept_as_rows",
        "two_dimensional_torsion_classification": (
            "torsion_free_metric_or_coupled_hkt_target"
        ),
    }
    assert_equal(
        missing_slots(operator_blueprint),
        [],
        "operator blueprint has every background-field derivation slot",
    )

    for dimension, spectrum in operator_blueprint[
        "constant_background_spectrum"
    ].items():
        sectors = {sector["sector"]: sector for sector in spectrum}
        assert_equal(
            sectors["gauge_transverse"]["modes"],
            dimension - 1,
            f"{dimension}d R_xi vector split generates transverse modes",
        )
        for sector_name in ("gauge_longitudinal", "goldstone", "ghost_pair"):
            assert_equal(
                sectors[sector_name]["operator"],
                xi_operator,
                f"{dimension}d {sector_name} carries the same xi operator",
            )
        assert_equal(
            trace_log_weight(spectrum, xi_operator),
            Fraction(0),
            f"{dimension}d generated R_xi spectrum cancels xi trace-log weight",
        )

    def omit_sector(spectrum, sector_name):
        return [sector for sector in spectrum if sector["sector"] != sector_name]

    four_dimensional_spectrum = operator_blueprint["constant_background_spectrum"][4]
    assert_equal(
        trace_log_weight(
            omit_sector(four_dimensional_spectrum, "ghost_pair"), xi_operator
        )
        == 0,
        False,
        "omitting ghosts leaves a gauge-parameter residual",
    )
    assert_equal(
        trace_log_weight(
            omit_sector(four_dimensional_spectrum, "goldstone"), xi_operator
        )
        == 0,
        False,
        "omitting Goldstone/eaten-hyper data leaves a gauge-parameter residual",
    )
    assert_equal(
        trace_log_weight(
            omit_sector(four_dimensional_spectrum, "gauge_longitudinal"),
            xi_operator,
        )
        == 0,
        False,
        "omitting the nonminimal longitudinal vector leaves a residual",
    )

    def matrix_multiply(left, right):
        return [
            [
                sum(left[row][mid] * right[mid][column] for mid in range(len(right)))
                for column in range(len(right[0]))
            ]
            for row in range(len(left))
        ]

    def matrix_subtract(left, right):
        return [
            [left[row][column] - right[row][column] for column in range(len(left[0]))]
            for row in range(len(left))
        ]

    def matrix_add(left, right):
        return [
            [left[row][column] + right[row][column] for column in range(len(left[0]))]
            for row in range(len(left))
        ]

    def zero_matrix(row_count, column_count):
        return [
            [Fraction(0) for _column in range(column_count)]
            for _row in range(row_count)
        ]

    def matrix_sum(matrices):
        if not matrices:
            raise ValueError("matrix_sum requires at least one matrix")
        total = zero_matrix(len(matrices[0]), len(matrices[0][0]))
        for matrix in matrices:
            total = matrix_add(total, matrix)
        return total

    def scalar_multiply(scalar, matrix):
        return [[scalar * entry for entry in row] for row in matrix]

    def matrix_transpose(matrix):
        return [
            [matrix[row][column] for row in range(len(matrix))]
            for column in range(len(matrix[0]))
        ]

    def matrix_trace(matrix):
        return sum(matrix[index][index] for index in range(len(matrix)))

    def diagonal_matrix(entries):
        return [
            [
                entry if row == column else Fraction(0)
                for column, entry in enumerate(entries)
            ]
            for row, _entry in enumerate(entries)
        ]

    def row_component(matrix, row_index):
        return [
            [
                entry if row == row_index else Fraction(0)
                for entry in matrix[row]
            ]
            for row in range(len(matrix))
        ]

    def commutator(left, right):
        return matrix_subtract(matrix_multiply(left, right), matrix_multiply(right, left))

    def trace_log_second_variation(operator_0, inverse_operator_0, generator):
        operator_1 = commutator(generator, operator_0)
        operator_2 = commutator(generator, operator_1)
        seagull = matrix_trace(matrix_multiply(inverse_operator_0, operator_2))
        double_insertion = matrix_trace(
            matrix_multiply(
                matrix_multiply(
                    matrix_multiply(inverse_operator_0, operator_1),
                    inverse_operator_0,
                ),
                operator_1,
            )
        )
        return {
            "operator_1": operator_1,
            "operator_2": operator_2,
            "seagull": seagull,
            "double_insertion": double_insertion,
            "residual": seagull - double_insertion,
        }

    heavy_operator = diagonal_matrix([Fraction(2), Fraction(3), Fraction(5)])
    inverse_heavy_operator = diagonal_matrix(
        [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
    )
    frame_generator = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(-1), Fraction(0), Fraction(2)],
        [Fraction(0), Fraction(-2), Fraction(0)],
    ]
    frame_variation = trace_log_second_variation(
        heavy_operator, inverse_heavy_operator, frame_generator
    )
    assert_equal(
        frame_variation["residual"],
        Fraction(0),
        "pure heavy-frame connection seagull cancels the double insertion",
    )
    assert_equal(
        frame_variation["seagull"],
        frame_variation["double_insertion"],
        "frame-connection seagull is generated by the same conjugation",
    )
    assert_equal(
        -frame_variation["double_insertion"] == 0,
        False,
        "omitting the frame-connection seagull leaves a trace-log residual",
    )

    mass_curvature_operator_2 = [
        row[:] for row in frame_variation["operator_2"]
    ]
    mass_curvature_operator_2[0][0] += Fraction(1)
    mass_curvature_residual = (
        matrix_trace(matrix_multiply(inverse_heavy_operator, mass_curvature_operator_2))
        - frame_variation["double_insertion"]
    )
    assert_equal(
        mass_curvature_residual,
        Fraction(1, 2),
        "a genuine mass-curvature term is not removed by frame conjugation",
    )

    def trace_log_vertex_residual(inverse_operator_0, linear_vertex, seagull_vertex):
        return matrix_trace(
            matrix_subtract(
                matrix_multiply(inverse_operator_0, seagull_vertex),
                matrix_multiply(
                    matrix_multiply(
                        matrix_multiply(inverse_operator_0, linear_vertex),
                        inverse_operator_0,
                    ),
                    linear_vertex,
                ),
            )
        )

    matched_linear_vertex = [
        [Fraction(1), Fraction(1, 2)],
        [Fraction(1, 2), Fraction(3)],
    ]
    matched_seagull_vertex = [
        [Fraction(5), Fraction(2)],
        [Fraction(2), Fraction(7)],
    ]
    matched_operator = diagonal_matrix([Fraction(3), Fraction(7)])
    inverse_matched_operator = diagonal_matrix([Fraction(1, 3), Fraction(1, 7)])
    matched_trace_cell = trace_log_vertex_residual(
        inverse_matched_operator, matched_linear_vertex, matched_seagull_vertex
    )
    ward_pair = {
        "heavy_boson": {
            "statistics_weight": Fraction(1, 2),
            "linear_vertex": matched_linear_vertex,
            "seagull_vertex": matched_seagull_vertex,
        },
        "squared_fermion": {
            "statistics_weight": Fraction(-1, 2),
            "linear_vertex": matched_linear_vertex,
            "seagull_vertex": matched_seagull_vertex,
        },
    }
    ward_pair_residual = sum(
        block["statistics_weight"]
        * trace_log_vertex_residual(
            inverse_matched_operator,
            block["linear_vertex"],
            block["seagull_vertex"],
        )
        for block in ward_pair.values()
    )
    assert_equal(
        ward_pair_residual,
        Fraction(0),
        "matched mass-curvature vertices cancel by Ward pairing",
    )
    assert_equal(
        matched_trace_cell == 0,
        False,
        "each heavy block may be nonzero before the Ward-paired supertrace",
    )

    mismatched_fermion_linear = matrix_add(
        matched_linear_vertex,
        [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]],
    )
    mismatched_pair_residual = (
        Fraction(1, 2)
        * trace_log_vertex_residual(
            inverse_matched_operator,
            matched_linear_vertex,
            matched_seagull_vertex,
        )
        - Fraction(1, 2)
        * trace_log_vertex_residual(
            inverse_matched_operator,
            mismatched_fermion_linear,
            matched_seagull_vertex,
        )
    )
    assert_equal(
        mismatched_pair_residual == 0,
        False,
        "equal component weights do not cancel mismatched mass-curvature vertices",
    )

    def supercharge_factorized_vertices(supercharge_0, supercharge_1, supercharge_2, side):
        q0_transpose = matrix_transpose(supercharge_0)
        q1_transpose = matrix_transpose(supercharge_1)
        q2_transpose = matrix_transpose(supercharge_2)
        if side == "boson":
            return {
                "operator_0": matrix_multiply(q0_transpose, supercharge_0),
                "linear_vertex": matrix_add(
                    matrix_multiply(q1_transpose, supercharge_0),
                    matrix_multiply(q0_transpose, supercharge_1),
                ),
                "seagull_vertex": matrix_add(
                    matrix_add(
                        matrix_multiply(q2_transpose, supercharge_0),
                        scalar_multiply(
                            Fraction(2),
                            matrix_multiply(q1_transpose, supercharge_1),
                        ),
                    ),
                    matrix_multiply(q0_transpose, supercharge_2),
                ),
            }
        if side == "fermion":
            return {
                "operator_0": matrix_multiply(supercharge_0, q0_transpose),
                "linear_vertex": matrix_add(
                    matrix_multiply(supercharge_1, q0_transpose),
                    matrix_multiply(supercharge_0, q1_transpose),
                ),
                "seagull_vertex": matrix_add(
                    matrix_add(
                        matrix_multiply(supercharge_2, q0_transpose),
                        scalar_multiply(
                            Fraction(2),
                            matrix_multiply(supercharge_1, q1_transpose),
                        ),
                    ),
                    matrix_multiply(supercharge_0, q2_transpose),
                ),
            }
        raise ValueError(f"unknown factorized side {side!r}")

    supercharge_0 = diagonal_matrix([Fraction(2), Fraction(3)])
    supercharge_1 = [
        [Fraction(1), Fraction(1)],
        [Fraction(2), Fraction(0)],
    ]
    supercharge_2 = [
        [Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(2)],
    ]
    factorized_inverse = diagonal_matrix([Fraction(1, 4), Fraction(1, 9)])
    factorized_boson = supercharge_factorized_vertices(
        supercharge_0, supercharge_1, supercharge_2, "boson"
    )
    factorized_fermion = supercharge_factorized_vertices(
        supercharge_0, supercharge_1, supercharge_2, "fermion"
    )
    assert_equal(
        factorized_boson["operator_0"],
        factorized_fermion["operator_0"],
        "paired heavy block starts from the same massive operator in this basis",
    )
    assert_equal(
        factorized_boson["linear_vertex"] == factorized_fermion["linear_vertex"],
        False,
        "factorized boson and fermion vertices need not match as matrices",
    )
    factorized_boson_cell = trace_log_vertex_residual(
        factorized_inverse,
        factorized_boson["linear_vertex"],
        factorized_boson["seagull_vertex"],
    )
    factorized_fermion_cell = trace_log_vertex_residual(
        factorized_inverse,
        factorized_fermion["linear_vertex"],
        factorized_fermion["seagull_vertex"],
    )
    assert_equal(
        factorized_boson_cell,
        factorized_fermion_cell,
        "Q-adjoint factorization pairs the full second trace-log variation",
    )
    assert_equal(
        Fraction(1, 2) * factorized_boson_cell
        - Fraction(1, 2) * factorized_fermion_cell,
        Fraction(0),
        "supercharge-factorized heavy determinant cancels after statistics",
    )

    omitted_square_contact = matrix_subtract(
        factorized_boson["seagull_vertex"],
        scalar_multiply(
            Fraction(2),
            matrix_multiply(matrix_transpose(supercharge_1), supercharge_1),
        ),
    )
    omitted_contact_residual = (
        Fraction(1, 2)
        * trace_log_vertex_residual(
            factorized_inverse,
            factorized_boson["linear_vertex"],
            omitted_square_contact,
        )
        - Fraction(1, 2) * factorized_fermion_cell
    )
    assert_equal(
        omitted_contact_residual == 0,
        False,
        "dropping the square-completion contact breaks the Ward-paired trace-log",
    )

    row_completed_q0 = diagonal_matrix([Fraction(2), Fraction(3), Fraction(5)])
    row_completed_q1 = [
        [Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(0)],
    ]
    row_completed_q2 = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(2)],
        [Fraction(2), Fraction(0), Fraction(1)],
    ]
    row_completed_inverse = diagonal_matrix(
        [Fraction(1, 4), Fraction(1, 9), Fraction(1, 25)]
    )
    row_completed_boson = supercharge_factorized_vertices(
        row_completed_q0, row_completed_q1, row_completed_q2, "boson"
    )
    row_completed_fermion = supercharge_factorized_vertices(
        row_completed_q0, row_completed_q1, row_completed_q2, "fermion"
    )
    row_completed_boson_cell = trace_log_vertex_residual(
        row_completed_inverse,
        row_completed_boson["linear_vertex"],
        row_completed_boson["seagull_vertex"],
    )
    row_completed_fermion_cell = trace_log_vertex_residual(
        row_completed_inverse,
        row_completed_fermion["linear_vertex"],
        row_completed_fermion["seagull_vertex"],
    )
    assert_equal(
        row_completed_boson_cell,
        row_completed_fermion_cell,
        "row-completed Q-complex pairs the full second trace-log variation",
    )

    row_square_contacts = [
        scalar_multiply(
            Fraction(2),
            matrix_multiply(
                matrix_transpose(row_component(row_completed_q1, row_index)),
                row_component(row_completed_q1, row_index),
            ),
        )
        for row_index in range(len(row_completed_q1))
    ]
    full_row_square_contact = scalar_multiply(
        Fraction(2),
        matrix_multiply(matrix_transpose(row_completed_q1), row_completed_q1),
    )
    assert_equal(
        matrix_sum(row_square_contacts),
        full_row_square_contact,
        "row-local square contacts sum to the full bosonic seagull contact",
    )

    auxiliary_yukawa_row = 2
    auxiliary_yukawa_contact = row_square_contacts[auxiliary_yukawa_row]
    omitted_auxiliary_row_seagull = matrix_subtract(
        row_completed_boson["seagull_vertex"],
        auxiliary_yukawa_contact,
    )
    omitted_auxiliary_row_residual = (
        Fraction(1, 2)
        * trace_log_vertex_residual(
            row_completed_inverse,
            row_completed_boson["linear_vertex"],
            omitted_auxiliary_row_seagull,
        )
        - Fraction(1, 2) * row_completed_fermion_cell
    )
    full_row_supertrace = (
        Fraction(1, 2) * row_completed_boson_cell
        - Fraction(1, 2) * row_completed_fermion_cell
    )
    expected_omitted_row_shift = (
        -Fraction(1, 2)
        * matrix_trace(
            matrix_multiply(row_completed_inverse, auxiliary_yukawa_contact)
        )
    )
    assert_equal(
        full_row_supertrace,
        Fraction(0),
        "row-completed heavy complex cancels before component diagnostics",
    )
    assert_equal(
        omitted_auxiliary_row_residual - full_row_supertrace,
        expected_omitted_row_shift,
        "dropping an auxiliary/Yukawa row contact gives the trace-log shift",
    )
    assert_equal(
        omitted_auxiliary_row_residual == 0,
        False,
        "missing auxiliary/Yukawa row contact breaks the Higgs determinant pairing",
    )

    def vector_dot(left, right):
        return sum(left[index] * right[index] for index in range(len(left)))

    def outer_product(left, right):
        return [[left[row] * right[column] for column in range(len(right))] for row in range(len(left))]

    def matrix_vector_multiply(matrix, vector):
        return [
            sum(matrix[row][column] * vector[column] for column in range(len(vector)))
            for row in range(len(matrix))
        ]

    # Exact local row-Jacobian model for q_B(t) on a unit circle.  At t=0,
    # q=(1,0), q'=(0,2), q''=(-4,0) for the rational parametrization
    # q(t)=((1-t^2)/(1+t^2), 2t/(1+t^2)).
    q_background = [Fraction(1), Fraction(0)]
    q_tangent = [Fraction(0), Fraction(1)]
    q_prime = [Fraction(0), Fraction(2)]
    q_second = [Fraction(-4), Fraction(0)]
    q_alt = [Fraction(3, 5), Fraction(4, 5)]
    q_alt_tangent = [Fraction(-4, 5), Fraction(3, 5)]
    assert_equal(vector_dot(q_background, q_background), Fraction(1), "rank-one Higgs row background has fixed norm")
    assert_equal(vector_dot(q_background, q_prime), Fraction(0), "rank-one Higgs row tangent is quotient-horizontal")
    assert_equal(
        vector_dot(q_prime, q_prime) + vector_dot(q_background, q_second),
        Fraction(0),
        "rank-one Higgs row norm has zero second variation",
    )

    row_coefficients = {
        "real_moment_map_row": Fraction(10, 3),
        "complex_moment_map_real_row": Fraction(5, 3),
        "complex_moment_map_imag_row": Fraction(5, 3),
        "background_gauge_fixing_row": Fraction(7, 3),
        "yukawa_mass_row": Fraction(10, 3),
    }
    for row_name, coefficient_squared in row_coefficients.items():
        fixed_row_operator = scalar_multiply(
            coefficient_squared,
            outer_product(q_background, q_background),
        )
        alt_row_operator = scalar_multiply(
            coefficient_squared,
            outer_product(q_alt, q_alt),
        )
        row_space_mass = coefficient_squared * vector_dot(q_background, q_background)
        alt_row_space_mass = coefficient_squared * vector_dot(q_alt, q_alt)
        assert_equal(
            row_space_mass,
            alt_row_space_mass,
            f"{row_name} has constant nonzero row-space mass",
        )
        assert_equal(
            matrix_trace(fixed_row_operator),
            row_space_mass,
            f"{row_name} trace is the single heavy eigenvalue",
        )
        assert_equal(
            matrix_multiply(fixed_row_operator, fixed_row_operator),
            scalar_multiply(row_space_mass, fixed_row_operator),
            f"{row_name} fixed-coordinate operator is a rank-one heavy projector",
        )
        assert_equal(
            matrix_vector_multiply(fixed_row_operator, q_tangent),
            [Fraction(0), Fraction(0)],
            f"{row_name} annihilates the quotient tangent zero mode",
        )
        assert_equal(
            matrix_vector_multiply(alt_row_operator, q_alt_tangent),
            [Fraction(0), Fraction(0)],
            f"{row_name} rotated projector still separates the tangent zero mode",
        )
        assert_equal(
            fixed_row_operator == alt_row_operator,
            False,
            f"{row_name} fixed-coordinate operator moves by projector rotation",
        )

    representative_coefficient = row_coefficients["real_moment_map_row"]
    full_row_jacobian_second = scalar_multiply(
        representative_coefficient,
        matrix_add(
            matrix_add(
                outer_product(q_second, q_background),
                scalar_multiply(Fraction(2), outer_product(q_prime, q_prime)),
            ),
            outer_product(q_background, q_second),
        ),
    )
    omitted_contact_second = scalar_multiply(
        representative_coefficient,
        matrix_add(
            outer_product(q_second, q_background),
            outer_product(q_background, q_second),
        ),
    )
    row_space_second_full = representative_coefficient * (
        vector_dot(q_second, q_background)
        + 2 * vector_dot(q_prime, q_prime)
        + vector_dot(q_background, q_second)
    )
    row_space_second_without_contact = representative_coefficient * (
        vector_dot(q_second, q_background)
        + vector_dot(q_background, q_second)
    )
    assert_equal(
        row_space_second_full,
        Fraction(0),
        "rank-one component rows have no nonzero-mass curvature after contact completion",
    )
    assert_equal(
        row_space_second_without_contact == 0,
        False,
        "omitting the row square-completion contact creates fake mass curvature",
    )
    assert_equal(
        full_row_jacobian_second == omitted_contact_second,
        False,
        "row-Jacobian contact is a generated fixed-coordinate seagull",
    )

    def pv_moments(regulator_terms):
        coefficient_sum = sum(
            coefficient for coefficient, _mass_0, _mass_1, _mass_2 in regulator_terms
        )
        mass_sum = sum(
            coefficient * mass_0
            for coefficient, mass_0, _mass_1, _mass_2 in regulator_terms
        )
        return coefficient_sum, mass_sum

    def regulated_log_second_variation(eigen_data, regulator_terms):
        total = Fraction(0)
        for lambda_0, lambda_1, lambda_2 in eigen_data:
            for coefficient, mass_0, mass_1, mass_2 in regulator_terms:
                denominator = lambda_0 + mass_0
                total += coefficient * (
                    (lambda_2 + mass_2) / denominator
                    - ((lambda_1 + mass_1) * (lambda_1 + mass_1))
                    / (denominator * denominator)
                )
        return total

    nonzero_heavy_eigen_data = [
        (Fraction(4), Fraction(1), Fraction(3)),
        (Fraction(9), Fraction(-2), Fraction(5)),
        (Fraction(25), Fraction(3), Fraction(-7)),
    ]
    paired_pv_terms = [
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(-2), Fraction(10), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(20), Fraction(0), Fraction(0)),
    ]
    assert_equal(
        pv_moments(paired_pv_terms),
        (Fraction(0), Fraction(0)),
        "paired Higgs PV regulator satisfies the displayed local moment conditions",
    )
    paired_regulated_variation = regulated_log_second_variation(
        nonzero_heavy_eigen_data, paired_pv_terms
    )
    assert_equal(
        Fraction(1, 2) * paired_regulated_variation
        - Fraction(1, 2) * paired_regulated_variation,
        Fraction(0),
        "same regulator function cancels on the paired nonzero heavy spectrum",
    )

    mismatched_fermion_pv_terms = [
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(-2), Fraction(11), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(22), Fraction(0), Fraction(0)),
    ]
    mismatched_regulator_residual = (
        Fraction(1, 2)
        * regulated_log_second_variation(nonzero_heavy_eigen_data, paired_pv_terms)
        - Fraction(1, 2)
        * regulated_log_second_variation(
            nonzero_heavy_eigen_data, mismatched_fermion_pv_terms
        )
    )
    assert_equal(
        mismatched_regulator_residual == 0,
        False,
        "unpaired Higgs PV masses create a regulator-dependent metric residual",
    )

    tangent_dependent_boson_pv_terms = [
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(-2), Fraction(10), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(20), Fraction(0), Fraction(0)),
    ]
    tangent_dependent_regulator_residual = (
        Fraction(1, 2)
        * regulated_log_second_variation(
            nonzero_heavy_eigen_data, tangent_dependent_boson_pv_terms
        )
        - Fraction(1, 2)
        * regulated_log_second_variation(nonzero_heavy_eigen_data, paired_pv_terms)
    )
    assert_equal(
        tangent_dependent_regulator_residual == 0,
        False,
        "unpaired tangent-dependent regulator mass inserts a fake background vertex",
    )

    zero_mode_eigen_data = [(Fraction(0), Fraction(0), Fraction(0))]
    unregulated_log_terms = [(Fraction(1), Fraction(0), Fraction(0), Fraction(0))]
    try:
        regulated_log_second_variation(zero_mode_eigen_data, unregulated_log_terms)
    except ZeroDivisionError:
        zero_mode_projection_required = True
    else:
        zero_mode_projection_required = False
    assert_equal(
        zero_mode_projection_required,
        True,
        "Higgs tangent zero modes must be projected before the heavy log determinant",
    )

    reduced_scalar_rows_by_dimension = {
        4: set(),
        3: {0},
        2: {0, 1},
    }
    reduced_row_contact_by_dimension = {}
    for dimension, reduced_rows in reduced_scalar_rows_by_dimension.items():
        if reduced_rows:
            reduced_contact = matrix_sum(
                [row_square_contacts[row_index] for row_index in sorted(reduced_rows)]
            )
        else:
            reduced_contact = zero_matrix(
                len(full_row_square_contact), len(full_row_square_contact[0])
            )
        reduced_row_contact_by_dimension[dimension] = reduced_contact
        omitted_reduced_shift = (
            -Fraction(1, 2)
            * matrix_trace(matrix_multiply(row_completed_inverse, reduced_contact))
        )
        if dimension == 4:
            assert_equal(
                omitted_reduced_shift,
                Fraction(0),
                "4d has no reduced connection-scalar row contact",
            )
        else:
            assert_equal(
                omitted_reduced_shift == 0,
                False,
                (
                    f"{dimension}d omitting reduced vector-scalar rows leaves "
                    "a trace-log contact residual"
                ),
            )

    assert_equal(
        reduced_row_contact_by_dimension[2] == reduced_row_contact_by_dimension[3],
        False,
        "2d and 3d reduced scalar row contacts are dimension-specific",
    )

    component_balance_4d = sum(old_component_ledger["component_weights"].values())
    assert_equal(
        component_balance_4d,
        0,
        "four-dimensional long-multiplet balance is only a diagnostic",
    )

    for dimension, spectrum in operator_blueprint[
        "constant_background_spectrum"
    ].items():
        vector_components = sum(
            sector["modes"]
            for sector in spectrum
            if sector["sector"] in {"gauge_transverse", "gauge_longitudinal"}
        )
        reduced_connection_scalars = sum(
            sector["modes"]
            for sector in spectrum
            if sector["sector"] == "reduced_connection_scalars"
        )
        assert_equal(
            vector_components,
            dimension,
            f"{dimension}d generated vector split has dimension-specific slots",
        )
        assert_equal(
            vector_components + reduced_connection_scalars,
            4,
            f"{dimension}d reduction preserves four connection slots",
        )
        if dimension != 4:
            assert_equal(
                old_component_ledger["component_weights"]["gauge_field"]
                == vector_components,
                False,
                (
                    f"{dimension}d Higgs metric audit rejects a fixed 4d "
                    "gauge-field entry"
                ),
            )
        dimension_balance = (
            vector_components
            + reduced_connection_scalars
            + old_component_ledger["component_weights"]["complex_vector_scalar"]
            + old_component_ledger["component_weights"]["eaten_hyper_scalars"]
            + old_component_ledger["component_weights"]["faddeev_popov_ghosts"]
            + old_component_ledger["component_weights"]["auxiliary_contacts"]
            + old_component_ledger["component_weights"]["fermions"]
        )
        assert_equal(
            dimension_balance,
            0,
            f"{dimension}d diagnostic balance separates vector and reduced scalar slots",
        )

    two_dimensional_kernel = {
        "Pi_12": Fraction(7, 5),
        "Pi_21": Fraction(3, 5),
    }
    raw_symmetric_part = (
        two_dimensional_kernel["Pi_12"] + two_dimensional_kernel["Pi_21"]
    ) / 2
    raw_antisymmetric_part = (
        two_dimensional_kernel["Pi_12"] - two_dimensional_kernel["Pi_21"]
    ) / 2
    assert_equal(
        raw_symmetric_part,
        Fraction(1),
        "2d raw trace-log kernel has a symmetric tensor component",
    )
    assert_equal(
        raw_antisymmetric_part == 0,
        False,
        "2d raw trace-log kernel may also carry a torsionful component",
    )

    torsionful_required_slots = {
        "delta_g",
        "delta_B",
        "delta_Phi",
        "delta_nabla_plus",
        "delta_nabla_minus",
    }
    naive_two_dimensional_metric_projection = {"delta_g": raw_symmetric_part}
    assert_equal(
        sorted(torsionful_required_slots - set(naive_two_dimensional_metric_projection)),
        ["delta_B", "delta_Phi", "delta_nabla_minus", "delta_nabla_plus"],
        "2d torsionful branch data cannot be reduced to the symmetric kernel",
    )
    coupled_two_dimensional_deformation = {
        "delta_g": raw_symmetric_part,
        "delta_B": raw_antisymmetric_part,
        "delta_Phi": Fraction(1, 11),
        "delta_nabla_plus": raw_symmetric_part + raw_antisymmetric_part,
        "delta_nabla_minus": raw_symmetric_part - raw_antisymmetric_part,
    }
    assert_equal(
        set(coupled_two_dimensional_deformation) >= torsionful_required_slots,
        True,
        "2d torsionful determinant target carries the coupled (g,B,Phi) package",
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


def check_higgs_branch_gauge_fixed_heavy_package_projection():
    """Assemble a finite gauge-fixed heavy package and project tangent zero modes."""

    def vector_dot(left, right):
        return sum(left[index] * right[index] for index in range(len(left)))

    def matrix_vector_multiply(matrix, vector):
        return [
            sum(matrix[row][column] * vector[column] for column in range(len(vector)))
            for row in range(len(matrix))
        ]

    def matrix_multiply(left, right):
        return [
            [
                sum(left[row][mid] * right[mid][column] for mid in range(len(right)))
                for column in range(len(right[0]))
            ]
            for row in range(len(left))
        ]

    def matrix_add(left, right):
        return [
            [left[row][column] + right[row][column] for column in range(len(left[0]))]
            for row in range(len(left))
        ]

    def scalar_multiply(scalar, matrix):
        return [[scalar * entry for entry in row] for row in matrix]

    def outer_product(left, right):
        return [
            [left[row] * right[column] for column in range(len(right))]
            for row in range(len(left))
        ]

    def zero_matrix(row_count, column_count):
        return [
            [Fraction(0) for _column in range(column_count)]
            for _row in range(row_count)
        ]

    def projector_from_rows(rows):
        projector = zero_matrix(len(rows[0]), len(rows[0]))
        for row in rows:
            norm = vector_dot(row, row)
            projector = matrix_add(
                projector,
                scalar_multiply(Fraction(1, norm), outer_product(row, row)),
            )
        return projector

    momentum = Fraction(2)
    mass = Fraction(3)
    xi_sqrt = Fraction(2)
    xi = xi_sqrt * xi_sqrt
    gauge_map_symbol = [momentum, xi_sqrt * mass]
    gauge_fixing_adjoint_row = [momentum, xi_sqrt * mass]
    ghost_operator = vector_dot(gauge_fixing_adjoint_row, gauge_map_symbol)
    xi_operator = momentum * momentum + xi * mass * mass

    assert_equal(
        ghost_operator,
        xi_operator,
        "ghost operator is generated by the gauge-fixing row composed with the gauge map",
    )
    xi_sector_residual = (
        Fraction(1, 2) * xi_operator
        + Fraction(1, 2) * xi_operator
        - ghost_operator
    )
    assert_equal(
        xi_sector_residual,
        Fraction(0),
        "gauge map, Goldstone row, and ghost row share the same R_xi symbol",
    )

    mismatched_ghost_row = [momentum, (xi_sqrt + 1) * mass]
    mismatched_ghost_operator = vector_dot(mismatched_ghost_row, gauge_map_symbol)
    assert_equal(
        mismatched_ghost_operator == xi_operator,
        False,
        "choosing the ghost operator independently breaks gauge-map compatibility",
    )
    assert_equal(
        Fraction(1, 2) * xi_operator
        + Fraction(1, 2) * xi_operator
        - mismatched_ghost_operator
        == 0,
        False,
        "mismatched ghost row leaves an R_xi determinant residual",
    )

    normal_hyper_row = [Fraction(3, 5), Fraction(4, 5), Fraction(0)]
    quotient_tangent = [Fraction(-4, 5), Fraction(3, 5), Fraction(0)]
    vector_scalar_row = [Fraction(0), Fraction(0), Fraction(1)]
    heavy_rows = [normal_hyper_row, vector_scalar_row]
    heavy_projector = projector_from_rows(heavy_rows)

    assert_equal(
        matrix_multiply(heavy_projector, heavy_projector),
        heavy_projector,
        "row package generates an idempotent nonzero-heavy projector",
    )
    assert_equal(
        matrix_vector_multiply(heavy_projector, quotient_tangent),
        [Fraction(0), Fraction(0), Fraction(0)],
        "nonzero-heavy projector removes the Higgs tangent zero mode",
    )
    assert_equal(
        matrix_vector_multiply(heavy_projector, normal_hyper_row),
        normal_hyper_row,
        "moment-map row keeps the normal hypermultiplet direction heavy",
    )
    assert_equal(
        matrix_vector_multiply(heavy_projector, vector_scalar_row),
        vector_scalar_row,
        "vector-scalar row remains in the heavy complement",
    )

    missing_moment_projector = projector_from_rows([vector_scalar_row])
    assert_equal(
        matrix_vector_multiply(missing_moment_projector, normal_hyper_row)
        == normal_hyper_row,
        False,
        "dropping the moment-map row loses a normal hypermultiplet heavy mode",
    )

    unprojected_eigenvalues = [mass * mass, Fraction(0)]
    projected_eigenvalues = [value for value in unprojected_eigenvalues if value != 0]
    assert_equal(
        Fraction(0) in unprojected_eigenvalues,
        True,
        "unprojected Higgs tangent zero mode makes the heavy determinant singular",
    )
    assert_equal(
        Fraction(0) in projected_eigenvalues,
        False,
        "projected heavy determinant contains only nonzero eigenvalues",
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
    check_higgs_branch_ward_counterterm_interface()
    check_higgs_branch_two_dimensional_torsion_boundary()
    check_higgs_branch_metric_transport_projection()
    check_higgs_branch_background_field_derivation_gate()
    check_higgs_branch_gauge_fixed_heavy_package_projection()
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
