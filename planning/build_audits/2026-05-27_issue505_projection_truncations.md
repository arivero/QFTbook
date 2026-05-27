# Issue #505 Projection-Truncation Checkpoint

## Scope

This checkpoint strengthens the rigorous Wilsonian RG chapter by turning the
warning about finite-dimensional RG truncations into labeled mathematical
statements.

## Manuscript Changes

- Added a section on projection truncations and residual control in Volume XI,
  Chapter 7.
- Defined the projected RG fixed-point equation
  \(P_NF(V_N)=0\), the complementary projection \(Q_N=1-P_N\), and the
  complement residual \(\epsilon_N(V_N;A)=\|AQ_NF(V_N)\|\).
- Proved by explicit finite-dimensional example that a projected RG zero can
  be spurious and need not imply a fixed point of the full RG map.
- Proved the corollary that a projected zero lifts to a true fixed point only
  after the complement residual and the Newton--Kantorovich constants satisfy
  the full Banach-space contraction inequalities.

## Companion Check

- Added `calculation-checks/rg_projection_checks.py`, using exact rational
  arithmetic to verify the spurious projected-zero example and the
  complement-residual lift calculation.

## Verification

- `python3 calculation-checks/rg_projection_checks.py`: passed.
- `python3 -m py_compile calculation-checks/rg_projection_checks.py`: passed.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; final PDF at
  `monograph/tex/main.pdf` with 2084 pages.
