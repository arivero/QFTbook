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
- A later clarification pass added an explicit "What is, and is not, proved"
  remark immediately after the proof, so the reader cannot confuse the
  fixed-loop finite-coordinate theorem with a theorem about existence of a
  nonperturbative continuum QFT whose perturbative expansion is the BPHZ
  series.

## Boundary

BPHZ is perturbative by definition.  The corollary therefore does not assert
a nonperturbative equivalence involving a nonexistent nonperturbative BPHZ
construction.  The separate nonperturbative question is whether a Wilsonian
or constructive continuum theory exists and has the BPHZ-renormalized series
as its perturbative asymptotic expansion in the chosen local coordinates;
that question requires model-specific existence of the measures or
functionals, cutoff-uniform Banach estimates, and the relevant Legendre
transforms.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean final log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1239 pages.
