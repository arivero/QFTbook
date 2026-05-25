# 2026-05-25 Issue #471: Gauge-Higgs Solitons

## Scope

GitHub issue #471 requested magnetic monopoles, the 't Hooft--Polyakov
monopole, BPS monopoles, vortices, and sphalerons.  The issue title referred
to Volume IV, but the current repository volume map places classical
Yang--Mills and matter fields in
`monograph/tex/volumes/volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`;
the present Volume IV is the axiomatic/nonperturbative-framework volume.

## Manuscript Changes

- Added Section `Finite-Energy Gauge-Higgs Solitons` to the classical
  Yang--Mills chapter.
- Defined the smooth finite-energy gauge-Higgs sector, the vacuum orbit
  \(\mathcal O_v\), stabilizer \(H\), and asymptotic boundary map
  \(S^2_\infty\to G/H\).
- Derived the magnetic-sector classification
  \(\pi_2(G/H)\simeq\pi_1(H)\) under the stated simply-connected hypothesis on
  \(G\), with \(SU(2)\to U(1)\) as the canonical monopole example.
- Derived the BPS energy bound by square completion in trace-form
  normalization:
  \[
    E\ge {4\pi\over g_{\mathrm{YM}}^2}|\Gamma_{\mathrm m}|,
    \qquad
    \Gamma_{\mathrm m}={1\over 4\pi}
      \int_{S^2_\infty}\operatorname{tr}(\Phi B_i)\,\dd S_i.
  \]
- Stated the \(SU(2)\) integer-sector bound only after fixing the primitive
  magnetic cocharacter, avoiding a hidden conflict with the monograph's
  non-half-trace generator convention.
- Added the hedgehog ansatz, radial Bogomolny ODEs, and the explicit
  Prasad--Sommerfield profile
  \(K(\rho)=\rho/\sinh\rho\), \(H(\rho)=\coth\rho-\rho^{-1}\).
- Added the Abelian-Higgs Nielsen--Olesen vortex, the critical-coupling BPS
  completion, flux quantization, and vortex equations.
- Added the spatial Chern--Simons functional and the classification of the
  sphaleron as an unstable finite-energy saddle.
- Added two TikZ figures: the boundary-map/topological-sector diagram and the
  Bogomolny-square-completion diagram.
- Updated the classical Yang--Mills chapter dossier with the new definitions,
  claims, and figure requirements.

## Normalization Check

The section deliberately phrases the monopole mass bound first in terms of the
trace-form surface charge \(\Gamma_{\mathrm m}\).  The familiar
\(4\pi v|n|/g^2\) form is not written until a primitive magnetic generator has
been fixed, because the scalar called \(v\) depends on the chosen matrix
normalization for the \(SU(2)\) Cartan generator.  This keeps the result
consistent with the chapter convention
\[
  \mathcal L_{\mathrm{YM}}
  =-\frac{1}{4g_{\mathrm{YM}}^2}\operatorname{tr}(F_{\mu\nu}F^{\mu\nu}),
  \qquad
  \operatorname{tr}(t^a t^b)=\delta^{ab}
\]
unless another normalization is explicitly declared.

## Verification

Completed after the edit:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 816 pages.
