# Issue #287 Mixed-Symmetry Unitarity Bounds Pass

## Scope

- Addressed GitHub issue #287:
  `[Vol V Ch 7] Higher-spin / mixed-symmetry unitarity bounds absent`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`.

## Mathematical Content Added

- Introduced two-row traceless tensor primaries
  \(\mathcal H_{a,b}\), \(a\ge b\ge1\).
- Stated the tensor Casimir formula
  \(C_\lambda=\sum_i\lambda_i(\lambda_i+D-2i)\) in the normalization
  \(C_1=D-1\).
- Displayed the stable-range decomposition of
  \(\mathcal H_1\otimes\mathcal H_{a,b}\) into add-one-box and
  remove-one-box channels:
  \(\mathcal H_{a+1,b}\),
  \(\mathcal H_{a,b+1}\),
  \(\mathcal H_{a,b,1}\),
  \(\mathcal H_{a-1,b}\), and
  \(\mathcal H_{a,b-1}\), with absent-channel caveats.
- Computed the level-one positivity inequalities channel by channel.
- Proved the first-level two-row bounds:
  \(\Delta\ge a+D-2\) for \(a>b\), and
  \(\Delta\ge a+D-3\) for \(a=b\).
- Identified the corresponding projected-divergence null equations at
  saturation.

## Verification Targets

- The new mixed-symmetry section derives its bounds from the displayed
  Gram-matrix/Casimir formula and the stated vector-tensor decomposition.
- Low-dimensional Hodge-duality caveats are stated before using the
  stable-range Young-diagram decomposition.
- The chapter dossier was updated to record the new claim and its audit
  obligation.
