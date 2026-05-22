# Callan--Symanzik Chart Derivation Audit

Date: 2026-05-22.

Development pass:

- Rewrote the Callan--Symanzik section of the 1PI RG chapter as a derivation
  from a renormalization chart rather than an asserted formula.
- Defined the bare regulated correlator, the bare-to-renormalized parameter
  map, the field factor \(Z_\phi\), the RG vector field, and the field
  anomalous dimension before writing the equation.
- Separated auxiliary-scale dependence from dimensional homogeneity and then
  combined the two to obtain the fixed-point field scaling dimension
  \(\Delta_\phi=d_\phi^{\rm eng}+\gamma_{\phi,\ast}\).
- Kept operator-insertion Callan--Symanzik equations out of this chapter and
  left them to the subsequent local-operator chapter.
- Updated the 1PI RG chapter dossier to require this derivational standard.

Verification:

- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- rendered and visually inspected the affected Chapter 32 pages of
  `/Users/xiyin/QFT/monograph/tex/main.pdf`

Result:

- All checks passed.
- The edited theorem/proof block and scaling equations render cleanly.
