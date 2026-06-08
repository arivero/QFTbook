#!/usr/bin/env python3
"""Cross-chapter checks for curvature-squared Euler-tensor conventions.

Evidence contract.
Target claims: Volume XII Chapter 2 and Chapter 11 use one shared
inverse-metric-variation convention for the Ricci-squared Euler tensor:
Chapter 2's J_{mu nu} is Chapter 11's H^(2)_{mu nu}, with trace +2 Box R in
four dimensions.
Independent construction: exact rational trace algebra, Weyl-variation
coefficient bookkeeping, a linearized conformally flat polynomial fixture that
isolates the derivative signs away from the Einstein/constant-curvature
special case, and text-contract checks in both chapters.
Imported assumptions: standard Palatini variation identities and the
curvature convention already declared in the chapters.  The check verifies
the sign convention and cross-chapter wiring, not the analytic stress-tensor
renormalization theorem.
Negative controls: the old Chapter 2 derivative signs give trace -2 Box R,
the opposite Weyl coefficient, and the wrong non-Einstein conformally flat
linearized H^(2) tensor.
Scope boundary: this finite check does not prove the Hollands-Wald local
freedom theorem, the trace-anomaly heat-kernel expansion, or the
semiclassical existence problem.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
POINT_SPLITTING_CHAPTER = (
    REPO_ROOT
    / "monograph/tex/volumes/volume_xii/chapter02_point_splitting_stress_tensor.tex"
)
SEMICLASSICAL_CHAPTER = (
    REPO_ROOT
    / "monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex"
)
TRACE_ANOMALY_CHAPTER = (
    REPO_ROOT
    / "monograph/tex/volumes/volume_xii/chapter03_trace_anomalies.tex"
)

MultiIndex = tuple[int, ...]
Polynomial = dict[MultiIndex, Fraction]
Matrix = tuple[tuple[Fraction, ...], ...]

DIMENSION = 4
H2_DERIVATIVE_SIGNS = {
    "nabla_nabla_R": Fraction(-1),
    "box_ricci": Fraction(1),
    "metric_box_R": Fraction(1, 2),
}
OLD_CHAPTER2_SIGNS = {
    "nabla_nabla_R": Fraction(1),
    "box_ricci": Fraction(-1),
    "metric_box_R": Fraction(-1, 2),
}


def assert_equal(name: str, lhs, rhs) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: {lhs!r} != {rhs!r}")


def assert_contains(text: str, phrase: str, context: str) -> None:
    normalized_text = " ".join(text.split())
    normalized_phrase = " ".join(phrase.split())
    compact_text = "".join(text.split())
    compact_phrase = "".join(phrase.split())
    if (
        phrase not in text
        and normalized_phrase not in normalized_text
        and compact_phrase not in compact_text
    ):
        raise AssertionError(f"{context}: missing {phrase!r}")


def assert_not_contains(text: str, phrase: str, context: str) -> None:
    normalized_text = " ".join(text.split())
    normalized_phrase = " ".join(phrase.split())
    compact_text = "".join(text.split())
    compact_phrase = "".join(phrase.split())
    if phrase in text or normalized_phrase in normalized_text or compact_phrase in compact_text:
        raise AssertionError(f"{context}: stale forbidden phrase {phrase!r}")


def ricci_squared_trace_box_coefficient(
    signs: dict[str, Fraction] | None = None,
    dimension: int = DIMENSION,
) -> Fraction:
    if signs is None:
        signs = H2_DERIVATIVE_SIGNS
    return (
        signs["nabla_nabla_R"]
        + signs["box_ricci"]
        + dimension * signs["metric_box_R"]
    )


def r_squared_trace_box_coefficient(dimension: int = DIMENSION) -> Fraction:
    return Fraction(2 * dimension - 2)


def full_ricci_squared_weyl_coefficient(
    signs: dict[str, Fraction] | None = None,
    dimension: int = DIMENSION,
) -> Fraction:
    return -2 * ricci_squared_trace_box_coefficient(signs, dimension)


def r_squared_weyl_scheme_shift_coefficient(dimension: int = DIMENSION) -> Fraction:
    if dimension != 4:
        raise ValueError("this finite scheme-coordinate check is four-dimensional")
    return Fraction(-12)


def poly_derivative(poly: Polynomial, axis: int) -> Polynomial:
    result: Polynomial = {}
    for powers, coefficient in poly.items():
        power = powers[axis]
        if power == 0:
            continue
        new_powers = list(powers)
        new_powers[axis] -= 1
        key = tuple(new_powers)
        result[key] = result.get(key, Fraction(0)) + coefficient * power
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def poly_derivative_multi(poly: Polynomial, axes: tuple[int, ...]) -> Polynomial:
    result = poly
    for axis in axes:
        result = poly_derivative(result, axis)
    return result


def poly_add(*polys: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            result[powers] = result.get(powers, Fraction(0)) + coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def poly_scale(poly: Polynomial, scalar: Fraction) -> Polynomial:
    return {powers: scalar * coefficient for powers, coefficient in poly.items() if scalar * coefficient}


def poly_laplacian(poly: Polynomial, dimension: int = DIMENSION) -> Polynomial:
    return poly_add(
        *(
            poly_derivative_multi(poly, (axis, axis))
            for axis in range(dimension)
        )
    )


def poly_value(poly: Polynomial, point: tuple[Fraction, ...]) -> Fraction:
    total = Fraction(0)
    for powers, coefficient in poly.items():
        monomial = coefficient
        for value, power in zip(point, powers):
            monomial *= value ** power
        total += monomial
    return total


def linear_conformally_flat_h2_fixture(
    signs: dict[str, Fraction] | None = None,
) -> Matrix:
    if signs is None:
        signs = H2_DERIVATIVE_SIGNS
    sigma: Polynomial = {
        (4, 0, 0, 0): Fraction(2),
        (2, 2, 0, 0): Fraction(3),
        (0, 1, 3, 0): Fraction(5),
        (0, 0, 2, 2): Fraction(7),
        (0, 0, 0, 4): Fraction(11),
    }
    point = (Fraction(1), Fraction(2), Fraction(-1), Fraction(1))
    lap_sigma = poly_laplacian(sigma)
    scalar_curvature_linear = poly_scale(lap_sigma, Fraction(-6))
    ricci_linear: tuple[tuple[Polynomial, ...], ...] = tuple(
        tuple(
            poly_add(
                poly_scale(poly_derivative_multi(sigma, (row, col)), Fraction(-2)),
                poly_scale(lap_sigma, Fraction(-1) if row == col else Fraction(0)),
            )
            for col in range(DIMENSION)
        )
        for row in range(DIMENSION)
    )
    return tuple(
        tuple(
            poly_value(
                poly_add(
                    poly_scale(
                        poly_derivative_multi(scalar_curvature_linear, (row, col)),
                        signs["nabla_nabla_R"],
                    ),
                    poly_scale(
                        poly_laplacian(ricci_linear[row][col]),
                        signs["box_ricci"],
                    ),
                    poly_scale(
                        poly_laplacian(scalar_curvature_linear),
                        signs["metric_box_R"] if row == col else Fraction(0),
                    ),
                ),
                point,
            )
            for col in range(DIMENSION)
        )
        for row in range(DIMENSION)
    )


def expected_linear_conformally_flat_h2_fixture() -> Matrix:
    sigma: Polynomial = {
        (4, 0, 0, 0): Fraction(2),
        (2, 2, 0, 0): Fraction(3),
        (0, 1, 3, 0): Fraction(5),
        (0, 0, 2, 2): Fraction(7),
        (0, 0, 0, 4): Fraction(11),
    }
    point = (Fraction(1), Fraction(2), Fraction(-1), Fraction(1))
    lap_sigma = poly_laplacian(sigma)
    lap2_sigma = poly_laplacian(lap_sigma)
    return tuple(
        tuple(
            poly_value(
                poly_add(
                    poly_scale(
                        poly_derivative_multi(lap_sigma, (row, col)),
                        Fraction(4),
                    ),
                    poly_scale(
                        lap2_sigma,
                        Fraction(-4) if row == col else Fraction(0),
                    ),
                ),
                point,
            )
            for col in range(DIMENSION)
        )
        for row in range(DIMENSION)
    )


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum(matrix[index][index] for index in range(len(matrix)))


def check_ricci_squared_trace_and_weyl_variation() -> None:
    assert_equal("R^2 Euler trace Box R coefficient", r_squared_trace_box_coefficient(), Fraction(6))
    assert_equal(
        "Ricci-squared Euler trace Box R coefficient",
        ricci_squared_trace_box_coefficient(),
        Fraction(2),
    )
    assert_equal(
        "old Ricci-squared trace sign",
        ricci_squared_trace_box_coefficient(OLD_CHAPTER2_SIGNS),
        Fraction(-2),
    )
    assert_equal(
        "full Ricci-squared Weyl coefficient",
        full_ricci_squared_weyl_coefficient(),
        Fraction(-4),
    )
    if full_ricci_squared_weyl_coefficient(OLD_CHAPTER2_SIGNS) == Fraction(-4):
        raise AssertionError("old Ricci-squared signs passed the Weyl variation")
    assert_equal(
        "R^2 trace-anomaly scheme-coordinate Weyl coefficient",
        r_squared_weyl_scheme_shift_coefficient(),
        Fraction(-12),
    )


def check_non_einstein_conformally_flat_h2_fixture() -> None:
    corrected = linear_conformally_flat_h2_fixture(H2_DERIVATIVE_SIGNS)
    expected = expected_linear_conformally_flat_h2_fixture()
    assert_equal("linear non-Einstein conformally flat H2 fixture", corrected, expected)
    stale = linear_conformally_flat_h2_fixture(OLD_CHAPTER2_SIGNS)
    if stale == expected:
        raise AssertionError("old Ricci-squared signs passed the conformally flat fixture")
    off_diagonal = [
        corrected[row][col]
        for row in range(DIMENSION)
        for col in range(DIMENSION)
        if row != col
    ]
    if all(entry == 0 for entry in off_diagonal):
        raise AssertionError("fixture accidentally collapsed to an Einstein/constant-curvature test")
    sigma: Polynomial = {
        (4, 0, 0, 0): Fraction(2),
        (2, 2, 0, 0): Fraction(3),
        (0, 1, 3, 0): Fraction(5),
        (0, 0, 2, 2): Fraction(7),
        (0, 0, 0, 4): Fraction(11),
    }
    point = (Fraction(1), Fraction(2), Fraction(-1), Fraction(1))
    scalar_curvature_linear = poly_scale(poly_laplacian(sigma), Fraction(-6))
    assert_equal(
        "linear H2 trace fixture",
        matrix_trace(corrected),
        2 * poly_value(poly_laplacian(scalar_curvature_linear), point),
    )


def check_cross_chapter_text_contract() -> None:
    ch2 = POINT_SPLITTING_CHAPTER.read_text(encoding="utf-8")
    ch11 = SEMICLASSICAL_CHAPTER.read_text(encoding="utf-8")
    ch3 = TRACE_ANOMALY_CHAPTER.read_text(encoding="utf-8")

    for phrase in [
        r"\(J_{\mu\nu}=H^{(2)}_{\mu\nu}\)",
        r"-\nabla_\mu\nabla_\nu R",
        r"+\Box_gR_{\mu\nu}",
        r"+\frac12g_{\mu\nu}\Box_gR",
        r"g^{\mu\nu}J_{\mu\nu}=2\Box_gR",
        "same inverse-metric variation convention",
    ]:
        assert_contains(ch2, phrase, "Chapter 2 Ricci-squared convention")
    assert_not_contains(
        ch2,
        r"+\nabla_\mu\nabla_\nu R -\Box_gR_{\mu\nu} -\frac12g_{\mu\nu}\Box_gR",
        "Chapter 2 Ricci-squared convention",
    )

    for phrase in [
        r"\(H^{(1)}_{\mu\nu}=I_{\mu\nu}\)",
        r"\(H^{(2)}_{\mu\nu}=J_{\mu\nu}\)",
        r"-\nabla_\mu\nabla_\nu R",
        r"+\Box R_{\mu\nu}",
        r"+\frac12g_{\mu\nu}\Box R",
        r"g^{\mu\nu}H^{(2)}_{\mu\nu}=2\Box R",
    ]:
        assert_contains(ch11, phrase, "Chapter 11 Ricci-squared convention")

    for phrase in [
        r"\delta_\sigma\int_M d^4x\,\sqrt g\,R^2",
        r"-12\int_M d^4x\,\sqrt g\,\sigma\,\nabla^2R",
        r"coefficient of \(\nabla^2R\) in four dimensions is a scheme coordinate",
        r"shifts the coefficient \(b\)",
    ]:
        assert_contains(ch3, phrase, "Chapter 3 trace-anomaly scheme coordinate")


def main() -> None:
    check_ricci_squared_trace_and_weyl_variation()
    check_non_einstein_conformally_flat_h2_fixture()
    check_cross_chapter_text_contract()
    print("Curvature-squared Euler convention cross-chapter checks passed.")


if __name__ == "__main__":
    main()
