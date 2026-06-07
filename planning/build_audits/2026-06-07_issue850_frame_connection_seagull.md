# 2026-06-07 Issue #850 Frame-Connection Seagull

## Scope

This pass continues the Volume VII Chapter 08 Higgs-branch metric repair.  The
previous #850 increment derived the constant-background `R_xi`
longitudinal/Goldstone/ghost determinant cancellation from generated quadratic
operators.  The next determinant-level gap is the tangent-vertex/seagull pairing
created by a slowly varying Higgs background.

## Change

Chapter 08 now adds `ex:higgs-branch-frame-connection-seagull`.  For a regulated
heavy fluctuation block whose slowly varying Higgs tangent only changes the
orthonormal heavy-field frame,

```text
O(s) = U(s) O_0 U(s)^{-1},
```

the text derives

```text
dot O = [T,O_0],
ddot O = [T,[T,O_0]],
STr(O_0^{-1} ddot O - O_0^{-1} dot O O_0^{-1} dot O) = 0.
```

This identifies the seagull and the double insertion as the two Taylor
coefficients of the same covariant operator.  Dropping the seagull is therefore
a spurious source of Higgs-metric terms, not an allowed simplification.

## Companion

`susy_moduli_space_checks.py` now constructs a finite exact matrix example of
the same trace-log identity.  It derives the linear insertion and seagull from a
single conjugating generator, verifies exact cancellation, and includes two
negative controls:

- omitting the seagull leaves a nonzero trace-log residual;
- adding genuine mass curvature leaves a nonzero residual, so the check does
  not erase the actual remaining `Pi_mn` calculation.

## Quality Boundary

This is a determinant-infrastructure calculation, not a replacement for the
full Higgs-branch metric theorem.  It closes the pure moving-frame part of the
tangent-dependent trace-log.  The remaining mass-curvature, auxiliary-contact,
fermion, mixed-diagram, and all-order Ward/counterterm pieces remain open #850
obligations.

## Verification Plan

- Run the focused `susy_moduli_space_checks.py` companion and `py_compile`.
- Run focused Chapter 08 theorem/display/prose/style audits.
- Run calculation evidence/inventory and chapter-dossier audits.
- Run full Python calculation checks and full monograph build/log scan before
  staging.

## Verification Result

Completed on 2026-06-07.  The focused moduli-space companion,
`py_compile`, Chapter 08 theorem-form, display-label, negative-scope, and
style-density audits, calculation evidence-contract and inventory audits,
chapter-dossier audit, full strict monograph text harness, full Python
calculation suite, `git diff --check`, and full monograph build/log scan all
passed before staging.  The first full build caught one overfull paragraph in
the new scope sentence; the paragraph was shortened and the build/log scan then
passed cleanly.
