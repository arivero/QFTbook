# Issue #526 Groomed \(z_g\) Sudakov-Conditioning Pass

## Scope

This pass strengthens the modern jet-substructure treatment in Volume II,
Chapter 19b by adding the groomed momentum-sharing coordinate \(z_g\).  The
new text treats \(z_g\) as a stopping-time observable on the
Cambridge--Aachen declustering tree rather than as an ordinary IRC-safe number
attached to every event.

## Manuscript Change

- Added controlled approximation `ca:sudakov-conditioned-zg`.
- Defined \(z_g\) and \(\theta_g\) as the first soft-drop-accepted split.
- Derived the first-accepted-split density
  \[
    \Delta_i(\vartheta_g)\,
    a_i\overline P_i(z_g)\,
    {d\vartheta_g\over\vartheta_g}\,dz_g
  \]
  with the grooming-support indicator.
- Derived the mMDT limit in which the normalized leading distribution is
  \(\overline P_i(z_g)/\int_{z_{\rm cut}}^{1/2}\overline P_i(z)\,dz\).
- Separated this Sudakov-conditioned statement from fixed-order IRC safety and
  from a full QCD factorization theorem.

## Calculation Check

- Extended `calculation-checks/soft_drop_irc_checks.py` with exact rational
  checks for:
  - normalization of the leading mMDT \(z_g\) weights;
  - cancellation of coupling and finite angular-cutoff dependence after
    conditioning on accepted events;
  - the \(\beta_{\rm SD}>0\) angular-support condition for
    \(z_g<z_{\rm cut}\).

## Verification

Commands run after the edit:

```bash
python3 calculation-checks/soft_drop_irc_checks.py
python3 -m py_compile calculation-checks/soft_drop_irc_checks.py
tools/run_calculation_checks.sh --python-only --only soft_drop_irc
git diff --check
python3 tools/audit_theorem_form.py
python3 tools/audit_unnumbered_display_labels.py
tools/audit_chapter_dossiers.sh
tools/audit_negative_scope_prose.py
tools/audit_monograph_text.sh
tools/build_monograph.sh
```

