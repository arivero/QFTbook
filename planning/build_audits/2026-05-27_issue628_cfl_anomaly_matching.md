# Issue #628 CFL Anomaly Matching Pass

Date: 2026-05-27

## Scope

This pass extends the dense-QCD/CFL development in
`monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
by adding the background-field anomaly-matching layer for the exact connected
continuous symmetry
\[
  SU(3)_L\times SU(3)_R\times U(1)_B .
\]

## Content Added

- Defined the chiral flavor and baryon background fields \(A_L,A_R,B\) and
  fixed the half-trace flavor convention used for anomaly coefficients.
- Computed the local UV six-form anomaly polynomial of massless
  \(N_f=N_c=3\) QCD in these backgrounds:
  \[
    I_6^{\rm UV}
    =
    \frac{N_c}{6(2\pi)^3}
    [\operatorname{tr}F_L^3-\operatorname{tr}F_R^3]
    +
    \frac{N_cq_B}{2(2\pi)^3}
    F_B[\operatorname{tr}F_L^2-\operatorname{tr}F_R^2].
  \]
- Derived the mixed coefficient \(N_cq_B/2=1/2\) for quark baryon charge
  \(q_B=1/3\).
- Stated the CFL matching of the pure nonabelian chiral anomaly by the
  level-\(N_c\) gauged Wess--Zumino--Witten functional of \(\Sigma\), using
  the monograph's existing WZW level theorem.
- Added the baryon-Goldstone mixed-anomaly representative
  \[
    -\frac{D_B\phi_B}{2\pi}
    \wedge
    \frac{\operatorname{tr}F_L^2-\operatorname{tr}F_R^2}{2(2\pi)^2},
    \qquad
    D_B\phi_B=d\phi_B-B,
  \]
  and proved that its exterior derivative reproduces the UV mixed anomaly.
- Added a normalization remark separating the background-normalized
  baryon Goldstone coordinate from the charge of a chosen local CFL order
  operator.
- Added exact calculation checks for the pure anomaly coefficient, WZW level,
  mixed baryon-flavor coefficient, vector-subgroup cancellation, and the sign
  in \(d(D_B\phi_B)=-F_B\).

## Verification

Recorded before commit:

- `python3 calculation-checks/qcd_phase_checks.py`: passed with
  `All QCD phase-structure checks passed.`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- calculation-checks/README.md
  calculation-checks/qcd_phase_checks.py
  monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex
  planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md
  planning/build_audits/2026-05-27_issue628_cfl_anomaly_matching.md`: passed.
- Targeted primitive-fraction scan on the touched TeX, check, dossier, and
  audit files: no matches.
- `tools/build_monograph.sh`: passed; monograph build and log scan clean.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2216`.

## Remaining Work

The dense-QCD chapter still needs the microscopic weak-coupling computation
of CFL low-energy constants, neutrality beyond ideal CFL with quark masses
and beta equilibrium, crystalline phases, and non-Fermi-liquid corrections.
