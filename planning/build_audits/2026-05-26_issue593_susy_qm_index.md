# 2026-05-26 Issue #593: Berezin, SUSY QM, and Worldline Index Density

## Scope

Issue #593 asked for the remaining stringbook-related material in the
fermionic path-integral chapter: a functorial formulation of Berezin
integration, a worked supersymmetric quantum-mechanics Witten-index example,
and the periodic-fermion worldline derivation of the Atiyah--Singer density.

## Manuscript Changes

- Added a finite-dimensional Berezin pushforward section to
  `volume_i/chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex`.
- Added supersymmetric quantum mechanics with supercharges
  \(Q,Q^\dagger\), Hamiltonian \(H=\{Q,Q^\dagger\}/2\), positive-spectrum
  pairing, and the harmonic superpotential \(W(x)=mx^2/2\) giving \(I_W=1\).
- Added a worldline index-density calculation for a twisted spin Dirac
  operator, deriving the \(\widehat A(TM)\operatorname{ch}(E)\) density from
  periodic fermions, normal-coordinate expansion, determinant products, and
  fermion zero-mode Berezin integration.

## Calculation Check

Added `calculation-checks/susy_qm_index_checks.py`, which verifies:

- the oscillator supertrace identity
  \(1/(1-q)-q/(1-q)=1\);
- the even-minus-odd zero-mode count for \(W(x)=mx^2/2\);
- the two-variable Berezin Pfaffian extraction;
- the \(\widehat A\)-series
  \((x/2)/\sinh(x/2)=1-x^2/24+7x^4/5760-31x^6/967680+\cdots\).
