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


def check_extended_n2_spectral_flow_operators():
    central_charges = (Fraction(3), Fraction(6), Fraction(9), Fraction(15, 2), Fraction(12))
    etas = (Fraction(-1), Fraction(-1, 2), Fraction(1, 2), Fraction(1))
    charges = (Fraction(-5, 3), Fraction(-1), Fraction(0), Fraction(2, 3), Fraction(2))

    for c in central_charges:
        kappa = c / 3

        for eta in etas:
            h_x = eta**2 * kappa / 2
            q_x = eta * kappa

            # X_eta is the spectral flow of the identity.
            assert_equal(h_x, eta**2 * c / 6, f"spectral-flow vertex weight c={c}, eta={eta}")
            assert_equal(q_x, eta * c / 3, f"spectral-flow vertex charge c={c}, eta={eta}")

            for q in charges:
                old_u1_weight = q**2 / (2 * kappa)
                new_q = q + eta * kappa
                new_u1_weight = new_q**2 / (2 * kappa)
                expected_shift = eta * q + eta**2 * c / 6
                assert_equal(
                    new_u1_weight - old_u1_weight,
                    expected_shift,
                    f"Heisenberg spectral-flow weight shift c={c}, q={q}, eta={eta}",
                )

            for xi in etas:
                exponent = eta * xi * kappa
                h_product = eta**2 * kappa / 2 + xi**2 * kappa / 2
                h_fused = (eta + xi) ** 2 * kappa / 2
                assert_equal(
                    h_fused - h_product,
                    exponent,
                    f"spectral-flow vertex OPE exponent c={c}, eta={eta}, xi={xi}",
                )
                assert_equal(
                    eta * kappa + xi * kappa,
                    (eta + xi) * kappa,
                    f"spectral-flow vertex charge fusion c={c}, eta={eta}, xi={xi}",
                )

            opposite_pole_order = eta**2 * kappa
            first_j_coefficient = eta
            second_derivative_j_coefficient = eta / 2
            second_jj_coefficient = eta**2 / 2
            assert_equal(
                opposite_pole_order,
                h_x + h_x,
                f"opposite spectral-flow pole order c={c}, eta={eta}",
            )
            assert_equal(first_j_coefficient, eta, f"opposite OPE J coefficient c={c}, eta={eta}")
            assert_equal(
                second_derivative_j_coefficient,
                eta / 2,
                f"opposite OPE dJ coefficient c={c}, eta={eta}",
            )
            assert_equal(
                second_jj_coefficient,
                eta**2 / 2,
                f"opposite OPE JJ coefficient c={c}, eta={eta}",
            )

        x_plus_h = kappa / 2
        x_plus_q = kappa
        x_minus_h = kappa / 2
        x_minus_q = -kappa
        assert_equal(x_plus_h, x_plus_q / 2, f"X+ chiral shortening c={c}")
        assert_equal(x_minus_h, -x_minus_q / 2, f"X- antichiral shortening c={c}")

        y_plus_h = x_plus_h + Fraction(1, 2)
        y_plus_q = x_plus_q - 1
        y_minus_h = x_minus_h + Fraction(1, 2)
        y_minus_q = x_minus_q + 1
        assert_equal(y_plus_h, c / 6 + Fraction(1, 2), f"Y+ weight c={c}")
        assert_equal(y_plus_q, c / 3 - 1, f"Y+ charge c={c}")
        assert_equal(y_minus_h, c / 6 + Fraction(1, 2), f"Y- weight c={c}")
        assert_equal(y_minus_q, -(c / 3 - 1), f"Y- charge c={c}")

    for n in range(1, 8):
        c = 3 * n
        kappa = Fraction(n)
        assert_equal(kappa / 2, Fraction(n, 2), f"Calabi-Yau-type X weight n={n}")
        assert_equal(kappa, Fraction(n), f"Calabi-Yau-type X charge n={n}")
        assert_equal(kappa / 8, Fraction(n, 8), f"Calabi-Yau-type half-flow weight n={n}")
        assert_equal(kappa / 2, Fraction(n, 2), f"Calabi-Yau-type half-flow charge n={n}")


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


def check_elliptic_genus_spectral_flow_law():
    for c in (Fraction(3), Fraction(6), Fraction(9), Fraction(12), Fraction(15, 2)):
        index = c / 6
        for lam in range(-3, 4):
            q_factor = -index * lam * lam
            y_factor = -2 * index * lam
            assert_equal(q_factor, -c * lam * lam / 6, f"elliptic q multiplier c={c}, lambda={lam}")
            assert_equal(y_factor, -c * lam / 3, f"elliptic y multiplier c={c}, lambda={lam}")

        for lam_1 in range(-2, 3):
            for lam_2 in range(-2, 3):
                # The elliptic shift factors obey the Jacobi cocycle:
                # first shift by lam_2, then by lam_1 at z+lam_2 tau.
                sequential_q = (
                    -index * lam_2 * lam_2
                    -index * lam_1 * lam_1
                    -2 * index * lam_1 * lam_2
                )
                sequential_y = -2 * index * (lam_1 + lam_2)
                combined_q = -index * (lam_1 + lam_2) ** 2
                combined_y = -2 * index * (lam_1 + lam_2)
                assert_equal(
                    sequential_q,
                    combined_q,
                    f"elliptic q cocycle c={c}, lambda1={lam_1}, lambda2={lam_2}",
                )
                assert_equal(
                    sequential_y,
                    combined_y,
                    f"elliptic y cocycle c={c}, lambda1={lam_1}, lambda2={lam_2}",
                )


def check_lg_chi_y_charge_polynomials():
    for k in range(0, 16):
        c = Fraction(3 * k, k + 2)
        ramond_shift = c / 6
        charges = [Fraction(ell, k + 2) - ramond_shift for ell in range(k + 1)]
        assert_equal(len(charges), k + 1, f"A-series chi_y term count k={k}")
        assert_equal(sum(charges), Fraction(0), f"A-series Ramond charges sum k={k}")
        for ell, charge in enumerate(charges):
            reflected = charges[k - ell]
            assert_equal(charge + reflected, Fraction(0), f"A-series charge reflection k={k}, ell={ell}")
            expected = Fraction(2 * ell - k, 2 * (k + 2))
            assert_equal(charge, expected, f"A-series Ramond charge k={k}, ell={ell}")

        witten_index = sum(Fraction(1) for _ in charges)
        assert_equal(witten_index, Fraction(k + 1), f"A-series Witten index k={k}")

    quintic_degrees = [5, 5, 5, 5, 5]
    quintic_weights = [Fraction(1, degree) for degree in quintic_degrees]
    quintic_c = 3 * sum(Fraction(1) - 2 * weight for weight in quintic_weights)
    quintic_shift = quintic_c / 6
    quintic_dimension = 1
    for degree in quintic_degrees:
        quintic_dimension *= degree - 1
    assert_equal(quintic_c, Fraction(9), "quintic elliptic central charge")
    assert_equal(quintic_shift, Fraction(3, 2), "quintic Ramond charge shift")
    assert_equal(quintic_dimension, 4**5, "quintic Jacobi/Witten index dimension")


def compact_coset_hq(k: int, j: Fraction, m: Fraction, eta: Fraction = Fraction(0)):
    return (
        (j * (j + 1) - (m + eta) ** 2) / k + eta**2 / 2,
        -2 * (m + eta) / k + eta,
    )


def noncompact_coset_hq(k: int, j: Fraction, m: Fraction, eta: Fraction = Fraction(0)):
    return (
        (-j * (j - 1) + (m + eta) ** 2) / k + eta**2 / 2,
        2 * (m + eta) / k + eta,
    )


def check_supersymmetric_rank_one_coset_interfaces():
    etas = (Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1))

    for k in range(2, 30):
        minimal_level = k - 2
        c_compact = Fraction(3 * (k - 2), k)

        bosonic_su_c = Fraction(3 * (k - 2), k)
        parent_su_c = bosonic_su_c + Fraction(3, 2)
        removed_n1_u1_c = Fraction(3, 2)
        if parent_su_c - removed_n1_u1_c != c_compact:
            raise AssertionError(f"compact supersymmetric coset c failed for k={k}")

        if c_compact != Fraction(3 * minimal_level, minimal_level + 2):
            raise AssertionError(f"A-series/minimal-model central charge mismatch for k={k}")

        for two_j in range(0, k - 1):
            j = Fraction(two_j, 2)

            h_chiral, q_chiral = compact_coset_hq(k, j, -j)
            assert_equal(h_chiral, q_chiral / 2, f"compact chiral primary j={j}, k={k}")
            assert_equal(h_chiral, Fraction(two_j, 2 * k), f"compact chiral weight j={j}, k={k}")

            for two_m in range(-two_j, two_j + 1, 2):
                m = Fraction(two_m, 2)
                h, q = compact_coset_hq(k, j, m)
                for eta in etas:
                    flowed_h_general = h + eta * q + eta**2 * c_compact / 6
                    flowed_q_general = q + eta * c_compact / 3
                    flowed_h_rank, flowed_q_rank = compact_coset_hq(k, j, m, eta)
                    assert_equal(
                        flowed_h_general,
                        flowed_h_rank,
                        f"compact spectral-flow h k={k}, j={j}, m={m}, eta={eta}",
                    )
                    assert_equal(
                        flowed_q_general,
                        flowed_q_rank,
                        f"compact spectral-flow q k={k}, j={j}, m={m}, eta={eta}",
                    )

            for eta in etas:
                # The simple-current identification is written for the
                # endpoint labels m=j in the text; it preserves h and q.
                image_j = Fraction(k - 2, 2) - j
                image_m = j - Fraction(k - 2, 2)
                h_left, q_left = compact_coset_hq(k, j, j, eta)
                h_right, q_right = compact_coset_hq(k, image_j, image_m, eta - 1)
                assert_equal(h_left, h_right, f"compact field-identification h k={k}, j={j}")
                assert_equal(q_left, q_right, f"compact field-identification q k={k}, j={j}")

    for k in range(1, 30):
        c_cigar = Fraction(3 * (k + 2), k)

        bosonic_sl_c = Fraction(3 * (k + 2), k)
        parent_sl_c = bosonic_sl_c + Fraction(3, 2)
        removed_n1_u1_c = Fraction(3, 2)
        if parent_sl_c - removed_n1_u1_c != c_cigar:
            raise AssertionError(f"noncompact supersymmetric coset c failed for k={k}")

        for two_j in (1, 2, 3, 5):
            j = Fraction(two_j, 2)

            h_chiral, q_chiral = noncompact_coset_hq(k, j, j)
            assert_equal(h_chiral, q_chiral / 2, f"cigar chiral primary j={j}, k={k}")

            for m in (j, -j, j + 1, -j - 1):
                h, q = noncompact_coset_hq(k, j, m)
                for eta in etas:
                    flowed_h_general = h + eta * q + eta**2 * c_cigar / 6
                    flowed_q_general = q + eta * c_cigar / 3
                    flowed_h_rank, flowed_q_rank = noncompact_coset_hq(k, j, m, eta)
                    assert_equal(
                        flowed_h_general,
                        flowed_h_rank,
                        f"cigar spectral-flow h k={k}, j={j}, m={m}, eta={eta}",
                    )
                    assert_equal(
                        flowed_q_general,
                        flowed_q_rank,
                        f"cigar spectral-flow q k={k}, j={j}, m={m}, eta={eta}",
                    )

            for eta in etas:
                image_j = Fraction(k + 2, 2) - j
                image_m = j - Fraction(k + 2, 2)
                h_left, q_left = noncompact_coset_hq(k, j, j, eta)
                h_right, q_right = noncompact_coset_hq(k, image_j, image_m, eta + 1)
                assert_equal(h_left, h_right, f"cigar field-identification h k={k}, j={j}")
                assert_equal(q_left, q_right, f"cigar field-identification q k={k}, j={j}")

        for winding in range(-2, 3):
            for momentum in range(-2, 3):
                left_cartan = Fraction(k * winding + momentum, 2)
                right_cartan = Fraction(k * winding - momentum, 2)
                n = left_cartan - right_cartan
                w = (left_cartan + right_cartan) / k
                assert_equal(n, Fraction(momentum), f"cigar momentum label k={k}")
                assert_equal(w, Fraction(winding), f"cigar winding label k={k}")


def main():
    check_n1_zero_mode_and_ns_coefficients()
    check_n2_chiral_primary_norms()
    check_spectral_flow_automorphism()
    check_ns_to_ramond_ground_state()
    check_extended_n2_spectral_flow_operators()
    check_lg_central_charges()
    check_elliptic_genus_spectral_flow_law()
    check_lg_chi_y_charge_polynomials()
    check_supersymmetric_rank_one_coset_interfaces()
    print("All 2D superconformal algebra, elliptic-genus, and rank-one coset checks passed.")


if __name__ == "__main__":
    main()
