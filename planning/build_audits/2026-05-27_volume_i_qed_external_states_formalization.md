# Volume I Chapter 19 Formalization Pass

Date: 2026-05-27.

Files:

- `monograph/tex/volumes/volume_i/chapter19_quantum_electrodynamics_and_external_states.tex`
- `calculation-checks/qed_external_state_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_i/chapter19_quantum_electrodynamics_external_states.md`

Scope:

- Promoted the QED representative datum, Abelian Dirac coupling covariance,
  local charge neutrality, Wilson-line dressed charged insertions, gauge-fixed
  source functional, representative Feynman rules, LSZ external factors, tree
  Compton hard kernel, tree Compton Ward identity, cross-section functional,
  and infrared boundary of charged scattering into labeled theorem-style
  environments with proofs.
- Kept the conceptual status of charged spinor external factors explicit:
  literal LSZ pole residues require an infrared-regulated sector with an
  isolated charged one-particle shell; in massless QED the same rows are hard
  kernel data requiring inclusive or dressed infrared completion.
- Added `qed_external_state_checks.py` for finite convention checks of local
  charge phases, Abelian Wilson-line endpoint phases, Abelian
  Faddeev--Popov field independence, tree Compton Ward-cancellation signs, and
  fixed-incoming-label cross-section counting.

Verification:

- `python3 calculation-checks/qed_external_state_checks.py`
- `python3 -m py_compile calculation-checks/qed_external_state_checks.py`
- targeted long-line scan on edited files
- targeted weak-language scan on edited files
- `git diff --check` on edited files
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`
