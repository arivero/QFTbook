# Foundational Framework Maps

Date: 2026-05-21

## Scope

This pass strengthened the beginning of Volume I after the subject-volume
reorganization.

- Added a new opening section on Wightman, local-net, and Euclidean
  presentations of local QFT.
- Added a comparison-map figure showing Wightman fields, local nets,
  Euclidean data, and the Hilbert-space vacuum sector.
- Added an AQFT section explaining how a local net plus a state produces
  bounded local correlation functions, and how point fields require
  additional affiliation or limiting data.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- Deferred-topic scan over `monograph/tex/volumes`: clean.
- Hard-coded chapter-number prose scan over reader-facing TeX: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 328 pages.
