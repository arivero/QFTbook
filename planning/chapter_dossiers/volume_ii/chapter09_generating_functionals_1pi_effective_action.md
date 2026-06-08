# Volume II, Chapter 9 Dossier: Generating Functionals And The 1PI Effective Action
Source-File: monograph/tex/volumes/volume_ii/chapter23_generating_functionals_and_the_one_particle_irreducible_effective_action.tex

## Source Position

- Primary local source: second-sequence handwritten material, pages 71--80.
- Current monograph position: opening chapter of the renormalization volume,
  after the analytic \(S\)-matrix and high-energy-bound development.
- Source-order predecessor: infrared divergences and inclusive QED.
- Immediate successor in the monograph: renormalizability and local
  counterterms.
- Role in the monograph: introduce the exact source functional, its connected
  logarithm, and the Legendre transform whose vertices are the one-particle
  irreducible kernels.  This is the correct local organizing device for
  renormalization.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 71--80;
  checked against rendered page images `/tmp/qft253b_1pi_src-071.png`
  through `/tmp/qft253b_1pi_src-080.png` on 2026-05-22.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`, used
  only as a comparison layer.
- `SRC-EXTERNAL`: standard constructive and perturbative references on the
  effective action, including rigorous Legendre-transform conventions and the
  Euclidean convexity theorem.  These references are contextual; the chapter
  should be self-contained in notation and claims.

## Construction Task

The chapter must define the following objects before using them:

- the regulated functional integral \(Z[J]\);
- the opening notation dictionary separating the source functional \(Z[J]\)
  from the Kallen--Lehmann/LSZ pole residue \(Z_\phi^{\rm pole}\), the finite
  momentum-subtraction field rescaling \(Z_{\rm MOM}(\mu)\), the total
  chart field factor \(Z_\phi^{\rm chart}\), the minimal-subtraction pole
  factor \(Z_\phi^{\rm MS}\), and the composite-source mixing distributions
  \(\mathcal Z^I{}_{A_1\cdots A_r}\);
- the convention that \(D_\Lambda^{\rm ref}\phi\) denotes the finite-regulator
  scalar reference density, while \(\dd\mu_{C_\Lambda}\) denotes a Gaussian
  reference measure with the quadratic kinetic term absorbed;
- the logarithm \(\mathcal W[J]=\log Z[J]\) and the Lorentzian connected
  functional \(W[J]\) with \(Z[J]=e^{iW[J]}\);
- the status classification of \(\log Z\): algebraic logarithm in a completed
  formal perturbative ring, ordinary real logarithm for a positive finite
  Euclidean source functional, or a locally chosen branch of a zero-free
  Lorentzian complex source functional;
- source derivatives of \(Z[J]\) and \(\mathcal W[J]\);
- the Lorentzian--Euclidean source-convention bridge, including
  \(\mathcal W_L=iW_L\), \(\mathcal W_E=-W_E\), the source-sign map
  \(J_E=-J_L^{\rm W}\), and the connected-derivative normalizations;
- the positive finite Euclidean regulator assumption for convexity, including
  the regulated measurable configuration space, positive finite measure, real
  source domain, source-field pairing, and finiteness/nonvanishing of
  \(Z_{E,\Lambda}[J]\);
- the source-dependent field \(\varphi_J(x)=\delta W/\delta J(x)\);
- the Legendre transform \(\Gamma[\varphi]=W[J_\varphi]-\int\varphi J_\varphi\);
- the distinction between the local differentiable/formal Legendre transform
  used to define perturbative 1PI functionals and the convex
  Legendre--Fenchel transform defined from a positive Euclidean measure;
- the field-source inverse relation and \(\delta\Gamma/\delta\varphi=-J\);
- the background split \(\phi=\varphi+\widehat\phi\);
- the condition \(\langle\widehat\phi\rangle_{\varphi}=0\);
- the kernels \(\Gamma^{(n)}\) and their relation to amputated 1PI diagrams;
- the reconstruction of connected functions as trees built from exact
  propagators and exact 1PI vertices;
- the effective potential as the zero-derivative part of the local formal 1PI
  action, distinct from the exact convex Legendre--Fenchel effective action;
- the one-loop determinant formula for a constant scalar background,
  \(V_1=(2{\rm Vol})^{-1}\operatorname{Tr}\log(-\partial^2+V_0''(\varphi))\);
- the \(\overline{\rm MS}\) one-loop result
  \(V_1=M^4(\varphi)(\log(M^2(\varphi)/\mu^2)-3/2)/(64\pi^2)\);
- the Coleman--Weinberg finite subtraction condition
  \(V_{\rm eff}^{(4)}(M)=\lambda_{\rm CW}\), the resulting
  \(-25/6\) constant, the formal stationary scale, and the perturbative
  limitation of pure massless \(\lambda\phi^4\);
- dimensional transmutation as the RG statement that a running dimensionless
  coupling may be traded for the scale at which it reaches a specified
  reference value;
- the finite-regulator hypotheses under which Schwinger--Dyson integration by
  parts is legitimate, including the possible logarithmic derivative of the
  reference density and the separate BRST/BV treatment required in gauge
  theories;
- the condensed DeWitt notation used in the Schwinger--Dyson hierarchy;
- the insertion identity
  \(\langle(S_i[\phi]+J_i)\mathcal O[\phi]\rangle_J
  =i\langle\delta\mathcal O/\delta\phi^i\rangle_J\), the source-functional
  form
  \([S_i((1/i)\delta/\delta J)+J_i]Z[J]=0\), and the connected form obtained
  by shifting source derivatives through \(Z[J]=e^{iW[J]}\);
- the exact 1PI quantum equation of motion
  \(\Gamma_i[\varphi]=\langle S_i[\phi]\rangle_{J_\varphi}\);
- the first explicit members of the quartic scalar Schwinger--Dyson hierarchy:
  the full propagator equation and the full four-point vertex equation,
  including the connected four-point hierarchy equation, the Legendre
  identities for the connected four- and six-point kernels, and the statement
  that closing either equation is an additional approximation requiring its
  own control;
- the Euclidean convexity statement and its finite-dimensional toy model.

## Claim Ledger

1. With \(Z[J]=e^{iW[J]}\), connected Green functions are generated by
   \(\log Z[J]=iW[J]\), while \(\delta W/\delta J\) is the
   source-dependent one-point function.
1a. The meaning of \(\log Z\) is not uniform across regulators: formal
    perturbation theory uses the algebraic logarithm of
    \(Z[J]/Z[0]=1+A[J]\), positive Euclidean constructions use the ordinary
    real logarithm on a source domain with \(0<Z_E[J]<\infty\), and
    Lorentzian oscillatory constructions require a locally chosen branch on a
    source neighborhood with \(Z_L[J]\neq0\).
2. If the source-field map is locally invertible, the Legendre transform
   \(\Gamma[\varphi]=W[J_\varphi]-\int\varphi J_\varphi\) obeys
   \(\delta\Gamma/\delta\varphi=-J_\varphi\).
2a. In perturbative regulators such as dimensional regularization with
    minimal subtraction, \(W\), \(J_\varphi\), and \(\Gamma\) are formal local
    source-chart objects constructed coefficient by coefficient; no convexity
    statement follows because there is no positive finite measure.
3. The Hessians satisfy
   \[
     \int \dd^Dz\,
     \Gamma^{(2)}(x,z)W^{(2)}(z,y)=-\delta^{(D)}(x-y)
   \]
   in the Lorentzian convention of the chapter.
4. The background representation of \(e^{i\Gamma[\varphi]}\) has a linear
   source term chosen so that all quantum-field tadpoles vanish.
5. With this tadpole condition, connected diagrams that separate after cutting
   one internal propagator are generated by trees of lower 1PI kernels and are
   absent from \(\Gamma\).
6. In momentum space, the source insertion is a one-valent vertex with factor
   \(i\widetilde J(k)\) in the stated Fourier convention.
7. For a cubic microscopic interaction, the background split
   \(\phi=\varphi+\widehat\phi\) produces
   \(\varphi^3\), \(\varphi^2\widehat\phi\),
   \(\varphi\widehat\phi^2\), and \(\widehat\phi^3\) vertices, together with
   the source one-point vertex that enforces
   \(\langle\widehat\phi\rangle_\varphi=0\).
8. \(i\Gamma^{(n)}\) is computed perturbatively by amputated 1PI \(n\)-point
   diagrams with off-shell external momenta.
9. The derivative expansion of \(\Gamma\) is the low-momentum expansion of
   the exact local couplings when the relevant amplitudes are analytic.
10. Massless lines can make the low-momentum expansion nonanalytic, so the
   derivative expansion must be formulated with its domain of validity stated.
11. The exact connected functional is recovered from \(\Gamma\) by solving the
   stationary equation \(\delta\Gamma/\delta\varphi=-J\); diagrammatically,
   connected functions are trees made from exact 1PI vertices.
11a. At a translation-invariant finite scalar regulator, integration by parts
    in field space gives the exact Schwinger--Dyson insertion identity.  If
    the reference density is not translation invariant, its logarithmic
    derivative is part of the identity; if the change of variables has a
    nontrivial Jacobian, that Jacobian is an insertion.
11b. The equation \(\Gamma_i[\varphi]=\langle S_i[\phi]\rangle_{J_\varphi}\)
    is the exact 1PI equation of motion in the chosen source-coordinate system.  It is
    equivalent to the connected functional identity
    \(S_i(\varphi+(1/i)\delta/\delta J)1+J_i=0\).
11c. For quartic scalar theory, differentiating the connected
    Schwinger--Dyson identity gives an exact propagator equation involving the
    exact connected four-point kernel.  Differentiating three more times gives
    an exact connected four-point hierarchy member; substituting the Legendre
    identities for \(W^{(4)}\) and \(W^{(6)}\) gives the full four-point 1PI
    vertex equation involving the exact six-point vertex and the tree made
    from two exact four-point vertices joined by one exact propagator.
11d. A Schwinger--Dyson truncation is not part of the identity.  The act of
    discarding higher connected kernels or higher 1PI vertices must be
    justified by a stated small parameter, kinematic regime, renormalization
    condition with an error estimate, or explicit nonperturbative ansatz.
12. In the Euclidean convention
    \(Z_E[J]=e^{-W_E[J]}\), under the labeled positive finite Euclidean
    regulator assumption, \(W_E\) is concave and the corresponding
    Legendre--Fenchel transform is convex.  The finite-regulator convexity
    proof does not by itself establish a continuum Schwinger-functional limit.
13. The convention bridge is
    \(\mathcal W_L=\log Z_L=iW_L\) and
    \(\mathcal W_E=\log Z_E=-W_E\).  For the Euclidean source term
    \(-\langle J_E,\phi\rangle_E\), connected Schwinger distributions are
    \((-1)^n\delta^n\mathcal W_E|_{J=0}\), while Lorentzian connected
    time-ordered distributions are
    \(i^{-n}\delta^n\mathcal W_L|_{J=0}\).  The formal source-sign conversion
    under \(t=-i\tau\) is \(J_E=-J_L^{\rm W}\).
14. The finite-dimensional double-well model illustrates convexification and
    the domain of the perturbative saddle expansion: after the source
    subtracts the tangent line at a chosen branch, perturbation theory
    requires a positive quadratic shifted exponent.
15. The convex Legendre--Fenchel effective action and the perturbative 1PI
    effective action agree only where both constructions are defined, the
    convex conjugate is differentiable, and the source-field map is locally
    invertible.
16. The letter \(Z\) has no chapter-wide meaning by itself: in this part
    \(Z[J]\) is a source functional, \(Z_\phi^{\rm pole}\) is the isolated
    one-particle spectral atom used in LSZ, \(Z_{\rm MOM}(\mu)\) is a finite
    subtraction-scale field coordinate, \(Z_\phi^{\rm chart}\) is the
    Callan--Symanzik bare-to-renormalized field factor, \(Z_\phi^{\rm MS}\)
    is the minimal-subtraction pole factor, and \(\mathcal Z\) denotes
    composite-source mixing data.
17. For a constant background in massless \(\lambda\phi^4\),
    \(M^2(\varphi)=V_0''(\varphi)=\lambda\varphi^2/2\), and
    \[
      V_{\rm eff}^{\overline{\rm MS}}
      =
      \frac{\lambda}{24}\varphi^4
      +
      \frac{\lambda^2\varphi^4}{256\pi^2}
      \left(\log\frac{\lambda\varphi^2}{2\mu^2}-\frac32\right)
      +O(\lambda^3).
    \]
18. The one-loop effective potential satisfies the RG equation through
    \(O(\lambda^2)\) because
    \(\mu\partial_\mu V_1=-\lambda^2\varphi^4/(128\pi^2)\) cancels
    \(\beta_\lambda\partial_\lambda(\lambda\varphi^4/24)\) with
    \(\beta_\lambda=3\lambda^2/(16\pi^2)+O(\lambda^3)\).
19. In the Coleman--Weinberg finite subtraction chart
    \(V_{\rm eff}^{(4)}(M)=\lambda_{\rm CW}\),
    \[
      V_{\rm CW}
      =
      \frac{\lambda_{\rm CW}}{24}\varphi^4
      +
      \frac{\lambda_{\rm CW}^2}{256\pi^2}\varphi^4
      \left(\log\frac{\varphi^2}{M^2}-\frac{25}{6}\right)
      +O(\lambda_{\rm CW}^3).
    \]
    The constant follows from
    \(\partial_\varphi^4[\varphi^4\log(\varphi^2/M^2)]_{\varphi=M}=100\).
20. The formal nonzero stationary point obeys
    \[
      v=M\exp\left(\frac{11}{6}
        -\frac{16\pi^2}{3\lambda_{\rm CW}(M)}\right),
      \qquad
      V_{\rm CW}''(v)=\lambda_{\rm CW}^2v^2/(32\pi^2)+\cdots .
    \]
    This exhibits the scale-generating algebra, but in pure scalar theory it
    is not a controlled weak-coupling minimum: at \(M=v\) one needs
    \(\lambda_{\rm CW}=32\pi^2/11\), while small \(\lambda_{\rm CW}(M)\)
    makes the logarithm \(O(1/\lambda)\).
21. Dimensional transmutation is stated generally as
    \[
      \log(\Lambda_{g_*}/\mu)=\int_{g(\mu)}^{g_*}\dd g/\beta(g),
    \]
    so that a dimensionless coupling coordinate is replaced by a scale on the
    RG trajectory.  The sign and physical interpretation depend on the beta
    function; pure scalar \(\phi^4\) has a positive one-loop beta function,
    unlike asymptotically free gauge theory.
22. Gauge-theory perturbative effective potentials require the Nielsen
    identity of `sec:nielsen-identity-gauge-effective-potential`: off-shell
    potentials and stationary field coordinates are gauge-chart data, while
    exact stationary values are gauge independent only under the stated
    BRST/BV hypotheses.  Derivative-expanded saddles require the full
    functional identity, not only the zero-derivative potential.

## Figure Requirements

- Source insertions generating connected diagrams and the Legendre transform
  from \(W[J]\) to \(\Gamma[\varphi]\).
- Momentum-space source one-valent vertex with factor
  \(i\widetilde J(k)\).
- Cubic background split diagram showing background legs, quantum fluctuation
  legs, and the \(J_\varphi\widehat\phi\) vertex.
- Tadpole cancellation and 1PI kernels in the background-field expansion.
- Reconstruction of connected Green functions as trees of exact 1PI vertices.
- Euclidean convexity figure showing \(W_E[J]\) as a concave response
  functional and \(\Gamma_E[\varphi]\) as the convex Legendre transform.
- Branch/tangent finite-dimensional figure showing why a perturbative branch
  expansion requires a positive quadratic fluctuation form.

## Audit Notes

- No reader-facing references to source pages, course numbers, or the
  transcription workflow.
- Keep all signs explicit.  Lorentzian and Euclidean conventions are stated
  separately.
- Do not pass from Lorentzian source derivatives to Euclidean source
  derivatives without displaying the relevant powers of \(i\) and the sign
  introduced by the Euclidean source term.
- Avoid slogan-based contrasts.  Define the objects being used and state their
  assumptions.
- When later chapters use dimensional regularization, minimal subtraction, or
  formal BPHZ/1PI diagrams, interpret \(\Gamma\) as the local formal
  perturbative 1PI functional, not as the exact convex Legendre--Fenchel
  effective action, unless a positive Euclidean regulator is explicitly
  assumed.
- 2026-05-22 page-level source/figure audit complete.  Handwritten pages
  71--80 were rendered as `/tmp/qft253b_1pi_src-071.png` through
  `/tmp/qft253b_1pi_src-080.png`; compiled pages were checked as
  `/tmp/qft_ch29_1pi_actual-186.png` through
  `/tmp/qft_ch29_1pi_actual-196.png`, with the polished branch/tangent figure
  checked at `/tmp/qft_ch29_1pi_polished-195.png`.
- 2026-05-24 issue #235 pass: added the Lorentzian--Euclidean source bridge,
  including the log conventions, connected-derivative normalizations, the
  \(J_E=-J_L^{\rm W}\) sign map for the chapter's Euclidean source convention,
  and the instruction that Lorentz/spin/time-derivative indices require their
  own Wick-rotation matrices.
- 2026-05-25 issue #442 pass: moved the Wick-rotation sign chain to the first
  Lorentzian source definition as well:
  \(iS_L+i\langle J_L,\phi\rangle_L\mapsto
  -S_E+\langle J_L^{\rm W},\phi_E\rangle_E
  =-S_E-\langle J_E,\phi_E\rangle_E\) with
  \(J_E=-J_L^{\rm W}\).  This prevents the opening \(+\ii\langle J,\phi\rangle\)
  convention from appearing inconsistent with the later Euclidean
  positive-measure convention.
- 2026-05-24 issue #240 pass: added an explicit distinction between the local
  differentiable/formal 1PI Legendre transform used in perturbation theory
  and the convex Legendre--Fenchel transform that requires a positive finite
  Euclidean measure.  The manuscript now states that dimensional
  regularization/MS does not supply the positivity hypotheses for the
  Euclidean convexity theorem.
- 2026-05-24 issue #308 pass: promoted the positive-measure input for the
  Euclidean convexity theorem to the labeled assumption
  `ass:positive-euclidean-regulator-convexity`, with the regulated measurable
  space, positive finite measure, source domain, pairing, and
  integrability/nonzero partition-function hypotheses stated before the
  Hölder argument.
- 2026-05-24 issue #310 pass: replaced the ambiguous
  \([D\phi]_\Lambda\) source-functional notation by
  \(D_\Lambda^{\rm ref}\phi\) in the finite-dimensional scalar convention and
  cross-referenced the Gaussian/reference-density distinction from Volume I.
- 2026-05-24 issue #318 pass: added the missing status declaration for
  \(\log Z\) at the first use of the connected functional.  The manuscript now
  classifies the logarithm separately in formal perturbative, positive
  Euclidean constructive, and Lorentzian complex-branch settings before
  applying connected-kernel or Legendre-transform formulas.
- 2026-05-24 issue #433 pass: added the opening \(Z\)-factor dictionary for
  the renormalization part, explicitly separating \(Z[J]\) from
  \(Z_\phi^{\rm pole}\), \(Z_{\rm MOM}(\mu)\), \(Z_\phi^{\rm chart}\),
  \(Z_\phi^{\rm MS}\), and the composite-source mixing distributions
  \(\mathcal Z\).
- 2026-05-25 issue #452 pass: added the missing Schwinger--Dyson section next
  to the Legendre construction.  The chapter now states the finite-regulator
  integration-by-parts hypotheses, derives the insertion and source-functional
  identities, converts them to connected and 1PI form, and works out the full
  propagator and full four-point vertex members for quartic scalar theory with
  explicit truncation caveats.
- 2026-05-25 issue #458 pass: added the Coleman--Weinberg effective-potential
  section.  The manuscript now derives the one-loop determinant from the
  constant-background quadratic operator, evaluates the
  \(\overline{\rm MS}\) log potential, checks RG-scale cancellation against
  \(\beta_\lambda=3\lambda^2/(16\pi^2)\), derives the CW finite-subtraction
  potential with the \(-25/6\) constant, solves for the formal generated
  scale, states the pure-scalar perturbative-control limitation, and gives the
  general RG definition of dimensional transmutation.
- 2026-06-05 issue #773 cross-reference pass: added the gauge-theory caveat
  after the Coleman--Weinberg branch discussion, pointing to the BV Nielsen
  identity section and recording that gauge-fixed effective potentials are
  chart coordinates rather than off-shell observables.
