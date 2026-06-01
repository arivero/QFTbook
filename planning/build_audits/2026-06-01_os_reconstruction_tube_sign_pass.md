# OS reconstruction tube-sign pass

Related issue: GitHub #695, foundational/AQFT proof-debt.

## Scope

This pass audits the sign convention connecting ordered Euclidean OS
correlators to Lorentzian Wightman tube boundary values.  The monograph uses
mostly-plus signature.  With positive-energy support in \(\overline V_+\), the
Wightman forward tube is
\[
  z=\xi-\ii\eta,\qquad \eta\in V_+,
\]
because \(p\cdot\eta\le0\) gives exponential damping in
\(\exp(i p\cdot z)=\exp(i p\cdot\xi+p\cdot\eta)\).

## Manuscript Changes

- In Volume IV Chapter 2, inserted the ordered Euclidean-time map
  \(z^0=-i\tau=t-i\epsilon\) immediately after the OS boundary-value
  prescription.
- Rewrote the OS Lorentzian boundary-value package so the forward tube is
  stated as \(z_j-z_{j+1}=\xi_j-i\eta_j\), equivalently
  \(-\operatorname{Im}(z_j-z_{j+1})\in V_+^\circ\).
- Corrected the polynomial tube-estimate statements and consequence proof to
  use the tube depth \(\eta\), rather than the literal imaginary variable.
- Clarified the application of the abstract Fourier--Laplace theorem:
  its variable is \(x+i y\) with \(p\cdot y>0\), while the physical
  Wightman tube has \(y=-\eta\).

## Calculation Check

Added `calculation-checks/os_tube_sign_checks.py`, which verifies:

- \(p\cdot\eta<0\) for sampled future timelike \(p,\eta\) in mostly-plus
  signature;
- ordered Euclidean times \(\epsilon_1>\epsilon_2\) give future tube depth
  \(\epsilon_1-\epsilon_2\) and literal imaginary part
  \(-(\epsilon_1-\epsilon_2)\);
- the abstract cone variable \(y=-\eta\) has positive pairing with the
  spectral cone.

## Verification

Targeted commands run in this pass:

- `tools/run_calculation_checks.sh --list --only os_tube_sign --skip-wolfram`
- `python3 calculation-checks/os_tube_sign_checks.py`

Full structural audits and build are recorded in the commit containing this
note.
