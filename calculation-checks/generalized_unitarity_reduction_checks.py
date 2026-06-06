#!/usr/bin/env python3
"""Finite checks for generalized unitarity and loop reduction.

The companion section in Volume II, Chapter 6 develops the bridge from
Cutkosky discontinuities to generalized cuts, scalar-integral reconstruction,
IBP reduction, and master-integral differential equations.  This script
checks the exact algebraic structure behind the one-loop reconstruction package,
the worked massless phi^4 example including the cut-invisible MS pole and
one-loop running, the finite two-scale box master, and the one-loop bubble
family, including numerator sector projection and the
equal-mass threshold family with its lower tadpole master and branch, the
two-loop equal-mass sunrise maximal-cut curve with its elliptic discriminant
and physical threshold, a multi-loop maximal-cut/contact-sector projection
gate, a dual-contour master-coefficient extraction gate, and finite helicity,
color, state-sum, and regulator bookkeeping for the
Yang-Mills MHV/all-plus control examples, including the planar N=4 MHV
quadruple-cut reconstruction, the five-gluon all-plus rational template, and
the four-point color-kinematics/double-copy gateway together with the
one-loop surface-term obstruction to naive double copy and the local
Jacobi-repair condition under which a common color-null surface direction is
also a double-copy null direction against a Jacobi-satisfying second copy.
It also checks a
finite triple-cut triangle projection after known box residues have been
subtracted, a finite two-master threshold-mixing model, a two-letter
master-transport model with boundary and branch negative controls, a physical
master-discontinuity closure gate comparing transported master jumps with
Cutkosky channel data, including a separate two-particle phase-space
state-sum computation for the scalar bubble, the finite
Laurent-pole bookkeeping that turns a reconstructed virtual amplitude into a finite
observable only after infrared subtraction, real radiation, scheme transport,
and the unresolved measurement cell have been assembled, and the two-loop
infrared-pole consistency gate relating
`A^(2)`, `I^(1) A^(1)`, `I^(2) A^(0)`, and the NNLO finite
observable.

Evidence contract.
Target claims: the generalized-unitarity section of Volume II Chapter 6,
especially the phi^4 cut reconstruction, the negative controls for incomplete
cut sets, the MS pole/running extraction from the crossing-complete scalar
amplitude, and four-dimensional blind spots, the bubble IBP identity, and the
bubble numerator-reduction sector projection and bubble master differential
equation, the equal-mass bubble threshold family, plus the finite two-scale
massless box master, the two-loop equal-mass sunrise elliptic maximal-cut
data, the gauge-theory MHV
box and all-plus rational-term comparison, the planar N=4 MHV quadruple-cut
state-sum accounting, the local two-master
threshold-mixing datum in a Fuchsian differential system, the two-letter
transport/boundary audit for a reduced master sector, and the
physical channel-discontinuity closure audit before the
virtual-to-observable finite remainder assembly; additionally, the five-point
all-plus rational amplitude has the correct little-group weights, mass
dimension, cyclic term coverage, and strict four-dimensional cut
invisibility, and the four-point color-kinematics gateway separates
gauge-amplitude equivalence from Jacobi-compatible numerator data needed for
the double copy, and a one-loop Jacobi triplet surface term can be invisible
to cuts and color-weighted gauge integration while changing a naive
double-copy pairing, while a common Jacobi-repair direction is double-copy
null only when the second numerator copy is Jacobi-satisfying, and the
triple-cut triangle projection isolates the triangle coefficient only after
known box residues have been subtracted.  The
one-loop reconstruction package is checked as an ordered
data package separating cuts, representative choice, rational/regulator data,
reduction, boundary/branch data, subtraction, and observable assembly.
Independent construction: finite cut-signature matrices over rational
numbers, a finite ordered gate/incidence model for the reconstruction package,
an explicit identical-state symmetry factor, a nullspace model for
local/rational terms invisible to four-dimensional cuts, exact rational
pole-residue and beta-function coefficient bookkeeping for the scalar
subtraction step, and exact rational
checks of the one-loop bubble IBP coefficients at several regulator values;
exact rational projection of a bubble numerator into parent and lower sectors,
including the parent-cut coefficient and vector Passarino-Veltman reduction;
exact small-momentum series checks for the equal-mass bubble threshold master,
including its lower-tadpole inhomogeneity and timelike branch interval;
quartic-discriminant and Landau-stationarity checks for the equal-mass sunrise
maximal cut, including the distinction between the physical threshold and the
pseudo-threshold;
exact rational projection of parent-topology contact terms into lower sectors
after propagator cancellation and before IBP master projection;
exact finite inversion of a contour/master pairing matrix, with surface and
lower-sector pollution subtracted before coefficient extraction;
exact finite matching of a physical Cutkosky channel datum computed from the
state sum and phase-space normalization against extracted coefficients times
transported master discontinuities, plus lower-sector and subtraction jumps;
spinor-bracket exponent ledgers for little-group weights and dimensions; and
a finite four-gluon helicity enumeration for all-plus two-particle cuts;
finite topology-signature checks for maximal versus two-particle cuts in the
N=4 MHV box reconstruction and a finite on-shell-supermultiplet state count;
Laurent-polynomial arithmetic for triple-cut triangle projection after
known box subtraction, including contour-average and partial-subtraction
negative controls;
finite spinor-bracket power counting and helicity-cut enumeration for the
five-gluon all-plus rational template;
exact Laurent bookkeeping for the dimension-shifted mu_perp^4 box residue,
including the three-simplex pole, strict four-dimensional cut blindness, and
massive-scalar coefficient extraction;
finite cubic-channel color/numerator algebra for the four-point
color-kinematics gateway, a finite loop-Jacobi triplet surface-term model, and
a finite common-repair model for loop-level double-copy null directions;
nilpotent rational matrix algebra for threshold monodromy and regular
boundary constants; noncommuting two-letter residue algebra for first-order
transport, path-order sensitivity, and cut-invisible boundary shifts;
fixed-normalization finite box checks, including pole-subtraction
bookkeeping, polynomial log algebra, branch continuation, a sector-boundary
quadrature, and a numerical dilogarithm-parameter integral independent of the
encoded log-square answer; Laurent-pole arithmetic for virtual/real infrared
cancellation, plus-distribution measurement cells, finite scheme transport, and
two-loop recursive pole subtraction.
Imported assumptions: dimensional regularization, the standard massless
two-particle phase-space normalization with the common factor of pi stripped
off, the Feynman-parameter gamma-function form of the bubble master, and the
vanishing of scaleless tadpoles in dimensional regularization; the
four-dimensional Yang-Mills tree selection rule that nonzero four-gluon trees
have two negative helicities, up to parity.
Negative controls: the script rejects an s-channel-only ansatz, verifies that
local counterterms are invisible to cuts, and constructs two amplitudes with
identical four-dimensional cuts but different D-dimensional rational probes;
it rejects the one-channel scalar pole/beta shortcut and a cut-only attempt to
fix finite subtraction constants;
it also verifies that the all-plus one-loop rational structure is invisible
to strict four-dimensional two-particle cuts but visible to a nonzero
mu_perp^2 massive-scalar probe, verifies that an s-channel cut alone cannot
separate the N=4 MHV box from lower-topology contamination and that a
gluon-only state sum is not the N=4 supermultiplet, verifies the same
rational blind spot at five points, verifies that a gauge-equivalent
non-Jacobi numerator shift changes the naive numerator square, verifies that a
dimension-shifted mu_perp^4 numerator is missed by strict four-dimensional cuts
but leaves the finite rational residue read by massive unitarity, verifies that a
cut-invisible surface/contact shift can leave the gauge amplitude unchanged
while breaking loop-level numerator Jacobi and changing the naive double-copy
pairing, verifies that a common Jacobi repair is not double-copy null against
a defective second copy and that sampled cuts do not prove the full Jacobi
defect is absent, verifies that the raw triple-cut constant can mix a triangle
coefficient with constant parts of known box residues and that omitting one
box subtraction leaves a wrong triangle coefficient, and rejects virtual-only
pole cancellation,
omitted rational finite
remainders, one-cut-only finite-box deformations, missing finite-box boundary
data, branch-label omission,
diagonal one-master threshold shortcuts, cut-only boundary reconstruction,
parent-cut-only sector projection when lower sectors are not scaleless,
non-dual or surface-polluted contour coefficient extraction,
raw-contour, Euclidean-value, wrong-sheet, and omitted-lower-sector shortcuts
in physical master-discontinuity closure,
and rejects defining the physical cut by the reconstructed discontinuity
instead of by the state sum,
homogeneous one-master shortcuts for the equal-mass bubble threshold family,
Euclidean branch reuse above the massive two-particle threshold,
logarithmic one-master shortcuts for the sunrise elliptic maximal cut,
maximal-cut-only multi-loop reconstruction when lower sectors carry scale,
branch/path omission in a two-letter master transport, virtual-only
observable assembly, untransported finite IR-scheme shifts, wrong unresolved
subtraction measurements, frozen locally inclusive measurement shortcuts,
non-infrared-safe logarithmic weights, two-loop remainder extraction that drops
`I^(1) A^(1)`, and NNLO observable assembly that omits the `|F^(1)|^2` hard
term.
Scope boundary: a pass checks the finite reconstruction and reduction
bookkeeping; it does not compute a nonabelian helicity amplitude from Feynman
graphs, prove unitarity from Wightman axioms, solve general multi-loop
integral families, prove loop-level color-kinematics duality, or replace the
real-radiation/factorization construction needed for infrared-safe
observables.
"""

from __future__ import annotations

import math
from fractions import Fraction


def assert_equal(name: str, value: object, expected: object) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name}: condition failed")


def assert_false(name: str, condition: bool) -> None:
    if condition:
        raise AssertionError(f"{name}: unexpectedly true")


def assert_close_float(name: str, value: float, expected: float, tol: float = 1.0e-10) -> None:
    if not math.isfinite(value) or not math.isfinite(expected) or not math.isfinite(tol):
        raise AssertionError(f"{name}: non-finite numerical comparison")
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value:.16g}, expected {expected:.16g}")


def simpson_integral(function, lower: float, upper: float, panels: int) -> float:
    if panels % 2:
        raise ValueError("Simpson integration needs an even number of panels")
    step = (upper - lower) / panels
    total = function(lower) + function(upper)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(lower + index * step)
    return total * step / 3.0


def real_dilog_from_parameter_integral(z: float) -> float:
    # Li_2(z) = - int_0^1 log(1-z x) dx/x on the real interval used below.
    def integrand(x: float) -> float:
        if x == 0.0:
            return z
        return -math.log1p(-z * x) / x

    return simpson_integral(integrand, 0.0, 1.0, 20000)


def rank(matrix: list[list[Fraction]]) -> int:
    """Row rank over the rationals."""
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    pivot_row = 0
    for col in range(n_cols):
        pivot = None
        for row in range(pivot_row, n_rows):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row:
                continue
            factor = rows[row][col]
            if factor:
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


def quartic_discriminant(
    coeffs: tuple[Fraction, Fraction, Fraction, Fraction, Fraction],
) -> Fraction:
    a, b, c, d, e = coeffs
    return (
        256 * a**3 * e**3
        - 192 * a**2 * b * d * e**2
        - 128 * a**2 * c**2 * e**2
        + 144 * a**2 * c * d**2 * e
        - 27 * a**2 * d**4
        + 144 * a * b**2 * c * e**2
        - 6 * a * b**2 * d**2 * e
        - 80 * a * b * c**2 * d * e
        + 18 * a * b * c * d**3
        + 16 * a * c**4 * e
        - 4 * a * c**3 * d**2
        - 27 * b**4 * e**2
        + 18 * b**3 * c * d * e
        - 4 * b**3 * d**3
        - 4 * b**2 * c**3 * e
        + b**2 * c**2 * d**2
    )


CHANNELS = ("s", "t", "u")
BASIS = ("B_s", "B_t", "B_u", "local", "four_dimensional_rational_null")
BracketPowers = dict[tuple[int, int], int]
Laurent = tuple[Fraction, Fraction]
Laurent3 = tuple[Fraction, Fraction, Fraction]
Matrix = list[list[Fraction]]
Vector = list[Fraction]
LogPolynomial = dict[tuple[int, int], Fraction]


def clean_poly(poly: LogPolynomial) -> LogPolynomial:
    return {powers: coeff for powers, coeff in poly.items() if coeff}


def poly_add(left: LogPolynomial, right: LogPolynomial) -> LogPolynomial:
    result = dict(left)
    for powers, coeff in right.items():
        result[powers] = result.get(powers, Fraction(0)) + coeff
    return clean_poly(result)


def poly_scale(scale: Fraction, poly: LogPolynomial) -> LogPolynomial:
    return clean_poly({powers: scale * coeff for powers, coeff in poly.items()})


def poly_derivative(poly: LogPolynomial, variable: int) -> LogPolynomial:
    result: LogPolynomial = {}
    for powers, coeff in poly.items():
        power = powers[variable]
        if power == 0:
            continue
        new_powers = list(powers)
        new_powers[variable] -= 1
        new_key = (new_powers[0], new_powers[1])
        result[new_key] = result.get(new_key, Fraction(0)) + coeff * power
    return clean_poly(result)


def laurent_add(left: Laurent, right: Laurent) -> Laurent:
    return (left[0] + right[0], left[1] + right[1])


def laurent_sub(left: Laurent, right: Laurent) -> Laurent:
    return (left[0] - right[0], left[1] - right[1])


def laurent_scale(scale: Fraction, value: Laurent) -> Laurent:
    return (scale * value[0], scale * value[1])


def laurent3_add(left: Laurent3, right: Laurent3) -> Laurent3:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def laurent3_sub(left: Laurent3, right: Laurent3) -> Laurent3:
    return (left[0] - right[0], left[1] - right[1], left[2] - right[2])


def laurent3_scale(scale: Fraction, value: Laurent3) -> Laurent3:
    return (scale * value[0], scale * value[1], scale * value[2])


def laurent_to_laurent3(value: Laurent) -> Laurent3:
    return (Fraction(0), value[0], value[1])


def laurent_product_to_laurent3(left: Laurent, right: Laurent) -> Laurent3:
    return (
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[1] * right[1],
    )


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[row][k] * right[k][col] for k in range(len(right)))
            for col in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][col] - right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def matrix_vector_mul(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum(row[col] * vector[col] for col in range(len(vector)))
        for row in matrix
    ]


def vector_add(left: Vector, right: Vector) -> Vector:
    return [left[index] + right[index] for index in range(len(left))]


def vector_sub(left: Vector, right: Vector) -> Vector:
    return [left[index] - right[index] for index in range(len(left))]


def vector_scale(scale: Fraction, vector: Vector) -> Vector:
    return [scale * entry for entry in vector]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(left[index] * right[index] for index in range(len(left)))


def four_dimensional_cut_signature(basis_name: str) -> tuple[Fraction, Fraction, Fraction]:
    if basis_name == "B_s":
        return (Fraction(1), Fraction(0), Fraction(0))
    if basis_name == "B_t":
        return (Fraction(0), Fraction(1), Fraction(0))
    if basis_name == "B_u":
        return (Fraction(0), Fraction(0), Fraction(1))
    if basis_name in {"local", "four_dimensional_rational_null"}:
        return (Fraction(0), Fraction(0), Fraction(0))
    raise ValueError(basis_name)


def channel_cuts(coefficients: dict[str, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    cuts = [Fraction(0), Fraction(0), Fraction(0)]
    for basis_name, coefficient in coefficients.items():
        signature = four_dimensional_cut_signature(basis_name)
        for index, value in enumerate(signature):
            cuts[index] += coefficient * value
    return tuple(cuts)


def massless_two_body_phase_space_times_pi() -> Fraction:
    """Return pi * integral dPhi_2 for two ordered massless particles in D=4."""

    # In the center-of-mass frame,
    #   dPhi_2 = (2pi)^4/(2pi)^6 * int d^3k/(4|k|^2)
    #            delta(sqrt{s} - 2|k|)
    #          = 1/(4pi^2) * pi * 1/2 = 1/(8pi).
    # Multiplying by pi leaves the exact rational coefficient used below.
    prefactor_after_angular_integration = Fraction(1, 4)
    energy_delta_jacobian = Fraction(1, 2)
    return prefactor_after_angular_integration * energy_delta_jacobian


def check_phi4_cut_reconstruction() -> None:
    lam = Fraction(5, 3)
    tree = -lam
    identical_state_factor = Fraction(1, 2)

    # Strip the common i/(8 pi) factor from the massless two-body phase-space
    # discontinuity.  The cut-normalized bubble has unit signature in these
    # units, so the coefficient is read directly.
    assert_equal(
        "massless two-body phase-space normalization",
        massless_two_body_phase_space_times_pi(),
        Fraction(1, 8),
    )
    expected_channel_cut = identical_state_factor * tree * tree
    expected_coeff = lam * lam / 2
    assert_equal("identical-state cut coefficient", expected_channel_cut, expected_coeff)

    reconstructed = {"B_s": expected_coeff, "B_t": expected_coeff, "B_u": expected_coeff}
    expected_cuts = (expected_coeff, expected_coeff, expected_coeff)
    assert_equal("all channel cuts reconstructed", channel_cuts(reconstructed), expected_cuts)

    s_only = {"B_s": expected_coeff}
    assert_equal("s-only ansatz matches s cut", channel_cuts(s_only)[0], expected_coeff)
    assert_equal("s-only ansatz misses t cut", channel_cuts(s_only)[1], Fraction(0))
    assert_false("s-only ansatz is crossing complete", channel_cuts(s_only) == expected_cuts)

    with_local_counterterm = dict(reconstructed)
    with_local_counterterm["local"] = Fraction(17, 11)
    assert_equal(
        "local counterterm has no discontinuity",
        channel_cuts(with_local_counterterm),
        expected_cuts,
    )

    cut_matrix = [
        list(four_dimensional_cut_signature(basis_name))
        for basis_name in BASIS
    ]
    assert_equal("four-dimensional cut rank", rank(cut_matrix), 3)
    assert_true("cut map has local/rational nullspace", len(BASIS) - rank(cut_matrix) == 2)


def check_phi4_ms_running_from_crossed_cuts() -> None:
    # Strip the common factor 1/(16 pi^2).  Each channel contributes
    # (lambda^2/2) * B, and in D=4-2 epsilon the one-loop beta coefficient is
    # twice the simple-pole residue.
    lam = Fraction(5, 3)
    channel_count = Fraction(3)
    bubble_coefficient = lam * lam / 2
    pole_residue = channel_count * bubble_coefficient
    beta_coefficient = 2 * pole_residue
    assert_equal(
        "phi4 crossed-channel pole residue in 1/(16pi^2) units",
        pole_residue,
        Fraction(25, 6),
    )
    assert_equal(
        "phi4 beta coefficient in 1/(16pi^2) units",
        beta_coefficient,
        3 * lam * lam,
    )

    # The finite bubble is -log((-x-i0)/mu^2)+c_sub.  Differentiating with
    # respect to log(mu) gives 2 per channel, reproducing the beta coefficient
    # that cancels the running of the tree amplitude -lambda.
    log_mu_derivative = channel_count * bubble_coefficient * 2
    assert_equal(
        "phi4 finite-log mu derivative cancels tree running",
        log_mu_derivative,
        beta_coefficient,
    )

    one_channel_pole = bubble_coefficient
    one_channel_beta = 2 * one_channel_pole
    assert_true(
        "single-channel cut misses crossed-channel beta factor",
        one_channel_beta != beta_coefficient,
    )
    assert_equal(
        "single-channel beta is one third of full beta",
        channel_count * one_channel_beta,
        beta_coefficient,
    )

    finite_subtraction_shift = Fraction(7, 11)
    amplitude_shift = channel_count * bubble_coefficient * finite_subtraction_shift
    finite_coupling_redefinition = amplitude_shift
    tree_shift = -finite_coupling_redefinition
    assert_equal(
        "finite local scheme shift compensated by coupling redefinition",
        amplitude_shift + tree_shift,
        Fraction(0),
    )

    local_shift = {"local": finite_coupling_redefinition}
    assert_equal(
        "finite local subtraction constant remains cut invisible",
        channel_cuts(local_shift),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    assert_true(
        "cut-only data cannot determine finite local subtraction",
        finite_subtraction_shift != 0 and channel_cuts(local_shift) == (0, 0, 0),
    )


def check_one_loop_reconstruction_datum() -> None:
    gates = (
        "cut_data",
        "representative",
        "rational_regulator",
        "reduction",
        "boundary_branch",
        "subtraction",
        "observable",
    )
    gate_order = {gate: index for index, gate in enumerate(gates)}
    dependency_edges = (
        ("cut_data", "representative"),
        ("representative", "rational_regulator"),
        ("representative", "reduction"),
        ("reduction", "boundary_branch"),
        ("boundary_branch", "subtraction"),
        ("subtraction", "observable"),
    )
    for source, target in dependency_edges:
        assert_true(
            f"{source} precedes {target}",
            gate_order[source] < gate_order[target],
        )

    example_coverage = {
        "phi4_cut_reconstruction": {"cut_data", "representative"},
        "all_plus_rational_probe": {
            "cut_data",
            "representative",
            "rational_regulator",
        },
        "master_transport": {"reduction", "boundary_branch"},
        "finite_remainder": {"subtraction"},
        "infrared_safe_observable": {"observable"},
    }
    covered = set().union(*example_coverage.values())
    assert_equal("one-loop reconstruction gates covered", covered, set(gates))

    single_gate_omissions = {
        f"omit_{gate}": set(gates) - {gate}
        for gate in gates
    }
    omission_matrix = [
        [
            Fraction(1) if gate not in shortcut else Fraction(0)
            for gate in gates
        ]
        for shortcut in single_gate_omissions.values()
    ]
    assert_equal(
        "single-gate omissions are distinguished",
        rank(omission_matrix),
        len(gates),
    )

    residuals = {
        "cut_data": Fraction(1, 101),
        "representative": Fraction(1, 103),
        "rational_regulator": Fraction(1, 107),
        "reduction": Fraction(1, 109),
        "boundary_branch": Fraction(1, 113),
        "subtraction": Fraction(1, 127),
        "observable": Fraction(1, 131),
    }
    exact_budget = sum(residuals.values(), Fraction(0))

    four_dimensional_cut_shortcut = {"cut_data", "representative"}
    assert_equal(
        "four-dimensional cut shortcut missing gates",
        set(gates) - four_dimensional_cut_shortcut,
        {
            "rational_regulator",
            "reduction",
            "boundary_branch",
            "subtraction",
            "observable",
        },
    )
    four_dimensional_cut_budget = sum(
        residuals[gate] for gate in four_dimensional_cut_shortcut
    )
    assert_true(
        "four-dimensional cut shortcut underbudgets reconstruction",
        four_dimensional_cut_budget < exact_budget,
    )

    virtual_shortcut = set(gates) - {"observable"}
    virtual_budget = sum(residuals[gate] for gate in virtual_shortcut)
    assert_equal(
        "virtual-only shortcut misses observable residual",
        exact_budget - virtual_budget,
        residuals["observable"],
    )
    assert_true(
        "virtual-only shortcut underbudgets physical comparison",
        virtual_budget < exact_budget,
    )


def d_dimensional_probe_signature(basis_name: str) -> Fraction:
    # A toy D-dimensional probe sees the evanescent numerator sector.  It is
    # invisible to strictly four-dimensional cuts, but can leave a finite
    # rational term after a regulator pole multiplies an O(epsilon) numerator.
    if basis_name == "four_dimensional_rational_null":
        return Fraction(1)
    return Fraction(0)


def check_four_dimensional_cut_blind_spot() -> None:
    base = {"B_s": Fraction(2), "B_t": Fraction(3), "B_u": Fraction(5)}
    shifted = dict(base)
    shifted["four_dimensional_rational_null"] = Fraction(7)
    assert_equal("same four-dimensional cuts", channel_cuts(base), channel_cuts(shifted))
    base_probe = sum(
        coefficient * d_dimensional_probe_signature(name)
        for name, coefficient in base.items()
    )
    shifted_probe = sum(
        coefficient * d_dimensional_probe_signature(name)
        for name, coefficient in shifted.items()
    )
    assert_equal("base D-dimensional rational probe", base_probe, Fraction(0))
    assert_equal("shifted D-dimensional rational probe", shifted_probe, Fraction(7))
    assert_true("D-dimensional information distinguishes amplitudes", base_probe != shifted_probe)


def little_group_weights(
    angle_powers: BracketPowers,
    square_powers: BracketPowers,
    legs: tuple[int, ...] = (1, 2, 3, 4),
) -> tuple[int, ...]:
    """Return exponents of t_i under lambda_i -> t_i lambda_i."""
    weights = {leg: 0 for leg in legs}
    for (left, right), power in angle_powers.items():
        weights[left] += power
        weights[right] += power
    for (left, right), power in square_powers.items():
        weights[left] -= power
        weights[right] -= power
    return tuple(weights[leg] for leg in legs)


def bracket_mass_dimension(
    angle_powers: BracketPowers,
    square_powers: BracketPowers,
) -> int:
    return sum(angle_powers.values()) + sum(square_powers.values())


def add_powers(*power_maps: BracketPowers) -> BracketPowers:
    result: BracketPowers = {}
    for power_map in power_maps:
        for bracket, power in power_map.items():
            result[bracket] = result.get(bracket, 0) + power
    return {bracket: power for bracket, power in result.items() if power != 0}


def four_gluon_tree_nonzero(helicities: tuple[int, int, int, int]) -> bool:
    negative_count = sum(1 for helicity in helicities if helicity == -1)
    return negative_count == 2


def plus_tree_possible_with_internal(
    external_plus_count: int,
    internal_helicities: tuple[int, int],
) -> bool:
    leg_count = external_plus_count + 2
    negative_count = sum(1 for helicity in internal_helicities if helicity == -1)
    if leg_count == 3:
        return negative_count in {1, 2}
    return negative_count == 2


def all_plus_massive_scalar_probe(mu_perp_squared: Fraction) -> Fraction:
    # The four-point all-plus rational term is seen by the evanescent sector:
    # the product of two massive-scalar cut trees carries two powers of
    # mu_perp^2 in this finite ledger.
    return mu_perp_squared * mu_perp_squared


def check_mu4_dimension_shift_rational_residue() -> None:
    # In the shifted 8-2 eps scalar box, the leading Feynman-parameter pole is
    # Gamma(eps) times the volume of the three-simplex, 1/6.  Multiplication by
    # the evanescent dimension-shift prefactor -eps(1-eps) leaves -1/6.
    simplex_volume = Fraction(1, factorial(3))
    shifted_box_pole = simplex_volume
    dimension_shift_residue = -shifted_box_pole
    assert_equal("mu4 shifted box simplex volume", simplex_volume, Fraction(1, 6))
    assert_equal("mu4 dimension-shift finite residue", dimension_shift_residue, -Fraction(1, 6))

    # The finite part of the shifted box does not affect the epsilon^0 residue:
    # (-eps+eps^2) * (a/eps + b + O(eps)) has finite term -a.
    shifted_box_finite_part = Fraction(17, 19)
    finite_from_pole_and_finite_part = -shifted_box_pole
    assert_equal(
        "mu4 dimension shift ignores shifted finite part at epsilon zero",
        finite_from_pole_and_finite_part,
        dimension_shift_residue,
    )
    assert_true(
        "mu4 shifted finite part is not the rational residue",
        shifted_box_finite_part != -dimension_shift_residue,
    )

    # A strict four-dimensional cut evaluates the massive-scalar probe at
    # mu_perp^2=0 and therefore sees no coefficient, while massive unitarity
    # extracts the coefficient of (mu_perp^2)^2 before applying the shift.
    cut_tree_product_by_mu2_power = {0: Fraction(0), 1: Fraction(0), 2: Fraction(5, 7)}
    strict_four_dimensional_cut = cut_tree_product_by_mu2_power.get(0, Fraction(0))
    massive_scalar_mu4_coefficient = cut_tree_product_by_mu2_power[2]
    assert_equal("strict 4D all-plus mu4 cut is zero", strict_four_dimensional_cut, Fraction(0))
    assert_equal("massive unitarity extracts mu4 coefficient", massive_scalar_mu4_coefficient, Fraction(5, 7))

    recovered_rational = massive_scalar_mu4_coefficient * dimension_shift_residue
    assert_equal("massive unitarity mu4 rational residue", recovered_rational, -Fraction(5, 42))
    assert_true(
        "strict 4D cut misses nonzero mu4 rational residue",
        recovered_rational != strict_four_dimensional_cut,
    )

    wrong_sign_residue = shifted_box_pole
    assert_true(
        "wrong mu_perp sign changes rational residue",
        massive_scalar_mu4_coefficient * wrong_sign_residue != recovered_rational,
    )

    no_shift_shortcut = Fraction(0)
    assert_true(
        "omitting dimension shift loses all-plus rational residue",
        no_shift_shortcut != recovered_rational,
    )


def factorial(value: int) -> int:
    result = 1
    for factor in range(2, value + 1):
        result *= factor
    return result


def n4_mhv_topology_signature(name: str) -> tuple[Fraction, Fraction, Fraction]:
    """Return (quadruple cut, s two-particle cut, t two-particle cut)."""
    if name == "box":
        return (Fraction(1), Fraction(1), Fraction(1))
    if name == "s_triangle":
        return (Fraction(0), Fraction(1), Fraction(0))
    if name == "t_triangle":
        return (Fraction(0), Fraction(0), Fraction(1))
    if name in {"bubble", "rational_or_local"}:
        return (Fraction(0), Fraction(0), Fraction(0))
    raise ValueError(name)


def n4_mhv_cut_signature(coefficients: dict[str, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    cuts = [Fraction(0), Fraction(0), Fraction(0)]
    for topology, coefficient in coefficients.items():
        signature = n4_mhv_topology_signature(topology)
        for index, value in enumerate(signature):
            cuts[index] += coefficient * value
    return tuple(cuts)


def check_gauge_theory_helicity_controls() -> None:
    parke_taylor_angle = {
        (1, 2): 3,   # <12>^4 / <12>
        (2, 3): -1,
        (3, 4): -1,
        (4, 1): -1,
    }
    parke_taylor_square: BracketPowers = {}
    assert_equal(
        "Parke-Taylor little-group weights",
        little_group_weights(parke_taylor_angle, parke_taylor_square),
        (2, 2, -2, -2),
    )
    assert_equal(
        "Parke-Taylor mass dimension",
        bracket_mass_dimension(parke_taylor_angle, parke_taylor_square),
        0,
    )

    st_dimension = 4
    scalar_box_dimension = -4
    assert_equal(
        "N=4 MHV box dimension",
        bracket_mass_dimension(parke_taylor_angle, parke_taylor_square)
        + st_dimension
        + scalar_box_dimension,
        0,
    )
    assert_equal(
        "N=4 MHV box inherits tree little-group weights",
        little_group_weights(parke_taylor_angle, parke_taylor_square),
        (2, 2, -2, -2),
    )

    all_plus_angle = {(1, 2): -1, (3, 4): -1}
    all_plus_square = {(1, 2): 1, (3, 4): 1}
    assert_equal(
        "all-plus rational little-group weights",
        little_group_weights(all_plus_angle, all_plus_square),
        (-2, -2, -2, -2),
    )
    assert_equal(
        "all-plus rational mass dimension",
        bracket_mass_dimension(all_plus_angle, all_plus_square),
        0,
    )

    nonzero_two_particle_cuts = []
    for h_left_1 in (-1, 1):
        for h_left_2 in (-1, 1):
            left_tree = (h_left_1, 1, 1, h_left_2)
            right_tree = (-h_left_2, 1, 1, -h_left_1)
            if four_gluon_tree_nonzero(left_tree) and four_gluon_tree_nonzero(right_tree):
                nonzero_two_particle_cuts.append((left_tree, right_tree))
    assert_equal("strict 4D all-plus two-particle cuts", nonzero_two_particle_cuts, [])

    assert_equal(
        "all-plus massive-scalar probe vanishes in 4D",
        all_plus_massive_scalar_probe(Fraction(0)),
        Fraction(0),
    )
    assert_true(
        "all-plus massive-scalar probe sees evanescent sector",
        all_plus_massive_scalar_probe(Fraction(3, 5)) != 0,
    )


def check_n4_mhv_quadruple_cut_reconstruction() -> None:
    multiplet_by_eta_degree = (1, 4, 6, 4, 1)
    assert_equal("N=4 on-shell multiplet state count", sum(multiplet_by_eta_degree), 16)
    bosonic_states = (
        multiplet_by_eta_degree[0]
        + multiplet_by_eta_degree[2]
        + multiplet_by_eta_degree[4]
    )
    fermionic_states = multiplet_by_eta_degree[1] + multiplet_by_eta_degree[3]
    assert_equal("N=4 bosonic states", bosonic_states, 8)
    assert_equal("N=4 fermionic states", fermionic_states, 8)

    delta8_component_angle = {(1, 2): 4}
    cyclic_denominator_angle = {
        (1, 2): -1,
        (2, 3): -1,
        (3, 4): -1,
        (4, 1): -1,
    }
    tree_component_angle = add_powers(delta8_component_angle, cyclic_denominator_angle)
    assert_equal(
        "N=4 superamplitude component gives Parke-Taylor numerator",
        tree_component_angle,
        {
            (1, 2): 3,
            (2, 3): -1,
            (3, 4): -1,
            (4, 1): -1,
        },
    )
    assert_equal(
        "N=4 MHV tree component little-group weights",
        little_group_weights(tree_component_angle, {}),
        (2, 2, -2, -2),
    )
    assert_equal(
        "N=4 MHV tree component mass dimension",
        bracket_mass_dimension(tree_component_angle, {}),
        0,
    )

    # The quadruple-cut coefficient is st times the tree amplitude.  In the
    # scalar-box normalization used in the text, the average over two isolated
    # cut solutions gives unit maximal-cut normalization.
    two_cut_solutions = 2
    quadruple_cut_average = Fraction(1, 2)
    assert_equal(
        "quadruple-cut solution average",
        two_cut_solutions * quadruple_cut_average,
        Fraction(1),
    )
    st_dimension = 4
    scalar_box_dimension = -4
    assert_equal(
        "N=4 MHV box coefficient dimension",
        bracket_mass_dimension(tree_component_angle, {}) + st_dimension,
        4,
    )
    assert_equal(
        "N=4 MHV integrated box amplitude dimension",
        bracket_mass_dimension(tree_component_angle, {})
        + st_dimension
        + scalar_box_dimension,
        0,
    )

    target_box_coefficient = Fraction(7, 3)
    pure_box = {"box": target_box_coefficient}
    contaminated_same_s_cut = {
        "box": target_box_coefficient - Fraction(2, 5),
        "s_triangle": Fraction(2, 5),
    }
    assert_equal(
        "single s cut cannot separate box and triangle contamination",
        n4_mhv_cut_signature(pure_box)[1],
        n4_mhv_cut_signature(contaminated_same_s_cut)[1],
    )
    assert_true(
        "maximal cut separates the box coefficient",
        n4_mhv_cut_signature(pure_box)[0]
        != n4_mhv_cut_signature(contaminated_same_s_cut)[0],
    )

    reconstructed = {
        "box": target_box_coefficient,
        "s_triangle": Fraction(0),
        "t_triangle": Fraction(0),
        "bubble": Fraction(0),
        "rational_or_local": Fraction(0),
    }
    assert_equal(
        "N=4 MHV reconstructed cut signatures",
        n4_mhv_cut_signature(reconstructed),
        (target_box_coefficient, target_box_coefficient, target_box_coefficient),
    )
    lower_topology_remainder = {
        name: coefficient
        for name, coefficient in reconstructed.items()
        if name != "box"
    }
    assert_equal(
        "N=4 MHV lower-topology remainder vanishes on cuts",
        n4_mhv_cut_signature(lower_topology_remainder),
        (Fraction(0), Fraction(0), Fraction(0)),
    )

    gluon_only_internal_states = 2
    assert_true(
        "gluon-only state sum is not the N=4 multiplet",
        gluon_only_internal_states != sum(multiplet_by_eta_degree),
    )
    assert_true(
        "gluon-only state sum lacks Bose-Fermi balance",
        gluon_only_internal_states != fermionic_states,
    )
    assert_equal("four-point leading-color cyclic trace terms", factorial(4) // 4, 6)


def check_triple_cut_triangle_projection_after_box_subtraction() -> None:
    def poly_add_int(
        left: dict[int, Fraction],
        right: dict[int, Fraction],
    ) -> dict[int, Fraction]:
        result = dict(left)
        for power, coeff in right.items():
            result[power] = result.get(power, Fraction(0)) + coeff
            if result[power] == 0:
                del result[power]
        return result

    def poly_scale_int(scale: Fraction, poly: dict[int, Fraction]) -> dict[int, Fraction]:
        return {
            power: scale * coeff
            for power, coeff in poly.items()
            if scale * coeff
        }

    def constant_projection(poly: dict[int, Fraction]) -> Fraction:
        return poly.get(0, Fraction(0))

    triangle_coefficient = Fraction(7, 5)
    triangle_cut_residue = {0: Fraction(1)}
    spurious_surface_terms = {
        -2: Fraction(11, 13),
        -1: Fraction(-3, 7),
        1: Fraction(5, 9),
        3: Fraction(-17, 19),
    }
    box_data = [
        (
            Fraction(2, 3),
            {-1: Fraction(5), 0: Fraction(-7, 4), 1: Fraction(11, 6)},
        ),
        (
            Fraction(-4, 9),
            {-2: Fraction(13, 5), 0: Fraction(3, 2), 2: Fraction(-19, 7)},
        ),
    ]

    raw_triple_cut = poly_add_int(
        poly_scale_int(triangle_coefficient, triangle_cut_residue),
        spurious_surface_terms,
    )
    known_box_contamination: dict[int, Fraction] = {}
    for box_coefficient, box_residue in box_data:
        raw_triple_cut = poly_add_int(
            raw_triple_cut,
            poly_scale_int(box_coefficient, box_residue),
        )
        known_box_contamination = poly_add_int(
            known_box_contamination,
            poly_scale_int(box_coefficient, box_residue),
        )

    raw_constant = constant_projection(raw_triple_cut)
    expected_box_constant = sum(
        box_coefficient * constant_projection(box_residue)
        for box_coefficient, box_residue in box_data
    )
    assert_equal(
        "triple-cut raw constant contains box residue",
        raw_constant,
        triangle_coefficient + expected_box_constant,
    )
    assert_true(
        "raw triple-cut constant is not triangle coefficient",
        raw_constant != triangle_coefficient,
    )

    post_box_triple_cut = poly_add_int(
        raw_triple_cut,
        poly_scale_int(Fraction(-1), known_box_contamination),
    )
    assert_equal(
        "post-box triple-cut constant projection",
        constant_projection(post_box_triple_cut),
        triangle_coefficient,
    )
    assert_equal(
        "spurious triple-cut terms have zero contour average",
        constant_projection(spurious_surface_terms),
        Fraction(0),
    )

    partial_subtraction = poly_add_int(
        raw_triple_cut,
        poly_scale_int(-box_data[0][0], box_data[0][1]),
    )
    assert_true(
        "omitting a known box subtraction leaves wrong triangle coefficient",
        constant_projection(partial_subtraction) != triangle_coefficient,
    )

    shifted_box_residue = poly_add_int(box_data[0][1], {0: Fraction(5, 8)})
    shifted_box_contamination = poly_add_int(
        poly_scale_int(box_data[0][0], shifted_box_residue),
        poly_scale_int(box_data[1][0], box_data[1][1]),
    )
    wrong_post_box = poly_add_int(
        raw_triple_cut,
        poly_scale_int(Fraction(-1), shifted_box_contamination),
    )
    assert_true(
        "wrong box normalization spoils triangle projection",
        constant_projection(wrong_post_box) != triangle_coefficient,
    )

    reparametrization_scale = Fraction(3, 5)
    reparametrized_spurious = {
        power: coeff * (reparametrization_scale ** power)
        for power, coeff in spurious_surface_terms.items()
    }
    assert_equal(
        "nonzero Laurent powers remain invisible to constant projection",
        constant_projection(reparametrized_spurious),
        Fraction(0),
    )


def check_five_gluon_all_plus_rational_template() -> None:
    legs = (1, 2, 3, 4, 5)
    denominator_angle: BracketPowers = {
        (1, 2): -1,
        (2, 3): -1,
        (3, 4): -1,
        (4, 5): -1,
        (5, 1): -1,
    }

    trace_terms: list[tuple[int, BracketPowers, BracketPowers]] = []
    for omitted in legs:
        kept = tuple(leg for leg in legs if leg != omitted)
        i, j, k, ell = kept
        trace_angle = {(i, j): 1, (k, ell): 1}
        trace_square = {(j, k): 1, (ell, i): 1}
        trace_terms.append((omitted, trace_angle, trace_square))

    assert_equal("five-point all-plus trace terms", len(trace_terms), 5)
    assert_equal(
        "five-point trace numerator covers each omitted leg",
        {omitted for omitted, _, _ in trace_terms},
        set(legs),
    )

    for omitted, trace_angle, trace_square in trace_terms:
        assert_equal(
            f"five-point trace term {omitted} little-group neutral",
            little_group_weights(trace_angle, trace_square, legs),
            (0, 0, 0, 0, 0),
        )
        full_angle = add_powers(denominator_angle, trace_angle)
        assert_equal(
            f"five-point all-plus term {omitted} little-group weights",
            little_group_weights(full_angle, trace_square, legs),
            (-2, -2, -2, -2, -2),
        )
        assert_equal(
            f"five-point all-plus term {omitted} mass dimension",
            bracket_mass_dimension(full_angle, trace_square),
            -1,
        )

    nonzero_strict_cuts: list[tuple[int, int, int]] = []
    for left_external_plus_count in range(1, 5):
        right_external_plus_count = 5 - left_external_plus_count
        for h1 in (-1, 1):
            for h2 in (-1, 1):
                left_possible = plus_tree_possible_with_internal(
                    left_external_plus_count,
                    (h1, h2),
                )
                right_possible = plus_tree_possible_with_internal(
                    right_external_plus_count,
                    (-h2, -h1),
                )
                if left_possible and right_possible:
                    nonzero_strict_cuts.append((left_external_plus_count, h1, h2))
    assert_equal("strict 4D five-gluon all-plus two-particle cuts", nonzero_strict_cuts, [])

    assert_equal(
        "five-point all-plus massive-scalar probe vanishes in 4D",
        all_plus_massive_scalar_probe(Fraction(0)),
        Fraction(0),
    )
    assert_equal(
        "five-point all-plus evanescent probe power",
        all_plus_massive_scalar_probe(Fraction(2, 3)),
        Fraction(4, 9),
    )


def check_four_point_color_kinematics_gateway() -> None:
    s = Fraction(2)
    t = Fraction(3)
    u = Fraction(-5)
    denominators = [s, t, u]
    assert_equal("four-point massless Mandelstam sum", s + t + u, Fraction(0))

    colors = [Fraction(1), Fraction(2), Fraction(-3)]
    assert_equal("four-point color Jacobi", sum(colors, Fraction(0)), Fraction(0))

    numerators = [
        s * (t - u),
        t * (u - s),
        u * (s - t),
    ]
    assert_equal(
        "four-point kinematic Jacobi",
        sum(numerators, Fraction(0)),
        Fraction(0),
    )

    gauge_amplitude = sum(
        colors[index] * numerators[index] / denominators[index]
        for index in range(3)
    )
    gravity_amplitude = sum(
        numerators[index] * numerators[index] / denominators[index]
        for index in range(3)
    )
    assert_equal("four-point gauge amplitude value", gauge_amplitude, Fraction(-3))
    assert_equal("four-point numerator-square value", gravity_amplitude, Fraction(270))

    gauge_equivalent_deltas = [Fraction(2), Fraction(-1), Fraction(0)]
    assert_equal(
        "generalized-gauge color null shift",
        dot(colors, gauge_equivalent_deltas),
        Fraction(0),
    )
    shifted_numerators = [
        numerators[index] + denominators[index] * gauge_equivalent_deltas[index]
        for index in range(3)
    ]
    shifted_gauge_amplitude = sum(
        colors[index] * shifted_numerators[index] / denominators[index]
        for index in range(3)
    )
    assert_equal(
        "generalized-gauge shift leaves gauge amplitude",
        shifted_gauge_amplitude,
        gauge_amplitude,
    )
    assert_true(
        "gauge-equivalent numerator can break kinematic Jacobi",
        sum(shifted_numerators, Fraction(0)) != 0,
    )
    shifted_naive_square = sum(
        shifted_numerators[index] * shifted_numerators[index] / denominators[index]
        for index in range(3)
    )
    assert_true(
        "naive double copy changes under non-Jacobi gauge shift",
        shifted_naive_square != gravity_amplitude,
    )

    jacobi_preserving_delta = Fraction(7)
    jacobi_shifted_numerators = [
        numerators[index] + jacobi_preserving_delta * denominators[index]
        for index in range(3)
    ]
    assert_equal(
        "common denominator-weighted shift preserves Jacobi",
        sum(jacobi_shifted_numerators, Fraction(0)),
        Fraction(0),
    )
    mixed_double_copy = sum(
        jacobi_shifted_numerators[index] * numerators[index] / denominators[index]
        for index in range(3)
    )
    assert_equal(
        "Jacobi-compatible one-copy shift leaves double copy",
        mixed_double_copy,
        gravity_amplitude,
    )
    both_copy_shift = sum(
        jacobi_shifted_numerators[index]
        * jacobi_shifted_numerators[index]
        / denominators[index]
        for index in range(3)
    )
    assert_equal(
        "Jacobi-compatible two-copy shift leaves four-point square",
        both_copy_shift,
        gravity_amplitude,
    )


def check_loop_level_color_kinematics_surface_obstruction() -> None:
    colors = [Fraction(1), Fraction(2), Fraction(-3)]
    assert_equal("loop Jacobi triplet color sum", sum(colors, Fraction(0)), Fraction(0))

    numerators = [Fraction(2), Fraction(3), Fraction(-5)]
    second_copy = [Fraction(4), Fraction(1), Fraction(-5)]
    assert_equal(
        "loop numerator Jacobi representative",
        sum(numerators, Fraction(0)),
        Fraction(0),
    )
    assert_equal(
        "second numerator copy Jacobi representative",
        sum(second_copy, Fraction(0)),
        Fraction(0),
    )

    cut_signature = [Fraction(11), Fraction(13), Fraction(17)]
    surface_cut_signature = [Fraction(0), Fraction(0), Fraction(0)]
    shifted_cut_signature = vector_add(cut_signature, surface_cut_signature)
    assert_equal(
        "surface/contact shift invisible to selected cuts",
        shifted_cut_signature,
        cut_signature,
    )

    surface_shift = [Fraction(2), Fraction(-1), Fraction(0)]
    assert_equal(
        "surface shift color-weighted gauge null",
        dot(colors, surface_shift),
        Fraction(0),
    )
    gauge_amplitude = dot(colors, numerators)
    shifted_numerators = vector_add(numerators, surface_shift)
    shifted_gauge_amplitude = dot(colors, shifted_numerators)
    assert_equal(
        "surface shift leaves gauge amplitude integral",
        shifted_gauge_amplitude,
        gauge_amplitude,
    )

    assert_equal(
        "surface shift creates loop Jacobi defect",
        sum(shifted_numerators, Fraction(0)),
        Fraction(1),
    )
    assert_true(
        "shifted loop representative is not color-kinematics",
        sum(shifted_numerators, Fraction(0)) != 0,
    )

    double_copy = dot(numerators, second_copy)
    shifted_double_copy = dot(shifted_numerators, second_copy)
    assert_equal(
        "surface shift changes naive double-copy pairing by defect",
        shifted_double_copy - double_copy,
        dot(surface_shift, second_copy),
    )
    assert_true(
        "integrated gauge null is not a double-copy null",
        shifted_double_copy != double_copy,
    )

    jacobi_restoring_compensation = vector_scale(Fraction(-1), surface_shift)
    repaired_numerators = vector_add(shifted_numerators, jacobi_restoring_compensation)
    assert_equal(
        "compensated surface shift restores numerator Jacobi",
        sum(repaired_numerators, Fraction(0)),
        Fraction(0),
    )
    assert_equal(
        "Jacobi repair cancels double-copy surface shift",
        dot(jacobi_restoring_compensation, second_copy),
        -dot(surface_shift, second_copy),
    )


def check_loop_level_jacobi_repair_double_copy_null() -> None:
    colors = [Fraction(1), Fraction(2), Fraction(-3)]
    assert_equal("Jacobi repair color null direction", sum(colors, Fraction(0)), Fraction(0))

    numerators = [Fraction(5), Fraction(7), Fraction(-10)]
    jacobi_defect = sum(numerators, Fraction(0))
    assert_equal("unrepaired loop numerator Jacobi defect", jacobi_defect, Fraction(2))

    common_repair = [-(jacobi_defect / 3)] * 3
    repaired_numerators = vector_add(numerators, common_repair)
    assert_equal(
        "common surface repair restores loop numerator Jacobi",
        sum(repaired_numerators, Fraction(0)),
        Fraction(0),
    )
    assert_equal(
        "common Jacobi repair is color-weighted gauge null",
        dot(colors, common_repair),
        Fraction(0),
    )

    second_copy = [Fraction(4), Fraction(1), Fraction(-5)]
    assert_equal(
        "second copy satisfies loop numerator Jacobi",
        sum(second_copy, Fraction(0)),
        Fraction(0),
    )
    double_copy_before = dot(numerators, second_copy)
    double_copy_after = dot(repaired_numerators, second_copy)
    assert_equal(
        "common Jacobi repair is double-copy null against Jacobi second copy",
        double_copy_after,
        double_copy_before,
    )

    defective_second_copy = [Fraction(4), Fraction(1), Fraction(-4)]
    assert_true(
        "defective second copy has Jacobi defect",
        sum(defective_second_copy, Fraction(0)) != 0,
    )
    defective_double_copy_after = dot(repaired_numerators, defective_second_copy)
    defective_double_copy_before = dot(numerators, defective_second_copy)
    assert_equal(
        "common repair shift pairs with defective second-copy Jacobi sum",
        defective_double_copy_after - defective_double_copy_before,
        common_repair[0] * sum(defective_second_copy, Fraction(0)),
    )
    assert_true(
        "common repair is not double-copy null against defective second copy",
        defective_double_copy_after != defective_double_copy_before,
    )

    graph_dependent_color_null_shift = [Fraction(2), Fraction(-1), Fraction(0)]
    assert_equal(
        "graph-dependent shift can be color null",
        dot(colors, graph_dependent_color_null_shift),
        Fraction(0),
    )
    assert_true(
        "graph-dependent color-null shift is not common Jacobi repair",
        graph_dependent_color_null_shift != common_repair,
    )
    graph_shifted_double_copy = dot(
        vector_add(numerators, graph_dependent_color_null_shift),
        second_copy,
    )
    assert_true(
        "graph-dependent color-null shift can change double copy",
        graph_shifted_double_copy != double_copy_before,
    )

    sampled_cut_defect = Fraction(0)
    assert_true(
        "cut-sampled Jacobi vanishing does not prove full defect",
        sampled_cut_defect == 0 and jacobi_defect != 0,
    )


def check_finite_two_scale_box_master() -> None:
    # Variables are Ls=log S and Lt=log T.  The fixed reduced-box convention is
    # ST I_4/(2 r_Gamma) plus the two soft/collinear pole terms, leaving
    # 1/2 (Ls-Lt)^2 + pi^2/2.
    raw_pole_signature = {"S": Fraction(-1), "T": Fraction(-1)}
    pole_subtraction = {"S": Fraction(1), "T": Fraction(1)}
    assert_equal(
        "finite box S pole cancelled by declared subtraction",
        raw_pole_signature["S"] + pole_subtraction["S"],
        Fraction(0),
    )
    assert_equal(
        "finite box T pole cancelled by declared subtraction",
        raw_pole_signature["T"] + pole_subtraction["T"],
        Fraction(0),
    )

    finite_box: LogPolynomial = {
        (2, 0): Fraction(1, 2),
        (1, 1): Fraction(-1),
        (0, 2): Fraction(1, 2),
    }
    log_ratio: LogPolynomial = {
        (1, 0): Fraction(1),
        (0, 1): Fraction(-1),
    }
    assert_equal(
        "finite box S differential equation",
        poly_derivative(finite_box, 0),
        log_ratio,
    )
    assert_equal(
        "finite box T differential equation",
        poly_derivative(finite_box, 1),
        poly_scale(Fraction(-1), log_ratio),
    )
    assert_equal(
        "finite box scale invariance",
        poly_add(poly_derivative(finite_box, 0), poly_derivative(finite_box, 1)),
        {},
    )

    second_derivative_matrix = [
        [
            poly_derivative(poly_derivative(finite_box, row), col).get((0, 0), Fraction(0))
            for col in (0, 1)
        ]
        for row in (0, 1)
    ]
    assert_equal(
        "finite box Hessian in log variables",
        second_derivative_matrix,
        [[Fraction(1), Fraction(-1)], [Fraction(-1), Fraction(1)]],
    )
    assert_equal("finite box Hessian rank", rank(second_derivative_matrix), 1)

    def bose_kernel(t: float) -> float:
        if t == 0.0:
            return 1.0
        return t / math.expm1(t)

    boundary_from_sector_integral = 3.0 * simpson_integral(bose_kernel, 0.0, 40.0, 2000)
    boundary_constant = math.pi * math.pi / 2.0
    assert_close_float(
        "finite box Euclidean boundary from sector integral",
        boundary_from_sector_integral,
        boundary_constant,
        tol=1.0e-12,
    )

    for ratio in (1.5, 2.0, 0.4):
        parameter_value = (
            boundary_constant
            - real_dilog_from_parameter_integral(1.0 - ratio)
            - real_dilog_from_parameter_integral(1.0 - 1.0 / ratio)
        )
        log_square_value = 0.5 * math.log(ratio) ** 2 + boundary_constant
        assert_close_float(
            f"finite box parameter integral agrees with log-square ratio={ratio}",
            parameter_value,
            log_square_value,
            tol=1.0e-10,
        )

    wrong_boundary_value = 0.0
    assert_true(
        "finite box differential equations alone do not fix boundary",
        abs(wrong_boundary_value - boundary_from_sector_integral) > 1.0,
    )

    one_cut_deformation = poly_add(finite_box, {(0, 1): Fraction(5, 17)})
    assert_equal(
        "one-cut deformation preserves S derivative",
        poly_derivative(one_cut_deformation, 0),
        poly_derivative(finite_box, 0),
    )
    assert_true(
        "one-cut deformation changes T derivative",
        poly_derivative(one_cut_deformation, 1) != poly_derivative(finite_box, 1),
    )
    assert_true(
        "one-cut deformation breaks scale invariance",
        poly_add(
            poly_derivative(one_cut_deformation, 0),
            poly_derivative(one_cut_deformation, 1),
        )
        != {},
    )

    # On the physical s-channel branch, Ls -> R - i*pi and Lt -> 0.
    # The finite box has imaginary part -pi R in this normalization, while the
    # fixed pi^2/2 boundary cancels the real -pi^2/2 from the square.
    ls_squared_coeff = finite_box[(2, 0)]
    imaginary_pi_log_coeff = -2 * ls_squared_coeff
    boundary_pi_squared_coeff = Fraction(1, 2)
    real_pi_squared_coeff = boundary_pi_squared_coeff - ls_squared_coeff
    assert_equal(
        "finite box physical branch imaginary coefficient",
        imaginary_pi_log_coeff,
        Fraction(-1),
    )
    assert_equal(
        "finite box physical branch pi-squared coefficient",
        real_pi_squared_coeff,
        Fraction(0),
    )
    assert_true(
        "branch-labelled box differs from Euclidean continuation",
        imaginary_pi_log_coeff != 0,
    )


def check_bubble_ibp_identity() -> None:
    samples = [
        (Fraction(1, 11), Fraction(3, 2), Fraction(5, 7)),
        (Fraction(-1, 13), Fraction(7, 5), Fraction(11, 3)),
        (Fraction(2, 17), Fraction(19, 6), Fraction(13, 10)),
    ]
    for epsilon, q_squared, master in samples:
        dimension = Fraction(4) - 2 * epsilon
        squared_propagator = -(dimension - 3) * master / q_squared
        scaleless_tadpole = Fraction(0)
        ibp_residual = (
            (dimension - 3) * master
            - scaleless_tadpole
            + q_squared * squared_propagator
        )
        assert_equal(f"bubble IBP residual epsilon={epsilon}", ibp_residual, Fraction(0))

        derivative = -epsilon * master / q_squared
        differential_residual = q_squared * derivative + epsilon * master
        assert_equal(
            f"bubble master differential equation epsilon={epsilon}",
            differential_residual,
            Fraction(0),
        )


def check_bubble_numerator_sector_projection() -> None:
    samples = [
        (Fraction(3), Fraction(4), Fraction(5), Fraction(7), Fraction(11)),
        (
            Fraction(-2, 3),
            Fraction(5, 6),
            Fraction(13, 7),
            Fraction(-3, 5),
            Fraction(19, 4),
        ),
        (
            Fraction(11, 9),
            Fraction(-7, 3),
            Fraction(2, 5),
            Fraction(17, 8),
            Fraction(23, 6),
        ),
    ]
    for c_parent, c_dot_p, c_d0, c_d1, q_squared in samples:
        parent_coefficient = c_parent - c_dot_p / 2
        one_over_d0_coefficient = (c_d1 + c_dot_p / 2) / q_squared
        one_over_d1_coefficient = (c_d0 - c_dot_p / 2) / q_squared

        # Substitute 2 ell.P = D1 - D0 - Q^2 and compare the polynomial
        # numerator obtained after multiplying the sector decomposition by
        # D0 D1.  The tuple records (constant, D0 coefficient, D1 coefficient).
        projected_polynomial = (
            parent_coefficient,
            one_over_d1_coefficient,
            one_over_d0_coefficient,
        )
        direct_polynomial = (
            c_parent - c_dot_p / 2,
            (c_d0 - c_dot_p / 2) / q_squared,
            (c_d1 + c_dot_p / 2) / q_squared,
        )
        assert_equal(
            f"bubble numerator sector projection q^2={q_squared}",
            projected_polynomial,
            direct_polynomial,
        )

        # On the parent double cut, D0 = D1 = 0 and ell.P / Q^2 = -1/2.
        parent_cut_value = c_parent - c_dot_p / 2
        assert_equal(
            f"bubble parent-cut coefficient q^2={q_squared}",
            parent_cut_value,
            parent_coefficient,
        )

        parent_master = Fraction(29, 31)
        lower_sector_0 = Fraction(5, 13)
        lower_sector_1 = Fraction(-7, 17)
        full_integral = (
            parent_coefficient * parent_master
            + one_over_d0_coefficient * lower_sector_0
            + one_over_d1_coefficient * lower_sector_1
        )
        cut_only_integral = parent_cut_value * parent_master
        assert_true(
            f"non-scaleless lower sectors are parent-cut blind q^2={q_squared}",
            full_integral != cut_only_integral,
        )

        massless_dimreg_integral = parent_coefficient * parent_master
        assert_equal(
            f"scaleless lower sectors collapse q^2={q_squared}",
            massless_dimreg_integral,
            cut_only_integral,
        )

    q_squared = Fraction(37, 10)
    bubble_master = Fraction(19, 23)
    p_dot_vector_integral = -q_squared * bubble_master / 2
    vector_coefficient = p_dot_vector_integral / q_squared
    assert_equal(
        "bubble vector Passarino-Veltman coefficient",
        vector_coefficient,
        -bubble_master / 2,
    )


def check_equal_mass_bubble_threshold_family() -> None:
    # F_m(z) = int_0^1 log(1 + 4 z x(1-x)) dx has exact coefficients
    # (-1)^(n+1) 4^n/n * (n!)^2/(2n+1)! near z=0.
    max_order = 7
    coefficients = {
        n: (
            Fraction((-1) ** (n + 1) * (4 ** n), n)
            * Fraction(factorial(n) * factorial(n), factorial(2 * n + 1))
        )
        for n in range(1, max_order + 1)
    }
    assert_equal("equal-mass bubble finite part has zero boundary", coefficients.get(0), None)
    assert_equal(
        "equal-mass bubble small-z coefficients",
        [coefficients[n] for n in range(1, 4)],
        [Fraction(2, 3), Fraction(-4, 15), Fraction(16, 105)],
    )

    # The master equation is 2 z (1+z) F'(z) + F(z) = 2 z T_m with T_m=1.
    coefficients_with_zero = {0: Fraction(0), **coefficients}
    for power in range(1, max_order + 1):
        lhs_coefficient = (
            2 * power * coefficients_with_zero[power]
            + 2 * (power - 1) * coefficients_with_zero[power - 1]
            + coefficients_with_zero[power]
        )
        rhs_coefficient = Fraction(2) if power == 1 else Fraction(0)
        assert_equal(
            f"equal-mass bubble inhomogeneous DE coefficient z^{power}",
            lhs_coefficient,
            rhs_coefficient,
        )

    homogeneous_shortcut_residual = (
        2 * coefficients_with_zero[1] + coefficients_with_zero[1]
    )
    assert_equal(
        "equal-mass bubble lower-tadpole inhomogeneity",
        homogeneous_shortcut_residual,
        Fraction(2),
    )
    assert_true(
        "homogeneous one-master shortcut misses threshold family",
        homogeneous_shortcut_residual != 0,
    )

    z_threshold = Fraction(-1)
    x_stationary = Fraction(1, 2)
    denominator = 1 + 4 * z_threshold * x_stationary * (1 - x_stationary)
    derivative = 4 * z_threshold * (1 - 2 * x_stationary)
    assert_equal("equal-mass bubble Landau denominator", denominator, Fraction(0))
    assert_equal("equal-mass bubble Landau stationary point", derivative, Fraction(0))

    beta = Fraction(3, 5)
    r = 1 / (1 - beta * beta)
    x_minus = (1 - beta) / 2
    x_plus = (1 + beta) / 2
    assert_equal("equal-mass bubble branch sample r", r, Fraction(25, 16))
    assert_equal("massive threshold negative interval length", x_plus - x_minus, beta)
    midpoint_denominator = 1 - 4 * r * x_stationary * (1 - x_stationary)
    assert_true("timelike branch crosses logarithm cut", midpoint_denominator < 0)
    imaginary_part_in_units_of_pi = -(x_plus - x_minus)
    assert_equal(
        "equal-mass bubble imaginary part coefficient",
        imaginary_part_in_units_of_pi,
        -beta,
    )
    assert_true(
        "Euclidean branch reuse misses threshold imaginary part",
        Fraction(0) != imaginary_part_in_units_of_pi,
    )


def check_two_loop_sunrise_elliptic_maximal_cut() -> None:
    # For the equal-mass sunrise in the affine patch x3=1,
    # P_r(x,y) = (x+y+1)(xy+x+y)-rxy.  Eliminating y gives
    # w^2 = Delta_r(x), with quartic coefficients below.
    def delta_coefficients(
        r_value: Fraction,
    ) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
        return (
            Fraction(1),
            2 - 2 * r_value,
            r_value * r_value - 6 * r_value + 3,
            2 - 2 * r_value,
            Fraction(1),
        )

    for r_value in [Fraction(0), Fraction(1), Fraction(4), Fraction(9)]:
        expected = 256 * r_value * r_value * (r_value - 9) * (r_value - 1) ** 3
        assert_equal(
            f"sunrise quartic discriminant r={r_value}",
            quartic_discriminant(delta_coefficients(r_value)),
            expected,
        )

    generic_r = Fraction(4)
    assert_true(
        "generic sunrise maximal cut is genus one",
        quartic_discriminant(delta_coefficients(generic_r)) != 0,
    )
    branch_points = 4
    genus = (branch_points - 2) // 2
    assert_equal("four branch points give elliptic genus", genus, 1)

    threshold_r = Fraction(9)
    x_threshold = Fraction(1)
    y_threshold = Fraction(1)
    p_value = (
        (x_threshold + y_threshold + 1)
        * (x_threshold * y_threshold + x_threshold + y_threshold)
        - threshold_r * x_threshold * y_threshold
    )
    dp_dx = (
        (x_threshold * y_threshold + x_threshold + y_threshold)
        + (x_threshold + y_threshold + 1) * (y_threshold + 1)
        - threshold_r * y_threshold
    )
    dp_dy = (
        (x_threshold * y_threshold + x_threshold + y_threshold)
        + (x_threshold + y_threshold + 1) * (x_threshold + 1)
        - threshold_r * x_threshold
    )
    assert_equal("sunrise physical threshold curve point", p_value, Fraction(0))
    assert_equal("sunrise physical threshold x-stationarity", dp_dx, Fraction(0))
    assert_equal("sunrise physical threshold y-stationarity", dp_dy, Fraction(0))
    assert_true(
        "sunrise physical threshold has positive Feynman parameters",
        x_threshold > 0 and y_threshold > 0,
    )

    pseudo_r = Fraction(1)
    pseudo_x = Fraction(1)
    pseudo_y = Fraction(-1)
    pseudo_value = (
        (pseudo_x + pseudo_y + 1) * (pseudo_x * pseudo_y + pseudo_x + pseudo_y)
        - pseudo_r * pseudo_x * pseudo_y
    )
    assert_equal("sunrise pseudo-threshold curve point", pseudo_value, Fraction(0))
    assert_false(
        "sunrise pseudo-threshold is positive-parameter physical threshold",
        pseudo_x > 0 and pseudo_y > 0,
    )

    log_alphabet_discriminant = 0
    elliptic_discriminant = quartic_discriminant(delta_coefficients(generic_r))
    assert_true(
        "logarithmic one-master shortcut loses the sunrise elliptic curve",
        elliptic_discriminant != log_alphabet_discriminant,
    )


def check_multi_loop_maximal_cut_sector_projection() -> None:
    denominators = frozenset({"D1", "D2", "D3"})
    parent_sector = ("D1", "D2", "D3")
    numerator_terms = {
        frozenset(): Fraction(5, 7),
        frozenset({"D1"}): Fraction(2, 3),
        frozenset({"D2"}): -Fraction(3, 5),
        frozenset({"D3"}): Fraction(7, 11),
        frozenset({"D1", "D2"}): Fraction(13, 17),
    }

    def maximal_cut_residue(terms: dict[frozenset[str], Fraction]) -> Fraction:
        return terms.get(frozenset(), Fraction(0))

    def cancelled_sector(support: frozenset[str]) -> tuple[str, ...]:
        return tuple(sorted(denominators - support))

    sector_projection: dict[tuple[str, ...], Fraction] = {}
    for support, coefficient in numerator_terms.items():
        sector = cancelled_sector(support)
        sector_projection[sector] = sector_projection.get(sector, Fraction(0)) + coefficient

    expected_projection = {
        parent_sector: Fraction(5, 7),
        ("D2", "D3"): Fraction(2, 3),
        ("D1", "D3"): -Fraction(3, 5),
        ("D1", "D2"): Fraction(7, 11),
        ("D3",): Fraction(13, 17),
    }
    assert_equal("multi-loop contact terms cancel into lower sectors", sector_projection, expected_projection)
    assert_equal("parent maximal cut sees only top residue", maximal_cut_residue(numerator_terms), Fraction(5, 7))

    shifted_terms = {
        **numerator_terms,
        frozenset({"D1"}): numerator_terms[frozenset({"D1"})] + Fraction(1, 19),
        frozenset({"D3"}): numerator_terms[frozenset({"D3"})] - Fraction(1, 23),
    }
    assert_equal(
        "same parent maximal cut after contact-sector shift",
        maximal_cut_residue(shifted_terms),
        maximal_cut_residue(numerator_terms),
    )

    shifted_projection: dict[tuple[str, ...], Fraction] = {}
    for support, coefficient in shifted_terms.items():
        sector = cancelled_sector(support)
        shifted_projection[sector] = shifted_projection.get(sector, Fraction(0)) + coefficient
    assert_true(
        "same maximal cut can have different lower-sector projection",
        shifted_projection != sector_projection,
    )

    master_weights = {
        parent_sector: Fraction(3, 2),
        ("D2", "D3"): -Fraction(5, 4),
        ("D1", "D3"): Fraction(7, 6),
        ("D1", "D2"): Fraction(11, 10),
        ("D3",): -Fraction(13, 9),
    }
    full_reduced_value = sum(
        coefficient * master_weights[sector]
        for sector, coefficient in sector_projection.items()
    )
    parent_cut_only_value = sector_projection[parent_sector] * master_weights[parent_sector]
    assert_true(
        "parent maximal cut alone misses reduced lower-sector masters",
        full_reduced_value != parent_cut_only_value,
    )

    scaleless_sectors = {
        ("D2", "D3"): False,
        ("D1", "D3"): True,
        ("D1", "D2"): False,
        ("D3",): False,
    }
    reduced_with_scaleless_collapse = (
        sector_projection[parent_sector] * master_weights[parent_sector]
        + sum(
            sector_projection[sector] * master_weights[sector]
            for sector, is_scaleless in scaleless_sectors.items()
            if not is_scaleless
        )
    )
    all_lower_scaleless_shortcut = parent_cut_only_value
    assert_true(
        "scaleless-collapse shortcut valid only sector by sector",
        reduced_with_scaleless_collapse != all_lower_scaleless_shortcut,
    )

    omitted_lower_majorant = sum(
        abs(sector_projection[sector] * master_weights[sector])
        for sector in scaleless_sectors
        if not scaleless_sectors[sector]
    )
    assert_true(
        "lower-sector master omission bounded by absolute projection budget",
        abs(reduced_with_scaleless_collapse - all_lower_scaleless_shortcut)
        <= omitted_lower_majorant,
    )


def check_dual_contour_master_coefficient_extraction() -> None:
    pairing: Matrix = [
        [Fraction(1), Fraction(2)],
        [Fraction(3), Fraction(5)],
    ]
    determinant = pairing[0][0] * pairing[1][1] - pairing[0][1] * pairing[1][0]
    assert_true("dual-contour pairing is invertible", determinant != 0)
    inverse_pairing: Matrix = [
        [pairing[1][1] / determinant, -pairing[0][1] / determinant],
        [-pairing[1][0] / determinant, pairing[0][0] / determinant],
    ]
    assert_equal(
        "inverse pairing matrix",
        matrix_mul(inverse_pairing, pairing),
        [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]],
    )

    master_coefficients = [Fraction(7, 11), -Fraction(5, 13)]
    surface_kernel = [Fraction(0), Fraction(0)]
    lower_sector_contact = [Fraction(3, 17), -Fraction(2, 19)]
    contour_values = vector_add(
        matrix_vector_mul(pairing, master_coefficients),
        lower_sector_contact,
    )
    reconstructed = matrix_vector_mul(
        inverse_pairing,
        vector_sub(contour_values, vector_add(surface_kernel, lower_sector_contact)),
    )
    assert_equal("dual-contour coefficient extraction", reconstructed, master_coefficients)

    raw_contour_shortcut = contour_values
    assert_true(
        "raw contour values are not master coefficients",
        raw_contour_shortcut != master_coefficients,
    )
    omitted_contact = matrix_vector_mul(inverse_pairing, contour_values)
    assert_true(
        "omitting lower-sector contact shifts coefficients",
        omitted_contact != master_coefficients,
    )

    polluted_surface = [Fraction(1, 23), Fraction(-1, 29)]
    polluted_values = vector_add(contour_values, polluted_surface)
    polluted_reconstruction = matrix_vector_mul(
        inverse_pairing,
        vector_sub(polluted_values, lower_sector_contact),
    )
    assert_true(
        "surface-polluted contours shift extracted coefficients",
        polluted_reconstruction != master_coefficients,
    )
    surface_shift = matrix_vector_mul(inverse_pairing, polluted_surface)
    assert_equal(
        "surface pollution coefficient shift",
        vector_sub(polluted_reconstruction, master_coefficients),
        surface_shift,
    )

    cut_errors = [Fraction(1, 101), Fraction(1, 103)]
    contact_errors = [Fraction(1, 107), Fraction(1, 109)]
    coefficient_error = matrix_vector_mul(
        inverse_pairing,
        vector_add(cut_errors, contact_errors),
    )
    row_majorants = [
        sum(
            abs(inverse_pairing[row][col]) * (cut_errors[col] + contact_errors[col])
            for col in range(2)
        )
        for row in range(2)
    ]
    for index, error in enumerate(coefficient_error):
        assert_true(
            f"dual-contour error majorant {index}",
            abs(error) <= row_majorants[index],
        )

    nondual_pairing: Matrix = [
        [Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(4)],
    ]
    assert_equal(
        "nondual contour pairing cannot distinguish two masters",
        rank(nondual_pairing),
        1,
    )


def check_master_discontinuity_closure_gate() -> None:
    lam = Fraction(7, 5)
    tree_amplitude = -lam
    identical_state_factor = Fraction(1, 2)
    phase_space = massless_two_body_phase_space_times_pi()

    # Physical side: compute the s-channel Cutkosky datum from the unordered
    # identical-particle state sum.  A common factor i/pi is stripped.
    scalar_physical_cut_datum = (
        identical_state_factor
        * tree_amplitude
        * tree_amplitude
        * phase_space
    )

    # Master side: transport the cut-normalized bubble to the physical sheet,
    # then multiply by the independently reconstructed bubble coefficient.
    bubble_coefficient = lam * lam / 2
    bubble_master_discontinuity = phase_space
    scalar_reconstructed_discontinuity = bubble_coefficient * bubble_master_discontinuity
    assert_equal(
        "physical state-sum cut equals transported bubble-master jump",
        scalar_reconstructed_discontinuity,
        scalar_physical_cut_datum,
    )

    ordered_state_sum = tree_amplitude * tree_amplitude * phase_space
    assert_true(
        "ordered state sum misses identical-particle symmetry factor",
        ordered_state_sum != scalar_physical_cut_datum,
    )

    wrong_bubble_jump = phase_space / 2
    wrong_reconstruction = bubble_coefficient * wrong_bubble_jump
    wrong_self_defined_physical_cut = wrong_reconstruction
    assert_equal(
        "self-defined physical cut would hide wrong master jump",
        wrong_reconstruction,
        wrong_self_defined_physical_cut,
    )
    assert_true(
        "independent state-sum datum rejects wrong master jump",
        wrong_self_defined_physical_cut != scalar_physical_cut_datum,
    )

    local_uv_counterterm_discontinuity = Fraction(0)
    assert_equal(
        "local UV counterterm contributes no channel discontinuity",
        scalar_physical_cut_datum + local_uv_counterterm_discontinuity,
        scalar_physical_cut_datum,
    )

    coefficients = [bubble_coefficient, Fraction(3, 17)]
    master_discontinuity = [bubble_master_discontinuity, Fraction(0)]
    lower_sector_discontinuity = -Fraction(2, 23)
    subtraction_discontinuity = Fraction(1, 29)
    physical_cut_datum = (
        scalar_physical_cut_datum
        + lower_sector_discontinuity
        + subtraction_discontinuity
    )
    reconstructed_discontinuity = (
        dot(coefficients, master_discontinuity)
        + lower_sector_discontinuity
        + subtraction_discontinuity
    )
    assert_equal(
        "full channel closure includes lower sector and subtraction jumps",
        reconstructed_discontinuity,
        physical_cut_datum,
    )

    pairing: Matrix = [
        [Fraction(1), Fraction(2)],
        [Fraction(3), Fraction(5)],
    ]
    raw_contour_values = matrix_vector_mul(pairing, coefficients)
    raw_contour_discontinuity = (
        dot(coefficients, raw_contour_values)
        + lower_sector_discontinuity
        + subtraction_discontinuity
    )
    assert_true(
        "raw contour values are not physical master discontinuities",
        raw_contour_discontinuity != physical_cut_datum,
    )

    euclidean_master_values = [Fraction(5, 7), Fraction(11, 17)]
    euclidean_value_shortcut = (
        dot(coefficients, euclidean_master_values)
        + lower_sector_discontinuity
        + subtraction_discontinuity
    )
    assert_true(
        "Euclidean master values do not replace boundary-value jumps",
        euclidean_value_shortcut != physical_cut_datum,
    )

    omitted_lower_sector = dot(coefficients, master_discontinuity) + subtraction_discontinuity
    assert_true(
        "omitting lower-sector discontinuity changes physical cut closure",
        omitted_lower_sector != physical_cut_datum,
    )

    wrong_sheet_discontinuity = (
        dot(coefficients, vector_scale(Fraction(-1), master_discontinuity))
        + lower_sector_discontinuity
        + subtraction_discontinuity
    )
    assert_true(
        "wrong sheet flips the physical discontinuity",
        wrong_sheet_discontinuity != physical_cut_datum,
    )

    untransported_subtraction = (
        dot(coefficients, master_discontinuity)
        + lower_sector_discontinuity
        - subtraction_discontinuity
    )
    assert_true(
        "subtraction branch must be transported with the amplitude",
        untransported_subtraction != physical_cut_datum,
    )

    coefficient_errors = [Fraction(1, 101), Fraction(1, 103)]
    master_jump_errors = [Fraction(1, 107), Fraction(1, 109)]
    residuals = {
        "state_sum": Fraction(1, 113),
        "coefficients": sum(
            abs(master_discontinuity[index]) * coefficient_errors[index]
            for index in range(2)
        ),
        "master_jump": sum(
            abs(coefficients[index]) * master_jump_errors[index]
            for index in range(2)
        ),
        "lower_sector": Fraction(1, 127),
        "sheet": Fraction(1, 131),
        "subtraction": Fraction(1, 137),
    }
    closure_error = sum(residuals.values(), Fraction(0))
    majorant = sum(abs(value) for value in residuals.values())
    assert_true(
        "master discontinuity closure residual bound",
        abs(closure_error) <= majorant,
    )
    underbudget = majorant - residuals["lower_sector"] - residuals["sheet"]
    assert_true(
        "omitting lower-sector and sheet errors underbudgets physical cut closure",
        closure_error > underbudget,
    )


def check_branch_and_landau_ledger() -> None:
    # In the expansion
    #   Gamma(eps)[exp(i pi eps)-exp(-i pi eps)]/(16 pi^2),
    # the branch jump contributes 2 i pi eps and Gamma(eps) contributes 1/eps.
    # Stripping the common factor i/pi leaves 2/16 = 1/8, matching the
    # massless two-body phase-space coefficient used in the text.
    branch_jump_linear_coefficient = Fraction(2)
    normalization = Fraction(16)
    assert_equal(
        "cut-normalized bubble discontinuity coefficient",
        branch_jump_linear_coefficient / normalization,
        Fraction(1, 8),
    )

    singular_loci = {"bubble_differential_equation": {Fraction(0)}}
    landau_loci = {"massless_two_particle_threshold": {Fraction(0)}}
    assert_equal(
        "bubble differential singularity matches Landau threshold",
        singular_loci["bubble_differential_equation"],
        landau_loci["massless_two_particle_threshold"],
    )


def check_two_master_threshold_mixing() -> None:
    threshold_residue: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0)],
    ]
    zero_matrix: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    assert_equal(
        "nilpotent threshold residue",
        matrix_mul(threshold_residue, threshold_residue),
        zero_matrix,
    )

    log_constants = [Fraction(5, 7), Fraction(11, 13)]
    stripped_monodromy = matrix_vector_mul(threshold_residue, log_constants)
    assert_equal(
        "threshold monodromy feeds second master",
        stripped_monodromy,
        [Fraction(0), Fraction(5, 7)],
    )

    log_coordinate = Fraction(3, 5)
    singular_solution = vector_add(
        log_constants,
        vector_scale(log_coordinate, stripped_monodromy),
    )
    log_derivative = stripped_monodromy
    fuchsian_rhs = matrix_vector_mul(threshold_residue, singular_solution)
    assert_equal(
        "two-master Fuchsian equation residual",
        vector_sub(log_derivative, fuchsian_rhs),
        [Fraction(0), Fraction(0)],
    )

    diagonal_shortcut: Matrix = [
        [threshold_residue[0][0], Fraction(0)],
        [Fraction(0), threshold_residue[1][1]],
    ]
    shortcut_monodromy = matrix_vector_mul(diagonal_shortcut, log_constants)
    assert_true(
        "diagonal one-master shortcut misses threshold mixing",
        shortcut_monodromy != stripped_monodromy,
    )

    amplitude_weights = [Fraction(2, 3), Fraction(-5, 4)]
    exact_discontinuity = dot(amplitude_weights, stripped_monodromy)
    shortcut_discontinuity = dot(amplitude_weights, shortcut_monodromy)
    assert_true(
        "dropping threshold mixing changes amplitude discontinuity",
        exact_discontinuity != shortcut_discontinuity,
    )

    regular_boundary_a = [Fraction(2, 5), Fraction(3, 7)]
    regular_boundary_b = [
        Fraction(2, 5) - Fraction(1, 17),
        Fraction(3, 7) + Fraction(1, 19),
    ]
    value_a = vector_add(regular_boundary_a, singular_solution)
    value_b = vector_add(regular_boundary_b, singular_solution)
    assert_equal(
        "same threshold monodromy under regular boundary shift",
        matrix_vector_mul(threshold_residue, log_constants),
        stripped_monodromy,
    )
    assert_true(
        "cut data do not fix regular boundary constants",
        dot(amplitude_weights, value_a) != dot(amplitude_weights, value_b),
    )

    residuals = {
        "threshold_mixing": abs(exact_discontinuity - shortcut_discontinuity),
        "regular_boundary": abs(dot(amplitude_weights, vector_sub(value_b, value_a))),
    }
    total_difference = (
        exact_discontinuity
        - shortcut_discontinuity
        + dot(amplitude_weights, vector_sub(value_b, value_a))
    )
    majorant = sum(residuals.values(), Fraction(0))
    assert_true("two-master reconstruction residual bound", abs(total_difference) <= majorant)
    underbudget = majorant - residuals["regular_boundary"]
    assert_true(
        "omitting boundary residual underbudgets multi-master comparison",
        abs(total_difference) > underbudget,
    )


def check_two_letter_master_transport() -> None:
    a0: Matrix = [
        [Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0)],
    ]
    a1: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0)],
    ]
    zero_matrix: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    assert_equal(
        "x-letter residue is nilpotent",
        matrix_mul(a0, a0),
        zero_matrix,
    )
    assert_equal(
        "one-minus-x residue is nilpotent",
        matrix_mul(a1, a1),
        zero_matrix,
    )

    commutator = matrix_sub(matrix_mul(a0, a1), matrix_mul(a1, a0))
    assert_equal(
        "two-letter residue commutator",
        commutator,
        [
            [Fraction(1), Fraction(0)],
            [Fraction(0), Fraction(-1)],
        ],
    )

    epsilon = Fraction(1, 11)
    l0 = Fraction(3, 5)
    l1 = Fraction(-4, 9)
    boundary = [Fraction(2, 3), Fraction(5, 7)]
    x_disc_stripped = matrix_vector_mul(a0, boundary)
    one_minus_x_disc_stripped = matrix_vector_mul(a1, boundary)
    assert_equal(
        "x-letter stripped discontinuity",
        x_disc_stripped,
        [Fraction(5, 7), Fraction(0)],
    )
    assert_equal(
        "one-minus-x stripped discontinuity",
        one_minus_x_disc_stripped,
        [Fraction(0), Fraction(2, 3)],
    )

    first_order_action = vector_add(
        vector_scale(l0, x_disc_stripped),
        vector_scale(l1, one_minus_x_disc_stripped),
    )
    transported = vector_add(boundary, vector_scale(epsilon, first_order_action))
    assert_equal(
        "first-order two-letter transport",
        transported,
        [Fraction(163, 231), Fraction(1429, 2079)],
    )
    assert_equal(
        "dlog-x differential equation at first order",
        vector_scale(epsilon, x_disc_stripped),
        matrix_vector_mul(a0, vector_scale(epsilon, boundary)),
    )
    assert_equal(
        "dlog-one-minus-x differential equation at first order",
        vector_scale(epsilon, one_minus_x_disc_stripped),
        matrix_vector_mul(a1, vector_scale(epsilon, boundary)),
    )

    kernel_shift = [Fraction(0), Fraction(1, 5)]
    shifted_boundary = vector_add(boundary, kernel_shift)
    assert_equal(
        "same one-minus-x cut after kernel boundary shift",
        matrix_vector_mul(a1, shifted_boundary),
        one_minus_x_disc_stripped,
    )
    amplitude_weights = [Fraction(7, 13), Fraction(-5, 11)]
    assert_true(
        "cut-only boundary reconstruction misses finite master value",
        dot(amplitude_weights, shifted_boundary) != dot(amplitude_weights, boundary),
    )

    path_order_difference = vector_scale(
        l0 * l1,
        matrix_vector_mul(commutator, boundary),
    )
    assert_equal(
        "second-order path-order commutator contribution",
        path_order_difference,
        [Fraction(-8, 45), Fraction(4, 21)],
    )
    assert_true(
        "forgetting path ordering loses a nonzero master contribution",
        path_order_difference != [Fraction(0), Fraction(0)],
    )

    branch_path_residual = abs(
        dot(amplitude_weights, vector_scale(epsilon * l0, x_disc_stripped))
    )
    boundary_residual = abs(dot(amplitude_weights, kernel_shift))
    residuals = {
        "connection": Fraction(1, 89),
        "boundary": boundary_residual,
        "branch_path": branch_path_residual,
        "lower_sector": Fraction(1, 97),
        "UV_IR": Fraction(1, 101),
        "observable": Fraction(1, 103),
    }
    exact_difference = sum(residuals.values(), Fraction(0))
    majorant = sum(abs(value) for value in residuals.values())
    assert_equal(
        "two-letter transport residual telescope",
        exact_difference,
        majorant,
    )
    underbudget = majorant - residuals["boundary"] - residuals["branch_path"]
    assert_true(
        "omitting boundary and branch residuals underbudgets transport comparison",
        exact_difference > underbudget,
    )


def check_virtual_to_observable_assembly() -> None:
    tree = Fraction(3, 2)
    ir_operator = (Fraction(-5, 3), Fraction(7, 11))
    finite_remainder = Fraction(11, 13)
    real_finite = Fraction(17, 19)

    virtual = laurent_add(
        laurent_scale(tree, ir_operator),
        (Fraction(0), finite_remainder),
    )
    extracted_remainder = laurent_sub(virtual, laurent_scale(tree, ir_operator))
    assert_equal(
        "finite remainder after IR subtraction",
        extracted_remainder,
        (Fraction(0), finite_remainder),
    )

    virtual_cross_section = laurent_scale(2 * tree, virtual)
    integrated_real = laurent_add(
        laurent_scale(-2 * tree * tree, ir_operator),
        (Fraction(0), real_finite),
    )
    assembled = laurent_add(virtual_cross_section, integrated_real)
    expected_finite = 2 * tree * finite_remainder + real_finite
    assert_equal(
        "virtual-real pole cancellation",
        assembled,
        (Fraction(0), expected_finite),
    )
    assert_true(
        "virtual-only contribution still has IR pole",
        virtual_cross_section[0] != 0,
    )

    rational_term = Fraction(5, 17)
    missing_rational_remainder = finite_remainder - rational_term
    missing_rational_observable = 2 * tree * missing_rational_remainder + real_finite
    assert_true(
        "omitting rational term changes finite observable",
        missing_rational_observable != expected_finite,
    )

    finite_scheme_shift = Fraction(4, 9)
    shifted_ir_operator = laurent_add(ir_operator, (Fraction(0), finite_scheme_shift))
    shifted_remainder = finite_remainder - finite_scheme_shift * tree
    shifted_virtual = laurent_add(
        laurent_scale(tree, shifted_ir_operator),
        (Fraction(0), shifted_remainder),
    )
    assert_equal(
        "finite IR-scheme transport leaves virtual amplitude unchanged",
        shifted_virtual,
        virtual,
    )

    shifted_real_finite = real_finite + 2 * tree * tree * finite_scheme_shift
    shifted_observable = 2 * tree * shifted_remainder + shifted_real_finite
    assert_equal(
        "finite IR-scheme transport leaves observable unchanged",
        shifted_observable,
        expected_finite,
    )
    untransported_observable = 2 * tree * shifted_remainder + real_finite
    assert_true(
        "untransported finite IR-scheme shift changes observable",
        untransported_observable != expected_finite,
    )

    residuals = {
        "cut": Fraction(1, 101),
        "rational": Fraction(1, 103),
        "IBP": Fraction(1, 107),
        "UV": Fraction(1, 109),
        "IR_real": Fraction(1, 113),
        "factorization": Fraction(1, 127),
        "measurement": Fraction(1, 131),
    }
    exact_observable = expected_finite + sum(residuals.values(), Fraction(0))
    majorant = sum(abs(value) for value in residuals.values())
    assert_equal(
        "one-loop observable residual telescope",
        exact_observable - expected_finite,
        sum(residuals.values(), Fraction(0)),
    )
    assert_true(
        "one-loop observable reconstruction bound",
        abs(exact_observable - expected_finite) <= majorant,
    )
    underbudget = majorant - abs(residuals["IR_real"]) - abs(residuals["measurement"])
    assert_true(
        "omitted observable residuals underbudget comparison",
        abs(exact_observable - expected_finite) > underbudget,
    )


def check_unresolved_measurement_cell_assembly() -> None:
    born_weight = Fraction(3, 2)
    w0 = Fraction(5, 7)
    w1 = -Fraction(2, 9)
    w2 = Fraction(4, 11)
    virtual_finite = Fraction(13, 17)
    nonsingular_real = Fraction(19, 23)

    # W(x) = w0 + w1 x + w2 x^2, so int_0^1 (W(x)-W(0))/x dx = w1 + w2/2.
    plus_measurement = w1 + Fraction(1, 2) * w2
    assert_equal("unresolved plus-measurement integral", plus_measurement, Fraction(-4, 99))

    virtual_cell = (
        -born_weight * w0,
        born_weight * virtual_finite * w0,
    )
    real_cell = (
        born_weight * w0,
        born_weight * plus_measurement + nonsingular_real,
    )
    assembled_cell = laurent_add(virtual_cell, real_cell)
    expected_finite = (
        born_weight * virtual_finite * w0
        + born_weight * plus_measurement
        + nonsingular_real
    )
    assert_equal(
        "unresolved measurement-cell pole cancellation",
        assembled_cell,
        (Fraction(0), expected_finite),
    )

    resolved_value = w0 + w1 + w2
    wrong_subtraction_real = (
        born_weight * resolved_value,
        born_weight * plus_measurement + nonsingular_real,
    )
    wrong_subtraction_cell = laurent_add(virtual_cell, wrong_subtraction_real)
    assert_true(
        "wrong resolved-event subtraction measurement leaves pole",
        wrong_subtraction_cell[0] != 0,
    )
    assert_equal(
        "wrong subtraction pole coefficient",
        wrong_subtraction_cell[0],
        born_weight * (resolved_value - w0),
    )

    frozen_measurement_real = (
        born_weight * w0,
        nonsingular_real,
    )
    frozen_cell = laurent_add(virtual_cell, frozen_measurement_real)
    assert_true(
        "freezing measurement to reduced event erases finite unresolved term",
        frozen_cell[1] != expected_finite,
    )
    assert_equal(
        "frozen-measurement finite defect",
        expected_finite - frozen_cell[1],
        born_weight * plus_measurement,
    )

    virtual_only_cell = virtual_cell
    assert_true(
        "virtual-only measurement cell keeps unresolved pole",
        virtual_only_cell[0] != 0,
    )

    cutoff_l = Fraction(4)
    larger_cutoff_l = Fraction(8)
    log_weight_integral = -Fraction(1, 2) * cutoff_l * cutoff_l
    larger_log_weight_integral = -Fraction(1, 2) * larger_cutoff_l * larger_cutoff_l
    assert_true(
        "non-infrared-safe log weight grows with unresolved cutoff",
        abs(larger_log_weight_integral) > 3 * abs(log_weight_integral),
    )


def check_two_loop_ir_pole_consistency_gate() -> None:
    tree = Fraction(3, 5)
    ir_one_loop = (Fraction(-7, 3), Fraction(5, 11))
    finite_one_loop = Fraction(13, 17)
    ir_two_loop = (Fraction(11, 7), Fraction(-2, 5), Fraction(19, 23))
    finite_two_loop = Fraction(-29, 31)

    one_loop_amplitude = laurent_add(
        laurent_scale(tree, ir_one_loop),
        (Fraction(0), finite_one_loop),
    )
    one_loop_subtraction_on_one_loop = laurent_product_to_laurent3(
        ir_one_loop,
        one_loop_amplitude,
    )
    two_loop_subtraction_on_tree = laurent3_scale(tree, ir_two_loop)
    two_loop_amplitude = laurent3_add(
        laurent3_add(one_loop_subtraction_on_one_loop, two_loop_subtraction_on_tree),
        (Fraction(0), Fraction(0), finite_two_loop),
    )

    extracted_two_loop_remainder = laurent3_sub(
        laurent3_sub(two_loop_amplitude, one_loop_subtraction_on_one_loop),
        two_loop_subtraction_on_tree,
    )
    assert_equal(
        "two-loop finite remainder after recursive IR subtraction",
        extracted_two_loop_remainder,
        (Fraction(0), Fraction(0), finite_two_loop),
    )

    expanded_lower_loop_ledger = laurent3_add(
        laurent3_add(
            laurent3_scale(tree, laurent_product_to_laurent3(ir_one_loop, ir_one_loop)),
            two_loop_subtraction_on_tree,
        ),
        laurent_to_laurent3(laurent_scale(finite_one_loop, ir_one_loop)),
    )
    expanded_two_loop_amplitude = laurent3_add(
        expanded_lower_loop_ledger,
        (Fraction(0), Fraction(0), finite_two_loop),
    )
    assert_equal(
        "two-loop pole ledger expanded through lower-loop data",
        expanded_two_loop_amplitude,
        two_loop_amplitude,
    )

    missing_i1_a1 = laurent3_sub(two_loop_amplitude, two_loop_subtraction_on_tree)
    assert_true(
        "dropping I1 times A1 leaves two-loop poles",
        missing_i1_a1[0] != 0 or missing_i1_a1[1] != 0,
    )

    i1_finite_only = laurent_to_laurent3(
        laurent_scale(finite_one_loop, ir_one_loop)
    )
    missing_i1_squared_tree = laurent3_sub(
        laurent3_sub(two_loop_amplitude, i1_finite_only),
        two_loop_subtraction_on_tree,
    )
    assert_true(
        "using only I1 times F1 misses the squared one-loop pole",
        missing_i1_squared_tree[0] != 0,
    )

    virtual_virtual = laurent3_add(
        laurent3_scale(2 * tree, two_loop_amplitude),
        laurent_product_to_laurent3(one_loop_amplitude, one_loop_amplitude),
    )
    hard_finite = 2 * tree * finite_two_loop + finite_one_loop * finite_one_loop
    real_virtual_double_real_finite = Fraction(37, 41)
    factorization_finite = Fraction(-5, 37)
    finite_hard_laurent = (
        Fraction(0),
        Fraction(0),
        hard_finite,
    )
    unresolved_subtractions = laurent3_add(
        laurent3_scale(-1, laurent3_sub(virtual_virtual, finite_hard_laurent)),
        (
            Fraction(0),
            Fraction(0),
            real_virtual_double_real_finite + factorization_finite,
        ),
    )
    assembled_observable = laurent3_add(virtual_virtual, unresolved_subtractions)
    expected_observable = (
        hard_finite
        + real_virtual_double_real_finite
        + factorization_finite
    )
    assert_equal(
        "NNLO virtual-real-real pole cancellation",
        assembled_observable,
        (Fraction(0), Fraction(0), expected_observable),
    )
    assert_true(
        "NNLO virtual-only contribution still has IR poles",
        virtual_virtual[0] != 0 or virtual_virtual[1] != 0,
    )

    omitted_lower_loop_hard_square = (
        2 * tree * finite_two_loop
        + real_virtual_double_real_finite
        + factorization_finite
    )
    assert_true(
        "omitting the one-loop hard square changes the NNLO observable",
        omitted_lower_loop_hard_square != expected_observable,
    )

    residuals = {
        "cut2": Fraction(1, 137),
        "rational2": Fraction(1, 139),
        "IBP2": Fraction(1, 149),
        "master2": Fraction(1, 151),
        "lower1": Fraction(1, 157),
        "UV2": Fraction(1, 163),
        "IR_RV_RR2": Fraction(1, 167),
        "factorization2": Fraction(1, 173),
        "measurement2": Fraction(1, 179),
    }
    exact_observable = expected_observable + sum(residuals.values(), Fraction(0))
    majorant = sum(abs(value) for value in residuals.values())
    assert_true(
        "two-loop observable reconstruction bound",
        abs(exact_observable - expected_observable) <= majorant,
    )
    underbudget = majorant - abs(residuals["lower1"]) - abs(residuals["IR_RV_RR2"])
    assert_true(
        "two-loop residual budget must include lower-loop and IR real sectors",
        abs(exact_observable - expected_observable) > underbudget,
    )


def main() -> None:
    check_phi4_cut_reconstruction()
    check_phi4_ms_running_from_crossed_cuts()
    check_one_loop_reconstruction_datum()
    check_four_dimensional_cut_blind_spot()
    check_gauge_theory_helicity_controls()
    check_mu4_dimension_shift_rational_residue()
    check_n4_mhv_quadruple_cut_reconstruction()
    check_triple_cut_triangle_projection_after_box_subtraction()
    check_five_gluon_all_plus_rational_template()
    check_four_point_color_kinematics_gateway()
    check_loop_level_color_kinematics_surface_obstruction()
    check_loop_level_jacobi_repair_double_copy_null()
    check_finite_two_scale_box_master()
    check_bubble_ibp_identity()
    check_bubble_numerator_sector_projection()
    check_equal_mass_bubble_threshold_family()
    check_two_loop_sunrise_elliptic_maximal_cut()
    check_multi_loop_maximal_cut_sector_projection()
    check_dual_contour_master_coefficient_extraction()
    check_master_discontinuity_closure_gate()
    check_branch_and_landau_ledger()
    check_two_master_threshold_mixing()
    check_two_letter_master_transport()
    check_virtual_to_observable_assembly()
    check_unresolved_measurement_cell_assembly()
    check_two_loop_ir_pole_consistency_gate()
    print("All generalized unitarity and loop-reduction checks passed.")


if __name__ == "__main__":
    main()
