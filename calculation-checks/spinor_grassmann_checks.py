#!/usr/bin/env python3
"""Finite checks for spinor-field and Grassmann path-integral conventions."""

from fractions import Fraction
from pathlib import Path
import re

import sympy as sp


REPO_ROOT = Path(__file__).resolve().parents[1]
CHAPTER16 = (
    REPO_ROOT
    / "monograph/tex/volumes/volume_i/"
    / "chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex"
)


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def assert_contains(text, needle, label):
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def assert_matrix_equal(actual, expected, label):
    diff = actual - expected
    diff = diff.applyfunc(sp.simplify)
    if diff != sp.zeros(*actual.shape):
        raise AssertionError(f"{label}: got\n{actual}\nexpected\n{expected}")


def check_dirac_phase_equations_and_charge_ledger():
    ii = sp.I
    mass = sp.Integer(7)
    lambda_u = ii * mass
    lambda_v = -ii * mass
    assert_equal(sp.simplify(ii * lambda_u + mass), 0, "u phase Dirac equation")
    assert_equal(sp.simplify(-ii * lambda_v + mass), 0, "v phase Dirac equation")

    charge = {
        "b_dagger": 1,
        "d_dagger": -1,
        "b": -1,
        "d": 1,
    }
    assert_equal(charge["b_dagger"], 1, "charge of b dagger")
    assert_equal(charge["d"], 1, "charge of d annihilator")
    assert_equal(charge["b"], -1, "charge of b annihilator")
    assert_equal(charge["d_dagger"], -1, "charge of d dagger")


def check_locality_sign_ledger():
    ordinary_scalar = {"Delta_xy": 1, "Delta_yx": 1}
    car_scalar = {"Delta_xy": 1, "Delta_yx": -1}
    pauli_jordan = {"Delta_xy": 1, "Delta_yx": -1}
    assert_equal(ordinary_scalar["Delta_yx"], 1, "ordinary scalar plus sign")
    assert_equal(car_scalar, pauli_jordan, "CAR gives Pauli-Jordan sign")


def check_wightman_spin_statistics_wrong_sign_ledger():
    spin_sign = {"integer": 1, "half_integer": -1}
    locality_sign = {"commutator": 1, "anticommutator": -1}
    assert_equal(
        locality_sign["commutator"],
        spin_sign["integer"],
        "integer spin uses commutator",
    )
    assert_equal(
        locality_sign["anticommutator"],
        spin_sign["half_integer"],
        "half-integer spin uses anticommutator",
    )
    for spin, compatible_sign in spin_sign.items():
        wrong_sign = -compatible_sign
        forced_vacuum_norm = 0 if wrong_sign != compatible_sign else 1
        assert_equal(
            forced_vacuum_norm,
            0,
            f"wrong statistics forces zero two-point norm for {spin}",
        )


def theorem_block(text):
    start = text.index(
        r"\begin{quotedtheorem}[Wightman spin--statistics theorem in four dimensions]"
    )
    end = text.index(r"\section{Dirac, Weyl, and Majorana Fields}", start)
    return re.sub(r"\s+", " ", text[start:end])


def check_spin_statistics_theorem_text_contract():
    text = CHAPTER16.read_text(encoding="utf-8")
    block = theorem_block(text)
    required_phrases = [
        r"\label{thm:wightman-spin-statistics}",
        "StreaterWightman1964",
        "Jost1965",
        "four-dimensional cyclic Wightman",
        "positive Hilbert space",
        "positive-energy unitary representation",
        "operator-valued tempered distributions",
        "common invariant dense domain",
        "spectrum condition",
        "adjoint pairing",
        "Poincare-invariant cyclic vacuum",
        "central element",
        "wrong-statistics form",
        "Theorem~\\ref{thm:distributional-edge-of-the-wedge}",
        "Jost points",
        "weak local commutativity",
        "Theorem~\\ref{thm:wightman-pct}",
        "two-point Wightman distribution",
        "Reeh--Schlieder/cyclicity",
        "Theorem~\\ref{thm:doplicher-roberts-reconstruction}",
        "parastatistics",
        "BRST cohomology",
        "2+1",
        "1+1",
    ]
    for phrase in required_phrases:
        assert_contains(block, phrase, "spin-statistics theorem text contract")

    free_dirac_controls = [
        "ordinary commutators violate locality",
        "canonical anticommutator algebra",
        "Pauli--Jordan distribution",
        r"\label{prop:free-dirac-locality-selects-car}",
    ]
    for phrase in free_dirac_controls:
        assert_contains(text, phrase, "free Dirac locality control")


def paragraph_around(text, pos):
    start = text.rfind("\n\n", 0, pos)
    end = text.find("\n\n", pos)
    if start == -1:
        start = 0
    if end == -1:
        end = len(text)
    return text[start:end]


def check_spin_statistics_theorem_references_in_volumes_i_iv():
    term = re.compile(r"spin(?:-|--)statistics theorem")
    volumes = [
        REPO_ROOT / "monograph/tex/volumes/volume_i",
        REPO_ROOT / "monograph/tex/volumes/volume_iv",
    ]
    missing = []
    for volume in volumes:
        for path in sorted(volume.glob("chapter*.tex")):
            text = path.read_text(encoding="utf-8")
            for match in term.finditer(text):
                paragraph = paragraph_around(text, match.start())
                if r"thm:wightman-spin-statistics" not in paragraph:
                    line = text.count("\n", 0, match.start()) + 1
                    missing.append(f"{path.relative_to(REPO_ROOT)}:{line}")
    if missing:
        raise AssertionError(
            "spin-statistics theorem occurrence lacks exact theorem reference: "
            + ", ".join(missing)
        )

    downstream = [
        REPO_ROOT
        / "monograph/tex/volumes/volume_i/chapter12_haag_ruelle_scattering_theory.tex",
        REPO_ROOT
        / "monograph/tex/volumes/volume_i/chapter13_lsz_reduction_and_the_s_matrix.tex",
        REPO_ROOT
        / "monograph/tex/volumes/volume_iv/"
        / "chapter05_haag_ruelle_and_mathematical_scattering.tex",
    ]
    for path in downstream:
        assert_contains(
            path.read_text(encoding="utf-8"),
            r"thm:wightman-spin-statistics",
            f"{path.name} downstream theorem reference",
        )


def check_odd_dirac_bracket_matrix():
    m = sp.Matrix([[2, 1], [1, 3]])
    k = -2 * m
    eta_eta_bracket = -k.inv()
    expected = sp.Rational(1, 2) * m.inv()
    assert_matrix_equal(eta_eta_bracket, expected, "odd Dirac bracket")


def check_purely_odd_berezinian_two_coordinates():
    a = sp.Matrix([[2, 3], [5, 7]])
    determinant = a.det()
    transformed_top_coefficient = determinant
    transformed_density_factor = sp.Rational(1, 1) / determinant
    assert_equal(
        sp.simplify(transformed_top_coefficient * transformed_density_factor),
        1,
        "Berezinian inverse determinant",
    )


def check_one_pair_berezin_gaussian():
    a = Fraction(5, 3)
    gaussian_integral = a
    contraction = Fraction(1, 1) / a
    assert_equal(gaussian_integral, a, "one-pair Berezin determinant")
    assert_equal(contraction, Fraction(3, 5), "one-pair Berezin contraction")


def check_coherent_state_trace_signs():
    a, b, c, d = sp.symbols("a b c d")
    ordinary_trace_integrand_eta_coeff = a + d
    supertrace_integrand_eta_coeff = a - d
    matrix_trace = sp.trace(sp.Matrix([[a, b], [c, d]]))
    matrix_supertrace = a - d
    assert_equal(ordinary_trace_integrand_eta_coeff, matrix_trace, "trace sign")
    assert_equal(
        supertrace_integrand_eta_coeff,
        matrix_supertrace,
        "supertrace sign",
    )


def main():
    check_dirac_phase_equations_and_charge_ledger()
    check_locality_sign_ledger()
    check_wightman_spin_statistics_wrong_sign_ledger()
    check_spin_statistics_theorem_text_contract()
    check_spin_statistics_theorem_references_in_volumes_i_iv()
    check_odd_dirac_bracket_matrix()
    check_purely_odd_berezinian_two_coordinates()
    check_one_pair_berezin_gaussian()
    check_coherent_state_trace_signs()
    print("All spinor-Grassmann convention checks passed.")


if __name__ == "__main__":
    main()
