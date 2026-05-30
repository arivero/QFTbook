# Standard Model Top-Higgs Subsystem Quoted-Theorem Pass

Date: 2026-05-30

Scope:
- Volume II, Chapter 19c, former `qthm:sm-one-loop-top-higgs-subsystem`.
- Quoted-theorem audit: perturbative one-loop coefficient packages should not
  masquerade as imported theorems when the local role is a controlled
  minimal-subtraction calculation.

Edits:
- Replaced the quoted theorem with a `controlledapproximation`.
- Added the matrix one-loop pole equations for \(Y_u\) and \(\lambda\) in
  the Standard Model coupling chart.
- Defined the local quantities
  \(T_Y\), \(Q_Y\), and \(G_u\), including the unrescaled
  \(Q=T^3+Y\) hypercharge coefficient.
- Added a coefficient ledger identifying the one-loop diagram classes:
  Yukawa vertex/external-field poles, gauge poles, scalar fish graphs,
  pure-gauge four-Higgs poles, Yukawa-scalar mixed poles, and the closed
  fermion box.
- Derived the rank-one specialization \(Y_u=\operatorname{diag}(0,0,y_t)\),
  giving \(T_Y=3y_t^2\), \(Q_Y=3y_t^4\), and the displayed
  \(\beta_{y_t}\), \(\beta_\lambda\) equations.
- Updated the later Higgs-running remark to refer to the controlled
  approximation rather than a quoted theorem.
- Extended `calculation-checks/standard_model_anomaly_checks.py` to verify the
  rank-one specialization of the matrix equations.
- Updated the calculation-check README and chapter dossier.

Verification:
- `git diff --check`.
- `python3 tools/audit_theorem_form.py`.
- `python3 tools/audit_unnumbered_display_labels.py`.
- `tools/audit_negative_scope_prose.py`.
- `tools/audit_monograph_text.sh`.
- `tools/audit_chapter_dossiers.sh`.
- `python3 calculation-checks/standard_model_anomaly_checks.py`.
- `tools/build_monograph.sh`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2622 pages.

Remaining Boundary:
- This pass does not derive the primitive one-loop Feynman integrals anew in
  the Standard Model chapter.  Those logarithmic pole integrals are part of
  the perturbative renormalization machinery developed earlier.  A future
  electroweak appendix could expand the full component Feynman-rule
  calculation if the chapter needs a completely local diagram-by-diagram
  derivation.
