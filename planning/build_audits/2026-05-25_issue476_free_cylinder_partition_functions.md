# Issue #476 Audit: Free Fermion And Free Maxwell Cylinder Partition Functions

## Scope

GitHub issue #476 reported that the radial-quantization chapter contained the
free-scalar operator partition function but lacked the parallel spin-\(1/2\)
and spin-\(1\) free-field partition functions on the cylinder.

## Manuscript Changes

- Added `The Free Fermion Operator Partition Function` to
  `chapter04_radial_quantization_and_state_operator_correspondence.tex`.
- Defined the spinor module \(S\), spinor dimension \(s_S\), free spinor
  scaling dimension \(\Delta_\psi=(D-1)/2\), and the Dirac null descendant
  \(\gamma^\mu\widehat P_\mu|\psi\rangle\).
- Derived the spinor short-module character
  \(f_\psi(q)=s_Sq^{(D-1)/2}/(1-q)^{D-1}\), including the four-dimensional
  Weyl and Dirac specializations.
- Added the exterior-algebra operator partition function for fermionic
  letters, with the \((-1)^F\) variant stated separately.
- Added `The Free Maxwell Operator Partition Function` for conformal Maxwell
  theory in \(D=4\).
- Derived the Maxwell field-strength character from the polynomial jet
  complex:
  \(6q^2\) field-strength components, \(-8q^3\) from Bianchi and Maxwell
  constraints, and \(+2q^4\) from the scalar reducibility identities.
- Displayed the equivalent form
  \(f_{\rm Max}(q)=q^2(6-8q+2q^2)/(1-q)^4=(6q^2-2q^3)/(1-q)^3\), its chiral
  \(F^\pm\) decomposition, and the bosonic symmetric-algebra operator
  partition function.

## Calculation Checks

- Added `calculation-checks/free_cylinder_partition_checks.py`.
- The script checks:
  - the four-dimensional scalar reduction already used in the chapter;
  - Weyl and Dirac fermion degeneracies through several levels;
  - the Maxwell numerator identity and the first Maxwell degeneracies;
  - the short-module numerator multiplicities.

## Verification Plan

- Run `python3 calculation-checks/free_cylinder_partition_checks.py`.
- Run `git diff --check`.
- Run the strict monograph text audit and chapter dossier audit.
- Build the monograph and inspect rendered pages of the revised chapter.

## Verification Results

- `python3 calculation-checks/free_cylinder_partition_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed with a clean log scan after replacing an
  undefined `\Spin` macro by `\operatorname{Spin}`.
- `pdfinfo monograph/tex/main.pdf` reported 877 pages.
- Rendered and inspected physical PDF pages 809--811, covering the free
  fermion short-module derivation, the Weyl/Dirac specializations, the
  Maxwell field-strength complex, the Maxwell character identity, and the
  transition to the Cardy section.
