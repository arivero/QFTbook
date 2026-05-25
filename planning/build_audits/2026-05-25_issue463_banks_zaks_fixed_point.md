# Issue #463 Audit: Banks-Zaks Fixed Point

## Scope

- GitHub issue: #463, "[Vol III] Banks-Zaks fixed point / IR fixed point in
  non-Abelian gauge theory absent."
- Manuscript locus:
  - `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
- Dossier locus:
  - `planning/chapter_dossiers/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_dis.md`
- Calculation-check locus:
  - `calculation-checks/banks_zaks_two_loop_checks.py`

## Content Added

- Replaced the skeletal Banks-Zaks paragraph with an explicit two-loop
  analysis in the monograph's gauge-generator normalization.
- Defined \(a=g^2/(16\pi^2)\) and used
  \(\beta_a=-2B_0a^2-2B_1a^3+O(a^4)\), with
  \[
    B_0=\frac{11}{3}C_A-\frac{4}{3}T_RN_f,\qquad
    B_1=\frac{34}{3}C_A^2
      -\left(\frac{20}{3}C_AT_R+4C_RT_R\right)N_f .
  \]
- Showed directly that analytic coupling redefinitions
  \(a'=a+r_1a^2+r_2a^3+\cdots\) preserve \(B_0\) and \(B_1\).
- Specialized to fundamental \(SU(N_c)\) with
  \(C_A=2N_c\), \(T_F=1\), \(C_F=(N_c^2-1)/N_c\), deriving
  \[
    B_0=\frac{2}{3}(11N_c-2N_f),\qquad
    B_1=\frac{136}{3}N_c^2
      -\left(\frac{52}{3}N_c-\frac4{N_c}\right)N_f .
  \]
- Derived the perturbative window
  \[
    \frac{34N_c^3}{13N_c^2-3}<N_f<\frac{11}{2}N_c,
  \]
  the \(\epsilon_{\rm BZ}=(11N_c-2N_f)/3\) expansion,
  \(a_*=\epsilon_{\rm BZ}/(25N_c^2-11)+O(\epsilon_{\rm BZ}^2)\), and
  \(\omega_{\rm BZ}=4\epsilon_{\rm BZ}^2/(25N_c^2-11)+O(\epsilon_{\rm BZ}^3)\).
- Added the massless-flavor, integer-\(N_f\), and Veneziano-regime caveats.

## Verification

- `python3 calculation-checks/banks_zaks_two_loop_checks.py`: passed.
- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 843 pages.
- Rendered and inspected affected manuscript pages:
  - Chapter 47 Banks-Zaks derivation and figure, printed pages 638--640.
