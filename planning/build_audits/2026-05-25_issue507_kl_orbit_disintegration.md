# 2026-05-25 Issue #507: Kallen--Lehmann Orbit Disintegration

## Scope

GitHub issue #507 flagged the proof of invariant mass-shell disintegration in
the Kallen--Lehmann chapter.  The previous proof invoked a "standard
orbit-disintegration theorem" without verifying the hypotheses needed for the
noncompact Lorentz group action on the forward cone.

## Manuscript Changes

- Replaced the black-box proof in Proposition
  `prop:kallen-lehmann-mass-shell-disintegration`.
- Restricted to \(X=\overline V_+\setminus\{0\}\), using the hypothesis that
  the origin has no atom.
- Verified the Mackey--Effros regular-orbit hypotheses for
  \(G=SO^+(1,D-1)\):
  - \(G\) is locally compact second countable.
  - \(X\) is locally compact, second countable, sigma-compact, and standard
    Borel.
  - The nonzero orbits are the positive massive shells
    \(\Sigma_s^+\), \(s>0\), and the punctured future light cone
    \(\Sigma_0^{+\times}\).
  - The quotient is the standard Borel space \([0,\infty)\), with Borel
    section \(c(0)=\ell=(1,1,0,\ldots,0)\) and
    \(c(s)=k_s=(\sqrt{s},0,\ldots,0)\) for \(s>0\).
  - Stabilizers are the closed unimodular groups \(SO(D-1)\) and
    \(ISO(D-2)=\mathbb R^{D-2}\rtimes SO(D-2)\).
- Identified the normalized invariant Radon shell measures
  \[
    d\sigma_s(p)=\frac{d^Dp}{(2\pi)^{D-1}}\theta(p^0)\delta(p^2+s),
  \]
  and the null-shell limit at \(s=0\).
- Explained measurability of \(s\mapsto\sigma_s\) against compactly supported
  test functions and absorption of the conditional scalar \(c(s)\) into the
  Kallen--Lehmann measure \(d\rho(s)\).
- Updated the chapter dossier with the new orbit-measure notation and issue
  certification note.

## Verification

Completed after the edit:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 819 pages.
