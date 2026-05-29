# Build Audit: KW Beta-Function Rank Count

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #605, with overlap for #588's four-dimensional
\(\mathcal N=1\) gauge-dynamics foundation.

## Scope

This pass strengthens the field-theoretic Klebanov--Witten conformal-manifold
discussion in Volume VII Chapter 06.  The chapter already stated the local
conformal manifold as a quoted continuum-SCFT theorem.  This pass adds the
necessary beta-function rank-count arithmetic that the theorem must satisfy.

## Source And Convention Notes

- The calculation is entirely inside four-dimensional \(\mathcal N=1\)
  field theory.
- No superstring, compactification, D-brane, holographic, or AdS/CFT
  derivation is used.
- The result is a necessary local beta-function count in the
  \(SU(2)_A\times SU(2)_B\times U(1)_B\)-preserving source chart.  It is not
  a proof that the continuum fixed point exists, that an RG trajectory reaches
  it, or that the conformal manifold is nonsingular.

## Substantive Changes

- Added the KW beta-function rank-count calculation.
- Derived
  `B_1=B_2=N(1+gamma_A+gamma_B)` for the two KW gauge-factor NSVZ
  numerators.
- Derived the quartic-superpotential marginality defect
  `B_h=1+gamma_A+gamma_B` from the chiral-operator dimension condition.
- Recorded that the three local vanishing conditions have rank one in the
  symmetry-preserving source chart, and reduce to `gamma=-1/2` at the
  exchange-symmetric point.
- Extended `susy_n1_conifold_checks.py`, the calculation-check README, and
  the Chapter 06 dossier.

## Verification

- `python3 calculation-checks/susy_n1_conifold_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed with clean TeX log scan.
- `pdfinfo monograph/tex/main.pdf`: 1558 pages, 6160899 bytes.

## Status

This advances #605 but does not close it.  The full conformal-manifold
existence statement remains a quoted nonperturbative continuum-SCFT input.
