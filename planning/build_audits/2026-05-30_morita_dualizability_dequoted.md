# Morita Two-Dualizability Pass

Date: 2026-05-30

Issue context:

- Advances #698, the TQFT and higher-categorical quoted-theorem proof-debt
  cluster.

Scope:

- `monograph/tex/volumes/volume_viii/chapter02_bordism_functoriality_extended_tqft.tex`
- `planning/chapter_dossiers/volume_viii/chapter02_bordism_functoriality_extended_tqft.md`
- `calculation-checks/tqft_frobenius_gluing_checks.py`
- `calculation-checks/README.md`

Substantive changes:

- Removed the cobordism-hypothesis `quotedtheorem` wrapper and kept the full
  framed classification theorem as an external higher-categorical boundary.
- Added a local definition of the finite-dimensional Morita `2`-category used
  in the chapter.
- Proved that a finite-dimensional separable algebra is fully `2`-dualizable
  in that Morita target by constructing the dual object, evaluation and
  coevaluation bimodules, and the separability-idempotent splitting
  `A^e -> A` that supplies finite projectivity and hence adjoints.
- Worked out the semisimple algebra `A = k^r` as the extended refinement of
  the ordinary Frobenius-algebra TQFT.
- Extended the paired calculation check to verify the semisimple separability
  idempotent, the splitting of `A^e -> A`, and `HH_0(k^r)=k^r`.

Verification plan:

- Run the edited `tqft_frobenius_gluing_checks.py`.
- Run the standard theorem/prose/display-label/dossier audits and rebuild the
  monograph.
