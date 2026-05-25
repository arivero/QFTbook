# Issue #464 Audit: Brout--Englert--Higgs Mechanism

## Scope

- GitHub issue: #464, "[Vol IV] Higgs mechanism / BEH spontaneous
  gauge-symmetry breaking completely absent."
- Manuscript loci:
  - `monograph/tex/volumes/volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`
  - `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`
- Dossier locus:
  - `planning/chapter_dossiers/volume_ii/chapter18_classical_yang_mills_matter.md`

## Content Added

- Added a dedicated Brout--Englert--Higgs mechanism section after matter
  representations and before finite-energy gauge-Higgs solitons.
- Developed the Abelian Higgs model in the monograph's coupling-absorbed
  gauge convention:
  \[
    D_\mu\phi=\partial_\mu\phi-iA_\mu\phi,\qquad
    \mathcal L=-\frac{1}{4e^2}F^2+|D\phi|^2
      -\lambda(|\phi|^2-v^2/2)^2 .
  \]
- Derived the quadratic mixing
  \[
    |D\phi|^2
      =\frac12(\partial h)^2
       +\frac12(\partial_\mu\pi-vA_\mu)^2+\cdots,
  \]
  the scalar mass \(m_h^2=2\lambda v^2\), and vector mass \(m_A=ev\) after
  canonical normalization.
- Introduced the gauge-invariant unitary-gauge coordinate
  \(B_\mu=A_\mu-v^{-1}\partial_\mu\theta\).
- Derived the \(R_\xi\) gauge-fixing functional
  \(\mathcal F_\xi=\partial_\mu A^\mu+\xi e^2v\pi\), cancellation of
  \(A_\mu\partial^\mu\pi\) mixing, the \(R_\xi\) vector propagator, and the
  gauge-dependent Goldstone/ghost mass \(\sqrt{\xi}m_A\).
- Added a BEH mode-accounting figure explaining the relation among scalar
  orbit coordinates, massive vector polarizations, and BRST-unphysical fields.
- Developed the nonabelian mass matrix
  \(K_{ab}=\operatorname{Re}(t_R^a v,t_R^b v)_R\), identified its kernel with
  the stabilizer Lie algebra \(\mathfrak h\), and stated the
  \(\dim G-\dim H\) massive-vector count.
- Added the orbit differential \(q_v(X)=i\,t_R(X)v\), a local BEH mode-count
  proposition with proof, and the identity
  \(D_\mu(v+\eta)=\partial_\mu\eta-q_v(A_\mu)+O(A_\mu\eta)\) as the precise
  local relation between gauge-orbit scalar coordinates and longitudinal
  vector polarizations.
- Added the nonabelian \(R_\xi\) gauge-fixing functional
  \(\mathcal F_\xi=\partial^\mu A_\mu+\xi g_{\rm YM}^2q_v^\dagger\eta\) in a
  local chart, with \(q_v^\dagger q_v\) controlling the broken-sector
  unphysical scalar and ghost masses.
- Added the adjoint \(SU(2)\to U(1)\) example and the electroweak
  \(SU(2)\times U(1)\to U(1)_{\rm em}\) structural pointer.
- Added a local renormalizability paragraph: \(R_\xi\) gauges make power
  counting manifest and BRST identities control counterterms; unitary gauge is
  a classical spectrum coordinate chart, not the manifest proof gauge.
- Cross-referenced the new section from the Goldstone-theorem discussion of
  gauged directions.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed.
- `pdfinfo monograph/tex/main.pdf`: 847 pages.
- Rendered and inspected the affected Chapter 43 BEH pages and the Chapter 50
  Goldstone-theorem cross-reference pages with `pdftoppm`/`view_image`; no
  overfull visual layout, broken figure, or formula collision was found.
