# 2026-05-26 Volume VIII BF Finite Model Deepening

## Scope

- Rewrote Volume VIII, Chapter 3 from a thin BF-theory outline into a
  self-contained development of classical nonabelian BF theory, compact
  abelian normalization, the finite \(\mathbb Z_N\) cochain model, Wilson and
  surface observables, and boundary/BFV data.
- Fixed the finite nonabelian gauge-transformation convention so that the
  displayed finite action of \(\mathcal G(P)\) differentiates to
  \(\delta_c A=\dd_A c\) and \(\delta_c B=[B,c]\).
- Added a public calculation check for the finite cochain identities used in
  the chapter.

## Mathematical Content Added

- Variation of
  \(S_{\rm BF}=2\pi i\int_M\langle B\wedge F_A\rangle\), including the
  covariant Leibniz sign that gives the field equations
  \(F_A=0\) and \(\dd_A B=0\).
- Proof of the \(B\)-field shift symmetry and its boundary term, together
  with the reducibility chain that requires ghosts-for-ghosts in BV.
- Differential-character normalization for compact abelian BF theory and its
  finite \(\mathbb Z_N\) cochain replacement.
- Finite Fourier proof that the normalized cochain sum gives
  \[
    Z_{\rm BF}^{(N)}(K)
    =
    |H^1(K;\mathbb Z_N)|/|H^0(K;\mathbb Z_N)|
  \]
  for connected \(K\), hence the groupoid cardinality of flat
  \(\mathbb Z_N\)-bundles.
- Derivation of the Wilson/surface linking phase from the finite constraint
  \(\delta a=-p\sigma_\Sigma\).

## Verification

- `python3 calculation-checks/bf_theory_checks.py`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1365`.
