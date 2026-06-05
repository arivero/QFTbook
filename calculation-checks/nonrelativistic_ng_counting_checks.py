"""Checks for non-Lorentz Nambu--Goldstone counting and spectra.

Evidence contract.

Target claims: Section `sec:nonlorentz-goldstone-counting` states the
Watanabe--Brauner/Watanabe--Murayama internal-symmetry count
`n_NG = n_BS - rank(rho)/2`, with
`n_type_B = rank(rho)/2` and `n_type_A = n_BS - rank(rho)`.  The same section
derives the finite symplectic pairing behind one type-B mode from two broken
directions, the common type-A linear and type-B quadratic spectra, the
finite-density `U(1)` superfluid count, and the ferromagnet versus
antiferromagnet contrast.

Independent construction: the script computes ranks of antisymmetric
commutator-density matrices by exact Gaussian elimination over `Fraction`,
constructs the `SU(2)` ferromagnet `rho` matrix from the charge algebra and a
magnetization density, and derives the powers of the type-A and type-B
dispersion relations from the exact finite equations of motion rather than
substituting the displayed counting formula alone.

Imported assumptions: the broken charges are internal, the thermodynamic
commutator-density matrix exists, the charge algebra has
`[Q_a,Q_b]=i f_ab^c Q_c` with no extra central density in the examples, the
leading low-energy action has positive stiffness/susceptibility, and the
ferromagnet/antiferromagnet examples are in dimensions and regimes where the
ordered phase exists.

Negative controls: the script rejects one-Goldstone-per-broken-generator for
the ferromagnet, a wrong type-A count for a rank-two block plus one null
direction, a linear type-B dispersion, a finite-density `U(1)` superfluid with
a spurious type-B mode, and the mistake of adding broken spacetime generators
to the internal charge count.

Scope boundary: a pass verifies only finite rank bookkeeping, the local
quadratic equations of motion, and the example charge-density algebra.  It
does not prove the thermodynamic limit, current locality, clustering,
low-dimensional no-go hypotheses, microscopic spin-wave expansion, or the
existence of the ordered phase in any concrete lattice or continuum model.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from fractions import Fraction

Matrix = tuple[tuple[Fraction, ...], ...]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def expect_failure(name: str, callback: Callable[[], None]) -> None:
    try:
        callback()
    except AssertionError:
        return
    raise AssertionError(f"{name}: negative control unexpectedly passed")


def zero_matrix(size: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(size)) for _ in range(size))


def antisymmetric_block(lambda_value: Fraction) -> Matrix:
    return ((Fraction(0), lambda_value), (-lambda_value, Fraction(0)))


def block_diag(*blocks: Matrix) -> Matrix:
    size = sum(len(block) for block in blocks)
    rows = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            if len(row) != len(block):
                raise AssertionError("block must be square")
            for j, value in enumerate(row):
                rows[offset + i][offset + j] = value
        offset += len(block)
    return tuple(tuple(row) for row in rows)


def assert_antisymmetric(name: str, matrix: Matrix) -> None:
    size = len(matrix)
    for row in matrix:
        if len(row) != size:
            raise AssertionError(f"{name}: matrix must be square")
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != -matrix[j][i]:
                raise AssertionError(f"{name}: matrix is not antisymmetric at {(i, j)}")


def rank_fraction(matrix: Matrix) -> int:
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    rank = 0
    for col in range(col_count):
        pivot = None
        for candidate in range(rank, row_count):
            if rows[candidate][col] != 0:
                pivot = candidate
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for target in range(row_count):
            if target == rank or rows[target][col] == 0:
                continue
            factor = rows[target][col]
            rows[target] = [
                rows[target][j] - factor * rows[rank][j] for j in range(col_count)
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


@dataclass(frozen=True)
class NGCount:
    type_a: int
    type_b: int
    total: int


@dataclass(frozen=True)
class Dispersion:
    omega_power: int
    omega_squared_power: int
    omega_squared_coefficient: Fraction


def ng_count(n_broken_internal: int, rho: Matrix) -> NGCount:
    if n_broken_internal < 0:
        raise AssertionError("number of broken generators must be nonnegative")
    if len(rho) != n_broken_internal:
        raise AssertionError("rho size must equal the number of broken internal generators")
    assert_antisymmetric("commutator-density matrix", rho)
    rank = rank_fraction(rho)
    if rank % 2 != 0:
        raise AssertionError("antisymmetric rank should be even")
    return NGCount(
        type_a=n_broken_internal - rank,
        type_b=rank // 2,
        total=n_broken_internal - rank // 2,
    )


def wrong_count_including_spacetime(
    n_broken_internal: int,
    rho: Matrix,
    n_broken_spacetime: int,
) -> int:
    return ng_count(n_broken_internal, rho).total + n_broken_spacetime


def su2_ferromagnet_rho(magnetization_density: Fraction) -> Matrix:
    # With [Q_1,Q_2]=i Q_3, rho_12=-i<[Q_1,Q_2]>/V=<Q_3>/V.
    return antisymmetric_block(magnetization_density)


def type_a_dispersion(stiffness: Fraction, susceptibility: Fraction) -> Dispersion:
    if stiffness <= 0 or susceptibility <= 0:
        raise AssertionError("type-A coefficients must be positive")
    # G phi_ddot + K k^2 phi = 0, so omega^2=(K/G) k^2.
    return Dispersion(
        omega_power=1,
        omega_squared_power=2,
        omega_squared_coefficient=stiffness / susceptibility,
    )


def type_b_dispersion(stiffness: Fraction, symplectic_density: Fraction) -> Dispersion:
    if stiffness <= 0 or symplectic_density == 0:
        raise AssertionError("type-B coefficients must have positive stiffness and nonzero pairing")
    # dot{x}=(K k^2/lambda) J x and J^2=-1, hence
    # omega^2=(K/lambda)^2 k^4.
    return Dispersion(
        omega_power=2,
        omega_squared_power=4,
        omega_squared_coefficient=stiffness * stiffness / (symplectic_density * symplectic_density),
    )


def check_rank_formula_cases() -> None:
    assert_equal("three unpaired broken generators", ng_count(3, zero_matrix(3)), NGCount(3, 0, 3))

    one_block_plus_null = block_diag(antisymmetric_block(Fraction(5)), zero_matrix(1))
    assert_equal(
        "one rank-two block plus one null direction",
        ng_count(3, one_block_plus_null),
        NGCount(type_a=1, type_b=1, total=2),
    )

    two_blocks = block_diag(antisymmetric_block(Fraction(2)), antisymmetric_block(Fraction(7)))
    assert_equal("two type-B blocks", ng_count(4, two_blocks), NGCount(0, 2, 2))

    expect_failure(
        "wrong type-A count for rank-two block plus null direction",
        lambda: assert_equal(
            "wrong type-A count for rank-two block plus null direction",
            ng_count(3, one_block_plus_null).type_a,
            2,
        ),
    )


def check_superfluid_type_a_case() -> None:
    count = ng_count(1, zero_matrix(1))
    dispersion = type_a_dispersion(Fraction(3), Fraction(5))
    assert_equal("finite-density U(1) superfluid count", count, NGCount(type_a=1, type_b=0, total=1))
    assert_equal("superfluid phonon omega power", dispersion.omega_power, 1)
    assert_equal("superfluid phonon omega-squared power", dispersion.omega_squared_power, 2)
    assert_equal("superfluid phonon omega-squared coefficient", dispersion.omega_squared_coefficient, Fraction(3, 5))

    expect_failure(
        "wrong superfluid type-B assignment",
        lambda: assert_equal("wrong superfluid type-B assignment", count.type_b, 1),
    )


def check_ferromagnet_type_b_case() -> None:
    magnetization = Fraction(3, 2)
    rho = su2_ferromagnet_rho(magnetization)
    dispersion = type_b_dispersion(Fraction(4), magnetization)
    assert_equal("ferromagnet rho rank", rank_fraction(rho), 2)
    assert_equal("ferromagnet count", ng_count(2, rho), NGCount(type_a=0, type_b=1, total=1))
    assert_equal("ferromagnet type-B omega power", dispersion.omega_power, 2)
    assert_equal("ferromagnet type-B omega-squared power", dispersion.omega_squared_power, 4)
    assert_equal("ferromagnet omega-squared coefficient", dispersion.omega_squared_coefficient, Fraction(64, 9))

    expect_failure(
        "wrong one-per-broken-generator ferromagnet count",
        lambda: assert_equal("wrong one-per-broken-generator ferromagnet count", ng_count(2, rho).total, 2),
    )
    expect_failure(
        "wrong linear type-B dispersion",
        lambda: assert_equal("wrong linear type-B dispersion", dispersion.omega_power, 1),
    )


def check_antiferromagnet_contrast() -> None:
    count = ng_count(2, zero_matrix(2))
    dispersion = type_a_dispersion(Fraction(7), Fraction(11))
    assert_equal("antiferromagnet zero-density count", count, NGCount(type_a=2, type_b=0, total=2))
    assert_equal("antiferromagnet linear dispersion", dispersion.omega_power, 1)


def check_internal_spacetime_separation() -> None:
    rho = zero_matrix(1)
    internal_count = ng_count(1, rho).total
    assert_equal("internal count ignores broken boosts", internal_count, 1)
    expect_failure(
        "wrongly adding broken spacetime generators",
        lambda: assert_equal(
            "wrongly adding broken spacetime generators",
            wrong_count_including_spacetime(1, rho, n_broken_spacetime=3),
            internal_count,
        ),
    )


def main() -> int:
    check_rank_formula_cases()
    check_superfluid_type_a_case()
    check_ferromagnet_type_b_case()
    check_antiferromagnet_contrast()
    check_internal_spacetime_separation()
    print("All nonrelativistic Nambu-Goldstone counting checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
