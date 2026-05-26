# Issue #587 Anomaly Polynomial And Inflow Development

## Scope

- GitHub issue: `#587`, Block D anomaly computations.
- Manuscript loci:
  - `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
  - `monograph/tex/volumes/volume_ix/chapter06_anomaly_inflow_invertible_field_theories.tex`
- Calculation-check locus:
  - `calculation-checks/anomaly_polynomial_descent_checks.py`

## Content Added

- Added an index-normalized anomaly-polynomial section to Volume II Chapter 20.
  It defines \(\mathcal I_6=[\widehat A(TM)\operatorname{ch}_R(E)]_6\),
  expands it to the cubic gauge/flavor term and the mixed
  gauge-gravitational term, and relates the index normalization to the
  \(2\pi i\) effective-action descent normalization.
- Added explicit \(U(1)\), \(SU(N)\), and one-generation Standard Model
  examples, including cubic, mixed gravitational, mixed nonabelian-\(U(1)\),
  and finite \(SU(2)\) checks.
- Added a proposition formulating anomaly matching as equality of anomaly
  lines under RG flow, modulo local counterterm lines.
- Expanded Volume IX Chapter 6 with a coefficient-level five-dimensional
  inflow derivation for a four-dimensional left-handed Weyl fermion and the
  explicit abelian inflow action
  \[
    -2\pi i\int_X
    \left[
      q^3 A F^2/(6(2\pi)^3)
      -
      q A p_1(TX)/(24(2\pi))
    \right].
  \]
- Added a precise construction-level discussion of noninvertible chiral
  defects as anomaly-trivialized transformation walls, with compact-QED axial
  defects linked to the detailed Volume IX Chapter 11 construction.
- Updated the Volume II and Volume IX chapter dossiers and the calculation
  check index.

## Verification

- `python3 calculation-checks/anomaly_polynomial_descent_checks.py`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- Independent scan of `monograph/tex/main.log` and
  `monograph/tex/build/latexmk.out` for unresolved references/citations,
  TeX errors, overfull/underfull boxes, and hyperref token warnings.
- `pdfinfo monograph/tex/main.pdf` reports 1440 pages.
