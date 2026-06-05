# Issue #755/#597 instanton slot asymptotics clarity pass

Date: 2026-06-05.

Scope:

- Chapter: Volume II, Chapter 20, BPST instanton / semiclassical vertex.
- Local target: proof of
  `prop:instanton-individual-zero-mode-form-factor`.
- Companion evidence already present:
  `check_instanton_zero_mode_tail_local_limit()` in
  `calculation-checks/bpst_instanton_normalization_checks.py`.

Substance audit:

- This is a coherence and editorial-precision repair, not a new local
  infrastructure lemma.
- The later hard four-slot instanton endpoint estimates use the coefficient
  `F_zm(t)=3/(4t^3)+O(t^(-5))`.
- The monograph previously appealed to standard large-`t` Bessel asymptotics
  at exactly that load-bearing point.  The text now displays the product
  expansions for `I0 K1`, `I1 K0`, and `I1 K1`, then shows the cancellation of
  the `t^(-1)` terms and the surviving `3/(4t^3)` coefficient.

Quality boundary:

- This pass supports the user concern about coherence drift in heavily touched
  chapters: it makes a later endpoint-control claim reproducible at the point
  where its coefficient is introduced.
- It does not claim to close #597 or #755.  The larger instanton program still
  needs additional determinant/source/amplitude work, and #755 remains a
  manuscript-wide exposition audit.

Verification completed:

- Full Python calculation suite.
- BPST instanton companion check.
- Focused Chapter 20 theorem/display/negative-scope/style audits.
- Chapter dossier and monograph text audits.
- Calculation-check inventory and evidence-contract audits.
- Process-metadata leak scan on the touched TeX/check files.
- Full monograph build and log scan.
