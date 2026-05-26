# 2026-05-26 Issue #598: Sine-Gordon / Massive Thirring Bosonization

## Scope

Issue #598 flagged that the Volume VI sine-Gordon chapter stated the
Coleman relation and Mandelstam operator without deriving the vertex-OPE
normalization, current-sector Gaussian, operator dictionary, or RG matching.

## Manuscript Changes

- Expanded `volume_vi/chapter08_sine_gordon_massive_thirring_affine_toda.tex`
  into a multi-subsection treatment of the massive Thirring equivalence.
- Added the canonical free-boson vertex OPE and derived
  \(\Delta_\alpha=\alpha^2/(4\pi)\), distinguishing it from the
  \(V_\alpha V_{-\alpha}\) singular exponent \(\alpha^2/(2\pi)\).
- Derived \(4\pi/\beta^2=1+g_T/\pi\) from the Euclidean current-sector
  Gaussian and the rescaling of the free-Dirac mass operator.
- Derived the current dictionary, the fermion-number/topological-charge
  equality, and the Mandelstam exchange phase from equal-time commutators.
- Added an operator dictionary, the free-fermion two-point check, the
  marginal endpoint \(g_T=-\pi/2\), chiral and nonabelian extensions, and the
  precise scope of compact-radius defect formulations.

## Calculation Check

Added `calculation-checks/sg_thirring_bosonization_checks.py`, which verifies:

- vertex-OPE exponent and scaling dimension;
- Coleman's coupling map at the free point and marginal endpoint;
- current-dictionary coefficient after the canonical rescaling;
- Mandelstam exchange exponent and free-fermion dimension;
- the relevance threshold for the sine-Gordon cosine.
