# 2026-06-06 Issue #597 Finite Determinant Scheme Transport

## Scope

- Local chapter: Volume II, Chapter 20D, `Instantons as Physical Amplitudes`.
- Local companion: `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- Issue lane: #597, instantons as physical amplitudes with carefully
  regularized measure and fluctuation data.

## Change

- Added `ca:instanton-finite-determinant-scheme-transport` after the
  reference-channel determinant calibration block.
- The new block states that a finite one-loop determinant constant is not a
  standalone physical number.  It is transported only together with:
  coupling/action conversion, the running bosonic zero-mode power,
  orientation measure, source-frame determinant, and physical projection.
- The displayed transport identity is
  `C_S' Gamma_S' lambda_act^{-1} lambda_Omega lambda_src lambda_phys =
  C_S Gamma_S`, with the corresponding finite constant transformation and a
  multiplicative residual bound.

## Physics Rationale

- This targets the harder instanton-amplitude layer: determinant
  normalization in a specified scheme and its relation to source/projection
  data.
- It is not an ADHM/moduli-space expansion.  The point is to keep the
  fluctuation determinant constant tied to the QFT amplitude coordinate where
  it is used.
- It also sharpens the warning that quoting a Pauli--Villars or subtraction
  constant without the source frame and physical projection does not compute a
  physical hard amplitude.

## Companion Evidence

- Added `check_finite_determinant_scheme_transport()`.
- The finite rational model verifies:
  - exact leading-amplitude preservation under full scheme transport;
  - source-frame determinant conversion from two chiral zero-mode blocks;
  - failure of determinant-constant-only transport;
  - failure when the running zero-mode power, source determinant, or physical
    projection conversion is omitted;
  - multiplicative conversion-residual control, with a bridge residual kept
    separate.

## Re-Audit Notes

- No directive, issue-tracker, review, Claude, or monitoring language was
  added to monograph TeX.
- The edit is amplitude-facing: it makes the determinant normalization part of
  a physical source/projection calculation and does not claim to compute the
  continuum determinant constant itself.
