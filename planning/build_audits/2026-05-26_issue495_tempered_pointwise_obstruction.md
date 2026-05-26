# 2026-05-26 Issue 495: Temperedness Versus Pointwise Boundedness

GitHub issue: #495, polynomial boundedness from Wightman axioms where
possible.

This pass does not claim the full Jin--Martin theorem.  It closes a logical
gap in the text by proving that the already-added distributional
polynomial-growth theorem is strictly weaker than the pointwise fixed-\(t\)
polynomial bound needed for dispersion-contour estimates.

## Manuscript Addition

Volume II, Chapter 7 now contains
`prop:temperedness-does-not-imply-pointwise-polynomial-bound`.

The proposition constructs a smooth nonnegative \(L^1(\mathbb R)\) function
\[
  f(s)=\sum_{n\ge1}e^{n^2}\psi(e^{3n^2}(s-n)),
\]
where \(\psi\in C_c^\infty((-1/4,1/4))\), \(\psi\ge0\), and \(\psi(0)=1\).
The support intervals are pairwise disjoint and locally finite, so \(f\) is
smooth.  The \(L^1\) norm is finite because each spike has area
\(e^{n^2}e^{-3n^2}\int\psi=e^{-2n^2}\int\psi\).  Therefore \(f\) defines a
tempered distribution bounded by the Schwartz seminorm \(p_{0,0}\), but
\[
  f(n)\ge e^{n^2},
\]
which violates every polynomial pointwise bound.

## Logical Consequence

The monograph now explicitly proves that Wightman temperedness by itself
cannot control pointwise high-energy amplitudes.  The pointwise fixed-\(t\)
Jin--Martin bound must use the genuinely analytic inputs: locality,
spectral support, edge-of-the-wedge/Jost--Lehmann--Dyson domains,
Lehmann--Martin ellipse control, and LSZ boundary-value regularity.  The
Froissart angular-tube bound remains a still stronger hypothesis unless
derived separately.

## Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`

Issue #495 remains open pending a self-contained construction of the full
Jin--Martin pointwise fixed-\(t\) proof layer.
