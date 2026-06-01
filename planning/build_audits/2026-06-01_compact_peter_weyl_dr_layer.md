# Compact Peter--Weyl DR Layer

Date: 2026-06-01.

Scope:
- Advanced GitHub issue #695 by adding the compact coordinate-algebra layer
  that sits between finite Tannakian examples and the full
  Doplicher--Roberts reconstruction theorem.

Manuscript changes:
- Added `Compact Peter--Weyl coordinate algebra` to
  `monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`.
- Defined the matrix coefficient
  \(f_{\ell,v}^W(g)=\ell(D_W(g)v)\), the representative-function algebra
  \(\operatorname{Pol}(G)\subset C(G)\), tensor-product multiplication, Hopf
  operations \(\Delta_{\rm H},\epsilon,S\), Haar functional \(h_G\), and the
  Peter--Weyl decomposition.
- Made the logical boundary explicit: this is the compact-group coordinate
  algebra that appears after the DHR category and fiber functor are already
  constructed; it is not a proof that an arbitrary local net has such a
  category or field algebra.

Calculation check:
- Extended `calculation-checks/dhr_dr_reconstruction_checks.py` with the
  finite \(S_3\) Peter--Weyl Hopf coordinate-algebra diagnostic.
- The check verifies that the trivial, sign, and standard matrix coefficient
  functions span \(\operatorname{Fun}(S_3)\), that the coproduct, counit, and
  antipode identities hold pointwise, that Haar averaging is bi-invariant,
  and that multiplication is compatible with the group-law coproduct.

Verification:
- `python3 calculation-checks/dhr_dr_reconstruction_checks.py`
- `python3 -m py_compile calculation-checks/dhr_dr_reconstruction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only dhr_dr_reconstruction`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
