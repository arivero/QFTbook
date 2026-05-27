#!/usr/bin/env python3
"""Finite checks for supersymmetric Wilsonian BV pushforward algebra."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


class FourierOdd:
    """Finite Fourier-polynomial algebra with odd variables eta, xi1, xi2."""

    def __init__(self, terms=None):
        self.terms = {
            (tuple(freqs), odd_mask): Fraction(coeff)
            for (freqs, odd_mask), coeff in (terms or {}).items()
            if coeff
        }

    @staticmethod
    def monomial(freqs, odd_mask=0, coeff=1):
        return FourierOdd({(tuple(freqs), odd_mask): Fraction(coeff)})

    def __add__(self, other):
        result = dict(self.terms)
        for key, coeff in other.terms.items():
            result[key] = result.get(key, Fraction(0)) + coeff
        return FourierOdd(result)

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return FourierOdd({key: -coeff for key, coeff in self.terms.items()})

    def scale(self, value):
        return FourierOdd({key: Fraction(value) * coeff for key, coeff in self.terms.items()})

    def even_derivative(self, frequency_index):
        result = {}
        for (freqs, odd_mask), coeff in self.terms.items():
            multiplier = freqs[frequency_index]
            if multiplier == 0:
                continue
            key = (freqs, odd_mask)
            result[key] = result.get(key, Fraction(0)) + multiplier * coeff
        return FourierOdd(result)

    def odd_left_derivative(self, odd_index):
        result = {}
        bit = 1 << odd_index
        for (freqs, odd_mask), coeff in self.terms.items():
            if not (odd_mask & bit):
                continue
            lower_bits = odd_mask & (bit - 1)
            sign = -1 if lower_bits.bit_count() % 2 else 1
            key = (freqs, odd_mask ^ bit)
            result[key] = result.get(key, Fraction(0)) + sign * coeff
        return FourierOdd(result)

    def laplacian_pair(self, frequency_index, odd_index):
        return self.odd_left_derivative(odd_index).even_derivative(frequency_index)

    def pushforward(self, fiber_frequency_index, fiber_odd_index):
        bit = 1 << fiber_odd_index
        result = {}
        for (freqs, odd_mask), coeff in self.terms.items():
            if freqs[fiber_frequency_index] != 0:
                continue
            if odd_mask & bit:
                continue
            key = (freqs, odd_mask)
            result[key] = result.get(key, Fraction(0)) + coeff
        return FourierOdd(result)

    def __eq__(self, other):
        return self.terms == other.terms

    def __repr__(self):
        return f"FourierOdd({self.terms!r})"


def total_laplacian(element):
    # Frequency slots: 0=y, 1=x1, 2=x2. Odd slots: 0=eta, 1=xi1, 2=xi2.
    return (
        element.laplacian_pair(0, 0)
        + element.laplacian_pair(1, 1)
        + element.laplacian_pair(2, 2)
    )


def sample_element():
    return (
        FourierOdd.monomial((2, 3, 0), 0b011, Fraction(5, 7))
        + FourierOdd.monomial((-1, 0, 4), 0b101, Fraction(-3, 2))
        + FourierOdd.monomial((0, 0, 0), 0b001, Fraction(9))
        + FourierOdd.monomial((5, 0, 0), 0b000, Fraction(4))
        + FourierOdd.monomial((3, -2, 1), 0b111, Fraction(6, 5))
    )


def check_bv_stokes_for_fiber_laplacian():
    alpha = sample_element()
    pushed_fiber_laplacian = alpha.laplacian_pair(1, 1).pushforward(1, 1)
    assert_equal(pushed_fiber_laplacian, FourierOdd(), "fiber BV Stokes")


def check_pushforward_chain_map():
    alpha = sample_element()
    pushed_total = total_laplacian(alpha).pushforward(1, 1)
    base_plus_remaining = (
        alpha.pushforward(1, 1).laplacian_pair(0, 0)
        + alpha.pushforward(1, 1).laplacian_pair(2, 2)
    )
    assert_equal(pushed_total, base_plus_remaining, "BV pushforward chain map")


def check_qme_preservation_model():
    beta = sample_element()
    alpha = total_laplacian(beta)
    assert_equal(total_laplacian(alpha), FourierOdd(), "finite BV Laplacian squares to zero")
    pushed = alpha.pushforward(1, 1)
    remaining_laplacian = pushed.laplacian_pair(0, 0) + pushed.laplacian_pair(2, 2)
    assert_equal(remaining_laplacian, FourierOdd(), "QME preservation after pushforward")


def check_semigroup_pushforward():
    alpha = sample_element()
    sequential = alpha.pushforward(1, 1).pushforward(2, 2)
    reverse = alpha.pushforward(2, 2).pushforward(1, 1)
    direct = alpha.pushforward(1, 1).pushforward(2, 2)
    assert_equal(sequential, reverse, "commuting product-cycle pushforwards")
    assert_equal(sequential, direct, "sequential equals direct pushforward")


def main():
    check_bv_stokes_for_fiber_laplacian()
    check_pushforward_chain_map()
    check_qme_preservation_model()
    check_semigroup_pushforward()
    print("All supersymmetric Wilsonian BV checks passed.")


if __name__ == "__main__":
    main()
