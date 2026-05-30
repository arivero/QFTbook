# Carlson Quoted-Theorem Boundary Pass

Date: 2026-05-30

Scope:
- Volume II, Chapter 7, `qthm:carlson-half-plane-uniqueness`.
- Global quoted-theorem audit: every quoted theorem must be accompanied by
  enough local proof mechanism that the manuscript is not merely importing a
  named result as an unexplained black box.

Edits:
- Replaced the compressed Carlson statement by explicit strict exponential
  type hypotheses in the closed right half-plane and on the imaginary-axis
  boundary.
- Added the zero-counting function \(N_F(R)\) and the half-plane
  Carleman--Jensen density estimate
  \[
    \int_1^R N_F(r)r^{-2}\,dr
    \le
    \frac{\sigma+\delta}{\pi}\log R+O_\delta(1).
  \]
- Derived the contradiction with zeros at every positive integer from the
  lower bound \(\int_1^R N_F(r)r^{-2}dr\ge \log R+O(1)\).
- Recorded the sharpness of the \(\pi\) threshold through \(\sin\pi J\).

Remaining boundary:
- The half-plane Carleman--Jensen formula and the elementary
  Phragmen--Lindelof smoothing are complex-analysis inputs rather than QFT
  theorems.  The QFT-specific use in Regge interpolation is now explicit:
  complex-\(J\) uniqueness requires an independently stated growth class.
