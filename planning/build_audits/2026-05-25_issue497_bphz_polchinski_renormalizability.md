# 2026-05-25 Issue #497 BPHZ--Polchinski Renormalizability Pass

GitHub issue: #497, deriving the relation between BPHZ forest-formula
renormalizability and Polchinski-style Wilsonian renormalizability.

## Manuscript Change

Volume II, Chapter 16 already contained the deep-proof replacement for the
old structural comparison: the comparison datum, the BPHZ-local-parts
proposition, the Wilsonian Taylor-remainder lemma, the finite-order matching
theorem, the low-mode Legendre-transform proof, and the recursive coordinate
map.

This pass adds a corollary that states the actual renormalizability
comparison:

- BPHZ renormalizability means finite projected 1PI coordinates after a
  specified massive forest formula, with finite local Taylor subtraction
  freedom.
- Polchinski-Wilsonian renormalizability means finite relevant/marginal
  Wilsonian local coordinates plus an irrelevant remainder controlled in the
  declared Wilsonian norm.
- The two criteria are equivalent only in the theorem's fixed-loop, massive,
  nonexceptional, finite-projector setting, up to the displayed
  \((\mu/\Lambda)^{p_N}\) error from omitted irrelevant coordinates.
- The proof goes in both directions and constructs the coordinate assignment
  from BPHZ local Taylor parts to Wilsonian local vertices, and from Wilsonian
  low-mode 1PI projectors back to BPHZ subtraction coordinates.

## Boundary

The corollary explicitly does not assert nonperturbative equivalence of BPHZ
and Wilsonian constructions.  Such a statement would require model-specific
existence of the measures or functionals, cutoff-uniform Banach estimates,
and the relevant Legendre transforms.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean final log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1239 pages.
