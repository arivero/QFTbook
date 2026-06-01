# 2026-06-01 Moore-Seiberg Defect-Junction Pass

## Scope

This pass addresses the remaining Volume V CFT depth concern that the
Moore--Seiberg system was previously named rather than developed at the point
where rational sewing and Verlinde data are introduced.

## Manuscript Changes

- Added `Moore--Seiberg Data as Defect-Junction Consistency` to
  `volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`.
- Defined the fusion spaces \(V_{ij}^{k}\) as junction spaces for topological
  lines labelled by chiral sectors.
- Displayed the \(F\)-move as the change of basis between the two four-point
  pants decompositions.
- Stated the associator pentagon, braiding hexagon, and balancing identity as
  equalities of maps in the semisimple defect category.
- Cross-linked the discussion to the Volume IX physical defect-category null
  quotient, so the Moore--Seiberg equations are treated as QFT defect-network
  consistency conditions with the analytic QFT construction boundary made
  explicit.

## Status

No new theorem was introduced.  The pass is a structural and logical
development: the analytic construction of Hilbert spaces, positive pairings,
correlation functions, and sewing maps remains the real theorem boundary.

## Verification

Clean in this pass:

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/build_monograph.sh`

The rebuilt manuscript is `monograph/tex/main.pdf`, 2798 pages.
