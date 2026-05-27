# Volume XII Point-Splitting Subtraction-Algebra Pass

## Scope

- `monograph/tex/volumes/volume_xii/chapter02_point_splitting_stress_tensor.tex`
- `planning/chapter_dossiers/volume_xii/chapter02_point_splitting_stress_tensor.md`
- `calculation-checks/point_splitting_stress_checks.py`
- `calculation-checks/README.md`

## Content Added

The point-splitting stress-tensor chapter now proves the basic algebra of
Hadamard subtraction.  The new proposition shows that the difference of two
Hadamard-state Wick-square expectation values is the diagonal of the smooth
two-point-function difference, and that changing the subtraction by a smooth
locally constructed biscalar \(S\) shifts the Wick square by
\[
  -\int f(x)S(x,x)d{\rm vol}_g(x)\,\mathbf 1 .
\]
This makes explicit which part of the construction is state dependence and
which part is finite local subtraction freedom.

The calculation check now verifies, using exact rational arithmetic, the
cancellation of the common singular subtraction in state differences and the
minus sign in the smooth-subtraction change.

## Verification

- `python3 calculation-checks/point_splitting_stress_checks.py`
- `python3 -m py_compile calculation-checks/point_splitting_stress_checks.py`
- `git diff --check`
- text audit for weak-language patterns in the edited TeX and dossier
- `tools/build_monograph.sh`
