# Master Convention Dictionary

This file records the global convention defaults for the monograph and the
allowed chapter-local deviations. It is an index, not a substitute for the
definitions in the manuscript. When a chapter uses a convention that is not one
of the global defaults below, the chapter top must say so through
`\ChapterConventions{...}{...}{...}{...}{...}` and this file must be updated.

## Global Defaults

The default Lorentzian metric is mostly plus:
`\eta_{\mu\nu}=\operatorname{diag}(-,+,\ldots,+)`.

The default Euclidean metric is positive: `\delta_{\mu\nu}`.

The default value of Planck's constant is `\hbar=1`, unless a formula displays
`\hbar` explicitly.

The default vacuum symbol is `\vac=\Omega` when a Hilbert-space vacuum vector is
present.

The default spacetime-translation convention is
`U(a)=\exp(\ii a^\mu P_\mu)` in Lorentzian Hilbert-space settings. Time
evolution is written as `\exp(-\ii Ht)` when a Hamiltonian time parameter is
singled out.

Represented internal or spacetime symmetry transformations use
`\exp(\ii\epsilon^A\widehat Q_A)` unless the chapter explicitly displays a
different sign convention.

Gauge-theory trace and coupling conventions are fixed where gauge theory is
introduced: Yang--Mills actions are written with the coupling in the form
`(4g^2)^{-1}\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})`, with the trace
normalization stated at the point of use. Anomaly formulae must refer back to
that trace normalization rather than silently switching to a different
generator convention.

Spinor and gamma-matrix conventions are primarily defined in
`monograph/tex/volumes/volume_i/chapter16a_spinor_conventions.tex`. The
monograph uses the mostly-plus Lorentzian convention and avoids mostly-minus
formulae except when explicitly comparing conventions.

## Chapter Header Implementation

The preamble defines the five-slot convention header
`\ChapterConventions{arena}{metric}{hbar}{vacuum}{signs}`. Standard wrappers
are:

`ConventionsLorentzian`: Lorentzian QFT with mostly-plus metric.

`ConventionsEuclidean`: Euclidean metric, no Hilbert-space vacuum unless
reconstructed or stated.

`ConventionsMixed`: Lorentzian and Euclidean structures both appear, with
domains stated locally.

`ConventionsRealTime`: real-time quantum-mechanical or Schwinger-Keldysh
settings, with metric only when a field-theory example is present.

`ConventionsEuclideanCFT`: Euclidean CFT, radial quantization invoked where
stated, positive Euclidean metric.

`ConventionsMixedCFT`: Lorentzian local-operator data and Euclidean radial or
conformal geometry both appear.

Every actual chapter file currently has a chapter-top convention header. The
only `chapter*.tex` file without one is
`volume_i/chapter16a_spinor_conventions.tex`, which is a section-level spinor
convention appendix input into another chapter rather than a standalone
`\chapter` file.

## Chapter-Deviation Registry

`volume_viii/chapter04_chern_simons_theory.tex` uses a custom
`\ChapterConventions` declaration. The classical Chern--Simons action is
metric-independent, so the metric slot says that no metric is part of the
classical action. Hilbert-space language appears only after a Hamiltonian
splitting or boundary state space is chosen.

Any future deviation must be added here at the same time as the manuscript
change. A deviation is not merely a stylistic preference: it must state which
formulae would be misread if the global default were silently applied.

## Maintenance Rule

When introducing a new symbol convention that affects signs, factors of `\ii`,
trace normalization, metric signature, charge normalization, or Hermitian
adjoints, do three things in the same commit:

1. State the convention in the chapter-top header or in the first local
   definition where it is used.
2. Link back to the primary definition home if the convention already has one.
3. Update this dictionary if the convention is global or is a chapter-local
   deviation from a global default.
