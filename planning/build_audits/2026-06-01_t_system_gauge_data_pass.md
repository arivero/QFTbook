# T-System Gauge Data Pass

## Scope

Volume VI Chapter 5B; live backlog connections #624, #562, and #564.

## Edit

Inserted a T-system gauge and analytic-data layer after the local Hirota and
Y-system derivation.  The new section defines T-gauge transformations
\[
  T_{a,s}\mapsto
  g_1^{[a+s]}g_2^{[a-s]}g_3^{[-a+s]}g_4^{[-a-s]}T_{a,s},
\]
derives the shared Hirota cocycle multiplier, proves in prose that
Y-functions are invariant under this gauge freedom, and defines an analytic
T-system datum as more than the local bilinear identity: gauge, boundary
functions, quantum determinant factors, zero/pole/cut/asymptotic data, and
the map to physical charges or transfer eigenvalues.

The purpose of the pass is to prevent the later QSC and TBA discussions from
treating Hirota algebra as if it were already a spectral construction.  The
local determinant identities are the algebraic skeleton; analytic data are
where the physical theory enters.

## Calculation Check

Extended `calculation-checks/nested_integrability_checks.py` with an exact
rational check of T-gauge covariance: all three Hirota monomials acquire the
same gauge factor, the Hirota residual scales by that factor, and the
Y-functions are invariant.

## Verification

- `python3 calculation-checks/nested_integrability_checks.py`: passed.
- `python3 -m py_compile calculation-checks/nested_integrability_checks.py`:
  passed.
- `git diff --check`: passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `python3 tools/audit_unnumbered_display_labels.py`: passed.
- `tools/audit_negative_scope_prose.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed after replacing the local `\Z` shorthand
  by `\mathbb Z`; rebuilt `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages:           2805`.
