#!/usr/bin/env python3
"""Exact finite checks for the Z2 strong-coupling surface expansion.

The checks enumerate the plaquette chain complex of small cubical boxes over
F_2.  They verify the one-cube Wilson-loop polynomial displayed in
Volume XI, Chapter 5 and the first rectangular surface counts used in the
finite strong-coupling area estimate.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class CubicalPlaquetteComplex:
    edge_index: dict[tuple[str, int, int, int], int]
    plaquette_boundaries: tuple[int, ...]

    @staticmethod
    def build(nx: int, ny: int, nz: int) -> "CubicalPlaquetteComplex":
        edges: list[tuple[str, int, int, int]] = []
        for x in range(nx):
            for y in range(ny + 1):
                for z in range(nz + 1):
                    edges.append(("x", x, y, z))
        for x in range(nx + 1):
            for y in range(ny):
                for z in range(nz + 1):
                    edges.append(("y", x, y, z))
        for x in range(nx + 1):
            for y in range(ny + 1):
                for z in range(nz):
                    edges.append(("z", x, y, z))

        edge_index = {edge: i for i, edge in enumerate(edges)}

        def edge_mask(boundary_edges: list[tuple[str, int, int, int]]) -> int:
            mask = 0
            for edge in boundary_edges:
                mask ^= 1 << edge_index[edge]
            return mask

        plaquette_boundaries: list[int] = []
        for x in range(nx):
            for y in range(ny):
                for z in range(nz + 1):
                    plaquette_boundaries.append(
                        edge_mask(
                            [
                                ("x", x, y, z),
                                ("y", x + 1, y, z),
                                ("x", x, y + 1, z),
                                ("y", x, y, z),
                            ]
                        )
                    )
        for x in range(nx):
            for y in range(ny + 1):
                for z in range(nz):
                    plaquette_boundaries.append(
                        edge_mask(
                            [
                                ("x", x, y, z),
                                ("z", x + 1, y, z),
                                ("x", x, y, z + 1),
                                ("z", x, y, z),
                            ]
                        )
                    )
        for x in range(nx + 1):
            for y in range(ny):
                for z in range(nz):
                    plaquette_boundaries.append(
                        edge_mask(
                            [
                                ("y", x, y, z),
                                ("z", x, y + 1, z),
                                ("y", x, y, z + 1),
                                ("z", x, y, z),
                            ]
                        )
                    )

        return CubicalPlaquetteComplex(edge_index, tuple(plaquette_boundaries))

    def rectangle_loop_xy(
        self, width: int, height: int, *, x0: int = 0, y0: int = 0, z: int = 0
    ) -> int:
        """Return the mod-2 boundary mask of an xy-plane rectangle."""

        mask = 0
        for x in range(x0, x0 + width):
            mask ^= 1 << self.edge_index[("x", x, y0, z)]
            mask ^= 1 << self.edge_index[("x", x, y0 + height, z)]
        for y in range(y0, y0 + height):
            mask ^= 1 << self.edge_index[("y", x0, y, z)]
            mask ^= 1 << self.edge_index[("y", x0 + width, y, z)]
        return mask

    def surface_counts(self, target_boundary: int) -> tuple[Counter[int], Counter[int]]:
        """Count surfaces by area with a given boundary and with zero boundary."""

        target_counts: Counter[int] = Counter()
        closed_counts: Counter[int] = Counter()
        number_of_plaquettes = len(self.plaquette_boundaries)
        for subset in range(1 << number_of_plaquettes):
            boundary = 0
            area = 0
            for i, plaquette_boundary in enumerate(self.plaquette_boundaries):
                if (subset >> i) & 1:
                    boundary ^= plaquette_boundary
                    area += 1
            if boundary == target_boundary:
                target_counts[area] += 1
            if boundary == 0:
                closed_counts[area] += 1
        return target_counts, closed_counts


def assert_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_one_cube_polynomial() -> None:
    complex_ = CubicalPlaquetteComplex.build(1, 1, 1)
    loop = complex_.rectangle_loop_xy(1, 1)
    target_counts, closed_counts = complex_.surface_counts(loop)

    assert_equal(dict(target_counts), {1: 1, 5: 1}, "one-cube numerator")
    assert_equal(dict(closed_counts), {0: 1, 6: 1}, "one-cube denominator")

    # These dictionaries are precisely the polynomial
    #     <W(C)> = (t + t^5)/(1 + t^6).
    numerator_exponents = sorted(target_counts.elements())
    denominator_exponents = sorted(closed_counts.elements())
    assert_equal(numerator_exponents, [1, 5], "one-cube numerator exponents")
    assert_equal(denominator_exponents, [0, 6], "one-cube denominator exponents")


def check_two_by_one_rectangle_counts() -> None:
    complex_ = CubicalPlaquetteComplex.build(2, 1, 1)
    loop = complex_.rectangle_loop_xy(2, 1)
    target_counts, closed_counts = complex_.surface_counts(loop)

    assert_equal(dict(target_counts), {2: 1, 6: 2, 8: 1}, "2x1 numerator")
    assert_equal(dict(closed_counts), {0: 1, 6: 2, 10: 1}, "2x1 denominator")
    assert_equal(min(target_counts), 2, "2x1 minimal area")
    assert_equal(target_counts[min(target_counts)], 1, "2x1 flat minimal surface")


def check_entropy_bound_arithmetic() -> None:
    complex_ = CubicalPlaquetteComplex.build(2, 1, 1)
    loop = complex_.rectangle_loop_xy(2, 1)
    target_counts, _ = complex_.surface_counts(loop)

    minimal_area = min(target_counts)
    excess_counts = {
        area - minimal_area: multiplicity for area, multiplicity in target_counts.items()
    }

    rho = 2
    k = 1
    for excess, multiplicity in excess_counts.items():
        if multiplicity > k * rho**excess:
            raise AssertionError("finite entropy bound failed")

    t = Fraction(1, 5)
    lhs = sum(multiplicity * t**excess for excess, multiplicity in excess_counts.items())
    rhs = Fraction(k, 1 - rho * t)
    if lhs > rhs:
        raise AssertionError("geometric entropy estimate failed at t=1/5")


def main() -> None:
    check_one_cube_polynomial()
    check_two_by_one_rectangle_counts()
    check_entropy_bound_arithmetic()
    print("Z2 strong-coupling surface-count checks passed.")


if __name__ == "__main__":
    main()
