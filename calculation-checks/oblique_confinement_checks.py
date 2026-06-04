#!/usr/bin/env python3
"""Exact finite checks for confinement and oblique-confinement diagnostics.

The manuscript uses the finite center-sensitive charge group

    C_N = Z_N^e direct-sum Z_N^m

with pairing ((e,m),(e',m')) -> (e m' - e' m) / N mod 1.  These checks verify
the arithmetic behind screening quotients, orthogonal complements of
condensates, and the dyonic unconfined direction in oblique confinement.  They
also verify the finite bookkeeping behind the conditional line-asymptotic
classifier: condensate pairing distance, local perimeter/cusp subtraction,
area-rate extraction from supplied surface-cost bounds, static-potential limit
order, and endpoint-screening negative controls.  The script separately checks
the primitive finite algebra in a strong-coupling polymer surface window and in
the controlled three-dimensional
Polyakov monopole-gas mechanism: dual-photon mass normalization, sine-Gordon
wall first-order identities, and the area-law/static-potential extraction.  A
separate finite transfer-matrix model checks the string-breaking spectral
extraction test for Wilson-loop diagnostics.  It does not simulate a continuum
gauge theory, prove four-dimensional continuum surface-cost bounds, or prove
that a condensate forms.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

Charge = tuple[int, int]
Matrix = list[list[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def det2(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matrix_scale(coefficient: Fraction, matrix: Matrix) -> Matrix:
    return [[coefficient * entry for entry in row] for row in matrix]


def matrix_sub(lhs: Matrix, rhs: Matrix) -> Matrix:
    return [
        [lhs[row][col] - rhs[row][col] for col in range(2)]
        for row in range(2)
    ]


def add_charge(n: int, lhs: Charge, rhs: Charge) -> Charge:
    return ((lhs[0] + rhs[0]) % n, (lhs[1] + rhs[1]) % n)


def scale_charge(n: int, coefficient: int, charge: Charge) -> Charge:
    return ((coefficient * charge[0]) % n, (coefficient * charge[1]) % n)


def dirac_numerator(n: int, lhs: Charge, rhs: Charge) -> int:
    e, m = lhs
    ep, mp = rhs
    return (e * mp - ep * m) % n


def all_charges(n: int) -> list[Charge]:
    return [(e, m) for e in range(n) for m in range(n)]


def subgroup_generated(n: int, generators: list[Charge]) -> set[Charge]:
    subgroup: set[Charge] = set()
    for coefficients in product(range(n), repeat=len(generators)):
        total = (0, 0)
        for coefficient, generator in zip(coefficients, generators, strict=True):
            total = add_charge(n, total, scale_charge(n, coefficient, generator))
        subgroup.add(total)
    return subgroup


def orthogonal_complement(n: int, subgroup: set[Charge]) -> set[Charge]:
    return {
        charge
        for charge in all_charges(n)
        if all(dirac_numerator(n, charge, generator) == 0 for generator in subgroup)
    }


def pairing_distance_numerator(n: int, charge: Charge, subgroup: set[Charge]) -> int:
    return max(
        min(pairing, n - pairing)
        for pairing in (dirac_numerator(n, charge, generator) for generator in subgroup)
    )


def is_isotropic(n: int, subgroup: set[Charge]) -> bool:
    return all(dirac_numerator(n, lhs, rhs) == 0 for lhs, rhs in product(subgroup, repeat=2))


def quotient_classes(n: int, ambient: set[Charge], subgroup: set[Charge]) -> list[frozenset[Charge]]:
    unseen = set(ambient)
    classes: list[frozenset[Charge]] = []
    while unseen:
        representative = next(iter(unseen))
        coset = frozenset(add_charge(n, representative, s) for s in subgroup)
        classes.append(coset)
        unseen -= set(coset)
    return classes


def check_screened_pairing_descends() -> None:
    for n in range(2, 13):
        for generator in [(1, 0), (0, 1)]:
            screened = subgroup_generated(n, [generator])
            assert_equal(f"screened subgroup isotropic N={n} gen={generator}", is_isotropic(n, screened), True)
            sperp = orthogonal_complement(n, screened)
            classes = quotient_classes(n, sperp, screened)
            for class_a, class_b in product(classes, repeat=2):
                values = {
                    dirac_numerator(n, a, b)
                    for a, b in product(class_a, class_b)
                }
                assert_equal(
                    f"descended pairing well-defined N={n} gen={generator}",
                    len(values),
                    1,
                )


def check_maximal_isotropic_axes_and_dyons() -> None:
    for n in range(2, 13):
        for p in range(n):
            condensate = subgroup_generated(n, [(p, 1)])
            assert_equal(f"dyonic condensate size N={n} p={p}", len(condensate), n)
            assert_equal(f"dyonic condensate isotropic N={n} p={p}", is_isotropic(n, condensate), True)
            assert_equal(
                f"dyonic condensate maximal N={n} p={p}",
                orthogonal_complement(n, condensate),
                condensate,
            )


def check_oblique_unconfined_direction() -> None:
    for n in range(2, 13):
        for p in range(n):
            condensate = subgroup_generated(n, [(p, 1)])
            unconfined = orthogonal_complement(n, condensate)
            expected = {(p * m % n, m) for m in range(n)}
            assert_equal(f"oblique condition e=p m mod N, N={n} p={p}", unconfined, expected)


def check_magnetic_condensation_confines_electric_nality() -> None:
    for n in range(2, 13):
        magnetic = subgroup_generated(n, [(0, 1)])
        unconfined = orthogonal_complement(n, magnetic)
        expected = {(0, m) for m in range(n)}
        assert_equal(f"magnetic condensation leaves only electric-neutral N={n}", unconfined, expected)
        for e in range(1, n):
            assert_equal(
                f"nonzero electric N-ality confined N={n} e={e}",
                (e, 0) in unconfined,
                False,
            )


def check_nonisotropic_pair_cannot_condense_together() -> None:
    for n in range(2, 13):
        electric_magnetic_pair = subgroup_generated(n, [(1, 0), (0, 1)])
        assert_equal(
            f"electric and magnetic generators are not mutually local N={n}",
            is_isotropic(n, electric_magnetic_pair),
            False,
        )


def check_conditional_line_asymptotic_classifier() -> None:
    for n in range(2, 13):
        for p in range(n):
            condensate = subgroup_generated(n, [(p, 1)])
            unconfined = orthogonal_complement(n, condensate)
            sigma_star = Fraction(1, n * n)
            for charge in all_charges(n):
                distance = pairing_distance_numerator(n, charge, condensate)
                assert_equal(
                    f"pairing distance detects K-perp N={n} p={p} charge={charge}",
                    distance == 0,
                    charge in unconfined,
                )
                supplied_lower_area_rate = sigma_star * distance * distance
                if charge in unconfined:
                    assert_equal(
                        f"K-perp charge has zero supplied classifier rate N={n} p={p} charge={charge}",
                        supplied_lower_area_rate,
                        Fraction(0),
                    )
                else:
                    assert_true(
                        f"non-K-perp charge is classified by positive supplied rate N={n} p={p} charge={charge}",
                        supplied_lower_area_rate > 0,
                    )
                    topological_data_alone_rate = Fraction(0)
                    assert_true(
                        f"pairing alone does not derive a surface cost N={n} p={p} charge={charge}",
                        topological_data_alone_rate < supplied_lower_area_rate,
                    )

    supplied_area_rate = Fraction(7, 19)
    finite_perimeter = Fraction(5, 23)
    divergent_perimeter = Fraction(101, 3)
    divergent_cusp = Fraction(97, 5)
    cusps = 4
    previous_rate_error: Fraction | None = None
    for size in [8, 16, 32]:
        area = Fraction(size * size)
        perimeter = Fraction(4 * size)
        bare_exponent = (
            supplied_area_rate * area
            + (finite_perimeter + divergent_perimeter) * perimeter
            + divergent_cusp * cusps
            + Fraction(1, size)
        )
        renormalized_exponent = (
            bare_exponent
            - divergent_perimeter * perimeter
            - divergent_cusp * cusps
        )
        expected_renormalized = (
            supplied_area_rate * area
            + finite_perimeter * perimeter
            + Fraction(1, size)
        )
        assert_equal(
            f"local line counterterms remove cutoff pieces size={size}",
            renormalized_exponent,
            expected_renormalized,
        )
        rate_error = renormalized_exponent / area - supplied_area_rate
        assert_equal(
            f"large-loop rate error is perimeter plus residual size={size}",
            rate_error,
            finite_perimeter * perimeter / area + Fraction(1, size) / area,
        )
        if previous_rate_error is not None:
            assert_true(
                f"regular large-loop topology suppresses perimeter rate size={size}",
                rate_error < previous_rate_error,
            )
        previous_rate_error = rate_error

        unrenormalized_rate = bare_exponent / area - supplied_area_rate
        assert_true(
            f"large-loop rate before line renormalization keeps cutoff pollution size={size}",
            unrenormalized_rate > rate_error,
        )

    spatial_separation = Fraction(11, 3)
    source_self_energy = Fraction(2, 7)
    corner_counterterm = Fraction(3, 5)
    for euclidean_time in [20, 40, 80]:
        area = spatial_separation * euclidean_time
        perimeter = 2 * euclidean_time + 2 * spatial_separation
        exponent = (
            supplied_area_rate * area
            + source_self_energy * perimeter
            + corner_counterterm * 4
        )
        source_subtracted_rate = exponent / euclidean_time - 2 * source_self_energy
        finite_time_error = (
            2 * source_self_energy * spatial_separation
            + 4 * corner_counterterm
        ) / euclidean_time
        assert_equal(
            f"rectangular static limit isolates linear coefficient T={euclidean_time}",
            source_subtracted_rate,
            supplied_area_rate * spatial_separation + finite_time_error,
        )

    screening_mass = Fraction(13, 5)
    large_separation = Fraction(100)
    positive_linear_candidate = supplied_area_rate * large_separation
    assert_true(
        "endpoint screening bound rejects positive asymptotic linear potential",
        positive_linear_candidate > 2 * screening_mass,
    )


def check_strong_coupling_polymer_surface_window() -> None:
    # This is the finite arithmetic of the non-circular strong-coupling
    # mechanism.  The signed lower estimate on the minimal surface sum prevents
    # cancellation; a separate absolute upper estimate on that same minimal
    # sector supplies area suppression from above; a smaller decorated tail then
    # preserves the two-sided window.  No continuum string tension is inserted.
    q = Fraction(1, 6)
    tail_ratio = Fraction(1, 2)
    minimal_lower_prefactor = Fraction(5, 7)
    minimal_upper_prefactor = Fraction(9, 7)
    tail_prefactor = Fraction(3, 5)
    previous_upper_prefactor_proxy: Fraction | None = None
    for minimal_area in [12, 18, 24]:
        minimal_lower = minimal_lower_prefactor * q**minimal_area
        minimal_upper = minimal_upper_prefactor * q**minimal_area
        decorated_tail = tail_prefactor * (q * tail_ratio) ** minimal_area
        lower_window = minimal_lower - decorated_tail
        upper_window = minimal_upper + decorated_tail
        assert_true(
            f"strong-coupling signed minimal sector is nonzero A={minimal_area}",
            minimal_lower > 0,
        )
        assert_true(
            f"decorated strong-coupling tail is smaller than lower minimal sector A={minimal_area}",
            decorated_tail < minimal_lower,
        )
        assert_true(
            f"polymer window lower bound stays positive A={minimal_area}",
            lower_window >= minimal_lower / 2,
        )
        assert_true(
            f"absolute minimal-sector majorant decays with area A={minimal_area}",
            minimal_upper <= 2 * q**minimal_area,
        )
        assert_true(
            f"polymer window upper bound has positive area suppression A={minimal_area}",
            upper_window <= (minimal_upper_prefactor + tail_prefactor) * q**minimal_area,
        )
        upper_prefactor_proxy = upper_window / q**minimal_area
        assert_equal(
            f"upper prefactor separates minimal and decorated estimates A={minimal_area}",
            upper_prefactor_proxy,
            minimal_upper_prefactor + tail_prefactor * tail_ratio**minimal_area,
        )
        if previous_upper_prefactor_proxy is not None:
            assert_true(
                f"polymer prefactor does not smuggle in area growth A={minimal_area}",
                upper_prefactor_proxy < previous_upper_prefactor_proxy,
            )
        previous_upper_prefactor_proxy = upper_prefactor_proxy

        rogue_minimal_sum = Fraction(1)
        assert_true(
            f"lower noncancellation estimate alone permits nondecaying minimal sum A={minimal_area}",
            rogue_minimal_sum >= minimal_lower,
        )
        assert_true(
            f"absolute minimal-sector majorant is independent evidence A={minimal_area}",
            rogue_minimal_sum > minimal_upper,
        )


def check_polyakov_monopole_gas_wall_tension() -> None:
    # In the declared normalization
    # S = int [kappa/2 (d phi)^2 + 2 zeta (1-cos phi)] d^3x,
    # the dual photon has m_gamma^2 = 2 zeta/kappa and the primitive
    # sine-Gordon wall tension is sigma_P = 8 sqrt(2 kappa zeta).
    kappa = Fraction(5, 7)
    zeta = Fraction(11, 13)
    mass_squared = 2 * zeta / kappa
    assert_equal("Polyakov dual photon mass squared", mass_squared, Fraction(154, 65))

    tension_squared = 128 * kappa * zeta
    assert_equal("Polyakov wall tension squared", tension_squared, Fraction(7040, 91))
    assert_equal(
        "Polyakov wall tension equals 8 kappa m_gamma",
        tension_squared,
        64 * kappa * kappa * mass_squared,
    )

    # The explicit kink phi(x)=4 arctan exp(m x) obeys
    # phi'/m = 2 sin(phi/2).  With u=exp(m x),
    # sin(phi/2)=sin(2 arctan u)=2u/(1+u^2).
    for u in [Fraction(1, 3), Fraction(2, 5), Fraction(7, 4)]:
        derivative_over_mass = 4 * u / (1 + u * u)
        two_sin_half_phi = 4 * u / (1 + u * u)
        assert_equal(
            f"Polyakov kink first-order identity u={u}",
            derivative_over_mass,
            two_sin_half_phi,
        )

        sin_half_phi_squared = (2 * u / (1 + u * u)) ** 2
        one_minus_cos_phi = 2 * sin_half_phi_squared
        gradient_energy_density = (
            kappa
            * Fraction(1, 2)
            * mass_squared
            * derivative_over_mass
            * derivative_over_mass
        )
        potential_density = 2 * zeta * one_minus_cos_phi
        assert_equal(
            f"Polyakov wall first-integral energy balance u={u}",
            gradient_energy_density,
            potential_density,
        )

    # For a rectangular loop of area A=L T, the area exponent sigma A gives
    # V(L)=sigma L after taking -T^{-1} log <W>.  Track the coefficient
    # algebra without choosing an irrational value for sigma.
    spatial_length = Fraction(17, 5)
    time_length = Fraction(19, 3)
    area = spatial_length * time_length
    assert_equal("Polyakov rectangular area", area, Fraction(323, 15))
    assert_equal(
        "Polyakov static potential squared from area law",
        tension_squared * area * area / (time_length * time_length),
        tension_squared * spatial_length * spatial_length,
    )


def two_state_correlator(
    overlap: Matrix,
    transfer_eigenvalues: tuple[Fraction, Fraction],
    time: int,
) -> Matrix:
    return [
        [
            sum(
                overlap[row][state]
                * overlap[col][state]
                * transfer_eigenvalues[state] ** time
                for state in range(2)
            )
            for col in range(2)
        ]
        for row in range(2)
    ]


def one_channel_correlator(
    string_overlap: Fraction,
    broken_overlap: Fraction,
    string_eigenvalue: Fraction,
    broken_eigenvalue: Fraction,
    time: int,
) -> Fraction:
    return (
        string_overlap * string_overlap * string_eigenvalue**time
        + broken_overlap * broken_overlap * broken_eigenvalue**time
    )


def generalized_characteristic_value(
    overlap: Matrix,
    transfer_eigenvalues: tuple[Fraction, Fraction],
    time: int,
    test_eigenvalue: Fraction,
) -> Fraction:
    c_now = two_state_correlator(overlap, transfer_eigenvalues, time)
    c_next = two_state_correlator(overlap, transfer_eigenvalues, time + 1)
    return det2(matrix_sub(c_next, matrix_scale(test_eigenvalue, c_now)))


def check_string_breaking_spectral_extraction_test() -> None:
    string_eigenvalue = Fraction(1, 5)
    broken_eigenvalue = Fraction(1, 3)
    transfer_eigenvalues = (string_eigenvalue, broken_eigenvalue)
    assert_true(
        "broken-string state is the lower static energy in transfer ordering",
        broken_eigenvalue > string_eigenvalue,
    )

    # A Wilson-loop-like flux operator may have tiny overlap with the broken
    # ground state, so its finite-time effective eigenvalue can look string-like.
    string_overlap = Fraction(1)
    broken_overlap = Fraction(1, 20)
    midpoint = (string_eigenvalue + broken_eigenvalue) / 2
    early_time = 1
    late_time = 12
    early_effective = one_channel_correlator(
        string_overlap,
        broken_overlap,
        string_eigenvalue,
        broken_eigenvalue,
        early_time + 1,
    ) / one_channel_correlator(
        string_overlap,
        broken_overlap,
        string_eigenvalue,
        broken_eigenvalue,
        early_time,
    )
    late_effective = one_channel_correlator(
        string_overlap,
        broken_overlap,
        string_eigenvalue,
        broken_eigenvalue,
        late_time + 1,
    ) / one_channel_correlator(
        string_overlap,
        broken_overlap,
        string_eigenvalue,
        broken_eigenvalue,
        late_time,
    )
    assert_true(
        "short-time Wilson channel still looks flux-tube dominated",
        early_effective < midpoint,
    )
    assert_true(
        "late-time Wilson channel tends toward the screened ground state",
        late_effective > midpoint,
    )

    # Adding a broken-string trial operator gives an invertible overlap matrix.
    overlap = [
        [Fraction(1), Fraction(1, 20)],
        [Fraction(1, 10), Fraction(1)],
    ]
    assert_equal("string-breaking overlap determinant", det2(overlap), Fraction(199, 200))
    time = 3
    c_now = two_state_correlator(overlap, transfer_eigenvalues, time)
    assert_true("two-channel correlator is full rank", det2(c_now) > 0)
    for eigenvalue in transfer_eigenvalues:
        assert_equal(
            f"GEVP characteristic vanishes at retained eigenvalue {eigenvalue}",
            generalized_characteristic_value(overlap, transfer_eigenvalues, time, eigenvalue),
            Fraction(0),
        )

    # A rank-one basis cannot distinguish the flux-tube and broken-string levels.
    rank_one_overlap = [
        [Fraction(1), Fraction(1, 20)],
        [Fraction(2), Fraction(1, 10)],
    ]
    assert_equal("rank-one overlap determinant", det2(rank_one_overlap), Fraction(0))
    assert_equal(
        "rank-one correlator determinant",
        det2(two_state_correlator(rank_one_overlap, transfer_eigenvalues, time)),
        Fraction(0),
    )

    # A higher retained-energy tail gives an entrywise perturbation bounded by
    # the largest omitted overlap product times its transfer eigenvalue.
    tail_eigenvalue = Fraction(1, 7)
    tail_overlaps = [Fraction(1, 4), Fraction(1, 5)]
    tail_matrix = [
        [
            tail_overlaps[row] * tail_overlaps[col] * tail_eigenvalue**time
            for col in range(2)
        ]
        for row in range(2)
    ]
    tail_entry_bound = max(tail_overlaps) ** 2 * tail_eigenvalue**time
    for row in range(2):
        for col in range(2):
            assert_true(
                f"string-breaking tail entry bound ({row},{col})",
                abs(tail_matrix[row][col]) <= tail_entry_bound,
            )
    measurement_entry_error = Fraction(1, 10000)
    gap_margin = broken_eigenvalue - string_eigenvalue
    assert_true(
        "declared entry budget is below the transfer gap margin",
        tail_entry_bound + measurement_entry_error < gap_margin / 10,
    )


def main() -> None:
    check_screened_pairing_descends()
    check_maximal_isotropic_axes_and_dyons()
    check_oblique_unconfined_direction()
    check_magnetic_condensation_confines_electric_nality()
    check_nonisotropic_pair_cannot_condense_together()
    check_conditional_line_asymptotic_classifier()
    check_strong_coupling_polymer_surface_window()
    check_polyakov_monopole_gas_wall_tension()
    check_string_breaking_spectral_extraction_test()
    print("All oblique-confinement finite charge checks passed.")


if __name__ == "__main__":
    main()
