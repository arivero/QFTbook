# Issue 495 Subtracted Cauchy Transform Pass

## Scope

- GitHub issue: #495, polynomial boundedness from Wightman axioms where
  possible.
- Branch: `main`.
- Files edited:
  - `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`
  - `planning/chapter_dossiers/volume_ii/chapter07_partial_waves_dispersion_froissart.md`

## Substantive Change

This pass adds the elementary analytic step that was missing between the
already-proved distributional temperedness statement and the pointwise
polynomial estimates used in fixed-\(t\) dispersion theory.

For a tempered cut distribution \(T\in\mathcal S'(\mathbb R)\) with finite
Schwartz-seminorm order \((r_T,N_T)\), and a subtraction number \(q>N_T\), the
chapter now proves that the subtracted Cauchy transform
\[
  \left\langle T(\sigma),
  \frac{(z-z_0)^q}{(\sigma-z)(\sigma-z_0)^q}
  \right\rangle
\]
is holomorphic off the cut and obeys
\[
  |F_q(z)|\le C(1+|z|)^q|\operatorname{Im}z|^{-r_T-1}.
\]
Consequently, a fixed-\(t\) amplitude with pole terms removed is pointwise
polynomially bounded on fixed contours away from the cuts whenever it admits
a finite-subtraction Cauchy representation with tempered cut distributions.

## Logical Boundary

This does not close #495.  The added proposition proves the non-QFT-specific
complex-analysis bridge.  The remaining Jin--Martin proof layer is a
monograph proof obligation: construct the fixed-\(t\) first-sheet domain and
finite-subtraction representation from locality, the spectrum condition,
LSZ pole separation, and the Jost--Lehmann--Dyson/Bros--Epstein--Glaser
analytic machinery.  The chapter now records the pieces of this domain proof
stack explicitly so they are not treated as permanent citation boundaries.

## Verification Plan

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

## Verification Results

- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed after shortening an overlong theorem
  title; monograph build and log scan are clean.
- `pdfinfo monograph/tex/main.pdf`: `Pages: 1951`, `File size: 7802943
  bytes`, `CreationDate: Tue May 26 22:59:46 2026 EDT`.
