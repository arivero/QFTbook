# Issue #643: Baryon Spectroscopy Catalog and HQET Spin Average

GitHub issue: #643.

Edited:

- `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
- `calculation-checks/qcd_spectroscopy_regge_checks.py`
- `calculation-checks/README.md`

Content added:

- Added light-baryon spectroscopy charts for the flavor octet and decuplet,
  with \(I\), hypercharge, and \(J^P\) stated as QCD spectral labels.
- Added a concrete excited-light-baryon channel chart for
  \(\Delta(1232)\), \(N(1440)\)-type, \(N(1535)\)-type,
  \(\Sigma(1385)\), \(\Lambda(1405)\)-type, and \(\Lambda(1520)\)
  channels, phrased as sheet-labeled pole problems rather than model names.
- Added one-heavy-quark baryon HQET charts for
  \(\Lambda_Q,\Xi_Q,\Sigma_Q,\Xi'_Q,\Omega_Q\), and a near-threshold
  heavy-sector chart including \(\Xi_{cc},\Omega_{cc}\), bottom baryons,
  \(P_c\)-type hidden-charm baryon poles, \(T_{cc}\)-type poles, and
  \(X(6900)\)-type heavy-quarkonium poles.
- Proved the heavy-baryon spin-average formula:
  the degeneracy-weighted average over \(J=j_\ell\pm \frac12\) cancels the
  chromomagnetic \(1/m_Q\) coordinate at the stated order.
- Added exact rational calculation checks for the spin-average cancellation,
  including the \(\Sigma_Q,\Sigma_Q^\ast\) case.

Verification:

- `python3 calculation-checks/qcd_spectroscopy_regge_checks.py`
- `python3 -m py_compile calculation-checks/qcd_spectroscopy_regge_checks.py tools/audit_style_density.py`
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_spectroscopy_regge_checks.py monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex planning/12_strict_writing_harness.md tools/audit_style_density.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_theorem_form.py`
- `tools/build_monograph.sh`

The full monograph build and log scan completed cleanly; the rebuilt PDF is
`monograph/tex/main.pdf` at 2475 pages.
