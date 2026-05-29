# Volume XII, Chapter 4 Dossier: The Unruh Effect and Wedge Modular Theory

## Logical Role

- Role in the monograph: connect curved/background QFT to wedge-local modular
  theory and thermal behavior of restricted vacuum states.
- Immediate predecessor: trace anomalies and background variations.
- Immediate successor: Hawking effect and horizon states.

## Definitions And Results

- Right Rindler wedge and boost flow.
- KMS statement for the vacuum restricted to a wedge algebra.
- Complex boost geometry: imaginary boost time sends right-wedge points into
  future/past tubes and imaginary angle \(\pi\) maps \(W_R\) to \(W_L\).
- Bisognano--Wichmann theorem, marked as a `quotedtheorem` with hypotheses.
- Self-contained free massive scalar wedge-KMS derivation for the polynomial
  wedge algebra, using tube analyticity and spacelike locality at imaginary
  boost angle \(\pi\).
- Accelerated-worldline specialization.
- Detector detailed-balance relation derived from the KMS boundary condition.

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

1. The wedge-restricted vacuum is KMS for boosts under the quoted
   Bisognano--Wichmann hypotheses.
2. The proper-time Unruh temperature is \(a/(2\pi)\).
3. For the free massive scalar, the wedge two-point KMS relation is proved
   from the past-tube analyticity of \(\Delta_+^{(m)}\), complex boost
   geometry, and vanishing of the free commutator at spacelike separation.
4. Wick's theorem extends the two-point result to the free polynomial wedge
   algebra.
5. The free scalar two-point function along an accelerated trajectory has the
   required imaginary-time periodicity.
6. Detector thermality requires weak coupling, stationary long-time limit, and
   controlled switching.

## Calculation Checks

- `calculation-checks/unruh_boost_geometry_checks.py`: verifies the complex
  boost imaginary-part formula, the \(i\pi\) right-to-left wedge map,
  right-left spacelike separation, and the detector detailed-balance exponent
  sign.

## Figures

- Rindler wedge diagram may be added later.

## Audit Notes

- 2026-05-29 anti-wrapper pass: demoted the polynomial wedge-algebra KMS
  corollary to prose.  The analytic theorem is the two-point strip/KMS result;
  the polynomial extension is the Wick expansion and termwise boundary-value
  calculation.
