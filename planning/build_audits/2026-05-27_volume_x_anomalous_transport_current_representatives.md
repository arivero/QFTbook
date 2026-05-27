# 2026-05-27 Volume X Anomalous Transport Current-Representative Pass

## Scope

This pass deepens Volume X, Chapter 9 by making the source protocol and
current-representative layer explicit before using anomalous equilibrium
functionals to define transport.  The target weakness was not the numerical
CME/CVE coefficients, but the logical infrastructure needed to state what
observable those coefficients define.

## Substantive Additions

- Added a hydrostatic anomalous-source datum: stationary background, thermal
  holonomies/chemical potentials, counterterm choice, and declaration of
  which source symmetries are exact versus anomalous.
- Defined consistent variational currents, covariant currents, and
  Bardeen--Zumino shifts in the sign convention used for anomalous source
  variations.
- Clarified the vector-preserving Bardeen convention used in the Dirac
  example: \(A_V\) is an exact background gauge field, while \(\mu_A\) is a
  hydrostatic axial source parameter rather than a conserved-charge chemical
  potential in sectors with nonzero anomaly density.
- Proved the spatial variation formula for the general hydrostatic
  Chern--Simons functional
  \(c_{AA}A\wedge dA+c_{Aa}A\wedge da+c_{aa}a\wedge da\), including the
  source and Kaluza--Klein curls.
- Extended the anomalous-transport calculation checks with exact rational
  bookkeeping for the general Chern--Simons variation coefficients.

## Verification

- `python3 calculation-checks/anomalous_transport_checks.py`: passed.
- `python3 -m py_compile calculation-checks/anomalous_transport_checks.py`:
  passed.
- Primitive-fraction scan on touched files: clean.
- `git diff --check` on touched files: clean.
- `tools/build_monograph.sh`: passed; strict text audit and log scan clean.
- `pdfinfo monograph/tex/main.pdf`: 2223 pages.

## Remaining Work

- The chapter still needs a deeper nonperturbative KMS derivation of
  anomaly-induced transport, a careful treatment of mixed
  gauge-gravitational inflow in hydrostatic variables beyond the displayed
  Dirac CVE coefficients, and QCD-specific applications such as chiral
  magnetic phenomenology with dynamical axial-charge relaxation and
  topological charge fluctuations.
