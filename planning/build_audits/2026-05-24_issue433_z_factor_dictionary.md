# Issue 433: Z-Factor Notation Dictionary

Date: 2026-05-24.

Issue:

- GitHub #433 flagged that the compiled volumes used \(Z\), \(Z_\phi\), and
  \(Z(\mu)\) for different objects: the source functional, the
  Kallen--Lehmann/LSZ one-particle residue, finite field normalizations,
  Callan--Symanzik field factors, MS pole factors, and operator/source mixing.

Fix:

- Added a front-door "Notation for Z-Factors in This Part" block at the
  opening of compiled Volume III.
- The dictionary separates \(Z[J]\), \(Z_\phi^{\rm pole}\),
  \(Z_{\rm MOM}(\mu)\), \(Z_\phi^{\rm chart}\),
  \(Z_\phi^{\rm MS}\), and
  \(\mathcal Z^I{}_{A_1\cdots A_r}\).
- The text states explicitly that \(Z_\phi\) in LSZ statements means
  \(Z_\phi^{\rm pole}\), while \(Z_\phi\) in Callan--Symanzik derivations
  means \(Z_\phi^{\rm chart}\).
- Updated the Kallen--Lehmann, LSZ, 1PI generating-functional, 1PI RG,
  renormalized-operator/MS, and Wilson--Fisher dossiers so the notation
  distinction is maintained by the planning harness.

Verification:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 785 pages.
