# Issue #389 Bose-Symmetric Bubble-Chain Audit

GitHub issue #389 flagged that the \(D=2\) \(\phi^4\) bubble-chain example in
Volume II, Chapter 5 displayed only the \(s\)-channel chain while the external
particles of a real scalar theory are identical bosons.

## Correction

The manuscript now labels the displayed resummation as
\[
  \mathcal M_{\mathrm{chain}}^{(s)}(s),
\]
the \((12)\)-channel bubble chain.  It then records the Bose-symmetric
truncation
\[
  \mathcal M_{\mathrm{Bose}}(s,z)
  =
  \mathcal M_{\mathrm{chain}}^{(s)}(s)
  +
  \mathcal M_{\mathrm{chain}}^{(t)}(t(s,z))
  +
  \mathcal M_{\mathrm{chain}}^{(u)}(u(s,z))
  +
  \mathcal M_{\mathrm{rest}}(s,z).
\]
In the identical-boson \(32\pi\) convention,
\[
  a_0^{\mathrm{Bose}}(s)
  =
  \frac{1}{64\pi}\int_{-1}^{1}dz\,
  \mathcal M_{\mathrm{Bose}}(s,z)
  =
  \frac{\mathcal M_{\mathrm{chain}}^{(s)}(s)}{32\pi}
  +
  a_{0,\mathrm{cross}}(s).
\]
Near the \(s\)-channel threshold, \(t(s,z)\) and \(u(s,z)\) remain near zero,
whereas the \((12)\)-channel invariant approaches \(4m^2\).  Under the local
no-crossed-threshold hypothesis, the crossed chains and omitted regular kernels
therefore contribute analytic background terms, while the \(s\)-channel chain
contains
\[
  f(s)\sim \frac{\pi}{m\sqrt{4m^2-s}}.
\]

## Files Changed

- `monograph/tex/volumes/volume_ii/chapter05_composite_bound_states_and_bethe_salpeter_amplitudes.tex`
- `planning/chapter_dossiers/volume_ii/chapter05_composite_bound_states_bethe_salpeter.md`
