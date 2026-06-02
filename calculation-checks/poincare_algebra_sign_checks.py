#!/usr/bin/env python3
"""Finite sign checks for the Volume I Poincare-algebra convention."""

from __future__ import annotations

import itertools
from collections import defaultdict

import sympy as sp


II = sp.I
ETA = [-1, 1, 1, 1]


Basis = tuple[str, int, int | None]
Linear = dict[Basis, sp.Expr]


def p(mu: int) -> Basis:
    return ("P", mu, None)


def j(mu: int, nu: int) -> Basis:
    if mu == nu:
        raise ValueError("antisymmetric Lorentz generator has distinct indices")
    if mu < nu:
        return ("J", mu, nu)
    return ("J", nu, mu)


def j_sign(mu: int, nu: int) -> int:
    if mu == nu:
        return 0
    return 1 if mu < nu else -1


def add_term(out: defaultdict[Basis, sp.Expr], coeff: sp.Expr, basis: Basis | None) -> None:
    if basis is None or coeff == 0:
        return
    out[basis] += coeff


def metric(mu: int, nu: int) -> int:
    return ETA[mu] if mu == nu else 0


def canonical_j_term(mu: int, nu: int) -> tuple[int, Basis | None]:
    sign = j_sign(mu, nu)
    if sign == 0:
        return 0, None
    return sign, j(mu, nu)


def bracket_basis(left: Basis, right: Basis, p_j_sign: int = -1) -> Linear:
    """Return [left,right].

    ``p_j_sign=-1`` is the convention used in the monograph:
    [P^mu,J^{rho sigma}] = -i(eta^{mu rho} P^sigma - eta^{mu sigma} P^rho).
    The alternative ``+1`` is used only to verify that the old sign fails.
    """

    kind_l, a, b = left
    kind_r, c, d = right
    out: defaultdict[Basis, sp.Expr] = defaultdict(lambda: sp.Integer(0))

    if kind_l == "P" and kind_r == "P":
        return {}

    if kind_l == "P" and kind_r == "J":
        assert d is not None
        add_term(out, p_j_sign * II * metric(a, c), p(d))
        add_term(out, -p_j_sign * II * metric(a, d), p(c))
        return dict(out)

    if kind_l == "J" and kind_r == "P":
        return scale(bracket_basis(right, left, p_j_sign), -1)

    assert b is not None and d is not None
    terms = [
        (-II * metric(b, c), (a, d)),
        (+II * metric(a, c), (b, d)),
        (+II * metric(b, d), (a, c)),
        (-II * metric(a, d), (b, c)),
    ]
    for coeff, (mu, nu) in terms:
        sign, basis = canonical_j_term(mu, nu)
        add_term(out, coeff * sign, basis)
    return dict(out)


def scale(vec: Linear, factor: sp.Expr) -> Linear:
    return {basis: sp.simplify(factor * coeff) for basis, coeff in vec.items() if coeff != 0}


def add(left: Linear, right: Linear) -> Linear:
    out: defaultdict[Basis, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for vec in (left, right):
        for basis, coeff in vec.items():
            out[basis] += coeff
    return {basis: sp.simplify(coeff) for basis, coeff in out.items() if sp.simplify(coeff) != 0}


def bracket(left: Linear, right: Linear, p_j_sign: int = -1) -> Linear:
    out: defaultdict[Basis, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for b_left, c_left in left.items():
        for b_right, c_right in right.items():
            for basis, coeff in bracket_basis(b_left, b_right, p_j_sign).items():
                out[basis] += c_left * c_right * coeff
    return {basis: sp.simplify(coeff) for basis, coeff in out.items() if sp.simplify(coeff) != 0}


def unit(basis: Basis) -> Linear:
    return {basis: sp.Integer(1)}


def assert_equal(label: str, actual: Linear, expected: Linear) -> None:
    all_basis = set(actual) | set(expected)
    for basis in all_basis:
        diff = sp.simplify(actual.get(basis, 0) - expected.get(basis, 0))
        if diff != 0:
            raise AssertionError(f"{label}: coefficient of {basis} differs by {diff}")


def jacobi(x: Basis, y: Basis, z: Basis, p_j_sign: int = -1) -> Linear:
    return add(
        add(
            bracket(unit(x), bracket(unit(y), unit(z), p_j_sign), p_j_sign),
            bracket(unit(y), bracket(unit(z), unit(x), p_j_sign), p_j_sign),
        ),
        bracket(unit(z), bracket(unit(x), unit(y), p_j_sign), p_j_sign),
    )


def check_all_jacobi_identities() -> None:
    basis = [p(mu) for mu in range(4)] + [j(mu, nu) for mu in range(4) for nu in range(mu + 1, 4)]
    for x, y, z in itertools.product(basis, repeat=3):
        assert_equal(f"Jacobi {x},{y},{z}", jacobi(x, y, z), {})


def check_rotation_and_boost_signs() -> None:
    assert_equal("[J12,P1]=+i P2", bracket(unit(j(1, 2)), unit(p(1))), {p(2): II})
    assert_equal("[J12,P2]=-i P1", bracket(unit(j(1, 2)), unit(p(2))), {p(1): -II})
    assert_equal("[P0,J01]=+i P1", bracket(unit(p(0)), unit(j(0, 1))), {p(1): II})


def check_old_sign_fails_issue_jacobi() -> None:
    failed = jacobi(p(0), j(0, 2), j(1, 2), p_j_sign=+1)
    if failed == {}:
        raise AssertionError("old [P,J] sign unexpectedly passed the issue Jacobi test")


def vector_generator(mu: int, nu: int) -> sp.Matrix:
    matrix = sp.zeros(4, 4)
    for rho in range(4):
        for sigma in range(4):
            matrix[rho, sigma] = -II * (
                metric(mu, rho) * (1 if nu == sigma else 0)
                - metric(nu, rho) * (1 if mu == sigma else 0)
            )
    return matrix


def chapter17_lorentz_rhs(mu: int, nu: int, rho: int, sigma: int) -> sp.Matrix:
    return -II * (
        metric(nu, rho) * vector_generator(mu, sigma)
        - metric(mu, rho) * vector_generator(nu, sigma)
        - metric(nu, sigma) * vector_generator(mu, rho)
        + metric(mu, sigma) * vector_generator(nu, rho)
    )


def assert_matrix_equal(label: str, actual: sp.Matrix, expected: sp.Matrix) -> None:
    diff = (actual - expected).applyfunc(sp.simplify)
    if diff != sp.zeros(*actual.shape):
        raise AssertionError(f"{label}:\n{actual}\n!=\n{expected}")


def check_vector_representation_and_massless_little_group() -> None:
    for mu, nu, rho, sigma in itertools.product(range(4), repeat=4):
        if mu == nu or rho == sigma:
            continue
        lhs = vector_generator(mu, nu) * vector_generator(rho, sigma) - vector_generator(rho, sigma) * vector_generator(mu, nu)
        rhs = chapter17_lorentz_rhs(mu, nu, rho, sigma)
        assert_matrix_equal(f"vector Lorentz commutator {mu}{nu},{rho}{sigma}", lhs, rhs)

    j3 = vector_generator(1, 2)
    n1 = vector_generator(0, 1) + vector_generator(3, 1)
    n2 = vector_generator(0, 2) + vector_generator(3, 2)
    assert_matrix_equal("massless little group [N1,N2]", n1 * n2 - n2 * n1, sp.zeros(4, 4))
    assert_matrix_equal("massless little group [J3,N1]", j3 * n1 - n1 * j3, II * n2)
    assert_matrix_equal("massless little group [J3,N2]", j3 * n2 - n2 * j3, -II * n1)


def main() -> None:
    check_all_jacobi_identities()
    check_rotation_and_boost_signs()
    check_old_sign_fails_issue_jacobi()
    check_vector_representation_and_massless_little_group()
    print("All Poincare-algebra sign checks passed.")


if __name__ == "__main__":
    main()
