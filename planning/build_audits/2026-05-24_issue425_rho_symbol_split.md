# Issue 425: Separating Spectral \(d\rho\) from Two-Body \(\beta(s)\)

Date: 2026-05-24.

Issue:

- GitHub #425 flagged that \(\rho\) denoted both the Kallen--Lehmann spectral
  measure \(d\rho\) and the unrelated two-body kinematic factor
  \(\sqrt{1-4m^2/s}\) or \(2p/\sqrt s\).

Fix:

- Kept \(d\rho\) and \(\rho_{\rm ac}\) for Kallen--Lehmann spectral measures
  and densities.
- Renamed the two-body kinematic factor to \(\beta(s)\) in:
  Volume I Chapter 14, Volume II Chapter 3, Volume II Chapter 6, and Volume II
  Chapter 7.
- Added an explicit notation sentence at the first partial-wave definition:
  \(\beta(s)\) is a scalar two-body kinematic factor, while \(\rho\) is
  reserved for spectral measures and densities.
- Updated the affected chapter dossiers.

Verification:

- `rg -n -F "\\rho(s)"` and `rg -n -F "rho(s)"` on the affected scattering
  files return no matches.
- The broader `\rho(s)` search in Volumes I--II returns only
  Kallen--Lehmann/LSZ spectral-measure uses and audit notes describing the
  rename.
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 784 pages.
