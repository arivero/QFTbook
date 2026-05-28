# 2026-05-28 Issue #639 Body Figure Callout Pass

Scope: monograph-wide labeled figure integration.

Actions:
- Added body-text callouts for all previously unreferenced labeled figure environments.
- Preserved the existing figure environments and captions; the pass integrates each figure into the surrounding derivation or definition.
- Tightened two long callout paragraphs after the build log reported overfull boxes.

Verification:
- `tools/audit_figures.py`
  - figure environments: 164
  - figure labels: 164
  - figure labels referenced from body text: 164
  - unreferenced labeled figures: 0
  - missing labels: 0
  - duplicate labels: 0
- `git diff --check`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_theorem_form.py`
- `tools/build_monograph.sh`
  - clean final log scan
  - regenerated `monograph/tex/main.pdf` at 2376 pages

Remaining issue #639 work:
- The audit still reports 85 inline TikZ diagrams outside figure environments.
- Those diagrams require a separate review pass because some may be small inline mathematical graphics, while others may deserve promoted figure environments with captions and labels.
