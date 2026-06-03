#!/usr/bin/env python3
"""Scalar conformal blocks in the monograph conventions.

The production rule in this file is deliberately dimension-sensitive:

* in D=2 and D=4, use the Dolan--Osborn hypergeometric closed forms for global
  scalar blocks;
* in D=3, or more generally for D>2 when no special closed form is selected,
  use the Dolan--Osborn/Hogervorst--Rychkov Casimir recursion for the
  z-series coefficients

    G_{Delta,l}(s,xi) = sum_{n,j} A_{n,j} P_{Delta+n,j}(s,xi),

  where P_{E,j}=s^E j!/(2 nu)_j C_j^nu(xi), nu=D/2-1.

The two-dimensional Virasoro conformal block is a different object from the
global D=2 block below.  It depends on the central charge and the external and
internal Virasoro weights, and it should be handled by a separate Zamolodchikov
recursion companion rather than being folded into this global-block file.

Production bootstrap runs should still interoperate with established tools
such as PyCFTBoot/SDPB or specialized 3D block packages.  This file is a small
transparent convention layer: it makes the recursion, normalization, and
crossing kernels auditable inside the monograph repository.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import mpmath as mp


mp.mp.dps = 50


@dataclass(frozen=True)
class ScalarBlockLabel:
    """A symmetric-traceless scalar-block exchange label."""

    delta: mp.mpf
    spin: int

    def __post_init__(self) -> None:
        if self.spin < 0:
            raise ValueError("spin must be nonnegative")


def _as_mpf(value: float | int | str | mp.mpf) -> mp.mpf:
    return value if isinstance(value, mp.mpf) else mp.mpf(value)


def k_beta(beta: float | int | str | mp.mpf, z: complex | mp.mpc) -> mp.mpc:
    """Return k_beta(z)=z^(beta/2) 2F1(beta/2,beta/2;beta;z)."""

    beta = _as_mpf(beta)
    if beta == 0 or (beta < 0 and beta == int(beta)):
        raise ValueError("k_beta is singular at nonpositive integer beta")
    z = mp.mpc(z)
    half_beta = beta / 2
    return z**half_beta * mp.hyp2f1(half_beta, half_beta, beta, z)


def pochhammer(a: float | int | str | mp.mpf, n: int) -> mp.mpf:
    if n < 0:
        raise ValueError("Pochhammer length must be nonnegative")
    out = mp.mpf(1)
    a = _as_mpf(a)
    for k in range(n):
        out *= a + k
    return out


def gegenbauer_or_harmonic(spin: int, dimension: float | int | str | mp.mpf, x: complex | mp.mpc) -> mp.mpc:
    """Return the angular polynomial used in the OPE-leading block term.

    For D>2 this is C_spin^lambda(x), lambda=D/2-1.  For D=2 the monograph
    uses the harmonic limiting normalization cos(spin*arccos(x)).
    """

    if spin < 0:
        raise ValueError("spin must be nonnegative")
    dimension = _as_mpf(dimension)
    x = mp.mpc(x)
    lam = dimension / 2 - 1
    if abs(lam) < mp.mpf("1e-40"):
        return mp.cos(spin * mp.acos(x))
    if spin == 0:
        return mp.mpc(1)
    if spin == 1:
        return 2 * lam * x
    c_prev = mp.mpc(1)
    c_curr = 2 * lam * x
    for n in range(2, spin + 1):
        c_next = (
            2 * (n + lam - 1) * x * c_curr
            - (n + 2 * lam - 2) * c_prev
        ) / n
        c_prev, c_curr = c_curr, c_next
    return c_curr


def leading_radial_block(
    label: ScalarBlockLabel,
    dimension: float | int | str | mp.mpf,
    r: float | int | str | mp.mpf,
    theta: float | int | str | mp.mpf,
) -> mp.mpc:
    """Return r^Delta C_spin^(D/2-1)(cos theta), with the D=2 harmonic limit."""

    r = _as_mpf(r)
    theta = _as_mpf(theta)
    return r**label.delta * gegenbauer_or_harmonic(label.spin, dimension, mp.cos(theta))


def casimir_eigenvalue(
    dimension: float | int | str | mp.mpf,
    energy: float | int | str | mp.mpf,
    spin: int,
) -> mp.mpf:
    """Return C_{E,j}=E(E-D)+j(j+D-2)."""

    dimension = _as_mpf(dimension)
    energy = _as_mpf(energy)
    return energy * (energy - dimension) + spin * (spin + dimension - 2)


def gamma_plus(energy: mp.mpf, spin: int, nu: mp.mpf) -> mp.mpf:
    return (energy + spin) ** 2 * (spin + 2 * nu) / (2 * (spin + nu))


def gamma_minus(energy: mp.mpf, spin: int, nu: mp.mpf) -> mp.mpf:
    if spin < 0:
        return mp.mpf(0)
    return (energy - spin - 2 * nu) ** 2 * spin / (2 * (spin + nu))


def allowed_spins(primary_spin: int, level: int) -> list[int]:
    """Return j=ell+n, ell+n-2, ..., down to the nonnegative endpoint."""

    top = primary_spin + level
    return list(range(top, -1, -2))


def z_series_coefficients(
    label: ScalarBlockLabel,
    dimension: float | int | str | mp.mpf,
    max_level: int,
) -> dict[tuple[int, int], mp.mpf]:
    """Compute A_{n,j} by the Casimir recursion in the z radial frame.

    This is the recursion displayed in Hogervorst--Rychkov for identical
    external scalars.  The normalization is A_{0,ell}=1.
    """

    if max_level < 0:
        raise ValueError("max_level must be nonnegative")
    dimension = _as_mpf(dimension)
    nu = dimension / 2 - 1
    if nu <= 0:
        raise ValueError("the Gegenbauer z-series recursion implemented here requires D>2")

    coeffs: dict[tuple[int, int], mp.mpf] = {(0, label.spin): mp.mpf(1)}
    c_primary = casimir_eigenvalue(dimension, label.delta, label.spin)

    for level in range(1, max_level + 1):
        energy = label.delta + level
        previous_energy = label.delta + level - 1
        for spin in allowed_spins(label.spin, level):
            numerator = mp.mpf(0)
            if spin - 1 >= 0:
                numerator += gamma_plus(previous_energy, spin - 1, nu) * coeffs.get(
                    (level - 1, spin - 1), mp.mpf(0)
                )
            numerator += gamma_minus(previous_energy, spin + 1, nu) * coeffs.get(
                (level - 1, spin + 1), mp.mpf(0)
            )
            if numerator == 0:
                continue
            denominator = casimir_eigenvalue(dimension, energy, spin) - c_primary
            if abs(denominator) < mp.mpf("1e-40"):
                raise ZeroDivisionError("Casimir recursion hit a shortening/degeneracy pole")
            coeffs[(level, spin)] = numerator / denominator
    return coeffs


def basis_p(
    dimension: float | int | str | mp.mpf,
    energy: float | int | str | mp.mpf,
    spin: int,
    s: float | int | str | mp.mpf,
    xi: complex | mp.mpc,
) -> mp.mpc:
    """Return P_{E,j}(s,xi)=s^E j!/(2nu)_j C_j^nu(xi)."""

    dimension = _as_mpf(dimension)
    energy = _as_mpf(energy)
    s = _as_mpf(s)
    nu = dimension / 2 - 1
    if spin == 0:
        normalization = mp.mpf(1)
    else:
        normalization = mp.factorial(spin) / pochhammer(2 * nu, spin)
    return s**energy * normalization * gegenbauer_or_harmonic(spin, dimension, xi)


def scalar_block_z_series(
    label: ScalarBlockLabel,
    dimension: float | int | str | mp.mpf,
    s: float | int | str | mp.mpf,
    theta: float | int | str | mp.mpf,
    max_level: int = 8,
) -> mp.mpc:
    """Evaluate the recursive z-series through `max_level`."""

    dimension = _as_mpf(dimension)
    s = _as_mpf(s)
    theta = _as_mpf(theta)
    xi = mp.cos(theta)
    coeffs = z_series_coefficients(label, dimension, max_level)
    total = mp.mpc(0)
    for (level, spin), coeff in coeffs.items():
        total += coeff * basis_p(dimension, label.delta + level, spin, s, xi)
    # The recursion is simplest in the HR-normalized basis
    # P_{E,j}=s^E j!/(2nu)_j C_j^nu.  The monograph block convention has
    # leading term s^Delta C_l^nu, so we undo the basis normalization of the
    # primary term at the end.
    primary_normalization = pochhammer(2 * (dimension / 2 - 1), label.spin) / mp.factorial(label.spin)
    return primary_normalization * total


def scalar_block_d2(label: ScalarBlockLabel, z: complex | mp.mpc, zbar: complex | mp.mpc) -> mp.mpc:
    """Return the radial-normalized global scalar block in D=2.

    The half-symmetrized normalization makes the leading radial behavior
    r^Delta cos(spin*theta), matching the D=2 harmonic convention in the text.
    """

    z = mp.mpc(z)
    zbar = mp.mpc(zbar)
    beta_plus = label.delta + label.spin
    beta_minus = label.delta - label.spin
    return mp.mpf("0.5") * (
        k_beta(beta_plus, z) * k_beta(beta_minus, zbar)
        + k_beta(beta_plus, zbar) * k_beta(beta_minus, z)
    )


def scalar_block_d4(label: ScalarBlockLabel, z: complex | mp.mpc, zbar: complex | mp.mpc) -> mp.mpc:
    """Return the OPE-normalized Dolan-Osborn scalar block in D=4.

    This is the generic long-multiplet expression.  Conserved-current or
    other short-multiplet limits require taking a limit before evaluation.
    """

    z = mp.mpc(z)
    zbar = mp.mpc(zbar)
    if abs(z - zbar) < mp.mpf("1e-40"):
        raise ValueError("the D=4 closed form is singular on z=zbar; use a limit")
    beta_plus = label.delta + label.spin
    beta_minus = label.delta - label.spin - 2
    return (z * zbar / (z - zbar)) * (
        k_beta(beta_plus, z) * k_beta(beta_minus, zbar)
        - k_beta(beta_plus, zbar) * k_beta(beta_minus, z)
    )


def scalar_block_closed_form(
    dimension: int,
    label: ScalarBlockLabel,
    z: complex | mp.mpc,
    zbar: complex | mp.mpc,
) -> mp.mpc:
    """Dispatch to the closed-form scalar block implemented in this file."""

    if dimension == 2:
        return scalar_block_d2(label, z, zbar)
    if dimension == 4:
        return scalar_block_d4(label, z, zbar)
    raise NotImplementedError("closed-form scalar blocks are implemented here for D=2 and D=4")


def scalar_block_auto(
    dimension: int,
    label: ScalarBlockLabel,
    z: complex | mp.mpc,
    zbar: complex | mp.mpc,
    max_level: int = 8,
) -> mp.mpc:
    """Evaluate the global scalar block by the preferred method for `dimension`.

    The automatic choice follows the chapter convention checks: hypergeometric
    closed forms in D=2 and D=4, and the Casimir z-series recursion otherwise.
    The recursive branch assumes a Euclidean radial pair, so zbar must be the
    conjugate of z up to numerical tolerance.
    """

    if dimension in (2, 4):
        return scalar_block_closed_form(dimension, label, z, zbar)
    if dimension <= 2:
        raise ValueError("the recursive global-block evaluator requires D>2")
    z = mp.mpc(z)
    zbar = mp.mpc(zbar)
    if abs(zbar - mp.conj(z)) > mp.mpf("1e-30"):
        raise ValueError("recursive z-series evaluation expects a Euclidean conjugate pair zbar=conj(z)")
    return scalar_block_z_series(label, dimension, abs(z), mp.arg(z), max_level=max_level)


def f_kernel(
    sign: int,
    delta_j: float | int | str | mp.mpf,
    delta_k: float | int | str | mp.mpf,
    block_uv: complex | mp.mpc,
    block_vu: complex | mp.mpc,
    u: complex | mp.mpc,
    v: complex | mp.mpc,
) -> mp.mpc:
    """Return the F_+ or F_- crossing combination from Chapter 9."""

    if sign not in (-1, 1):
        raise ValueError("sign must be +1 or -1")
    exponent = (_as_mpf(delta_j) + _as_mpf(delta_k)) / 2
    return mp.mpc(v) ** exponent * mp.mpc(block_uv) + sign * mp.mpc(u) ** exponent * mp.mpc(block_vu)


def cross_ratios_from_z(z: complex | mp.mpc, zbar: complex | mp.mpc) -> tuple[mp.mpc, mp.mpc]:
    """Return u=z zbar and v=(1-z)(1-zbar)."""

    z = mp.mpc(z)
    zbar = mp.mpc(zbar)
    return z * zbar, (1 - z) * (1 - zbar)


def point_from_radial(r: float | int | str | mp.mpf, theta: float | int | str | mp.mpf) -> tuple[mp.mpc, mp.mpc]:
    """Return the Euclidean conjugate pair z=r exp(i theta), zbar=r exp(-i theta)."""

    r = _as_mpf(r)
    theta = _as_mpf(theta)
    z = r * mp.e ** (1j * theta)
    return z, mp.conj(z)


def _assert_close(name: str, got: complex | mp.mpc, expected: complex | mp.mpc, tol: str = "1e-8") -> None:
    got_m = mp.mpc(got)
    expected_m = mp.mpc(expected)
    tolerance = mp.mpf(tol)
    for label, value in (
        ("got", got_m),
        ("expected", expected_m),
    ):
        if not (mp.isfinite(mp.re(value)) and mp.isfinite(mp.im(value))):
            raise AssertionError(f"{name} failed: {label} is nonfinite: {value!r}")
    if tolerance < 0 or not mp.isfinite(tolerance):
        raise AssertionError(f"{name} failed: nonfinite or negative tolerance {tol!r}")
    error = abs(got_m - expected_m)
    if not mp.isfinite(error):
        raise AssertionError(f"{name} failed: nonfinite error {error!r}")
    if error > tolerance:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_k_beta_leading() -> None:
    z = mp.mpf("1e-8")
    beta = mp.mpf("7.3")
    _assert_close("k_beta leading term", k_beta(beta, z) / (z ** (beta / 2)), 1, "1e-7")


def check_d2_leading_normalization() -> None:
    label = ScalarBlockLabel(delta=mp.mpf("4.5"), spin=3)
    r = mp.mpf("1e-6")
    theta = mp.mpf("0.71")
    z, zbar = point_from_radial(r, theta)
    got = scalar_block_d2(label, z, zbar) / (r**label.delta)
    expected = mp.cos(label.spin * theta)
    _assert_close("D=2 leading harmonic normalization", got, expected, "1e-5")


def check_d4_leading_normalization() -> None:
    label = ScalarBlockLabel(delta=mp.mpf("5.25"), spin=2)
    r = mp.mpf("1e-6")
    theta = mp.mpf("0.83")
    z, zbar = point_from_radial(r, theta)
    got = scalar_block_d4(label, z, zbar) / (r**label.delta)
    expected = gegenbauer_or_harmonic(label.spin, 4, mp.cos(theta))
    _assert_close("D=4 leading Gegenbauer normalization", got, expected, "1e-5")


def check_recursive_leading_normalization() -> None:
    label = ScalarBlockLabel(delta=mp.mpf("3.7"), spin=3)
    s = mp.mpf("1e-6")
    theta = mp.mpf("0.54")
    got = scalar_block_z_series(label, 3, s, theta, max_level=2) / (s**label.delta)
    expected = gegenbauer_or_harmonic(label.spin, 3, mp.cos(theta))
    _assert_close("recursive D=3 leading normalization", got, expected, "2e-5")


def check_recursive_d4_against_closed_form() -> None:
    label = ScalarBlockLabel(delta=mp.mpf("5.25"), spin=2)
    s = mp.mpf("0.035")
    theta = mp.mpf("0.73")
    z, zbar = point_from_radial(s, theta)
    recursive = scalar_block_z_series(label, 4, s, theta, max_level=12)
    closed = scalar_block_d4(label, z, zbar)
    _assert_close("recursive D=4 block against closed form", recursive, closed, "2e-10")


def check_auto_dispatch() -> None:
    label = ScalarBlockLabel(delta=mp.mpf("5.25"), spin=2)
    z, zbar = point_from_radial(mp.mpf("0.041"), mp.mpf("0.69"))
    _assert_close(
        "automatic D=4 block dispatch",
        scalar_block_auto(4, label, z, zbar, max_level=2),
        scalar_block_d4(label, z, zbar),
        "1e-40",
    )
    recursive = scalar_block_z_series(label, 3, abs(z), mp.arg(z), max_level=5)
    _assert_close(
        "automatic D=3 recursive dispatch",
        scalar_block_auto(3, label, z, zbar, max_level=5),
        recursive,
        "1e-40",
    )


def check_gegenbauer_specializations() -> None:
    x = mp.mpf("0.37")
    # D=3 gives Legendre polynomials.
    _assert_close("D=3 C_2^(1/2)", gegenbauer_or_harmonic(2, 3, x), (3 * x**2 - 1) / 2)
    # D=4 gives C_l^1(cos theta)=sin((l+1)theta)/sin(theta).
    theta = mp.mpf("0.62")
    for spin in range(5):
        got = gegenbauer_or_harmonic(spin, 4, mp.cos(theta))
        expected = mp.sin((spin + 1) * theta) / mp.sin(theta)
        _assert_close(f"D=4 Gegenbauer spin {spin}", got, expected, "1e-40")


def check_block_symmetry_and_kernel() -> None:
    label = ScalarBlockLabel(delta=mp.mpf("6.1"), spin=2)
    z, zbar = point_from_radial(mp.mpf("0.09"), mp.mpf("0.7"))
    g_uv = scalar_block_d4(label, z, zbar)
    g_swapped = scalar_block_d4(label, zbar, z)
    _assert_close("D=4 block z-zbar symmetry", g_uv, g_swapped, "1e-40")

    u, v = cross_ratios_from_z(z, zbar)
    f_plus = f_kernel(1, 1, 1, g_uv, g_swapped, u, v)
    f_minus = f_kernel(-1, 1, 1, g_uv, g_swapped, u, v)
    _assert_close("F+ equal-block reduction", f_plus, (u + v) * g_uv, "1e-40")
    _assert_close("F- equal-block reduction", f_minus, (v - u) * g_uv, "1e-40")


def run_checks() -> None:
    check_k_beta_leading()
    check_d2_leading_normalization()
    check_d4_leading_normalization()
    check_recursive_leading_normalization()
    check_recursive_d4_against_closed_form()
    check_auto_dispatch()
    check_gegenbauer_specializations()
    check_block_symmetry_and_kernel()
    print("All conformal-block companion checks passed.")


def parse_complex(value: str) -> mp.mpc:
    return mp.mpc(value.replace("i", "j"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run built-in normalization checks")
    parser.add_argument("--evaluate", action="store_true", help="evaluate a block instead of running checks")
    parser.add_argument("--dimension", type=int, default=4, help="spacetime dimension")
    parser.add_argument("--delta", default="5.25", help="exchanged scaling dimension")
    parser.add_argument("--spin", type=int, default=2, help="exchanged spin")
    parser.add_argument("--z", default=None, help="complex z, e.g. 0.1+0.03j")
    parser.add_argument("--zbar", default=None, help="complex zbar, e.g. 0.1-0.03j")
    parser.add_argument("--r", default="0.08", help="radial coordinate used when z,zbar are omitted")
    parser.add_argument("--theta", default="0.6", help="angle used when z,zbar are omitted")
    parser.add_argument("--max-level", type=int, default=8, help="maximum recursion level for D>2 z-series")
    parser.add_argument("--leading", action="store_true", help="print only the universal leading radial term")
    parser.add_argument(
        "--method",
        choices=("auto", "closed-form", "z-recursion"),
        default="auto",
        help="evaluation method: auto uses D=2,4 closed forms and recursion otherwise",
    )
    parser.add_argument(
        "--closed-form",
        action="store_true",
        help="deprecated alias for --method closed-form",
    )
    args = parser.parse_args()

    if args.check or not args.evaluate:
        run_checks()
        return

    label = ScalarBlockLabel(delta=_as_mpf(args.delta), spin=args.spin)
    if args.z is None or args.zbar is None:
        z, zbar = point_from_radial(_as_mpf(args.r), _as_mpf(args.theta))
    else:
        z, zbar = parse_complex(args.z), parse_complex(args.zbar)

    if args.leading:
        value = leading_radial_block(label, args.dimension, _as_mpf(args.r), _as_mpf(args.theta))
    elif args.closed_form or args.method == "closed-form":
        value = scalar_block_closed_form(args.dimension, label, z, zbar)
    elif args.method == "z-recursion":
        value = scalar_block_z_series(label, args.dimension, abs(z), mp.arg(z), max_level=args.max_level)
    else:
        value = scalar_block_auto(args.dimension, label, z, zbar, max_level=args.max_level)
    print(mp.nstr(value, 30))


if __name__ == "__main__":
    main()
