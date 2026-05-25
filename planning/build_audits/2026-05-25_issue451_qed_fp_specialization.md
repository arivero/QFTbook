# Issue 451 QED Faddeev--Popov specialization

GitHub issue: #451.

Scope addressed:

- `monograph/tex/volumes/volume_i/chapter19_quantum_electrodynamics_and_external_states.tex`
- `planning/chapter_dossiers/volume_i/chapter19_quantum_electrodynamics_external_states.md`

Manuscript changes:

- Added Proposition `prop:qed-abelian-faddeev-popov-specialization` deriving
  the QED Faddeev--Popov operator for
  \(F_\varphi[A]=\partial_\mu A^\mu-\varphi\):
  \[
    \mathcal M_{\rm QED}(x,y)=\Box_x\delta^{(4)}(x-y).
  \]
- Made explicit that \(\Delta_{\rm FP}^{U(1)}=\det{}'\Box\) only after
  residual zero modes are removed or separately fixed.
- Explained why the Abelian determinant cancels from normalized QED
  representative correlators and why a ghost representation would be free and
  decoupled, producing no QED ghost vertex.
- Added the forward comparison to the nonabelian Lorenz-gauge operator
  \(\partial^\mu D_\mu(A)\), the interacting ghost determinant, and the
  Singer--Gribov obstruction, with direct references to the BRST chapter.
- Updated the chapter dossier so the Abelian specialization and deferred
  nonabelian construction are part of the recorded chapter contract.

Verification plan:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

Calculation-check scripts are not rerun because this is a TeX/dossier framing
and derivation edit with no calculation-check script or harness changes.
