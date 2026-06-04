#!/usr/bin/env python3
r"""Exact arithmetic checks for Volume VI integrable RG-flow conventions.

Evidence contract.
Target claims: the perturbed-CFT and integrable-RG-flow arithmetic in Volume
VI Chapter 6, including the \(\phi_{1,3}\) Kac data, minimal-model
central-charge drops, polynomial scalar Landau-Ginzburg multicritical ledger,
source-scaling and massless-dispersion signs, the Zamolodchikov trace
sum-rule coefficient \(9/E^4\), the minimal-flow central-charge targets, and
the retained trace-form-factor \(c\)-sum residual bound.
Independent construction: the checks recompute Kac weights, source exponents,
central charges, radial-integral coefficients, toy spectral atoms, and
residual decompositions directly with exact rational arithmetic rather than
reading chapter display strings.
Imported assumptions: the tests use the unitary minimal-model central-charge
formula, the chapter's stress-tensor normalization, positivity of retained
trace spectral weights, and declared nonnegative reconstruction residuals for
particle tails, rapidity tails, contact/source extensions, Fubini exchange,
local operator reconstruction, trace normalization, and TBA endpoint
identification.
Negative controls: wrong signs or coefficients, missing residual terms,
exact TBA endpoint matching overread as a local observable reconstruction, and
signed-cancellation pseudo-bounds are rejected.
Scope boundary: a pass checks finite arithmetic and reconstruction-budget
bookkeeping; it does not prove existence of a local QFT, analytic convergence
of a form-factor expansion, trace-operator normalization in a concrete model,
or the TBA/vacuum-energy identification theorem.
"""

from __future__ import annotations

from fractions import Fraction

from check_utils import assert_gt as assert_gt_bound
from check_utils import assert_leq as assert_leq_bound


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got}, expected {expected}")


def minimal_c(m: int) -> Fraction:
    return Fraction(1, 1) - Fraction(6, m * (m + 1))


def kac_weight(m: int, r: int, s: int) -> Fraction:
    numerator = ((m + 1) * r - m * s) ** 2 - 1
    denominator = 4 * m * (m + 1)
    return Fraction(numerator, denominator)


def check_phi_13_data() -> None:
    for m in range(3, 20):
        h_13 = kac_weight(m, 1, 3)
        delta_13 = 2 * h_13
        y_13 = Fraction(2, 1) - delta_13
        assert_equal(f"h_13 for m={m}", h_13, Fraction(m - 1, m + 1))
        assert_equal(
            f"Delta_13 for m={m}",
            delta_13,
            Fraction(2 * (m - 1), m + 1),
        )
        assert_equal(f"y_13 for m={m}", y_13, Fraction(4, m + 1))


def check_minimal_model_c_drops() -> None:
    for m in range(4, 20):
        drop = minimal_c(m) - minimal_c(m - 1)
        assert_equal(
            f"minimal-model c drop m={m}",
            drop,
            Fraction(12, m * (m * m - 1)),
        )

    assert_equal("Ising central charge", minimal_c(3), Fraction(1, 2))
    assert_equal("tricritical Ising central charge", minimal_c(4), Fraction(7, 10))
    assert_equal(
        "tricritical-to-Ising c drop",
        minimal_c(4) - minimal_c(3),
        Fraction(1, 5),
    )
    assert_equal("three-state Potts central charge", minimal_c(5), Fraction(4, 5))
    assert_equal(
        "Potts-to-tricritical-Ising c drop",
        minimal_c(5) - minimal_c(4),
        Fraction(1, 10),
    )


def check_polynomial_scalar_lg_multicritical_ledger() -> None:
    for m in range(3, 20):
        highest_degree = 2 * m - 2
        eom_descendant_power = highest_degree - 1
        order_field_basis_count = eom_descendant_power
        even_coupling_count = m - 1
        dimensionless_even_ratios = even_coupling_count - 1

        assert_equal(
            f"LG highest degree K=2m-2 m={m}",
            Fraction(highest_degree, 1),
            Fraction(2 * m - 2, 1),
        )
        assert_equal(
            f"LG EOM descendant power m={m}",
            Fraction(eom_descendant_power, 1),
            Fraction(2 * m - 3, 1),
        )
        assert_equal(
            f"LG order-field quotient count m={m}",
            Fraction(order_field_basis_count, 1),
            Fraction(2 * m - 3, 1),
        )
        assert_equal(
            f"LG even tuning ratios m={m}",
            Fraction(dimensionless_even_ratios, 1),
            Fraction(m - 2, 1),
        )

        # The proposed multicritical endpoint is the unitary minimal model
        # M(m,m+1); this check guards only the arithmetic used in the
        # interface, not the theorem-level RG construction.
        c_value = minimal_c(m)
        assert_equal(
            f"LG minimal-model c formula m={m}",
            c_value,
            Fraction(1, 1) - Fraction(6, m * (m + 1)),
        )

    assert_equal("Ising LG order-field count", Fraction(2 * 3 - 3, 1), Fraction(3, 1))
    assert_equal("tricritical LG order-field count", Fraction(2 * 4 - 3, 1), Fraction(5, 1))


def check_kac_identification_for_phi_13() -> None:
    for m in range(3, 20):
        identified = (m - 1, m - 2)
        assert_equal(
            f"Kac identification h_13 m={m}",
            kac_weight(m, 1, 3),
            kac_weight(m, identified[0], identified[1]),
        )


def check_source_scaling_linearization() -> None:
    # lambda(mu) = mu^{-y} g has mu d_lambda/d_mu = -y lambda.
    for m in range(3, 20):
        y = Fraction(4, m + 1)
        derivative_over_lambda = -y
        length_flow_over_lambda = y
        assert_equal(
            f"source beta sign m={m}",
            derivative_over_lambda,
            -Fraction(4, m + 1),
        )
        assert_equal(
            f"length-flow sign m={m}",
            length_flow_over_lambda,
            Fraction(4, m + 1),
        )


def check_massless_dispersion_identities() -> None:
    # Use rational e^theta samples q.  Right movers have E=p=M q/2;
    # left movers have E=-p=M/(2q).  Both are exactly null.
    for q in (Fraction(1, 3), Fraction(2, 1), Fraction(5, 2)):
        m_scale = Fraction(7, 1)
        e_right = m_scale * q / 2
        p_right = e_right
        e_left = m_scale / (2 * q)
        p_left = -e_left
        assert_equal(
            f"right mover null q={q}",
            e_right * e_right - p_right * p_right,
            Fraction(0, 1),
        )
        assert_equal(
            f"left mover null q={q}",
            e_left * e_left - p_left * p_left,
            Fraction(0, 1),
        )


def check_trace_sum_rule_coefficient() -> None:
    # In the normalization used in the chapter,
    # (3/(4 pi)) * (2 pi) * int_0^infty rho^3 exp(-E rho) d rho
    # = 9 / E^4.  We keep only exact rational coefficients; the common
    # factor of pi cancels between the prefactor and angular integral.
    radial_factor = Fraction(6, 1)
    angular_times_prefactor = Fraction(3, 2)
    assert_equal(
        "trace sum-rule spectral coefficient",
        angular_times_prefactor * radial_factor,
        Fraction(9, 1),
    )

    for energy in (Fraction(1, 1), Fraction(3, 2), Fraction(5, 1)):
        got = angular_times_prefactor * radial_factor / (energy**4)
        assert_equal(
            f"trace sum-rule energy weight E={energy}",
            got,
            Fraction(9, 1) / (energy**4),
        )


def check_phi13_trace_sum_rule_targets() -> None:
    for m in range(4, 20):
        delta_c = minimal_c(m) - minimal_c(m - 1)
        assert_equal(
            f"phi13 c-theorem target m={m}",
            delta_c,
            Fraction(12, m * (m * m - 1)),
        )

        # A single positive toy spectral atom with squared form factor
        # delta_c E^4 / 9 would reproduce the displayed sum-rule target.
        # This is not a physical truncation; it guards the coefficient and
        # the direction of the central-charge drop.
        energy = Fraction(m + 2, m)
        spectral_atom = delta_c * (energy**4) / 9
        reconstructed = Fraction(9, 1) * spectral_atom / (energy**4)
        assert_equal(
            f"toy trace spectral atom reconstructs delta c m={m}",
            reconstructed,
            delta_c,
        )


def check_trace_c_sum_rule_reconstruction_bound() -> None:
    # Tricritical Ising to Ising supplies a concrete positive target
    # Delta c = 1/5.  The retained coordinate below is intentionally
    # incomplete; the residual bound must keep the omitted observable and
    # endpoint/normalization residuals visible.
    delta_c_loc = minimal_c(4) - minimal_c(3)
    retained_sequence = [
        Fraction(1, 10),
        Fraction(3, 20),
        Fraction(7, 40),
    ]
    retained = retained_sequence[-1]
    assert_equal("tricritical-to-Ising target for residual bound", delta_c_loc, Fraction(1, 5))

    for earlier, later in zip(retained_sequence, retained_sequence[1:]):
        assert_leq_bound(
            "positive retained c-sum approximants are monotone",
            earlier,
            later,
            tol=Fraction(0, 1),
        )
    assert_leq_bound(
        "retained positive c-sum stays below full positive target",
        retained,
        delta_c_loc,
        tol=Fraction(0, 1),
    )

    observable_residuals = {
        "particle-tail": Fraction(1, 80),
        "rapidity-tail": Fraction(1, 160),
        "contact-source-extension": Fraction(1, 320),
        "fubini-domination": Fraction(1, 640),
        "local-operator-reconstruction": Fraction(1, 640),
    }
    observable_budget = sum(observable_residuals.values(), Fraction(0, 1))
    observable_error = abs(delta_c_loc - retained)
    assert_equal("trace c-sum observable residual telescope", observable_error, observable_budget)
    assert_leq_bound(
        "trace c-sum observable residual bound",
        observable_error,
        observable_budget,
        tol=Fraction(0, 1),
    )

    trace_normalization_residual = Fraction(1, 320)
    tba_endpoint_residual = Fraction(1, 640)
    tba_delta = delta_c_loc + trace_normalization_residual + tba_endpoint_residual
    comparison_error = abs(tba_delta - retained)
    comparison_budget = observable_budget + trace_normalization_residual + tba_endpoint_residual
    assert_equal("trace c-sum TBA comparison residual telescope", comparison_error, comparison_budget)
    assert_leq_bound(
        "trace c-sum TBA comparison residual bound",
        comparison_error,
        comparison_budget,
        tol=Fraction(0, 1),
    )

    assert_gt_bound(
        "exact endpoint match still leaves local observable residual",
        abs(delta_c_loc - retained),
        Fraction(0, 1),
    )
    assert_gt_bound(
        "omitted trace normalization underbudgets TBA comparison",
        comparison_error,
        comparison_budget - trace_normalization_residual,
    )
    assert_gt_bound(
        "omitted local reconstruction underbudgets observable comparison",
        observable_error,
        observable_budget - observable_residuals["local-operator-reconstruction"],
    )

    signed_residuals = [Fraction(1, 80), -Fraction(1, 80)]
    signed_budget = sum(signed_residuals, Fraction(0, 1))
    absolute_budget = sum((abs(term) for term in signed_residuals), Fraction(0, 1))
    assert_equal("signed residual cancellation vanishes", signed_budget, Fraction(0, 1))
    assert_gt_bound(
        "signed cancellation hides nonzero positive residual mass",
        absolute_budget,
        signed_budget,
    )


def main() -> None:
    check_phi_13_data()
    check_minimal_model_c_drops()
    check_polynomial_scalar_lg_multicritical_ledger()
    check_kac_identification_for_phi_13()
    check_source_scaling_linearization()
    check_massless_dispersion_identities()
    check_trace_sum_rule_coefficient()
    check_phi13_trace_sum_rule_targets()
    check_trace_c_sum_rule_reconstruction_bound()
    print("All integrable RG-flow checks passed.")


if __name__ == "__main__":
    main()
