# 2026-05-30 DHR/DR Reconstruction Status Pass

## Scope

This pass addresses the quoted-theorem proof-debt concern for the
Doplicher--Roberts reconstruction in Volume IV, Chapter 4.  The theorem is not
demoted: it is a deep theorem of AQFT and categorical duality.  The manuscript
weakness was the insufficient separation between the hypotheses that must be
verified in a QFT example and the compact group / charged field algebra that
the theorem reconstructs.

## Manuscript Change

- Added a reconstruction-logic paragraph after
  `thm:doplicher-roberts-reconstruction`.
- Separated the QFT-specific construction of a rigid symmetric
  `C^*`-tensor category from the Tannakian compact-group duality.
- Displayed the operator relations of the reconstructed charged multiplets:
  the charged-field intertwining relation, the Cuntz-type normalization, the
  recovery formula for the DHR endomorphism, and the compact-group action on
  a charged multiplet.
- Recorded the theorem boundary: bounded-region DHR sectors with finite
  statistics are the input category.  Long-range Gauss-law sectors,
  Wilson-line/spacelike-cone localization, infraparticles, and confining
  charged objects require a different localization category before an
  analogous reconstruction or Haag--Ruelle scattering statement can be asked.

## Issue Alignment

- #695: improves the AQFT quoted-theorem proof-boundary audit without
  pretending to supply the full DR proof.
- #527/#528: cross-links conceptually to the charged-sector Haag--Ruelle/LSZ
  program by making clear that Wilson-line charged sectors are outside the
  bounded-region DHR hypothesis package.
- #691: preserves a genuinely deep quoted theorem while removing possible
  wrapper ambiguity around its hypotheses and outputs.
