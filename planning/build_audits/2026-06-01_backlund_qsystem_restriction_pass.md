# Bäcklund Q-System Restriction Pass

## Scope

Volume VI Chapter 5B; live backlog connections #624, #562, and #564.

## Edit

Inserted a section explaining Bäcklund elimination as a precise finite
Q-system operation.  For a Q-system \(\{Q_A\}_{A\subset I}\) and a color
\(c\in I\), the restricted family
\[
  Q^{(c)}_A=Q_{A\cup\{c\}},
  \qquad A\subset I\setminus\{c\},
\]
obeys the same local QQ-relation on the smaller index set.  The text explains
how this local restriction mirrors recursive nested monodromy and why the
restricted empty function \(Q^{(c)}_\varnothing=Q_c\) forces a separate
normalization/gauge discussion before one interprets the reduced problem as a
polynomial Bethe problem or QSC analytic chart.

The pass intentionally does not promote the local identity to theorem-family
rank.  The algebra is the original Plücker/QQ relation with a larger base
subset; the QFT-relevant content is the explicit separation between local
Bäcklund algebra and analytic normalization data.

## Calculation Check

Extended `calculation-checks/nested_integrability_checks.py` with a finite
determinant check: for each removed color in a four-color Wronskian Q-system,
the Q-functions containing that color satisfy the smaller QQ-system at
sample spectral points.

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
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages:           2806`.
