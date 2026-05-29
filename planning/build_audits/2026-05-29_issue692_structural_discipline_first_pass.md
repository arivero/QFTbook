# Issue #692 structural discipline first pass

This audit records the first concrete cleanup pass for GitHub issue #692.
The issue was not treated as a substitute for the deeper open backlog; it was
used to remove specific local failures in first-use discipline, proposition
form, and forward-reference hygiene.

## Manuscript changes

- `monograph/tex/volumes/volume_i/chapter01_what_is_qft.tex`: the first
  appearance of the Feynman two-point distribution now states the mostly-plus
  Lorentzian convention, the Fourier phase, the sign of the prefactor, the
  `i\epsilon` prescription, and the scalar time-ordering rule at separated
  times.  The equal-time extension is described as the distributional
  extension fixed by the same prescription, rather than being left implicit.

- `monograph/tex/volumes/volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex`:
  Proposition `prop:joint-translation-spectrum` is now a proposition rather
  than a proof-fragment embedded in theorem form.  The derivation has been
  moved to the proof, and the text identifies the Lie-algebra commutator as
  the differential shadow of the joint spectral calculus.

- `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`:
  the Lehmann-ellipse parameter
  `\zeta(z)=z+\sqrt{z^2-1}` now carries its branch cut and normalization
  `\zeta(z)\sim 2z` at first use.  Later references point back to that
  definition instead of promising a definition later.

- `monograph/tex/volumes/volume_i/chapter16a_spinor_conventions.tex`: the
  first mention of the Lorentz action now points directly to the defining
  spin-representation definition.

- `monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`:
  the Coleman--Norton positivity condition now points to the actual displayed
  realization equation instead of using a forward-reference phrase.

## Checks

- `rg -n "specified below|defined below|as defined later|will be defined below" monograph/tex/volumes`
  returns no hits.
- `python3 tools/audit_theorem_form.py` passes.
- `python3 tools/audit_negative_scope_prose.py` passes.
- `git diff --check` passes.
- `tools/build_monograph.sh` passes, producing
  `monograph/tex/main.pdf` with 2539 pages.

## Remaining scope

Issue #692 explicitly framed further passes as separate work.  The immediate
findings in that issue are addressed here; the global proof-depth, figure,
physics-normalization, and later-volume expansion issues remain tracked by
their own open GitHub issues and by `claude_review.md`.
