# Small-Instanton Boundary Exponent Pass

Date: 2026-06-01

Issue lane: #597.

## Scope

This pass continues the carefully regularized instanton-measure work after
the ADHM quotient-density and finite-regulator determinant-datum passes.
The missing local analytic layer was the small-instanton/Uhlenbeck boundary
criterion: which power of the instanton size \(\rho\) must be controlled
after determinants, insertions, zero-mode saturation, and counterterms have
been paired.

## Manuscript Changes

- Added a "Small-instanton boundary exponent" paragraph in Volume II,
  Chapter 20.
- Defined a one-instanton boundary exponent datum for a specified insertion
  datum \(\mathcal X\): numbers \(\beta_{\mathcal X}\), \(\delta>0\), and a
  locally bounded coefficient \(A_{\mathcal X}(a,U)\) such that the scalar
  one-instanton chart density has the small-\(\rho\) form
  \[
    C_{\mathcal X}(\mu)\rho^{b_0+\beta_{\mathcal X}-5}
    (A_{\mathcal X}(a,U)+O(\rho^\delta))
    d^4a\,d\rho\,d\Omega_{N_c}.
  \]
- Derived the local Uhlenbeck-boundary threshold
  \(b_0+\beta_{\mathcal X}>4\) from the one-dimensional size integral,
  including the logarithmic borderline.
- Separated asymptotic freedom \(b_0>0\) from local small-instanton
  integrability of a chosen observable.
- Recorded that center collisions with local insertions and higher-charge
  Uhlenbeck strata are additional boundary faces, not covered by the
  single collapsed charge exponent datum.

## Calculation Check

Extended `calculation-checks/bpst_instanton_normalization_checks.py` with
exact rational checks for:

- pure \(SU(2)\) and pure \(SU(3)\) vacuum one-instanton local finiteness;
- \(SU(3)\), \(N_f=16\), where \(b_0>0\) but the vacuum small-\(\rho\)
  exponent fails the \(b_0>4\) integrability threshold;
- recovery of finiteness after adding an insertion exponent
  \(\beta_{\mathcal X}=4\);
- the borderline logarithmic divergence at equality;
- equality between the antiderivative denominator and the threshold margin
  \(b_0+\beta_{\mathcal X}-4\).

Updated the calculation-check README and Volume II Chapter 20 dossier.

## Verification

Targeted verification should include:

```bash
python3 calculation-checks/bpst_instanton_normalization_checks.py
python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py
git diff --check
python3 tools/audit_theorem_form.py
python3 tools/audit_unnumbered_display_labels.py
tools/audit_negative_scope_prose.py
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
tools/build_monograph.sh
```

This pass still does not close #597.  It supplies the single-boundary-face
power criterion.  The full issue still needs specified continuum determinant
constants, estimates near higher Uhlenbeck strata and center-collision
faces, plus further soliton/monopole/instanton quantization development.
