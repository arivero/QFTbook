#!/usr/bin/env python3
"""Exact checks for conformal-algebra and light-transform conventions.

The manuscript uses three related convention layers:

1. Euclidean conformal Killing vector fields with
   M_{mu nu}=x_mu d_nu-x_nu d_mu and
   K_mu=x^2 d_mu-2 x_mu x.rho d_rho.
2. Hermitian charges with U(s)=exp(i s Q), so
   [Q_X,Q_Y]=-i Q_[X,Y].
3. The radial real form used for descendant Gram matrices.

This script checks the sign table tying those layers to the
light-transform weight map (Delta,J)->(1-J,1-Delta).  It is finite
polynomial algebra, not a check of the analytic existence of the light
transform as an operator-valued distribution.
"""

from __future__ import annotations

from fractions import Fraction


DIM = 3
Monomial = tuple[int, ...]
Poly = dict[Monomial, Fraction]
VectorField = tuple[Poly, ...]
ComplexCoeff = tuple[Fraction, Fraction]


def clean(poly: Poly) -> Poly:
    return {monomial: coeff for monomial, coeff in poly.items() if coeff}


def monomial(exponents: tuple[int, ...], coefficient: Fraction = Fraction(1)) -> Poly:
    return clean({exponents: coefficient})


def const(coefficient: Fraction | int) -> Poly:
    return monomial((0,) * DIM, Fraction(coefficient))


def var(index: int) -> Poly:
    exponents = [0] * DIM
    exponents[index] = 1
    return monomial(tuple(exponents))


def poly_add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for mon, coeff in right.items():
        out[mon] = out.get(mon, Fraction(0)) + coeff
    return clean(out)


def poly_neg(poly: Poly) -> Poly:
    return {mon: -coeff for mon, coeff in poly.items()}


def poly_sub(left: Poly, right: Poly) -> Poly:
    return poly_add(left, poly_neg(right))


def poly_scale(scale: Fraction | int, poly: Poly) -> Poly:
    return clean({mon: Fraction(scale) * coeff for mon, coeff in poly.items()})


def poly_mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for left_mon, left_coeff in left.items():
        for right_mon, right_coeff in right.items():
            mon = tuple(a + b for a, b in zip(left_mon, right_mon))
            out[mon] = out.get(mon, Fraction(0)) + left_coeff * right_coeff
    return clean(out)


def poly_derivative(poly: Poly, index: int) -> Poly:
    out: Poly = {}
    for mon, coeff in poly.items():
        if mon[index] == 0:
            continue
        new_mon = list(mon)
        new_mon[index] -= 1
        out[tuple(new_mon)] = out.get(tuple(new_mon), Fraction(0)) + coeff * mon[index]
    return clean(out)


def vf_add(left: VectorField, right: VectorField) -> VectorField:
    return tuple(poly_add(a, b) for a, b in zip(left, right))


def vf_neg(field: VectorField) -> VectorField:
    return tuple(poly_neg(component) for component in field)


def vf_sub(left: VectorField, right: VectorField) -> VectorField:
    return vf_add(left, vf_neg(right))


def vf_scale(scale: Fraction | int, field: VectorField) -> VectorField:
    return tuple(poly_scale(scale, component) for component in field)


def zero_vf() -> VectorField:
    return tuple({} for _ in range(DIM))


def bracket(left: VectorField, right: VectorField) -> VectorField:
    components: list[Poly] = []
    for target in range(DIM):
        component: Poly = {}
        for source in range(DIM):
            component = poly_add(
                component,
                poly_sub(
                    poly_mul(left[source], poly_derivative(right[target], source)),
                    poly_mul(right[source], poly_derivative(left[target], source)),
                ),
            )
        components.append(component)
    return tuple(components)


def p(mu: int) -> VectorField:
    components = [{} for _ in range(DIM)]
    components[mu] = const(1)
    return tuple(components)


def dilation() -> VectorField:
    return tuple(var(i) for i in range(DIM))


def rotation(mu: int, nu: int) -> VectorField:
    components = [{} for _ in range(DIM)]
    components[nu] = poly_add(components[nu], var(mu))
    components[mu] = poly_sub(components[mu], var(nu))
    return tuple(components)


def x_squared() -> Poly:
    out: Poly = {}
    for i in range(DIM):
        out = poly_add(out, poly_mul(var(i), var(i)))
    return out


def special_conformal(mu: int) -> VectorField:
    components: list[Poly] = []
    for rho in range(DIM):
        term = poly_scale(-2, poly_mul(var(mu), var(rho)))
        if rho == mu:
            term = poly_add(term, x_squared())
        components.append(term)
    return tuple(components)


def assert_vf(name: str, got: VectorField, expected: VectorField) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_conformal_killing_brackets() -> None:
    d = dilation()
    zero = zero_vf()

    for mu in range(DIM):
        assert_vf(f"[D,P_{mu}]", bracket(d, p(mu)), vf_neg(p(mu)))
        assert_vf(f"[D,K_{mu}]", bracket(d, special_conformal(mu)), special_conformal(mu))
        assert_vf(f"[P_{mu},P_{mu}]", bracket(p(mu), p(mu)), zero)
        assert_vf(f"[K_{mu},K_{mu}]", bracket(special_conformal(mu), special_conformal(mu)), zero)
        for nu in range(DIM):
            assert_vf(f"[P_{mu},P_{nu}]", bracket(p(mu), p(nu)), zero)
            assert_vf(f"[K_{mu},K_{nu}]", bracket(special_conformal(mu), special_conformal(nu)), zero)

            expected_pk = vf_scale(2, rotation(mu, nu))
            if mu == nu:
                expected_pk = vf_sub(expected_pk, vf_scale(2, d))
            assert_vf(f"[P_{mu},K_{nu}]", bracket(p(mu), special_conformal(nu)), expected_pk)

            for rho in range(DIM):
                expected_mp = zero
                if rho == nu:
                    expected_mp = vf_add(expected_mp, p(mu))
                if rho == mu:
                    expected_mp = vf_sub(expected_mp, p(nu))
                assert_vf(
                    f"[M_{mu}{nu},P_{rho}]",
                    bracket(rotation(mu, nu), p(rho)),
                    expected_mp,
                )

            for rho in range(DIM):
                for sigma in range(DIM):
                    expected_mm = zero
                    if nu == rho:
                        expected_mm = vf_add(expected_mm, rotation(mu, sigma))
                    if mu == rho:
                        expected_mm = vf_sub(expected_mm, rotation(nu, sigma))
                    if nu == sigma:
                        expected_mm = vf_sub(expected_mm, rotation(mu, rho))
                    if mu == sigma:
                        expected_mm = vf_add(expected_mm, rotation(nu, rho))
                    assert_vf(
                        f"[M_{mu}{nu},M_{rho}{sigma}]",
                        bracket(rotation(mu, nu), rotation(rho, sigma)),
                        expected_mm,
                    )


def charge_i_coeff_from_vector_coeff(coeff: Fraction) -> Fraction:
    """If [X,Y]=coeff*Z, then [Q_X,Q_Y]=i*(-coeff)*Q_Z."""

    return -coeff


def check_charge_sign_conversion() -> None:
    assert_equal("[Dhat,Phat] i-coefficient", charge_i_coeff_from_vector_coeff(Fraction(-1)), Fraction(1))
    assert_equal("[Dhat,Khat] i-coefficient", charge_i_coeff_from_vector_coeff(Fraction(1)), Fraction(-1))
    assert_equal("[Phat,Khat] D i-coefficient", charge_i_coeff_from_vector_coeff(Fraction(-2)), Fraction(2))
    assert_equal("[Phat,Khat] M i-coefficient", charge_i_coeff_from_vector_coeff(Fraction(2)), Fraction(-2))


def cadd(left: ComplexCoeff, right: ComplexCoeff) -> ComplexCoeff:
    return (left[0] + right[0], left[1] + right[1])


def cmul(left: ComplexCoeff, right: ComplexCoeff) -> ComplexCoeff:
    return (left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0])


def cscale(scale: Fraction | int, value: ComplexCoeff) -> ComplexCoeff:
    return (Fraction(scale) * value[0], Fraction(scale) * value[1])


def check_radial_real_form_conversion() -> None:
    one: ComplexCoeff = (Fraction(1), Fraction(0))
    i: ComplexCoeff = (Fraction(0), Fraction(1))
    minus_i: ComplexCoeff = (Fraction(0), Fraction(-1))

    # P_rad=i P_L and K_rad=-i K_L, so the prefactor multiplying the
    # Lorentzian [P_L,K_L] bracket is one.
    prefactor = cmul(i, minus_i)
    assert_equal("P_rad K_rad prefactor", prefactor, one)

    # [P_L,K_L]=i(2 delta D_L - 2 J_L), and
    # D_L=i D_rad, J_L=i J_rad.
    d_rad_coeff = cmul(cscale(2, i), i)
    j_rad_coeff = cmul(cscale(-2, i), i)
    assert_equal("[P_rad,K_rad] D coefficient", d_rad_coeff, (Fraction(-2), Fraction(0)))
    assert_equal("[P_rad,K_rad] J coefficient", j_rad_coeff, (Fraction(2), Fraction(0)))

    # Antisymmetry and J_{nu mu}=-J_{mu nu} give the displayed Gram-matrix
    # convention [K_mu,P_nu]=2 delta D - 2 J_{nu mu}.
    kp_d_coeff = cscale(-1, d_rad_coeff)
    # [K_mu,P_nu] is -[P_nu,K_mu].  The latter contains
    # +2 J_{nu mu}, so the displayed coefficient of J_{nu mu} is -2.
    kp_j_numu_coeff = cscale(-1, j_rad_coeff)
    assert_equal("[K_rad,P_rad] D coefficient", kp_d_coeff, (Fraction(2), Fraction(0)))
    assert_equal("[K_rad_mu,P_rad_nu] J_numu coefficient", kp_j_numu_coeff, (Fraction(-2), Fraction(0)))


def check_light_transform_weight_map() -> None:
    test_pairs = (
        (Fraction(3, 1), Fraction(1, 1)),
        (Fraction(4, 1), Fraction(2, 1)),
        (Fraction(5, 1), Fraction(3, 1)),
        (Fraction(7, 2), Fraction(5, 2)),
    )
    for delta, spin in test_pairs:
        p_homogeneity = spin - 1
        z_homogeneity = 1 - delta
        transformed_delta = 1 - spin
        transformed_spin = 1 - delta
        assert_equal("P homogeneity equals -Delta_L", p_homogeneity, -transformed_delta)
        assert_equal("Z homogeneity equals J_L", z_homogeneity, transformed_spin)

    spacetime_dimension = Fraction(4, 1)
    stress_tensor_spin = Fraction(2, 1)
    assert_equal("stress-tensor light-transform Delta", 1 - stress_tensor_spin, Fraction(-1))
    assert_equal("stress-tensor light-transform spin", 1 - spacetime_dimension, Fraction(-3))


def main() -> None:
    check_conformal_killing_brackets()
    check_charge_sign_conversion()
    check_radial_real_form_conversion()
    check_light_transform_weight_map()
    print("All conformal light-transform algebra checks passed.")


if __name__ == "__main__":
    main()
