#!/usr/bin/env python3
"""Finite toric-code checks for the gauge-phase chapter.

The script verifies only finite Pauli and chain-complex algebra used in the
monograph: stabilizer commutation, global stabilizer redundancies, the
four-dimensional ground space on a square torus, logical line anticommutation,
contractible stabilizer loops, and the constant local energy barrier of a
simple logical string.
"""

from __future__ import annotations

from dataclasses import dataclass


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class SquareTorus:
    size: int

    def __post_init__(self) -> None:
        if self.size < 3:
            raise ValueError("Use size >= 3 to avoid degenerate small-cell overlaps.")

    def edge_index(self, kind: str, x: int, y: int) -> int:
        x %= self.size
        y %= self.size
        offset = 0 if kind == "h" else self.size * self.size
        return offset + y * self.size + x

    def edge_mask(self, kind: str, x: int, y: int) -> int:
        return 1 << self.edge_index(kind, x, y)

    def star_x_mask(self, x: int, y: int) -> int:
        return (
            self.edge_mask("h", x, y)
            ^ self.edge_mask("h", x - 1, y)
            ^ self.edge_mask("v", x, y)
            ^ self.edge_mask("v", x, y - 1)
        )

    def plaquette_z_mask(self, x: int, y: int) -> int:
        return (
            self.edge_mask("h", x, y)
            ^ self.edge_mask("v", x + 1, y)
            ^ self.edge_mask("h", x, y + 1)
            ^ self.edge_mask("v", x, y)
        )

    def stars(self) -> list[int]:
        return [self.star_x_mask(x, y) for y in range(self.size) for x in range(self.size)]

    def plaquettes(self) -> list[int]:
        return [self.plaquette_z_mask(x, y) for y in range(self.size) for x in range(self.size)]

    def horizontal_z_loop(self, y: int) -> int:
        mask = 0
        for x in range(self.size):
            mask ^= self.edge_mask("h", x, y)
        return mask

    def vertical_z_loop(self, x: int) -> int:
        mask = 0
        for y in range(self.size):
            mask ^= self.edge_mask("v", x, y)
        return mask

    def horizontal_x_cocycle_column(self, x: int) -> int:
        """Dual vertical X loop, represented on horizontal primal edges."""

        mask = 0
        for y in range(self.size):
            mask ^= self.edge_mask("h", x, y)
        return mask

    def vertical_x_cocycle_row(self, y: int) -> int:
        """Dual horizontal X loop, represented on vertical primal edges."""

        mask = 0
        for x in range(self.size):
            mask ^= self.edge_mask("v", x, y)
        return mask

    def partial_horizontal_z_string(self, length: int, y: int) -> int:
        mask = 0
        for x in range(length):
            mask ^= self.edge_mask("h", x, y)
        return mask


def parity(mask: int) -> int:
    return mask.bit_count() & 1


def anticommutes(x_mask: int, z_mask: int) -> bool:
    return parity(x_mask & z_mask) == 1


def gf2_rank(rows: list[int]) -> int:
    basis: dict[int, int] = {}
    for row in rows:
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis)


def xor_all(rows: list[int]) -> int:
    total = 0
    for row in rows:
        total ^= row
    return total


def syndrome_count(stabilizer_masks: list[int], pauli_mask: int) -> int:
    return sum(1 for stabilizer in stabilizer_masks if anticommutes(stabilizer, pauli_mask))


def check_stabilizer_commutation(lattice: SquareTorus) -> None:
    for star in lattice.stars():
        for plaquette in lattice.plaquettes():
            assert_true(not anticommutes(star, plaquette), "every star commutes with every plaquette")


def check_global_redundancy_and_ground_dimension(lattice: SquareTorus) -> None:
    stars = lattice.stars()
    plaquettes = lattice.plaquettes()
    assert_equal(xor_all(stars), 0, "product of all star stabilizers is the identity")
    assert_equal(xor_all(plaquettes), 0, "product of all plaquette stabilizers is the identity")
    expected_single_species_rank = lattice.size * lattice.size - 1
    assert_equal(gf2_rank(stars), expected_single_species_rank, "independent star constraints")
    assert_equal(gf2_rank(plaquettes), expected_single_species_rank, "independent plaquette constraints")
    number_of_edges = 2 * lattice.size * lattice.size
    stabilizer_rank = gf2_rank(stars) + gf2_rank(plaquettes)
    encoded_qubits = number_of_edges - stabilizer_rank
    assert_equal(encoded_qubits, 2, "two encoded qubits on the torus")
    assert_equal(2**encoded_qubits, 4, "four-dimensional ground space on the torus")


def check_logical_line_pairing(lattice: SquareTorus) -> None:
    z_x = lattice.horizontal_z_loop(0)
    z_y = lattice.vertical_z_loop(0)
    x_dual_y = lattice.horizontal_x_cocycle_column(0)
    x_dual_x = lattice.vertical_x_cocycle_row(0)

    assert_equal(syndrome_count(lattice.stars(), z_x), 0, "closed Z_x loop has no star endpoints")
    assert_equal(syndrome_count(lattice.stars(), z_y), 0, "closed Z_y loop has no star endpoints")
    assert_equal(syndrome_count(lattice.plaquettes(), x_dual_y), 0, "dual X_y loop is a cocycle")
    assert_equal(syndrome_count(lattice.plaquettes(), x_dual_x), 0, "dual X_x loop is a cocycle")

    assert_true(anticommutes(x_dual_y, z_x), "dual X_y and primal Z_x have odd intersection")
    assert_true(anticommutes(x_dual_x, z_y), "dual X_x and primal Z_y have odd intersection")
    assert_true(not anticommutes(x_dual_y, z_y), "dual X_y and primal Z_y have zero intersection")
    assert_true(not anticommutes(x_dual_x, z_x), "dual X_x and primal Z_x have zero intersection")

    assert_equal(gf2_rank(lattice.stars() + [x_dual_y]), gf2_rank(lattice.stars()) + 1, "dual X_y is not a star product")
    assert_equal(gf2_rank(lattice.plaquettes() + [z_x]), gf2_rank(lattice.plaquettes()) + 1, "Z_x is not a plaquette product")


def check_contractible_local_indistinguishability_mechanism(lattice: SquareTorus) -> None:
    single_horizontal_edge = lattice.edge_mask("h", 0, 0)
    assert_equal(
        syndrome_count(lattice.stars(), single_horizontal_edge),
        2,
        "single-edge Z operator creates two star violations",
    )
    assert_equal(
        syndrome_count(lattice.plaquettes(), single_horizontal_edge),
        2,
        "single-edge X operator creates two plaquette violations",
    )
    assert_equal(
        syndrome_count(lattice.stars(), lattice.edge_mask("v", 0, 0)),
        2,
        "single vertical-edge Z operator creates two star violations",
    )
    assert_equal(
        syndrome_count(lattice.plaquettes(), lattice.edge_mask("v", 0, 0)),
        2,
        "single vertical-edge X operator creates two plaquette violations",
    )

    plaquette_boundary = lattice.plaquette_z_mask(0, 0)
    two_plaquette_boundary = lattice.plaquette_z_mask(0, 0) ^ lattice.plaquette_z_mask(1, 0)
    assert_equal(syndrome_count(lattice.stars(), plaquette_boundary), 0, "contractible plaquette Z loop has no endpoints")
    assert_equal(syndrome_count(lattice.stars(), two_plaquette_boundary), 0, "contractible rectangle Z loop has no endpoints")
    assert_equal(
        gf2_rank(lattice.plaquettes() + [plaquette_boundary]),
        gf2_rank(lattice.plaquettes()),
        "one plaquette boundary is a plaquette stabilizer",
    )
    assert_equal(
        gf2_rank(lattice.plaquettes() + [two_plaquette_boundary]),
        gf2_rank(lattice.plaquettes()),
        "contractible rectangle boundary is a product of plaquette stabilizers",
    )

    star_support = lattice.star_x_mask(0, 0)
    assert_equal(syndrome_count(lattice.plaquettes(), star_support), 0, "star X support has no plaquette syndrome")
    assert_equal(gf2_rank(lattice.stars() + [star_support]), gf2_rank(lattice.stars()), "star support is a star stabilizer")


def check_constant_string_barrier(lattice: SquareTorus) -> None:
    for length in range(1, lattice.size):
        partial = lattice.partial_horizontal_z_string(length, 0)
        assert_equal(syndrome_count(lattice.stars(), partial), 2, "open partial string has two endpoint star violations")
    closed = lattice.partial_horizontal_z_string(lattice.size, 0)
    assert_equal(syndrome_count(lattice.stars(), closed), 0, "closed noncontractible string has no endpoints")
    energy_costs_in_units_of_j = [
        2 * syndrome_count(lattice.stars(), lattice.partial_horizontal_z_string(length, 0))
        for length in range(1, lattice.size)
    ]
    assert_equal(max(energy_costs_in_units_of_j), 4, "simple local logical string has constant 4J barrier")


def main() -> None:
    lattice = SquareTorus(size=5)
    check_stabilizer_commutation(lattice)
    check_global_redundancy_and_ground_dimension(lattice)
    check_logical_line_pairing(lattice)
    check_contractible_local_indistinguishability_mechanism(lattice)
    check_constant_string_barrier(lattice)
    print("Toric-code finite one-form laboratory checks passed.")


if __name__ == "__main__":
    main()
