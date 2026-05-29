# Twenty-Sixth Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue #691 by reading another high-signal subset of the theorem/proof queue
after the twenty-fifth pass.  This pass separated two failure modes: theorem
wrappers around calculations, and theorem statements whose hypotheses were too
thin to carry the advertised conclusion.

## Demoted From Theorem-Family Form

- `Wick graph expansion and connected cumulants` is now a fixed-regulator
  Wick-expansion paragraph.  Wick pairings, denominator cancellation, and
  connected-component selection remain explicit.
- `Cone structure and the small-instanton boundary` is now an ADHM
  coordinate-calculation paragraph.  The radial density
  \(\rho^{4N_c-5}\dd\rho\,\dd\Omega_{N_c}\) and the \(\rho=0\) degeneration
  remain.
- `One-loop running factor in the one-instanton density` is now a
  running-factor calculation paragraph.  The universal \((\mu\rho)^{b_0}\)
  dependence remains separated from the scheme-dependent determinant constant.
- `Polyakov--Wiegmann identity in the chapter normalization` is now a
  normalization calculation paragraph in the integrable sigma-model chapter.
- `One-loop planar \(SU(2)\) Hamiltonian` is now a planar one-loop Hamiltonian
  calculation paragraph.  This avoids presenting the current coefficient
  fixing, which invokes the adjacent exchange integral, as a fully independent
  theorem.

## Strengthened In Theorem-Family Form

- `Strong-coupling area mechanism` remains a proposition, but its hypotheses
  now state the actual area estimates: no smaller center-sensitive surfaces,
  a nonzero minimal-area sum with lower exponential bound, and an exponentially
  smaller bound on larger decorated surfaces.  The proof now derives the upper
  and lower exponential area bounds from these estimates and explicitly says
  that the exact string tension requires the full convergent polymer sum.

## Retained After Reading

The finite Grassmann reflection-positivity criterion, transfer-matrix
commutativity, K-S positive-energy cylinder, cutoff-limit invariance criterion,
integrated nonsinglet axial Ward identity, Fredholm expansion, largest-time
identity, Lichnerowicz formula, Coulomb-slice atlas, BV Stokes restriction,
monopole lower bound, PCT modular corollary, conformal Laplacian covariance,
and Chern--Simons Polyakov--Wiegmann lemma remain theorem-family candidates
for now.  They are short because the surrounding setup carries much of the
notation, but they supply reusable positivity, representation, functional
analytic, microlocal, gauge-slice, or geometric machinery.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 569.
- Proof environments: 564.
- Strict regenerated high-signal short/cue-heavy queue: 15 candidates.  This
  queue is now mostly structural compact proofs, but it remains a reading queue
  rather than a completion certificate.

## Verification

- Stale-label scan for the five removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 2579 pages.
