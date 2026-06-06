# Build Audit: Issue #597 Observable-Handoff Ledger

Date: 2026-06-06

Scope:
- Continued `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added an observable-handoff section distinguishing hard source coefficients,
  dilute theta curvature, \(U(1)_A\)-odd zero-mode-zone susceptibility kernels,
  and real-time axial relaxation rates.
- Updated the focused companion check, calculation-check inventory, and Chapter
  20D dossier.

Physics-depth rationale:
- The pass turns the instanton amplitude architecture toward physical QCD
  observables instead of adding more moduli-space or local-cell data.
- It cross-links to the existing Ch20 theta/dilute-gas, \(U(1)_A\), and
  real-time axial-rate machinery while making the handoff discipline explicit
  in the dedicated instanton-amplitude chapter.
- The main distinction is physical: a source coefficient, a vacuum curvature,
  a Euclidean susceptibility kernel, and a retarded diffusion/relaxation rate
  have different final maps and cannot be substituted for one another.

Companion evidence:
- `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  now verifies finite examples rejecting hard-source-as-theta-curvature,
  theta-curvature-as-real-time-rate, \(U(1)_A\)-kernel-as-theta-curvature, and
  dilute-instanton curvature substituted for Witten--Veneziano input without a
  same-scheme comparison budget.

Scope guard:
- No directives, issue-tracker text, or monitoring instructions were inserted
  into monograph TeX.
- This pass advances the physical-observable side of issue #597 and is also
  relevant to the QCD-rigor lane in issue #630.
