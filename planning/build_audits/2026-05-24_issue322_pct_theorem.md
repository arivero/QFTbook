# Issue #322 Audit: PCT/CPT Theorem

## Scope

- GitHub issue: `#322`, reporting that the manuscript invoked CPT-type
  symmetries only in passing and lacked a theorem-level PCT/CPT statement.
- Manuscript files:
  - `monograph/tex/volumes/volume_iv/chapter01_wightman_fields_and_reconstruction.tex`
  - `monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`

## Resolution

- Added a dedicated section `The PCT Theorem` to the Wightman reconstruction
  chapter.
- Added Theorem `thm:wightman-pct`, with explicit hypotheses:
  four-dimensional Wightman field presentation, proper orthochronous Poincare
  covariance, cyclic invariant vacuum, spectrum condition, adjoint-domain
  condition, tempered Wightman distributions, graded local commutativity, and
  closure of the field-label family under the PCT test-function operation.
- The theorem states the antiunitary \(\Theta_{\rm PCT}\), vacuum invariance,
  Poincare implementation \((a,\Lambda)\mapsto(-a,\Lambda)\), field covariance
  on smeared distributions, and the corresponding Wightman-function identity.
- The text explicitly records that no mass gap is required for the Wightman
  PCT theorem; mass gaps enter scattering and DHR sector questions separately.
- Added a proof outline using the standard Wightman/Jost mechanism: tube
  analyticity from the spectrum condition, complex Lorentz extension, graded
  locality at Jost points, edge-of-the-wedge continuation, then construction
  of the antiunitary on the reconstruction finite-sequence domain.
- Added Corollary `cor:aqft-pct-from-modular-covariance` to the
  superselection chapter, deriving the AQFT PCT antiunitary in four dimensions
  from wedge modular covariance/Bisognano--Wichmann data:
  \(\Theta_{\rm PCT}=U(R_\perp(\pi))J_{W_R}\).
- Replaced the previous loose phrase "CPT-type symmetries" by an explicit
  reference to the new modular PCT corollary.

## Quality Boundary

- The proof given is a theorem-level derivation outline, not a full
  replacement for the classic Jost proof.  It identifies each load-bearing
  input and explains how the Hilbert-space antiunitary is constructed from the
  distributional PCT identity.
- The statement is restricted to four-dimensional CPT/PCT to avoid silently
  importing dimension-dependent orientation and spin-cover conventions.
