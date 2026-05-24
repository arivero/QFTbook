# Issue #291 TTT Osborn--Petkou Structure Count Pass

## Scope

- Addressed GitHub issue #291:
  `[Vol V Ch 8] TTT structure count '3 in D >= 4' asserted without justification`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`.

## Content Added

- Identified the displayed parity-even \(TTT\) tensor basis as the
  Osborn--Petkou separated-point position-space basis.
- Added an explicit source footnote to Osborn and Petkou,
  `Implications of Conformal Invariance in Field Theories for General
  Dimensions`, Ann. Phys. 231 (1994), arXiv:hep-th/9307010.
- Made the counting argument visible:
  conformal covariance, tracelessness, and permutation symmetry reduce the
  ansatz to five coefficients; conservation imposes two independent equations;
  the remaining \(D\ge4\) structures are parametrized by \(a,b,c\).
- Added the collinear-frame independence check using the transverse
  \(O(D-1)\)-invariant coefficients \(r,s,u\).
- Added the \(D=3\) degeneration:
  the transverse space is two-dimensional, the collinear tensor depends only
  on \(r-4u\) and \(s+2u\), and
  \(\mathcal I^{(1)}-\mathcal I^{(2)}+2\mathcal I^{(3)}=0\).
- Displayed an explicit two-structure parity-even \(D=3\) basis and noted
  that a separate parity-odd \(D=3\) structure is outside this parity-even
  basis.

## Verification Targets

- The manuscript must not merely assert the number three for \(D\ge4\).
- The \(D=3\) reduction to two parity-even structures must be explicit.
- The discussion must remain separated-point and must not conflate the
  stress-tensor Ward-normalized contact-term problem with the separated
  tensor-structure count.
