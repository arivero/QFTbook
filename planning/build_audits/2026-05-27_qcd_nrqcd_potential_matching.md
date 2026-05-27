# 2026-05-27 QCD NRQCD And Potential Matching

## Scope

- Corrected the large-\(N_c\) half-trace conversion in Volume II, Chapter 19:
  with \(\operatorname{tr}_{\square}(t^at^b)=\delta^{ab}\), the common
  half-trace coupling satisfies \(g_{\rm ht}^2=2g^2\), hence
  \(\lambda_{\rm ht}=2\lambda\).
- Added a nonrelativistic heavy-pair section after the HQET Wilson-line
  section.
- Defined the NRQCD datum with Pauli quark and charge-conjugated antiquark
  fields, the leading Schrödinger action, local gauge-covariant operators, and
  renormalized heavy-pair composites.
- Proved the free NRQCD dispersion, defined gauge-invariant singlet and octet
  quarkonium bilocals using equal-time Wilson transporters, and proved their
  gauge covariance.
- Added the pNRQCD singlet action and derived the tree-level singlet color
  factor \(-C_F\), giving \(V_S^{(0)}(r)=-g^2C_F/(4\pi r)\) in the monograph
  trace convention.
- Added a controlled-approximation statement for the hard/soft/ultrasoft
  hierarchy and for the distinction between weak-coupling and strong-coupling
  pNRQCD matching.

## Checks

- `python3 calculation-checks/large_n_topology_checks.py`
- `python3 calculation-checks/qcd_nrqcd_checks.py`
- `python3 -m py_compile calculation-checks/qcd_nrqcd_checks.py`
- `git diff --check -- ...` on the changed manuscript, calculation-check,
  README, dossier, and audit files.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 2163 pages, 8765358 bytes, PDF 1.5.

## Status

This pass gives the operator and matching-coordinate foundation for later
quarkonium development.  It does not yet develop the full perturbative
potential through loops, renormalon-subtracted mass schemes, spin-dependent
potentials, inclusive quarkonium decay factorization, or lattice/static-energy
matching.
