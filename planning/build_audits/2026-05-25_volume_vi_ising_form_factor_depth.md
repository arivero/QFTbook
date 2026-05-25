# Volume VI Ising Form-Factor Depth Pass

## Trigger

- `claude_review.md` flagged that Volume VI introduced the form-factor
  bootstrap without displaying explicit form factors.
- The neighboring sine-Gordon pass strengthened the scattering data; this pass
  adds an operator-level exact example.

## Manuscript Edits

- Expanded
  `monograph/tex/volumes/volume_vi/chapter04_form_factor_bootstrap_local_operators.tex`
  with free-Majorana examples.
- Added the energy-density two-particle form factor as a finite local scalar
  datum checking Watson exchange and \(2\pi i\) cyclicity.
- Added the odd Ising order/twist form-factor family
  \(F_{2k+1}=v i^k\prod_{i<j}\tanh((\theta_i-\theta_j)/2)\).
- Proved Watson exchange, odd-particle cyclicity, and the kinematic
  annihilation-pole recursion, including the residue computation fixing the
  \(i^k\) phase.
- Updated the Volume VI Chapter 4 dossier.

## Calculation Check

- Added `calculation-checks/ising_form_factor_checks.py`.
- `python3 calculation-checks/ising_form_factor_checks.py` passed.

## Build Verification

- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed in
  `monograph/tex`.
- `main.pdf` now builds to 1195 pages, with no undefined references in
  `main.log`.
