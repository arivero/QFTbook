# Finite Pfaffian Orientation Model Pass

Date: 2026-05-31.

Scope:
- Volume XII, Chapter 7, Pfaffian-line and mod-two-index discussion.
- GitHub issue context: #696 anomaly quoted-theorem proof debt.

Changes:
- Added a finite real skew-block model for the Pfaffian line before the
  Witten \(SU(2)\) global-anomaly theorem boundary.
- The new text defines \(q_a=a\,e^1\wedge e^2\), records
  \(\operatorname{pf}(q_a)=a\) and \(\det(q_a)=a^2\), and explains how a
  single block crossing changes the orientation of the real Pfaffian line.
- For direct sums of blocks, the text derives
  \(\operatorname{pf}(\oplus_r q_{a_r})=\prod_r a_r\), making the holonomy
  sign the parity of block sign crossings.  This isolates the finite
  orientation mechanism from the quoted infinite-dimensional elliptic
  mod-two-index theorem.

Companion checks:
- Extended `calculation-checks/eta_global_anomaly_checks.py` with exact
  finite Pfaffian checks: Pfaffian-square versus determinant product,
  crossing-parity sign change, and direct-sum multiplicativity.
- Updated the calculation-check README and the Volume XII Chapter 7 dossier.

Verification:
- `python3 calculation-checks/eta_global_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/eta_global_anomaly_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh` completed cleanly; `main.pdf` rebuilt at 2750 pages.
