# Issue #608 Quartic Tail And Uniform-Integrability Pass

Date: 2026-05-26.

Scope: Volume XI, Chapter 9, stochastic quantization and constructive scalar
models.

## Mathematical Additions

- Added a theorem-level criterion converting exponential moment bounds for a
  finite list of cylinder coordinates into uniform integrability of every
  polynomial OS cylinder observable built from those coordinates.  The proof
  displays the polynomial-by-exponential domination and the tail estimate
  needed in the truncation step of OS reflection positivity.
- Added a finite-lattice quartic-tail proposition: a scalar finite cutoff
  with nonnegative kinetic energy and quartic coercive local potential has
  finite exponential quartic moments at that cutoff.  The proof completes the
  quartic square with an explicit Young inequality.
- Updated the \(\Phi^4_2\) assembly theorem so finite-cutoff lattice
  integrability, continuum uniform integrability, and regulator comparison
  are kept logically separate.

## Verification

- Updated `calculation-checks/constructive_scalar_spde_checks.py` with checks
  for the one-site quartic moment scaling, the coercivity Young inequality,
  and the exponential-tail domination used in the uniform-integrability proof.
- Ran `python3 calculation-checks/constructive_scalar_spde_checks.py`; it
  passed.
- Ran `tools/audit_monograph_text.sh`; it passed.
- Ran `tools/audit_chapter_dossiers.sh`; it passed.
- Ran `tools/build_monograph.sh`; it passed and produced
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf` reports 1524 pages.
- The final `monograph/tex/main.log` contains no LaTeX warnings, undefined
  control sequences, fatal errors, overfull boxes, or underfull boxes.

## Remaining Boundary

This pass does not prove continuum tightness or cutoff-uniform exponential
moment bounds.  It isolates the exact estimate needed for polynomial
Schwinger functions and OS quadratic forms once a constructive cutoff family
is placed in a common topology.
