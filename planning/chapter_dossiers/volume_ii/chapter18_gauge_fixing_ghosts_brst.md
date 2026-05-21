# Volume II, Gauge Fixing, Ghosts, and BRST Cohomology Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Follows the construction of classical Yang--Mills theory and matter
  representations.
- Precedes QCD renormalization, chiral anomalies, global anomalies, and
  infrared gauge-theory structure.
- Role in the monograph: formulate gauge fixing as a local coordinate choice on
  gauge orbits, introduce the Faddeev--Popov determinant and ghosts, define the
  BRST differential, and identify the cohomological objects that control
  physical states, local operators, counterterms, and anomalies.

## Source And Reference Controls

- `SRC-QFT-PDF`: second-sequence handwritten material after the classical
  Yang--Mills construction; used for the local order of gauge fixing, ghost
  fields, and BRST.
- `SRC-EXTERNAL`:
  `references/sound_references/barnich_brandt_henneaux_local_brst_cohomology_hep-th_0002245.pdf`
  and text sidecar, especially Sections 2.3, 2.6, and 2.7.
- The external source is used for the distinction between \(H(s)\) and
  \(H(s\mid d)\), for the contractible-pair/nonminimal-sector statement, and for
  the roles of ghost-number-zero and ghost-number-one local cohomology.
- The chapter does not reproduce the full antifield/BV computation of local
  BRST cohomology.

## Framework

- Perturbative Yang--Mills theory on a fixed spacetime \(M\), in a local
  trivialization of the gauge bundle.
- Compact gauge group \(G\) with structure constants fixed by the preceding
  Yang--Mills chapter.
- Local gauge fixing around a field-space region where the Faddeev--Popov
  operator is transverse after separating residual zero modes.
- Off-shell nilpotent BRST differential using the Nakanishi--Lautrup field.
- Local cohomology is formulated in the algebra of finite jets of fields and
  ghosts.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\mathcal A\) | affine space of local gauge potentials |
| \(\mathcal G\) | local gauge group |
| \(F(A)\) | gauge-condition map |
| \(\mathcal M_F(A)\) | Faddeev--Popov operator |
| \(\Delta_F(A)\) | Faddeev--Popov determinant |
| \(c,\bar c\) | ghost and antighost fields |
| \(B\) | Nakanishi--Lautrup auxiliary field |
| \(s\) | BRST differential |
| \(\Psi\) | gauge-fixing fermion |
| \(\mathcal F_{\mathrm{loc}}\) | algebra of local functions in finite jets |
| \(\Omega^p_{\mathrm{loc}}\) | local \(p\)-forms |
| \(d\) | spacetime exterior derivative |
| \(H^g(s)\) | local BRST cohomology at ghost number \(g\) |
| \(H^{g,D}(s\mid d)\) | BRST cohomology of local \(D\)-forms modulo \(d\) |
| \(Q\) | canonical BRST charge |
| \(\mathcal K\) | gauge-fixed indefinite state space |
| \(\mathcal H_{\mathrm{phys}}\) | ghost-number-zero BRST cohomology of states |

## Claims Established

- Gauge fixing is a local coordinate construction on gauge orbits, encoded
  perturbatively by the Faddeev--Popov determinant.
- Ghosts represent the Faddeev--Popov determinant and carry fermionic statistics
  although they are Lorentz scalars.
- The BRST differential is an odd ghost-number-one derivation with \(s^2=0\).
- The gauge-fixing and ghost action is \(s\)-exact after introducing the
  Nakanishi--Lautrup field.
- \(H^0(s;\mathcal F_{\mathrm{loc}})\) describes local gauge-invariant
  composite operators modulo BRST-exact representatives.
- \(H^{0,D}(s\mid d)\) controls local counterterm densities and
  \(H^{1,D}(s\mid d)\) controls candidate local anomalies.
- The nonminimal pair \((\bar c,B)\) is contractible and can be removed from
  cohomology under the standard perturbative regularity assumptions.
- Physical states are represented by ghost-number-zero cohomology of the
  canonical BRST charge when positivity of the quotient is established.

## Figure Requirements

- The present chapter currently uses equations rather than figures.
- If a figure is added, it should show the relation between gauge orbit, local
  slice, Faddeev--Popov determinant, and BRST complex; it must not portray gauge
  redundancy as a physical symmetry acting on distinct states.

## Open Boundaries

- Full BV/antifield formalism is not developed here.
- Global Gribov-copy issues are acknowledged as beyond the perturbative local
  slice.
- Positivity of the BRST quotient is stated as a required condition rather than
  proved in full generality.
