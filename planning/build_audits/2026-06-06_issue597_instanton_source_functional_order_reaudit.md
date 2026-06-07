# 2026-06-06 Issue #597 Instanton Source-Functional Order Re-Audit

## Scope

- Target: `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Planning companion: `planning/chapter_dossiers/volume_ii/chapter20d_instantons_physical_amplitudes.md`.
- Issue connection: #597 dedicated instanton physics, with the user constraint
  that instantons should be developed as QFT amplitudes and observables rather
  than as moduli-space geometry alone.

## Finding

The dedicated instanton chapter already contains the amplitude-facing
machinery: source functional, density normalization, zero-mode selection,
proper-time determinant, hard four-source benchmark, Wilsonian OPE split,
normal-fluctuation source response, physical projection, cluster correction,
and observable maps.

The coherence problem was at the chapter entrance.  The opening calculation
order still said the density comes first, while the actual chapter now begins
with the finite-regulator source functional.  That wording weakened the
physics priority by making the fluctuation density sound like the first
object, rather than one input to a source-channel amplitude.

## Repair

- Corrected the opening order-of-calculation paragraph so the source
  functional is first, followed by density normalization, channel data, the
  hard benchmark, normal-fluctuation source response, cluster corrections, and
  observable maps.
- Changed visible architecture wording from finite-regulator datum to
  finite-regulator inputs, from Wilsonian OPE datum to Wilsonian OPE input,
  from hard amplitude assembly bound to hard amplitude assembly control, and
  from prescription/window-stability datum to input.
- Preserved labels and all equations.

This is a chapter-flow and physics-architecture pass, not a new calculation
cell.  No calculation companion needed to change because no formula or
finite-check claim changed.

## Verification Plan

- Focused Ch20D style-density audit.
- Focused theorem-form, display-label, negative-scope, and process-language
  scans.
- Dossier and strict monograph text audits.
- Full monograph build.
