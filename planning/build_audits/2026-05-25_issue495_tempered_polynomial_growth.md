# Issue 495 Tempered Polynomial Growth Audit

## Scope

This pass advances GitHub issue #495 by proving the boundedness statement that
follows directly from Wightman temperedness and LSZ boundary values, while
separating it from stronger fixed-\(t\) and angular-tube pointwise bounds.

## Edits

- Expanded
  `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`
  at the start of the polynomial-boundedness section.
- Added a proposition proving that a tempered distribution is bounded by a
  finite Schwartz seminorm and therefore has polynomially bounded pairings
  with translated high-energy packets
  \(\varphi_{R,\Delta}(s)=\Delta^{-1}\varphi((s-R)/\Delta)\).
- Added a fixed-\(t\) LSZ corollary: after stable-particle pole terms are
  separated, a tempered fixed-\(t\) boundary value obeys
  \[
    |\langle\mathcal M_t,\varphi_{R,\Delta}\rangle|
    \le C_{\varphi,t}(1+|R|+\Delta)^{N_t}.
  \]
- Clarified that this distributional statement is what Wightman temperedness
  supplies immediately.  Pointwise cut-plane polynomial boundedness
  (Jin--Martin type) and the positive-\(t\) angular-tube boundedness used in
  Froissart--Martin are stronger analytic inputs.
- Updated the Volume II Chapter 7 dossier with the new symbols, claim, and
  audit note.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean rebuild with log scan.
- `pdfinfo monograph/tex/main.pdf`: 1308 pages, generated 2026-05-25.

## Issue Status

Issue #495 should remain open after this pass.  The monograph now contains a
self-contained proof of the distributional polynomial bound derivable from
temperedness.  A complete self-contained proof of the Jin--Martin fixed-\(t\)
pointwise theorem would require the full Jost--Lehmann--Dyson/Bros--Epstein--
Glaser/Lehmann--Martin analytic machinery and remains a later deep pass.
