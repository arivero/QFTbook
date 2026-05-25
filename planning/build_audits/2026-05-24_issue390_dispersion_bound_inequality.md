# Issue #390 Dispersion-Bound Inequality Audit

GitHub issue #390 flagged that the forward absorptive estimate in Volume II,
Chapter 7 used a long aligned chain whose later equality signs could be read as
equating \(\operatorname{Im}\mathcal M(s,0)\) with the elastic-channel
\(L^2\) expression.  The elastic expression is correct, but it is a lower bound
on the total absorptive part unless the scattering is purely elastic.

## Correction

The manuscript now separates the two statements:
\[
  \operatorname{Im}\mathcal M(s,0)
  =
  \sqrt{s(s-4m^2)}\,\sigma_{\rm tot}(s)
  \ge
  \sqrt{s(s-4m^2)}\,\sigma_{\rm el}(s),
\]
and
\[
  \sqrt{s(s-4m^2)}\,\sigma_{\rm el}(s)
  =
  \frac{1}{32\pi\sqrt{s(s-4m^2)}}
  \int_{-(s-4m^2)}^0 dt\,|\mathcal M(s,t)|^2 .
\]
It then states the combined lower bound explicitly.

## Files Changed

- `monograph/tex/volumes/volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex`
- `planning/chapter_dossiers/volume_ii/chapter07_partial_waves_dispersion_froissart.md`
