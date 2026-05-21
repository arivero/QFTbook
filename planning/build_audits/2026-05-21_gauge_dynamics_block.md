# 2026-05-21 Gauge Dynamics Block

## Scope

Expanded the next compiled Volume II block after classical Yang--Mills theory:

- Gauge fixing, Faddeev--Popov ghosts, BRST differential, physical cohomology,
  and Slavnov--Taylor identities.
- QCD renormalization, one-loop asymptotic freedom, dimensional
  transmutation, physical color-singlet external states, deep inelastic
  current correlators, OPE, parton distributions, and DGLAP evolution.
- Axial anomalies, Fujikawa measure derivation, nonabelian anomaly
  coefficients, gauge-anomaly cancellation, and the invariant strong CP
  parameter.
- Global anomalies, anomaly matching, spontaneous symmetry breaking, chiral
  symmetry of massless QCD, pion effective actions, and the
  Wess--Zumino--Witten functional.

## Reader-Facing Inclusion

The four chapters are now included after
`chapter17_yang_mills_theory_and_matter_fields.tex` in
`volume_ii_current.tex`.

## Verification

Ran:

```bash
tools/build_monograph.sh
```

Result:

- strict monograph text audit clean;
- cross-references resolved after the latexmk rerun;
- final LaTeX log scan clean;
- compiled PDF produced at `monograph/tex/main.pdf`.

## Next Local Target

The next systematic gap is the omitted 1PI renormalization-group chapter file,
followed by completing the QCD/anomaly sequence with dedicated chapters for
factorization refinements, topological terms, and low-energy chiral dynamics
if the current combined chapters are later split into the full provisional
architecture.
