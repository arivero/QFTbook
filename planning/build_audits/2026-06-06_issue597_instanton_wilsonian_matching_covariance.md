# Issue #597 instanton Wilsonian matching covariance pass

Date: 2026-06-06.

Scope:
- Vol II Ch20D, `Instantons as Physical Amplitudes`.
- Added `ca:instanton-wilsonian-matching-covariance` inside
  `sec:instanton-hard-wilsonian-ope-datum`.
- Extended `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  with a finite two-operator matching-covariance test.

Physics-depth audit:
- This pass targets the use of an instanton hard source kernel as QFT data,
  not the geometry of the instanton moduli space.
- The new block separates the short instanton coefficient from the
  renormalized operator matrix element, the anomalous-dimension transport,
  the moving Wilsonian boundary flux, the long-size shell, and the physical
  residuals.
- This directly addresses the amplitude-side subtlety: the instanton
  "vertex" is a scheme-dependent coordinate until it is paired with the
  operator matrix element and the long-distance remainder.

Negative controls added:
- Finite operator-basis mixing cannot be handled by transforming only the
  coefficient.
- A moving size boundary leaves a nonzero flow if the long-size shell is
  omitted.
- A residual budget that drops the long-shell term underbudgets the completed
  matching flow.

Scope guard:
- No directive, review, monitoring, or issue-tracker language was inserted
  into TeX.
- The change is an architecture bridge for physical amplitudes, not an ADHM or
  moduli-space expansion.
