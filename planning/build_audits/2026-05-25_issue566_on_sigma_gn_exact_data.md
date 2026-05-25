# 2026-05-25 Issue 566: O(N) Sigma And Gross-Neveu Exact Data

## Scope

Issue #566 flagged that the Volume VI `O(N)`/Gross-Neveu chapter lacked the
Zamolodchikov exact `O(N)` sigma-model S-matrix, an explicit large-`N`
mass-gap calculation, and paired calculation checks.

## Edits

- Added the exact minimal `O(N)` sigma-model vector S-matrix in index form,
  including the gamma-function expression for \(\sigma_2(\theta)\) and the
  rational crossing relations defining \(\sigma_1\) and \(\sigma_3\).
- Added a proposition proving channel unitarity and crossing by reducing the
  channel eigenvalues to the gamma recurrence identity and elementary rational
  products.
- Added the Zamolodchikov-Faddeev Yang-Baxter component convention and the
  scalar-free rational `O(N)` tensor underlying factorization.
- Added a large-`N` sigma-model gap-equation derivation with the cutoff
  solution \(M=\Lambda(\exp(4\pi/\lambda)-1)^{-1/2}\) and the leading
  beta function \(\mu\,d\lambda/d\mu=-\lambda^2/(2\pi)+O(1/N)\).
- Corrected the Gross-Neveu auxiliary-field saddle to include the explicit
  factor of \(N\) from the fermion determinant and stated the corresponding
  large-`N` mass transmutation formula.
- Added `calculation-checks/on_sigma_gn_checks.py`.

## Targeted Verification

```text
python3 calculation-checks/on_sigma_gn_checks.py
All O(N) sigma-model and large-N gap checks passed.
```

The targeted check includes the gamma-function scalar identity, channel
unitarity, crossing, finite-dimensional Yang-Baxter component identity, and
large-`N` gap and beta-function algebra.

## Full Verification

```text
tools/audit_monograph_text.sh
Strict monograph text audit clean.

tools/audit_chapter_dossiers.sh
Chapter dossier metadata audit clean.

git diff --check

tools/build_monograph.sh
Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf

pdfinfo monograph/tex/main.pdf
Pages:           1279
```
