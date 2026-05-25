# Issue #467 Audit: Center Symmetry and Polyakov Loop

## Scope

- GitHub issue: #467, "[Vol IV] Center symmetry / Polyakov loop /
  deconfinement order parameter absent."
- Manuscript locus:
  - `monograph/tex/volumes/volume_ii/chapter17b_lattice_yang_mills_nonperturbative_definition.tex`
- Calculation-check locus:
  - `calculation-checks/center_polyakov_checks.py`
- Dossier locus:
  - `planning/chapter_dossiers/volume_ii/chapter18a_lattice_yang_mills_nonperturbative_definition.md`

## Content Added

- Added a finite-temperature lattice section after reflection positivity and
  before the Wilson-loop strong-coupling area-law section.
- Defined the thermal lattice
  \(\Lambda_{a,N_s,N_t}\), inverse temperature
  \(\beta_{\mathrm T}=aN_t\), and separated it from the Wilson coupling
  \(\beta_{\rm lat}=N/g_0^2\).
- Defined the pure \(SU(N)\) thermal center transformation by multiplying all
  temporal links crossing one time slice by \(z_m\in Z_N\).
- Proved at finite cutoff that the Wilson action and Haar measure are
  invariant: temporal plaquettes receive \(z_m\) and \(z_m^{-1}\) on opposite
  temporal links, and spatial plaquettes are unchanged.
- Defined the Polyakov holonomy and normalized Polyakov loop
  \(P_R(\mathbf x)=d_R^{-1}\chi_R(\mathcal P(\mathbf x))\).
- Derived its center transformation
  \(P_R\mapsto \exp(2\pi i m k_R/N)P_R\), with \(k_R\) the \(N\)-ality.
- Added the finite-volume vanishing argument for a charged Polyakov-loop
  expectation and the correct infinite-volume/small-source order parameter.
- Added the static-source free-energy interpretation, including line
  self-energy renormalization, and the Polyakov-loop pair free-energy
  relation.
- Defined deconfinement in the center-symmetry sense and separated it from the
  zero-temperature Wilson-loop area law.
- Recorded that dynamical matter of nonzero \(N\)-ality explicitly breaks the
  corresponding center subgroup, so the fundamental Polyakov loop is not an
  exact QCD order parameter with fundamental quarks.
- Added a TikZ figure for the center slice, Polyakov loop, plaquette
  invariance, and center phase.

## Verification

- Passed: `python3 calculation-checks/center_polyakov_checks.py`.
- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
- Passed: `pdfinfo monograph/tex/main.pdf` reports 862 pages.
- Rendered and inspected physical pages 607--609 at 144 dpi.  The thermal
  center/Polyakov-loop figure and the principal order-parameter and
  static-source formulas are legible and non-overlapping after a figure
  spacing correction.
