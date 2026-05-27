#!/usr/bin/env python3
"""Finite algebra checks for gauge-covariant link smearing.

These checks support Volume XI, Chapter 5.  They verify the polar-projection
equivariance and stout-smearing algebra used in the text.
"""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def random_su(n: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    q = q @ np.diag(np.conjugate(phases))
    det_q = np.linalg.det(q)
    return q / det_q ** (1 / n)


def inverse_square_root_positive(h: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h)
    require(np.all(vals > 0), "positive matrix should have positive eigenvalues")
    return vecs @ np.diag(vals ** (-0.5)) @ vecs.conjugate().T


def polar_unitary(x: np.ndarray) -> np.ndarray:
    return x @ inverse_square_root_positive(x.conjugate().T @ x)


def su_project_from_polar(x: np.ndarray) -> np.ndarray:
    u = polar_unitary(x)
    n = u.shape[0]
    return u / np.linalg.det(u) ** (1 / n)


def su_algebra_projection(m: np.ndarray) -> np.ndarray:
    anti = 0.5 * (m - m.conjugate().T)
    n = m.shape[0]
    return anti - np.trace(anti) * np.eye(n, dtype=complex) / n


def expm_by_eigen(q: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eig(q)
    return vecs @ np.diag(np.exp(vals)) @ np.linalg.inv(vecs)


def check_polar_projection_equivariance() -> None:
    rng = np.random.default_rng(314159)
    n = 3
    x = np.eye(n) + 0.2 * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
    g = random_su(n, rng)
    h = random_su(n, rng)
    left = su_project_from_polar(g @ x @ h.conjugate().T)
    right = g @ su_project_from_polar(x) @ h.conjugate().T
    require(np.allclose(left, right, atol=1e-10), "polar SU projection should be equivariant")
    require(np.allclose(left.conjugate().T @ left, np.eye(n), atol=1e-10), "projection should be unitary")
    require(abs(np.linalg.det(left) - 1) < 1e-10, "projection should have determinant one")


def check_su_algebra_projection() -> None:
    rng = np.random.default_rng(271828)
    m = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q = su_algebra_projection(m)
    require(np.allclose(q + q.conjugate().T, 0, atol=1e-12), "projected matrix should be anti-Hermitian")
    require(abs(np.trace(q)) < 1e-12, "projected matrix should be traceless")

    u = expm_by_eigen(q)
    require(np.allclose(u.conjugate().T @ u, np.eye(3), atol=1e-10), "exp(q) should be unitary")
    require(abs(np.linalg.det(u) - 1) < 1e-10, "exp(q) should have determinant one")


def check_stout_covariance_at_algebra_level() -> None:
    rng = np.random.default_rng(161803)
    n = 3
    link = random_su(n, rng)
    staple = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    g_left = random_su(n, rng)
    g_right = random_su(n, rng)

    omega = staple @ link.conjugate().T
    q = su_algebra_projection(omega)

    transformed_staple = g_left @ staple @ g_right.conjugate().T
    transformed_link = g_left @ link @ g_right.conjugate().T
    transformed_omega = transformed_staple @ transformed_link.conjugate().T
    transformed_q = su_algebra_projection(transformed_omega)

    require(
        np.allclose(transformed_q, g_left @ q @ g_left.conjugate().T, atol=1e-10),
        "stout algebra element should transform by endpoint conjugation",
    )


def main() -> None:
    check_polar_projection_equivariance()
    check_su_algebra_projection()
    check_stout_covariance_at_algebra_level()
    print("All link-smearing checks passed.")


if __name__ == "__main__":
    main()
