# Pointed Walker-Wang Construction Demotion

Date: 2026-05-31

Issue context:

- Continues #691, the theorem/proposition substance audit.
- Also touches #698 because the Walker-Wang boundary discussion is part of the
  TQFT quoted-theorem proof-debt cluster.

Scope:

- `monograph/tex/volumes/volume_viii/chapter09_boundaries_defects_and_categories.tex`
- `planning/chapter_dossiers/volume_viii/chapter09_boundaries_defects_and_categories.md`
- `planning/build_audits/2026-05-30_pointed_walker_wang_boundary_dequoted.md`
- `tools/audit_theorem_form.py`

Substantive correction:

- The pointed Walker-Wang block was still written as a theorem, although its
  actual content is a finite lattice mechanism plus the transparent-line
  criterion.  The hard continuum/categorical Walker-Wang statement remains a
  theorem-boundary topic elsewhere.
- Demoted the block to a construction and removed the proof environment.
- Made the finite input explicit: edge labels in a finite abelian group,
  vertex fusion by the group law, plaquette-loop recoupling, the monodromy
  phase `M(a,x)=exp(2 pi i b(a,x))`, and the operational deconfinement
  criterion as commutation with every plaquette recoupling away from endpoints.
- Kept the useful result as a finite criterion:
  `a` is deconfined if and only if `M(a,x)=1` for all `x`, equivalently
  `a in Rad(A,b)`.
- Added a theorem-form audit guard so the same title cannot return as a
  theorem/proposition/lemma/corollary wrapper.

Verification plan:

- Run theorem-form, prose, label, dossier, and TeX build audits before pushing.
