# 2026-06-06 Issue #597 Hori--Vafa Degree-d Iteration Audit

## Scope

- Volume VII Chapter 9 now extends the projective-space instanton comparison
  from the degree-one stable-map/vortex assembly to the protected
  degree-`d` observable `R(H^{N-1+dN}) = q_phys^d`.
- The new TeX block treats the mirror residue as a prediction to be matched
  by a direct A-twisted sector calculation, not as a derivation that bypasses
  collective-coordinate measure, determinant-line, zero-mode, gluing,
  compactification, operator-map, and contact-term data.
- The pass is deliberately physics-facing: the residual telescope is organized
  around the amplitude/observable assembly that a direct instanton
  computation must control.

## Companion Check

- `calculation-checks/susy_2d_lg_glsm_checks.py` adds
  `check_cp_degree_d_quantum_product_iteration`.
- The check verifies the exact residue and quantum-product trace identity
  through finite rational arithmetic.
- Negative controls reject bare-FI powers, iterated line-count-only
  arguments, omitted gluing residuals, omitted off-pairing leakage, and
  unsaturated residual-zero-mode gates.

## Re-audit Notes

- The new material is placed after the existing degree-one stable-map
  incidence residual template and before the cigar/Liouville section, so it
  consolidates the projective-space instanton argument rather than scattering
  another local lemma elsewhere.
- Process notes remain in planning files only.  The monograph TeX states the
  physics comparison and residual equations without issue-tracker or planning
  directives.
