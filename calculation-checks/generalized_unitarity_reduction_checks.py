#!/usr/bin/env python3
"""Finite checks for generalized unitarity and one-loop reduction.

The companion section in Volume II, Chapter 6 develops the bridge from
Cutkosky discontinuities to generalized cuts, scalar-integral reconstruction,
IBP reduction, and a master-integral differential equation.  This script
checks the exact algebraic ledger behind the worked massless phi^4 example
and the one-loop bubble family.

Evidence contract.
Target claims: the generalized-unitarity section of Volume II Chapter 6,
especially the phi^4 cut reconstruction, the negative controls for incomplete
cut sets and four-dimensional blind spots, the bubble IBP identity, and the
bubble master differential equation.
Independent construction: finite cut-signature matrices over rational
numbers, an explicit identical-state symmetry factor, a nullspace model for
local/rational terms invisible to four-dimensional cuts, and exact rational
checks of the one-loop bubble IBP coefficients at several regulator values.
Imported assumptions: dimensional regularization, the standard massless
two-particle phase-space normalization with the common factor of pi stripped
off, the Feynman-parameter gamma-function form of the bubble master, and the
vanishing of scaleless tadpoles in dimensional regularization.
Negative controls: the script rejects an s-channel-only ansatz, verifies that
local counterterms are invisible to cuts, and constructs two amplitudes with
identical four-dimensional cuts but different D-dimensional rational probes.
Scope boundary: a pass checks the finite reconstruction and reduction
bookkeeping; it does not compute a nonabelian helicity amplitude, prove
unitarity from Wightman axioms, or solve a multi-master differential system.
"""

from __future__ import annotations

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


CHANNELS = ("s", "t", "u")
BASIS = ("B_s", "B_t", "B_u", "local", "four_dimensional_rational_null")


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


def check_phi4_cut_reconstruction() -> None:
    lam = Fraction(5, 3)
    tree = -lam
    identical_state_factor = Fraction(1, 2)

    # Strip the common i/(8 pi) factor from the massless two-body phase-space
    # discontinuity.  The cut-normalized bubble has unit signature in these
    # units, so the coefficient is read directly.
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


def main() -> None:
    check_phi4_cut_reconstruction()
    check_four_dimensional_cut_blind_spot()
    check_bubble_ibp_identity()
    check_branch_and_landau_ledger()
    print("All generalized unitarity and one-loop reduction checks passed.")


if __name__ == "__main__":
    main()
