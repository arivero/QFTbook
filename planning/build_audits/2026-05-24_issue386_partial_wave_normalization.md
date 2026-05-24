# Issue #386 Partial-Wave Normalization Audit

GitHub issue #386 flagged an internal inconsistency in Volume II, Chapter 4:
the chapter announced an ordered \(16\pi\) partial-wave expansion but later used
the identical-boson relation
\[
  \mathcal M_s=-16\pi i\,\rho_1^{-1}(S_0-1).
\]

## Correction

The external stable channel in the resonance discussion is the symmetric
\(\phi_1\phi_1\) channel.  The chapter now uses the same convention as the
partial-wave chapter:
\[
  \mathcal M(s,z)
  =
  32\pi
  \sum_{\ell\ {\rm even}}(2\ell+1)a_\ell(s)P_\ell(z),
  \qquad
  S_\ell=1+2i\rho_1a_\ell .
\]
For the angle-independent resonant \(s\)-channel exchange,
\[
  a_0^{(s)}(s)=\frac{\mathcal M_s(s)}{32\pi},
  \qquad
  S_0(s)-1=\frac{i\rho_1(s)}{16\pi}\mathcal M_s(s),
\]
which gives
\[
  \mathcal M_s(s)
  =
  -16\pi i\,\rho_1(s)^{-1}(S_0(s)-1).
\]

## Files Changed

- `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`
- `planning/chapter_dossiers/volume_ii/chapter04_resonances_dressed_propagators.md`

The ordered \(16\pi\) convention remains mentioned only as a labelled-leg
bookkeeping convention before Bose symmetrization, not as the convention used
for the elastic resonance partial wave.
