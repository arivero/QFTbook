# Build Audit: Issue #460 Wilson-Fisher Two-Loop NLO Data

## Issue

- GitHub issue: #460, oldest open issue after #459 was closed.
- Requested substance: derive the two-loop epsilon-expansion/NLO
  Wilson-Fisher data, at minimum for \(\eta\) and \(\nu\).

## Manuscript Edits

- Added `Two-Loop Pole Data and NLO Epsilon Expansion` to
  `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`.
- Introduced \(x=\lambda_{\rm MS}/(16\pi^2)\) and the two-loop MS pole map
  \[
    g_0/(16\pi^2)=\mu^\epsilon
    [x+3x^2/\epsilon+x^3(9/\epsilon^2-17/(6\epsilon))+O(x^4)].
  \]
- Added the two-loop momentum-carrying \(\phi^2\) source pole
  \[
    \log Z_{2,\rm src}^{\rm MS}
    =(-x+5x^2/12)/\epsilon+\text{double poles}+O(x^3).
  \]
- Proved the algebra from the pole map to
  \(\beta_x^\epsilon=-\epsilon x+3x^2-\frac{17}{3}x^3+O(x^4)\),
  \(\gamma_2=x-\frac56x^2+O(x^3)\), and
  \(\gamma_\phi=x^2/12+O(x^3)\).
- Solved for
  \(x_*=\epsilon/3+17\epsilon^2/81+O(\epsilon^3)\) and derived
  \[
    \eta=\epsilon^2/54+O(\epsilon^3),\qquad
    \nu=1/2+\epsilon/12+7\epsilon^2/162+O(\epsilon^3),
  \]
  together with
  \(\Delta_\phi\), \(\gamma_{2*}\), \(\Delta_{\phi^2}\), \(y_t\), and
  \(\omega=\epsilon-17\epsilon^2/27+O(\epsilon^3)\).
- Updated the critical-surface, odd-source, quartic-irrelevant-operator, and
  low-lying-dimension table formulas to the two-loop/NLO values.

## Calculation Check

- Added `calculation-checks/wilson_fisher_epsilon_checks.py`, using exact
  rational arithmetic to verify the algebra from the two-loop pole
  coefficients to \(x_*\), \(\eta\), \(\gamma_{2*}\), \(y_t\), \(\nu\), and
  \(\omega\).
- Updated `calculation-checks/README.md`.

## Dossier Edits

- Updated
  `planning/chapter_dossiers/volume_ii/chapter15_wilson_fisher_fixed_point_scaling_operators.md`
  with the two-loop construction task, claim ledger entries, and audit note.

## Verification

- `git diff --check`: clean.
- `python3 calculation-checks/wilson_fisher_epsilon_checks.py`: passed with
  exact rational arithmetic.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; wrote
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 834 pages.
- Rendered and inspected PDF pages 481--484 for the new two-loop pole-data
  section and exponent derivation, and page 488 for the updated
  operator-spectrum figure and low-lying-dimension table.
