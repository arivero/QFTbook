# Issue #882 Vol X Real-Time Convention Audit

## Scope

- Canonical owner: Volume X Chapter 4 convention ledger.
- Synchronized chapters: Volume X Chapters 1, 2, and 12.
- Physics surface protected: KMS detailed balance, source response for
  \(H-hB\), Kubo spectral slopes, Euclidean-to-retarded reconstruction, and QCD
  transport inverse maps.

## Repairs

- Chapter 1 separates unsigned fermionic Wightman KMS from the signed lesser
  propagator and Euclidean antiperiodicity.
- Chapter 1 corrects the source-response sign:
  \(K^R=i\theta\langle[A,B]\rangle=-G^{R,\mathrm{comm}}\).
- Chapter 2 distinguishes
  \(\widehat\rho=\rho_{\rm comm}/(2\pi)\), uses the retarded
  \(z-\omega\) denominator, and states \(G_E(i\omega_n)=-G^R(i\omega_n)\)
  for nonzero Matsubara frequency in the declared convention.
- Chapter 12 inserts the missing \(d\omega/(2\pi)\) in the positive-frequency
  Euclidean kernel and requires the inverse matrix \(M_{i\alpha}\) and
  stability norm to use the same normalization.

## Regression Checks

- `kms_foundation_checks.py`: one-mode fermion unsigned/signed lesser check,
  Euclidean antiperiodicity, and finite two-level source-impulse response sign.
- `finite_temperature_path_integral_checks.py`: harmonic oscillator
  \(\rho_{\rm comm}\) versus \(\widehat\rho\), Euclidean kernel normalization,
  retarded denominator, and Matsubara sign.
- `qcd_phase_checks.py`: exact rational inverse-map negative control for the
  missing \(1/(2\pi)\) kernel normalization.

## Scope Boundary

This pass is convention infrastructure and argument architecture.  It prevents
later transport and QCD extraction formulae from inheriting wrong signs or
normalizations, but it is not itself a new continuum hydrodynamic theorem or a
deeper microscopic derivation of QCD transport.
