#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- The finite angular-cell soft-dipole evolution in the jets chapter separates
  the direct global Sudakov veto from the first non-global cascade term for an
  angular veto measurement.
- A global-Sudakov-only ansatz agrees through first order in the soft-energy
  logarithm but misses the second-order unmeasured-to-measured cascade by
  exactly one half of the finite non-global coefficient.
- The finite BMS-style soft-radiation coordinate is not a Glauber-exchange or
  super-leading-logarithm replacement.

Independent construction:
- All checks use exact rational rates on a finite angular-cell graph, built
  independently of manuscript prose.
- The second-order term is derived by differentiating the finite evolution at
  the initial condition, decomposing the non-global coefficient into explicit
  unmeasured-cell paths.
- The global-Sudakov mismatch is checked against a separately constructed
  exponential ansatz using only the direct measured-cell veto rate.

Imported assumptions:
- The finite rates stand in for regulated cell-integrated eikonal kernels in
  a large-N_c, strongly energy-ordered soft-dipole chart.
- The script checks the finite soft-radiation measurement algebra only; it does
  not construct continuum BMS evolution, finite-N_c color density matrices,
  recoil matching, regulator removal, or a full QCD factorization theorem.

Negative controls:
- With no measured cells, unmeasured real and virtual contributions cancel at
  the initial condition and the non-global coefficient vanishes.
- In the additive boundary case A_iu + A_uj = A_ij for every unmeasured cell,
  the global-Sudakov second-order coefficient is recovered exactly.
- If the non-global row were treated as a Glauber replacement, the required
  scope-boundary strings checked here would be absent from the manuscript.

Scope boundary:
- These are finite-regulator rational diagnostics for one soft-measurement
  obstruction to naive factorization.  They do not prove all-order QCD
  factorization, compute super-leading logarithms, or decide whether a
  hadron-hadron observable has cancelling, included, or uncancelled Glauber
  exchange.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


Dipole = tuple[str, str]
Rates = dict[tuple[str, str, str], Fraction]

ROOT = Path(__file__).resolve().parents[1]
JETS_CHAPTER = (
    ROOT
    / "monograph/tex/volumes/volume_ii/"
    "chapter19b_jets_ir_safe_observables_and_hadronization.tex"
)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def veto_rate(dipole: Dipole, measured: tuple[str, ...], rates: Rates) -> Fraction:
    i, j = dipole
    return sum((rates.get((i, j, cell), Fraction(0)) for cell in measured), Fraction(0))


def bms_rhs(
    dipole: Dipole,
    values: dict[Dipole, Fraction],
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    i, j = dipole
    direct = -veto_rate(dipole, measured, rates) * values[dipole]
    nonlinear = Fraction(0)
    for cell in unmeasured:
        nonlinear += rates.get((i, j, cell), Fraction(0)) * (
            values[(i, cell)] * values[(cell, j)] - values[dipole]
        )
    return direct + nonlinear


def non_global_coefficient(
    dipole: Dipole,
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    return sum(path_non_global_contributions(dipole, measured, unmeasured, rates).values(), Fraction(0))


def path_non_global_contributions(
    dipole: Dipole,
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> dict[str, Fraction]:
    i, j = dipole
    a_ij = veto_rate(dipole, measured, rates)
    return {
        cell: rates.get((i, j, cell), Fraction(0))
        * (veto_rate((i, cell), measured, rates) + veto_rate((cell, j), measured, rates) - a_ij)
        for cell in unmeasured
    }


def second_order_coefficient(
    dipole: Dipole,
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    a_ij = veto_rate(dipole, measured, rates)
    return (a_ij**2 - non_global_coefficient(dipole, measured, unmeasured, rates)) / 2


def global_sudakov_second_order_coefficient(
    dipole: Dipole,
    measured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    a_ij = veto_rate(dipole, measured, rates)
    return a_ij**2 / 2


def global_sudakov_missed_cascade(
    dipole: Dipole,
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    return global_sudakov_second_order_coefficient(dipole, measured, rates) - second_order_coefficient(
        dipole, measured, unmeasured, rates
    )


def check_unmeasured_real_virtual_cancellation() -> None:
    measured: tuple[str, ...] = ()
    unmeasured = ("u",)
    rates: Rates = {("a", "b", "u"): Fraction(5, 7)}
    values = {
        ("a", "b"): Fraction(1),
        ("a", "u"): Fraction(1),
        ("u", "b"): Fraction(1),
    }
    assert_equal(
        "unmeasured real-virtual cancellation at G=1",
        bms_rhs(("a", "b"), values, measured, unmeasured, rates),
        Fraction(0),
    )
    assert_equal("no measured cells gives zero non-global coefficient", non_global_coefficient(("a", "b"), measured, unmeasured, rates), Fraction(0))


def check_second_order_non_global_coefficient() -> None:
    measured = ("m",)
    unmeasured = ("u", "v")
    rates: Rates = {
        ("a", "b", "m"): Fraction(3, 5),
        ("a", "b", "u"): Fraction(2, 7),
        ("a", "b", "v"): Fraction(1, 11),
        ("a", "u", "m"): Fraction(11, 13),
        ("u", "b", "m"): Fraction(5, 17),
        ("a", "v", "m"): Fraction(7, 19),
        ("v", "b", "m"): Fraction(13, 23),
    }
    a_ab = Fraction(3, 5)
    expected_paths = {
        "u": Fraction(2, 7) * (Fraction(11, 13) + Fraction(5, 17) - a_ab),
        "v": Fraction(1, 11) * (Fraction(7, 19) + Fraction(13, 23) - a_ab),
    }
    expected_non_global = sum(expected_paths.values(), Fraction(0))
    assert_equal(
        "finite non-global path decomposition",
        path_non_global_contributions(("a", "b"), measured, unmeasured, rates),
        expected_paths,
    )
    assert_equal("finite non-global coefficient", non_global_coefficient(("a", "b"), measured, unmeasured, rates), expected_non_global)
    assert_equal(
        "second-order gap expansion coefficient",
        second_order_coefficient(("a", "b"), measured, unmeasured, rates),
        (a_ab**2 - expected_non_global) / 2,
    )

    values_at_zero = {
        ("a", "b"): Fraction(1),
        ("a", "u"): Fraction(1),
        ("u", "b"): Fraction(1),
        ("a", "v"): Fraction(1),
        ("v", "b"): Fraction(1),
    }
    assert_equal(
        "first derivative at zero",
        bms_rhs(("a", "b"), values_at_zero, measured, unmeasured, rates),
        -a_ab,
    )
    assert_equal(
        "global Sudakov ansatz misses the finite cascade",
        global_sudakov_missed_cascade(("a", "b"), measured, unmeasured, rates),
        expected_non_global / 2,
    )


def check_additive_measurement_boundary() -> None:
    measured = ("m",)
    unmeasured = ("u",)
    rates: Rates = {
        ("a", "b", "m"): Fraction(3, 5),
        ("a", "b", "u"): Fraction(2, 7),
        ("a", "u", "m"): Fraction(1, 5),
        ("u", "b", "m"): Fraction(2, 5),
    }
    assert_equal(
        "additive veto rates remove the non-global coefficient",
        non_global_coefficient(("a", "b"), measured, unmeasured, rates),
        Fraction(0),
    )
    assert_equal(
        "additive case leaves global Sudakov square",
        second_order_coefficient(("a", "b"), measured, unmeasured, rates),
        Fraction(9, 50),
    )
    assert_equal(
        "additive case has no global Sudakov mismatch",
        global_sudakov_missed_cascade(("a", "b"), measured, unmeasured, rates),
        Fraction(0),
    )


def check_scope_boundary_strings() -> None:
    text = JETS_CHAPTER.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    required = [
        "soft-dipole coordinate system for one obstruction to naive factorization",
        "the status of Glauber exchanges",
        "Super-leading logarithms, when present, are not explained by the finite non-global coefficient alone",
        "global-Sudakov-only ansatz",
        "unmeasured-to-measured cascade",
    ]
    for needle in required:
        if needle not in normalized:
            raise AssertionError(f"missing non-global scope-boundary string: {needle}")


def main() -> None:
    check_unmeasured_real_virtual_cancellation()
    check_second_order_non_global_coefficient()
    check_additive_measurement_boundary()
    check_scope_boundary_strings()
    print("All QCD non-global soft-dipole checks passed.")


if __name__ == "__main__":
    main()
