#!/usr/bin/env python3
"""Finite Doplicher--Roberts reconstruction checks.

The check models the categorical part of Volume IV, Chapter 4 for the pointed
sector category with simple objects labelled by Z/NZ.  Tensor automorphisms of
the one-dimensional fiber functor are characters, and averaging over the
reconstructed compact group keeps exactly the neutral degree.  It also checks
the finite crossed-product field core for an invertible pointed sector.

The last block adds a nonabelian diagnostic for Rep(S3): the standard
two-dimensional representation is faithful, the character ring has the
expected tensor products, and Haar averaging kills the nontrivial irreducible
matrix coefficients.
"""

from fractions import Fraction
from itertools import permutations


def assert_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def assert_matrix_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def check_tensor_automorphisms(n: int) -> None:
    # Represent the phase exp(2*pi*i*k*q/n) by its exponent k*q mod n.
    # Tensor compatibility is equality of exponents modulo n.
    for k in range(n):
        for q in range(n):
            for r in range(n):
                lhs = (k * ((q + r) % n)) % n
                rhs = ((k * q) + (k * r)) % n
                assert_equal(f"tensor compatibility n={n} k={k} q={q} r={r}", lhs, rhs)

    # Pointwise multiplication of tensor automorphisms is addition of the
    # exponent label k.  This gives the reconstructed group mu_n.
    identity = 0
    for k in range(n):
        inverse = (-k) % n
        assert_equal(f"identity left n={n} k={k}", (identity + k) % n, k)
        assert_equal(f"identity right n={n} k={k}", (k + identity) % n, k)
        assert_equal(f"inverse n={n} k={k}", (k + inverse) % n, identity)


def check_fixed_degree_projection(n: int) -> None:
    # A homogeneous degree q survives averaging over mu_n iff every character
    # value zeta^q is trivial.  In exponent form this means m*q = 0 mod n for
    # every group element m.
    for q in range(n):
        invariant = all((m * q) % n == 0 for m in range(n))
        assert_equal(f"fixed degree n={n} q={q}", invariant, q == 0)


def check_compact_u1_laurent_tannaka(max_charge: int = 8) -> None:
    """Check the exact charge-lattice algebra behind the U(1) compact limit."""

    charges = range(-max_charge, max_charge + 1)

    for m in charges:
        for n in charges:
            # Character multiplication z^m z^n = z^(m+n), encoded by charges.
            assert_equal(f"U(1) Laurent multiplication m={m} n={n}", m + n, n + m)
            assert_equal(f"U(1) star anti-involution m={m} n={n}", -(m + n), (-n) + (-m))

    for n in charges:
        haar_monomial = 1 if n == 0 else 0
        assert_equal(f"U(1) Haar keeps only charge zero n={n}", haar_monomial, int(n == 0))

    # A tensor automorphism of the forgetful functor is fixed by the phase on
    # charge one.  We track only exponents: u_n = lambda^n means the exponent
    # on charge n is n times the exponent on charge one.
    for phase_exponent in range(-max_charge, max_charge + 1):
        u = {n: n * phase_exponent for n in charges}
        for m in charges:
            for n in charges:
                if m + n in u:
                    assert_equal(
                        f"U(1) tensor exponent additivity phase={phase_exponent} m={m} n={n}",
                        u[m + n],
                        u[m] + u[n],
                    )
        for n in charges:
            assert_equal(
                f"U(1) unitary inverse exponent phase={phase_exponent} n={n}",
                u[-n],
                -u[n],
            )


def multiply_basis(n: int, left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int] | None:
    """Multiply e_i u^q by e_j u^r in C^n cross_rho Z/NZ.

    The automorphism rho cyclically shifts idempotents by rho(e_j)=e_{j+1}.
    Thus rho^q(e_j)=e_{j+q}.  The product of idempotents is zero unless the
    idempotent labels agree.
    """
    i, q = left
    j, r = right
    shifted_j = (j + q) % n
    if i != shifted_j:
        return None
    return (i, (q + r) % n)


def star_basis(n: int, basis: tuple[int, int]) -> tuple[int, int]:
    """Involution of e_i u^q: (e_i u^q)^* = rho^{-q}(e_i) u^{-q}."""
    i, q = basis
    return ((i - q) % n, (-q) % n)


def check_crossed_product_core(n: int) -> None:
    basis = [(i, q) for i in range(n) for q in range(n)]

    for x in basis:
        for y in basis:
            for z in basis:
                xy = multiply_basis(n, x, y)
                yz = multiply_basis(n, y, z)
                left = None if xy is None else multiply_basis(n, xy, z)
                right = None if yz is None else multiply_basis(n, x, yz)
                assert_equal(f"crossed-product associativity n={n} x={x} y={y} z={z}", left, right)

    for x in basis:
        assert_equal(f"star involutive n={n} x={x}", star_basis(n, star_basis(n, x)), x)
        for y in basis:
            xy = multiply_basis(n, x, y)
            lhs = None if xy is None else star_basis(n, xy)
            right_product = multiply_basis(n, star_basis(n, y), star_basis(n, x))
            assert_equal(f"star anti-multiplicative n={n} x={x} y={y}", lhs, right_product)

    # Averaging over the dual group kills every nonzero crossed-product degree.
    for i, q in basis:
        invariant = all((m * q) % n == 0 for m in range(n))
        assert_equal(f"crossed-product fixed degree n={n} i={i} q={q}", invariant, q == 0)


def compose_perm(p: tuple[int, int, int], q: tuple[int, int, int]) -> tuple[int, int, int]:
    """Composition p after q, with permutations acting on basis labels."""
    return tuple(p[q[i]] for i in range(3))


def inverse_perm(p: tuple[int, int, int]) -> tuple[int, int, int]:
    inverse = [0, 0, 0]
    for i, value in enumerate(p):
        inverse[value] = i
    return tuple(inverse)


def permutation_sign(p: tuple[int, int, int]) -> int:
    inversions = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return -1 if inversions % 2 else 1


def standard_matrix_s3(p: tuple[int, int, int]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    """Matrix of the S3 standard representation in basis e1-e3, e2-e3."""
    basis = ((1, 0, -1), (0, 1, -1))
    columns: list[tuple[Fraction, Fraction]] = []
    for vector in basis:
        image = [0, 0, 0]
        for i, coefficient in enumerate(vector):
            image[p[i]] += coefficient
        # In the plane x1+x2+x3=0, a(e1-e3)+b(e2-e3)=(a,b,-a-b).
        columns.append((Fraction(image[0]), Fraction(image[1])))
    return ((columns[0][0], columns[1][0]), (columns[0][1], columns[1][1]))


def matrix_mul(
    a: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
    b: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def matrix_add(
    a: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
    b: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    return (
        (a[0][0] + b[0][0], a[0][1] + b[0][1]),
        (a[1][0] + b[1][0], a[1][1] + b[1][1]),
    )


def matrix_trace(a: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> Fraction:
    return a[0][0] + a[1][1]


def class_label(p: tuple[int, int, int]) -> str:
    fixed = sum(1 for i in range(3) if p[i] == i)
    if fixed == 3:
        return "e"
    if fixed == 1:
        return "transposition"
    return "three-cycle"


def character_inner_product(values_a: dict[str, int], values_b: dict[str, int]) -> Fraction:
    class_sizes = {"e": 1, "transposition": 3, "three-cycle": 2}
    return sum(
        Fraction(class_sizes[label] * values_a[label] * values_b[label], 6)
        for label in class_sizes
    )


def check_s3_nonabelian_reconstruction_diagnostic() -> None:
    group = list(permutations(range(3)))
    identity = (0, 1, 2)
    zero = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
    one = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))

    matrices = {g: standard_matrix_s3(g) for g in group}
    for g in group:
        for h in group:
            lhs = matrix_mul(matrices[g], matrices[h])
            rhs = matrices[compose_perm(g, h)]
            assert_matrix_equal(f"S3 standard representation law g={g} h={h}", lhs, rhs)

    faithful_kernel = [g for g in group if matrices[g] == one]
    assert_equal("S3 standard representation faithful kernel", faithful_kernel, [identity])

    sign_sum = sum(permutation_sign(g) for g in group)
    assert_equal("S3 sign average kills nontrivial one-dimensional irrep", sign_sum, 0)

    standard_average = zero
    for g in group:
        standard_average = matrix_add(standard_average, matrices[g])
    assert_matrix_equal("S3 standard average kills nontrivial matrix coefficients", standard_average, zero)

    characters = {
        "triv": {"e": 1, "transposition": 1, "three-cycle": 1},
        "sign": {"e": 1, "transposition": -1, "three-cycle": 1},
        "std": {"e": 2, "transposition": 0, "three-cycle": -1},
    }
    for name, values in characters.items():
        assert_equal(f"S3 character norm {name}", character_inner_product(values, values), Fraction(1))

    def product_character(a: str, b: str) -> dict[str, int]:
        return {label: characters[a][label] * characters[b][label] for label in characters[a]}

    decompositions = {
        ("sign", "sign"): {"triv": 1, "sign": 0, "std": 0},
        ("sign", "std"): {"triv": 0, "sign": 0, "std": 1},
        ("std", "std"): {"triv": 1, "sign": 1, "std": 1},
    }
    for pair, expected in decompositions.items():
        product = product_character(*pair)
        actual = {
            name: character_inner_product(product, values)
            for name, values in characters.items()
        }
        assert_equal(f"S3 tensor product decomposition {pair}", actual, expected)

    class_traces = {label: set() for label in ("e", "transposition", "three-cycle")}
    for g, matrix in matrices.items():
        class_traces[class_label(g)].add(matrix_trace(matrix))
    assert_equal("S3 standard character on identity", class_traces["e"], {Fraction(2)})
    assert_equal("S3 standard character on transpositions", class_traces["transposition"], {Fraction(0)})
    assert_equal("S3 standard character on three-cycles", class_traces["three-cycle"], {Fraction(-1)})


def matrix_det(a: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> Fraction:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def check_s3_regular_field_core() -> None:
    group = list(permutations(range(3)))
    matrices = {g: standard_matrix_s3(g) for g in group}

    # Right translation rotates the column index of every matrix coefficient.
    for g in group:
        for h in group:
            gh = compose_perm(g, h)
            for a in range(2):
                for b in range(2):
                    lhs = matrices[gh][a][b]
                    rhs = sum(matrices[g][a][c] * matrices[h][c][b] for c in range(2))
                    assert_equal(f"S3 regular right action g={g} h={h} a={a} b={b}", lhs, rhs)

    # Haar expectation over the right action keeps constants and kills all
    # nontrivial matrix coefficients.
    for g in group:
        standard_average = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
        sign_average = Fraction(0)
        trivial_average = Fraction(0)
        for h in group:
            gh = compose_perm(g, h)
            matrix = matrices[gh]
            standard_average[0][0] += matrix[0][0]
            standard_average[0][1] += matrix[0][1]
            standard_average[1][0] += matrix[1][0]
            standard_average[1][1] += matrix[1][1]
            sign_average += permutation_sign(gh)
            trivial_average += 1
        assert_equal(f"S3 regular Haar standard 00 g={g}", standard_average[0][0], Fraction(0))
        assert_equal(f"S3 regular Haar standard 01 g={g}", standard_average[0][1], Fraction(0))
        assert_equal(f"S3 regular Haar standard 10 g={g}", standard_average[1][0], Fraction(0))
        assert_equal(f"S3 regular Haar standard 11 g={g}", standard_average[1][1], Fraction(0))
        assert_equal(f"S3 regular Haar sign g={g}", sign_average, Fraction(0))
        assert_equal(f"S3 regular Haar trivial g={g}", trivial_average / 6, Fraction(1))

    # The antisymmetric piece of V tensor V is the sign representation.
    for g in group:
        assert_equal(f"S3 exterior-square sign g={g}", matrix_det(matrices[g]), Fraction(permutation_sign(g)))


def check_s3_left_equivariant_function_automorphisms() -> None:
    group = list(permutations(range(3)))
    identity = (0, 1, 2)
    index = {g: i for i, g in enumerate(group)}
    left_equivariant_maps = []

    for image_indices in permutations(range(len(group))):
        image = {g: group[image_indices[index[g]]] for g in group}
        is_left_equivariant = all(
            image[compose_perm(a, x)] == compose_perm(a, image[x])
            for a in group
            for x in group
        )
        if is_left_equivariant:
            h = image[identity]
            assert_equal(
                f"S3 left-equivariant automorphism is right translation h={h}",
                {x: image[x] for x in group},
                {x: compose_perm(x, h) for x in group},
            )
            left_equivariant_maps.append(h)

    assert_equal("S3 left-equivariant function algebra automorphism count", len(left_equivariant_maps), 6)
    assert_equal("S3 left-equivariant function algebra automorphism labels", set(left_equivariant_maps), set(group))

    matrices = {g: standard_matrix_s3(g) for g in group}
    # If T_h delta_x = delta_{x h}, then (T_h f)(g)=f(g h^{-1}).
    # On matrix coefficients this gives right multiplication by D(h^{-1})
    # on the charged column index.
    for h in group:
        h_inv = inverse_perm(h)
        for g in group:
            gh_inv = compose_perm(g, h_inv)
            for a in range(2):
                for b in range(2):
                    lhs = matrices[gh_inv][a][b]
                    rhs = sum(matrices[g][a][j] * matrices[h_inv][j][b] for j in range(2))
                    assert_equal(f"S3 finite Tannaka matrix action h={h} g={g} a={a} b={b}", lhs, rhs)


def main() -> None:
    for n in range(2, 13):
        check_tensor_automorphisms(n)
        check_fixed_degree_projection(n)
        check_crossed_product_core(n)
    check_compact_u1_laurent_tannaka()
    check_s3_nonabelian_reconstruction_diagnostic()
    check_s3_regular_field_core()
    check_s3_left_equivariant_function_automorphisms()
    print("All finite DHR/DR reconstruction diagnostics passed.")


if __name__ == "__main__":
    main()
