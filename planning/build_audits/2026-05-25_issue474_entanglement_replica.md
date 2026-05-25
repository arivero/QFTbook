# Issue #474 Audit: Entanglement Entropy And Replica Method

## 2026-05-25 Supersession Note

This audit is historical.  The entanglement/replica chapter and its
calculation check were later moved out of the compiled CFT volume to
`deprecated/volume_iii_premature_topics/`.  The current architecture treats
entanglement in QFT, if developed, as an AQFT/local-algebraic subject requiring
von Neumann algebras, modular theory, split-property or regulator hypotheses,
relative entropy, and type-III issues before replica or entropy formulae are
used.

## Scope

GitHub issue #474 reported that the CFT volume lacked a substantive treatment
of entanglement entropy, the replica trick, the two-dimensional
\(S=(c/3)\log(L/\epsilon)\) formula, and the conformal-ball analogue involving
universal \(F_D\) or Euler-anomaly data.

## Manuscript Changes

- Added `chapter03b_entanglement_entropy_and_replica_method.tex` to Volume V,
  immediately after the stress-tensor/Weyl-anomaly chapter.
- Defined regulated reduced density matrices, Renyi entropies, von Neumann
  entropy, and modular Hamiltonians, with explicit regulator, continuum
  factorization, gauge-constraint, and edge-mode caveats.
- Derived the entanglement first law
  \(\delta S_A=\operatorname{Tr}(\delta\rho_AK_A)\).
- Developed the replica construction as
  \(\operatorname{Tr}\rho_A^n=Z[M_n(A)]/Z[M_1]^n\), with
  \(S_A=(n\partial_n-1)W_n|_{n=1}\), and stated analytic continuation in \(n\)
  as an additional hypothesis.
- Derived the two-dimensional single-interval formula from the uniformizing
  map, Schwarzian stress-tensor transformation, twist-field dimension
  \(h_n=\bar h_n=c_{2d}(n-1/n)/24\), and the twist two-point function.
- Added the universal interval entropy
  \(S=(c_{2d}/3)\log(L/\epsilon)+\hbox{constant}\), plus circle and thermal
  conformal-map descendants.
- Added the conformal map from the causal diamond of a ball to
  \(\mathbb R\times\mathbb H^{D-1}\), the local vacuum ball modular
  Hamiltonian, the hyperbolic-cylinder thermal replica formula, and the
  universal ball entropy in even and odd spacetime dimension.

## Calculation Checks

- Added `calculation-checks/entanglement_replica_checks.py`.
- The script checks:
  - the derivative of \(h_n\) and the twist two-point exponent giving the
    \(c/3\) interval coefficient;
  - the sign of \(S=(n\partial_n-1)W_n|_{n=1}\) for \(W_n=-\log Z_n\);
  - the signs in
    \(S_{\rm univ}=(-1)^{D/2-1}4a_D\log(R/\epsilon)\) for even \(D\) and
    \(S_{\rm univ}=(-1)^{(D-1)/2}F_D\) for odd \(D\), including
    \(a_2=c/12\Rightarrow4a_2=c/3\).

## Verification Plan

- Run `python3 calculation-checks/entanglement_replica_checks.py`.
- Run `git diff --check`.
- Run the monograph text and dossier audits.
- Build the monograph and inspect the rendered pages of the new chapter.

## Verification Results

- `python3 calculation-checks/entanglement_replica_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed after rewriting one negative
  analytic-continuation sentence into a positive hypothesis statement.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed with a clean log scan.
- `pdfinfo monograph/tex/main.pdf` reported 873 pages.
- Rendered and inspected physical PDF pages 785--788, covering the chapter
  opening, regulated entropy definitions, replica construction, two-dimensional
  twist derivation, interval entropy formula, and ball universal entropy
  formula.
