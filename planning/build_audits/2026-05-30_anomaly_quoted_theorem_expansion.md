# 2026-05-30 Anomaly Quoted-Theorem Expansion

## Scope

This pass continues the quoted-theorem proof-debt audit for #696.  It targets
two convention-sensitive QFT anomaly theorem boundaries:

- the cubic perturbative gauge obstruction in Volume II, Chapter 20;
- the ghost-number-one BV anomaly obstruction in Volume II, Chapter 24.

## Manuscript Change

- Added the local descent mechanism after the cubic gauge-obstruction quoted
  theorem:
  - \(\mathsf F^a\) are even two-forms, so
    \(\operatorname{tr}_R(\mathsf F^3)\) depends on the symmetric cubic
    tensor;
  - the ghost insertion form
    \(\operatorname{tr}_R(t^a\{t^b,t^c\})\) is identified as the same tensor
    in the Ward-identity normalization;
  - the descent equations and counterterm shifts are displayed;
  - the local BRST cohomology classification input is named as the step that
    makes a nonzero tensor a genuine local obstruction.
- Added the QME-to-descent mechanism after the BV ghost-number-one anomaly
  quoted theorem:
  - wrote the first nonzero QME defect as a local ghost-number-one four-form;
  - derived its relative-cocycle condition from the linearized BV differential
    and the Jacobi identity;
  - displayed the local counterterm shift;
  - connected the BV class to the ordinary consistent gauge anomaly through
    the BV--BRST comparison and descent from
    \(\frac{\ii}{24\pi^2}\operatorname{Tr}_R(\mathsf F^3)\).

## Remaining Proof Debt

This pass improves #696 but does not close it.  The monograph still needs
deeper local derivations for finite \(SU(2)\) global anomaly phases, WZW level
matching, determinant/Pfaffian-line holonomies, APS/eta convention bridges,
and any remaining anomaly-related quoted theorem boundaries.
