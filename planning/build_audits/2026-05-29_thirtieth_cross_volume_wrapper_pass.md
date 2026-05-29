# 2026-05-29 Thirtieth Cross-Volume Wrapper Pass

## Scope

This pass continues GitHub issue #691.  The audit read theorem-family
statements together with their proof environments and removed wrappers where
the proof was only a local calculation, a direct use of a definition, or a
composition of assumptions.  The derivations were retained in the manuscript
as prose calculations so the mathematical content remains visible without a
false theorem/proposition signal.

## Demotions

Eighteen theorem-family wrappers were demoted in this batch:

- Volume I, Chapter 12: spectral-filter phase cancellation for the
  Haag--Ruelle one-particle vector.
- Volume I, Chapter 12: unitarity and matrix elements of the scattering
  operator as a Hilbert-space consequence of the wave-operator definition.
- Volume I, Chapter 15: massive spin labels from the covering group.
- Volume II, Chapter 13: stress-tensor criterion for conformal currents.
- Volume II, Chapter 17: low-velocity monopole dynamics from the
  moduli-space kinetic substitution.
- Volume III, Chapter 1: virial-improvement calculation for conformal
  currents.
- Volume III, Chapter 2: conformal current from a traceless stress tensor.
- Volume III, Chapter 3: Weyl covariance of the conformal Laplacian.
- Volume III, Chapter 4: free-fermion short-module letter character.
- Volume III, Chapter 5: cylinder conformal charges and radial adjointness.
- Volume III, Chapter 8: spinning two-point tensor structures.
- Volume V, Chapter 11: symmetric-product torus partition function.
- Volume VII, Chapter 1: on-shell particle multiplets.
- Volume VII, Chapter 1: massive \(\mathcal N=1\) oscillator module.
- Volume VII, Chapter 1: massless \(\mathcal N=1\) helicity pair.
- Volume VII, Chapter 7: rigid special-K\"ahler metric from the prepotential.
- Volume VII, Chapter 13: scalar crossing monodromy cocycle.
- Volume XI, Chapter 7: Gaussian linearization in hierarchical Wick
  coordinates.

The theorem-form audit guardrail was extended with these titles so future
reintroductions of the same decorative wrapper pattern are flagged.

## Retained After Reading

Several short proof environments were read but retained because the statement
is a genuine domain lemma, a nontrivial estimate, or a compact statement whose
proof is short only because substantial hypotheses and definitions have already
been set up:

- Dijkgraaf--Witten triangulation independence of the cocycle weight.
- Finite Grassmann reflection-positivity criterion.
- Fredholm expansion and canonical coefficients.
- Entropy production and positivity of first-order hydrodynamic transport.
- Exact bosonized local gauge sector of the Schwinger model.
- Associativity and commutator in perturbative algebraic QFT.
- BV pushforward statements with boundary or QME hypotheses.
- Rindler normal form and Lichnerowicz formula.
- Trace-class one-channel sewing estimate.
- Leading Hadamard transport equation.
- Isolated spectral atom and first-sheet pole.
- Causal support of the Bogoliubov field.
- Nelson-stability \(L^q\) density bounds.
- Endpoint finite-part and endpoint-exponent analysis in large-\(N\) two
  dimensional QCD.

## Counts

After the demotions in this batch:

- theorem environments: 97
- proposition environments: 393
- lemma environments: 29
- corollary environments: 10
- proof environments: 524
- total theorem-family environments: 529

The present estimate is that roughly 8--15 high-confidence weak wrappers remain
and that a deeper second pass may expose another 15--25 borderline cases where
substance is hidden in assumptions rather than in the named statement.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- stale-label scan for all removed labels in this batch
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` returned `Pages: 2581`
