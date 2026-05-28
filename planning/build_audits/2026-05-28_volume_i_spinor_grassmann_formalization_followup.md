# Volume I Chapter 16 Spinor-Grassmann Formalization Follow-Up

Date: 2026-05-28.

Files:

- Chapter 16 TeX source.
- Chapter 16 dossier.

Scope:

- Promoted the Dirac/Weyl/Majorana representation block to a definition and a
  proof of Lorentz-covariant chiral and Majorana reductions.
- Formalized finite odd first-order mechanics, the second-class constraint
  matrix, the odd Dirac bracket, and the two-state quantization check.
- Added a finite Grassmann algebra/Berezin derivative definition and
  formalized Berezin pushforward functoriality.
- Formalized the supersymmetric quantum-mechanics datum, the harmonic
  oscillator Witten index, and the periodic-fermion worldline index-density
  calculation.
- Formalized the free Dirac functional integral, the Dirac propagator inverse,
  the isolated spinor pole datum, locality of the conjugate pole residue,
  spinorial mass-shell residues, spinorial LSZ pole assignments, and the first
  four-fermion direct-minus-exchange vertex.

Verification:

- `python3 calculation-checks/spinor_grassmann_checks.py`
- `python3 -m py_compile calculation-checks/spinor_grassmann_checks.py`
- targeted ASCII scan on the edited chapter/dossier/audit
- targeted weak-language scan on the edited chapter/dossier/audit
- targeted long-line scan on the edited chapter/dossier/audit
- `git diff --check` on edited files
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`
