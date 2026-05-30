# Boundary Entropy Gradient-Formula Pass

Date: 2026-05-30

## Scope

This pass advances issue #697 for the BCFT proof-debt cluster.  It targets the
boundary \(g\)-theorem paragraph in Volume V, Chapter 14, which previously
hid the analytic content behind the phrase "usual assumptions."

## Changes

- Replaced the old boundary \(g\)-theorem quoted block by the sharper boundary
  entropy gradient formula.
- Defined the renormalized boundary trace equation
  \(\theta=B^a\phi_a+\partial_\tau j\), the quotient by redundant
  total-derivative directions, the finite-temperature boundary entropy
  \(s=(1-L\partial_L)\log z\), and the positive susceptibility metric
  \(G_{ab}\) built from connected boundary two-point functions.
- Derived the monotonicity statement
  \(d s/d\log L=-B^aG_{ab}B^b\le0\), hence \(g_{\rm UV}\ge g_{\rm IR}\) for a
  flow between boundary fixed points.
- Added a mechanism paragraph explaining how the stress-tensor Ward identity,
  coupling differentiation, contact-term subtraction, and reflection positivity
  enter the gradient formula.

## Proof-Form Status

The endpoint inequality is no longer treated as an independent theorem.  It is
a derived consequence of the quoted gradient formula and positivity.  The full
analytic proof of the gradient formula remains a theorem boundary, but its
assumptions and local role are now explicit at the point of use.
