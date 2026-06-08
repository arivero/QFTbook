# Volume XII, Chapter 4 Dossier: The Unruh Effect and Wedge Modular Theory
Source-File: monograph/tex/volumes/volume_xii/chapter04_unruh_effect_modular_theory.tex

## Logical Role

- Role in the monograph: connect curved/background QFT to wedge-local modular
  theory and thermal behavior of restricted vacuum states.
- Immediate predecessor: trace anomalies and background variations.
- Immediate successor: Hawking effect and horizon states.

## Definitions And Results

- Right Rindler wedge and boost flow.
- KMS statement for the vacuum restricted to a wedge algebra, with the
  distributional free-field core separated from the bounded Weyl/von Neumann
  algebra theorem.
- Complex boost geometry: imaginary boost time sends right-wedge points into
  future/past tubes and imaginary angle \(\pi\) maps \(W_R\) to \(W_L\).
- Bisognano--Wichmann theorem recorded as an external AQFT theorem boundary,
  with the local proof obligation discharged in the free massive scalar model.
- Self-contained free massive scalar two-point wedge-KMS derivation as a
  distributional boundary-value theorem, using tube analyticity and spacelike
  locality at imaginary boost angle \(\pi\).
- Wick-polynomial distributional core, stated as an unbounded analytic core
  rather than a completed \(C^\ast\)-algebra KMS theorem.
- Bounded Weyl/von Neumann algebra KMS theorem boundary, tied to
  Bisognano--Wichmann and the free quasifree Weyl construction.
- Accelerated-worldline specialization.
- Detector response split into finite switched probability, stationary
  spectral detailed balance, controlled long-time switching limit with
  explicit local density/global tail hypotheses, measure-limit alternatives
  for atoms and thresholds, and a normalized four-dimensional massless Planck
  rate.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(W_R\) | right Rindler wedge |
| \(K\) | Lorentz boost generator |
| \(\eta\) | boost time |
| \(\tau\) | accelerated observer proper time |
| \(a\) | proper acceleration |
| \(T_{\rm Unruh}\) | Unruh temperature |
| \(\Delta_+^{(m)}\) | massive free scalar positive-frequency two-point distribution |
| \(\alpha_\eta\) | boost automorphism of wedge-local fields |

## Claim Ledger

1. The general Bisognano--Wichmann theorem is identified as an external
   structural theorem boundary; the chapter proves the wedge-restricted
   two-point distributional KMS statement directly for the free massive scalar
   and records the bounded Weyl/von Neumann algebra KMS theorem as a separate
   bounded-observable assertion.
2. The proper-time Unruh temperature is \(a/(2\pi)\).
3. For the free massive scalar, the wedge two-point KMS relation is proved
   from the past-tube analyticity of \(\Delta_+^{(m)}\), complex boost
   geometry, and vanishing of the free commutator at spacelike separation.
4. Wick's theorem extends the two-point result to a free polynomial
   distributional core; the completed \(C^\ast\)-algebra theorem is carried by
   bounded Weyl observables or by a separately specified unbounded analytic
   domain.
5. The free scalar two-point function along an accelerated trajectory has the
   required imaginary-time periodicity.
6. Detector thermality requires weak coupling, stationary spectral KMS, a
   controlled long-time switching family, and separation of finite probability
   from stationary transition rate.  The pointwise \(O(T^{-1})\) switching
   estimate is conditional on an absolutely continuous Lipschitz density near
   the detector gap, absence of an atom there, polynomial spectral-measure
   growth, and enough Fourier decay/moments of the switch.  General spectral
   measures are treated by weak measure convergence of the switched
   convolution, not by assigning a pointwise rate.
7. For a four-dimensional massless scalar, the stationary excitation rate is
   \(E/(2\pi)(e^{2\pi E/a}-1)^{-1}\), with de-excitation fixed by spectral
   detailed balance.

## Calculation Checks

- `calculation-checks/unruh_boost_geometry_checks.py`: verifies the complex
  boost imaginary-part formula, the \(i\pi\) right-to-left wedge map,
  right-left spacelike separation, the detector detailed-balance exponent
  sign, the four-dimensional massless Planck detector rate, finite-switching
  spectral smearing as a non-exact detailed-balance control, the actual
  scaled Fourier switching kernel
  \(\widehat\chi_T(\nu)=T\widehat\chi(T\nu)\), the normalized
  approximate-identity mass and \(O(T^{-1})\) Lipschitz convolution error,
  atom-at-gap growth, insufficient-tail and wrong-normalization negative
  controls, and compact smooth switching as a nonanalytic contour-regulator
  control.

## Figures

- Rindler wedge diagram may be added later.

## Audit Notes

- 2026-05-29 anti-wrapper pass: demoted the polynomial wedge-algebra KMS
  corollary to prose.  The analytic theorem is the two-point strip/KMS result;
  the polynomial extension is the Wick expansion and termwise boundary-value
  calculation.
- 2026-05-30 Bisognano--Wichmann dequote pass: removed the remaining general
  `quotedtheorem` wrapper from the chapter.  The general AQFT result is now an
  explicit theorem-boundary remark, and the chapter's proved content is the
  free scalar wedge-KMS theorem with its tube-analyticity and locality
  argument.
- 2026-06-08 issue #729 printed-order pass: added an opening dependency
  boundary distinguishing the fixed-background wedge-local AQFT theorem from
  pAQFT interacting curved-spacetime constructions.  This keeps Unruh
  thermality from being used as an unstated interacting horizon theorem.
- 2026-06-08 issue #906 KMS/detector pass: separated the proved
  distributional two-point KMS core from the bounded Weyl/von Neumann algebra
  KMS theorem, replaced switched-contour detailed-balance prose with the
  stationary spectral KMS theorem plus a controlled \(\chi_T\) long-time
  limit, added the normalized four-dimensional massless detector rate, and
  recorded finite-switching and compact-smooth-switch negative controls.
- 2026-06-08 issue #934 switching-rate hypotheses pass: replaced the
  measure-as-density shortcut by a positive tempered spectral measure
  \(d\mu_G\), made pointwise rates conditional on local absolute continuity,
  Lipschitz density, no atom at the detector gap, polynomial spectral growth,
  and switch Fourier tail bounds, split the proof into near/far regions, and
  added measure-limit text for atoms, thresholds, and singular spectra.
