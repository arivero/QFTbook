# Issue #641 Negative-Scope Prose Sweep

## Scope

Addressed GitHub issue #641, which identified the recurring prose pattern in
which a paragraph states a datum and then follows with a corrective sentence of
the form "This is not ..." or "X is not a substitute for Y."  The correction
does useful scope work, but the wording makes the scope appear as an
afterthought.  This pass rewrites the targeted forms as direct positive scope
statements throughout the compiled TeX volumes.

## Manuscript Changes

- Replaced all occurrences of the targeted issue patterns:
  `This is not`, `It is not, by itself`, `should not be read/confused`,
  `not be confused with`, `not a substitute`, `not merely`, `not cosmetic`,
  and `not a choice of notation`.
- Preserved genuinely negative mathematical content where needed by replacing
  rhetorical negation with direct statements of the relevant construction,
  theorem scope, required additional data, or separate existence problem.
- Touched the affected passages across Volumes I through XII, including the
  Wilson--Fisher formal fixed-point status, lattice Yang--Mills scaling,
  gauge-fixing/BRST locality, the hybrid Standard Model datum, radial
  quantization adjoints, charged Haag--Ruelle status, logarithmic CFT,
  supersymmetric localization, anomaly inflow, thermal QCD, constructive RG,
  stochastic quantization, and curved-spacetime examples.

## Harness

- Added `tools/audit_negative_scope_prose.py`, a narrow audit for the exact
  backward-corrective phrase family identified in the issue.
- Added the audit to `tools/build_monograph.sh`.
- Added the Positive Scope Prose Rule to
  `planning/12_strict_writing_harness.md`.

## Verification

- `tools/audit_negative_scope_prose.py`
- `rg -n "This is not|this is not|It is not, by itself|it is not, by itself|should not be (confused|read|interpreted)|not be confused with|not a substitute|not merely|not cosmetic|not a choice of notation" monograph/tex/volumes`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_theorem_form.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The full build regenerated `monograph/tex/main.pdf` at 2355 pages and the
final build-log scan was clean.
