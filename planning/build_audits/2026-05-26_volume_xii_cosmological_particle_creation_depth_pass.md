# Volume XII Chapter 8 Cosmological Particle-Creation Depth Pass

Date: 2026-05-26.

## Scope

- Rewrote the cosmological-spacetimes chapter from a short topic list into a
  derivation-centered account of particle creation as a relation between
  complex structures on the real symplectic solution space.
- Derived the spatially flat Robertson--Walker scalar mode equation in
  conformal time, including the explicit effective frequency
  \(k^2+a^2(m^2+\xi R)-p\mathcal H'-p^2\mathcal H^2\).
- Proved the massless conformal-coupling cancellation in arbitrary spacetime
  dimension.
- Defined compatible complex structures, one-particle Hilbert spaces, and
  the Fock representation attached to a positive-frequency choice.
- Added the diagonal Shale--Stinespring criterion to distinguish finite
  particle density from unitary equivalence of Fock representations.
- Proved Bogoliubov normalization and the out-particle number formula from
  the Wronskian and annihilator transformation.
- Added the instantaneous frequency-jump example as a normalization check,
  with the corresponding particle number formula.
- Derived the Riccati equation for the adiabatic frequency and recorded the
  second-order adiabatic frequency.
- Proved positivity of switched detector response from positive type of the
  Wightman two-point function.
- Derived the de Sitter \(\nu\)-parameter and the normalized Bunch--Davies
  Hankel mode with its past positive-frequency asymptotic and Wronskian
  normalization.
- Clarified the backreaction boundary: particle production is a diagnostic
  extracted from a selected state, not a closed semiclassical Einstein
  equation.

## Calculation Checks

- Added `calculation-checks/cosmological_particle_creation_checks.py`.
- The script checks the conformal-coupling cancellation, de Sitter
  \(\nu\)-parameter arithmetic, the sudden-quench Bogoliubov normalization,
  a power-law adiabatic Riccati identity, and finite positive-type detector
  Gram forms.
- Updated `calculation-checks/README.md` and the chapter dossier to include
  the new check.

## Verification

- `python3 calculation-checks/cosmological_particle_creation_checks.py`
- `python3 -m py_compile calculation-checks/cosmological_particle_creation_checks.py`
- `python3 calculation-checks/point_splitting_stress_checks.py`
- `python3 calculation-checks/hawking_bogoliubov_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The first xelatex pass had the expected undefined-reference warnings from the
new labels; latexmk reran xelatex and the final build/log scan was clean.

The clean build produced `monograph/tex/main.pdf` with 1836 pages, creation
time Tue May 26 21:00:46 2026 EDT, and file size 7,311,391 bytes.

## Residual Work

- Add a smooth exactly solvable scale-factor example, rather than only the
  sudden-jump normalization model.
- Develop interacting cosmological QFT and semiclassical backreaction beyond
  the free-field and fixed-background diagnostics.
