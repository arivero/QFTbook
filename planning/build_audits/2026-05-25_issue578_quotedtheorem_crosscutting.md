# Build Audit: Issue 578 Quoted-Theorem Cross-Cutting Pass

Date: 2026-05-25

## Scope

Addressed GitHub issue #578 by checking the named theorem-boundary examples
and converting the remaining ordinary theorem environments that were not
locally proved.

## Changes

- `volume_viii/chapter02_bordism_functoriality_extended_tqft.tex`: converted
  the cobordism hypothesis from `theorem` to `quotedtheorem` and stated that
  it is used as target-category boundary data rather than proved locally.
- `volume_xii/chapter04_unruh_effect_modular_theory.tex`: converted the
  Bisognano--Wichmann boundary statement from `theorem` to `quotedtheorem`
  and separated the quoted AQFT theorem from the free-field detector check.
- Updated the Volume VIII and Volume XII chapter dossiers to record the
  quoted-theorem status.
- Rechecked the earlier named issue instances: the `Phi^4_3` constructive
  output theorem and the stochastic-quantization theorems were already
  converted to `quotedtheorem` in earlier issue passes.

## Verification

- `rg -n "Proof architecture|Why this is the needed theorem|Proof of the mechanism"`
  over `monograph/tex/volumes`: no remaining matches.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 1259 pages.
