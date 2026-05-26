# 2026-05-26 Ising Spin Form Factor And TFFSA Pass

## Source Material Checked Locally

- Downloaded to ignored `references/` directory:
  - `references/fonseca_zamolodchikov_ising_magnetic_free_energy_0112167.pdf`
  - `references/fonseca_zamolodchikov_ward_identities_ising_0309228.pdf`
- Extracted local text to `/tmp/fz0112167.txt` and `/tmp/fz0309228.txt`.
- Checked the convention-sensitive points used in the manuscript:
  - In the convention of the Ward-identity paper, \(m>0\) is the ordered
    phase and \(\langle\sigma\rangle=\bar\sigma\ne0\).
  - The spin-field two-particle form factor is
    \(i\bar\sigma\tanh((\beta_1-\beta_2)/2)\).
  - Crossing one particle gives the connected one-to-one matrix element
    \(i\bar\sigma\coth((\beta_1-\beta_2)/2)\).
  - The finite-volume/TFFSA use of spin matrix elements requires sector,
    density-of-states, disconnected-contraction, and finite-size-correction
    choices.

## Manuscript Changes

- Volume VI, Chapter 4:
  - Added the even semi-local Ising spin-field product family
    \(F_{2k}^{\sigma_+}=\bar\sigma i^kP_{2k}\).
  - Derived Watson exchange, semi-local cyclicity with phase \(-1\), and the
    semi-local annihilation-pole equation from the product formula.
  - Derived the mixed bra/ket connected matrix element by crossing, producing
    \(\tanh\)-factors within each side and \(\coth\)-factors between crossed
    and uncrossed rapidities.
  - Identified the Fonseca-Zamolodchikov one-to-one spin matrix element as a
    crossed boundary value in the chapter's conventions.
- Volume XI, Chapter 10:
  - Added the two-coupling Ising TCSA datum
    \(H_{\rm CFT}+\tau\int\varepsilon+h\int\sigma\).
  - Added the TFFSA reorganization based on exact massive-Majorana finite
    volume states and spin-field form factors.
  - Defined the connected TFFSA spin matrix element with momentum
    conservation, free density of states, disconnected-contraction caveat, and
    finite-size-correction status.
  - Proved the Feshbach-Schur complement identity behind truncation
    counterterms and high-energy-tail corrections.

## Companion Checks

- Extended `calculation-checks/ising_form_factor_checks.py` to verify:
  - even spin-field Watson exchange;
  - semi-local cyclicity phase \(-1\);
  - crossing to the \(\coth\) one-to-one matrix element;
  - the general mixed bra/ket product;
  - the semi-local kinematic-pole residue.

## Verification

- `python3 calculation-checks/ising_form_factor_checks.py`
  passed with `All Ising form-factor checks passed.`
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1345 pages.
- `rg -n "Overfull|Undefined|Warning: Reference" monograph/tex/main.log`
  returned no matches after the final build.
