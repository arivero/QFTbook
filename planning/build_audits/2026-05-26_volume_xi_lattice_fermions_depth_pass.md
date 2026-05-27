# 2026-05-26 Volume XI Lattice Fermions Depth Pass

## Scope

Deepened Volume XI, Chapter 11 from a skeletal overview into a theorem-level
finite-regulator chapter.  The pass incorporates the usable material from
`references/lattice fermion.tex` while correcting the presentation into the
standard Dirac/Wilson, staggered, reflection-positive, and Ginsparg-Wilson
frameworks.

## Manuscript Changes

- Proved the finite Berezin Gaussian determinant and propagator identities.
- Proved Brillouin-torus index cancellation for symbols
  \(D_f(p)=\ii\gamma\cdot f(p)\), including the chirality signs of the
  \(2^D\) naive doubler corners.
- Defined the standard spin-scalar Wilson operator and proved the corner
  mass expansion \(m+2rn_\epsilon/a\).
- Added a mid-link reflection figure and a finite Grassmann
  reflection-positivity criterion for crossing factors
  \(\prod_j(1+c_j\Theta(F_j)F_j)\).
- Applied the criterion to the free nearest-neighbor mid-link cut and
  recorded the one-fermion obstruction to site and diagonal reflections.
- Proved Wilson mid-link reflection positivity at \(r=1\) by reducing the
  crossing hopping term to positive projector components.
- Developed the two-dimensional staggered fermion reflection map and proved
  reflection positivity of the staggered Thirring interaction for \(U\geq0\).
- Proved the Ginsparg-Wilson chiral invariance, the Berezinian index factor,
  the overlap Ginsparg-Wilson relation, and the spectral-asymmetry formula
  for the overlap index.
- Added a domain-wall/overlap relation paragraph and a locality warning tied
  to the spectral gap of the Wilson kernel.

## Calculation Check

- Added `calculation-checks/lattice_fermion_chiral_checks.py`.
- The script verifies:
  - naive doubler chirality cancellation in \(D=4\);
  - Wilson corner-mass degeneracies;
  - exact Ginsparg-Wilson matrix algebra and the overlap index;
  - finite Berezinian index normalization;
  - nonnegative reflection-crossing coefficients;
  - Wilson reflection-projector algebra;
  - staggered phase signs.

## Verification

- `python3 calculation-checks/lattice_fermion_chiral_checks.py`
- `python3 -m py_compile calculation-checks/lattice_fermion_chiral_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 1854 pages, 7378174 bytes.
