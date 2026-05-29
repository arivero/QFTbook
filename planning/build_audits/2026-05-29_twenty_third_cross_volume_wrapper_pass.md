# Twenty-Third Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue #691 by reading another cross-volume batch of short or cue-heavy
theorem-family proofs as complete statement-proof units.  This pass focused on
items whose proofs were finite matrix algebra, local Taylor expansion,
Gaussian completing-the-square, or representation-coordinate bookkeeping.

## Demoted From Theorem-Family Form

- `Crossing matrices in the \(\pi\pi\) isospin basis` is now a worked
  normalization paragraph.  The content is the change of basis
  \(C=MPM^{-1}\) from scalar-amplitude coordinates to Roy-coordinate isospin
  amplitudes.
- `Stability of the multi-charge diffusion matrix` is now a linear-algebra
  paragraph.  The physical hypotheses remain explicit: positive static
  susceptibility and positive semidefinite dissipative conductivity.
- `Mean-zero source at one loop` is now part of the background-field
  construction.  The calculation is Gaussian completing-the-square after the
  Legendre source has been introduced.
- `Ising genus-one invariant` is now a finite modular-matrix calculation
  inside the rational-genus-one discussion.  The higher sewing problem remains
  separated from this finite check.
- `Rephasing invariance of \(J_{\rm CKM}\)` is now a flavor-coordinate
  paragraph.  The phase cancellation and row/column-orthogonality argument are
  preserved without presenting them as a theorem.
- `Coefficient preservation by the truncated conformal map` is now a
  Borel--Leroy approximation paragraph.  The theorem-level input remains
  Watson's lemma and the analytic growth hypotheses; the local statement is a
  Taylor-coordinate calculation.
- `Free scalar tree-level cutoff expansion` is now a worked tree-level
  Symanzik expansion.  The distributional remainder estimate is retained.
- `Perturbative center-broken minima in pure Yang--Mills` is now a worked
  Weiss-potential paragraph.  The assumptions remain visible: one-loop
  perturbative high-temperature potential and pure \(SU(N_c)\) holonomy.

## Retained After Reading

The following candidates were read in this pass or in the immediately
preceding queue refresh and retained in theorem-family form for now:
Fredholm expansion for trace-class kernels, transfer-matrix commutativity from
RTT, the largest-time identity, K-S positive-energy cylinder construction,
Coulomb-slice atlas, McKean--Singer identity, Lichnerowicz formula,
Feshbach--Schur reduction with resolvent control, finite Grassmann
reflection-positivity, and positive-energy Witten-index pairing.  Their proofs
perform a reusable construction, invoke a genuine analytic theorem, or supply a
load-bearing mechanism rather than merely substituting a convention.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 594.
- Proof environments: 589.
- Local regenerated broad short/cue-heavy queue: 128 candidates, split as
  12 score-three and 116 score-two items under the current heuristic.  This is
  a reading queue rather than a defect count.

## Verification

- Stale-label scan for the eight removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `git diff --check`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 2579 pages.
