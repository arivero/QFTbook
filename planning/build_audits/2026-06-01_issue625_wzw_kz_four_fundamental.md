# 2026-06-01 Issue #625 WZW KZ Four-Fundamental Pass

Issue lane: GitHub #625, Volume V two-dimensional CFT depth-pass-B.

## Purpose

The WZW section already derived the Knizhnik--Zamolodchikov equation from
the current Ward identity and the Sugawara translation operator.  This pass
adds the first concrete invariant-space reduction: four fundamental
\(SU(2)_k\) insertions.  The goal is to make the abstract
\(\Omega_{ij}\)-connection visible as an explicit finite Fuchsian system,
with conventions fixed by the WZW current normalization in the chapter.

## Manuscript Changes

- Added the `SU(2) four-fundamental reduction` paragraph to Volume V,
  Chapter 11.
- Fixed the finite-generator convention through the Fierz identity
  \(\sum_a t^a_\alpha{}^\gamma t^a_\beta{}^\delta
    =\delta_\alpha{}^\delta\delta_\beta{}^\gamma
     -\frac12\delta_\alpha{}^\gamma\delta_\beta{}^\delta\).
- Defined the invariant tensors \(\mathcal I_s,\mathcal I_t,\mathcal I_u\)
  and the relation \(\mathcal I_s-\mathcal I_t+\mathcal I_u=0\).
- Displayed the exact actions of \(\Omega_{12}\) and \(\Omega_{23}\) on the
  \((\mathcal I_s,\mathcal I_t)\) basis.
- Wrote the resulting \(2\times2\) KZ system and identified the singlet and
  triplet residue eigenvalues \(-3/2\) and \(1/2\), hence local monodromy
  exponents \(-3/[2(k+2)]\) and \(1/[2(k+2)]\).

## Calculation Check

Extended `calculation-checks/wzw_sugawara_coset_checks.py` to verify:

- the epsilon-tensor invariant relation;
- the \(\Omega_{12}\) and \(\Omega_{23}\) residue matrices on the invariant
  basis;
- the singlet/triplet residue eigenvalues from
  \((C_\mu-2C_{\rm fund})/2\).

## Verification

Run after the edit:

```bash
python3 calculation-checks/wzw_sugawara_coset_checks.py
python3 -m py_compile calculation-checks/wzw_sugawara_coset_checks.py
tools/run_calculation_checks.sh --python-only --only wzw_sugawara_coset
tools/audit_theorem_form.py
tools/audit_unnumbered_display_labels.py
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
python3 tools/audit_negative_scope_prose.py
git diff --check
tools/build_monograph.sh
```

## Scope

This pass does not close #625.  It closes a concrete KZ-example gap in the
WZW/coset section.  Remaining #625 work still includes broader
Cardy--Lewellen sewing beyond rational diagonal cases, further Coulomb-gas
minimal-model integration, and higher-loop nonlinear sigma-model depth.
