# 2026-05-25 Issue #570 BPHZ--Polchinski Proof-Gap Pass

GitHub issue: #570, concerning the proof of the finite-order
BPHZ--Wilsonian/Polchinski matching theorem in
`monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`.

## Manuscript Changes

- Replaced the previously implicit smooth-cutoff low-source identity by a
  precise dichotomy:
  - for a source-independent Wilsonian action, exact low-source preservation
    is proved only under an admissible plateau cutoff and the condition
    \(C_>J=0\);
  - for non-plateau smooth profiles, the manuscript now introduces the exact
    source-dependent Wilsonian action \(L_{\Lambda,J}^{\rm src}\) and states
    that a separate theorem would need source-vertex coordinates or an
    explicit leakage estimate.
- Added Lemma `lem:plateau-low-source-identity`, proving the finite-regulator
  identity \(W_\Lambda^{\rm low}[J]=W_{\Lambda_0}[J]\) from Gaussian
  convolution and the vanishing of
  \(\langle J,C_>J\rangle\) on the plateau-supported source space.
- Defined the low 1PI object as the Legendre transform after restriction of
  the connected functional to the finite low-source space \(\mathcal E_<\);
  the text now explicitly avoids identifying it with the restriction of a
  full Legendre transform.
- Strengthened Theorem `thm:finite-order-bphz-wilsonian-matching` by adding:
  - the plateau-cutoff and low-source support hypotheses;
  - the tuned Polchinski-flow counterterm trajectory for
    \(\Lambda_0\to\infty\);
  - the perturbative or model-specific status of the bounded-chart
    hypothesis, especially for non-asymptotically-free scalar examples.
- Added Lemma `lem:bphz-commutes-with-wilsonian-vertex-split`, proving that
  the BPHZ forest operation commutes with the retained/omitted Wilsonian
  vertex decomposition
  \(L_\Lambda=L_\Lambda^{(N)}+v_{\perp,N}\), provided the Wilsonian norm
  bounds include the resulting Taylor-subtracted kernels.
- Updated the comparison corollary and status remarks so the proved statement
  is only the fixed-loop, massive, nonexceptional, finite-projector,
  plateau-cutoff, tuned-trajectory theorem.  No nonperturbative BPHZ
  construction or generic continuum QFT existence theorem is claimed.

## Issue-Gap Accounting

- Gap A: closed by the plateau lemma and by removing the exact
  source-independent claim for non-plateau smooth cutoffs.
- Gap B: closed in the theorem statement and proof by requiring a tuned
  Polchinski-flow counterterm trajectory.
- Gap C: closed by using the now-proved Chapter 9 BPHZ theorem
  `thm:bphz-finiteness-massive-euclidean-scalar`, with Hepp-sector
  Taylor-remainder estimates.
- Gap D: closed by making the bounded-chart hypothesis explicitly
  perturbative order by order, or nonperturbative only when the relevant norm
  bounds are proved for the trajectory.
- Gap E: closed by the new forest-linearity lemma.
- Gap F: closed by replacing the ambiguous "supported below Lambda" condition
  with support strictly inside the plateau; non-plateau profiles are excluded
  from this theorem unless a leakage theorem is added.

## Verification

Completed after the manuscript and dossier edits:

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; PDF rebuilt at
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 1251 pages, letter paper, PDF 1.5.
