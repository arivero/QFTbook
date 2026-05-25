# Volume IX Ising Kramers-Wannier Defect Pass

## Trigger

The open review stream had flagged that the categorical-symmetry volume still
lacked a substantial noninvertible example and that the SymTFT discussion
should be concrete rather than purely schematic.  I addressed this in the
core categorical-symmetry chapter rather than deferring it to a later
special-topics volume.

## Manuscript Edits

- Expanded `volume_ix/chapter09_categorical_symmetry_and_defect_fusion.tex`
  with the Ising/Kramers--Wannier defect category:
  \[
    \eta^2=1,\qquad \eta\mathcal N=\mathcal N\eta=\mathcal N,\qquad
    \mathcal N^2=1+\eta .
  \]
- Added a proof of the Frobenius--Perron dimensions
  \(d_1=d_\eta=1\), \(d_{\mathcal N}=\sqrt2\).
- Added the Ising modular \(S\)-matrix and derived the defect eigenvalues
  \(\lambda_a(i)=S_{ai}/S_{1i}\), including the zero of
  \(\mathcal N\) on the spin sector.
- Proved that these eigenvalues represent the fusion algebra on local
  primary sectors.
- Added a limited, explicit SymTFT comparison map for rational examples:
  bulk topological lines to boundary topological defects to endomorphisms of
  the local-operator space.

## Calculation Check

- Added `calculation-checks/ising_defect_fusion_checks.py`, using exact
  \(\mathbb Q(\sqrt2)\) arithmetic to verify fusion associativity, the
  dimension homomorphism, modular \(S\)-matrix orthogonality, the Verlinde
  formula, and the diagonal line-action identities.

## Verification

- `python3 calculation-checks/ising_defect_fusion_checks.py`
  passed.
- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
  passed from `monograph/tex`.
- `pdfinfo monograph/tex/main.pdf` reports 1199 pages.
- `rg -n "undefined|multiply defined|LaTeX Warning: Reference"
  monograph/tex/main.log` returned no matches.
