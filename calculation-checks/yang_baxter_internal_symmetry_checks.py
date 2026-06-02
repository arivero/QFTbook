#!/usr/bin/env python3
"""Exact finite checks for Yang--Baxter internal-symmetry conventions.

These checks accompany Volume VI, Chapter 3.  They verify three convention-
sensitive algebraic facts used in the chapter: the additive fixed-tensor
rational Yang--Baxter identity, the corresponding spectral classical
Yang--Baxter commutator identity for r(u)=P/u, and the O(N) vector-channel
projector decomposition into singlet, antisymmetric, and traceless-symmetric
subspaces.
"""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[Fraction]]


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def zero_matrix(n: int) -> Matrix:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def identity(n: int) -> Matrix:
    out = zero_matrix(n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def matmul(a: Matrix, b: Matrix) -> Matrix:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * entry for entry in row] for row in a]


def trace(a: Matrix) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def tensor_index(indices: tuple[int, ...], dim: int) -> int:
    out = 0
    for value in indices:
        out = dim * out + value
    return out


def tensor_indices(index: int, length: int, dim: int) -> tuple[int, ...]:
    values = [0] * length
    for position in range(length - 1, -1, -1):
        values[position] = index % dim
        index //= dim
    return tuple(values)


def flip_two_body(dim: int) -> Matrix:
    p = zero_matrix(dim * dim)
    for a in range(dim):
        for b in range(dim):
            incoming = dim * a + b
            outgoing = dim * b + a
            p[outgoing][incoming] = Fraction(1)
    return p


def pair_operator(pair: tuple[int, int], two_body: Matrix, *, dim: int, length: int = 3) -> Matrix:
    """Embed a two-body operator into V^{tensor length} in fixed tensor order."""

    size = dim**length
    op = zero_matrix(size)
    left, right = pair
    for incoming_index in range(size):
        incoming = tensor_indices(incoming_index, length, dim)
        two_body_incoming = dim * incoming[left] + incoming[right]
        for two_body_outgoing in range(dim * dim):
            coefficient = two_body[two_body_outgoing][two_body_incoming]
            if coefficient == 0:
                continue
            outgoing = list(incoming)
            outgoing[left] = two_body_outgoing // dim
            outgoing[right] = two_body_outgoing % dim
            op[tensor_index(tuple(outgoing), dim)][incoming_index] += coefficient
    return op


def rational_quantum_r(u: Fraction, dim: int) -> Matrix:
    """Yang's rational R-matrix in the convention R(u)=u Id + P."""

    return add(scale(u, identity(dim * dim)), flip_two_body(dim))


def rational_classical_r(u: Fraction, dim: int) -> Matrix:
    return scale(Fraction(1, 1) / u, flip_two_body(dim))


def check_additive_fixed_tensor_yang_baxter_identity() -> None:
    dim = 2
    u = Fraction(2)
    v = Fraction(5)
    r12 = pair_operator((0, 1), rational_quantum_r(u, dim), dim=dim)
    r13 = pair_operator((0, 2), rational_quantum_r(u + v, dim), dim=dim)
    r23 = pair_operator((1, 2), rational_quantum_r(v, dim), dim=dim)
    lhs = matmul(matmul(r12, r13), r23)
    rhs = matmul(matmul(r23, r13), r12)
    assert_equal(lhs, rhs, "additive fixed-tensor rational Yang-Baxter identity")


def check_spectral_classical_yang_baxter_identity() -> None:
    dim = 2
    u = Fraction(2)
    v = Fraction(5)
    r12 = pair_operator((0, 1), rational_classical_r(u, dim), dim=dim)
    r13 = pair_operator((0, 2), rational_classical_r(u + v, dim), dim=dim)
    r23 = pair_operator((1, 2), rational_classical_r(v, dim), dim=dim)
    lhs = add(add(commutator(r12, r13), commutator(r12, r23)), commutator(r13, r23))
    assert_equal(lhs, zero_matrix(dim**3), "spectral classical Yang-Baxter commutator identity")


def contraction_operator_on_vector_square(dim: int) -> Matrix:
    """The O(N)-invariant contraction K with K(e_k tensor e_l)=delta_kl sum_i e_i tensor e_i."""

    k_op = zero_matrix(dim * dim)
    for k in range(dim):
        incoming = dim * k + k
        for i in range(dim):
            outgoing = dim * i + i
            k_op[outgoing][incoming] = Fraction(1)
    return k_op


def check_on_vector_channel_projectors() -> None:
    dim = 3
    id_two = identity(dim * dim)
    flip = flip_two_body(dim)
    contraction = contraction_operator_on_vector_square(dim)
    p_singlet = scale(Fraction(1, dim), contraction)
    p_antisymmetric = scale(Fraction(1, 2), sub(id_two, flip))
    p_symmetric_traceless = sub(scale(Fraction(1, 2), add(id_two, flip)), p_singlet)

    projectors = {
        "singlet": p_singlet,
        "antisymmetric": p_antisymmetric,
        "symmetric traceless": p_symmetric_traceless,
    }
    for name, projector in projectors.items():
        assert_equal(matmul(projector, projector), projector, f"O(N) {name} projector idempotence")

    names = list(projectors)
    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            assert_equal(
                matmul(projectors[left], projectors[right]),
                zero_matrix(dim * dim),
                f"O(N) {left}/{right} projector orthogonality",
            )
            assert_equal(
                matmul(projectors[right], projectors[left]),
                zero_matrix(dim * dim),
                f"O(N) {right}/{left} projector orthogonality",
            )

    resolution = add(add(p_singlet, p_antisymmetric), p_symmetric_traceless)
    assert_equal(resolution, id_two, "O(N) vector tensor-square projector resolution")
    assert_equal(trace(p_singlet), Fraction(1), "O(N) singlet-channel rank")
    assert_equal(trace(p_antisymmetric), Fraction(dim * (dim - 1), 2), "O(N) antisymmetric-channel rank")
    assert_equal(
        trace(p_symmetric_traceless),
        Fraction(dim * (dim + 1), 2) - 1,
        "O(N) symmetric-traceless-channel rank",
    )


def main() -> None:
    check_additive_fixed_tensor_yang_baxter_identity()
    check_spectral_classical_yang_baxter_identity()
    check_on_vector_channel_projectors()
    print("All Yang-Baxter internal-symmetry checks passed.")


if __name__ == "__main__":
    main()
