# Volume IX Global Forms And Line Lattices Audit

## Scope

- Deepened `monograph/tex/volumes/volume_ix/chapter01_global_forms_and_higher_form_symmetry.tex`.
- Added exact arithmetic checks in
  `calculation-checks/global_form_line_lattice_checks.py`.
- Updated the calculation-check index and the Volume IX Chapter 1 dossier.

## Mathematical Content Added

- Defined character and cocharacter lattices for compact tori and specialized
  them to the weight, root, coweight, and coroot lattices of \(G_{\rm sc}\).
- Stated the global form \(G=G_{\rm sc}/\Gamma\) as a change of both
  \(X^*(T_G)\) and \(X_*(T_G)\), not merely as a name for the gauge group.
- Proved the Wilson-charge descent criterion through central characters.
- Worked out \(SU(N)/\mathbb Z_k\): Wilson \(N\)-ality must lie in
  \(k\mathbb Z_N\), while finite magnetic cocharacter classes lie in
  \((N/k)\mathbb Z_N\).
- Defined genuine line operators separately from lines requiring attached
  surfaces.
- Defined the finite Dirac pairing on Wilson--'t Hooft charges and proved
  maximal isotropy of
  \(L_{N,k,p}=\langle(k,0),(p,N/k)\rangle\).
- Replaced the previous informal higher-form symmetry discussion by an
  abelian group-like \(p\)-form symmetry definition using topological defects,
  Pontryagin-dual charges, and linking action.
- Distinguished electric one-form symmetry \(Z(G)\) from magnetic one-form
  symmetry \(\pi_1(G)^\vee\).

## Verification

- `python3 calculation-checks/global_form_line_lattice_checks.py`
  passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed and rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf` reports 1349 pages.
