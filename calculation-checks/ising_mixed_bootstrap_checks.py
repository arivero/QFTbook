#!/usr/bin/env python3
"""Exact checks for the mixed-correlator Ising bootstrap conventions."""

from __future__ import annotations

from fractions import Fraction


Lin = tuple[Fraction, Fraction]  # coefficients of (Delta_sigma, Delta_epsilon)
DistVec = dict[str, Lin]
Symbol = tuple[str, str, str]  # lambda monomial, F sign, channel label
Expr = dict[Symbol, Fraction]

ZERO_LIN: Lin = (Fraction(0), Fraction(0))
DELTA_SIGMA: Lin = (Fraction(1), Fraction(0))
DELTA_EPSILON: Lin = (Fraction(0), Fraction(1))
DISTANCES = ("12", "13", "14", "23", "24", "34")


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def lin_add(a: Lin, b: Lin) -> Lin:
    return (a[0] + b[0], a[1] + b[1])


def lin_sub(a: Lin, b: Lin) -> Lin:
    return (a[0] - b[0], a[1] - b[1])


def lin_scale(q: Fraction | int, a: Lin) -> Lin:
    q = Fraction(q)
    return (q * a[0], q * a[1])


def lin_half(a: Lin) -> Lin:
    return lin_scale(Fraction(1, 2), a)


def dist_zero() -> DistVec:
    return {key: ZERO_LIN for key in DISTANCES}


def dist_add(a: DistVec, b: DistVec) -> DistVec:
    return {key: lin_add(a[key], b[key]) for key in DISTANCES}


def dist_sub(a: DistVec, b: DistVec) -> DistVec:
    return {key: lin_sub(a[key], b[key]) for key in DISTANCES}


def dist_key(i: int, j: int) -> str:
    a, b = sorted((i, j))
    return f"{a}{b}"


def dimension(label: str) -> Lin:
    if label == "s":
        return DELTA_SIGMA
    if label == "e":
        return DELTA_EPSILON
    raise ValueError(f"unknown external label {label!r}")


def prefactor_exponents(labels: tuple[str, str, str, str]) -> DistVec:
    """Return exponents of X_ij = |x_i - x_j|^2 in the chapter prefactor."""

    d1, d2, d3, d4 = (dimension(label) for label in labels)
    out = dist_zero()
    out["12"] = lin_scale(-1, lin_half(lin_add(d1, d2)))
    out["34"] = lin_scale(-1, lin_half(lin_add(d3, d4)))
    out["24"] = lin_half(lin_sub(d1, d2))
    out["14"] = lin_half(lin_add(lin_sub(d2, d1), lin_sub(d3, d4)))
    out["13"] = lin_half(lin_sub(d4, d3))
    return out


def permuted_prefactor_exponents(
    labels: tuple[str, str, str, str], new_to_old: tuple[int, int, int, int]
) -> DistVec:
    """Evaluate the prefactor after a point permutation in old coordinates."""

    new_labels = tuple(labels[old_index - 1] for old_index in new_to_old)
    new_prefactor = prefactor_exponents(new_labels)  # exponents in new labels 1,...,4
    out = dist_zero()
    for key, exponent in new_prefactor.items():
        i, j = int(key[0]), int(key[1])
        old_key = dist_key(new_to_old[i - 1], new_to_old[j - 1])
        out[old_key] = lin_add(out[old_key], exponent)
    return out


def cross_ratio_monomial(u_power: Lin, v_power: Lin) -> DistVec:
    """Return exponents of u^u_power v^v_power in the X_ij variables."""

    out = dist_zero()
    # u = X12 X34/(X13 X24)
    for key, coeff in (("12", 1), ("34", 1), ("13", -1), ("24", -1)):
        out[key] = lin_add(out[key], lin_scale(coeff, u_power))
    # v = X14 X23/(X13 X24)
    for key, coeff in (("14", 1), ("23", 1), ("13", -1), ("24", -1)):
        out[key] = lin_add(out[key], lin_scale(coeff, v_power))
    return out


def check_prefactor_crossing_ratios() -> None:
    swap_24 = (1, 4, 3, 2)
    swap_13 = (3, 2, 1, 4)

    identical = ("s", "s", "s", "s")
    ratio = dist_sub(
        permuted_prefactor_exponents(identical, swap_24),
        prefactor_exponents(identical),
    )
    expected = cross_ratio_monomial(DELTA_SIGMA, lin_scale(-1, DELTA_SIGMA))
    assert_equal("identical scalar 2<->4 prefactor ratio", ratio, expected)

    sigma_sigma_epsilon_epsilon = ("s", "s", "e", "e")
    ratio = dist_sub(
        permuted_prefactor_exponents(sigma_sigma_epsilon_epsilon, swap_13),
        prefactor_exponents(sigma_sigma_epsilon_epsilon),
    )
    expected = cross_ratio_monomial(
        DELTA_SIGMA,
        lin_scale(Fraction(-1, 2), lin_add(DELTA_SIGMA, DELTA_EPSILON)),
    )
    assert_equal("sigma sigma epsilon epsilon 1<->3 prefactor ratio", ratio, expected)

    epsilon_epsilon_sigma_sigma = ("e", "e", "s", "s")
    ratio = dist_sub(
        permuted_prefactor_exponents(epsilon_epsilon_sigma_sigma, swap_13),
        prefactor_exponents(epsilon_epsilon_sigma_sigma),
    )
    expected = cross_ratio_monomial(
        DELTA_EPSILON,
        lin_scale(Fraction(-1, 2), lin_add(DELTA_SIGMA, DELTA_EPSILON)),
    )
    assert_equal("epsilon epsilon sigma sigma 1<->3 prefactor ratio", ratio, expected)

    epsilon_sigma_sigma_epsilon = ("e", "s", "s", "e")
    ratio = dist_sub(
        permuted_prefactor_exponents(epsilon_sigma_sigma_epsilon, swap_13),
        prefactor_exponents(epsilon_sigma_sigma_epsilon),
    )
    expected = cross_ratio_monomial(
        lin_scale(Fraction(1, 2), lin_add(DELTA_SIGMA, DELTA_EPSILON)),
        lin_scale(-1, DELTA_SIGMA),
    )
    assert_equal("epsilon sigma sigma epsilon companion prefactor ratio", ratio, expected)


BlockTerm = tuple[int, int, str]  # u-power of a, v-power of a, block argument
BlockExpr = dict[BlockTerm, int]


def clean_block(expr: BlockExpr) -> BlockExpr:
    return {key: value for key, value in expr.items() if value != 0}


def block_add(a: BlockExpr, b: BlockExpr) -> BlockExpr:
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
    return clean_block(out)


def block_neg(a: BlockExpr) -> BlockExpr:
    return {key: -value for key, value in a.items()}


def block_swap_uv(a: BlockExpr) -> BlockExpr:
    swapped_arg = {"Guv": "Gvu", "Gvu": "Guv"}
    out: BlockExpr = {}
    for (u_power, v_power, arg), value in a.items():
        key = (v_power, u_power, swapped_arg[arg])
        out[key] = out.get(key, 0) + value
    return clean_block(out)


def check_fpm_symmetry() -> None:
    f_plus = {(0, 1, "Guv"): 1, (1, 0, "Gvu"): 1}
    f_minus = {(0, 1, "Guv"): 1, (1, 0, "Gvu"): -1}
    assert_equal("F+ symmetry under u<->v", block_swap_uv(f_plus), f_plus)
    assert_equal("F- antisymmetry under u<->v", block_swap_uv(f_minus), block_neg(f_minus))


def check_spin_exchange_sign() -> None:
    for spin in range(8):
        expected = 1 if spin % 2 == 0 else -1
        assert_equal(f"spin exchange sign ell={spin}", (-1) ** spin, expected)


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def outer(a: Fraction, b: Fraction) -> Matrix:
    return ((a * a, a * b), (a * b, b * b))


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] + b[0][0], a[0][1] + b[0][1]),
        (a[1][0] + b[1][0], a[1][1] + b[1][1]),
    )


def determinant(m: Matrix) -> Fraction:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def quadratic_form(m: Matrix, x: Fraction, y: Fraction) -> Fraction:
    return m[0][0] * x * x + 2 * m[0][1] * x * y + m[1][1] * y * y


def check_even_ope_psd_matrices() -> None:
    samples = [(Fraction(1), Fraction(2)), (Fraction(-3), Fraction(5))]
    matrices = [outer(a, b) for a, b in samples]
    for index, matrix in enumerate(matrices):
        assert_equal(f"rank-one determinant {index}", determinant(matrix), Fraction(0))
        for x, y in samples:
            if quadratic_form(matrix, x, y) < 0:
                raise AssertionError(f"rank-one PSD check {index} failed")

    total = mat_add(matrices[0], matrices[1])
    if total[0][0] < 0 or total[1][1] < 0 or determinant(total) < 0:
        raise AssertionError(f"sum of even-sector outer products is not PSD: {total!r}")
    for x, y in samples:
        if quadratic_form(total, x, y) < 0:
            raise AssertionError("summed even-sector PSD quadratic form failed")


def expr_clean(expr: Expr) -> Expr:
    return {key: value for key, value in expr.items() if value != 0}


def expr_add(a: Expr, b: Expr) -> Expr:
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction(0)) + value
    return expr_clean(out)


def expr_scale(q: Fraction | int, a: Expr) -> Expr:
    return expr_clean({key: Fraction(q) * value for key, value in a.items()})


def f_symbol(sign: str, channel: str, coeff: Fraction | int = 1) -> Expr:
    return {("", sign, channel): Fraction(coeff)}


def attach_monomial(monomial: str, a: Expr) -> Expr:
    return {
        (monomial, sign, channel): coeff
        for (_, sign, channel), coeff in a.items()
    }


def qform(matrix: tuple[tuple[Expr, Expr], tuple[Expr, Expr]]) -> Expr:
    monomial = {(0, 0): "aa", (0, 1): "ab", (1, 0): "ab", (1, 1): "bb"}
    out: Expr = {}
    for i in range(2):
        for j in range(2):
            out = expr_add(out, attach_monomial(monomial[(i, j)], matrix[i][j]))
    return out


def zero_expr() -> Expr:
    return {}


def check_five_vector_packing() -> None:
    zero_matrix = ((zero_expr(), zero_expr()), (zero_expr(), zero_expr()))
    for spin in range(4):
        sign = 1 if spin % 2 == 0 else -1
        v_minus = [
            zero_expr(),
            zero_expr(),
            f_symbol("F-", "se,se"),
            expr_scale(sign, f_symbol("F-", "es,se")),
            expr_scale(-sign, f_symbol("F+", "es,se")),
        ]
        v_plus = [
            ((f_symbol("F-", "ss,ss"), zero_expr()), (zero_expr(), zero_expr())),
            ((zero_expr(), zero_expr()), (zero_expr(), f_symbol("F-", "ee,ee"))),
            zero_matrix,
            (
                (zero_expr(), f_symbol("F-", "ss,ee", Fraction(1, 2))),
                (f_symbol("F-", "ss,ee", Fraction(1, 2)), zero_expr()),
            ),
            (
                (zero_expr(), f_symbol("F+", "ss,ee", Fraction(1, 2))),
                (f_symbol("F+", "ss,ee", Fraction(1, 2)), zero_expr()),
            ),
        ]

        got = [
            expr_add(qform(v_plus[i]), attach_monomial("cc", v_minus[i]))
            for i in range(5)
        ]
        expected = [
            {("aa", "F-", "ss,ss"): Fraction(1)},
            {("bb", "F-", "ee,ee"): Fraction(1)},
            {("cc", "F-", "se,se"): Fraction(1)},
            {
                ("ab", "F-", "ss,ee"): Fraction(1),
                ("cc", "F-", "es,se"): Fraction(sign),
            },
            {
                ("ab", "F+", "ss,ee"): Fraction(1),
                ("cc", "F+", "es,se"): Fraction(-sign),
            },
        ]
        assert_equal(f"five-vector packing ell={spin}", got, expected)


def main() -> None:
    check_prefactor_crossing_ratios()
    check_fpm_symmetry()
    check_spin_exchange_sign()
    check_even_ope_psd_matrices()
    check_five_vector_packing()
    print("All mixed-correlator Ising bootstrap checks passed.")


if __name__ == "__main__":
    main()
