# Anomaly Chern--Weil descent-coefficient pass

Date: 2026-06-01.

Issue context: GitHub #696, anomaly proof debt in monograph conventions.

## Scope

Volume II, Chapter 20 already stated the four-dimensional chiral anomaly as
the descent of
\[
  I_6^R=\frac{\ii}{24\pi^2}\operatorname{tr}_R(\mathsf F^3)
\]
and displayed the Chern--Simons five-form
\[
  \operatorname{tr}_R\left(
    \mathsf A(\dd\mathsf A)^2
    +\frac32\mathsf A^3\dd\mathsf A
    +\frac35\mathsf A^5
  \right).
\]
The coefficient check existed in `calculation-checks/`, but the manuscript
called the representative "standard" without deriving the coefficients.
That was too much hidden convention arithmetic for the anomaly chapter.

## Manuscript changes

- Inserted the Chern--Weil homotopy
  \(\mathsf A_t=t\mathsf A\),
  \(\mathsf F_t=t\,\dd\mathsf A+t^2\mathsf A^2\).
- Derived
  \[
    \frac{\dd}{\dd t}\operatorname{tr}_R(\mathsf F_t^3)
    =
    3\dd\,\operatorname{tr}_R(\mathsf A\mathsf F_t^2)
  \]
  from Bianchi identity and trace cyclicity.
- Integrated in \(t\) to obtain the coefficients
  \(1,\frac32,\frac35\), including the cyclicity step that turns the two
  mixed terms into \(\operatorname{tr}_R(\mathsf A^3\dd\mathsf A)\).
- Added the corresponding \(n=2\) descent homotopy coefficients
  \(6\int_0^1(1-t)t\dd t=1\) and
  \(6\int_0^1(1-t)t^2\dd t=\frac12\) for the displayed
  \(I_4^{(1)}\) representative.

## Calculation check

`calculation-checks/anomaly_polynomial_descent_checks.py` now verifies the
\(n=2\) consistent-descent homotopy coefficients in exact rational
arithmetic, in addition to the existing universal Chern--Simons
transgression coefficients.

This pass narrows #696 but does not close it.  The full APS,
Bismut--Freed, Dai--Freed, and real mod-two-index analytic infrastructure
remains a genuine theorem-boundary cluster.
