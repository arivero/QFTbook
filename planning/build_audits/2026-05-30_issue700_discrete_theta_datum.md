# Issue #700: Discrete Theta Defining Datum

## Target

Volume IX, Chapter 5 was flagged in issue #700 because it discussed finite
topological phases, Pontryagin-square counterterms, global forms, and line
lattices without first aggregating the central "discrete theta" object into a
definition.

## Edit

- Added `def:discrete-theta-datum` at the chapter opening.
- The definition separates:
  - finite-cochain discrete theta data
    `(C_D,A,q,[omega],omega_loc)`;
  - global-form Yang-Mills data
    `(g,G,B_G(M),w_2^Gamma,theta,tau_disc,L_line)`.
- For `SU(N)/Z_k`, the definition names the line lattice
  `L_{N,k,p}=<(k,0),(p,N/k)>` and records `p in Z_k` as part of the global
  definition of the theory.
- Rewrote the finite-topological-action paragraph and the continuum
  gauge-theory status section to refer back to the named datum.
- Updated the Chapter 5 dossier.

## Scope

This pass addresses the definition-locality failure.  It does not prove a
nonperturbative continuum construction of all four-dimensional global forms
and discrete theta terms; that remains
`op:discrete-theta-continuum-qft`.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh` (clean; `main.pdf` has 2675 pages)
