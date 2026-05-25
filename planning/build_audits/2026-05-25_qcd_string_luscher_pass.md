# QCD String Luscher-Term Pass

## Trigger

Open issue #492 records the need for an extensive QCD-string treatment.  The
existing manuscript had a flux-tube section but moved too quickly from the
static-gauge effective action to the universal \(1/L\) correction.  This pass
turns that step into an explicit determinant derivation and adds a finite
calculation check for the displayed coefficients.

## Manuscript Edits

- Expanded
  `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
  in the QCD-string section.
- Added Proposition `prop:qcd-string-luscher-term`, deriving the open and
  closed Luscher terms from the free transverse worldsheet determinant after
  local counterterm subtraction.
- Added the Nambu--Goto open and closed ground-state square-root expansions
  as reference effective-string coordinates, not as definitions of the QCD
  string.
- Added controlled approximation `ca:qcd-effective-string-expansion`, stating
  the data needed for an effective-string prediction and separating universal
  terms from lattice-matched coefficients.
- Updated the QCD chapter dossier and calculation-check README.

## Calculation Check

- Added `calculation-checks/qcd_string_luscher_checks.py`, verifying the
  rational coefficients behind the open and closed Casimir terms and the
  displayed Nambu--Goto \(1/L\) and \(1/L^3\) expansions.

## Verification

- `python3 calculation-checks/qcd_string_luscher_checks.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed
  from `monograph/tex`.
- `pdfinfo monograph/tex/main.pdf` reports 1202 pages.
- `rg -n "LaTeX Warning: (Reference|There were undefined|Label\\(s\\) may have changed)|undefined references|multiply defined" monograph/tex/main.log`
  returned no matches.
- `rg -n -F "Foreign command \\over" monograph/tex/main.log` returned no
  matches.
