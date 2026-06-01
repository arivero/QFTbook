# 2026-06-01 Issue #630 BK Closure Boundary Pass

Issue lane: GitHub #630, QCD rigor uplift.

## Purpose

This pass tightens the small-\(x\) QCD discussion at the point where the
usual literature often jumps from Wilson-line rapidity evolution to the BK
equation.  The manuscript now inserts the missing finite-regulator layer:
the first dipole projection of the Balitsky hierarchy and the connected
double-dipole coordinate whose suppression is required before the BK closure
is a controlled approximation.

## Manuscript Changes

- Added the paragraph block `Dipole projection and the BK closure boundary`
  in Volume II, Chapter 19, inside the finite Wilson-line/JIMWLK subsection.
- Defined finite cell weights
  \(\omega_{\mathbf x\mathbf y;\mathbf z}(Y)\), first dipole coordinates
  \(S_{\mathbf x\mathbf y}^{(1)}\), and double-dipole coordinates
  \(S_{\mathbf x\mathbf z;\mathbf z\mathbf y}^{(2)}\).
- Displayed the finite first Balitsky projection before any closure.
- Defined the connected closure coordinate
  \(E_{\mathbf x\mathbf y}^{\rm BK}\).
- Derived the closed finite BK equation in the amplitude variable
  \(N_{\mathbf x\mathbf y}=1-S_{\mathbf x\mathbf y}\) only after setting the
  connected coordinate to zero.
- Added the finite Gronwall estimate
  \(d(Y)\le\int_0^Y e^{3L(Y-s)}\varepsilon(s)\,ds\), making explicit the
  norm and rapidity interval in which a BK approximation would have to be
  justified.

## Calculation Check

Updated `calculation-checks/qcd_bfkl_small_x_checks.py` with exact rational
checks for:

- \(S\)-to-\(N\) conversion of the finite BK vector field;
- inward pointing of the closed unit-cube vector field;
- transparent and black-disk fixed points;
- the \(3L\) Lipschitz ledger behind the finite Gronwall estimate.

## Verification

Run after the edit:

```bash
python3 calculation-checks/qcd_bfkl_small_x_checks.py
python3 -m py_compile calculation-checks/qcd_bfkl_small_x_checks.py
tools/run_calculation_checks.sh --python-only --only qcd_bfkl_small_x
tools/audit_theorem_form.py
tools/audit_unnumbered_display_labels.py
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
git diff --check
tools/build_monograph.sh
```

## Scope

This does not close #630.  It narrows the small-\(x\) subcluster by making
the BK closure a finite, normed approximation problem rather than a slogan.
Remaining #630 work still includes continuum JIMWLK limit estimates,
stronger SCET/Glauber factorization bounds, refined jet factorization, exact
Chern-Simons-matter solution layers, and hydrodynamics-from-QCD development.
