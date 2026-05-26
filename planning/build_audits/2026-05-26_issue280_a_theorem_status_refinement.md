# Build Audit: Four-Dimensional A-Theorem Status Refinement

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #280 status refinement, prompted by the monograph-wide rigor
standard for physical arguments.

## Scope

This pass sharpens the Volume III Chapter 01 discussion of the
Komargodski--Schwimmer dilaton effective-action argument.  The previous text
already stated S-matrix assumptions, but some phrasing could still be read as
promoting the dilaton construction to a theorem-level proof.  This pass makes
the status boundary explicit.

## Substantive Changes

- Rephrased the four-dimensional \(a_{\rm W}\) paragraph as a conditional
  dilaton-dispersion argument, not as a theorem-level proof from general
  four-dimensional QFT axioms.
- Listed the load-bearing assumptions: endpoint CFTs, a renormalized
  stress-tensor source functional along the flow, controlled weak spectator
  dilaton decoupling, an infrared prescription, analyticity, crossing,
  polynomial boundedness, unitarity, and contour control.
- Rephrased the dispersion identity as a formal sum rule under these
  assumptions, and the interpolating \(a(\mu)\) as a conditional scattering
  object rather than an intrinsic nonperturbative local RG \(c\)-function.
- Updated the Chapter 01 dossier so future agents do not treat the
  dilaton-effective-action story as a rigorous universal \(a\)-theorem proof.

## Verification

- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/run_calculation_checks.sh`: passed.
- `tools/build_monograph.sh`: passed with clean TeX log scan.
- `pdfinfo monograph/tex/main.pdf`: 1557 pages, 6157213 bytes.

## Status

This does not reopen #280 by itself; it corrects the epistemic status of the
material added for that issue.
