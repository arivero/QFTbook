# Volume I, Chapter 16a Dossier: Spinor and Gamma-Matrix Conventions

## Source Placement

- Included immediately after the spinor-field and Grassmann path-integral
  material, before gauge theory and anomaly calculations use spinor signs.
- Centralizes the mostly-plus Lorentzian gamma convention, Dirac adjoint,
  chirality, two-component index algebra, Majorana conjugation, dimensional
  continuation prescription, and low-dimensional spinor blocks.
- The four-dimensional basis and Wess-Bagger comparison are modeled on the
  source spinor appendix and checked against the repository calculation
  scripts rather than imported as convention lore.

## Framework

- Lorentzian metric in four dimensions:
  \(\eta_{\mu\nu}=\operatorname{diag}(-,+,+,+)\).
- Clifford relation:
  \(\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\mathbf1_S\).
- Dirac adjoint:
  \(\beta=\ii\gamma^0\), \(\bar\psi=\psi^\dagger\beta\).
- Chirality:
  \(\gamma_5=-\ii\gamma^0\gamma^1\gamma^2\gamma^3\) and
  \(\epsilon^{0123}=+1\).
- Epsilon symbols are fixed by
  \(\epsilon^{12}=\epsilon_{12}=1\) and the analogous dotted convention.
- Dimensional continuation with \(\gamma_5\) is recorded only as a
  perturbative trace prescription, not as a non-perturbative definition of a
  fermionic path integral.
- Two-dimensional conventions are split into the Dirac-anomaly basis and the
  chiral-component Majorana basis used in the source free-fermion appendix.
  They are related by an explicit similarity transformation and must not be
  conflated at the level of displayed matrix components.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(S\) | complex four-dimensional Dirac spinor module |
| \(\gamma^\mu\) | mostly-plus Lorentzian Clifford generators |
| \(\beta\) | \(\ii\gamma^0\), defining the Dirac adjoint |
| \(S^{\mu\nu}\) | spinor Lorentz generator \(-\ii[\gamma^\mu,\gamma^\nu]/4\) |
| \(R(\Lambda)\) | spin representation matrix covering \(\Lambda\in SO^+(1,3)\) |
| \(\gamma_5\) | four-dimensional chirality matrix |
| \(P_\pm\) | chiral projectors \((1\pm\gamma_5)/2\) |
| \(\rho^\mu_{+-},\rho^\mu_{-+}\) | chiral off-diagonal gamma blocks |
| \(B\) | anti-linear Majorana-conjugation matrix, \(B=\gamma_2\) |
| \(C\) | transposed-contraction matrix \(B\gamma^0\) |
| \(U_{\rm ch}\) | same-metric Wess-Bagger-to-Weinberg chiral phase matrix |
| \(\ell_\parallel,\ell_\perp\) | physical and continued loop-momentum components |
| \(\Gamma^\mu\) | lower-dimensional Lorentzian or Euclidean gamma matrices |
| \(\widehat\Gamma^\pm\) | light-cone gamma matrices in the free-fermion basis |
| \(U_2\) | basis-change matrix between the \(D=2\) Dirac and chiral-component bases |

## Claims Established

- `def:four-dimensional-mostly-plus-spinor-convention` fixes the metric,
  explicit gamma basis, Dirac adjoint, Dirac density, and Hermitian current
  normalization.
- The basic Clifford/adjoint/current paragraph derives the slash-square,
  beta-pairing, and current-Hermiticity identities from the explicit Clifford
  data.
- `def:spin-representation-and-chirality` fixes
  \(S^{\mu\nu}\), \(R(\Lambda)\), \(\gamma_5\), chiral projectors, and the
  \(\gamma_5\) trace convention.
- The spin covariance and chirality trace paragraph derives the spin-generator
  commutator, Clifford covariance, beta-pairing invariance, chirality
  algebra, and \(4\ii\epsilon^{\mu\nu\rho\sigma}\) trace normalization.
- `def:two-component-block-epsilon-conventions` records the chiral gamma
  blocks, raising/lowering conventions, and complex-conjugation convention.
- The \(\rho_{+-}/\rho_{-+}\) minus sign and the
  \(2\eta_{\mu\nu}\) contraction are retained as an explicit convention check
  in prose rather than theorem form.
- `def:majorana-conjugation-weinberg-basis` fixes the anti-linear Majorana
  real structure.  Its Lorentz covariance and the corrected infinitesimal sign
  \((S^{\mu\nu})^*=-B S^{\mu\nu}B^{-1}\) are recorded as an explicit
  convention calculation in prose rather than theorem-family content.
- The same-metric Wess--Bagger phase translation is retained as an explicit
  basis-change calculation in prose, with the warning that the gamma-matrix
  phase and the two-component epsilon conventions must both be translated.
- `def:dimensional-reduction-chiral-trace-prescription` states the
  four-dimensional \(\gamma_5\) trace prescription used in perturbative
  anomaly calculations.
- `def:three-dimensional-mostly-plus-majorana-convention` and
  `prop:three-dimensional-clifford-symmetric-block-identities` fix the real
  \(D=3\) Majorana convention and prove the symmetric lowered gamma blocks.
- `def:two-dimensional-mostly-plus-spinor-trace-convention` and
  `prop:two-dimensional-chirality-trace` fix the \(D=2\) chirality trace used
  in anomaly calculations.
- `def:two-dimensional-chiral-component-majorana-convention` records the
  two-dimensional chiral-component convention
  \((\widehat\Gamma^+)_{++}=(\widehat\Gamma^-)_{--}=2\ii\), while
  `prop:two-dimensional-chiral-component-dirac-compatibility` proves its
  explicit basis-change relation to the \(D=2\) Dirac-anomaly convention.
- `def:recursive-euclidean-clifford-basis` and
  `prop:euclidean-recursion-preserves-clifford-relations` prove the even
  Euclidean Clifford recursion and chirality-square identity.
- `def:six-eight-dimensional-euclidean-spinor-blocks` records the \(SO(6)\)
  and \(SO(8)\) block conventions needed later for supersymmetry.

## Figure Requirements

- No standalone figures are required for this convention appendix; the chapter
  is controlled by explicit matrices, algebraic identities, and calculation
  checks.

## Calculation Checks

- `calculation-checks/gamma_trace_checks.py` and
  `calculation-checks/gamma_trace_checks.wl` check the pre-existing trace and
  anomaly-normalization identities.
- `calculation-checks/spinor_convention_checks.py` checks the complete finite
  algebra added in the 2026-05-27 formalization pass: Clifford algebra,
  beta-pairing, spin-generator commutators, \(\gamma_5\) trace, rho-block
  signs, Majorana \(B\), Wess-Bagger phase translation, low-dimensional
  Lorentzian traces, the source notes chiral-component free-fermion light-cone gamma
  convention, and Euclidean recursion.

## Exclusions

- No mostly-minus convention is introduced.
- No non-perturbative meaning is assigned to dimensional regularization or
  dimensional reduction.
- No supersymmetry transformation law is fixed here; later supersymmetry
  chapters must import these spinor conventions and then define their own
  field and Hilbert-space representation conventions separately.
