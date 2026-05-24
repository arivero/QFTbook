# 2026-05-24 Issue #368 Bose Fock Odot Normalization

GitHub issue #368 flagged that the first bosonic Fock-space construction used
the symmetric tensor notation without declaring the normalization of
\(\psi_1\odot\cdots\odot\psi_n\), while the Haag--Ruelle chapter later used the
creation-operator convention.

Changes made:

- Added the symmetric projection
  \(\Pi_{s,n}=n!^{-1}\sum_{\sigma\in S_n}U_\sigma\) in Volume I, Chapter 5.
- Defined
  \[
    \psi_1\odot\cdots\odot\psi_n
    =
    \sqrt{n!}\Pi_{s,n}(\psi_1\otimes\cdots\otimes\psi_n).
  \]
- Displayed the resulting inner product
  \[
    \delta_{mn}\sum_{\sigma\in S_n}\prod_j
    \langle\psi_j,\chi_{\sigma(j)}\rangle_{\Hilb_1}.
  \]
- Updated the Chapter 5 and Haag--Ruelle chapter dossiers.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
