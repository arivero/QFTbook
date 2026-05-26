# 2026-05-25 Issue 580: OS Reconstruction Proof Stack

## Scope

Issue #580 flagged QFT-specific steps in the OS reconstruction chapter that
were too compressed: boundary values from the corrected OS-II analytic input,
locality from Euclidean permutation symmetry, recovery of Schwinger functions,
semigroup self-adjointness, field-domain closability, uniqueness, and the
failure mode of the first OS reconstruction theorem.

## Edits

- Strengthened the Klein--Landau failure-mode remark by citing the path-space
  semigroup work and spelling out that the missing point is bounded and
  strongly continuous positive-time translation on the OS quotient.
- Added a Fourier--Laplace boundary-value proposition proving that spectral
  support in a cone plus finite distributional order produces holomorphic tube
  functions with polynomial tempered bounds and tempered boundary values.
- Clarified how the OS-II linear-growth estimate enters reconstruction: it is
  the Euclidean-side analytic estimate controlling distributional order, while
  spectral support comes from the positive-energy translation representation
  and the continued Lorentz transformations.
- Expanded the edge-of-the-wedge proof by defining the Jost-point condition,
  explaining how adjacent spacelike-separated orderings meet at the real edge,
  and deriving smeared local graded commutativity on the dense OS domain.
- Expanded the reverse-continuation argument using uniqueness in the connected
  ordered tube and noting explicitly that contact-term extensions on diagonals
  are not recovered from off-diagonal analytic continuation.
- Added a chapter dossier for Volume IV Chapter 2 with notation inventory,
  claim ledger, figure ledger, and audit note.

## Targeted Verification

No calculation script was edited for this functional-analytic proof pass.

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The monograph build and log scan completed cleanly.  The rebuilt PDF has
1289 pages.
