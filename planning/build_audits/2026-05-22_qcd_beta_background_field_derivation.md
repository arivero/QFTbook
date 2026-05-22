# 2026-05-22 QCD Beta-Function Repair Audit

## Trigger

The compiled QCD chapter stated the one-loop QCD beta function but did not
transcribe or reconstruct the explicit background-field calculation from the
second-sequence source notes.  The missing calculation is conceptually
important because it computes the gauge-invariant coefficient in the
background 1PI effective action rather than treating the beta function as a
collection of gauge-fixed vertex renormalizations.

## Source Check

- Primary PDF checked: `references/253b lecture notes 2023.pdf`, pages
  182--201.
- Rendered pages inspected: `/private/tmp/qft253b_qcd_beta_pages-182.png`,
  `-183.png`, `-190.png`, `-196.png`, `-197.png`, `-198.png`, `-199.png`,
  `-200.png`.
- Comparison transcription checked:
  `references/253b transcribed lecture notes.tex`, lines around 7306--8057.

## Correction

The comparison transcription contains a coefficient error in the determinant
summary.  The handwritten page gives

\[
  \operatorname{Tr}\log D_{\rm gh}
  \supset
  {1\over 12}\operatorname{tr}_{\rm adj}\widetilde F^2
  {1\over 8\pi^2}{\mu^{-\epsilon}\over\epsilon},
\]

not \(1/2\).  With the vector determinant coefficient \(-5/3\) and the
bosonic factor \(-1/2\), the pure-gauge contribution is

\[
  -{1\over2}\left(-{5\over3}\right)+{1\over12}
  ={11\over12}.
\]

The manuscript now uses

\[
  b={11\over12}C_A-{N_f\over3}T_R,
  \qquad
  \beta(g)
  =
  -{g^3\over16\pi^2}
  \left({11\over3}C_A-{4\over3}T_RN_f\right)+O(g^5).
\]

## Manuscript Changes

- `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
  now includes:
  - background split and background gauge covariance;
  - one-loop determinant ratio;
  - constant-background/IR-cutoff extraction;
  - quark determinant quartic calculation;
  - corrected ghost and vector determinant coefficients;
  - derivation from bare-coupling independence to the beta function;
  - two figures for the background-field logic and the constant-background
    box.

## Follow-Up

- Perform a page-by-page source coverage pass for the remaining 253a and 253b
  material, with special priority on the 1PI effective action, 1PI RG, and
  Wilsonian RG sections.
- The strict writing harness now requires every source derivation, example,
  figure, and conceptual distinction to be explicitly incorporated, corrected,
  deferred, or moved out of core scope.
