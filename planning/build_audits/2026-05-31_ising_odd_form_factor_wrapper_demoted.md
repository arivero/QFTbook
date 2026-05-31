# Ising Odd Form-Factor Wrapper Demotion

Date: 2026-05-31

GitHub issue: #691, anti-wrapper proof-substance audit.

## Scope

Volume VI, Chapter 4 contains the free Majorana / Ising form-factor examples.
The odd product family
\[
  F_{2k+1}^{\Sigma}=v\,i^k\prod_{i<j}\tanh((\theta_i-\theta_j)/2)
\]
is an important convention check: it fixes Watson exchange, odd cyclicity, and
the kinematic-residue sign for the product ansatz.

## Change

The statement titled `Ising odd form-factor family` was demoted from
proposition/proof form to an ordinary verification paragraph.  Its mathematical
content was preserved: the chapter still checks antisymmetry, \(2\pi i\)
periodicity, the spectator-pair cancellation at the annihilation pole, and the
\(i^k\) phase needed for the residue equation.

This is a finite algebraic verification of an explicit ansatz, whereas the
nearby separated Euclidean spectral-series convergence statement remains in
proposition form because it proves a genuine analytic reconstruction property.

## Harness

`tools/audit_theorem_form.py` now rejects `Ising odd form-factor family` if it
is reintroduced as a theorem-family title.
