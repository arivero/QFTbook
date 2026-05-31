# Repulsive Sausage Block-Unitarity Wrapper Demotion

Date: 2026-05-31

Scope:

- Volume VI, Chapter 9, `chapter09_on_gross_neveu_sigma_model_families.tex`.
- GitHub issue context: #691 semantic theorem/proof-form audit.

Change:

- Demoted the former proposition "Repulsive-sausage strip analyticity and
  block unitarity" to a paragraph-level bootstrap consistency check.
- Preserved the physical-strip denominator analysis and the charge \(Q=2\),
  \(Q=1\), and \(Q=0\) block-unitarity identities.
- Updated the later controlled approximation so it refers to the checks above
  rather than to a proposition.
- Added a theorem-form audit guard so the old title is flagged if reintroduced
  as theorem-family content.

Rationale:

- The calculation verifies explicit hyperbolic-function identities for a
  written meromorphic S-matrix proposal.  It is important convention control,
  especially because it separates bootstrap consistency from constructive
  local-QFT realization, but the proof is not an independent theorem about a
  sigma-model QFT.

Verification planned:

- `python3 calculation-checks/sigma_model_family_checks.py`
- `python3 -m py_compile calculation-checks/sigma_model_family_checks.py tools/audit_theorem_form.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
