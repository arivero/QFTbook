# QCD String Excited-Spectrum Pass

## Trigger

Issue #492 remains open after the Luscher-term pass because the QCD-string
discussion still needs the flux-tube excitation spectrum.  This pass develops
the first spectral layer: the oscillator Hilbert space of transverse
worldsheet fields and the Nambu--Goto reference spectrum, with the scope of
the claim kept separate from a derivation of the QCD string itself.

## Manuscript Edits

- Expanded
  `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
  with a new excited-flux-tube-level subsection.
- Defined open-string oscillator occupation numbers and level
  \(N=\sum_{i,n}nN_{n,i}\), with Gaussian large-\(L\) energies.
- Added the open oscillator generating function
  \(\prod_{n\ge1}(1-q^n)^{-c_\perp}\) and the first \(D=4\) coefficients.
- Defined closed-string left/right levels, quantized longitudinal momentum,
  and level matching \(N_L-N_R=q\).
- Added the Nambu--Goto reference spectra for open and closed flux tubes and
  their \(1/L^3\) expansions, explicitly framed as reference effective-string
  coordinates rather than definitions of the QCD string.
- Updated the QCD chapter dossier and calculation-check README.

## Calculation Check

- Extended `calculation-checks/qcd_string_luscher_checks.py` to verify the
  \(D=4\) open oscillator degeneracies, the excited open and closed
  large-\(L\) expansion coefficients, and the closed-string level-matching
  example, while retaining the Luscher-term checks.

## Verification

- `python3 calculation-checks/qcd_string_luscher_checks.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed
  from `monograph/tex`.
- `pdfinfo monograph/tex/main.pdf` reports 1203 pages.
- `rg -n "LaTeX Warning: (Reference|There were undefined|Label\\(s\\) may have changed)|undefined references|multiply defined" monograph/tex/main.log`
  returned no matches.
- `rg -n -F "Foreign command \\over" monograph/tex/main.log` returned no
  matches.
