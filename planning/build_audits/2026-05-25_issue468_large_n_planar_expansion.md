# Issue #468 Audit: 't Hooft Large-\(N_c\) Planar Expansion

## Scope

GitHub issue #468 reported that the QCD chapter mentioned large-\(N\) only as
a coupling rescaling and lacked the systematic 't Hooft topological expansion:
double-line notation, planar limit, genus expansion, and explicit nonplanar
\(1/N^2\) suppression.

## Manuscript Changes

- Added `The 't Hooft Large-\(N_c\) Expansion` to
  `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`,
  placed between Wilson-loop/static-potential material and the QCD-string
  section.
- Fixed the convention at the start of the section:
  \(\operatorname{tr}_{\square}(t^at^b)=\delta^{ab}\),
  \(C_A=2N_c\), \(T_F=1\), and
  \(\lambda=g^2N_c\), with comparison to the common half-trace
  \(\lambda_{\rm ht}=2\lambda\).
- Derived the \(SU(N_c)\) double-line completeness relation in the displayed
  trace convention and explained the status of the traceless subtraction.
- Derived the ribbon-graph power
  \(N_c^{V-E+F}=N_c^{2-2h-b}\) from propagator, vertex, and face factors.
- Added an explicit theta-graph computation comparing a planar routing
  \((V,E,F)=(2,3,3)\) to a one-handle routing \((V,E,F)=(2,3,1)\), giving
  \(N_c^{-2}\) nonplanar suppression at fixed \(\lambda\).
- Added single-trace factorization, fixed-\(N_f\) versus Veneziano
  quark-boundary scaling, and the leading scaling of meson, glueball, baryon,
  and vacuum amplitudes with explicit caveats about required spectral
  hypotheses.
- Added a double-line topology figure with the adjoint color-flow propagator,
  planar theta graph, and one-handle theta graph.

## Calculation Checks

- Added `calculation-checks/large_n_topology_checks.py`.
- The script verifies:
  - an explicit Hermitian traceless \(SU(N)\) basis with
    \(\operatorname{tr}(t^at^b)=\delta^{ab}\);
  - the completeness relation
    \(\sum_a(t^a)^i{}_j(t^a)^k{}_\ell
    =\delta^i{}_\ell\delta^k{}_j
    -N^{-1}\delta^i{}_j\delta^k{}_\ell\) for \(2\le N\le6\);
  - the \(N_c^{-2}\) planar-to-one-handle theta-graph suppression;
  - normalized single-trace scaling and fixed-\(N_f\) versus Veneziano
    boundary counting.

## Verification Plan

- Run the new calculation check directly.
- Run `git diff --check`.
- Run the monograph text and dossier audits.
- Build the monograph and inspect the rendered page containing the new
  double-line figure.

## Verification Results

- `python3 calculation-checks/large_n_topology_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` completed with clean log scan.
- `pdfinfo monograph/tex/main.pdf` reports 865 pages.
- Rendered the physical PDF page containing figure 47.6 with `pdftoppm` and
  inspected `/tmp/qft_issue468_large_n-672.png`; the double-line labels,
  planar theta graph, one-handle theta graph, and caption are visible and not
  overlapping.
