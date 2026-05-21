# Analyticity and Landau First-Sheet Pass

Date: 2026-05-22

Scope:
- Tightened the fixed-\(t\) first-sheet discussion: stated the kinematic conventions, physical \(t\)-interval, right-hand and crossed-channel cuts, physical upper-edge boundary value, and the role of bound-state poles.
- Clarified the structural assumptions behind real analyticity and crossing: mass gap, Poincare invariance, locality, unitarity, stable LSZ external states, and the separate status of polynomial boundedness.
- Expanded the tube-analyticity and edge-of-the-wedge discussion so crossing is stated as a local analytic-continuation statement after external one-particle poles are isolated.
- Reworked the Landau discussion as a necessary stationary-pinch condition, with explicit sheet, orientation, numerator, and positive-parameter qualifications.
- Added details for ordinary two-particle thresholds, pseudo-threshold parameter signs, triangle anomalous thresholds, and the Coleman-Norton spacetime interpretation.
- Rephrased residual negative framing so the chapter states the active structures and assumptions directly.

Verification:
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- Rendered and visually inspected PDF pages 164--174 at 150 dpi, covering the chapter opening, first-sheet/cut-plane figure, crossing figure, pinch figure, Landau-equation page, bubble-threshold figure, triangle/vector-closure figure, and the transition into the following dispersion chapter.

Follow-up:
- A later pass should develop a more systematic nonperturbative account of maximal analyticity domains and state precisely which parts are theorem, hypothesis, or perturbative diagnostic.
