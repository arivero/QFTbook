# General ADHM Quotient Pass

Date: 2026-06-01

Issue lane: #597.

## Scope

This pass advances the instanton part of the soliton/monopole/instanton
issue.  The manuscript already contained the BPST solution, the charge-one
ADHM chart, the charge-one orientation cone, and the one-instanton running
density.  The missing local layer was the general charge-\(k\) ADHM quotient
datum and its \(4kN_c\) dimension count before specializing to \(k=1\).

## Manuscript Changes

- Added Definition `def:framed-adhm-quotient-datum` in Volume II,
  Chapter 20.
- Defined the vector spaces \(W\simeq\mathbb C^{N_c}\) and
  \(K\simeq\mathbb C^k\), the ADHM variables
  \((B_1,B_2,I,J)\), the complex and real moment maps, the \(U(K)\) action,
  and the stability condition.
- Added Proposition `prop:adhm-quotient-dimension-count`, proving the local
  real dimension \(4kN_c\) at smooth stable transverse points by an explicit
  variables-minus-equations-minus-quotient count.
- Identified the two complex trace parts of \(B_1,B_2\) as the four center
  coordinates and the centered dimension as \(4kN_c-4\).
- Added the Uhlenbeck boundary interpretation: a degeneration in which a
  subspace of \(K\) decouples from the framing records pointlike collapsed
  instanton charge, with strata
  \(\mathcal M_{k-\ell,N_c}^{\rm smooth}\times
  \operatorname{Sym}^{\ell}(\mathbb R^4)\).

## Calculation Check

Extended `calculation-checks/bpst_instanton_normalization_checks.py` with
finite arithmetic checks for:

- the general charge-\(k\) framed ADHM quotient dimension \(4kN_c\);
- the centered dimension \(4kN_c-4\);
- the decomposition of the two complex trace parts of \(B_1,B_2\) as four
  center coordinates.

Updated the calculation-check README and the Volume II Chapter 20 dossier.

## Verification

Targeted verification should include:

```bash
python3 calculation-checks/bpst_instanton_normalization_checks.py
python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py
git diff --check
python3 tools/audit_theorem_form.py
python3 tools/audit_unnumbered_display_labels.py
tools/audit_negative_scope_prose.py
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
tools/build_monograph.sh
```

This pass does not close #597.  It supplies the general ADHM quotient and
dimension layer, but #597 still includes determinant constants in specified
schemes, the actual multi-instanton measure beyond dimension counting,
compactification/boundary-stratum estimates for the path integral, and
further soliton and monopole quantization material.
