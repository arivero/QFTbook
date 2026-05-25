# Issue #472 Audit: NLO Chiral Perturbation Theory And Gasser--Leutwyler Basis

## Scope

GitHub issue #472 reported that the pion chapter developed the pion coset but
did not name chiral perturbation theory, did not present the
Gasser--Leutwyler \(L_1,\ldots,L_{10}\) NLO basis, and did not compute an
explicit chiral logarithm such as the NLO pion mass.

## Manuscript Changes

- Added `\section{Chiral Perturbation Theory at NLO}`
  to
  `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`,
  between the mass-spurion discussion and the Wess--Zumino--Witten section.
- Defined chiral perturbation theory as the derivative/source/quark-mass
  expansion of the QCD current generating functional, not merely as an
  expansion in pion fields.
- Stated the chiral order assignments
  \(D_\mu U,\ell_\mu,r_\mu=O(p)\) and
  \(F_{\mu\nu}^{L,R},\chi=O(p^2)\), and derived Weinberg's graph-counting
  formula
  \[
    \nu=2+2L+\sum_iV_i(d_i-2).
  \]
- Displayed the three-flavor even-parity
  Gasser--Leutwyler \(O(p^4)\) basis \(L_1,\ldots,L_{10}\) in the manuscript's
  left/right convention \(U\mapsto LUR^{-1}\), including the source-contact
  constants \(H_1,H_2\), with a footnote identifying the original
  Gasser--Leutwyler papers and noting the convention translation.
- Added the \(\Gamma_i\) table and running equation
  \(\mu\,dL_i^r/d\mu=-\Gamma_i/(16\pi^2)\).
- Added a worked two-flavor pion-mass chiral logarithm:
  \[
    M_{\pi,\rm phys}^2
    =
    M^2\left[
      1+\frac{M^2}{32\pi^2f^2}\log\frac{M^2}{\mu^2}
      +\frac{2l_3^r(\mu)M^2}{f^2}
    \right]+O(M^6),
  \]
  including the tadpole logarithm and cancellation of \(\mu\)-dependence by
  \(\mu\,dl_3^r/d\mu=1/(32\pi^2)\).

## Calculation Checks

- Added `calculation-checks/chpt_nlo_checks.py`.
- The script verifies:
  - the \(L_1,\ldots,L_{10}\) label count;
  - selected \(\Gamma_i\) table entries, including
    \(\Gamma_9+\Gamma_{10}=0\);
  - scale cancellation in the two-flavor \(M_\pi^2\) NLO logarithm.

## Verification Plan

- Run the new calculation check directly.
- Run `git diff --check`.
- Run the monograph text and dossier audits.
- Build the monograph and inspect the pages containing the new NLO ChPT
  section.

## Verification Results

- `python3 calculation-checks/chpt_nlo_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed after shortening the displayed section
  heading to remove an overfull heading line.
- `pdfinfo monograph/tex/main.pdf` reported 868 pages.
- Rendered and inspected physical PDF pages 743--745, covering the section
  opening, the displayed \(L_1,\ldots,L_{10}\) functional, the \(\Gamma_i\)
  table, and the two-flavor pion-mass chiral logarithm.
