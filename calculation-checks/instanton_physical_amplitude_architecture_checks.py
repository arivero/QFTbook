"""Finite checks for the instanton physical-amplitude architecture chapter.

Evidence contract.

Target claims:
- `def:instanton-physical-amplitude-channel` and
  `eq:instanton-physical-channel-functional`: the physical channel depends on
  the collective density, nonzero-mode determinant, zero-mode source
  determinant, endpoint/projection weights, and residuals, not on the moduli
  measure alone.
- `prop:instanton-moduli-equivalent-channel-separation`: two channels with the
  same collective-coordinate and determinant weights can have different, or
  zero, two-flavor source amplitudes.
- `prop:two-flavor-source-mass-determinant-coordinate`: the mass-saturated
  activity, mass-assisted source terms, and four-source coefficient are
  distinct coordinates of det(M+B).
- `ca:finite-cell-instanton-channel-control`: finite retained-cell residuals
  and source-determinant perturbations obey the displayed absolute bounds.

Independent construction:
- The checks build small exact rational cell models from scratch.  They compute
  two-by-two determinants, mass/source polynomials, physical projection bins,
  and residual sums directly, rather than importing BPST radial integrals or
  copying a monograph coefficient.

Imported assumptions:
- The finite model assumes that the continuum instanton window has already been
  reduced to finitely many regulator cells and that two light flavors give a
  two-by-two zero-mode source determinant.  It does not assume any continuum
  determinant constant, ADHM volume, or spectral-continuation theorem.

Negative controls:
- The script rejects a plus sign in the off-diagonal determinant term, a
  moduli-only prediction that ignores zero-mode rank, a rank-one source matrix
  treated as a nonzero four-source channel, a single Euclidean cell sum used as
  a spectral-bin observable, and a residual bound that omits the external
  projection/sector remainder.

Scope boundary:
- Passing these checks proves only finite algebra and channel bookkeeping.  It
  does not prove continuum convergence of the instanton integral, compute the
  Pauli--Villars determinant constant, establish a Lorentzian scattering
  theorem, or justify any specific dilute-gas regime.
"""

from __future__ import annotations

from fractions import Fraction

from check_utils import assert_close, assert_geq, assert_gt, assert_leq


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def det2(matrix: Matrix2) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def trace2(matrix: Matrix2) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def add2(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def matmul2(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def inv2(matrix: Matrix2) -> Matrix2:
    determinant = det2(matrix)
    if determinant == 0:
        raise AssertionError("singular matrix")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def max_abs_entry(matrix: Matrix2) -> Fraction:
    return max(abs(entry) for row in matrix for entry in row)


def assert_not_equal(name: str, actual: Fraction, bad: Fraction) -> None:
    if actual == bad:
        raise AssertionError(f"{name}: wrong shortcut unexpectedly matched {actual!r}")


def check_two_flavor_mass_source_determinant_coordinate() -> None:
    m_u = Fraction(2, 5)
    m_d = Fraction(3, 7)
    mass: Matrix2 = ((m_u, Fraction(0)), (Fraction(0), m_d))
    source: Matrix2 = (
        (Fraction(11, 13), Fraction(5, 17)),
        (Fraction(7, 19), Fraction(13, 23)),
    )
    full = det2(add2(mass, source))
    polynomial = (
        m_u * m_d
        + m_u * source[1][1]
        + m_d * source[0][0]
        + source[0][0] * source[1][1]
        - source[0][1] * source[1][0]
    )
    assert_close("mass/source determinant polynomial", float(full), float(polynomial))

    wrong_plus = (
        m_u * m_d
        + m_u * source[1][1]
        + m_d * source[0][0]
        + source[0][0] * source[1][1]
        + source[0][1] * source[1][0]
    )
    assert_not_equal("off-diagonal determinant sign", full, wrong_plus)

    vacuum_coordinate = m_u * m_d
    four_source_coordinate = det2(source)
    assert_not_equal("vacuum coordinate is not four-source coefficient", vacuum_coordinate, four_source_coordinate)
    assert_gt("four-source coefficient nonzero", abs(float(four_source_coordinate)), 0.0)


def check_moduli_equivalent_channel_separation() -> None:
    weights = [Fraction(1, 3), Fraction(2, 5), Fraction(7, 11)]
    determinants = [Fraction(13, 17), Fraction(19, 23), Fraction(29, 31)]
    base_cells = [w * d for w, d in zip(weights, determinants)]
    moduli_only = sum(base_cells, Fraction(0))

    full_rank_sources: list[Matrix2] = [
        ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(3))),
        ((Fraction(3), Fraction(1, 2)), (Fraction(1, 5), Fraction(5))),
        ((Fraction(5, 2), Fraction(2, 3)), (Fraction(1, 7), Fraction(7, 3))),
    ]
    rank_one_sources: list[Matrix2] = [
        ((Fraction(2), Fraction(4)), (Fraction(3), Fraction(6))),
        ((Fraction(5), Fraction(10)), (Fraction(1), Fraction(2))),
        ((Fraction(7), Fraction(14)), (Fraction(3), Fraction(6))),
    ]

    full_rank_channel = sum(
        base * det2(source)
        for base, source in zip(base_cells, full_rank_sources)
    )
    rank_one_channel = sum(
        base * det2(source)
        for base, source in zip(base_cells, rank_one_sources)
    )

    assert_gt("moduli-only retained density nonzero", float(moduli_only), 0.0)
    assert_close("rank-one source channel vanishes", float(rank_one_channel), 0.0)
    assert_gt("full-rank source channel nonzero", abs(float(full_rank_channel)), 0.0)
    assert_not_equal("moduli-only shortcut cannot predict full-rank channel", moduli_only, full_rank_channel)


def check_projection_not_recoverable_from_one_euclidean_sum() -> None:
    cell_coefficients = [Fraction(1), Fraction(2), Fraction(3)]
    alternate_coefficients = [Fraction(3), Fraction(2), Fraction(1)]
    euclidean_sum = sum(cell_coefficients, Fraction(0))
    alternate_sum = sum(alternate_coefficients, Fraction(0))
    first_bin = [Fraction(1), Fraction(0), Fraction(0)]

    projected = sum(p * c for p, c in zip(first_bin, cell_coefficients))
    alternate_projected = sum(p * c for p, c in zip(first_bin, alternate_coefficients))

    assert_close("same Euclidean source sum", float(euclidean_sum), float(alternate_sum))
    assert_not_equal("one Euclidean sum does not determine spectral bin", projected, alternate_projected)
    assert_gt("projected ambiguity visible", abs(float(projected - alternate_projected)), 0.0)


def check_finite_cell_residual_bound() -> None:
    cells = [Fraction(5, 7), Fraction(-2, 9), Fraction(4, 11)]
    epsilons = [Fraction(1, 20), Fraction(1, 15), Fraction(1, 25)]
    deltas = [Fraction(1, 30), Fraction(-1, 20), Fraction(1, 40)]
    external_residual = Fraction(1, 5)
    external_actual = Fraction(1, 8)

    leading = sum(cells, Fraction(0))
    exact = sum(c * (1 + delta) for c, delta in zip(cells, deltas)) + external_actual
    error = abs(exact - leading)
    bound = sum(abs(c) * eps for c, eps in zip(cells, epsilons)) + external_residual
    underbudget = sum(abs(c) * eps for c, eps in zip(cells, epsilons))

    assert_leq("finite-cell residual bound", float(error), float(bound))
    assert_gt("omitting external residual underbudgets", float(error), float(underbudget))


def check_source_determinant_stability_bound() -> None:
    base: Matrix2 = ((Fraction(3), Fraction(1)), (Fraction(1), Fraction(2)))
    perturbation: Matrix2 = ((Fraction(1, 20), Fraction(-1, 50)), (Fraction(1, 60), Fraction(1, 40)))

    relative_matrix = matmul2(inv2(base), perturbation)
    eta = max_abs_entry(relative_matrix)
    relative_error = abs(det2(add2(base, perturbation)) - det2(base)) / abs(det2(base))
    bound = 2 * eta + eta * eta

    assert_leq("source determinant stability", float(relative_error), float(bound))
    assert_geq("positive determinant margin", float(abs(det2(base))), 1.0)


def main() -> None:
    check_two_flavor_mass_source_determinant_coordinate()
    check_moduli_equivalent_channel_separation()
    check_projection_not_recoverable_from_one_euclidean_sum()
    check_finite_cell_residual_bound()
    check_source_determinant_stability_bound()
    print("instanton physical amplitude architecture checks passed")


if __name__ == "__main__":
    main()
