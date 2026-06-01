# Anomaly WZW descent-coordinate pass

Related issue: GitHub #696, anomaly proof debt in monograph conventions.

## Scope

This pass tightens the logical bridge between the local descent chapter and
the Wess--Zumino--Witten level-matching discussion.  The issue is not the
numerical equality \(n=N_c\) by itself; the missing point was which part of a
counterterm-dependent anomaly representative is actually being compared.

## Manuscript Changes

- Volume II Chapter 20 now records the finite Abelianized Bardeen-counterterm
  algebra
  \[
    d'_{abc}=d_{abc}+\frac12(h_{ab,c}+h_{ac,b}),
    \qquad h_{ab,c}=-h_{ba,c},
  \]
  and the invariant consequence \(d'_{(abc)}=d_{(abc)}\).
- Volume II Chapter 21 now states that the
  \(\operatorname{Tr}(\alpha\,dA\,dA)\) term in the QCD/WZW comparison is the
  lowest-background coordinate of the symmetric descent class, while the
  \(O(A^3)\) terms are the Wess--Zumino-consistent completion inside the same
  class after a counterterm convention is chosen.

## Calculation Check

Extended `calculation-checks/anomaly_matching_wzw_checks.py` to verify with
exact rational arithmetic that the Bardeen shift has zero complete
symmetrization for sample antisymmetric \(h_{ab,c}\).

## Verification

Commands run clean in this pass:

- `python3 calculation-checks/anomaly_matching_wzw_checks.py`
- `python3 -m py_compile calculation-checks/anomaly_matching_wzw_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --list --only anomaly_matching_wzw --skip-wolfram`
- `tools/build_monograph.sh`

The full build is clean at 2812 pages.
