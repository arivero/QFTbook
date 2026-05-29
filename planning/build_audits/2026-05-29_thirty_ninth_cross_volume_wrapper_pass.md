# Thirty-Ninth Cross-Volume Anti-Wrapper Pass

Date: 2026-05-29.

Issue context: continuing GitHub issue #691 and the cross-cutting
assertion-vs-derivation concern in #562.  This pass moved beyond the shortest
proof queue and targeted theorem-family statements whose hypotheses already
contained most of the claimed content.

## Demotions

Three proposition/proof wrappers were demoted to controlled-approximation
or scope statements.  In each case the mathematical content was retained, but
the theorem-family packaging was removed.

1. `prop:observable-type-threshold-preservation` in Volume VII, Chapter 7b.
   The former proposition is now
   `ca:observable-type-threshold-comparison`.  The text states the required
   Wilsonian/common-regulator, low-momentum, gap, and fixed line-lattice data,
   then explains what is actually transported across the threshold:
   holomorphic local coordinates, derivative-expanded nonchiral Wilsonian
   coordinates, and declared line-charge labels.  Spectral masses, string
   tensions, and line-defect excitation energies are separated as dynamical
   spectral problems rather than proposition-level consequences.

2. `prop:sm-stu-domain` in Volume II, Chapter 19c.  The former proposition is
   now `ca:sm-stu-domain`.  The \(S,T,U\) discussion is framed as a restricted
   two-point projection: analytic transverse self-energies, retention only of
   constant and first-derivative Taylor data at \(q^2=0\), and fixed
   \(\alpha_{\rm em}\), \(G_F\), and \(m_Z\) input coordinates.  The text now
   emphasizes that nonanalytic thresholds, detector functionals, vertex
   corrections, box corrections, and independent four-fermion operators are
   additional coordinates outside this projection.

3. `prop:lattice-strong-coupling-area-law` in Volume IX, Chapter 4.  The
   former proposition is now `ca:lattice-strong-coupling-area-law`.  The
   statement no longer pretends to prove an area law from estimates that
   already contain exponential lower/upper bounds.  It records the controlled
   lattice strong-coupling mechanism and states that theorem status begins
   only after the polymer estimates are proved for the chosen lattice action.

The reference in the oblique-confinement diagnostic section was updated from
`Proposition~\ref{prop:lattice-strong-coupling-area-law}` to the controlled
estimate `\ref{ca:lattice-strong-coupling-area-law}`.

## Guardrails

`tools/audit_theorem_form.py` now rejects theorem-family reintroduction of
the three demoted titles:

- `Observable-type preservation under a controlled threshold`
- `Domain of the \(S,T,U\) projection`
- `Strong-coupling area mechanism`

## Read And Retained

I also read nearby cue-heavy candidates before editing:

- `prop:relation-of-mass-notions` is retained because it distinguishes
  spectral pole mass, finite 1PI subtraction coordinates, MS running
  coordinates, and lattice gap scaling in one place; the proof connects a
  Kallen--Lehmann atom, the finite inverse propagator, and OS/lattice
  transfer-matrix interpretation.
- `cor:fixed-loop-bphz-polchinski-renormalizability` is retained because it
  is the fixed-loop comparison theorem requested in the BPHZ/Polchinski
  discussion, with explicit finite-order matching hypotheses and a recursive
  proof.
- `prop:auxiliary-pushforward-momentum-trace` is retained because it is a
  distributional pushforward/trace lemma needed for Dyson analyticity, not a
  formal algebraic substitution.
- `prop:finite-codimension-critical-surface` is retained because it makes the
  stable-manifold theorem operational in microscopic parameter coordinates;
  the proof is a Banach-submersion/implicit-function argument.
- `prop:haag-ruelle-cook-limits` is retained as a Cook criterion.  The
  proposition explicitly isolates the analytic estimates needed for
  Haag--Ruelle limits, and the following paragraphs identify the locality and
  spectral-isolation estimates that supply those hypotheses in the full
  theorem.

## Current Counts

After this pass:

- theorem environments: 94
- proposition environments: 364
- lemma environments: 29
- corollary environments: 10
- theorem-family total: 497
- proof environments: 492

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` gives 2592 pages.
