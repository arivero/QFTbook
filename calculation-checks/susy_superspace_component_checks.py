#!/usr/bin/env python3
"""Finite Grassmann checks for 4D N=1 superspace component conventions."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


class Form:
    def __init__(self, terms=None):
        self.terms = {
            mask: Fraction(coeff)
            for mask, coeff in (terms or {}).items()
            if coeff
        }

    @staticmethod
    def scalar(value):
        return Form({0: Fraction(value)})

    @staticmethod
    def basis(index):
        return Form({1 << index: Fraction(1)})

    def __add__(self, other):
        result = dict(self.terms)
        for mask, coeff in other.terms.items():
            result[mask] = result.get(mask, Fraction(0)) + coeff
        return Form(result)

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Form({mask: -coeff for mask, coeff in self.terms.items()})

    def scale(self, value):
        return Form({mask: Fraction(value) * coeff for mask, coeff in self.terms.items()})

    def wedge(self, other):
        result = {}
        for left_mask, left_coeff in self.terms.items():
            for right_mask, right_coeff in other.terms.items():
                if left_mask & right_mask:
                    continue
                inversions = 0
                for left_index in range(16):
                    if not (left_mask & (1 << left_index)):
                        continue
                    for right_index in range(left_index):
                        if right_mask & (1 << right_index):
                            inversions += 1
                sign = -1 if inversions % 2 else 1
                new_mask = left_mask | right_mask
                result[new_mask] = result.get(new_mask, Fraction(0)) + (
                    sign * left_coeff * right_coeff
                )
        return Form(result)

    def left_derivative(self, index):
        result = {}
        bit = 1 << index
        for mask, coeff in self.terms.items():
            if not (mask & bit):
                continue
            lower_bits = mask & (bit - 1)
            sign = -1 if lower_bits.bit_count() % 2 else 1
            result[mask ^ bit] = result.get(mask ^ bit, Fraction(0)) + sign * coeff
        return Form(result)

    def without_theta_square(self):
        """Extract coefficient relative to theta^2=2 theta^1 theta^2."""
        theta_mask = 0b11
        result = {}
        for mask, coeff in self.terms.items():
            if (mask & theta_mask) != theta_mask:
                continue
            if mask & ~theta_mask != mask ^ theta_mask:
                raise AssertionError("unexpected theta mask arithmetic")
            result[mask ^ theta_mask] = result.get(mask ^ theta_mask, Fraction(0)) + coeff / 2
        return Form(result)

    def __eq__(self, other):
        return self.terms == other.terms

    def __repr__(self):
        return f"Form({self.terms!r})"


THETA_1 = Form.basis(0)
THETA_2 = Form.basis(1)
THETA_SQUARE = THETA_1.wedge(THETA_2).scale(2)


def psi(flavor, upper_index):
    # Variables are psi(flavor=0,1; upper_index=1,2) after theta variables.
    return Form.basis(2 + 2 * flavor + (upper_index - 1))


def psi_lower(flavor, lower_index):
    # epsilon_{12}=1: psi_1=psi^2 and psi_2=-psi^1.
    if lower_index == 1:
        return psi(flavor, 2)
    if lower_index == 2:
        return -psi(flavor, 1)
    raise ValueError("spinor index must be 1 or 2")


def theta_dot_psi(flavor):
    return THETA_1.wedge(psi_lower(flavor, 1)) + THETA_2.wedge(psi_lower(flavor, 2))


def spinor_contraction(left_flavor, right_flavor):
    return (
        psi(left_flavor, 1).wedge(psi_lower(right_flavor, 1))
        + psi(left_flavor, 2).wedge(psi_lower(right_flavor, 2))
    )


def check_theta_square_normalization_and_derivative():
    assert_equal(
        THETA_SQUARE.terms,
        {0b11: Fraction(2)},
        "theta^2 equals 2 theta^1 theta^2",
    )
    assert_equal(
        THETA_SQUARE.left_derivative(0),
        THETA_2.scale(2),
        "left derivative d theta^2 / d theta^1",
    )
    assert_equal(
        THETA_SQUARE.left_derivative(1),
        THETA_1.scale(-2),
        "left derivative d theta^2 / d theta^2",
    )


def check_theta_psi_product_identity():
    for left in range(2):
        for right in range(2):
            product = theta_dot_psi(left).wedge(theta_dot_psi(right))
            expected = THETA_SQUARE.wedge(spinor_contraction(left, right)).scale(
                Fraction(-1, 2)
            )
            assert_equal(
                product,
                expected,
                f"(theta psi_{left})(theta psi_{right}) identity",
            )


def check_chiral_f_term_yukawa_coefficient():
    hessian = [
        [Fraction(3), Fraction(-2)],
        [Fraction(-2), Fraction(5)],
    ]
    quadratic_theta_part = Form.scalar(0)
    expected_yukawa = Form.scalar(0)
    for left in range(2):
        for right in range(2):
            quadratic_theta_part += theta_dot_psi(left).wedge(theta_dot_psi(right)).scale(
                hessian[left][right]
            )
            expected_yukawa += spinor_contraction(left, right).scale(
                Fraction(-1, 2) * hessian[left][right]
            )

    assert_equal(
        quadratic_theta_part.without_theta_square(),
        expected_yukawa,
        "F-term Yukawa coefficient -1/2 W_ij psi^i psi^j",
    )


def check_auxiliary_elimination():
    # L_aux = Fbar F + F W + Fbar Wbar with Wbar=W in this finite real test.
    for w in (Fraction(-3, 2), Fraction(0), Fraction(5)):
        on_shell_f = -w
        lagrangian = on_shell_f * on_shell_f + on_shell_f * w + on_shell_f * w
        assert_equal(lagrangian, -w * w, "Wess-Zumino auxiliary elimination")
        potential = -lagrangian
        assert_equal(potential, w * w, "positive F-term potential")


def main():
    check_theta_square_normalization_and_derivative()
    check_theta_psi_product_identity()
    check_chiral_f_term_yukawa_coefficient()
    check_auxiliary_elimination()
    print("All superspace component convention checks passed.")


if __name__ == "__main__":
    main()
