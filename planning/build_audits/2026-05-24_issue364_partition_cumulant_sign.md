# 2026-05-24 Issue #364 Partition Cumulant Sign

GitHub issue #364 flagged that the multi-insertion source-coordinate partition
formula had the correct factor \((-1)^{r-|\pi|}\), but the explanation could be
read as mixing unrelated minus signs.

Changes made:

- Rewrote the derivation around the finite-regulator partition formula.
- Introduced \(D^\Lambda_A=-\delta/\delta\eta_\Lambda^A\) and
  \(D^0_I=-\delta/\delta\eta_0^I\).
- Explained that ordinary Faà di Bruno is first applied to the connected
  functional \(W=\log Z\), and only then are ordinary derivatives rewritten as
  connected insertion derivatives.
- Derived the factor
  \[
    (-1)^r(-1)^{|\pi|}=(-1)^{r-|\pi|}
  \]
  for a partition with \(|\pi|\) bare connected cumulants.
- Added the equivalent blockwise explanation: a block \(B\) of size \(|B|\)
  collapses \(|B|\) renormalized insertion derivatives into one connected
  cumulant and contributes \((-1)^{|B|-1}\).
- Updated the renormalized-operators dossier.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
