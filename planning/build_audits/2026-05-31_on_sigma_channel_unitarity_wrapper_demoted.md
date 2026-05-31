# O(N) Sigma-Model Channel Unitarity Wrapper Demotion

Date: 2026-05-31

Scope:

- Volume VI, Chapter 9, `chapter09_on_gross_neveu_sigma_model_families.tex`.
- GitHub issue context: #691 semantic theorem/proof-form audit.

Change:

- Demoted the former proposition "Channel unitarity and crossing" to a
  paragraph-level normalization check.
- Preserved the singlet, symmetric-traceless, and antisymmetric channel
  eigenvalues; the unitarity equations; the crossing relations; the projector
  decomposition; and the gamma-function recurrence calculation.
- Reworded the prose to say explicitly that this is a check of the displayed
  meromorphic \(O(N)\)-invariant S-matrix tensor, not an independent
  structural theorem about the sigma-model QFT.
- Updated the chapter dossier and added a theorem-form audit guard so the old
  title is flagged if reintroduced.

Verification planned:

- `python3 calculation-checks/on_sigma_gn_checks.py`
- `python3 -m py_compile calculation-checks/on_sigma_gn_checks.py tools/audit_theorem_form.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
