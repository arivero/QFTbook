# Seiberg-Witten Hypermultiplet Monodromy Factor-Two Pass

Date: 2026-05-30.

## Scope

- Chapter:
  `monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`.
- Issue context: continuing the proof-substance and theorem-boundary audit,
  with relevance to GitHub #626 and #691.

## Defect Addressed

The rank-one hypermultiplet monodromy lemma previously invoked the phrase
"a massless hypermultiplet contributes twice the primitive
Picard-Lefschetz shift" without deriving the factor two.  That was too close
to a memorized Seiberg-Witten convention: the proof used the correct matrix,
but the load-bearing normalization was hidden.

## Edit

- Added a local electric-frame derivation for a primitive light charge
  `gamma`.
- Chose a symplectic complement `eta` with `<eta,gamma>=1` and set
  `z=Z_gamma`, `z_D=Z_eta`.
- Displayed the singular Wilsonian threshold of a charge-one
  `N=2` hypermultiplet,
  `tau_sing(z)=-(i/pi) log z` up to single-valued holomorphic terms.
- Derived the local monodromy `z_D -> z_D+2 z`.
- Used the decomposition `delta=k eta+ell gamma`,
  `k=<delta,gamma>`, to derive
  `Z_delta -> Z_delta + 2 <delta,gamma> Z_gamma`.
- Re-derived the displayed matrix in the original `(a_D,a)` period basis and
  then checked symplecticity and unipotence.
- Extended `calculation-checks/sw_su2_periods.py` so the factor-two local
  threshold is executable, not only textual.

## Status

This pass does not close #626 or #691.  It removes one additional compact
proof-boundary weakness in the supersymmetric volume and records the
normalization mechanism that must be preserved in future Seiberg-Witten
expansions.
