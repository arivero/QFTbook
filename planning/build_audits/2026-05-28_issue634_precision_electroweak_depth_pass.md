# 2026-05-28 Issue #634: Precision Electroweak Depth Pass

## Scope

Third focused development pass on GitHub issue #634 for
`monograph/tex/volumes/volume_ii/chapter19c_standard_model_hybrid_definition.tex`.

This pass adds the precision electroweak two-point source-chart coordinates
usually denoted \(S,T,U\), with the input scheme and analyticity hypotheses
made explicit.

## Manuscript Changes

- Added Section `Precision Electroweak Self-Energy Coordinates`.
- Defined the transverse self-energy difference
  \(\Delta\Pi_{VV'}(q^2)\) for \(V,V'\in\{W,Z,\gamma\}\) relative to a
  reference electroweak source chart with the same input values of
  \(\alpha_{\rm em}\), \(G_F\), and \(m_Z\).
- Stated the electromagnetic on-shell conditions
  \(\Delta\Pi_{\gamma\gamma}(0)=\Delta\Pi_{Z\gamma}(0)=0\).
- Defined the finite \(S,T,U\) coordinates from the zero-momentum Taylor data
  of the renormalized two-point functions.
- Proved that, for pure mass-coordinate shifts, \(\alpha_{\rm em}T\) is the
  first-order shift of the \(\rho=m_W^2/(m_Z^2c_W^2)\) coordinate.
- Stated the domain of the \(S,T,U\) projection: analytic transverse
  two-point corrections through first derivative order, after fixing the
  input coordinates.  Vertex, box, four-fermion, threshold, and detector data
  remain separate coordinates of a hybrid prediction.

## Calculation Check

- Extended `calculation-checks/standard_model_anomaly_checks.py`.
- New checks verify the tree electroweak mass identity, the \(T\)-as-\(\rho\)
  fractional-shift algebra, and vanishing of \(S,U\) for universal or
  custodially aligned derivative corrections in the declared coordinate chart.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/standard_model_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/standard_model_anomaly_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh` (`main.pdf`, 2340 pages)

## Remaining Issue #634 Work

This pass does not close #634.  Remaining large items include the full muon
\(g-2\) hybrid calculation, a more explicit dimension-six operator-basis
ledger, the chiral-lattice construction connection, and a careful treatment of
Higgs vacuum-stability flow as a scheme-dependent RG/source-chart statement.
