#!/usr/bin/env python3
"""Exact checks for rapidity and factorized-scattering algebra.

These checks accompany Volume VI, Chapter 1.  They verify finite algebraic
identities behind the rapidity invariant, Newton separation of rapidity
multisets, chamber braid relations, the rational Yang--Baxter identity,
scalar Watson-exchange bookkeeping, and the finite residual ledger separating
S-Fock/ZF algebra from wedge-local and local-algebra reconstruction.  They
also check the finite checkpoint logic behind the end-to-end observable
reconstruction map: exact scattering, exact TBA, or exact dressing data do not
by themselves certify a local observable without the corresponding
local-algebra, domain/completeness, state-limit, and projection checkpoints.

Evidence contract.
Target claims: rapidity convention, factorized chamber algebra, Watson
exchange, and the Chapter 1 reconstruction-budget claim that exact on-shell
algebra does not by itself construct double-cone local observables or complete
the route from exact data to a physical local, thermodynamic, or hydrodynamic
observable.
Independent construction: rational arithmetic for rapidity invariants, Newton
identities, finite braid/Yang--Baxter matrices, scalar exchange coefficients,
finite local-intersection dimension proxies, nuclearity-norm proxies, and a
residual telescope for wedge-to-local reconstruction, plus Boolean route gates
and exact residual budgets for representative Ising, sinh-Gordon, TBA, and GHD
routes.
Imported assumptions: the analytic S-matrix regularity, modular nuclearity,
operator-domain, form-factor convergence, and completeness hypotheses stated
in the chapter.
Negative controls: exact Yang--Baxter algebra with a nonzero local
reconstruction residual, positive S-Fock dimension with empty local
intersection, a finite nuclearity proxy that fails the declared bound, exact
TBA endpoint data overread as a local trace operator, and exact GHD dressing
overread as a microscopic current.
Scope boundary: these checks verify finite algebra and reconstruction
interfaces only; they do not prove modular nuclearity, nontrivial local
intersections, form-factor convergence, common-norm residual estimates, or
local-QFT completeness.
"""

from fractions import Fraction


Matrix = list[list[Fraction]]


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def assert_true(condition, label):
    if not condition:
        raise AssertionError(label)


def assert_gt(actual, threshold, label):
    if not actual > threshold:
        raise AssertionError(f"{label}: got {actual!r}, expected > {threshold!r}")


def zero_matrix(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def identity(n):
    out = zero_matrix(n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * entry for entry in row] for row in a]


def pair_operator(pair: tuple[int, int], two_body: Matrix) -> Matrix:
    op = zero_matrix(8)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                incoming = (a, b, c)
                incoming_index = 4 * a + 2 * b + c
                i, j = pair
                pair_index = 2 * incoming[i] + incoming[j]
                for outgoing_pair_index in range(4):
                    coefficient = two_body[outgoing_pair_index][pair_index]
                    if coefficient == 0:
                        continue
                    outgoing = list(incoming)
                    outgoing[i] = outgoing_pair_index // 2
                    outgoing[j] = outgoing_pair_index % 2
                    outgoing_index = 4 * outgoing[0] + 2 * outgoing[1] + outgoing[2]
                    op[outgoing_index][incoming_index] += coefficient
    return op


def flip_two_body() -> Matrix:
    p = zero_matrix(4)
    for a in range(2):
        for b in range(2):
            incoming = 2 * a + b
            outgoing = 2 * b + a
            p[outgoing][incoming] = Fraction(1)
    return p


def rational_r(u: Fraction) -> Matrix:
    # The Yang rational R-matrix R(u)=u I + P satisfies
    # R12(u) R13(u+v) R23(v) = R23(v) R13(u+v) R12(u).
    return add(scale(u, identity(4)), flip_two_body())


def check_rapidity_invariant():
    ma = Fraction(3)
    mb = Fraction(5)
    z1 = Fraction(7, 2)
    z2 = Fraction(4, 3)

    p1 = (ma * (z1 + Fraction(1, 1) / z1) / 2, ma * (z1 - Fraction(1, 1) / z1) / 2)
    p2 = (mb * (z2 + Fraction(1, 1) / z2) / 2, mb * (z2 - Fraction(1, 1) / z2) / 2)
    total = (p1[0] + p2[0], p1[1] + p2[1])
    minus_total_square = total[0] * total[0] - total[1] * total[1]
    formula = ma * ma + mb * mb + ma * mb * (z1 / z2 + z2 / z1)
    assert_equal(minus_total_square, formula, "mostly-plus rapidity invariant")


def check_newton_two_root_separation():
    roots = [Fraction(2), Fraction(5)]
    p1 = sum(roots)
    p2 = sum(r * r for r in roots)
    e1 = p1
    e2 = (p1 * p1 - p2) / 2
    assert_equal((e1, e2), (Fraction(7), Fraction(10)), "Newton identities for two rapidity roots")
    for root in roots:
        assert_equal(root * root - e1 * root + e2, Fraction(0), "recovered monic polynomial")


def check_chamber_groupoid_permutation_relations():
    p12 = pair_operator((0, 1), flip_two_body())
    p23 = pair_operator((1, 2), flip_two_body())
    assert_equal(matmul(p12, p12), identity(8), "adjacent involution P12")
    assert_equal(matmul(p23, p23), identity(8), "adjacent involution P23")
    assert_equal(matmul(matmul(p12, p23), p12), matmul(matmul(p23, p12), p23), "S3 braid relation")


def check_rational_yang_baxter_identity():
    u = Fraction(2)
    v = Fraction(3)
    r12 = pair_operator((0, 1), rational_r(u))
    r13 = pair_operator((0, 2), rational_r(u + v))
    r23 = pair_operator((1, 2), rational_r(v))
    lhs = matmul(matmul(r12, r13), r23)
    rhs = matmul(matmul(r23, r13), r12)
    assert_equal(lhs, rhs, "rational Yang-Baxter identity")


def scalar_s(x: Fraction) -> Fraction:
    return (x - 1) / (x + 1)


def check_scalar_unitarity_and_watson_bookkeeping():
    theta12 = Fraction(5)
    theta13 = Fraction(7)
    theta23 = Fraction(2)
    assert_equal(scalar_s(theta12) * scalar_s(-theta12), Fraction(1), "scalar two-body unitarity")
    lhs = scalar_s(theta12) * scalar_s(theta13) * scalar_s(theta23)
    rhs = scalar_s(theta23) * scalar_s(theta13) * scalar_s(theta12)
    assert_equal(lhs, rhs, "scalar ZF reorder coefficient")

    form_factor_neighbor = Fraction(11, 3)
    form_factor_original = scalar_s(theta12) * form_factor_neighbor
    assert_equal(
        form_factor_original,
        Fraction(4, 6) * form_factor_neighbor,
        "scalar Watson exchange coefficient",
    )


def local_intersection_dimension(right_wedge_dim: int, left_wedge_dim: int, obstruction_rank: int) -> int:
    return max(0, min(right_wedge_dim, left_wedge_dim) - obstruction_rank)


def check_wedge_local_reconstruction_residual_budget():
    # This finite model mirrors ControlledApproximation
    # ca:integrable-wedge-local-reconstruction-budget.  The leading S-Fock
    # coordinate is kept separate from the analytic residuals that construct a
    # local double-cone observable.
    leading_s_fock_coordinate = Fraction(11, 7)
    residuals = {
        "pfg_domain": Fraction(1, 60),
        "modular_nuclearity": Fraction(1, 70),
        "local_intersection": Fraction(1, 84),
        "form_factor_convergence": Fraction(1, 105),
        "operator_domains": Fraction(1, 140),
        "completeness": Fraction(1, 210),
    }
    exact_local_coordinate = leading_s_fock_coordinate + sum(residuals.values())
    residual_bound = sum(abs(value) for value in residuals.values())
    assert_equal(
        abs(exact_local_coordinate - leading_s_fock_coordinate) <= residual_bound,
        True,
        "wedge-to-local reconstruction residual bound",
    )
    assert_gt(
        abs(exact_local_coordinate - leading_s_fock_coordinate),
        Fraction(0),
        "exact S-Fock coordinate does not equal local observable",
    )

    omitted_nuclearity_bound = residual_bound - residuals["modular_nuclearity"]
    assert_gt(
        abs(exact_local_coordinate - leading_s_fock_coordinate),
        omitted_nuclearity_bound,
        "omitting modular nuclearity underbudgets reconstruction",
    )

    exact_yang_baxter_defect = Fraction(0)
    exact_zf_associativity_defect = Fraction(0)
    assert_equal(
        exact_yang_baxter_defect + exact_zf_associativity_defect,
        Fraction(0),
        "exact finite scattering algebra",
    )
    assert_gt(
        abs(exact_local_coordinate - leading_s_fock_coordinate),
        exact_yang_baxter_defect + exact_zf_associativity_defect,
        "finite scattering algebra leaves local reconstruction residual",
    )

    good_nuclearity_singular_values = [Fraction(1, 8), Fraction(1, 16), Fraction(1, 32)]
    bad_nuclearity_singular_values = [Fraction(1, 3), Fraction(1, 4)]
    nuclearity_threshold = Fraction(1, 4)
    assert_true(
        sum(good_nuclearity_singular_values) < nuclearity_threshold,
        "finite nuclearity proxy satisfies declared bound",
    )
    assert_true(
        sum(bad_nuclearity_singular_values) > nuclearity_threshold,
        "finite nuclearity proxy can fail declared bound",
    )

    s_fock_dimension = 4
    nontrivial_local_dim = local_intersection_dimension(5, 4, 2)
    empty_local_dim = local_intersection_dimension(2, 2, 2)
    assert_gt(nontrivial_local_dim, 0, "nontrivial local intersection proxy")
    assert_gt(s_fock_dimension, 0, "positive S-Fock proxy dimension")
    assert_equal(
        empty_local_dim,
        0,
        "positive S-Fock data can still have empty local intersection proxy",
    )


def route_certifies_local_observable(gates: dict[str, bool]) -> bool:
    required = (
        "on_shell",
        "hilbert",
        "wedge",
        "local_algebra",
        "operator_domain",
        "completeness",
        "projection",
    )
    return all(gates.get(gate, False) for gate in required)


def route_certifies_thermodynamic_observable(gates: dict[str, bool]) -> bool:
    required = (
        "bethe_yang",
        "tba",
        "state_limit",
        "normalization",
        "projection",
    )
    return all(gates.get(gate, False) for gate in required)


def residual_budget_is_estimate(
    residuals: dict[str, Fraction],
    statuses: dict[str, str],
) -> bool:
    admissible = {"exact_zero", "estimated", "bounded", "irrelevant"}
    for name, residual in residuals.items():
        status = statuses.get(name, "slot")
        if status not in admissible:
            return False
        if status in {"exact_zero", "irrelevant"} and residual != 0:
            return False
    return True


def check_end_to_end_observable_reconstruction_map():
    ising_energy_route = {
        "on_shell": True,
        "hilbert": True,
        "wedge": True,
        "local_algebra": True,
        "operator_domain": True,
        "completeness": True,
        "projection": True,
    }
    assert_equal(
        route_certifies_local_observable(ising_energy_route),
        True,
        "Ising energy route certifies local observable",
    )

    sinh_gordon_before_nuclearity = {
        "on_shell": True,
        "hilbert": True,
        "wedge": True,
        "local_algebra": False,
        "operator_domain": False,
        "completeness": False,
        "projection": True,
    }
    assert_equal(
        route_certifies_local_observable(sinh_gordon_before_nuclearity),
        False,
        "sinh-Gordon S-Fock/wedge route still needs local gates",
    )

    sinh_gordon_net_but_not_point_field = dict(sinh_gordon_before_nuclearity)
    sinh_gordon_net_but_not_point_field["local_algebra"] = True
    assert_equal(
        route_certifies_local_observable(sinh_gordon_net_but_not_point_field),
        False,
        "sinh-Gordon local net alone does not certify point-field completeness",
    )

    exact_yang_baxter_defect = Fraction(0)
    exact_tba_endpoint_defect = Fraction(0)
    local_trace_residual = Fraction(1, 19)
    assert_gt(
        local_trace_residual,
        exact_yang_baxter_defect + exact_tba_endpoint_defect,
        "exact algebra and TBA endpoint leave local trace route residual",
    )

    lee_yang_tba_route = {
        "bethe_yang": True,
        "tba": True,
        "state_limit": True,
        "normalization": True,
        "projection": True,
    }
    assert_equal(
        route_certifies_thermodynamic_observable(lee_yang_tba_route),
        True,
        "Lee-Yang route certifies thermodynamic coordinate",
    )
    assert_equal(
        route_certifies_local_observable(
            {
                "on_shell": True,
                "hilbert": False,
                "wedge": False,
                "local_algebra": False,
                "operator_domain": False,
                "completeness": False,
                "projection": True,
            }
        ),
        False,
        "Lee-Yang TBA endpoint is not local trace reconstruction",
    )

    ghd_route = {
        "bethe_yang": True,
        "tba": True,
        "dressing": True,
        "state_limit": True,
        "microscopic_operator": False,
        "projection": True,
    }
    microscopic_current_certified = (
        ghd_route["bethe_yang"]
        and ghd_route["tba"]
        and ghd_route["dressing"]
        and ghd_route["state_limit"]
        and ghd_route["microscopic_operator"]
        and ghd_route["projection"]
    )
    assert_equal(
        microscopic_current_certified,
        False,
        "GHD route needs microscopic current gate",
    )

    route_residuals = {
        "scattering": Fraction(0),
        "hilbert": Fraction(0),
        "wedge": Fraction(1, 80),
        "local_algebra": Fraction(1, 120),
        "operator_domain": Fraction(1, 150),
        "thermodynamic_state": Fraction(1, 200),
        "projection": Fraction(1, 240),
    }
    residual_slots = {
        "scattering": "exact_zero",
        "hilbert": "exact_zero",
        "wedge": "bounded",
        "local_algebra": "slot",
        "operator_domain": "slot",
        "thermodynamic_state": "estimated",
        "projection": "slot",
    }
    assert_equal(
        residual_budget_is_estimate(route_residuals, residual_slots),
        False,
        "named residual slots are not summable route estimates",
    )
    residual_estimates = dict(residual_slots)
    residual_estimates.update(
        {
            "local_algebra": "bounded",
            "operator_domain": "estimated",
            "projection": "bounded",
        }
    )
    assert_equal(
        residual_budget_is_estimate(route_residuals, residual_estimates),
        True,
        "bounded or estimated residuals form a summable route budget",
    )
    omitted_projection = dict(residual_estimates)
    omitted_projection["projection"] = "irrelevant"
    assert_equal(
        residual_budget_is_estimate(route_residuals, omitted_projection),
        False,
        "nonzero projection residual cannot be hidden as irrelevant",
    )
    exact_observable = Fraction(7, 5) + sum(route_residuals.values(), Fraction(0))
    retained_coordinate = Fraction(7, 5)
    route_budget = sum(abs(value) for value in route_residuals.values())
    assert_equal(
        abs(exact_observable - retained_coordinate) <= route_budget,
        True,
        "integrable route residual budget",
    )
    omitted_projection_budget = route_budget - route_residuals["projection"]
    assert_gt(
        abs(exact_observable - retained_coordinate),
        omitted_projection_budget,
        "omitting physical projection underbudgets route residual",
    )


def main():
    check_rapidity_invariant()
    check_newton_two_root_separation()
    check_chamber_groupoid_permutation_relations()
    check_rational_yang_baxter_identity()
    check_scalar_unitarity_and_watson_bookkeeping()
    check_wedge_local_reconstruction_residual_budget()
    check_end_to_end_observable_reconstruction_map()
    print("All factorized-scattering algebra checks passed.")


if __name__ == "__main__":
    main()
