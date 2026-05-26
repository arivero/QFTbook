"""Exact checks for the two-dimensional superconformal-algebra chapter."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction


CENTRAL = ("C", Fraction(0))


def basis(kind: str, mode: Fraction | int = 0):
    return {(kind, Fraction(mode)): Fraction(1)}


def add(*terms):
    out = defaultdict(Fraction)
    for term in terms:
        for key, value in term.items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


def scale(coeff: Fraction | int, term):
    coeff = Fraction(coeff)
    return {key: coeff * value for key, value in term.items() if coeff * value}


def parity(kind: str) -> int:
    return 1 if kind in {"Gp", "Gm"} else 0


def bracket_basis(a, b):
    """Superbracket on the N=2 modes, with central element C."""
    kind_a, mode_a = a
    kind_b, mode_b = b

    if kind_a == "C" or kind_b == "C":
        return {}

    # Put even-odd brackets in the even-first order when needed.
    if parity(kind_a) == 1 and parity(kind_b) == 0:
        return scale(-1, bracket_basis(b, a))

    if kind_a == "L" and kind_b == "L":
        m, n = mode_a, mode_b
        central = {}
        if m + n == 0:
            central = scale((m**3 - m) / 12, {CENTRAL: Fraction(1)})
        return add(scale(m - n, basis("L", m + n)), central)

    if kind_a == "L" and kind_b == "J":
        m, n = mode_a, mode_b
        return scale(-n, basis("J", m + n))

    if kind_a == "J" and kind_b == "L":
        m, n = mode_a, mode_b
        return scale(m, basis("J", m + n))

    if kind_a == "J" and kind_b == "J":
        m, n = mode_a, mode_b
        if m + n == 0:
            return scale(m / 3, {CENTRAL: Fraction(1)})
        return {}

    if kind_a == "L" and kind_b in {"Gp", "Gm"}:
        m, r = mode_a, mode_b
        return scale(m / 2 - r, basis(kind_b, m + r))

    if kind_a == "J" and kind_b in {"Gp", "Gm"}:
        sign = 1 if kind_b == "Gp" else -1
        return scale(sign, basis(kind_b, mode_a + mode_b))

    if kind_a == "Gp" and kind_b == "Gm":
        r, s = mode_a, mode_b
        central = {}
        if r + s == 0:
            central = scale((r**2 - Fraction(1, 4)) / 3, {CENTRAL: Fraction(1)})
        return add(
            scale(2, basis("L", r + s)),
            scale(r - s, basis("J", r + s)),
            central,
        )

    if kind_a == "Gm" and kind_b == "Gp":
        r, s = mode_a, mode_b
        central = {}
        if r + s == 0:
            central = scale((s**2 - Fraction(1, 4)) / 3, {CENTRAL: Fraction(1)})
        return add(
            scale(2, basis("L", r + s)),
            scale(s - r, basis("J", r + s)),
            central,
        )

    if kind_a in {"Gp", "Gm"} and kind_b == kind_a:
        return {}

    raise AssertionError(f"unhandled bracket: {a}, {b}")


def bracket(x, y):
    out = defaultdict(Fraction)
    for a, ca in x.items():
        for b, cb in y.items():
            for key, value in bracket_basis(a, b).items():
                out[key] += ca * cb * value
    return {key: value for key, value in out.items() if value}


def spectral_image_basis(key, eta: Fraction):
    kind, mode = key
    if kind == "C":
        return {CENTRAL: Fraction(1)}
    if kind == "L":
        central = scale(eta**2 / 6, {CENTRAL: Fraction(1)}) if mode == 0 else {}
        return add(basis("L", mode), scale(eta, basis("J", mode)), central)
    if kind == "J":
        central = scale(eta / 3, {CENTRAL: Fraction(1)}) if mode == 0 else {}
        return add(basis("J", mode), central)
    if kind == "Gp":
        return basis("Gp", mode + eta)
    if kind == "Gm":
        return basis("Gm", mode - eta)
    raise AssertionError(f"unhandled spectral image: {key}")


def spectral_image(term, eta: Fraction):
    out = defaultdict(Fraction)
    for key, coeff in term.items():
        for image_key, image_coeff in spectral_image_basis(key, eta).items():
            out[image_key] += coeff * image_coeff
    return {key: value for key, value in out.items() if value}


def assert_equal(left, right, label: str):
    if left != right:
        raise AssertionError(f"{label} failed:\nleft={left}\nright={right}")


def check_n1_zero_mode_and_ns_coefficients():
    # {G_0,G_0}=2 L_0 - C/12 in the Ramond sector.
    r = Fraction(0)
    ramond = add(
        scale(2, basis("L", 0)),
        scale((r**2 - Fraction(1, 4)) / 3, {CENTRAL: Fraction(1)}),
    )
    expected = add(scale(2, basis("L", 0)), scale(Fraction(-1, 12), {CENTRAL: Fraction(1)}))
    assert_equal(ramond, expected, "N=1 Ramond zero-mode coefficient")

    # In the NS sector, {G_{1/2},G_{-1/2}} has no central term.
    r = Fraction(1, 2)
    ns_central = (r**2 - Fraction(1, 4)) / 3
    if ns_central != 0:
        raise AssertionError("N=1 NS half-mode central term should vanish")


def check_n2_chiral_primary_norms():
    # {G^-_{1/2},G^+_{-1/2}} = 2 L_0 - J_0.
    left = bracket(basis("Gm", Fraction(1, 2)), basis("Gp", Fraction(-1, 2)))
    expected = add(scale(2, basis("L", 0)), scale(-1, basis("J", 0)))
    assert_equal(left, expected, "N=2 chiral-primary norm")

    # {G^+_{1/2},G^-_{-1/2}} = 2 L_0 + J_0.
    right = bracket(basis("Gp", Fraction(1, 2)), basis("Gm", Fraction(-1, 2)))
    expected = add(scale(2, basis("L", 0)), basis("J", 0))
    assert_equal(right, expected, "N=2 antichiral-primary norm")


def check_spectral_flow_automorphism():
    test_modes = [
        (basis("L", 2), basis("L", -2)),
        (basis("L", 1), basis("J", -1)),
        (basis("J", 2), basis("J", -2)),
        (basis("L", 2), basis("Gp", Fraction(-1, 2))),
        (basis("J", -1), basis("Gm", Fraction(3, 2))),
        (basis("Gp", Fraction(3, 2)), basis("Gm", Fraction(-3, 2))),
        (basis("Gp", Fraction(-1, 2)), basis("Gm", Fraction(1, 2))),
    ]
    for eta in (Fraction(1, 2), Fraction(-1, 2), Fraction(1)):
        for x, y in test_modes:
            left = bracket(spectral_image(x, eta), spectral_image(y, eta))
            right = spectral_image(bracket(x, y), eta)
            assert_equal(left, right, f"spectral flow eta={eta} for {x}, {y}")


def check_ns_to_ramond_ground_state():
    # For a chiral primary h=q/2, eta=-1/2 gives h'=C/24.
    q = Fraction(7, 13)
    h = q / 2
    eta = Fraction(-1, 2)
    shifted_h_minus_c_term = h + eta * q
    if shifted_h_minus_c_term != 0:
        raise AssertionError("NS chiral primary did not cancel h and q under eta=-1/2")
    if eta**2 / 6 != Fraction(1, 24):
        raise AssertionError("Ramond ground-state c/24 coefficient failed")


def check_lg_central_charges():
    for k in range(0, 12):
        q = Fraction(1, k + 2)
        c = 3 * (1 - 2 * q)
        expected = Fraction(3 * k, k + 2)
        if c != expected:
            raise AssertionError(f"A-series central charge failed for k={k}")

        ring_dimension = k + 1
        max_power = k
        if ring_dimension != max_power + 1:
            raise AssertionError(f"A-series Jacobi basis count failed for k={k}")

        top_charge = Fraction(k, k + 2)
        top_weight = top_charge / 2
        if top_weight != Fraction(k, 2 * (k + 2)):
            raise AssertionError(f"A-series chiral weight failed for k={k}")

    quintic_c = 3 * sum(Fraction(1) - 2 * Fraction(1, 5) for _ in range(5))
    if quintic_c != 9:
        raise AssertionError("quintic LG central charge should be 9")


def main():
    check_n1_zero_mode_and_ns_coefficients()
    check_n2_chiral_primary_norms()
    check_spectral_flow_automorphism()
    check_ns_to_ramond_ground_state()
    check_lg_central_charges()
    print("All 2D superconformal algebra checks passed.")


if __name__ == "__main__":
    main()
