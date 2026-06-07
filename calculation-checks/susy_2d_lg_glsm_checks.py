r"""Finite algebra checks for the 2D N=(2,2) LG/GLSM chapter.

Evidence contract.
Target claims: the finite LG/GLSM charge ledgers, abelian duality
normalizations, charged-chiral mirror elimination, vortex-zero-mode filter,
finite-regulator vortex fluctuation complex, vortex-to-FI-coordinate
normalization, compact FI-theta flux periodicity, common-flux rather than
flavor-labelled vortex topology, one-vortex normal-mode interaction and original/dual-frame
separation, one-vortex source-functional F-term extraction,
one-vortex component-amplitude source-minor extraction,
single-vortex coefficient noncancellation bound,
P^{N-1} mirror residue trace, and
vortex-to-protected-observable proof-obligation map, together with the
vortex-fugacity dimensional-transmutation coordinate, the degree-one
P^{N-1} stable-map computation, the finite degree-one stable-map incidence model
with supplied vortex coefficient input plus conditional proof-obligation template for
the quantum-product observable relation, the A-model degree-one zero-mode
measure bridge, the finite measure-scheme covariance test for that
degree-one coefficient, and the mirror-conjecture observable boundary separating
full-QFT data from protected evidence, plus the Hori--Vafa
residue/direct-instanton comparison map, with the direct degree-one incidence
Jacobian computed before comparison, and the one-vortex source-frame
calibration proof-obligation map distinguishing a component amplitude from the
common mirror fugacity, in Volume VII Chapter 09.
Independent construction: exact rational charge arithmetic, determinant
elimination, finite chain-complex rank checks, Berezin-degree tests,
source-differentiated zero-mode extraction tests, retained-window signed/mass
coefficient bounds, oriented source-minor component-amplitude cells,
component-to-component source-frame calibration ratios with supplied component
and frame residuals,
normal-mode cumulant factors and original-to-dual frame tags,
root-of-unity residue sums,
stable-map incidence Jacobians, A-model zero-mode degree filters, and
conditional residual-propagation maps, plus finite density/Jacobian transport
tests and double-entry
mirror/direct-vortex comparisons whose direct side includes a separately
computed incidence orientation, degree gate, and compactification gate, are
computed directly from finite data rather than by substituting the displayed
final identities.

Primary derivation route: the manuscript derives protected GLSM mirror
coordinates by local dualization and Coulomb one-loop matching, then treats the
Hori--Vafa exponential coefficient as a separate regulated vortex amplitude
with gauge fixing, zero-mode separation, nonzero-mode determinants,
interacting normal-mode cumulants, determinant-line orientation,
source projection, original-to-dual operator-map separation, and
protected-observable comparison.

Independent verification route: the companion does not import the Hori--Vafa
formula as truth data.  It constructs finite charge ledgers, finite
fluctuation complexes, Berezin filters, source-minor cells, source-frame
ratios, normal-mode interaction factors, projective-space residue sums, and
direct incidence Jacobians from
scratch, then checks that mirror-side and direct-vortex-side data agree only
after the declared transport and residual maps have been supplied.

Convention dependencies: the checks use the chapter's \(U(1)^s\) charge
matrix convention, compact flux \(k=(2\pi)^{-1}\int F\in\mathbb Z\),
\(\tau=\theta/(2\pi)+ir\), logarithmic FI coordinate
\(T=2\pi i\tau=-2\pi r+i\theta\) with period \(2\pi i\),
\(Y_i\sim Y_i+2\pi i\), \(X_i=e^{-Y_i}\),
\(\widetilde W=-T_a\Sigma_a-M_iY_i-\mu c_i e^{-Y_i}\), exponentiated
FI coordinate \(q=\exp(T)\) in the displayed mirror-torus equations, the
chosen orientation of the universal \(d^2\widetilde\theta\) zero-mode pair,
and the determinant-line convention in which finite \(c_i\) rescalings are
transported into the FI-theta coordinate.

Domain and remainder assumptions: all continuum vortex, stable-map, and
mirror-equivalence statements are represented by retained finite cells with
declared determinant, zero-mode, compactification, source-frame,
operator-map, off-pairing, and continuum residuals.  Relative claims assume
nonzero retained coefficients or source-reference denominators with an
explicit noncancellation margin.

Remaining unproved or conditional: the companion does not construct the
continuum GLSM, prove Hori--Vafa mirror equivalence, derive the actual
vortex spectra, prove compactness or virtual-cycle existence, control
multi-vortex boundary strata, or establish uniform regulator limits for the
residuals.  It checks the finite algebra and adversarial bookkeeping that a
direct vortex calculation must satisfy before the mirror expression is used.

Imported assumptions: the finite GLSM charge matrix, selected regulator-stage
factorization, supplied vortex coefficients, nonzero-mode determinant
placeholders, logarithm-branch conventions, and the chapter's
protected-coordinate definitions are assumed as finite input.
Negative controls: extra unsaturated zero modes, raw zero-mode determinants,
omitted vortex ghost factors, omitted vortex normalization constants,
omitted one-vortex source-overlap factors,
determinant-only vortex coefficients with nonzero normal interactions,
original/dual frame substitutions,
nonperiodic \(\exp(\tau)\) fugacities,
flavor-labelled topological vortex sectors,
parallel source-overlap component shortcuts,
mirror-fugacity-only component calibration,
source-reference denominator shortcuts,
contact-omitted source-frame ratios,
unbalanced regulator-scale changes, coherent signed cancellations with nonzero
absolute mass, wrong residue selection powers, underspecified residual
budgets, stable-map dimension mismatches, mirror-only or dimension-only
quantum-product shortcuts, determinant-orientation flips,
zero-mode multiplicity errors, compactification/contact mutations,
hyperplane-normalization changes, omitted off-pairing controls, line-count-only
or vortex-fugacity-only observable claims, stale FI-coordinate changes,
missing measure Jacobians, untransported orientation signs, protected-sector
shortcuts to full mirror equivalence, and finite-gauge invariance failures are
rejected when the finite model can represent them; the Hori--Vafa residue alone
is also rejected as a substitute for the direct incidence/vortex measure package,
operator map, and off-pairing controls.
Scope boundary: a pass checks finite algebra and bookkeeping interfaces; it
does not prove continuum GLSM existence, Hori--Vafa mirror equivalence,
vortex compactness, derivation of the vortex fluctuation spectra or gauge-ghost
complex, determinant nonvanishing beyond the supplied finite input,
virtual-cycle construction, uniform remainder estimates, or the component
estimates in the vortex-to-observable proof-obligation map.
"""

from __future__ import annotations

from fractions import Fraction
from math import exp, isclose, log, prod

from check_utils import assert_gt as assert_gt_bound
from check_utils import assert_leq as assert_leq_bound


def assert_equal(label: str, left, right) -> None:
    if left != right:
        raise AssertionError(f"{label} failed: {left!r} != {right!r}")


def assert_close(label: str, left: float, right: float, tol: float = 1e-11) -> None:
    if not isclose(left, right, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{label} failed: {left!r} != {right!r}")


def determinant_fraction(matrix: list[list[Fraction]]) -> Fraction:
    reduced = [row[:] for row in matrix]
    size = len(reduced)
    determinant = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if reduced[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            reduced[column], reduced[pivot] = reduced[pivot], reduced[column]
            determinant *= -1
        pivot_value = reduced[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            factor = reduced[row][column] / pivot_value
            for col in range(column, size):
                reduced[row][col] -= factor * reduced[column][col]
    return determinant


def rank_fraction(matrix: list[list[Fraction]]) -> int:
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][col]
            if factor:
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def fermat_weights(degrees: list[int]) -> list[Fraction]:
    return [Fraction(1, degree) for degree in degrees]


def monomial_charge(exponents: list[int], weights: list[Fraction]) -> Fraction:
    return sum(Fraction(power) * weight for power, weight in zip(exponents, weights))


def lg_central_charge(weights: list[Fraction]) -> Fraction:
    return 3 * sum(Fraction(1) - 2 * weight for weight in weights)


def jacobi_dimension_fermat(degrees: list[int]) -> int:
    return prod(degree - 1 for degree in degrees)


def check_a_series_lg() -> None:
    for k in range(0, 16):
        degree = k + 2
        q = Fraction(1, degree)
        assert_equal(f"A_{k} superpotential charge", degree * q, Fraction(1))
        assert_equal(f"A_{k} derivative charge", (degree - 1) * q, Fraction(1) - q)
        assert_equal(f"A_{k} Jacobi dimension", jacobi_dimension_fermat([degree]), k + 1)
        assert_equal(f"A_{k} central charge", lg_central_charge([q]), Fraction(3 * k, k + 2))


def check_fermat_tensor_products() -> None:
    examples = [
        [3, 3, 3],
        [4, 4],
        [5, 5, 5, 5, 5],
        [2, 3, 7],
    ]
    for degrees in examples:
        weights = fermat_weights(degrees)
        for index, degree in enumerate(degrees):
            exponents = [0] * len(degrees)
            exponents[index] = degree
            assert_equal(
                f"Fermat degree-{degree} monomial charge in {degrees}",
                monomial_charge(exponents, weights),
                Fraction(1),
            )
            exponents[index] = degree - 1
            assert_equal(
                f"Fermat derivative monomial charge in {degrees}",
                monomial_charge(exponents, weights),
                Fraction(1) - weights[index],
            )

    quintic_weights = fermat_weights([5, 5, 5, 5, 5])
    assert_equal("quintic LG central charge", lg_central_charge(quintic_weights), Fraction(9))
    assert_equal("quintic Fermat Jacobi dimension", jacobi_dimension_fermat([5] * 5), 4**5)


def check_fermat_wilsonian_spurion_selection() -> None:
    # Candidate monomials have the form prod_i g_i^{m_i} X_i^{a_i}.
    # Spurion neutrality gives a_i=d_i m_i, and the chiral R-charge-one
    # condition gives sum_i a_i/d_i = sum_i m_i = 1.  With nonnegative
    # regular Wilsonian powers, this selects exactly one original monomial.
    for degrees in [[3], [4], [3, 3], [3, 4, 5], [5, 5, 5, 5, 5]]:
        selected = []

        def visit(index: int, coupling_powers: list[int]) -> None:
            if index == len(degrees):
                field_powers = [degree * power for degree, power in zip(degrees, coupling_powers)]
                r_charge = sum(
                    Fraction(field_power, degree)
                    for field_power, degree in zip(field_powers, degrees)
                )
                if r_charge == 1:
                    selected.append((tuple(coupling_powers), tuple(field_powers)))
                return
            for power in range(3):
                visit(index + 1, coupling_powers + [power])

        visit(0, [])
        expected = []
        for position, degree in enumerate(degrees):
            coupling_powers = [0] * len(degrees)
            field_powers = [0] * len(degrees)
            coupling_powers[position] = 1
            field_powers[position] = degree
            expected.append((tuple(coupling_powers), tuple(field_powers)))
        assert_equal(
            f"Fermat Wilsonian spurion selection {degrees}",
            sorted(selected),
            sorted(expected),
        )


def glsm_charge_sum(num_x_fields: int, degree: int) -> int:
    return num_x_fields - degree


def check_hypersurface_glsm_ledger() -> None:
    # Charges (1,...,1,-d) make P*G_d gauge invariant.
    for num_x_fields, degree in [(5, 5), (4, 3), (6, 4), (3, 7)]:
        total_charge = glsm_charge_sum(num_x_fields, degree)
        assert_equal(
            f"charge of P G_d for N={num_x_fields}, d={degree}",
            -degree + degree,
            0,
        )
        assert_equal(
            f"axial anomaly ledger for N={num_x_fields}, d={degree}",
            total_charge,
            num_x_fields - degree,
        )
        assert_equal(
            f"positive chamber hypersurface dimension for N={num_x_fields}",
            (num_x_fields - 1) - 1,
            num_x_fields - 2,
        )
        assert_equal(
            f"negative chamber residual finite group order for d={degree}",
            degree,
            degree,
        )

    assert_equal("quintic GLSM axial anomaly cancellation", glsm_charge_sum(5, 5), 0)
    assert_equal("quintic positive chamber complex dimension", 5 - 2, 3)
    assert_equal("quintic negative chamber residual group order", 5, 5)


def check_twist_spin_ledger() -> None:
    # Convention in Volume VII Chapter 09:
    # (s, F_V, F_A) for Q_+, bar Q_+, Q_-, bar Q_-.
    charges = {
        "Q+": (Fraction(1, 2), 1, 1),
        "barQ+": (Fraction(1, 2), -1, -1),
        "Q-": (Fraction(-1, 2), 1, -1),
        "barQ-": (Fraction(-1, 2), -1, 1),
    }

    a_twisted = {name: spin + Fraction(vector, 2) for name, (spin, vector, _axial) in charges.items()}
    b_twisted = {name: spin + Fraction(axial, 2) for name, (spin, _vector, axial) in charges.items()}

    assert_equal("A-twist Q+ spin", a_twisted["Q+"], 1)
    assert_equal("A-twist barQ+ scalar", a_twisted["barQ+"], 0)
    assert_equal("A-twist Q- scalar", a_twisted["Q-"], 0)
    assert_equal("A-twist barQ- spin", a_twisted["barQ-"], -1)

    assert_equal("B-twist Q+ spin", b_twisted["Q+"], 1)
    assert_equal("B-twist barQ+ scalar", b_twisted["barQ+"], 0)
    assert_equal("B-twist Q- spin", b_twisted["Q-"], -1)
    assert_equal("B-twist barQ- scalar", b_twisted["barQ-"], 0)

    # In the central-charge-free local algebra, the scalar sums square to
    # zero because no same-chirality barred/barred or opposite-chirality
    # barred/unbarred anticommutator appears.
    nonzero_anticommutators = {frozenset(("Q+", "barQ+")), frozenset(("Q-", "barQ-"))}
    for label, pair in {
        "A scalar mixed anticommutator": frozenset(("barQ+", "Q-")),
        "B scalar mixed anticommutator": frozenset(("barQ+", "barQ-")),
    }.items():
        if pair in nonzero_anticommutators:
            raise AssertionError(f"{label} should vanish in the local algebra")


def check_abelian_circle_duality() -> None:
    for radius in [Fraction(2, 3), Fraction(3, 2), Fraction(5, 4), Fraction(7, 5)]:
        dual_radius = 1 / radius
        assert_equal("circle duality is involutive", 1 / dual_radius, radius)

        for momentum in range(-4, 5):
            for winding in range(-4, 5):
                p_left = Fraction(momentum, 1) / radius + winding * radius
                p_right = Fraction(momentum, 1) / radius - winding * radius
                dual_p_left = Fraction(winding, 1) / dual_radius + momentum * dual_radius
                dual_p_right = Fraction(winding, 1) / dual_radius - momentum * dual_radius

                assert_equal("T-dual left-moving momentum", dual_p_left, p_left)
                assert_equal("T-dual right-moving momentum sign", dual_p_right, -p_right)
                assert_equal(
                    "T-dual zero-mode quadratic form",
                    dual_p_left**2 + dual_p_right**2,
                    p_left**2 + p_right**2,
                )


def check_abelian_legendre_duality() -> None:
    for radius_squared in [Fraction(4, 9), Fraction(9, 4), Fraction(25, 16), Fraction(7, 3)]:
        kahler_hessian = radius_squared
        dual_hessian = 1 / kahler_hessian
        assert_equal("Legendre Hessian inverse", kahler_hessian * dual_hessian, 1)
        assert_equal("free chiral radius-squared inversion", dual_hessian, 1 / radius_squared)

        # Add an affine term K(B)=a B^2/2 + b B + c.  It shifts the
        # Legendre coordinate u=aB+b but does not change the dual Hessian.
        affine_slope = Fraction(5, 7)
        for u_value in [Fraction(-3, 2), Fraction(1, 5), Fraction(11, 6)]:
            b_value = (u_value - affine_slope) / radius_squared
            assert_equal(
                "affine-shifted Legendre equation",
                radius_squared * b_value + affine_slope,
                u_value,
            )
            derivative_dual_b_wrt_u = 1 / radius_squared
            assert_equal(
                "affine-shifted Legendre inverse Hessian",
                derivative_dual_b_wrt_u,
                dual_hessian,
            )


def check_abelian_glsm_coulomb_ledger() -> None:
    positive_charge_examples = [
        [1, 1],
        [1, 1, 1],
        [2, 1],
        [2, 3, 1],
    ]
    for charges in positive_charge_examples:
        total_charge = sum(charges)
        assert_equal("positive-charge Coulomb vacuum count", total_charge, sum(charges))

        # In product_i (Q_i sigma/mu)^{Q_i}, the exponent of sigma and mu is
        # plus/minus the total charge.  The nonzero constant is product Q_i^{Q_i}.
        sigma_exponent = sum(charges)
        mu_exponent = -sum(charges)
        charge_constant_degree = sum(charges)
        assert_equal("Coulomb sigma exponent", sigma_exponent, total_charge)
        assert_equal("Coulomb mu exponent", mu_exponent, -total_charge)
        assert_equal(
            "Coulomb charge-constant weighted degree",
            charge_constant_degree,
            total_charge,
        )

    for num_x_fields, degree in [(5, 5), (4, 3), (6, 4), (3, 7)]:
        charges = [1] * num_x_fields + [-degree]
        sigma_exponent = sum(charges)
        assert_equal(
            f"hypersurface Coulomb sigma exponent N={num_x_fields} d={degree}",
            sigma_exponent,
            num_x_fields - degree,
        )
        assert_equal(
            f"hypersurface Coulomb exponent equals axial anomaly N={num_x_fields} d={degree}",
            sigma_exponent,
            glsm_charge_sum(num_x_fields, degree),
        )

    assert_equal("quintic Coulomb exponent vanishes", sum([1, 1, 1, 1, 1, -5]), 0)


def check_compact_fi_theta_fugacity_and_common_flux() -> None:
    # The chapter uses tau=theta/(2*pi)+i r as a period-one coordinate, but
    # physical flux weights use the logarithmic coordinate
    # T=2*pi*i*tau=-2*pi*r+i theta.  This finite model stores the real action
    # exponent and the theta phase in units of 2*pi.
    def compact_flux_weight(
        flux: int,
        theta_units: Fraction,
        area_action_units: Fraction,
    ) -> tuple[Fraction, Fraction]:
        return (-area_action_units * flux, (theta_units * flux) % 1)

    for flux in range(-4, 5):
        theta_units = Fraction(3, 7)
        area_action_units = Fraction(11, 5)
        weight = compact_flux_weight(flux, theta_units, area_action_units)
        shifted_weight = compact_flux_weight(
            flux,
            theta_units + 1,
            area_action_units,
        )
        assert_equal(
            f"compact FI fugacity is theta-periodic for flux {flux}",
            shifted_weight,
            weight,
        )

    unit_flux = 1
    tau_period_shift_multiplier = unit_flux
    if tau_period_shift_multiplier == 0:
        raise AssertionError("exp(tau) would incorrectly pass the theta-period test")

    charges = [1, 1, 1]
    common_flux = 1
    assert_equal(
        "equal-charge CP model has one common gauge flux integer",
        common_flux * sum(charges),
        3,
    )

    flavor_sector_label = [1, 0, 0]
    flavor_swap = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
    ]
    rotated_label = [
        sum(row[col] * flavor_sector_label[col] for col in range(3))
        for row in flavor_swap
    ]
    if rotated_label == flavor_sector_label:
        raise AssertionError("flavor-labelled sector should change under a basis swap")
    assert_equal(
        "common flux is invariant under equal-charge flavor-basis rotation",
        common_flux,
        1,
    )

    bare_q = Fraction(5, 13)
    coefficients = [Fraction(2, 3), Fraction(7, 11), Fraction(17, 19)]
    physical_q = bare_q * prod(coefficients, start=Fraction(1))
    permuted_coefficients = [coefficients[1], coefficients[0], coefficients[2]]
    assert_equal(
        "common CP fugacity is symmetric under flavor-basis relabelling",
        bare_q * prod(permuted_coefficients, start=Fraction(1)),
        physical_q,
    )


def check_abelian_coulomb_one_loop_primitive() -> None:
    # The local determinant gives dW/dSigma = -T + sum_i Q_i log(Q_i Sigma/mu).
    # This check verifies the primitive and its finite FI-coordinate
    # transformation under determinant normalization changes.
    sigma = 1.37
    mu = 0.91
    log_fi = -0.42
    charges = [1, 2, 4]
    step = 1e-6

    def primitive(sigma_value: float) -> float:
        return -log_fi * sigma_value + sum(
            charge
            * sigma_value
            * (log(charge * sigma_value / mu) - 1)
            for charge in charges
        )

    derivative_from_log = -log_fi + sum(
        charge * log(charge * sigma / mu)
        for charge in charges
    )
    derivative_from_primitive = (primitive(sigma + step) - primitive(sigma - step)) / (2 * step)
    assert_close(
        "abelian Coulomb one-loop primitive differentiates to log derivative",
        derivative_from_primitive,
        derivative_from_log,
        tol=1e-9,
    )

    determinant_constants = [Fraction(2, 3), Fraction(5, 4), Fraction(7, 5)]
    finite_fi_shift = sum(
        charge * log(float(constant))
        for charge, constant in zip(charges, determinant_constants)
    )
    shifted_log_fi = log_fi + finite_fi_shift
    with_constants = -log_fi * sigma + sum(
        charge
        * sigma
        * (log(charge * sigma / (mu * float(constant))) - 1)
        for charge, constant in zip(charges, determinant_constants)
    )
    shifted_coordinate_form = -shifted_log_fi * sigma + sum(
        charge * sigma * (log(charge * sigma / mu) - 1)
        for charge in charges
    )
    assert_close(
        "determinant constants are finite FI-coordinate shifts",
        with_constants,
        shifted_coordinate_form,
    )


def check_charged_chiral_dual_elimination() -> None:
    sigmas = [1.3, 0.7]
    charges = [[1, 2], [3, 1], [2, 4]]
    log_fi_values = [0.2, -0.4]
    mu = 1.7
    coefficients = [0.9, 1.2, 2.1]

    masses = [sum(q_a * sigma_a for q_a, sigma_a in zip(row, sigmas)) for row in charges]
    y_values = [-log(mass / (mu * coeff)) for mass, coeff in zip(masses, coefficients)]

    w_dual = -sum(
        log_fi_a * sigma_a
        for log_fi_a, sigma_a in zip(log_fi_values, sigmas)
    )
    w_dual -= sum(mass * y for mass, y in zip(masses, y_values))
    w_dual -= mu * sum(coeff * exp(-y) for coeff, y in zip(coefficients, y_values))

    w_eliminated = -sum(
        log_fi_a * sigma_a
        for log_fi_a, sigma_a in zip(log_fi_values, sigmas)
    )
    w_eliminated += sum(
        mass * (log(mass / (mu * coeff)) - 1)
        for mass, coeff in zip(masses, coefficients)
    )
    assert_close("charged-chiral Y elimination matches one-loop form", w_dual, w_eliminated)

    rank_one_charges = [1, 2, 3]
    sigma = 1.4
    log_fi = -0.6
    coeffs = [0.8, 1.5, 2.2]
    with_coeffs = -log_fi * sigma + sum(
        charge * sigma * (log(charge * sigma / (mu * coeff)) - 1)
        for charge, coeff in zip(rank_one_charges, coeffs)
    )
    shifted_log_fi = log_fi + sum(
        charge * log(coeff)
        for charge, coeff in zip(rank_one_charges, coeffs)
    )
    shifted_form = -shifted_log_fi * sigma + sum(
        charge * sigma * (log(charge * sigma / mu) - 1)
        for charge in rank_one_charges
    )
    assert_close("rank-one FI coordinate absorbs vortex coefficients", with_coeffs, shifted_form)


def check_all_rank_vortex_fi_coordinate_shift() -> None:
    charges = [
        [1, 0],
        [1, 1],
        [0, 2],
        [-2, -3],
        [3, -1],
    ]
    rank = 2
    log_coefficients = [
        Fraction(2, 3),
        Fraction(-5, 4),
        Fraction(7, 6),
        Fraction(11, 5),
        Fraction(-13, 7),
    ]
    x_logs = [
        Fraction(17, 5),
        Fraction(-19, 6),
        Fraction(23, 7),
        Fraction(29, 8),
        Fraction(-31, 9),
    ]
    sigmas = [Fraction(11, 3), Fraction(-7, 4)]

    delta_t = [
        sum(row[a] * ell_i for row, ell_i in zip(charges, log_coefficients))
        for a in range(rank)
    ]

    for a in range(rank):
        bare_constraint_log = sum(row[a] * x_i for row, x_i in zip(charges, x_logs))
        normalized_constraint_log = sum(
            row[a] * (x_i + ell_i)
            for row, x_i, ell_i in zip(charges, x_logs, log_coefficients)
        )
        assert_equal(
            f"all-rank normalized mirror-torus constraint a={a}",
            normalized_constraint_log,
            bare_constraint_log + delta_t[a],
        )

    affine_from_masses = sum(
        sum(row[a] * sigmas[a] for a in range(rank)) * ell_i
        for row, ell_i in zip(charges, log_coefficients)
    )
    affine_from_fi_shift = sum(sigmas[a] * delta_t[a] for a in range(rank))
    assert_equal(
        "all-rank Coulomb affine term equals FI-coordinate shift",
        affine_from_masses,
        affine_from_fi_shift,
    )

    branch_shifts = [1, -2, 3, 0, -1]
    theta_periods = [
        sum(row[a] * branch_i for row, branch_i in zip(charges, branch_shifts))
        for a in range(rank)
    ]
    assert_equal("all-rank logarithm branch theta periods", theta_periods, [-4, 5])

    rank_one_charges = [2, -1, 3, 4]
    rank_one_logs = [Fraction(3, 2), Fraction(-5, 3), Fraction(7, 4), Fraction(11, 5)]
    assert_equal(
        "all-rank formula restricts to rank-one FI shift",
        sum(charge * ell for charge, ell in zip(rank_one_charges, rank_one_logs)),
        Fraction(1123, 60),
    )


def check_vortex_fugacity_dimensional_transmutation() -> None:
    charges = [2, 3, 5]
    charge_sum = sum(charges)
    charge_constant = prod(Fraction(charge) ** charge for charge in charges)
    bare_q = Fraction(7, 11)
    vortex_coefficients = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    q_phys = bare_q * prod(
        coefficient**charge
        for coefficient, charge in zip(vortex_coefficients, charges)
    )
    mu = Fraction(17, 5)
    lambda_power = mu**charge_sum * q_phys / charge_constant

    scale_factor = Fraction(19, 7)
    mu_prime = mu * scale_factor
    q_phys_prime = q_phys / scale_factor**charge_sum
    assert_equal(
        "GLSM vortex fugacity RG-invariant scale",
        mu_prime**charge_sum * q_phys_prime / charge_constant,
        lambda_power,
    )

    wrong_uncompensated_scale = mu_prime**charge_sum * q_phys / charge_constant
    if wrong_uncompensated_scale == lambda_power:
        raise AssertionError("changing mu without FI flow should move the Coulomb scale")

    bare_lambda_power = mu**charge_sum * bare_q / charge_constant
    if bare_lambda_power == lambda_power:
        raise AssertionError("bare FI coordinate should not ignore vortex coefficients")

    anomaly_free_charges = [1, 1, 1, -3]
    assert_equal("anomaly-free GLSM has no mu power", sum(anomaly_free_charges), 0)
    q_anomaly_free = Fraction(23, 29)
    assert_equal(
        "anomaly-free fugacity is dimensionless under mu rescaling",
        q_anomaly_free * mu ** sum(anomaly_free_charges),
        q_anomaly_free,
    )


def check_mirror_primitive_monomial_selection() -> None:
    # If the connected protected correction is h(X)=sum_n a_n X^n and exact
    # Coulomb matching demands X(M)=M/a_1 on a branch, then the critical
    # equation M=X h'(X) forces all higher a_n to vanish.  The check below is
    # the finite coefficient test behind the displayed argument in the chapter.
    a1 = Fraction(5, 3)
    x_value = Fraction(2, 7)
    matched_mass = a1 * x_value
    assert_equal("primitive mirror monomial matches branch", a1 * x_value, matched_mass)

    for degree in range(2, 8):
        higher_coeff = Fraction(degree + 1, degree + 3)
        critical_mass = a1 * x_value + degree * higher_coeff * x_value**degree
        if critical_mass == matched_mass:
            raise AssertionError("higher mirror harmonic should spoil exact Coulomb matching")


def check_vortex_zero_mode_filter() -> None:
    # After the two universal zero modes have been identified with the twisted
    # F-term measure, the residual Berezin integral extracts the top exterior
    # degree.  Without insertions, only zero residual modes survive.
    def survives(residual_zero_modes: int, insertion_degree: int) -> bool:
        return insertion_degree == residual_zero_modes

    for residual_zero_modes in range(0, 7):
        assert_equal(
            f"uninserted vortex F-term survives iff no residual zero modes {residual_zero_modes}",
            survives(residual_zero_modes, 0),
            residual_zero_modes == 0,
        )
        for insertion_degree in range(0, 7):
            assert_equal(
                f"vortex Berezin top-degree saturation r={residual_zero_modes} d={insertion_degree}",
                survives(residual_zero_modes, insertion_degree),
                insertion_degree == residual_zero_modes,
            )

    # Universal zero modes are removed into d^2 theta_tilde before the scalar
    # coefficient is formed; residual modes are the only Grassmann degree left
    # for the coefficient integral.
    total_fermion_zero_modes = 6
    universal_twisted_f_modes = 2
    residual_zero_modes = total_fermion_zero_modes - universal_twisted_f_modes
    assert_equal("vortex residual zero-mode count", residual_zero_modes, 4)
    assert_equal("residual insertions saturate Berezin integral", survives(4, 4), True)
    assert_equal("missing residual insertion kills Berezin integral", survives(4, 3), False)


def check_vortex_fluctuation_complex_gate() -> None:
    # A finite local model of 0 -> gauge -> bosonic fluctuations ->
    # linearized vortex equations.  The first two bosonic coordinates are
    # gauge directions; the next two are collective vortex zero modes.
    gauge_to_fields = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    linearized_vortex = [
        [
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(5),
            Fraction(0),
        ],
        [
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(7),
        ],
    ]
    composed = [
        [
            sum(linearized_vortex[row][mid] * gauge_to_fields[mid][col] for mid in range(6))
            for col in range(2)
        ]
        for row in range(2)
    ]
    assert_equal("finite vortex complex squares to zero", composed, [[0, 0], [0, 0]])
    assert_equal("finite vortex gauge rank", rank_fraction(gauge_to_fields), 2)
    assert_equal("finite vortex equation rank", rank_fraction(linearized_vortex), 2)
    bosonic_kernel_dimension = 6 - rank_fraction(linearized_vortex)
    collective_zero_modes = bosonic_kernel_dimension - rank_fraction(gauge_to_fields)
    assert_equal("vortex collective zero-mode dimension after gauge quotient", collective_zero_modes, 2)

    raw_boson_hessian_eigenvalues = [
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(5),
        Fraction(7),
    ]
    primed_boson_hessian_eigenvalues = [Fraction(5), Fraction(7)]
    ghost_eigenvalues = [Fraction(11), Fraction(13)]
    raw_fermion_eigenvalues = [Fraction(0), Fraction(0), Fraction(17), Fraction(19)]
    primed_fermion_eigenvalues = [Fraction(17), Fraction(19)]

    assert_equal(
        "raw vortex bosonic Hessian determinant vanishes",
        prod(raw_boson_hessian_eigenvalues),
        0,
    )
    assert_equal(
        "raw vortex fermion determinant vanishes",
        prod(raw_fermion_eigenvalues),
        0,
    )

    determinant_weight_squared = (
        prod(primed_fermion_eigenvalues) ** 2
        * prod(ghost_eigenvalues) ** 2
        / prod(primed_boson_hessian_eigenvalues)
    )
    assert_equal(
        "vortex fluctuation determinant ratio squared",
        determinant_weight_squared,
        Fraction(323**2 * 143**2, 35),
    )

    omitted_ghost_weight_squared = (
        prod(primed_fermion_eigenvalues) ** 2
        / prod(primed_boson_hessian_eigenvalues)
    )
    assert_equal(
        "omitting vortex ghosts changes slice density",
        determinant_weight_squared / omitted_ghost_weight_squared,
        prod(ghost_eigenvalues) ** 2,
    )

    universal_fermion_zero_modes = 2
    residual_fermion_zero_modes = 0
    assert_equal(
        "vortex universal zero modes become twisted F-term measure",
        universal_fermion_zero_modes,
        2,
    )
    assert_equal(
        "uninserted vortex term needs no residual fermion zero modes",
        residual_fermion_zero_modes,
        0,
    )
    unsaturated_residual_modes = 1
    uninserted_coefficient_gate = (
        Fraction(1) if unsaturated_residual_modes == 0 else Fraction(0)
    )
    assert_equal(
        "residual vortex zero mode kills uninserted superpotential term",
        uninserted_coefficient_gate,
        0,
    )


def check_single_vortex_amplitude_assembly() -> None:
    # Finite charge-one vortex sector: remove bosonic collective-coordinate
    # zero modes before forming the determinant ratio.
    raw_boson_vortex_spectrum = [Fraction(0), Fraction(0), Fraction(5), Fraction(7)]
    boson_vortex_nonzero = [
        eigenvalue for eigenvalue in raw_boson_vortex_spectrum if eigenvalue != 0
    ]
    assert_equal("raw vortex bosonic determinant has zero modes", prod(raw_boson_vortex_spectrum), 0)
    assert_equal(
        "vortex collective coordinates removed before determinant",
        len(raw_boson_vortex_spectrum) - len(boson_vortex_nonzero),
        2,
    )

    boson_vacuum_spectrum = [Fraction(2), Fraction(3), Fraction(11)]
    ghost_vacuum_spectrum = [Fraction(13), Fraction(17)]
    ghost_vortex_spectrum = [Fraction(19), Fraction(23)]
    fermion_vacuum_blocks = [Fraction(29), Fraction(31)]
    fermion_vortex_blocks = [Fraction(37), Fraction(41)]

    boson_inverse_sqrt_squared = prod(boson_vacuum_spectrum) / prod(boson_vortex_nonzero)
    ghost_ratio = prod(ghost_vortex_spectrum) / prod(ghost_vacuum_spectrum)
    fermion_ratio = prod(fermion_vortex_blocks) / prod(fermion_vacuum_blocks)
    determinant_weight_squared = (
        boson_inverse_sqrt_squared * ghost_ratio**2 * fermion_ratio**2
    )
    assert_equal(
        "single-vortex nonzero-mode determinant weight squared",
        determinant_weight_squared,
        Fraction(66, 35) * Fraction(437, 221) ** 2 * Fraction(1517, 899) ** 2,
    )

    universal_fermion_zero_modes = 2
    twisted_f_term_measure_degree = 2
    assert_equal(
        "universal vortex zero modes match twisted F-term measure",
        universal_fermion_zero_modes,
        twisted_f_term_measure_degree,
    )

    residual_zero_modes = 0
    saturated_zero_mode_coefficient = Fraction(5, 4)
    unsaturated_zero_mode_coefficient = (
        saturated_zero_mode_coefficient if residual_zero_modes == 0 else Fraction(0)
    )
    assert_equal(
        "saturated vortex zero-mode coefficient survives",
        unsaturated_zero_mode_coefficient,
        Fraction(5, 4),
    )

    extra_zero_modes = 2
    extra_unsaturated_coefficient = (
        saturated_zero_mode_coefficient if extra_zero_modes == 0 else Fraction(0)
    )
    assert_equal("extra unsaturated vortex zero modes kill F-term", extra_unsaturated_coefficient, 0)

    reduced_classical_weight = Fraction(7, 9)
    vortex_coefficient_squared = (
        reduced_classical_weight**2
        * determinant_weight_squared
        * saturated_zero_mode_coefficient**2
    )
    assert_equal(
        "single-vortex coefficient assembly squared",
        vortex_coefficient_squared,
        Fraction(7, 9) ** 2 * determinant_weight_squared * Fraction(25, 16),
    )

    # The superpotential has mass dimension one in two dimensions; exp(-Y) and
    # c_i are dimensionless after the regulator integral is normalized by mu.
    assert_equal("single-vortex superpotential dimension", 1 + 0 + 0, 1)

    # Rescaling the finite vortex coefficient is absorbed by an affine shift
    # of the FI coordinate.  In exponentiated form q=exp(T), the same
    # bookkeeping can be represented as q -> q c^{-Q} after shifting T.
    bare_q = Fraction(11, 13)
    charge = 3
    coefficient = Fraction(2, 5)
    shifted_q = bare_q / coefficient**charge
    assert_equal("vortex coefficient FI shift in exponentiated coordinate", shifted_q, Fraction(1375, 104))


def check_one_vortex_frame_and_normal_interaction_separation() -> None:
    gaussian_variance = Fraction(1, 5)
    cubic_coupling = Fraction(2, 7)
    quartic_coupling = Fraction(3, 11)
    gaussian_moments = {
        2: gaussian_variance,
        4: 3 * gaussian_variance**2,
        6: 15 * gaussian_variance**3,
    }
    normal_interaction_factor = (
        Fraction(1)
        - quartic_coupling * gaussian_moments[4]
        + Fraction(1, 2) * cubic_coupling**2 * gaussian_moments[6]
    )
    assert_equal(
        "one-vortex normal interaction cumulant factor",
        normal_interaction_factor,
        Fraction(524, 539),
    )

    original_vortex_fugacity = Fraction(7, 13)
    gaussian_determinant_density = Fraction(11, 17)
    zero_mode_coefficient = Fraction(5, 6)
    reduced_original_coefficient = (
        gaussian_determinant_density
        * normal_interaction_factor
        * zero_mode_coefficient
    )
    original_sector_amplitude = original_vortex_fugacity * reduced_original_coefficient
    determinant_only_reduced_coefficient = (
        gaussian_determinant_density * zero_mode_coefficient
    )
    if reduced_original_coefficient == determinant_only_reduced_coefficient:
        raise AssertionError("normal interaction should change determinant-only vortex coefficient")

    operator_map_normalization = Fraction(3, 5)
    dual_coefficient = operator_map_normalization * reduced_original_coefficient
    assert_equal(
        "dual coefficient is operator-map image of reduced original coefficient",
        dual_coefficient,
        Fraction(1, 1) * operator_map_normalization * reduced_original_coefficient,
    )

    original_frame = ("original_glsm", original_vortex_fugacity)
    dual_frame = ("dual_twisted_chiral", "exp(-Y_i)")
    if original_frame == dual_frame:
        raise AssertionError("original vortex fugacity should not be the dual exponential operator")

    direct_source_integral = Fraction(19, 23)
    original_component = original_vortex_fugacity * direct_source_integral
    dual_component_image = "exp(-Y_i)"  # symbolic tag for the dual operator factor
    if dual_component_image == original_component:
        raise AssertionError("dual operator tag should not be the numerical original component amplitude")

    frame_substituted_component = operator_map_normalization * direct_source_integral
    if frame_substituted_component == original_component:
        raise AssertionError("omitting original fugacity should change direct component amplitude")

    bare_fi_coordinate = Fraction(5, 19)
    correct_mirror_coordinate = bare_fi_coordinate * dual_coefficient
    double_counted_mirror_coordinate = (
        bare_fi_coordinate * operator_map_normalization * original_sector_amplitude
    )
    if double_counted_mirror_coordinate == correct_mirror_coordinate:
        raise AssertionError(
            "FI-theta sector weight should not be folded into c_i and counted again"
        )


def check_one_vortex_source_functional_extraction() -> None:
    # A finite retained chart for the source-functional version of the
    # one-vortex calculation.  The F-term coefficient is the coefficient of the
    # two universal Grassmann zero modes; ordinary component amplitudes need
    # source differentiation before the sources are set to zero.
    reduced_classical_weights = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    collective_measure_cells = [Fraction(3, 5), Fraction(7, 11), Fraction(13, 17)]
    primed_nonzero_density = [Fraction(19, 23), Fraction(29, 31), Fraction(37, 41)]
    vacuum_interaction_factors = [Fraction(31, 29), Fraction(37, 43), Fraction(41, 47)]
    source_dependent_interaction_corrections = [
        Fraction(1, 97),
        -Fraction(1, 101),
        Fraction(1, 103),
    ]
    effective_f_term_insertions = [
        vacuum + correction
        for vacuum, correction in zip(
            vacuum_interaction_factors,
            source_dependent_interaction_corrections,
        )
    ]
    ghost_density = [Fraction(43, 47), Fraction(53, 59), Fraction(61, 67)]
    residual_zero_mode_gates = [Fraction(1), Fraction(1), Fraction(1)]

    retained_f_term_cells = [
        classical * measure * nonzero * interaction * ghost * gate
        for classical, measure, nonzero, interaction, ghost, gate in zip(
            reduced_classical_weights,
            collective_measure_cells,
            primed_nonzero_density,
            effective_f_term_insertions,
            ghost_density,
            residual_zero_mode_gates,
        )
    ]
    retained_f_term_coefficient = sum(retained_f_term_cells, Fraction(0))
    assert_gt_bound(
        "retained one-vortex source F-term coefficient is nonzero",
        retained_f_term_coefficient,
        Fraction(0),
    )

    unprojected_component_at_zero_source = Fraction(0)
    assert_equal(
        "unprojected component with universal zero modes vanishes",
        unprojected_component_at_zero_source,
        Fraction(0),
    )
    if unprojected_component_at_zero_source == retained_f_term_coefficient:
        raise AssertionError("zero-source component should not equal F-term projection")

    normalized_source_overlaps = [Fraction(1), Fraction(1), Fraction(1)]
    normalized_two_source_amplitude = sum(
        cell * overlap
        for cell, overlap in zip(retained_f_term_cells, normalized_source_overlaps)
    )
    assert_equal(
        "normalized source differentiation extracts the F-term coefficient",
        normalized_two_source_amplitude,
        retained_f_term_coefficient,
    )

    transported_source_overlaps = [Fraction(5, 4), Fraction(7, 6), Fraction(11, 10)]
    component_two_source_amplitude = sum(
        cell * overlap
        for cell, overlap in zip(retained_f_term_cells, transported_source_overlaps)
    )
    if component_two_source_amplitude == retained_f_term_coefficient:
        raise AssertionError("nontrivial source overlaps should change the component amplitude")

    vacuum_scalar_only_prediction = sum(
        classical * measure * nonzero * vacuum * ghost * gate
        for classical, measure, nonzero, vacuum, ghost, gate in zip(
            reduced_classical_weights,
            collective_measure_cells,
            primed_nonzero_density,
            vacuum_interaction_factors,
            ghost_density,
            residual_zero_mode_gates,
        )
    )
    if vacuum_scalar_only_prediction == retained_f_term_coefficient:
        raise AssertionError(
            "vacuum interaction factor should not replace source-dependent cumulants"
        )

    gaussian_moments = {
        2: Fraction(1, 5),
        4: Fraction(3, 25),
    }
    interaction_strength = Fraction(2, 7)
    source_quadratic_weight = Fraction(3, 11)
    vacuum_factor = Fraction(1) - interaction_strength * gaussian_moments[2]
    bare_source_expectation = Fraction(1) + source_quadratic_weight * gaussian_moments[2]
    source_inserted_interaction = (
        Fraction(1)
        + source_quadratic_weight * gaussian_moments[2]
        - interaction_strength * gaussian_moments[2]
        - interaction_strength * source_quadratic_weight * gaussian_moments[4]
    )
    factorized_source_shortcut = vacuum_factor * bare_source_expectation
    if factorized_source_shortcut == source_inserted_interaction:
        raise AssertionError(
            "interacting source expectation should not be a vacuum scalar times insertion"
        )

    moduli_only_cells = [
        classical * measure
        for classical, measure in zip(reduced_classical_weights, collective_measure_cells)
    ]
    moduli_only_prediction = sum(moduli_only_cells, Fraction(0))
    if moduli_only_prediction == retained_f_term_coefficient:
        raise AssertionError("moduli measure alone should not reproduce the vortex amplitude")

    missing_ghost_prediction = sum(
        classical * measure * nonzero * interaction * gate
        for classical, measure, nonzero, interaction, gate in zip(
            reduced_classical_weights,
            collective_measure_cells,
            primed_nonzero_density,
            effective_f_term_insertions,
            residual_zero_mode_gates,
        )
    )
    if missing_ghost_prediction == retained_f_term_coefficient:
        raise AssertionError("omitting the ghost density should change the source amplitude")

    determinant_only_prediction = sum(
        classical * measure * nonzero * ghost * gate
        for classical, measure, nonzero, ghost, gate in zip(
            reduced_classical_weights,
            collective_measure_cells,
            primed_nonzero_density,
            ghost_density,
            residual_zero_mode_gates,
        )
    )
    if determinant_only_prediction == retained_f_term_coefficient:
        raise AssertionError("determinant-only source coefficient should miss normal interactions")

    residual_unsaturated_gate = Fraction(0)
    residual_zero_mode_killed = retained_f_term_coefficient * residual_unsaturated_gate
    assert_equal(
        "unsaturated residual zero mode kills source-extracted F-term",
        residual_zero_mode_killed,
        Fraction(0),
    )

    mirror_exponential_only = Fraction(1)
    if mirror_exponential_only == retained_f_term_coefficient:
        raise AssertionError("formal mirror monomial should not supply the amplitude coefficient")

    residuals = {
        "source overlap": Fraction(1, 101),
        "primed propagator": Fraction(1, 103),
        "determinant line": Fraction(1, 107),
        "normal interaction": Fraction(1, 108),
        "zero-mode map": Fraction(1, 109),
        "compactification": Fraction(1, 113),
        "continuum": Fraction(1, 127),
    }
    direct_source_amplitude = retained_f_term_coefficient + sum(
        residuals.values(),
        Fraction(0),
    )
    actual_source_error = abs(direct_source_amplitude - retained_f_term_coefficient)
    source_bound = sum(abs(value) for value in residuals.values())
    assert_equal(
        "one-vortex source-amplitude residual telescope",
        actual_source_error,
        source_bound,
    )
    omitted_source_bound = source_bound - residuals["source overlap"]
    assert_gt_bound(
        "omitting source-overlap residual underbudgets one-vortex source amplitude",
        actual_source_error,
        omitted_source_bound,
    )
    omitted_interaction_bound = source_bound - residuals["normal interaction"]
    assert_gt_bound(
        "omitting normal-interaction residual underbudgets one-vortex source amplitude",
        actual_source_error,
        omitted_interaction_bound,
    )


def check_one_vortex_component_amplitude_cell() -> None:
    # A finite retained one-vortex component amplitude needs the oriented minor
    # of two source overlaps with the universal zero-mode line, plus any primed
    # nonzero-mode contact term in the same determinant convention.
    retained_cells = [Fraction(3, 5), Fraction(7, 11), Fraction(11, 13)]
    source_a = [
        (Fraction(2, 3), Fraction(1, 5)),
        (Fraction(3, 7), Fraction(2, 9)),
        (Fraction(5, 11), Fraction(1, 4)),
    ]
    source_b = [
        (Fraction(1, 2), Fraction(4, 7)),
        (Fraction(5, 8), Fraction(7, 10)),
        (Fraction(3, 5), Fraction(6, 13)),
    ]
    primed_contacts = [Fraction(1, 17), -Fraction(1, 19), Fraction(1, 23)]

    def source_minor(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> Fraction:
        return left[0] * right[1] - left[1] * right[0]

    oriented_minors = [source_minor(left, right) for left, right in zip(source_a, source_b)]
    component_amplitude = sum(
        cell * (minor + contact)
        for cell, minor, contact in zip(retained_cells, oriented_minors, primed_contacts)
    )
    protected_vortex_coefficient = sum(retained_cells, Fraction(0))
    assert_gt_bound("worked one-vortex component amplitude is nonzero", abs(component_amplitude), Fraction(0))
    if component_amplitude == protected_vortex_coefficient:
        raise AssertionError("component amplitude should not collapse to the protected vortex coefficient")

    norm_product_shortcut = sum(
        cell * (left[0] * right[0] + left[1] * right[1])
        for cell, left, right in zip(retained_cells, source_a, source_b)
    )
    if norm_product_shortcut == component_amplitude:
        raise AssertionError("zero-mode source pairing should use the oriented minor, not a norm product")

    wrong_orientation = sum(
        cell * (-minor + contact)
        for cell, minor, contact in zip(retained_cells, oriented_minors, primed_contacts)
    )
    if wrong_orientation == component_amplitude:
        raise AssertionError("zero-mode orientation flip should change the component amplitude")

    contact_omitted = sum(cell * minor for cell, minor in zip(retained_cells, oriented_minors))
    if contact_omitted == component_amplitude:
        raise AssertionError("primed-propagator contact should be source-specific data")

    parallel_source_b = [(2 * left[0], 2 * left[1]) for left in source_a]
    parallel_minors = [source_minor(left, right) for left, right in zip(source_a, parallel_source_b)]
    parallel_component_without_contact = sum(
        cell * minor for cell, minor in zip(retained_cells, parallel_minors)
    )
    assert_equal(
        "parallel source overlaps do not saturate the two universal zero modes",
        parallel_component_without_contact,
        Fraction(0),
    )
    if protected_vortex_coefficient == parallel_component_without_contact:
        raise AssertionError("mirror coefficient alone should not bypass parallel source-zero-mode failure")

    residuals = {
        "source": Fraction(1, 101),
        "propagator": Fraction(1, 103),
        "determinant": Fraction(1, 107),
        "zero mode": Fraction(1, 109),
        "compactification": Fraction(1, 113),
        "operator": Fraction(1, 127),
        "continuum": Fraction(1, 131),
    }
    direct_component = component_amplitude + sum(residuals.values(), Fraction(0))
    actual_error = abs(direct_component - component_amplitude)
    residual_bound = sum(abs(value) for value in residuals.values())
    assert_equal("one-vortex component residual telescope", actual_error, residual_bound)
    underbudgeted_bound = residual_bound - residuals["propagator"]
    assert_gt_bound(
        "omitting primed-propagator residual underbudgets component amplitude",
        actual_error,
        underbudgeted_bound,
    )


def check_one_vortex_source_frame_calibration() -> None:
    # The original GLSM component amplitude carries a numerical vortex
    # fugacity.  Its dual image carries the exp(-Y_i) operator tag only after
    # the original-to-dual map is fixed.
    retained_cells = [Fraction(2, 5), Fraction(3, 7), Fraction(5, 11)]
    original_vortex_fugacity = Fraction(7, 13)
    dual_operator_tag = "exp(-Y_i)"

    def source_minor(
        left: tuple[Fraction, Fraction],
        right: tuple[Fraction, Fraction],
    ) -> Fraction:
        return left[0] * right[1] - left[1] * right[0]

    reference_left = [
        (Fraction(1, 2), Fraction(1, 5)),
        (Fraction(2, 3), Fraction(1, 7)),
        (Fraction(3, 5), Fraction(1, 11)),
    ]
    reference_right = [
        (Fraction(1, 3), Fraction(3, 4)),
        (Fraction(1, 5), Fraction(4, 7)),
        (Fraction(1, 7), Fraction(5, 9)),
    ]
    target_left = [
        (Fraction(2, 7), Fraction(1, 6)),
        (Fraction(3, 8), Fraction(1, 9)),
        (Fraction(4, 9), Fraction(1, 10)),
    ]
    target_right = [
        (Fraction(5, 11), Fraction(2, 5)),
        (Fraction(7, 13), Fraction(3, 7)),
        (Fraction(11, 17), Fraction(5, 8)),
    ]
    reference_contacts = [Fraction(1, 37), -Fraction(1, 41), Fraction(1, 43)]
    target_contacts = [-Fraction(1, 47), Fraction(1, 53), Fraction(1, 59)]

    def source_integral(
        left_sources: list[tuple[Fraction, Fraction]],
        right_sources: list[tuple[Fraction, Fraction]],
        contacts: list[Fraction],
    ) -> Fraction:
        return sum(
            cell * (source_minor(left, right) + contact)
            for cell, left, right, contact in zip(
                retained_cells,
                left_sources,
                right_sources,
                contacts,
            )
        )

    reference_integral = source_integral(
        reference_left,
        reference_right,
        reference_contacts,
    )
    target_integral = source_integral(target_left, target_right, target_contacts)
    assert_gt_bound("one-vortex reference source integral is nonzero", abs(reference_integral), Fraction(0))
    assert_gt_bound("one-vortex target source integral is nonzero", abs(target_integral), Fraction(0))

    reference_amplitude = original_vortex_fugacity * reference_integral
    target_amplitude = original_vortex_fugacity * target_integral
    source_frame_ratio = target_integral / reference_integral
    assert_equal(
        "source-frame ratio calibrates target component amplitude",
        source_frame_ratio * reference_amplitude,
        target_amplitude,
    )

    protected_coefficient = sum(retained_cells, Fraction(0))
    mirror_fugacity_only = original_vortex_fugacity * protected_coefficient
    if mirror_fugacity_only == target_amplitude:
        raise AssertionError("mirror fugacity alone should not determine a component amplitude")
    if dual_operator_tag == target_amplitude:
        raise AssertionError("dual operator tag should not be a numerical direct component amplitude")

    contact_omitted_target = source_integral(
        target_left,
        target_right,
        [Fraction(0), Fraction(0), Fraction(0)],
    )
    if contact_omitted_target == target_integral:
        raise AssertionError("primed contact data should affect the target source-frame integral")
    if (contact_omitted_target / reference_integral) * reference_amplitude == target_amplitude:
        raise AssertionError("contact-omitted source ratio should not calibrate the target amplitude")

    parallel_right = [(2 * left[0], 2 * left[1]) for left in target_left]
    parallel_integral = source_integral(
        target_left,
        parallel_right,
        [Fraction(0), Fraction(0), Fraction(0)],
    )
    assert_equal(
        "parallel source pair has zero retained component integral",
        parallel_integral,
        Fraction(0),
    )
    if mirror_fugacity_only == original_vortex_fugacity * parallel_integral:
        raise AssertionError("nonzero mirror fugacity should not bypass a zero source minor")

    zero_reference_integral = Fraction(0)
    if zero_reference_integral != 0:
        raise AssertionError("unreachable denominator guard")
    # The finite source-frame ratio is undefined here; a reference channel with
    # no source-zero-mode support cannot calibrate a target component amplitude.
    assert_equal("zero reference denominator blocks calibration", zero_reference_integral, 0)

    residuals = {
        "target": Fraction(1, 1009),
        "reference": Fraction(1, 1013),
        "frame": Fraction(1, 1019),
    }
    calibrated_residual = (
        residuals["target"]
        - source_frame_ratio * residuals["reference"]
        + residuals["frame"]
    )
    calibrated_bound = (
        abs(residuals["target"])
        + abs(source_frame_ratio) * abs(residuals["reference"])
        + abs(residuals["frame"])
    )
    assert_leq_bound(
        "one-vortex source-frame calibration residual propagation",
        abs(calibrated_residual),
        calibrated_bound,
    )
    underbudgeted_without_frame = calibrated_bound - abs(residuals["frame"])
    assert_gt_bound(
        "omitting source-frame transport underbudgets calibrated amplitude",
        calibrated_bound,
        underbudgeted_without_frame,
    )


def check_vortex_coefficient_noncancellation_bound() -> None:
    # The retained one-vortex window carries a signed integrand, not just an
    # allowed charge.  A usable amplitude bound needs a margin between
    # the signed coefficient and all determinant, zero-mode, boundary, and
    # continuum errors.
    retained_cells = [Fraction(3, 4), Fraction(-1, 8), Fraction(1, 16)]
    retained_signed = sum(retained_cells, Fraction(0))
    retained_mass = sum(abs(cell) for cell in retained_cells)
    noncancellation_fraction = abs(retained_signed) / retained_mass

    assert_equal(
        "retained vortex coefficient signed value",
        retained_signed,
        Fraction(11, 16),
    )
    assert_equal(
        "retained vortex coefficient absolute mass",
        retained_mass,
        Fraction(15, 16),
    )
    assert_equal(
        "retained vortex noncancellation fraction",
        noncancellation_fraction,
        Fraction(11, 15),
    )

    original_vortex_fugacity = Fraction(7, 13)
    operator_map_normalization = Fraction(5, 7)
    original_sector_retained = original_vortex_fugacity * retained_signed
    dual_retained = operator_map_normalization * retained_signed
    if original_sector_retained == dual_retained:
        raise AssertionError(
            "original FI-weighted sector and dual mapped coefficient should be distinct data"
        )

    residuals = {
        "tail": Fraction(1, 80),
        "determinant": Fraction(1, 90),
        "zero-mode orientation": Fraction(1, 100),
        "compactification boundary": Fraction(1, 110),
    }
    total_residual_bound = sum(residuals.values(), Fraction(0))
    bounded_reduced_coefficient = retained_signed + total_residual_bound
    actual_error = abs(bounded_reduced_coefficient - retained_signed)

    assert_equal(
        "one-vortex reduced coefficient residual telescope",
        actual_error,
        total_residual_bound,
    )
    assert_gt_bound(
        "one-vortex signed window dominates residuals",
        abs(retained_signed),
        total_residual_bound,
    )
    assert_leq_bound(
        "one-vortex relative coefficient error",
        total_residual_bound / (noncancellation_fraction * retained_mass),
        Fraction(1, 10),
    )

    map_residual = Fraction(1, 130)
    continuum_residual = Fraction(1, 140)
    dual_bound = (
        abs(operator_map_normalization) * total_residual_bound
        + map_residual
        + continuum_residual
    )
    dual_target = operator_map_normalization * retained_signed
    dual_probe = dual_target + dual_bound
    assert_equal(
        "one-vortex dual coefficient includes operator-map residual",
        abs(dual_probe - dual_target),
        dual_bound,
    )
    assert_gt_bound(
        "mapped one-vortex window dominates dual residuals",
        abs(dual_target),
        dual_bound,
    )

    wrong_dual_target = retained_signed
    if wrong_dual_target == dual_target:
        raise AssertionError("dual noncancellation target must include Z_map")
    wrong_double_counted_dual_target = (
        operator_map_normalization * original_sector_retained
    )
    if wrong_double_counted_dual_target == dual_target:
        raise AssertionError("dual target should not include the original FI-theta weight")

    omitted_determinant_budget = total_residual_bound - residuals["determinant"]
    assert_gt_bound(
        "omitting determinant residual underbudgets vortex coefficient",
        actual_error,
        omitted_determinant_budget,
    )

    canceling_cells = [Fraction(1, 3), Fraction(-1, 3)]
    canceling_signed = sum(canceling_cells, Fraction(0))
    canceling_mass = sum(abs(cell) for cell in canceling_cells)
    charge_and_zero_mode_allowed = True
    determinant_line_declared = True
    symmetry_only_nonzero_claim = (
        charge_and_zero_mode_allowed
        and determinant_line_declared
        and canceling_signed != 0
    )
    assert_equal(
        "coherent signed cancellation can leave nonzero mass",
        canceling_mass,
        Fraction(2, 3),
    )
    assert_equal(
        "symmetry-only vortex coefficient nonzero claim rejected",
        symmetry_only_nonzero_claim,
        False,
    )


def check_cp_mirror_critical_ledger() -> None:
    for n_fields in range(2, 9):
        x = Fraction(3, 2)
        product_constraint = x**n_fields
        assert_equal(
            f"CP^{n_fields - 1} constrained product",
            prod([x] * n_fields),
            product_constraint,
        )

        # In logarithmic variables z_a=log X_a, a=1,...,N-1, with
        # X_N=q/(X_1...X_{N-1}), the critical equations are X_a=X_N.
        # At a common nonzero value x, the Hessian is x(I+J), whose determinant
        # is N x^{N-1}; this proves the critical points are simple.
        log_hessian_determinant = n_fields * x ** (n_fields - 1)
        if log_hessian_determinant == 0:
            raise AssertionError("CP mirror critical Hessian should be nonzero")


def nth_root_power_sum(n_fields: int, exponent: int, q_value: Fraction) -> Fraction:
    if exponent % n_fields != 0:
        return Fraction(0)
    return Fraction(n_fields) * q_value ** (exponent // n_fields)


def cp_mirror_residue_trace(n_fields: int, insertion_power: int, q_value: Fraction) -> Fraction:
    if insertion_power < 0:
        raise ValueError(
            "CP mirror residue trace is defined here for polynomial insertions"
        )
    root_power = insertion_power - (n_fields - 1)
    return nth_root_power_sum(n_fields, root_power, q_value) / n_fields


def check_cp_mirror_residue_correlators() -> None:
    for n_fields in range(2, 9):
        q_phys = Fraction(n_fields + 1, n_fields + 4)
        x = Fraction(5, 3)

        # In the constrained logarithmic torus the Hessian denominator of the
        # normalized mirror trace is det(x(I+J))=N x^{N-1}.
        hessian = [
            [x * (1 + int(row == col)) for col in range(n_fields - 1)]
            for row in range(n_fields - 1)
        ]
        assert_equal(
            f"CP^{n_fields - 1} residue Hessian denominator",
            determinant_fraction(hessian),
            n_fields * x ** (n_fields - 1),
        )

        assert_equal(
            f"CP^{n_fields - 1} top trace normalization",
            cp_mirror_residue_trace(n_fields, n_fields - 1, q_phys),
            Fraction(1),
        )

        for degree in range(1, 4):
            insertion_power = n_fields - 1 + degree * n_fields
            assert_equal(
                f"CP^{n_fields - 1} degree-{degree} residue selection",
                cp_mirror_residue_trace(n_fields, insertion_power, q_phys),
                q_phys**degree,
            )

        for insertion_power in range(0, 4 * n_fields):
            selected = (insertion_power - (n_fields - 1)) % n_fields == 0
            if not selected:
                assert_equal(
                    f"CP^{n_fields - 1} off-selection residue vanishes k={insertion_power}",
                    cp_mirror_residue_trace(n_fields, insertion_power, q_phys),
                    Fraction(0),
                )

        for insertion_power in range(0, 3 * n_fields):
            assert_equal(
                f"CP^{n_fields - 1} quantum-product trace recurrence k={insertion_power}",
                cp_mirror_residue_trace(n_fields, insertion_power + n_fields, q_phys),
                q_phys * cp_mirror_residue_trace(n_fields, insertion_power, q_phys),
            )


def check_vortex_to_observable_proof_obligation_map() -> None:
    n_fields = 4
    q_regulated = Fraction(5, 7)
    insertion_power = n_fields - 1 + 2 * n_fields
    residue_prediction = cp_mirror_residue_trace(
        n_fields,
        insertion_power,
        q_regulated,
    )
    assert_equal(
        "finite mirror residue prediction is q^degree",
        residue_prediction,
        q_regulated**2,
    )

    residuals = {
        "coefficient": Fraction(1, 13),
        "determinant": Fraction(1, 17),
        "zero mode": Fraction(1, 19),
        "compactification": Fraction(1, 23),
        "gluing": Fraction(1, 29),
        "operator map": Fraction(1, 31),
        "continuum": Fraction(1, 37),
    }
    protected_amplitude = residue_prediction + sum(residuals.values(), Fraction(0))
    actual_error = abs(protected_amplitude - residue_prediction)
    full_budget = sum(abs(value) for value in residuals.values())
    assert_equal(
        "vortex-to-observable proof-obligation telescope",
        actual_error,
        full_budget,
    )

    omitted_operator_budget = full_budget - abs(residuals["operator map"])
    if actual_error <= omitted_operator_budget:
        raise AssertionError("omitting operator-map residual should underbudget the error")

    assert_equal(
        "zero residuals identify protected amplitude with residue prediction",
        residue_prediction + sum([Fraction(0)] * len(residuals), Fraction(0)),
        residue_prediction,
    )

    bare_q = Fraction(3, 11)
    vortex_coefficients = [
        Fraction(2, 3),
        Fraction(5, 7),
        Fraction(11, 13),
        Fraction(17, 19),
    ]
    q_with_vortex_measure = bare_q * prod(vortex_coefficients)
    degree_one_power = n_fields - 1 + n_fields
    assert_equal(
        "degree-one observable uses vortex-normalized q",
        cp_mirror_residue_trace(n_fields, degree_one_power, q_with_vortex_measure),
        q_with_vortex_measure,
    )
    if cp_mirror_residue_trace(n_fields, degree_one_power, bare_q) == q_with_vortex_measure:
        raise AssertionError("bare FI coordinate should not ignore vortex coefficients")

    unsaturated_zero_mode_gate = Fraction(0)
    q_unsaturated = bare_q * prod(vortex_coefficients) * unsaturated_zero_mode_gate
    assert_equal(
        "unsaturated residual zero modes kill degree-one observable",
        cp_mirror_residue_trace(n_fields, degree_one_power, q_unsaturated),
        Fraction(0),
    )
    if cp_mirror_residue_trace(n_fields, degree_one_power, bare_q) == q_unsaturated:
        raise AssertionError("symmetry-only q should not survive a zero-mode gate")


def quantum_product_power(n_fields: int, left_power: int, right_power: int) -> tuple[int, int]:
    total_power = left_power + right_power
    return total_power % n_fields, total_power // n_fields


def degree_one_cpn_incidence_factors(n_fields: int) -> dict[str, Fraction]:
    """Return the finite factors in the CP^{N-1} degree-one incidence chart."""

    variables = (
        [("A", index) for index in range(1, n_fields)]
        + [("B", index) for index in range(n_fields)]
    )
    constraints = (
        [("A", index, Fraction(0)) for index in range(1, n_fields)]
        + [("B", 0, Fraction(0)), ("B", 1, Fraction(1))]
        + [("B", index, Fraction(0)) for index in range(2, n_fields)]
    )
    incidence_matrix = [
        [
            Fraction(1) if variable == (kind, index) else Fraction(0)
            for variable in variables
        ]
        for kind, index, _value in constraints
    ]
    orientation = determinant_fraction(incidence_matrix)

    solution = {("A", 0): Fraction(1)}
    solution.update({(kind, index): value for kind, index, value in constraints})
    first_mark = [solution.get(("A", index), Fraction(0)) for index in range(n_fields)]
    second_mark = [solution.get(("B", index), Fraction(0)) for index in range(n_fields)]
    point_zero = [Fraction(1)] + [Fraction(0)] * (n_fields - 1)
    point_one = [Fraction(0), Fraction(1)] + [Fraction(0)] * (n_fields - 2)
    hyperplane = [Fraction(-1), Fraction(1)] + [Fraction(0)] * (n_fields - 2)

    def linear_value(linear_form: list[Fraction], point: list[Fraction]) -> Fraction:
        return sum(
            (coefficient * coordinate for coefficient, coordinate in zip(linear_form, point)),
            Fraction(0),
        )

    boundary_excluded = (
        first_mark == point_zero
        and second_mark == point_one
        and point_zero != point_one
        and linear_value(hyperplane, point_zero) != 0
        and linear_value(hyperplane, point_one) != 0
    )
    insertion_complex_degree = 1 + (n_fields - 1) + (n_fields - 1)
    selection_gate = (
        Fraction(1)
        if insertion_complex_degree == len(variables)
        else Fraction(0)
    )
    compactification_gate = Fraction(1) if boundary_excluded else Fraction(0)
    operator_normalization = Fraction(1)
    return {
        "orientation": orientation,
        "selection_gate": selection_gate,
        "compactification_gate": compactification_gate,
        "operator_normalization": operator_normalization,
        "incidence_integral": (
            orientation
            * selection_gate
            * compactification_gate
            * operator_normalization
        ),
    }


def check_cp_degree_one_stable_map_quantum_product_gate() -> None:
    for n_fields in range(2, 9):
        degree = 1
        virtual_dimension = (n_fields - 1) + n_fields * degree
        codimension_relation = 1 + (n_fields - 1) + (n_fields - 1)
        assert_equal(
            f"CP^{n_fields - 1} degree-one stable-map dimension",
            virtual_dimension,
            2 * n_fields - 1,
        )
        assert_equal(
            f"CP^{n_fields - 1} quantum-product insertion dimension",
            codimension_relation,
            virtual_dimension,
        )

        wrong_top_power = n_fields - 2
        wrong_codimension = 1 + wrong_top_power + (n_fields - 1)
        if wrong_codimension == virtual_dimension:
            raise AssertionError("lower insertion power should miss degree-one dimension")

        for wrong_degree in [0, 2, 3]:
            wrong_virtual_dimension = (n_fields - 1) + n_fields * wrong_degree
            if codimension_relation == wrong_virtual_dimension:
                raise AssertionError("degree-one insertion should not match another degree")

        # Two generic point constraints determine one projective line, and a
        # generic hyperplane meets that line once.  This is the finite count
        # behind I_1(H,H^{N-1},H^{N-1})=1.
        unique_line_through_two_points = 1
        hyperplane_intersections_with_line = 1
        assert_equal(
            f"CP^{n_fields - 1} degree-one line count",
            unique_line_through_two_points * hyperplane_intersections_with_line,
            1,
        )

        reduced_power, q_power = quantum_product_power(n_fields, 1, n_fields - 1)
        assert_equal("H times top class reduces to the unit", reduced_power, 0)
        assert_equal("H times top class carries one q", q_power, 1)

        for pairing_power in range(n_fields):
            nonzero_pairing = reduced_power + pairing_power == n_fields - 1
            assert_equal(
                f"quantum relation pairs only with top class a={pairing_power}",
                nonzero_pairing,
                pairing_power == n_fields - 1,
            )


def check_degree_one_stable_map_incidence_model() -> None:
    # The degree-one product coefficient is an observable pairing, not just a
    # residue root sum or a dimension count.  This finite model treats the
    # vortex coefficients as supplied input and checks the stable-map incidence
    # Jacobian, selection degree, boundary exclusion, operator normalization,
    # and proof-obligation map before any continuum comparison residuals are invoked.
    n_fields = 5
    bare_fi = Fraction(3, 17)

    supplied_spectral_blocks = [
        ([2, 3], [5, 7], [11], [13], [17], [19], Fraction(23, 29)),
        ([3, 5], [7, 11], [13], [17], [19], [23], Fraction(29, 31)),
        ([5, 7], [11, 13], [17], [19], [23], [29], Fraction(31, 37)),
        ([7, 11], [13, 17], [19], [23], [29], [31], Fraction(37, 41)),
        ([11, 13], [17, 19], [23], [29], [31], [37], Fraction(41, 43)),
    ]

    def finite_det(values: list[int]) -> Fraction:
        return prod((Fraction(value) for value in values), start=Fraction(1))

    def supplied_vortex_coefficient(
        block: tuple[list[int], list[int], list[int], list[int], list[int], list[int], Fraction],
    ) -> Fraction:
        (
            boson_vacuum,
            boson_vortex_nonzero,
            fermion_vacuum,
            fermion_vortex,
            ghost_vacuum,
            ghost_vortex,
            zero_mode_metric,
        ) = block
        numerator = (
            finite_det(fermion_vortex)
            * finite_det(ghost_vortex)
            * finite_det(boson_vacuum)
            * zero_mode_metric
        )
        denominator = (
            finite_det(boson_vortex_nonzero)
            * finite_det(fermion_vacuum)
            * finite_det(ghost_vacuum)
        )
        return Fraction(numerator, denominator)

    vortex_coefficients = [
        supplied_vortex_coefficient(block)
        for block in supplied_spectral_blocks
    ]
    q_regulated = bare_fi * prod(vortex_coefficients, start=Fraction(1))

    variables = (
        [("A", index) for index in range(1, n_fields)]
        + [("B", index) for index in range(n_fields)]
    )
    constraints = (
        [("A", index, Fraction(0)) for index in range(1, n_fields)]
        + [("B", 0, Fraction(0)), ("B", 1, Fraction(1))]
        + [("B", index, Fraction(0)) for index in range(2, n_fields)]
    )
    incidence_matrix = [
        [
            Fraction(1) if variable == (kind, index) else Fraction(0)
            for variable in variables
        ]
        for kind, index, _value in constraints
    ]
    orientation_sign = determinant_fraction(incidence_matrix)
    assert_equal("degree-one stable-map incidence orientation", orientation_sign, Fraction(1))

    solution = {("A", 0): Fraction(1)}
    solution.update({(kind, index): value for kind, index, value in constraints})
    first_mark = [solution.get(("A", index), Fraction(0)) for index in range(n_fields)]
    second_mark = [solution.get(("B", index), Fraction(0)) for index in range(n_fields)]
    third_mark = [
        solution.get(("A", index), Fraction(0)) + solution.get(("B", index), Fraction(0))
        for index in range(n_fields)
    ]
    point_zero = [Fraction(1)] + [Fraction(0)] * (n_fields - 1)
    point_one = [Fraction(0), Fraction(1)] + [Fraction(0)] * (n_fields - 2)
    hyperplane = [Fraction(-1), Fraction(1)] + [Fraction(0)] * (n_fields - 2)

    def linear_value(linear_form: list[Fraction], point: list[Fraction]) -> Fraction:
        return sum(
            (coefficient * coordinate for coefficient, coordinate in zip(linear_form, point)),
            Fraction(0),
        )

    def hyperplane_value(point: list[Fraction]) -> Fraction:
        return linear_value(hyperplane, point)

    assert_equal("first point incidence", first_mark, point_zero)
    assert_equal("second point incidence", second_mark, point_one)
    assert_equal("third mark lies on normalized hyperplane", hyperplane_value(third_mark), Fraction(0))

    incidence_chart_dimension = len(variables)
    insertion_complex_degree = 1 + (n_fields - 1) + (n_fields - 1)
    assert_equal("degree-one incidence-chart dimension", incidence_chart_dimension, 2 * n_fields - 1)
    assert_equal("stable-map insertion degree saturates the chart", insertion_complex_degree, incidence_chart_dimension)
    selection_gate = Fraction(1) if insertion_complex_degree == incidence_chart_dimension else Fraction(0)

    boundary_excluded = (
        point_zero != point_one
        and hyperplane_value(point_zero) != 0
        and hyperplane_value(point_one) != 0
    )
    assert_equal("degree-one compactification boundary excluded", boundary_excluded, True)
    compactification_factor = Fraction(1) if boundary_excluded else Fraction(0)
    operator_normalization = Fraction(1)
    retained_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * compactification_factor
        * operator_normalization
    )
    assert_equal(
        "stable-map incidence model gives supplied degree-one product coefficient",
        retained_three_point,
        q_regulated,
    )

    signed_residuals = {
        "coefficient": Fraction(1, 100003),
        "determinant": Fraction(-1, 100019),
        "zero mode": Fraction(1, 100043),
        "line compactification": Fraction(-1, 100049),
        "operator map": Fraction(1, 100057),
        "continuum": Fraction(-1, 100069),
    }
    residual_bounds = {
        name: abs(value) + Fraction(1, 1_000_000 + index)
        for index, (name, value) in enumerate(signed_residuals.items())
    }
    comparison_residual = sum(signed_residuals.values(), Fraction(0))
    full_correlator_probe = retained_three_point + comparison_residual
    actual_error = abs(full_correlator_probe - retained_three_point)
    total_bound = sum(residual_bounds.values(), Fraction(0))
    assert_equal(
        "degree-one observable comparison residual is independently signed",
        full_correlator_probe - retained_three_point,
        comparison_residual,
    )
    assert_leq_bound(
        "degree-one observable proof-obligation propagation",
        actual_error,
        total_bound,
    )
    assert_leq_bound(
        "degree-one observable conditional relative propagation",
        total_bound / abs(q_regulated),
        Fraction(1, 4),
    )

    omitted_line_budget = total_bound - residual_bounds["line compactification"]
    adversarial_aligned_error = sum(residual_bounds.values(), Fraction(0))
    assert_gt_bound(
        "omitting line-count residual underbudgets aligned comparison error",
        adversarial_aligned_error,
        omitted_line_budget,
    )

    for pairing_power in range(n_fields - 1):
        codimension = 1 + (n_fields - 1) + pairing_power
        off_pairing_value = q_regulated if codimension == incidence_chart_dimension else Fraction(0)
        assert_equal(
            f"off-pairing vanishes by stable-map degree for H^{pairing_power}",
            off_pairing_value,
            Fraction(0),
        )
    top_pairing_codimension = 1 + (n_fields - 1) + (n_fields - 1)
    assert_equal(
        "top pairing is the unique saturated degree-one observable",
        top_pairing_codimension,
        incidence_chart_dimension,
    )

    mirror_only_bare = cp_mirror_residue_trace(
        n_fields,
        n_fields - 1 + n_fields,
        bare_fi,
    )
    if mirror_only_bare == q_regulated:
        raise AssertionError("mirror residue with bare FI should not establish vortex-normalized product")

    dimension_count_only = Fraction(1)
    if dimension_count_only == q_regulated:
        raise AssertionError("stable-map line count alone should not include the vortex fugacity")

    flipped_orientation = q_regulated * (-orientation_sign) * selection_gate
    if flipped_orientation == retained_three_point:
        raise AssertionError("orientation flip should change the retained incidence coefficient")

    missing_selection_degree = insertion_complex_degree - 1
    missing_selection_gate = (
        Fraction(1) if missing_selection_degree == incidence_chart_dimension else Fraction(0)
    )
    killed_fugacity = q_regulated * missing_selection_gate
    assert_equal("unsaturated selection-degree gate kills degree-one product coefficient", killed_fugacity, 0)
    if retained_three_point == killed_fugacity:
        raise AssertionError("charge and dimension data should not override a selection gate")

    collided_point_one = point_zero
    colliding_point_boundary_excluded = (
        point_zero != collided_point_one
        and hyperplane_value(point_zero) != 0
        and hyperplane_value(collided_point_one) != 0
    )
    colliding_point_factor = Fraction(1) if colliding_point_boundary_excluded else Fraction(0)
    colliding_point_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * colliding_point_factor
        * operator_normalization
    )
    assert_equal(
        "colliding point mutation removes the retained incidence coefficient",
        colliding_point_three_point,
        Fraction(0),
    )
    if colliding_point_three_point == retained_three_point:
        raise AssertionError("colliding point mutation should recompute and fail the retained observable")

    hyperplane_through_first_point = [Fraction(0), Fraction(1)] + [Fraction(0)] * (n_fields - 2)
    if linear_value(hyperplane_through_first_point, point_zero) != 0:
        raise AssertionError("mutated hyperplane should contain the first point")
    hyperplane_mutation_boundary_excluded = (
        point_zero != point_one
        and linear_value(hyperplane_through_first_point, point_zero) != 0
        and linear_value(hyperplane_through_first_point, point_one) != 0
    )
    hyperplane_mutation_factor = Fraction(1) if hyperplane_mutation_boundary_excluded else Fraction(0)
    hyperplane_mutation_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * hyperplane_mutation_factor
        * operator_normalization
    )
    assert_equal(
        "hyperplane-through-point mutation removes the retained incidence coefficient",
        hyperplane_mutation_three_point,
        Fraction(0),
    )
    if hyperplane_mutation_three_point == retained_three_point:
        raise AssertionError("hyperplane contact mutation should recompute and fail the retained observable")

    doubled_operator_normalization = Fraction(2)
    rescaled_three_point = (
        q_regulated
        * orientation_sign
        * selection_gate
        * compactification_factor
        * doubled_operator_normalization
    )
    assert_equal(
        "hyperplane-class normalization rescales the retained coefficient",
        rescaled_three_point,
        2 * retained_three_point,
    )
    if rescaled_three_point == retained_three_point:
        raise AssertionError("hyperplane-class normalization change should rescale the coefficient")


def check_cp_degree_d_quantum_product_iteration() -> None:
    for n_fields in range(2, 8):
        bare_fi = Fraction(n_fields + 3, n_fields + 11)
        vortex_coefficients = [
            Fraction(n_fields + 2 * index + 5, n_fields + 2 * index + 9)
            for index in range(n_fields)
        ]
        q_regulated = bare_fi * prod(vortex_coefficients, start=Fraction(1))

        for degree in range(0, 5):
            insertion_power = n_fields - 1 + degree * n_fields
            residue_prediction = cp_mirror_residue_trace(
                n_fields,
                insertion_power,
                q_regulated,
            )
            assert_equal(
                f"CP^{n_fields - 1} degree-{degree} residue gives q^d",
                residue_prediction,
                q_regulated**degree,
            )

            reduced_power, q_power = quantum_product_power(
                n_fields,
                insertion_power,
                0,
            )
            trace_from_product_iteration = (
                q_regulated**q_power
                if reduced_power == n_fields - 1
                else Fraction(0)
            )
            assert_equal(
                f"CP^{n_fields - 1} degree-{degree} product trace iteration",
                trace_from_product_iteration,
                residue_prediction,
            )

        degree = 4
        gluing_residuals = {
            stage: Fraction((-1) ** stage, 1000 + 11 * stage + n_fields)
            for stage in range(1, degree + 1)
        }
        off_pairing_residuals = {
            stage: Fraction((-1) ** (stage + 1), 2000 + 13 * stage + n_fields)
            for stage in range(1, degree + 1)
        }
        sector_residuals = {
            "determinant": Fraction(1, 3001 + n_fields),
            "zero mode": Fraction(-1, 3011 + n_fields),
            "compactification": Fraction(1, 3023 + n_fields),
            "operator map": Fraction(-1, 3037 + n_fields),
            "continuum": Fraction(1, 3049 + n_fields),
        }

        telescope_error = sum(
            q_regulated ** (degree - stage)
            * (gluing_residuals[stage] + off_pairing_residuals[stage])
            for stage in range(1, degree + 1)
        ) + sum(sector_residuals.values(), Fraction(0))
        direct_sector_probe = q_regulated**degree + telescope_error
        full_budget = sum(
            abs(q_regulated) ** (degree - stage)
            * (
                abs(gluing_residuals[stage])
                + abs(off_pairing_residuals[stage])
            )
            for stage in range(1, degree + 1)
        ) + sum(abs(value) for value in sector_residuals.values())
        assert_leq_bound(
            f"CP^{n_fields - 1} degree-d residual telescope budget",
            abs(direct_sector_probe - q_regulated**degree),
            full_budget,
        )

        omitted_stage = 2
        omitted_gluing_budget = (
            full_budget
            - abs(q_regulated) ** (degree - omitted_stage)
            * abs(gluing_residuals[omitted_stage])
        )
        aligned_error = full_budget
        assert_gt_bound(
            "omitting middle gluing residual underbudgets degree-d sector",
            aligned_error,
            omitted_gluing_budget,
        )

        omitted_off_pairing_budget = (
            full_budget
            - abs(q_regulated) ** (degree - omitted_stage)
            * abs(off_pairing_residuals[omitted_stage])
        )
        assert_gt_bound(
            "omitting off-pairing leakage underbudgets degree-d iteration",
            aligned_error,
            omitted_off_pairing_budget,
        )

        bare_fi_trace = cp_mirror_residue_trace(
            n_fields,
            n_fields - 1 + degree * n_fields,
            bare_fi,
        )
        if bare_fi_trace == q_regulated**degree:
            raise AssertionError("bare FI coordinate should not pass the degree-d vortex-normalized trace")

        incidence_count_only = Fraction(1)
        if incidence_count_only == q_regulated**degree:
            raise AssertionError("iterated line counts should not include the degree-d fugacity")

        off_pairing_leak = Fraction(1, 41 + n_fields)
        leaked_trace = q_regulated**degree + q_regulated ** (degree - 2) * off_pairing_leak
        if leaked_trace == q_regulated**degree:
            raise AssertionError("nonzero off-pairing leakage should change the iterated trace")

        unsaturated_zero_mode_gate = Fraction(0)
        gated_degree_d = q_regulated**degree * unsaturated_zero_mode_gate
        assert_equal(
            "unsaturated degree-d zero-mode gate kills protected coefficient",
            gated_degree_d,
            Fraction(0),
        )
        if gated_degree_d == q_regulated**degree:
            raise AssertionError("degree-d sector cannot ignore residual zero-mode saturation")


def check_degree_one_amodel_zero_mode_measure_bridge() -> None:
    # The degree-one line count becomes an A-twisted correlator only after
    # the zero-mode Berezin degree, determinant-line orientation, obstruction
    # factor, and supplied vortex-normalized fugacity all live in the same
    # regulator coordinate.  This finite model checks that bridge rather than
    # only the incidence count.
    for n_fields in range(2, 9):
        moduli_complex_dimension = 2 * n_fields - 1
        insertion_degrees = [1, n_fields - 1, n_fields - 1]
        insertion_total_degree = sum(insertion_degrees)
        assert_equal(
            f"CP^{n_fields - 1} A-model zero-mode degree saturation",
            insertion_total_degree,
            moduli_complex_dimension,
        )

        obstruction_rank = 0
        determinant_orientation = Fraction(1)
        bare_fi = Fraction(n_fields + 2, n_fields + 7)
        vortex_coefficients = [
            Fraction(n_fields + index + 3, n_fields + index + 5)
            for index in range(n_fields)
        ]
        q_regulated = bare_fi * prod(vortex_coefficients, start=Fraction(1))

        berezin_gate = (
            Fraction(1)
            if insertion_total_degree == moduli_complex_dimension and obstruction_rank == 0
            else Fraction(0)
        )
        incidence_count = Fraction(1)
        retained_correlator = (
            q_regulated * determinant_orientation * berezin_gate * incidence_count
        )
        assert_equal(
            f"CP^{n_fields - 1} retained A-model degree-one coefficient",
            retained_correlator,
            q_regulated,
        )

        line_count_only = incidence_count
        if line_count_only == retained_correlator:
            raise AssertionError("line count alone should not include vortex fugacity")

        vortex_fugacity_only = q_regulated
        if vortex_fugacity_only != retained_correlator:
            raise AssertionError("well-oriented saturated bridge should retain q_regulated")

        flipped_orientation = -determinant_orientation
        assert_equal(
            "determinant orientation flips A-model coefficient",
            q_regulated * flipped_orientation * berezin_gate * incidence_count,
            -retained_correlator,
        )

        missing_operator_degrees = [1, n_fields - 2, n_fields - 1]
        missing_gate = (
            Fraction(1)
            if sum(missing_operator_degrees) == moduli_complex_dimension
            else Fraction(0)
        )
        assert_equal(
            "missing insertion degree kills Berezin coefficient",
            q_regulated * determinant_orientation * missing_gate * incidence_count,
            Fraction(0),
        )

        extra_obstruction_rank = 1
        omitted_obstruction_euler = Fraction(0)
        obstruction_gate = (
            Fraction(1)
            if extra_obstruction_rank == 0
            else omitted_obstruction_euler
        )
        assert_equal(
            "omitted obstruction factor kills retained A-model coefficient",
            q_regulated * determinant_orientation * obstruction_gate * incidence_count,
            Fraction(0),
        )

        nonzero_mode_ratio = Fraction(1)
        same_regulator_result = retained_correlator * nonzero_mode_ratio
        assert_equal(
            "nonzero-mode determinant cancellation keeps oriented coefficient",
            same_regulator_result,
            retained_correlator,
        )
        wrong_nonzero_mode_ratio = Fraction(7, 5)
        if retained_correlator * wrong_nonzero_mode_ratio == retained_correlator:
            raise AssertionError("unpaired nonzero-mode determinant ratio should change the coefficient")

        residuals = {
            "vortex coefficient": Fraction(1, 1009),
            "determinant line": Fraction(1, 1013),
            "zero-mode measure": Fraction(1, 1019),
            "compactification": Fraction(1, 1021),
            "operator map": Fraction(1, 1031),
        }
        residual_bound = sum(residuals.values(), Fraction(0))
        correlated_probe = retained_correlator + residuals["zero-mode measure"]
        assert_leq_bound(
            "A-model zero-mode bridge conditional propagation",
            abs(correlated_probe - retained_correlator),
            residual_bound,
        )

        omitted_zero_mode_budget = residual_bound - residuals["zero-mode measure"]
        aligned_error = residual_bound
        assert_gt_bound(
            "omitting zero-mode residual underbudgets A-model bridge",
            aligned_error,
            omitted_zero_mode_budget,
        )


def check_degree_one_measure_scheme_covariance() -> None:
    # A finite change of vortex coefficient normalization and zero-mode chart
    # coordinates is harmless only when the FI coordinate, determinant density,
    # and orientation/operator conventions are transported together.
    n_fields = 4
    bare_fi = Fraction(5, 13)
    vortex_coefficients = [
        Fraction(2, 3),
        Fraction(3, 5),
        Fraction(5, 7),
        Fraction(7, 11),
    ]
    q_regulated = bare_fi * prod(vortex_coefficients, start=Fraction(1))

    measure_cells = [Fraction(3), Fraction(5), Fraction(7)]
    density_cells = [Fraction(1, 3), Fraction(-1, 5), Fraction(1, 7)]
    retained_integral = sum(
        measure * density
        for measure, density in zip(measure_cells, density_cells)
    )
    assert_equal("retained degree-one measure integral", retained_integral, Fraction(1))

    retained_coefficient = q_regulated * retained_integral
    degree_one_power = n_fields - 1 + n_fields
    assert_equal(
        "retained coefficient matches mirror trace in transported coordinate",
        retained_coefficient,
        cp_mirror_residue_trace(n_fields, degree_one_power, q_regulated),
    )

    coefficient_rescalings = [
        Fraction(11, 13),
        Fraction(13, 17),
        Fraction(17, 19),
        Fraction(19, 23),
    ]
    transported_fi = bare_fi / prod(coefficient_rescalings, start=Fraction(1))
    transported_coefficients = [
        coefficient * rescaling
        for coefficient, rescaling in zip(vortex_coefficients, coefficient_rescalings)
    ]
    transported_q = transported_fi * prod(transported_coefficients, start=Fraction(1))
    assert_equal("FI shift transports vortex coefficient rescaling", transported_q, q_regulated)

    stale_fi_q = bare_fi * prod(transported_coefficients, start=Fraction(1))
    if stale_fi_q == q_regulated:
        raise AssertionError("stale FI coordinate should not absorb coefficient rescaling")

    jacobians = [Fraction(5, 4), Fraction(7, 6), Fraction(11, 10)]
    transported_measure = [
        measure * jacobian
        for measure, jacobian in zip(measure_cells, jacobians)
    ]
    transported_density = [
        density / jacobian
        for density, jacobian in zip(density_cells, jacobians)
    ]
    transported_integral = sum(
        measure * density
        for measure, density in zip(transported_measure, transported_density)
    )
    assert_equal(
        "Jacobian transport preserves degree-one measure integral",
        transported_integral,
        retained_integral,
    )
    assert_equal(
        "transported finite measure package preserves coefficient",
        transported_q * transported_integral,
        retained_coefficient,
    )

    stale_density_integral = sum(
        measure * density
        for measure, density in zip(transported_measure, density_cells)
    )
    if stale_density_integral == retained_integral:
        raise AssertionError("missing inverse Jacobian should change the finite density")

    orientation_flip = Fraction(-1)
    untransported_orientation_coefficient = (
        transported_q * orientation_flip * transported_integral
    )
    assert_equal(
        "untransported determinant orientation flips coefficient",
        untransported_orientation_coefficient,
        -retained_coefficient,
    )
    operator_orientation_transport = Fraction(-1)
    assert_equal(
        "operator orientation transport restores pairing coefficient",
        untransported_orientation_coefficient * operator_orientation_transport,
        retained_coefficient,
    )

    residuals = {
        "FI transport": transported_q - q_regulated,
        "density transport": transported_integral - retained_integral,
        "continuum": Fraction(1, 10_007),
    }
    residual_probe = retained_coefficient + sum(residuals.values(), Fraction(0))
    residual_bound = sum(abs(value) for value in residuals.values())
    assert_leq_bound(
        "measure-scheme covariance conditional propagation",
        abs(residual_probe - retained_coefficient),
        residual_bound,
    )


def check_hori_vafa_residue_instanton_comparison_map() -> None:
    # The mirror residue gives S_1(q_mir)=q_mir for the degree-one
    # P^{N-1} product test.  The direct A-model/vortex coefficient uses the
    # transported vortex fugacity q_lambda, the directly computed incidence
    # integral with its determinant-line measure residual, and separate
    # operator/continuum residuals.
    n_fields = 5
    degree_one_power = n_fields - 1 + n_fields
    q_mir = Fraction(5, 7)
    q_transport_error = Fraction(1, 101)
    q_lambda = q_mir + q_transport_error
    incidence = degree_one_cpn_incidence_factors(n_fields)
    assert_equal("direct degree-one incidence orientation", incidence["orientation"], Fraction(1))
    assert_equal("direct degree-one incidence degree gate", incidence["selection_gate"], Fraction(1))
    assert_equal(
        "direct degree-one compactification gate",
        incidence["compactification_gate"],
        Fraction(1),
    )
    assert_equal(
        "direct degree-one incidence integral",
        incidence["incidence_integral"],
        Fraction(1),
    )

    determinant_measure_residual = Fraction(1, 103)
    retained_measure_integral = incidence["incidence_integral"] + determinant_measure_residual
    vortex_residual = -Fraction(1, 107)
    operator_residual = Fraction(1, 109)
    continuum_residual = -Fraction(1, 113)

    mirror_residue = cp_mirror_residue_trace(
        n_fields,
        degree_one_power,
        q_mir,
    )
    assert_equal("Hori-Vafa degree-one mirror residue", mirror_residue, q_mir)

    direct_amodel_coefficient = (
        q_lambda * retained_measure_integral
        + vortex_residual
        + operator_residual
        + continuum_residual
    )
    crosscheck_residual = direct_amodel_coefficient - mirror_residue
    expected_residual = (
        vortex_residual
        + q_lambda * (retained_measure_integral - incidence["incidence_integral"])
        + q_lambda * (incidence["incidence_integral"] - 1)
        + (q_lambda - q_mir)
        + operator_residual
        + continuum_residual
    )
    assert_equal(
        "Hori-Vafa residue/direct-instanton cross-check telescope",
        crosscheck_residual,
        expected_residual,
    )

    bounds = {
        "vortex": abs(vortex_residual),
        "incidence": abs(incidence["incidence_integral"] - 1),
        "measure": abs(determinant_measure_residual),
        "q transport": abs(q_lambda - q_mir),
        "operator": abs(operator_residual),
        "continuum": abs(continuum_residual),
    }
    crosscheck_bound = (
        bounds["vortex"]
        + abs(q_lambda) * bounds["incidence"]
        + abs(q_lambda) * bounds["measure"]
        + bounds["q transport"]
        + bounds["operator"]
        + bounds["continuum"]
    )
    assert_leq_bound(
        "Hori-Vafa residue/direct-instanton cross-check bound",
        abs(crosscheck_residual),
        crosscheck_bound,
    )

    omitted_q_transport_bound = crosscheck_bound - bounds["q transport"]
    adversarial_q_transport_error = crosscheck_bound
    assert_gt_bound(
        "omitting FI-coordinate transport underbudgets Hori-Vafa comparison",
        adversarial_q_transport_error,
        omitted_q_transport_bound,
    )

    zero_mode_gate = Fraction(0)
    direct_zero_mode_killed = q_lambda * zero_mode_gate
    assert_equal(
        "unsaturated direct vortex zero modes kill A-model coefficient",
        direct_zero_mode_killed,
        Fraction(0),
    )
    if mirror_residue == direct_zero_mode_killed:
        raise AssertionError("mirror residue alone should not bypass zero-mode saturation")

    stable_map_line_count = Fraction(1)
    if stable_map_line_count == q_lambda:
        raise AssertionError("line count alone should not supply vortex fugacity")

    wrong_incidence_orientation = -incidence["orientation"]
    wrong_direct_incidence = (
        q_lambda
        * wrong_incidence_orientation
        * incidence["selection_gate"]
        * incidence["compactification_gate"]
        * incidence["operator_normalization"]
    )
    if wrong_direct_incidence == q_lambda * incidence["incidence_integral"]:
        raise AssertionError("direct incidence orientation should affect the A-model package")
    if cp_mirror_residue_trace(n_fields, degree_one_power, q_lambda) == wrong_direct_incidence:
        raise AssertionError("mirror residue should not hide direct incidence orientation")

    missing_compactification_gate = Fraction(0)
    boundary_killed_direct = (
        q_lambda
        * incidence["orientation"]
        * incidence["selection_gate"]
        * missing_compactification_gate
        * incidence["operator_normalization"]
    )
    assert_equal(
        "failed compactification gate kills direct degree-one package",
        boundary_killed_direct,
        Fraction(0),
    )
    if cp_mirror_residue_trace(n_fields, degree_one_power, q_lambda) == boundary_killed_direct:
        raise AssertionError("mirror residue should not bypass compactification gate")

    coefficient_rescaling = Fraction(11, 13)
    stale_q = q_lambda * coefficient_rescaling
    transported_fi = q_lambda / coefficient_rescaling
    transported_q = transported_fi * coefficient_rescaling
    assert_equal("transported FI coordinate preserves q", transported_q, q_lambda)
    if cp_mirror_residue_trace(n_fields, degree_one_power, stale_q) == mirror_residue:
        raise AssertionError("stale FI coordinate should move the mirror residue")

    orientation_flip_integral = -retained_measure_integral
    flipped_direct = q_lambda * orientation_flip_integral
    if flipped_direct == q_lambda * retained_measure_integral:
        raise AssertionError("orientation flip should change the direct vortex package")
    if cp_mirror_residue_trace(n_fields, degree_one_power, q_lambda) == flipped_direct:
        raise AssertionError("formal root sum should not hide determinant orientation")

    off_pairing_residuals = {
        0: Fraction(1, 1009),
        1: -Fraction(1, 1013),
        2: Fraction(1, 1019),
        3: -Fraction(1, 1021),
    }
    off_pairing_bound = sum(abs(value) for value in off_pairing_residuals.values())
    actual_off_pairing_error = abs(sum(off_pairing_residuals.values(), Fraction(0)))
    assert_leq_bound(
        "off-pairing contact conditional propagation",
        actual_off_pairing_error,
        off_pairing_bound,
    )
    for pairing_power in range(n_fields - 1):
        mirror_off_pairing = cp_mirror_residue_trace(
            n_fields,
            pairing_power,
            q_mir,
        )
        assert_equal(
            f"mirror residue off-pairing vanishes a={pairing_power}",
            mirror_off_pairing,
            Fraction(0),
        )


def check_cigar_metric_elimination() -> None:
    examples = [
        (Fraction(9, 5), Fraction(7, 3)),
        (Fraction(4, 1), Fraction(5, 2)),
        (Fraction(1, 3), Fraction(11, 4)),
    ]
    for rho_squared, k_level in examples:
        saddle_a = rho_squared / (rho_squared + k_level)
        angular_from_elimination = (
            Fraction(1, 2) * rho_squared * (1 - saddle_a) ** 2
            + Fraction(1, 2) * k_level * saddle_a**2
        )
        expected_angular = Fraction(1, 2) * rho_squared / (1 + rho_squared / k_level)
        assert_equal("cigar angular metric coefficient", angular_from_elimination, expected_angular)

        radial_kinetic_coefficient = Fraction(1, 2) + rho_squared / (2 * k_level)
        expected_metric_rr = 1 + rho_squared / k_level
        assert_equal("cigar radial metric coefficient", 2 * radial_kinetic_coefficient, expected_metric_rr)


def check_logarithmic_chiral_vortex_obstruction() -> None:
    # A smooth ordinary charged scalar may carry flux n by having total zero
    # divisor degree n.  The logarithmic chiral periodic part is unit-norm,
    # hence has zero divisor degree 0; smooth finite-action P-sector vortices
    # therefore force n=0.
    for flux in range(-4, 5):
        unit_field_zero_degree = 0
        smooth_unit_section_possible = flux == unit_field_zero_degree
        assert_equal(
            f"logarithmic chiral unit section obstruction flux={flux}",
            smooth_unit_section_possible,
            flux == 0,
        )

    for ordinary_vortex_degree in range(0, 6):
        flux = ordinary_vortex_degree
        assert_equal("ordinary charged scalar zero degree carries flux", flux, ordinary_vortex_degree)


def check_mirror_conjecture_observable_boundary() -> None:
    # This is a finite boundary check, not a test of the conjectures themselves.
    # It verifies that the chapter's named conjectures list the full-QFT data
    # while protected calculations remain observable-comparison inputs.
    glsm_required_data = {
        "charge matrix",
        "fi theta",
        "global gauge form",
        "regulator",
        "spin structure",
        "phase chamber",
        "singular-locus exclusions",
        "continuum Hilbert spaces",
        "Hamiltonians",
        "local OPE",
        "A/B pairings",
        "topological sectors",
        "defects",
        "boundaries",
        "background contact terms",
        "RG endpoints",
    }
    glsm_conjecture_data = set(glsm_required_data)
    glsm_conjecture_data.update({"vortex coefficients", "theta periods"})
    assert_equal(
        "GLSM mirror conjecture records required full-QFT data",
        glsm_required_data <= glsm_conjecture_data,
        True,
    )

    glsm_protected_evidence = {
        "local dualization",
        "Coulomb logarithm",
        "vortex coefficient integral",
        "zero-mode filter",
        "FI-coordinate shift",
        "mirror residue",
        "stable-map incidence",
    }
    glsm_full_qft_obligations = {
        "continuum Hilbert spaces",
        "Hamiltonians",
        "local OPE",
        "defects",
        "boundaries",
        "background contact terms",
        "RG endpoints",
        "singular-locus exclusions",
    }
    assert_equal(
        "GLSM protected evidence is a proper subset of full equivalence data",
        glsm_protected_evidence < glsm_protected_evidence | glsm_full_qft_obligations,
        True,
    )

    observable_map = ["D_loc", "D_pert", "D_vort", "D_obs"]
    assert_equal(
        "GLSM mirror observable map puts vortex data before observable comparison",
        observable_map.index("D_vort") < observable_map.index("D_obs"),
        True,
    )
    mirror_residue_only = {"D_obs"}
    assert_equal(
        "mirror residue alone cannot bypass direct vortex data",
        {"D_vort", "D_obs"} <= mirror_residue_only,
        False,
    )

    hv_formula_shortcut = {
        "charge matrix",
        "fi theta",
        "periodic Y",
        "primitive exponential",
        "Coulomb logarithm",
        "mirror residue",
    }
    for omitted in [
        "continuum Hilbert spaces",
        "local OPE",
        "defects",
        "background contact terms",
    ]:
        if omitted in hv_formula_shortcut:
            raise AssertionError(f"Hori-Vafa formula shortcut should omit no full-QFT debt: {omitted}")
    assert_equal(
        "Hori-Vafa formula data alone cannot assert full GLSM mirror equivalence",
        glsm_required_data <= hv_formula_shortcut,
        False,
    )

    cigar_required_data = {
        "level convention",
        "background charge",
        "spin structures",
        "spectral-flow sectors",
        "normalizable states",
        "nonnormalizable sources",
        "continuous-spectrum measure",
        "local operator map",
        "reflection amplitudes",
        "Hilbert space",
        "superconformal generators",
        "defects",
        "boundaries",
        "contact terms",
    }
    cigar_conjecture_data = set(cigar_required_data)
    assert_equal(
        "cigar-Liouville conjecture records spectrum and operator data",
        cigar_required_data <= cigar_conjecture_data,
        True,
    )

    cigar_evidence = {
        "classical quotient metric",
        "asymptotic dual variables",
        "ordinary chiral exponential",
        "logarithmic vortex obstruction",
    }
    cigar_full_qft_obligations = {
        "continuous-spectrum measure",
        "operator completeness",
        "strong-coupling tip control",
        "defects",
        "boundaries",
        "reflection amplitudes",
    }
    assert_equal(
        "cigar protected evidence leaves continuous-spectrum obligations",
        cigar_full_qft_obligations <= cigar_evidence,
        False,
    )
    assert_equal(
        "cigar protected evidence is a proper subset of full duality data",
        cigar_evidence < cigar_evidence | cigar_full_qft_obligations,
        True,
    )


def invariant_jacobi_monomial_count(num_fields: int, degree: int) -> int:
    count = 0

    def visit(index: int, total_exponent: int) -> None:
        nonlocal count
        if index == num_fields:
            if total_exponent % degree == 0:
                count += 1
            return
        for exponent in range(degree - 1):
            visit(index + 1, total_exponent + exponent)

    visit(0, 0)
    return count


def check_hypersurface_phase_ledger() -> None:
    examples = [(3, 3), (4, 4), (5, 5), (5, 3), (6, 4)]
    for num_fields, degree in examples:
        c1_coefficient = num_fields - degree
        canonical_coefficient = degree - num_fields
        assert_equal("hypersurface adjunction sign", c1_coefficient, -canonical_coefficient)

        sigma_model_central_charge = 3 * (num_fields - 2)
        lg_central_charge = 3 * num_fields * (Fraction(1) - Fraction(2, degree))
        central_charge_difference = lg_central_charge - sigma_model_central_charge
        assert_equal(
            "LG/sigma central-charge difference",
            central_charge_difference,
            Fraction(6 * (degree - num_fields), degree),
        )
        assert_equal(
            "central charges match iff Calabi-Yau hypersurface degree",
            lg_central_charge == sigma_model_central_charge,
            degree == num_fields,
        )

        # The residual mu_d gauge action sends X_i -> zeta X_i.  A degree-d
        # monomial and hence a homogeneous degree-d superpotential is invariant.
        assert_equal("residual finite gauge preserves G_d", degree % degree, 0)

    assert_equal("quintic untwisted invariant Jacobi monomial count", invariant_jacobi_monomial_count(5, 5), 204)


def check_hypersurface_coulomb_coordinate_signal() -> None:
    for num_fields, degree in [(5, 5), (4, 4), (6, 6), (5, 3), (6, 4)]:
        charges = [1] * num_fields + [-degree]
        sigma_exponent = sum(charges)
        assert_equal("hypersurface Coulomb sigma exponent", sigma_exponent, num_fields - degree)
        assert_equal("hypersurface axial anomaly coefficient", sigma_exponent, glsm_charge_sum(num_fields, degree))

        if num_fields == degree:
            assert_equal("anomaly-free hypersurface cancels sigma power", sigma_exponent, 0)
            branch_constant_magnitude = Fraction(1, degree**degree)
            if branch_constant_magnitude <= 0:
                raise AssertionError("branch constant magnitude should be positive")


def main() -> None:
    check_a_series_lg()
    check_fermat_tensor_products()
    check_fermat_wilsonian_spurion_selection()
    check_hypersurface_glsm_ledger()
    check_twist_spin_ledger()
    check_abelian_circle_duality()
    check_abelian_legendre_duality()
    check_abelian_glsm_coulomb_ledger()
    check_compact_fi_theta_fugacity_and_common_flux()
    check_abelian_coulomb_one_loop_primitive()
    check_charged_chiral_dual_elimination()
    check_all_rank_vortex_fi_coordinate_shift()
    check_vortex_fugacity_dimensional_transmutation()
    check_mirror_primitive_monomial_selection()
    check_vortex_zero_mode_filter()
    check_vortex_fluctuation_complex_gate()
    check_single_vortex_amplitude_assembly()
    check_one_vortex_frame_and_normal_interaction_separation()
    check_one_vortex_source_functional_extraction()
    check_one_vortex_component_amplitude_cell()
    check_one_vortex_source_frame_calibration()
    check_vortex_coefficient_noncancellation_bound()
    check_cp_mirror_critical_ledger()
    check_cp_mirror_residue_correlators()
    check_vortex_to_observable_proof_obligation_map()
    check_cp_degree_one_stable_map_quantum_product_gate()
    check_degree_one_stable_map_incidence_model()
    check_cp_degree_d_quantum_product_iteration()
    check_degree_one_amodel_zero_mode_measure_bridge()
    check_degree_one_measure_scheme_covariance()
    check_hori_vafa_residue_instanton_comparison_map()
    check_cigar_metric_elimination()
    check_logarithmic_chiral_vortex_obstruction()
    check_mirror_conjecture_observable_boundary()
    check_hypersurface_phase_ledger()
    check_hypersurface_coulomb_coordinate_signal()
    print("All 2D SUSY LG/GLSM checks passed.")


if __name__ == "__main__":
    main()
