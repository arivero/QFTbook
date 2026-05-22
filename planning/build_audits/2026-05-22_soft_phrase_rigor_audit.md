# Soft Phrase Rigor Audit

Date: 2026-05-22

Scope:
- End-to-end manuscript audit for prose that hid assumptions, domains, proof status, or normalization behind soft phrases.

Searches hardened:
- Removed reader-facing occurrences of weak shortcuts matching:
  `usual`, `usually`, `well-known`, `well known`, `one can show`, `one may show`, `it is known`, `schematically`, `formal expression`, `formal expansion`, `formal parameter`, `compact formal`, `formal Lorentzian`, and `formal same-line`.
- Remaining uses of fixed mathematical names such as standard boost or standard representation were left untouched when already defined by local convention.

Main repairs:
- Replaced vague theorem hypotheses with explicit data in the spin-statistics, DHR, Haag--Ruelle, Ising fixed-point, and QCD infrared discussions.
- Reclassified path-integral and perturbative shorthand as regulated, coefficientwise, or distributional statements.
- Clarified generalized kets as distributional coordinate functionals in a rigged-Hilbert/direct-integral setting.
- Replaced informal delta-normalized and contour-pole statements with distributional or denominator-level formulations.
- Added a Soft Phrase Audit Rule to the strict writing harness.

Verification:
- `rg` scan for the weak-claim patterns listed above returned no reader-facing manuscript matches.
- `git diff --check` passed.
- `tools/build_monograph.sh` completed cleanly and produced `monograph/tex/main.pdf`.

Residual risk:
- This pass removes one class of weak prose signals.  It does not certify every theorem, derivation, and figure in the manuscript; the next passes should continue chapter-by-chapter claim and notation ledgers.
