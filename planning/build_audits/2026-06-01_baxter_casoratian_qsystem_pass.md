# Baxter Casoratian Q-System Pass

## Scope

Volume VI Chapter 5B; live backlog connections #624, #562, and #564.

## Edit

Added a rank-one Baxter Casoratian section between the scalar \(TQ\)
relation and the higher-rank QQ-system.  The section treats the Baxter
relation as a genuine second-order finite-difference equation, defines the
half-shift Casoratian of two solutions, and proves the transport identity
\[
  d(u)\mathcal W(u+\ii/2)=a(u)\mathcal W(u-\ii/2).
\]
The text then specializes the result to the homogeneous \(XXX_{1/2}\)
normalization and explains why the companion Baxter solution is part of the
finite-difference datum behind Wronskian \(Q\)-systems and the later QSC
language.

## Calculation Check

Extended `calculation-checks/nested_integrability_checks.py` with an exact
rational recurrence check: two independent solutions of the same
second-order finite-difference equation satisfy the Casoratian transport
identity site by site.

## Verification

- `python3 calculation-checks/nested_integrability_checks.py`: passed.
- `python3 -m py_compile calculation-checks/nested_integrability_checks.py`: passed.
- `git diff --check`: passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `python3 tools/audit_unnumbered_display_labels.py`: passed.
- `tools/audit_negative_scope_prose.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages:           2804`.
