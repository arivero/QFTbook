# 2026-05-27 Issue #630 Theta And Witten--Veneziano Pass

## Scope

- Reviewed `claude_review.md` and the live #630 QCD rigor backlog.
- Added a finite-regulator topological susceptibility datum to Volume II,
  Chapter 20, immediately after the theta-sector decomposition.
- Proved the finite-volume cumulant identity
  \(E_{\Lambda,V_4}''(0)=V_4^{-1}
  (\langle Q^2\rangle-\langle Q\rangle^2)\), with the CP-invariant
  specialization \(\langle Q\rangle=0\).
- Added a theta-branch datum, thermodynamic unique-branch selection
  proposition, and cluster-decomposition test for convex mixtures of theta
  branches.
- Added a large-\(N_c\) singlet theta datum to Volume II, Chapter 21,
  separating pure-Yang--Mills susceptibility from full massless-QCD
  susceptibility.
- Derived the chiral-limit Witten--Veneziano coefficient
  \(m_{\eta_0}^2=2N_f\chi_{\rm YM}/f_\pi^2\) from the local
  \(U(N_f)\) singlet effective field and the pure-Yang--Mills theta branch.
- Added an exact calculation check for the cumulant identity, CP-symmetric
  first moment, theta branch relabeling, branch-mixture cluster covariance,
  thermodynamic branch suppression, massless-quark theta screening, and
  Witten--Veneziano mass coefficient.

## Checks

- `python3 calculation-checks/qcd_theta_witten_veneziano_checks.py` passed.
- `python3 -m py_compile calculation-checks/qcd_theta_witten_veneziano_checks.py` passed.
- `git diff --check -- monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex calculation-checks/qcd_theta_witten_veneziano_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_ii/chapter20_chiral_axial_anomalies.md planning/chapter_dossiers/volume_ii/chapter21_global_anomalies_ssb_pions.md planning/build_audits/2026-05-27_issue630_theta_witten_veneziano.md` passed.
- After the theta-branch and cluster-decomposition extension, `tools/build_monograph.sh`
  passed with strict text audit and final log scan clean.
- `pdfinfo monograph/tex/main.pdf` reports 2182 pages.

## Status

This addresses the theta/topological-susceptibility and Witten--Veneziano
subcluster of #630 at the current Volume II level.  It does not assert a
nonperturbative construction of continuum pure Yang--Mills, nor a proof of the
large-\(N_c\) matching hypothesis from first principles.
