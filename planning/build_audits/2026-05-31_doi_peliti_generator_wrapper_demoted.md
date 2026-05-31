# Doi-Peliti Generator Wrapper Demotion

Date: 2026-05-31

Scope:

- `monograph/tex/volumes/volume_x/chapter10_nonequilibrium_steady_states_open_systems.tex`
- `tools/audit_theorem_form.py`
- `planning/chapter_dossiers/volume_x/chapter10_nonequilibrium_steady_states_open_systems.md`

Audit finding:

- The finite Doi-Peliti generator identity was a coefficient check dressed as
  a proposition.  The calculation is useful because it fixes the dictionary
  between the reaction-network master equation and the normally ordered
  occupation-space operator, but it is not a theorem-family result.

Change:

- Demoted the proposition/proof pair to local construction prose with numbered
  equations for the falling-factorial action, the single-reaction term, and
  the projection-state probability-conservation identity.
- Added explicit language separating the algebraic finite-regulator dictionary
  from the real analytic questions: closed Markov generator domains, weighted
  sequence-space control, spatial continuum scaling, and coherent-state
  time-slicing convergence.
- Added the former proposition title to the theorem-form audit guard so the
  same wrapper does not return as a theorem-family environment.

Verification:

- Run the theorem-form and monograph text audits before commit.
