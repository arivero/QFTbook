# Core Depth Pass 4

Date: 2026-05-21

Scope: continue deepening the compiled core monograph while preserving the
logic that scattering is defined before LSZ and perturbative amplitudes, and
while keeping deferred frontier topics outside the active volume includes.

## Content Added

- Added a connected-truncation and external-amputation section to LSZ
  reduction, separating cumulants, external one-particle residue extraction,
  and scattering matrix elements.
- Added crossing from locality and tube analyticity to the analyticity
  chapter, tying crossed scattering regions to boundary values of one
  analytically continued four-point function after LSZ.
- Added the Callan--Symanzik equation as the action of the RG vector field on
  renormalized connected correlation functions, including field anomalous
  dimension and the multi-coupling form.
- Added explicit Wightman reconstruction formulas for the finite-sequence
  vector space, Wightman inner product, null quotient, field action, vacuum,
  and Poincare representation.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- Deferred-topic scan over `monograph/tex/volumes`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

Result: strict text audit clean; monograph build and log scan clean after
rewrapping the LSZ reduction-chain display.

PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 312 pages.
