# 2026-05-26 DPD Besov Product-Continuity Audit

## Scope

This pass develops the rough enhanced-noise product-continuity theorem for
the Da Prato--Debussche nonlinearity in
`monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.

## Mathematical Content

- Added Proposition `prop:spde-dpd-besov-product-continuity`.
- The proposition defines
  \(\mathcal C^\gamma=B^\gamma_{\infty,\infty}\) by a fixed dyadic
  Littlewood-Paley partition and states the canonical Bony product maps
  \[
    \mathcal C^\alpha\times\mathcal C^{-\kappa}\to
    \mathcal C^{-\kappa},
    \qquad
    \mathcal C^\alpha\times\mathcal C^\alpha\to\mathcal C^\alpha
  \]
  under \(0<\kappa<\alpha\).
- The proof derives the left paraproduct, right paraproduct, and resonant
  estimates directly from dyadic support geometry.  The resonant estimate
  uses precisely the summability condition \(\alpha-\kappa>0\).
- The proposition applies those bilinear bounds to prove local Lipschitz
  continuity of
  \(Y^3+3Y^2X_1+3YX_2+X_3\) as a map to
  \(C([0,T];\mathcal C^{-\kappa})\).
- The statement is careful about the full
  \(B_{\infty,\infty}\) space: Bony's formula gives the canonical product,
  rather than relying on a false density statement for smooth functions.
- The smooth-to-rough DPD roadmap now cites this proposition instead of an
  unnamed product-continuity theorem.
- The calculation-check companion verifies sample resonance, embedding,
  algebra, and DPD target-regularity arithmetic.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1533 pages.
- Log scan for LaTeX warnings, undefined control sequences, fatal errors,
  emergency stops, overfull boxes, and underfull boxes found no matches.
