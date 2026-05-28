# 2026-05-28 Issue #634: Muon g-2 Hybrid Pass

## Scope

Fourth focused development pass on GitHub issue #634 for
`monograph/tex/volumes/volume_ii/chapter19c_standard_model_hybrid_definition.tex`.

This pass adds muon \(g-2\) as the canonical Standard Model hybrid
observable: a single Pauli-form-factor coordinate whose computation uses
perturbative QED, electroweak matching, and nonperturbative QCD current
correlators.

## Manuscript Changes

- Added Section `Muon \(g-2\) as a Hybrid Prediction`.
- Defined \(a_\mu=(g_\mu-2)/2\) as the real Pauli-coordinate in the
  low-energy muon effective Hamiltonian, with the weak-decay width separated
  into absorptive operators rather than treating the muon as an exact stable
  Wigner particle of the full Standard Model.
- Derived the Schwinger coefficient
  \(a_\mu^{\rm QED,1}=\alpha/(2\pi)\) from the Volume I form-factor chapter.
- Defined the hybrid decomposition into QED, electroweak, HVP, HLbL, and
  declared-remainder source coordinates.
- Recorded the leading one-loop electroweak Pauli coefficient in the
  \(Q=T^3+Y\) convention.
- Defined HVP through the gauge-invariant hadronic electromagnetic
  current-current correlator and derived the dispersive formula with the
  Feynman-parameter kernel.
- Defined the Euclidean lattice HVP time-momentum coordinate and the HLbL
  four-current coordinate as nonperturbative QCD current-correlator
  functionals.
- Added a certification proposition listing the data required before a number
  assigned to \(a_\mu^{\rm SM}\) is a certified hybrid prediction.

## Calculation Check

- Extended `calculation-checks/standard_model_anomaly_checks.py`.
- New checks cover the Schwinger \(a_\mu\) coefficient, the leading
  electroweak coefficient normalization, and the HVP Feynman-parameter kernel
  identity.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/standard_model_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/standard_model_anomaly_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full manuscript build completed with a clean log scan and produced
`monograph/tex/main.pdf` with 2345 pages.

## Remaining Issue #634 Work

This pass does not close #634.  Remaining large items include a more explicit
dimension-six operator-basis ledger, the chiral-lattice construction
connection, and a careful Higgs vacuum-stability RG/source-chart treatment.
