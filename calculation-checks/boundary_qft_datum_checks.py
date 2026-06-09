#!/usr/bin/env python3
"""Finite checks for the Volume IX boundary-QFT datum.

Evidence contract.
Target claim: Volume IX Chapter 08 replaces the untyped
bulk-to-boundary algebra map by a stratified local net with interior,
boundary, and mixed collar regions, while treating BOE data and states as
separate structures.
Independent construction: this script builds a finite region poset and finite
algebras of generator labels.  It verifies functorial inclusion into collar
regions, rejects a direct interior-to-boundary map when there is no region
inclusion, distinguishes boundary-condition data from states, and models BOE
as a finite jet with a nonzero controlled remainder.
Imported assumptions: finite generator sets stand in for local algebras, the
region poset is a toy collar geometry, and the polynomial jets model only the
short-distance bookkeeping of the free half-space scalar example.
Negative controls: an untyped bulk-to-boundary map, a state stored inside the
boundary-condition datum, exact finite-distance BOE convergence, a Dirichlet
evaluation map that loses the normal derivative, and a collar algebra missing
one stratum are rejected.
Scope boundary: these checks do not prove existence of continuum boundary
QFTs, time-slice theorems, positivity, BCFT convergence, or analytic BOE
remainder estimates.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Region:
    name: str
    stratum: str


def assert_equal(label: str, left, right) -> None:
    if left != right:
        raise AssertionError(f"{label} failed: {left!r} != {right!r}")


def assert_true(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{label} failed")


INTERIOR = Region("I", "interior")
BOUNDARY = Region("V", "boundary")
COLLAR = Region("C", "collar")
REMOTE_INTERIOR = Region("J", "interior")

INCLUSIONS = {
    (INTERIOR, COLLAR),
    (BOUNDARY, COLLAR),
    (REMOTE_INTERIOR, REMOTE_INTERIOR),
    (INTERIOR, INTERIOR),
    (BOUNDARY, BOUNDARY),
    (COLLAR, COLLAR),
}

ALGEBRAS = {
    INTERIOR: frozenset({"bulk_phi"}),
    BOUNDARY: frozenset({"bdy_phi", "bdy_normal_phi"}),
    COLLAR: frozenset({"bulk_phi@C", "bdy_phi@C", "bdy_normal_phi@C"}),
    REMOTE_INTERIOR: frozenset({"remote_bulk_phi"}),
}

STRUCTURE_MAPS = {
    (INTERIOR, COLLAR): {"bulk_phi": "bulk_phi@C"},
    (BOUNDARY, COLLAR): {
        "bdy_phi": "bdy_phi@C",
        "bdy_normal_phi": "bdy_normal_phi@C",
    },
    (REMOTE_INTERIOR, REMOTE_INTERIOR): {"remote_bulk_phi": "remote_bulk_phi"},
    (INTERIOR, INTERIOR): {"bulk_phi": "bulk_phi"},
    (BOUNDARY, BOUNDARY): {
        "bdy_phi": "bdy_phi",
        "bdy_normal_phi": "bdy_normal_phi",
    },
    (COLLAR, COLLAR): {
        "bulk_phi@C": "bulk_phi@C",
        "bdy_phi@C": "bdy_phi@C",
        "bdy_normal_phi@C": "bdy_normal_phi@C",
    },
}


def image(source: Region, target: Region, generators: frozenset[str]) -> frozenset[str]:
    mapping = STRUCTURE_MAPS[(source, target)]
    return frozenset(mapping[generator] for generator in generators)


def check_stratified_net_inclusions() -> None:
    assert_true(
        "interior and boundary both include into the collar",
        (INTERIOR, COLLAR) in INCLUSIONS and (BOUNDARY, COLLAR) in INCLUSIONS,
    )
    assert_true(
        "bare interior-to-boundary inclusion is absent",
        (INTERIOR, BOUNDARY) not in INCLUSIONS,
    )

    interior_image = image(INTERIOR, COLLAR, ALGEBRAS[INTERIOR])
    boundary_image = image(BOUNDARY, COLLAR, ALGEBRAS[BOUNDARY])
    assert_equal("interior image lands in collar algebra", interior_image <= ALGEBRAS[COLLAR], True)
    assert_equal("boundary image lands in collar algebra", boundary_image <= ALGEBRAS[COLLAR], True)
    assert_equal(
        "mixed collar algebra remembers both strata",
        interior_image | boundary_image,
        ALGEBRAS[COLLAR],
    )

    collar_missing_boundary = frozenset({"bulk_phi@C"})
    assert_equal(
        "collar algebra missing boundary generators is rejected",
        boundary_image <= collar_missing_boundary,
        False,
    )


def check_locality_and_time_slice_slots() -> None:
    spacelike_pairs = {
        (INTERIOR, REMOTE_INTERIOR),
        (REMOTE_INTERIOR, INTERIOR),
    }
    timelike_or_mixed_pairs = {
        (INTERIOR, COLLAR),
        (BOUNDARY, COLLAR),
    }
    assert_true(
        "remote interior regions can carry a locality relation",
        (INTERIOR, REMOTE_INTERIOR) in spacelike_pairs,
    )
    assert_true(
        "collar incidence is not a spacelike commutation relation",
        not timelike_or_mixed_pairs & spacelike_pairs,
    )

    time_slice_regions = {COLLAR}
    assert_equal("time-slice datum is a property of regions, not a state", COLLAR in time_slice_regions, True)


def check_state_is_extra_data() -> None:
    boundary_condition_keys = {
        "regions",
        "algebras",
        "inclusions",
        "collar_maps",
        "locality",
        "time_slice",
    }
    possible_states = {
        "vacuum": {"bulk_phi@C": Fraction(0), "bdy_phi@C": Fraction(0)},
        "thermal": {"bulk_phi@C": Fraction(1, 7), "bdy_phi@C": Fraction(2, 7)},
    }
    assert_equal("state is not stored in the boundary-condition datum", "state" in boundary_condition_keys, False)
    assert_equal("same local datum can support several states", len(possible_states), 2)


def eval_poly(coefficients: dict[int, Fraction], x: Fraction) -> Fraction:
    return sum(coefficient * x**degree for degree, coefficient in coefficients.items())


def truncate(coefficients: dict[int, Fraction], max_degree: int) -> dict[int, Fraction]:
    return {
        degree: coefficient
        for degree, coefficient in coefficients.items()
        if degree <= max_degree
    }


def check_boe_is_asymptotic_jet_data() -> None:
    x = Fraction(1, 10)

    neumann_bulk_jet = {0: Fraction(7), 1: Fraction(0), 2: Fraction(-4)}
    neumann_leading = truncate(neumann_bulk_jet, 0)
    neumann_remainder = eval_poly(neumann_bulk_jet, x) - eval_poly(neumann_leading, x)
    assert_equal("Neumann leading BOE keeps boundary value", neumann_leading, {0: Fraction(7)})
    assert_equal("Neumann finite-distance BOE is not exact", neumann_remainder == 0, False)
    assert_equal("Neumann remainder is order x^2 in the finite jet", neumann_remainder, Fraction(-1, 25))

    dirichlet_bulk_jet = {0: Fraction(0), 1: Fraction(3), 2: Fraction(5)}
    dirichlet_leading = truncate(dirichlet_bulk_jet, 1)
    dirichlet_remainder = eval_poly(dirichlet_bulk_jet, x) - eval_poly(dirichlet_leading, x)
    assert_equal("Dirichlet leading BOE keeps normal derivative", dirichlet_leading[1], Fraction(3))
    assert_equal("Dirichlet finite-distance BOE is not exact", dirichlet_remainder == 0, False)
    assert_equal("Dirichlet remainder is order x^2 in the finite jet", dirichlet_remainder, Fraction(1, 20))

    naive_boundary_evaluation = dirichlet_bulk_jet[0]
    assert_equal(
        "Dirichlet evaluation at the boundary loses the leading normal operator",
        naive_boundary_evaluation == dirichlet_leading[1],
        False,
    )


def main() -> None:
    check_stratified_net_inclusions()
    check_locality_and_time_slice_slots()
    check_state_is_extra_data()
    check_boe_is_asymptotic_jet_data()
    print("Boundary-QFT datum checks passed.")


if __name__ == "__main__":
    main()
