# 2026-06-08 Issue #886/#887 Kinetic Shell and Collision Measure Audit

## Scope

Addressed the linked Volume X Chapter 8 kinetic-normalization issues:

- #886: invariant quasiparticle pole normalization and positive-shell
  projector.
- #887: scalar sunset full-product collision-measure factor and
  microreversibility hypothesis for the H theorem.

This pass deliberately stayed inside the physics architecture of kinetic
theory: Wigner projection, SK cut self-energies, phase-space measure,
Boltzmann kernel, and entropy production.  It did not add a tangent
mathematical cell or a new model unrelated to transport.

## Substance

- Restored the invariant mass-shell Jacobian:
  \(\delta((p^0)^2-E^2)=\frac1{2E}[\delta(p^0-E)+\delta(p^0+E)]\).
- Changed the force-free positive-shell projector from \(1/Z\) to \(2E/Z\).
- Corrected the scalar sunset counting: three negative-energy-line choices
  turn \(1/3!\) into \(1/2\); the outgoing \(p_3 \leftrightarrow p_4\)
  exchange is a full-product-measure relabeling, not an additional
  contraction.
- Propagated the factor into the scalar covariant kernel:
  self-energy weight \(\lambda_R^2/2\), KB collision projection \(1/2\),
  full-product covariant collision weight \(\lambda_R^2/4\).
- Replaced the generic "matrix element equals kernel weight" wording with a
  transition-measure convention \(\mathcal W_{ab;cd}\) that owns shell
  projection, identical-particle divisors, ordered/quotient conventions,
  spin/color data, and regulator/medium data.
- Made the channelwise H theorem explicitly conditional on
  \(\mathcal W_{ab;cd}(1,2;3,4)=\mathcal W_{cd;ab}(3,4;1,2)\).

## Re-Audit

- Physics depth: this pass changes the physical collision operator and its
  entropy proof, rather than adding another finite identity adjacent to the
  existing text.
- Coherence: the same shell and transition-measure convention now appears in
  the pole ansatz, KB projection, scalar cut derivation, general Boltzmann
  kernel, detailed-balance paragraph, entropy proof, hydrodynamic moments,
  calculation checks, evidence contract, and dossier.
- Scope restraint: no directive text was added to monograph TeX.  Planning
  and audit material stayed in planning files.
- Residual frontier: gauge-theory kinetic theory still needs a separate hard,
  soft, collinear, and LPM matching architecture; this scalar repair should
  not be read as that theorem.

## Verification

- `python3 calculation-checks/kinetic_theory_checks.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter08_kinetic_theory_controlled_limit.tex --fail`
- `bash tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter08_kinetic_theory_controlled_limit.tex`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

All listed commands passed after replacing plain-TeX `\over` fractions in the
new equations with `\frac{...}{...}`.
