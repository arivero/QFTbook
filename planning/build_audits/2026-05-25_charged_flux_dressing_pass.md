# Charged Flux Dressing Pass

## Trigger

Open issues #527 and #528 identify a foundational gap: ordinary
Haag--Ruelle scattering uses local or almost-local creators, whereas charged
particles in gauge theories require noncompact gauge-invariant dressings.
Earlier passes added the Gauss-law obstruction and finite-regulator dressed
LSZ theorem.  This pass deepens the missing bridge between Wilson-line
dressings, asymptotic flux, and the eikonal data used in dressed-state
perturbation theory.

## Manuscript Edits

- Expanded `volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
  with an asymptotic Wilson-line/worldline-current derivation.
- Added the regulated half-line current
  \[
    J^\mu_{q,u,\epsilon}(y;x)
    =
    q\int_0^\infty d\tau\,e^{-\epsilon\tau}
    u^\mu\delta^{(4)}(y-x-u\tau).
  \]
- Proved that its Fourier transform gives the soft eikonal denominator
  \(p\cdot k\), with the endpoint prescription separated from the homogeneous
  soft kernel.
- Added the boosted Coulomb angular flux density
  \[
    \mathcal E_{q,\mathbf v}(\mathbf n)
    =
    \frac{q}{4\pi}
    \frac{1-|\mathbf v|^2}{(1-\mathbf v\cdot\mathbf n)^2},
  \]
  proved that it integrates to \(q\), and proved that for \(q\ne0\) it
  determines the charged velocity.
- Created a chapter dossier for the theorem-level Haag--Ruelle/mathematical
  scattering chapter, including its charged-sector open problems.

## Calculation Check

- Added `calculation-checks/charged_flux_dressing_checks.py`, verifying the
  boosted Coulomb flux integral, the velocity/extrema relation, the regulated
  half-line Fourier transform, and equality of worldline-current and
  momentum-space eikonal denominators.

## Verification

- `python3 calculation-checks/charged_flux_dressing_checks.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed
  from `monograph/tex`.
- `pdfinfo monograph/tex/main.pdf` reports 1200 pages.
- `rg -n "undefined|multiply defined|LaTeX Warning: Reference"
  monograph/tex/main.log` returned no matches.
- `rg -n -F "Foreign command \\over" monograph/tex/main.log` returned no
  matches.
