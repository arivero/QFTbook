# Issue #848/#725 reflection Gamma-function spectral cell

Date: 2026-06-07

## Scope

This pass addresses the open cigar/Liouville reflection weakness from #848 and
the #725 evidence-independence critique of `reflection_factors()` in
`calculation-checks/susy_2d_lg_glsm_checks.py`.

The repair deliberately stays on the physical spectral side: it does not add
more moduli-space infrastructure.  It evaluates consequences of the imported
supercoset reflection amplitude that affect continuum density and discrete
state normalization.

## Substantive changes

- Replaced symbolic `Counter` cancellation of reflection factors with direct
  Gamma-function evaluation using `mpmath`.
- Checked continuous-series unitarity and `R(j)R(1-j)=1` at generic positive
  levels and admissible momentum/winding labels.
- Extracted the `nu(k)^(2is)` contribution to the reflection phase density and
  rejected the shortcut where `nu(k)` is omitted.
- Recorded that the raw normalization is not finite at the special level
  `k=1`, so a limiting or renormalized operator prescription is required.
- Checked one simple pole residue against the analytic Gamma-residue formula and
  rejected the mutated amplitude with the pole-carrying `Gamma(j+m)` factor
  removed.
- Updated Volume VII Ch09 to present the phase-density and residue consequences
  while preserving the boundary that the Liouville path-integral normalization,
  full continuous measure, all residues, operator completeness, and defect data
  remain open.

## Re-audit boundary

This is evidence for consequences of a declared reflection target, not a
derivation of the target.  It should not be counted as closure of #848.  The
remaining high-value work is to derive the same normalization from a declared
coset two-point function or Liouville path integral, match the full measure and
spin structures, and connect residues to the complete discrete spectrum.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/check_utils_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- focused Volume VII Ch09 theorem-form, unnumbered-display, strict text,
  negative-scope, style-density, and process-leakage audits
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- full `tools/run_calculation_checks.sh --python-only`
- full `tools/build_monograph.sh`
- `git diff --check`
