#!/usr/bin/env python3
"""Finite sign checks for the conformal-algebra conventions.

The checks use vector fields as the primary object.  Hermitian charges are
then compared through the convention

    [Q_X, Q_Y] = - i Q_[X,Y].

This prevents a sign from being accepted merely because two displayed charge
formulae share the same mistake.
"""

from __future__ import annotations

import itertools
from collections import defaultdict

import sympy as sp


II = sp.I
DIMENSION = 4
X = sp.symbols("x0:4")
EUCLIDEAN = (1, 1, 1, 1)
LORENTZIAN = (-1, 1, 1, 1)

Basis = tuple[str, int | None, int | None]
Linear = dict[Basis, sp.Expr]
VectorField = tuple[sp.Expr, ...]


def p(mu: int) -> Basis:
    return ("P", mu, None)


def k(mu: int) -> Basis:
    return ("K", mu, None)


def d() -> Basis:
    return ("D", None, None)


def j(mu: int, nu: int) -> Basis:
    if mu == nu:
        raise ValueError("antisymmetric generator has distinct indices")
    if mu < nu:
        return ("J", mu, nu)
    return ("J", nu, mu)


def j_sign(mu: int, nu: int) -> int:
    if mu == nu:
        return 0
    return 1 if mu < nu else -1


def metric(metric_diag: tuple[int, ...], mu: int, nu: int) -> int:
    return metric_diag[mu] if mu == nu else 0


def vector_add(*fields: VectorField) -> VectorField:
    return tuple(sum(field[i] for field in fields) for i in range(DIMENSION))


def vector_scale(coeff: sp.Expr, field: VectorField) -> VectorField:
    return tuple(coeff * component for component in field)


def vector_zero() -> VectorField:
    return tuple(sp.Integer(0) for _ in range(DIMENSION))


def vector_for_basis(basis: Basis, metric_diag: tuple[int, ...]) -> VectorField:
    kind, a, b = basis
    if kind == "D":
        return tuple(X[alpha] for alpha in range(DIMENSION))

    assert a is not None
    if kind == "P":
        return tuple(metric(metric_diag, a, alpha) for alpha in range(DIMENSION))

    if kind == "K":
        x_square = sum(metric_diag[beta] * X[beta] * X[beta] for beta in range(DIMENSION))
        return tuple(
            x_square * metric(metric_diag, a, alpha)
            - 2 * X[a] * X[alpha]
            for alpha in range(DIMENSION)
        )

    assert kind == "J" and b is not None
    return tuple(
        X[a] * metric(metric_diag, b, alpha)
        - X[b] * metric(metric_diag, a, alpha)
        for alpha in range(DIMENSION)
    )


def vector_for_linear(linear: Linear, metric_diag: tuple[int, ...]) -> VectorField:
    out = vector_zero()
    for basis, coeff in linear.items():
        out = vector_add(out, vector_scale(coeff, vector_for_basis(basis, metric_diag)))
    return out


def lie_bracket(left: VectorField, right: VectorField) -> VectorField:
    components: list[sp.Expr] = []
    for alpha in range(DIMENSION):
        left_on_right = sum(left[beta] * sp.diff(right[alpha], X[beta]) for beta in range(DIMENSION))
        right_on_left = sum(right[beta] * sp.diff(left[alpha], X[beta]) for beta in range(DIMENSION))
        components.append(sp.expand(left_on_right - right_on_left))
    return tuple(components)


def assert_vector_equal(label: str, actual: VectorField, expected: VectorField) -> None:
    for alpha, (a_component, e_component) in enumerate(zip(actual, expected)):
        diff = sp.expand(a_component - e_component)
        if diff != 0:
            raise AssertionError(f"{label}: component {alpha} differs by {diff}")


def assert_charge_relation(
    label: str,
    left: Basis,
    right: Basis,
    charge_rhs: Linear,
    metric_diag: tuple[int, ...],
) -> None:
    """Check a displayed Hermitian-charge commutator against vector fields."""

    actual_vector_bracket = lie_bracket(
        vector_for_basis(left, metric_diag),
        vector_for_basis(right, metric_diag),
    )
    # Since [Q_X,Q_Y] = -i Q_[X,Y], a displayed charge coefficient c
    # corresponds to vector-field coefficient i c.
    expected_vector_bracket = vector_for_linear(
        {basis: II * coeff for basis, coeff in charge_rhs.items()},
        metric_diag,
    )
    assert_vector_equal(label, actual_vector_bracket, expected_vector_bracket)


def add_term(out: defaultdict[Basis, sp.Expr], coeff: sp.Expr, basis: Basis | None) -> None:
    if basis is None or coeff == 0:
        return
    out[basis] += coeff


def canonical_j_term(mu: int, nu: int) -> tuple[int, Basis | None]:
    sign = j_sign(mu, nu)
    if sign == 0:
        return 0, None
    return sign, j(mu, nu)


def conformal_charge_bracket_basis(left: Basis, right: Basis, metric_diag: tuple[int, ...]) -> Linear:
    kind_l, a, b = left
    kind_r, c, e = right
    out: defaultdict[Basis, sp.Expr] = defaultdict(lambda: sp.Integer(0))

    if kind_l == "P" and kind_r == "P":
        return {}
    if kind_l == "K" and kind_r == "K":
        return {}
    if kind_l == "D" and kind_r == "D":
        return {}

    if kind_l == "D" and kind_r == "P":
        assert c is not None
        return {p(c): II}
    if kind_l == "P" and kind_r == "D":
        return scale(conformal_charge_bracket_basis(right, left, metric_diag), -1)

    if kind_l == "D" and kind_r == "K":
        assert c is not None
        return {k(c): -II}
    if kind_l == "K" and kind_r == "D":
        return scale(conformal_charge_bracket_basis(right, left, metric_diag), -1)

    if kind_l == "D" and kind_r == "J":
        return {}
    if kind_l == "J" and kind_r == "D":
        return {}

    if kind_l == "P" and kind_r == "K":
        assert a is not None and c is not None
        add_term(out, 2 * II * metric(metric_diag, a, c), d())
        sign, basis = canonical_j_term(a, c)
        add_term(out, -2 * II * sign, basis)
        return dict(out)
    if kind_l == "K" and kind_r == "P":
        return scale(conformal_charge_bracket_basis(right, left, metric_diag), -1)

    if kind_l == "J" and kind_r in {"P", "K"}:
        assert a is not None and b is not None and c is not None
        target = p if kind_r == "P" else k
        add_term(out, II * metric(metric_diag, c, a), target(b))
        add_term(out, -II * metric(metric_diag, c, b), target(a))
        return dict(out)
    if kind_l in {"P", "K"} and kind_r == "J":
        return scale(conformal_charge_bracket_basis(right, left, metric_diag), -1)

    assert kind_l == "J" and kind_r == "J"
    assert a is not None and b is not None and c is not None and e is not None
    terms = [
        (+II * metric(metric_diag, a, c), (b, e)),
        (-II * metric(metric_diag, b, c), (a, e)),
        (-II * metric(metric_diag, a, e), (b, c)),
        (+II * metric(metric_diag, b, e), (a, c)),
    ]
    for coeff, (mu, nu) in terms:
        sign, basis = canonical_j_term(mu, nu)
        add_term(out, coeff * sign, basis)
    return dict(out)


def scale(vec: Linear, factor: sp.Expr) -> Linear:
    return {basis: factor * coeff for basis, coeff in vec.items() if coeff != 0}


def linear_add(*vectors: Linear) -> Linear:
    out: defaultdict[Basis, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for vector in vectors:
        for basis, coeff in vector.items():
            out[basis] += coeff
    return {basis: coeff for basis, coeff in out.items() if coeff != 0}


def linear_bracket(left: Linear, right: Linear, metric_diag: tuple[int, ...]) -> Linear:
    out: defaultdict[Basis, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for b_left, c_left in left.items():
        for b_right, c_right in right.items():
            for basis, coeff in conformal_charge_bracket_basis(b_left, b_right, metric_diag).items():
                out[basis] += c_left * c_right * coeff
    return {basis: coeff for basis, coeff in out.items() if coeff != 0}


def assert_linear_equal(label: str, actual: Linear, expected: Linear) -> None:
    for basis in set(actual) | set(expected):
        diff = sp.expand(actual.get(basis, 0) - expected.get(basis, 0))
        if diff != 0:
            raise AssertionError(f"{label}: coefficient of {basis} differs by {diff}")


def check_displayed_charge_relations(metric_diag: tuple[int, ...], label_prefix: str) -> None:
    for mu in range(DIMENSION):
        assert_charge_relation(
            f"{label_prefix} [D,P{mu}]",
            d(),
            p(mu),
            {p(mu): II},
            metric_diag,
        )
        assert_charge_relation(
            f"{label_prefix} [D,K{mu}]",
            d(),
            k(mu),
            {k(mu): -II},
            metric_diag,
        )
    for rho in range(DIMENSION):
        for sigma in range(rho + 1, DIMENSION):
            assert_charge_relation(
                f"{label_prefix} [D,J{rho}{sigma}]",
                d(),
                j(rho, sigma),
                {},
                metric_diag,
            )

    for mu, nu in itertools.product(range(DIMENSION), repeat=2):
        charge_rhs: Linear = {d(): 2 * II * metric(metric_diag, mu, nu)}
        sign, basis = canonical_j_term(mu, nu)
        if basis is not None:
            charge_rhs[basis] = charge_rhs.get(basis, 0) - 2 * II * sign
        assert_charge_relation(
            f"{label_prefix} [P{mu},K{nu}]",
            p(mu),
            k(nu),
            charge_rhs,
            metric_diag,
        )

    for rho in range(DIMENSION):
        for sigma in range(rho + 1, DIMENSION):
            for mu in range(DIMENSION):
                for target_name, target_builder in (("P", p), ("K", k)):
                    charge_rhs = {
                        target_builder(sigma): II * metric(metric_diag, mu, rho),
                        target_builder(rho): -II * metric(metric_diag, mu, sigma),
                    }
                    assert_charge_relation(
                        f"{label_prefix} [J{rho}{sigma},{target_name}{mu}]",
                        j(rho, sigma),
                        target_builder(mu),
                        charge_rhs,
                        metric_diag,
                    )


def check_conformal_jacobi(metric_diag: tuple[int, ...], label_prefix: str) -> None:
    basis = (
        [p(mu) for mu in range(DIMENSION)]
        + [k(mu) for mu in range(DIMENSION)]
        + [d()]
        + [j(mu, nu) for mu in range(DIMENSION) for nu in range(mu + 1, DIMENSION)]
    )
    for x, y, z in itertools.product(basis, repeat=3):
        jacobi = linear_add(
            linear_bracket({x: 1}, linear_bracket({y: 1}, {z: 1}, metric_diag), metric_diag),
            linear_bracket({y: 1}, linear_bracket({z: 1}, {x: 1}, metric_diag), metric_diag),
            linear_bracket({z: 1}, linear_bracket({x: 1}, {y: 1}, metric_diag), metric_diag),
        )
        assert_linear_equal(f"{label_prefix} conformal Jacobi {x},{y},{z}", jacobi, {})


def check_load_bearing_jacobi_families(metric_diag: tuple[int, ...], label_prefix: str) -> None:
    """Check the Jacobi families most sensitive to sign mistakes.

    The full differential-vector-field realization used above is a Lie algebra,
    so the complete Jacobi identity is automatic.  These finite samples keep
    the regression focused on the sign-sensitive brackets without making the
    elementary convention script unnecessarily slow.
    """

    triples: list[tuple[Basis, Basis, Basis]] = []
    for mu, nu in itertools.product(range(DIMENSION), repeat=2):
        triples.append((d(), p(mu), k(nu)))
        triples.append((p(mu), k(nu), k((mu + nu) % DIMENSION)))
    for rho in range(DIMENSION):
        for sigma in range(rho + 1, DIMENSION):
            for mu, nu in itertools.product(range(DIMENSION), repeat=2):
                triples.append((j(rho, sigma), p(mu), k(nu)))
            for alpha in range(DIMENSION):
                triples.append((j(rho, sigma), j((rho + 1) % DIMENSION, (sigma + 1) % DIMENSION), p(alpha)))

    for x, y, z in triples:
        jacobi = linear_add(
            linear_bracket({x: 1}, linear_bracket({y: 1}, {z: 1}, metric_diag), metric_diag),
            linear_bracket({y: 1}, linear_bracket({z: 1}, {x: 1}, metric_diag), metric_diag),
            linear_bracket({z: 1}, linear_bracket({x: 1}, {y: 1}, metric_diag), metric_diag),
        )
        assert_linear_equal(f"{label_prefix} sign-sensitive Jacobi {x},{y},{z}", jacobi, {})


def ambient_basis(label: str, mu: int | None = None) -> Linear:
    """Euclidean chapter map from so(D+1,1) ambient generators.

    label="m" denotes the ambient (-1,mu) generator, label="0" the (0,mu)
    generator, and label="d" the (0,-1) dilatation generator when mu is None.
    """

    if label == "d":
        return {d(): 1}
    assert mu is not None
    if label == "0":
        return {p(mu): sp.Rational(1, 2), k(mu): sp.Rational(-1, 2)}
    if label == "m":
        return {p(mu): sp.Rational(1, 2), k(mu): sp.Rational(1, 2)}
    raise ValueError(label)


def ambient_pair_to_conformal(a: str | int, b_value: str | int) -> Linear:
    if a == b_value:
        return {}
    if isinstance(a, int) and isinstance(b_value, int):
        return {j(a, b_value): j_sign(a, b_value)}
    if {a, b_value} == {"0", "m"}:
        return ambient_basis("d") if (a, b_value) == ("0", "m") else scale(ambient_basis("d"), -1)
    if a == "0" and isinstance(b_value, int):
        return ambient_basis("0", b_value)
    if isinstance(a, int) and b_value == "0":
        return scale(ambient_basis("0", a), -1)
    if a == "m" and isinstance(b_value, int):
        return ambient_basis("m", b_value)
    if isinstance(a, int) and b_value == "m":
        return scale(ambient_basis("m", a), -1)
    raise ValueError((a, b_value))


def ambient_metric(index: str | int) -> int:
    if index == "m":
        return -1
    return 1


def check_euclidean_ambient_change_of_basis() -> None:
    ambient_indices: list[str | int] = ["m", "0", 0, 1, 2, 3]
    ambient_pairs = [
        (ambient_indices[a], ambient_indices[b])
        for a in range(len(ambient_indices))
        for b in range(a + 1, len(ambient_indices))
    ]

    def generator(a: str | int, b_value: str | int) -> Linear:
        return ambient_pair_to_conformal(a, b_value)

    def eta(a: str | int, b_value: str | int) -> int:
        return ambient_metric(a) if a == b_value else 0

    for (a, b_value), (c, e) in itertools.product(ambient_pairs, repeat=2):
        lhs = linear_bracket(generator(a, b_value), generator(c, e), EUCLIDEAN)
        rhs = linear_add(
            scale(generator(b_value, e), II * eta(a, c)),
            scale(generator(a, e), -II * eta(b_value, c)),
            scale(generator(b_value, c), -II * eta(a, e)),
            scale(generator(a, c), II * eta(b_value, e)),
        )
        assert_linear_equal(f"Euclidean so(D+1,1) basis {a}{b_value},{c}{e}", lhs, rhs)


def check_radial_real_form() -> None:
    """Check the radial map used in the unitarity-bound chapters."""

    def to_radial(linear: Linear) -> Linear:
        out: defaultdict[Basis, sp.Expr] = defaultdict(lambda: sp.Integer(0))
        for basis, coeff in linear.items():
            kind, a, b = basis
            if kind == "D":
                out[basis] += coeff * II
            elif kind == "J":
                out[basis] += coeff * II
            elif kind == "P":
                out[basis] += coeff * (-II)
            elif kind == "K":
                out[basis] += coeff * II
            else:
                raise ValueError(kind)
        return {basis: coeff for basis, coeff in out.items() if coeff != 0}

    def radial_bracket(left: Basis, right: Basis) -> Linear:
        # Invert the map:
        # D_rad=-i D_L, J_rad=-i J_L, P_rad=i P_L, K_rad=-i K_L.
        inverse_coeff = {"D": II, "J": II, "P": -II, "K": II}
        kind_l = left[0]
        kind_r = right[0]
        lorentzian_left = {left: inverse_coeff[kind_l]}
        lorentzian_right = {right: inverse_coeff[kind_r]}
        return to_radial(linear_bracket(lorentzian_left, lorentzian_right, EUCLIDEAN))

    for mu in range(DIMENSION):
        assert_linear_equal(f"radial [D,P{mu}]", radial_bracket(d(), p(mu)), {p(mu): 1})
        assert_linear_equal(f"radial [D,K{mu}]", radial_bracket(d(), k(mu)), {k(mu): -1})

    for mu, nu in itertools.product(range(DIMENSION), repeat=2):
        expected: Linear = {d(): -2 * metric(EUCLIDEAN, mu, nu)}
        sign, basis = canonical_j_term(mu, nu)
        if basis is not None:
            expected[basis] = expected.get(basis, 0) + 2 * sign
        assert_linear_equal(f"radial [P{mu},K{nu}]", radial_bracket(p(mu), k(nu)), expected)

        expected_kp: Linear = {d(): 2 * metric(EUCLIDEAN, mu, nu)}
        sign, basis = canonical_j_term(nu, mu)
        if basis is not None:
            expected_kp[basis] = expected_kp.get(basis, 0) - 2 * sign
        assert_linear_equal(f"radial [K{mu},P{nu}]", radial_bracket(k(mu), p(nu)), expected_kp)


def main() -> None:
    check_displayed_charge_relations(EUCLIDEAN, "Euclidean")
    check_displayed_charge_relations(LORENTZIAN, "Lorentzian")
    check_load_bearing_jacobi_families(EUCLIDEAN, "Euclidean")
    check_load_bearing_jacobi_families(LORENTZIAN, "Lorentzian")
    check_euclidean_ambient_change_of_basis()
    check_radial_real_form()
    print("All conformal-algebra sign checks passed.")


if __name__ == "__main__":
    main()
