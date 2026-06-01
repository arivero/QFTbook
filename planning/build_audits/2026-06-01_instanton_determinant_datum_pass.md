# Instanton Determinant Datum Pass

Date: 2026-06-01

Issue lane: #597.

## Scope

This pass continues the carefully regularized instanton-measure work.  The
previous two passes supplied the general ADHM quotient and the classical
quotient density.  The next missing piece was the finite-regulator
nonzero-mode determinant datum: what is meant by the determinant factor
before a continuum scheme, determinant-line trivialization, or
small-instanton boundary estimate has been chosen.

## Manuscript Changes

- Added a finite-regulator determinant-datum paragraph in Volume II,
  Chapter 20, immediately after the collective-coordinate measure formula.
- Defined the finite bosonic Hessian \(L_{\Lambda,z}^{\rm bos}\) on normal
  modes, ghost operator \(M_{\Lambda,z}^{\rm gh}\) with residual stabilizer
  zero modes removed, and regulated fermion kinetic operator
  \(\mathcal D_{\Lambda,z}^{R}\).
- Defined the nonzero-mode determinant datum
  \[
    \mathcal W_\Lambda^{\rm nz}(z)
    =
    \frac{\det' M_{\Lambda,z}^{\rm gh}}{\det' M_{\Lambda,0}^{\rm gh}}
    \left(
      \frac{\det L_{\Lambda,0}^{\rm bos}}
           {\det' L_{\Lambda,z}^{\rm bos}}
    \right)^{1/2}
    \bigotimes_R
    \frac{\operatorname{Pf}'\mathcal D_{\Lambda,z}^{R}}
         {\operatorname{Pf}\mathcal D_{\Lambda,0}^{R}} .
  \]
- Stated explicitly that chiral fermion factors are determinant/Pfaffian-line
  vectors, not numbers, until anomaly-line and zero-mode saturation data have
  been supplied.
- Rewrote the one-instanton finite-regulator measure as
  \(e^{-S_\Lambda(A_z)}\mathcal W_\Lambda^{\rm nz}(z)
    \dd\nu_{\Lambda,\mathcal M}(z)\).
- Added the finite Gaussian/Berezin derivation and the local-counterterm
  scheme-dependence statement: a counterterm difference
  \(c_0+c_1\log(\mu\rho)+R_\Lambda\) changes the constant, the
  \(\mu\rho\) power, and the remaining boundary/continuum analysis
  respectively.

## Calculation Check

Extended `calculation-checks/bpst_instanton_normalization_checks.py` with
finite arithmetic checks for:

- bosonic determinant inverse-square-root bookkeeping, tracked through the
  square to avoid irrational quantities;
- ghost determinant numerator factors;
- fermion nonzero-mode Pfaffian ratios;
- the combined vectorlike scalar determinant-datum power;
- the logarithmic power shift produced by a local counterterm
  \(c_1\log(\mu\rho)\).

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

This pass still does not close #597.  It defines the finite-regulator
nonzero-mode determinant datum and its scheme dependence.  The continuum
determinant constants in specified schemes, small-instanton boundary
estimates, and further soliton/monopole/instanton quantization remain open.
