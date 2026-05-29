# Twenty-Fourth Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue #691 by reading another batch of short or cue-heavy theorem-family
items as complete statement-proof units.  This pass focused on algebraic
coordinate checks whose assumptions carry the real content: ansatz-level
Seiberg--Witten curve selection, scalar-factor convention algebra, Mellin
prefactor bookkeeping, Standard Model charge bookkeeping, finite-dimensional
spectroscopy coordinate changes, and reflection-positivity coefficient
checks.

## Demoted From Theorem-Family Form

- `Minimal rank-one curve inside the two-singularity ansatz` is now an
  ansatz-bound paragraph.  The text still makes the strong hypotheses
  explicit and states that the QFT assertion lies at the Seiberg--Witten
  status boundary.
- `Matrix-channel origin of the scalar crossing multiplier` is now a worked
  scalar-factor convention paragraph.  The calculation remains, and the text
  still says that it does not construct the analytic crossed scalar branch.
- `Compatibility with the four-point prefactor` is now Mellin-coordinate
  bookkeeping.  The exponent matching and gamma-factor substitution remain in
  the text.
- `Gauge invariance of the minimal Yukawa sector` is now a charge and
  representation bookkeeping paragraph in the Standard Model hybrid chapter.
- `Velocity-labelled flux sectors` is now a boosted-Coulomb flux paragraph.
  The angular integral and velocity reconstruction remain visible.
- `Wilson mid-link positivity at \(r=1\)` is now a Wilson-fermion crossing
  factor paragraph; the finite Grassmann reflection-positivity criterion
  remains the actual proposition.
- `Basis covariance of finite-volume spectral extraction` is now a GEVP
  source-coordinate paragraph.  The distinction between invariant energies and
  chart-dependent overlap fractions remains explicit.
- `\(SU(2)\) Wilson character coefficients` is now a character-coefficient
  calculation paragraph.  The Bessel identity and positivity check remain
  paired with the calculation-check script.

## Retained After Reading

The massive \(\mathcal N=1\) oscillator module was read and retained: although
the proof is elementary Clifford-module representation theory, the statement
is a load-bearing distinction between Hilbert-space particle multiplets and
off-shell field multiplets.  The topological monopole lower bound,
finite-Grassmann reflection-positivity criterion, K-S positive-energy
cylinder, and trace-class/Fredholm machinery also remain theorem-family items
for now because their proofs provide reusable structures rather than just
coordinate substitutions.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 586.
- Proof environments: 581.
- Local regenerated broad short/cue-heavy queue: 127 candidates, split as
  12 score-three and 115 score-two items under the current heuristic.  This is
  a reading queue rather than a defect count.

## Verification

- Stale-label scan for the eight removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 2579 pages.
