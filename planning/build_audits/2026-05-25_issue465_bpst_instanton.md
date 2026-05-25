# Issue #465 Audit: BPST Instanton and Semiclassical Vertex

## Scope

- GitHub issue: #465, "[Vol IV] BPST instanton: explicit solution, action
  saturation, zero modes, 't Hooft vertex absent."
- Manuscript loci:
  - `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
  - `monograph/tex/volumes/volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`
- Calculation-check locus:
  - `calculation-checks/bpst_instanton_normalization_checks.py`
- Dossier locus:
  - `planning/chapter_dossiers/volume_ii/chapter20_chiral_axial_anomalies.md`

## Content Added

- Added a dedicated BPST instanton and semiclassical vertex section after the
  topological charge sector discussion.
- Defined Euclidean conventions, self-dual 't Hooft symbols, and the explicit
  regular-gauge \(SU(2)\) one-instanton
  \[
    A_\mu=2\eta^a_{\mu\nu}(x-a)^\nu[(x-a)^2+\rho^2]^{-1}T_a .
  \]
- Displayed the quadratic \(\eta\)-symbol identity needed to reduce the
  derivative and commutator terms in the curvature.
- Derived the curvature
  \[
    F_{\mu\nu}
    =
    -4\rho^2\eta^a_{\mu\nu}[(x-a)^2+\rho^2]^{-2}T_a
  \]
  and its self-duality.
- Displayed the singular-gauge representative and the winding-one boundary
  map \(S^3_\infty\to SU(2)\).
- Completed the Euclidean action square and evaluated
  \(\int F^a_{\mu\nu}F^a_{\mu\nu}=32\pi^2\), \(Q=1\), and
  \(S_E=8\pi^2/g_{\rm ht}^2\) in the common half-trace coupling.
- Explicitly related the common half-trace coupling to the monograph
  trace-delta coupling:
  \(g_{\rm ht}=\sqrt2\,g_{\rm YM}\), hence
  \(8\pi^2/g_{\rm ht}^2=4\pi^2/g_{\rm YM}^2\).
- Added a BPST data figure linking the connection, self-dual curvature,
  action saturation, collective coordinates, and fermion zero-mode saturation.
- Added the \(SU(2)\), \(k=1\) bosonic zero-mode count
  \(4+1+3=8\), and the \(SU(N_c)\) embedded count \(4N_c\).
- Used the index theorem to state fermion zero-mode counts
  \(n_+-n_-=2T_Rk\) in common half-trace notation.
- Derived the zero-mode Berezin selection rule and stated the QCD 't Hooft
  vertex as the chiral flavor determinant
  \(\det_{f f'}(\rho^3\bar\psi_{Rf}\psi_{Lf'})\) with
  \(\Delta Q_A=2N_f\), including the definition of the one-loop coefficient
  \(b_0=\frac{11}{3}N_c-\frac23N_f\).
- Added the electroweak \(SU(2)_L\) vertex
  \(\prod_r(q_{Lr}q_{Lr}q_{Lr}\ell_{Lr})\) and
  \(\Delta B=\Delta L=N_g\), \(\Delta(B-L)=0\),
  \(\Delta(B+L)=2N_g\).
- Added a cross-reference from the Yang--Mills topological-term discussion.

## Verification

- Passed: `python3 calculation-checks/bpst_instanton_normalization_checks.py`.
- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
- Passed: `pdfinfo monograph/tex/main.pdf` reported 850 pages.
- Passed: affected pages 682--686 were rendered and visually inspected from
  `monograph/tex/main.pdf`; the BPST figure and surrounding formulas were
  legible after shifting the arrow labels and tightening the middle curvature
  box.
