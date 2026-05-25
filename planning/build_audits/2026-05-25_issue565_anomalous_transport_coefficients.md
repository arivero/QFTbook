# 2026-05-25 Issue 565: Anomalous Transport Coefficients

## Scope

Issue #565 flagged that Volume X Chapter 9 defined anomalous transport but did
not display the chiral magnetic coefficient or a calculation check.

## Edits

- Added vector/axial source conventions and the translation from
  source-normalized currents to a physical electromagnetic current with
  charge \(Q=eq\).
- Derived the chiral magnetic coefficient from the thermal reduction of the
  vector-vector-axial inflow term:
  \(J_V^i=\mu_A B_V^i/(2\pi^2)\).
- Translated the result to the electromagnetic response
  \(J_{\rm em}^i=e^2q^2\mu_A B_{\rm em}^i/(2\pi^2)\).
- Added an independent lowest-Landau-level derivation of the same coefficient.
- Added the Dirac chiral vortical coefficients and explicitly recorded that
  the universal \(T^2\) contribution cancels in the vector current and appears
  in the axial vortical current.
- Added `calculation-checks/anomalous_transport_checks.py`.

## Targeted Verification

```text
python3 calculation-checks/anomalous_transport_checks.py
All anomalous-transport coefficient checks passed.
```

## Full Verification

```text
tools/audit_monograph_text.sh
Strict monograph text audit clean.

tools/audit_chapter_dossiers.sh
Chapter dossier metadata audit clean.

git diff --check

tools/build_monograph.sh
Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf

pdfinfo monograph/tex/main.pdf
Pages:           1281
```
