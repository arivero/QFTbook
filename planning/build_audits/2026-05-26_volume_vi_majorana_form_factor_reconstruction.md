# 2026-05-26 Volume VI Majorana Form-Factor Reconstruction Pass

## Scope

This pass deepens Volume VI, Chapter 4 by turning the free-Majorana
energy-density form factor from a sign-convention example into an explicit
correlator reconstruction calculation.

## Manuscript Changes

- Added Proposition `majorana-energy-two-particle-reconstruction`.
- Fixed the normalization data used in the calculation:
  \(\langle\theta'|\theta\rangle=2\pi\delta(\theta'-\theta)\),
  \(p^\mu(\theta)=m(\cosh\theta,\sinh\theta)\), and \(s=-P^2\).
- Derived the Lorentzian Fourier-space two-particle spectral density
  directly from the rapidity delta functions:
  \[
    \widetilde W_\varepsilon(P)
    =
    \theta(P^0)\theta(s-4m^2)
    \frac{|\kappa_\varepsilon|^2}{2m^2}
    \sqrt{1-\frac{4m^2}{s}}.
  \]
- Displayed the two roots in relative rapidity, the Jacobian
  \(\sqrt{s}\,m\sinh(\alpha_s/2)\), and the cancellation between the two
  roots and the identical-particle factor \(1/2\).
- Derived the Euclidean separated-point correlator as a Bessel-kernel
  integral:
  \[
    G_\varepsilon(r)
    =
    \frac{|\kappa_\varepsilon|^2}{2\pi^2}
    \int_0^\infty d\alpha\,
    \sinh^2(\alpha/2)K_0(2mr\cosh(\alpha/2)).
  \]
- Made explicit that contact terms at coincident points are outside the
  separated-point finite-particle spectral calculation.

## Companion Checks

- Extended `calculation-checks/ising_form_factor_checks.py` with finite
  checks for:
  - \(s=4m^2\cosh^2(\alpha/2)\);
  - \(|F_2^\varepsilon|^2=|\kappa_\varepsilon|^2(s-4m^2)/(4m^2)\);
  - the phase-space/Jacobian normalization of the displayed spectral density;
  - the Euclidean \(K_0\)-reduction prefactor.

## Verification

- `python3 calculation-checks/ising_form_factor_checks.py`
  passed with `All Ising form-factor checks passed.`
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1341 pages.
