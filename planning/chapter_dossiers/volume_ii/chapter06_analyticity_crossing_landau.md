# Volume II, Chapter 6 Dossier: Analyticity, Crossing, and Landau Singularities

## Scope

- Begins the general analytic-structure portion after bound states and
  resonances.
- Develops the physical \(s\)-channel region for identical massive scalar
  \(2\to2\) scattering and the first-sheet boundary value using the sheet
  convention introduced earlier in Chapter 3.
- States real analyticity and crossing as analytic properties of the
  continued amplitude under the standard massive-local-QFT hypotheses.
- Proves the primitive Wightman tube-domain theorem from spectral support and
  proves Jost-edge gluing of ordered tubes from local commutativity plus the
  edge-of-the-wedge theorem.
- Proves the Dyson/Jost--Lehmann hyperboloid representation for
  Dyson-regular causal commutator matrix elements.  The
  admissible-hyperboloid support restriction needed for the later
  fixed-\(t\) domain theorem is stated conditionally on support-pruned Dyson
  data in the coincidence slab, and the chapter explicitly separates the
  still-needed verification that the relevant LSZ source-current commutators
  satisfy Dyson regularity and support-pruning.
- Records the partial-wave unitarity boundary condition on the physical
  \(s\)-channel cut before using analytic continuation away from it.
- Adds a generalized-unitarity and one-loop-reduction bridge after Cutkosky:
  physical cuts versus algebraic generalized cuts, a one-loop reconstruction
  datum tying cut data, representative choice, rational/regulator input,
  reduction, boundary/branch data, subtraction, and observable assembly,
  one-loop scalar-integral reconstruction, a complete massless
  \(\lambda\phi^4\) four-point cut reconstruction with negative controls,
  a planar \(\mathcal N=4\)
  four-gluon MHV quadruple-cut reconstruction with explicit supermultiplet
  state sum and lower-topology negative control, a triple-cut triangle
  projection rule after known box-residue subtraction, the pure-Yang--Mills
  all-plus rational blind spot including the five-point all-plus
  partial-amplitude template, a four-point color--kinematics/double-copy
  gateway with generalized-gauge negative controls, a solved finite two-scale
  massless box master with branch data, the bubble
  IBP/differential equation master calculation, and a
  two-stage master-integral layer: first a local two-master threshold block,
  then a two-letter transport audit exposing connection data, Euclidean
  boundary constants, branch/path prescriptions, lower sectors, and the
  finite-remainder/observable assembly that separates reconstructed virtual
  amplitudes from infrared-safe physical observables.
- Adds Steinmann sequential-discontinuity constraints as a scoped causal
  boundary-value statement, with channel-overlap definitions, sheet/order
  conventions, an overlapping versus compatible finite example, and explicit
  status separation between quoted theorem input and locally checked causal
  algebra.
- Derives the Landau equations from Feynman-parameter pinches.
- Works out the two-particle threshold and triangle/anomalous-threshold
  examples.

## Source Spine

- `transcription/tex/253b/scattering_rg_qcd.tex`, subsection "Analyticity,
  Crossing, and Landau Singularities", through the Coleman--Thun/anomalous
  threshold discussion.
- `references/253b transcribed lecture notes.tex`, corresponding
  analyticity/Landau section, used cautiously to compare figures and source
  ordering.
- Volume I chapters on LSZ, partial waves, and unitarity.
- Volume II Chapters 3--5 for bound-state poles, resonance poles, and
  four-point pole factorization.
- Veltman's largest-time equation and the 't Hooft--Veltman Diagrammar
  treatment are used as theorem-boundary controls for graph-level Cutkosky
  line replacement.
- Bern--Dixon--Dunbar--Kosower, Bern--Dixon--Kosower, Britto--Cachazo--Feng,
  Ossola--Papadopoulos--Pittau, Forde, Bern--Morgan,
  Brandhuber--McNamara--Spence--Travaglini, Ussyukina--Davydychev,
  Passarino--Veltman,
  Chetyrkin--Tkachov, Tkachov, Kotikov, and Gehrmann--Remiddi form the source
  lineage for the generalized-unitarity, planar \(\mathcal N=4\) MHV
  quadruple-cut, rational-term, integrand-reduction, explicit box-function,
  IBP, and differential-equation bridge.
- Bern--Carrasco--Johansson's tree-level amplitude relations and double-copy
  construction supply the source spine for the four-point
  color--kinematics gateway; the chapter uses them only as a scoped entry
  point, not as a proof of loop-level numerator representations.
- Steinmann's original Wightman/retarded-commutator papers and the
  Stapp/Cahill--Stapp scattering-amplitude refinements are used as source
  traces for the quoted conditional Steinmann relation; the chapter does not
  treat the name "Steinmann relations" as a proof certificate.

## Definitions and Symbols

| Symbol | Meaning |
| --- | --- |
| \(s,t,u\) | mostly-plus Mandelstam invariants \(s=-(k_1+k_2)^2\), \(t=-(k_1-k_3)^2\), \(u=-(k_1-k_4)^2\) for incoming \(k_1,k_2\) and outgoing \(k_3,k_4\) |
| \(\mathcal M(s,t)\) | connected invariant amplitude, analytically continued where defined |
| \(\mathfrak S_m\) | complexified on-shell invariant surface \(s+t+u=4m^2\) |
| \(\mathcal O_{\mathrm{poly}}(\mathcal D)\) | holomorphic functions on a complex kinematic domain with local polynomial-growth boundary estimates |
| \(\operatorname{bv}F\) | boundary-value distribution of a holomorphic germ, tested in \(C_c^\infty\) locally and in Schwartz topology when polynomial growth controls noncompact edges |
| \(W_\sigma,w_\sigma\) | ordered Wightman distribution and its translation-reduced version for an ordering \(\sigma\in S_n\) |
| \(T_{n-1}\) | primitive mostly-plus forward tube \(\{\xi_j-\ii\eta_j:\eta_j\in V_+^\circ\}\) for reduced Wightman variables |
| \(C(\xi)\) | positive cone generated by the reduced differences \(\xi_j\) |
| Jost configuration | real reduced configuration for which every nonzero vector in \(C(\xi)\) is spacelike |
| primitive BEG envelope | envelope of holomorphy generated by all ordered Wightman tubes and their Jost-edge identifications |
| \(C(x)\) | causal commutator matrix coefficient, supported in the closed causal cone |
| \(R\) | momentum-space coincidence slab in which the causal Fourier transform vanishes |
| \(h_\pm(\vec q)\) | spacelike or null boundary graphs of a coincidence slab |
| \(H_\pm(u,\mu)\) | upper/lower sheets of the mass hyperboloid \((q-u)^2=-\mu^2\) |
| \(S_R\) | set of \(R\)-admissible hyperboloids supporting the Dyson weight |
| \(D_6\) | odd fundamental solution of the six-dimensional wave equation, normalized by \(\mathcal F_{\mathbf y}D_6(t,\cdot)(\mathbf k)=\sin(|\mathbf k|t)/|\mathbf k|\) |
| \(\pi_{y*}U\) | auxiliary pushforward of a six-dimensional lift, defined by normalized approximate identities in the \(y\)-dual variables |
| \(\iota^*F\) | trace of a six-dimensional momentum distribution at \(p_1=p_2=0\), \(\iota(q)=(q,0,0)\) |
| Dyson-regular commutator | causal commutator whose Fourier transform is the \(p_1=p_2=0\) restriction of a rotationally invariant six-dimensional wave-equation solution with well-defined Cauchy data |
| \(\mathcal H\Psi\) | Dyson hyperboloid transform pairing \(\Psi(u,\mu)\) with \(\varepsilon(q^0-u^0)\delta((q-u)^2+\mu^2)\) |
| support-pruned Dyson data | representative of the Dyson Cauchy-data class, modulo \(\ker\mathcal H\), supported in \(S_R\) for a specified coincidence slab |
| axis trace | restriction \(F(q,p_1,p_2)|_{p_1=p_2=0}\) of a six-dimensional Dyson lift |
| \(\Psi(u,\mu)\) | distributional Dyson weight in the causal-commutator representation |
| first sheet | branch reached from the physical Feynman prescription without crossing a cut |
| \(\alpha_i\) | Feynman parameters for internal lines |
| \(q_i(\ell,p)\) | internal momentum on line \(i\), affine in loop momenta and external momenta |
| \(S_\ell(s)\) | angular-momentum-\(\ell\) partial-wave scattering eigenvalue in the two-particle sector |
| \(\beta(s)\) | local square-root variable for a two-particle threshold, whose sign changes on the adjacent sheet |
| \(M_{\mathrm{inel}}\) | invariant mass threshold of the lightest inelastic channel |
| \(\Delta_m^\pm(x)\) | positive/negative-frequency on-shell Wightman distributions for mass \(m\) |
| \(G_\sigma\) | circled graph associated to a vertex circling \(\sigma\) in the largest-time identity |
| \(C\) | set of internal lines crossed by a perturbative physical cut |
| \(\operatorname{Cut}_C\mathcal I\) | algebraic generalized cut of a regulated loop integrand on the selected on-shell denominators |
| \(\mathfrak D_{1{\rm L}}\) | one-loop reconstruction datum collecting cut data, representative choice, rational/regulator input, reduction, boundary/branch data, subtraction, and observable assembly |
| \(D_{\rm cut},D_{\rm rep},D_{\rm rat},D_{\rm red},D_{\rm bc},D_{\rm sub},D_{\rm obs}\) | gates in the one-loop reconstruction datum: cuts/state sums, integrand representative, rational/regulator probes, reduction map, boundary/branch constants, subtraction convention, and observable data |
| \(D_i(\ell)\) | one-loop denominator \((\ell+K_i)^2+m_i^2-\ii0\) |
| \(I_r\) | scalar one-loop integral with \(r\) propagators in the declared regulator |
| \(C_{012}(t),R_b(t),\Pi_0\) | triple-cut residue on a residual cut parameter, known box residues visible on the same triple cut, and the Laurent constant projection used after box subtraction |
| \(R_n\) | rational term not fixed by a strictly four-dimensional cut analysis |
| \(\mathcal P_n\) | local subtraction polynomial or scheme-dependent counterterm |
| \(B(Q^2)\), \(\widehat B(x)\) | Euclidean bubble master and its four-dimensional cut-normalized physical continuation |
| \(I_{a,b}(Q^2)\) | Euclidean one-loop bubble integral family used for IBP reduction |
| \(\vec M\), \(A_T\), \(y_\gamma\) | local two-master threshold vector, nilpotent threshold residue, and sheet/path-labelled threshold coordinate in the multi-master differential-system model |
| \(\vec J\), \(A_0,A_1\), \(L_0^\gamma,L_1^\gamma\) | two-letter master-transport vector, residue matrices, and path-labelled logarithmic transports in the finite master-system audit |
| \(\Omega\), \(W_\alpha\), \(\mathcal U_\gamma\) | reduced master-integral connection, Landau-letter functions, and path-ordered transport from a Euclidean boundary point |
| \(\mu_\perp^2\) | squared loop momentum in the \(-2\epsilon\)-dimensional complement, invisible on four-dimensional cuts |
| \(\eta_i^A,Q^{A\alpha}\) | \(\mathcal N=4\) on-shell superspace variables and supermomentum used in the MHV quadruple-cut state sum |
| \(C_{\Box}^{\mathcal N=4}\) | planar four-gluon MHV scalar-box coefficient obtained from the maximal cut after integrating over the four internal on-shell multiplets |
| \(A_4^{(0)}(1^-,2^-,3^+,4^+)\) | color-ordered tree MHV four-gluon amplitude in the spinor-helicity convention used for the gauge-theory control |
| \(I_4^{(D)}(s,t)\) | dimensionally regulated massless scalar box in the four-point MHV control |
| \(S,T\), \(\mathcal F_{\Box}(S,T)\), \(\kappa_{\Box}\) | Euclidean box invariants \(S=-s>0,T=-t>0\), finite reduced two-scale box master after IR-pole subtraction, and its Euclidean boundary/subtraction constant |
| \(\operatorname{tr}_{-}(i j k l)\) | chiral spinor trace coordinate \(\langle i j\rangle[j k]\langle k l\rangle[l i]\) used in the five-point all-plus rational amplitude |
| \(C_{\rm loop}\), \(C_{\rm rat}\), \(C_{5,\rm rat}\) | loop-normalization and all-plus rational-term constants, fixed only after color, particle-content, and loop-measure conventions are declared |
| \(c_s,c_t,c_u\) | four-point cubic color factors satisfying the Lie-algebra Jacobi relation \(c_s+c_t+c_u=0\) |
| \(n_s,n_t,n_u\), \(\widetilde n_i\) | four-point generalized kinematic numerators and the second numerator copy used in the color--kinematics/double-copy gateway |
| \(S_\alpha,\mathcal J\) | one-loop contact/IBP/evanescent surface numerator shift in a Jacobi graph triplet and its induced kinematic Jacobi defect |
| \(\mathbf I^{(1)}_\Lambda\) | one-loop infrared subtraction operator used to define the finite remainder in a declared regulator and finite subtraction convention |
| \(\mathcal F^{(1)}_\Lambda\) | finite one-loop hard remainder after subtracting \(\mathbf I^{(1)}_\Lambda\mathcal A^{(0)}_\Lambda\) |
| \(\mathcal R_\Lambda^{\rm sub}[W]\), \(\mathcal C_\Lambda^{\rm fact}[W]\) | real-emission/subtraction and factorization/matching pieces needed to assemble an infrared-safe observable for measurement \(W\) |
| \(B_{\rm cut},B_{\rm rat},B_{\rm IBP},B_{\rm conn},B_{\rm bc},B_{\rm branch},B_{\rm lower},B_{\rm UV},B_{\rm IR/real},B_{\rm fact},B_{\rm meas}\) | residual bounds in the one-loop reconstructed-observable comparison and master-transport audit |
| \(s_I\) | all-incoming channel invariant \(-(\sum_{i\in I}p_i)^2\), with channel class \([I]=\{I,I^c\}\) |
| overlapping channels | channel classes \([I]\), \([J]\) for which \(I\cap J\), \(I\setminus J\), \(J\setminus I\), and \((I\cup J)^c\) are all nonempty |
| compatible channels | channel classes with complementary representatives that are disjoint or nested |
| \(\eta_I\) | sheet label specifying upper or lower boundary value in the \(s_I\) channel variable |
| \(\operatorname{Disc}_{I;\eta}\) | ordered channel discontinuity with the remaining sheet choices fixed by \(\eta\) |
| Landau equations | on-shell and stationary conditions for a contour pinch |
| anomalous threshold | first-sheet singularity from a compatible positive-parameter Landau pinch |

## Assumptions

- The external particles are the lightest identical stable scalars of mass
  \(m\) unless stated otherwise.
- Mostly-plus metric: an on-shell mass-\(m_i\) internal line satisfies
  \(q_i^2+m_i^2=0\).
- Perturbative diagrams are considered with Feynman denominators
  \(q_i^2+m_i^2-\ii0\).
- Partial-wave unitarity is stated as a boundary condition on the upper edge
  of the physical cut; angular analyticity and high-energy boundedness are
  deferred.
- Physical-cut discontinuities are separated into the exact Hilbert-space
  unitarity identity, which sums exact on-shell intermediate states, and the
  perturbative Cutkosky line-replacement rule, which is obtained only after a
  regulator, graph expansion, and perturbative ordering have been chosen.
- Graph-level Cutkosky replacement is derived from the largest-time identity:
  the sum over all circlings of a scalar graph vanishes, mixed circlings carry
  on-shell Wightman distributions, and the \(s\)-channel physical cut is the
  subsum whose mixed lines separate the external labels into the chosen
  subprocesses.
- Generalized cuts in the new section are algebraic or contour probes of a
  regulated one-loop integrand.  They coincide with physical Cutkosky cuts
  only after the relevant real positive-energy branch, state sum, and sheet
  have been imposed.
- The one-loop reconstruction datum is an ordered bookkeeping contract:
  generalized cuts constrain residues of an integrand representative,
  rational/regulator probes supply cut-invisible virtual information,
  reduction and boundary/branch data evaluate the master sector, and
  subtraction plus observable data are required before a virtual amplitude is
  promoted to a finite physical quantity.
- The one-loop scalar-basis discussion assumes dimensional regularization,
  declared scalar-integral normalizations, and subtraction of higher-topology
  contributions before lower-topology coefficients are read from triple and
  double cuts.
- The massless \(\lambda\phi^4\) example uses the interaction
  \(-\lambda\phi^4/4!\), identical unordered intermediate scalar states, and
  the cut-normalized bubble \(\widehat B=B/(16\pi^2)\), for which
  \(\operatorname{Disc}\widehat B=\ii/(8\pi)+O(\epsilon)\).
- The Yang--Mills helicity control uses color-ordered all-outgoing external
  gluons, four-dimensional spinor-helicity little-group weights, and the
  standard tree-level selection rule that a four-gluon tree amplitude is
  nonzero only in the two-negative or two-positive sector.  The planar
  \(\mathcal N=4\) MHV box example is a leading-color primitive partial
  amplitude; the full leading-color amplitude is recovered by the cyclic
  trace sum in the chosen generator convention.  Its maximal-cut coefficient
  uses the complete sixteen-state on-shell supermultiplet, not a gluon-only
  state sum.  Numerical all-plus coefficients are stated only up to the
  declared loop, color, and particle-content normalization.
- The color--kinematics gateway is restricted to four massless adjoint
  external particles at tree level, after contact terms have been absorbed
  into generalized cubic numerators.  It assumes \(s+t+u=0\), the color
  Jacobi relation, and a Jacobi-satisfying numerator representative.  The
  paragraph explicitly does not construct loop-level color--kinematics
  numerators.
- The finite box master is a reduced four-point massless scalar box after the
  universal soft/collinear pole part has been subtracted in a declared
  convention.  The displayed normalization fixes
  \(S\partial_S\mathcal F_{\Box}=\log(S/T)\); changing the scalar-integral or
  finite IR-subtraction convention rescales the finite function and shifts
  \(\kappa_{\Box}\) but does not remove the need for both \(S\)- and
  \(T\)-channel data plus branch prescription.
- The IBP identity assumes dimensional regularization, analytic continuation
  in \(\epsilon\), and the standard vanishing of scaleless tadpoles.  The
  bubble differential equation is solved with Euclidean boundary data at
  \(Q^2=\mu^2\) and physical branch \(Q^2\mapsto -s-\ii0\).
- The multi-master threshold model is a local Fuchsian block after
  lower-sector inhomogeneous terms have been separated.  It assumes that the
  physical sheet is specified by an analytic-continuation path and that
  Euclidean boundary constants are supplied independently from cut/monodromy
  data.
- The two-letter master-transport model is a finite normalized sector used to
  audit the data needed after IBP closure.  It checks boundary constants,
  noncommuting residues, branch/path prescriptions, and lower-sector residuals;
  it is not claimed to be an additional solved physical integral family beyond
  the explicit finite box master.
- The finite-observable assembly assumes a declared one-loop infrared
  subtraction convention, an infrared-safe measurement or matching target,
  and a real-emission/factorization construction using the same finite
  subtraction convention as the virtual finite remainder.  It is a comparison
  datum for one-loop observables, not a proof of all-order factorization.
- The Steinmann section assumes a declared boundary-value setting before the
  vanishing statement: connected time-ordered kernels or LSZ-reduced amplitudes
  with external pole/contact terms separated; selected channel boundary values
  as tempered distributions; perturbative causal factorization/largest-time or
  axiomatic Bros--Epstein--Glaser/Steinmann hypotheses; and exclusions of
  threshold endpoints, coincident configurations, and unseparated bound-state
  poles.
- The chapter proves only the finite causal-order obstruction and the
  double-Cauchy discontinuity algebra for the Steinmann discussion.  The full
  distributional existence and vanishing theorem is quoted conditionally from
  the Steinmann/Stapp/Cahill--Stapp framework.
- The analytic amplitudes are exact Hilbert-space boundary values when
  spectral/locality/LSZ hypotheses are being used; Landau and
  Feynman-parameter discussions are coefficientwise perturbative graph
  analyses with the status declared in
  `def:scattering-time-ordered-correlator-status`.
- Analyticity and crossing are used as structural hypotheses supported by
  locality, spectral support, LSZ, and perturbation theory; existing rigorous
  theorem sets cover only parts of the desired physical domain.
- Analytic continuation means continuation of a polynomial-growth holomorphic
  germ on the complexified on-shell invariant surface.  Equality on a real
  edge is equality of boundary-value distributions, and uniqueness is by
  edge-of-the-wedge plus the identity theorem on connected holomorphic
  domains.
- The primitive Wightman-domain theorem assumes Wightman temperedness,
  spectral support in \(\overline V_+\), translation covariance, and graded
  local commutativity.  It proves the ordered tube support and Jost gluing
  statements; it does not by itself prove the stronger fixed-\(t\)
  Lehmann--Martin cut plane.
- The Dyson representation theorem assumes a Dyson-regular tempered causal
  commutator, a distributional coincidence slab \(R\), and spacelike/null slab
  boundaries.  Dyson regularity is the explicit six-dimensional lift and
  Cauchy-data condition; the six-dimensional Cauchy formula itself is now
  proved in `prop:six-dimensional-distributional-cauchy-formula` from the
  spatial Fourier transform of the wave equation.  The auxiliary pushforward
  normalization is also theorem-level: `prop:auxiliary-pushforward-momentum-trace`
  proves that \(\pi_{y*}U=\kappa C\) is equivalent, with the chapter's
  Fourier convention, to \(\iota^*F=\kappa\widehat C\).  Dyson regularity is
  not automatic for an arbitrary Wightman distribution.  Under this
  hypothesis the theorem proves the hyperboloid representation; the support
  restriction to the admissible set \(S_R\) is a separate support-pruning
  statement about the Cauchy-data class modulo the kernel of the hyperboloid
  transform.  Local contact polynomials from source-current reduction are
  separated as subtraction/contact data.

## Claims to Derive

- The physical \(s\)-channel region has
  \[
    s=4(k^2+m^2),\qquad
    t=-2k^2(1-\cos\theta),\qquad
    s\ge4m^2-t,\quad t\le0.
  \]
- The positive \(t\)-channel thresholds used in crossing and angular
  analyticity are crossed-channel timelike invariants, not physical
  \(s\)-channel scattering angles.
- For fixed \(t<0\), the first sheet has a right-hand \(s\)-channel cut
  starting at \(4m^2\), a left-hand crossed-channel cut starting at \(-t\),
  and possible bound-state poles.
- The notation \(\mathcal M(s,t)\) must always specify whether it denotes the
  physical boundary-value distribution or the holomorphic germ on the relevant
  connected complex domain; no perturbative Borel summation is part of this
  definition.
- Primitive Wightman domain theorem: for every ordered Wightman distribution
  \(w_\sigma(\xi_1,\ldots,\xi_{n-1})\),
  \[
    \operatorname{supp}\widehat w_\sigma\subset(\overline V_+)^{n-1},
  \]
  and \(w_\sigma\) is the tempered boundary value of a holomorphic function on
  the forward tube \(T_{n-1}=\{\xi-\ii\eta:\eta\in(V_+^\circ)^{n-1}\}\), with
  polynomial tube bounds from the finite-order Schwartz seminorms of the
  Fourier transform.
- Jost-edge gluing theorem: if two orderings differ by an adjacent
  transposition in a Jost neighbourhood, graded local commutativity identifies
  their boundary distributions on the Jost edge up to the Koszul sign, and
  edge-of-the-wedge gives the common continuation to the envelope of the two
  primitive tubes.  Iterating adjacent transpositions produces the primitive
  Bros--Epstein--Glaser envelope.
- Four-point scattering output: after connected-part subtraction and
  stable-particle pole separation, LSZ boundary values in the physical
  \(s\)-, \(t\)-, and \(u\)-channel regions are boundary values of the same
  primitive analytic germ wherever the LSZ limits exist.  This is recorded in
  a remark rather than a theorem-family wrapper because it is a conditional
  transfer of the proved primitive tube/Jost-edge results through the LSZ
  boundary operation.  The fixed-\(t\) Jin--Martin domain remains a stronger
  retarded-commutator and Lehmann--Martin theorem, not a corollary of
  primitive tube analyticity alone.
- Dyson/Jost--Lehmann representation: if \(C(x)\) is a Dyson-regular causal
  commutator matrix coefficient, then
  \[
    \widehat C(q)=
    \langle\Psi(u,\mu),
      \varepsilon(q^0-u^0)\delta((q-u)^2+\mu^2)\rangle_{u,\mu},
  \]
  If in addition \(\widehat C\) vanishes in a slab \(R\) and the Dyson
  Cauchy data are support-pruned relative to \(R\), then \(\Psi\) can be
  chosen with \(\operatorname{supp}\Psi\subset S_R\), the set of hyperboloids
  whose upper sheet stays above \(h_+\) and lower sheet stays below \(h_-\).
  The implication from slab vanishing to such support-pruned data is not
  asserted without proof.
- Hyperboloid-transform support-pruning: for Dyson Cauchy data
  \(\Psi_\Sigma\), the support-restricted representative is a distribution
  \(\Psi_R\) satisfying
  \[
    \operatorname{supp}\Psi_R\subset S_R,\qquad
    \mathcal H\Psi_R=\mathcal H\Psi_\Sigma .
  \]
  This isolates the classical Jost--Lehmann support-removal step as a
  theorem-level input for the physical LSZ source-current kernels.
- Codimension-two trace nonuniqueness: there is a nonzero smooth tempered
  \(O(2)\)-invariant solution of the six-dimensional wave equation whose
  auxiliary-momentum trace \(F(q,0,0)\) vanishes on a slab.  The construction
  uses smooth radial \(1+2\)-dimensional wave data supported away from the
  auxiliary axis and proves the needed finite-propagation statement from the
  local energy identity.
- Six-dimensional wave-equation Cauchy formula: if
  \(F\in\mathcal S'(\mathbb R^{1,5})\) solves
  \(\Box_{1,5}F=0\) and has tempered Cauchy traces
  \(f=F|_{\tau=\tau_*}\), \(g=\partial_\tau F|_{\tau=\tau_*}\), then
  \[
    F(Y_0)=
    \langle f,\partial_\tau D_6(\tau_*-\tau_0,\cdot-\mathbf y_0)\rangle
    -
    \langle g,D_6(\tau_*-\tau_0,\cdot-\mathbf y_0)\rangle .
  \]
  This is part of the proof infrastructure for the Dyson/JLD theorem, not an
  unproved appeal to a standard wave-equation fact.
- Auxiliary pushforward/momentum trace theorem: if
  \(U\in\mathcal S'(\mathbb R_x^4\times\mathbb R_y^2)\) has a
  \(y\)-pushforward defined by approximate identities
  \(m_\epsilon(y)=\int\rho_\epsilon(p)e^{ip\cdot y}\dd^2p\), then the
  \(p=0\) trace of \(\widehat U(q,p)\) exists and equals
  \(\widehat{\pi_{y*}U}\); conversely a continuous \(p=0\) trace defines the
  pushforward.  This fixes the normalization of the Dyson lift's projection
  to the original four-dimensional commutator.
- LSZ retarded-commutator input: once the source-current commutator is
  verified to be Dyson-regular, it has the Dyson hyperboloid representation;
  in each spectral coincidence slab the support-restricted representation
  additionally requires support-pruned Dyson data.  Retarded and advanced
  transforms are boundary values of the same analytic continuation through
  the slab, up to finite local-contact polynomials.
- On the physical \(s\)-channel cut,
  \[
    \mathcal M(s,t)
    =
    -16\pi i\sqrt{\frac{s}{s-4m^2}}
    \sum_{\ell=0}^{\infty}(2\ell+1)P_\ell(\cos\theta)(S_\ell(s)-1),
    \qquad
    \cos\theta=1+\frac{2t}{s-4m^2},
  \]
  with \(|S_\ell(s)|\le1\) for \(s\ge4m^2\) and
  \(|S_\ell(s)|=1\) below the first inelastic threshold.
- The Cutkosky theorem must contain both pieces: the Hilbert-space
  discontinuity from \(S^\dagger S=1\) and the largest-time/circling argument
  that identifies a graph cut with on-shell line replacements.
- A generalized cut
  \[
    \operatorname{Cut}_C\mathcal I
    =
    \left.\mathcal I\prod_{i\in C}D_i\right|_{D_i=0}
  \]
  is an algebraic reconstruction probe until positive-energy support, state
  sums, and sheet data turn it into a physical cut.
- At one loop, the cut-visible scalar-integral expansion has the form
  \[
    \mathcal A_n^{(1)}
    =
    \sum c_4I_4+\sum c_3I_3+\sum c_2I_2+R_n+\mathcal P_n,
  \]
  with \(R_n\) and \(\mathcal P_n\) requiring information beyond strictly
  four-dimensional branch cuts.
- In massless \(\lambda\phi^4\), the \(s\)-channel cut of the one-loop
  four-point amplitude is
  \[
    \operatorname{Disc}_s\mathcal M_4^{(1)}
    =
    \ii\frac{1}{2!}\lambda^2\int d\Phi_2
    =
    \frac{\ii\lambda^2}{16\pi}+O(\epsilon),
  \]
  and the crossing-complete cut-constructible amplitude is
  \[
    \mathcal M_{4,\mathrm{cut}}^{(1)}
    =
    \frac{\lambda^2}{2}\{\widehat B(s)+\widehat B(t)+\widehat B(u)\}.
  \]
  An \(s\)-only ansatz matches one cut but misses the crossed cuts; local
  counterterms have no channel discontinuity.
- Four-dimensional generalized cuts can miss rational terms from
  \(-2\epsilon\)-dimensional numerator components.  D-dimensional unitarity,
  massive continuation, or independent rational recursion is needed when such
  terms matter.
- Planar \(\mathcal N=4\) SYM at four points gives a cut-constructible MHV
  control:
  \[
    A_{4,\mathcal N=4}^{(1)}
    =
    C_{\rm loop} s t\, A_4^{(0)}(1^-,2^-,3^+,4^+) I_4^{(D)}(s,t),
  \]
  with the box coefficient fixed by the quadruple cut after the
  supersymmetric state sum.  The state sum is represented by Berezin
  integration over the four internal on-shell multiplets; the integrations
  collapse the internal supermomentum constraints to the external
  \(\delta^{(8)}(Q)\) and leave the \(s t\) Jacobian.  One two-particle cut
  alone cannot distinguish the box from lower-topology contamination; after
  the box subtraction the triple and double cuts have no polynomial
  remainder and no rational remnant in this declared \(\mathcal N=4\)
  theory.
- Pure Yang--Mills all-plus is the rational negative control:
  four-dimensional two-particle cuts of
  \(A_4^{(1)}(1^+,2^+,3^+,4^+)\) vanish by the tree helicity selection rule,
  but the one-loop rational term
  \[
    C_{\rm rat}\frac{[12][34]}{\langle12\rangle\langle34\rangle}
  \]
  is nonzero.  The missing data are \(\mu_\perp^2\) or massive-scalar
  continuation data, whose dimension-shifted integrals leave the rational
  term.
- The same rational blind spot persists beyond four points.  The leading-color
  five-gluon all-plus partial amplitude is recorded as
  \[
    C_{5,\rm rat}
    \frac{\sum_{i<j<k<l}\operatorname{tr}_{-}(i j k l)}
    {\langle12\rangle\langle23\rangle\langle34\rangle
     \langle45\rangle\langle51\rangle}.
  \]
  Each trace term is little-group neutral, the cyclic denominator gives
  all-plus weights, the total dimension is \(4-5=-1\), and strict
  four-dimensional two-particle cuts still vanish by the tree helicity
  selection rule.  The missing input is again \(D\)-dimensional or
  massive-scalar unitarity data, not a local counterterm.
- Four-point color--kinematics gateway: after the tree amplitude is written in
  cubic form,
  \[
    \mathcal A_4^{\rm YM}
    =
    g^2\left(\frac{c_s n_s}{s}
             +\frac{c_t n_t}{t}
             +\frac{c_u n_u}{u}\right),
    \qquad c_s+c_t+c_u=0,
  \]
  a color--kinematics representative also obeys
  \(n_s+n_t+n_u=0\).  Generalized-gauge shifts preserving the gauge amplitude
  need not preserve this kinematic Jacobi relation, so a naive numerator
  square is not representation-independent.  The double-copy formula
  \[
    \mathcal M_4^{\rm grav}
    =
    \left(\frac{\kappa}{2}\right)^2
    \left(\frac{n_s\widetilde n_s}{s}
          +\frac{n_t\widetilde n_t}{t}
          +\frac{n_u\widetilde n_u}{u}\right)
  \]
  is asserted only for Jacobi-compatible numerator data and null shifts, such
  as the four-point common shift \(n_i\mapsto n_i+\alpha D_i\).
- The bubble IBP family obeys
  \[
    0=(D-2a-b)I_{a,b}-bI_{a-1,b+1}+bQ^2I_{a,b+1},
  \]
  and hence
  \[
    Q^2I_{1,2}=-(D-3)I_{1,1}=-(1-2\epsilon)I_{1,1}
  \]
  after the scaleless \(I_{0,2}\) sector is dropped.
- The bubble master satisfies
  \[
    Q^2\frac{d}{dQ^2}I_{1,1}(Q^2)=-\epsilon I_{1,1}(Q^2),
  \]
  with singular point \(Q^2=0\) matching the massless two-particle Landau
  threshold.
- The two-master threshold block uses
  \[
    A_T=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
    \vec M_{\rm sing}=(1+A_T\log y_\gamma)\vec C,
  \]
  so \(\operatorname{Mon}_{y=0}\vec M_{\rm sing}=2\pi i A_T\vec C\).  The
  branch of \(M_2\) is fed by \(C_1\), while regular constants
  \(\vec R_0\) change finite amplitudes without changing the threshold
  monodromy.  Hence cuts and IBP equations must be supplemented by boundary
  data, path/sheet data, and subtraction conventions.
- Steinmann definitions: for all-incoming momenta, a channel is the partition
  \([I]=\{I,I^c\}\) with \(s_I=-(\sum_{i\in I}p_i)^2\).  Two channels overlap
  exactly when no complementary representatives make them disjoint or nested.
  Ordered discontinuities are boundary-value differences with the remaining
  sheet labels held fixed; order and sheet are part of the notation.
- Quoted Steinmann relation: under the declared boundary-value hypotheses,
  \(\operatorname{Disc}_J\operatorname{Disc}_I F=0\) and
  \(\operatorname{Disc}_I\operatorname{Disc}_J F=0\) for overlapping channels,
  as distributions on the common real edge.  This is not asserted for arbitrary
  functions called amplitudes.
- Causal mechanism: for overlapping \(I,J\), the four nonempty sectors
  \(X=I\cap J\), \(Y=I\setminus J\), \(Z=J\setminus I\), \(W=(I\cup J)^c\)
  force a strict time-order two-cycle for every pair of cut orientations.  At
  five points, \(I=\{1,2\}\), \(J=\{2,3\}\) gives the explicit cycle between
  legs \(1\) and \(3\).  The compatible disjoint pair
  \(I=\{1,2\}\), \(K=\{3,4\}\) admits an acyclic order
  \(\{1,2\}\succ\{5\}\succ\{3,4\}\).
- Double spectral comparison: a compatible pair may have a local double Cauchy
  term whose ordered double discontinuity is
  \((2\pi i)^2\rho_{I,K}(s_I,s_K)\); the analogous overlapping double density
  is absent/zero under Steinmann.  This separates Cutkosky single cuts,
  Landau candidate singular surfaces, and Steinmann sequential-cut support.
- 2026-05-24 issue #391 pass: corrected the exact discontinuity identity to
  use \(\mathcal M_{X\alpha}\mathcal M_{X\beta}^*\), where
  \(\mathcal M_{\gamma\delta}\) denotes \(\delta\to\gamma\).  The conjugated
  factor is the adjoint matrix element for \(\beta\to X\), not the reversed
  amplitude \(X\to\beta\); replacing it by \(\mathcal M_{\beta X}^*\) would
  assume a separate reciprocity or time-reversal statement.
- Feynman-parameter pinches obey
  \[
    \alpha_i(q_i^2+m_i^2)=0,\qquad
    \sum_i \alpha_i q_i\cdot{\partial q_i\over\partial \ell_a^\mu}=0
  \]
  for every loop momentum \(\ell_a\).
- The two-propagator Landau equations give the ordinary two-particle
  threshold \(P^2=-4m^2\) in the equal-mass example.
- Triangle diagrams can produce first-sheet anomalous thresholds, including
  the equal-internal-mass criterion \(M_1,M_2<\sqrt2m\) versus
  \(M_1,M_2>\sqrt2m\), and the Coleman--Thun type mechanism.

## Figures

- Physical \(2\to2\) region and first-sheet \(s\)-plane.
- Crossing regions in the real \((s,t)\)-plane.
- Contour pinch leading to Landau equations.
- Bubble threshold Landau solution.
- Triangle Landau vector test and anomalous threshold.

## Boundaries

- No Lehmann ellipse, partial-wave convergence, Froissart--Martin mechanism,
  dispersion relations, or polynomial boundedness; those belong to the next
  chapter.
- No claim that primitive tube/Jost analyticity already gives the full
  fixed-\(t\) cut plane or the Jin--Martin polynomial bound.
- No attempt to make an axiomatic foundation out of perturbative Landau
  analysis.
- No extension of Steinmann relations to massless amplitudes, regulator
  limits, anomalous-threshold sheets, or symbol-level/extended Steinmann
  statements without additional hypotheses.
- No claim that the new generalized-unitarity section completes all of issue
  #769: the reconstruction-datum pass consolidates the already-present
  one-loop gates rather than solving a new integral family.  The scalar
  example and the MHV/all-plus helicity control close the first one-loop
  workflow and rational-term boundary.  The five-point
  all-plus template adds a genuine nonabelian one-loop partial amplitude
  beyond four points, the planar \(\mathcal N=4\) MHV block supplies a full
  cut-constructible nonabelian state-sum reconstruction in a declared
  supersymmetric theory, the four-point color--kinematics gateway supplies a
  tree-level numerator-representation and double-copy boundary, the one-loop
  surface-obstruction block explains why integrated gauge-null surface terms
  are not automatically double-copy nulls, the finite box block supplies one
  solved physical two-scale master, and the two-letter transport model makes
  the multi-master boundary/path contract explicit.  Nontrivial coupled
  physical multi-master families, finite-field technology, constructive
  loop-level color--kinematics numerator solutions, and higher-loop
  generalized cuts remain future work.

## Audit Notes

- 2026-05-24 issue #319 pass: added a chapter-opening status reminder
  separating exact Hilbert-space analytic boundary values from
  coefficientwise perturbative Landau/Feynman-parameter graph analysis.
- 2026-05-24 issue #425 pass: renamed the threshold square-root variable from
  \(\rho(s)\) to \(\beta(s)\) so it cannot be confused with the
  Kallen--Lehmann spectral measure \(d\rho\).
- 2026-05-24 issue #435 pass: linked the chapter's physical-region formulas
  to the part-wide mostly-plus Mandelstam convention and explicitly separated
  physical \(s\)-channel \(t\le0\) from positive crossed-channel timelike
  thresholds.
- 2026-05-27 issue #495 domain pass: added theorem-level proof of the
  primitive Wightman tube-domain theorem and Jost-edge gluing.  The proof
  constructs the spectral-support inclusion using intermediate spectral
  projections, obtains the Fourier--Laplace tube and tempered boundary-value
  bounds, derives Jost-edge equality from local commutativity, and applies
  edge-of-the-wedge as the complex-analysis tool that generates the primitive
  BEG envelope.  The chapter now states explicitly that the fixed-\(t\)
  Lehmann--Martin/Jin--Martin theorem requires additional retarded-commutator
  and LSZ-domain work.
- 2026-05-27 issue #495 JLD pass: added the causal-commutator Dyson
  representation theorem, then tightened it by introducing the
  Dyson-regularity hypothesis.  The proof uses the six-dimensional
  wave-equation lift of a causal distribution with well-defined Cauchy data,
  recovers the four-dimensional commutator as a boundary value on the
  auxiliary-momentum plane, rewrites the Cauchy formula as a superposition of
  mostly-plus mass hyperboloids.  A later tightening pass separated the
  admissible-hyperboloid support restriction from slab vanishing: the
  support-restricted representation now requires support-pruned Dyson data
  relative to the slab.  The same pass adds an explicit wave-equation example
  proving that vanishing of the \(p=0\) trace on a slab is not enough to
  determine or prune the six-dimensional data.  Remaining fixed-\(t\)
  closure work includes proving Dyson regularity and support-pruning for the
  LSZ source-current matrix coefficients, the Bros--Epstein--Glaser analytic
  completion, and the
  off-shell normal-coordinate and large-contour growth hypotheses needed to
  apply the LSZ-transfer and finite-subtraction Cauchy theorems of Volume II,
  Chapter 7.
- 2026-05-27 issue #495 spectral-support pass: added the source-current
  coincidence-region proposition.  The proof derives the Fourier-support
  inclusions for the two ordered source-current matrix elements from
  translation covariance and the joint spectral theorem, using spectral
  matrix distributions on
  \(B_f\times\operatorname{Spec}(P)\times B_i\).  The generalized
  sharp-momentum shorthand recovers the supports \(\Sigma_{bc}^{fi}-K\) and
  \(K-\Sigma_{cb}^{fi}\).  The coincidence slab used by the Dyson/JLD theorem
  is therefore a proved spectral-support output; the remaining source-current
  issues are Dyson regularity and support-pruned Dyson data, not the spectral
  vanishing region.
- 2026-05-27 issue #495 Dyson-lift microlocal pass: added the proposition
  isolating the ordinary distribution-product content of Dyson's light-cone
  lift.  Away from the vertex \((x,y)=(0,0)\), the product
  \(\pi^*C\delta(x_D^2-|y|^2)\) is proved to exist under the explicit
  wavefront condition
  \(\operatorname{WF}(C)\cap\mathcal N_{\rm lc}=\varnothing\).  The proof
  computes the pullback wavefront set, the conormal wavefront set of
  \(\delta(g)\), applies the product criterion, and proves that extension
  ambiguity at the vertex is exactly a finite contact polynomial after
  Fourier transform.  This does not prove Dyson regularity for the physical
  source-current kernels; it turns that phrase into a precise remaining
  wavefront/scaling or renormalized-lift theorem.
- 2026-05-27 issue #495 finite-scaling-degree lift pass: added Dyson
  regularity modulo contact terms and the punctured-lift extension theorem.
  The theorem now proves the local finite-scaling-degree extension mechanism
  with the required cone equation \((x_D^2-|y|^2)U=0\), \(O(2)\)-invariance,
  temperedness, and \(y\)-pushforward normalization modulo contact terms.  It
  also corrects a common false shortcut: support on the quadratic cone alone
  does not annihilate normal derivatives of delta at the vertex.  Remaining
  source-current work is therefore the actual QFT theorem verifying these
  wavefront/scaling, cone-equation, pushforward, and Cauchy-trace hypotheses
  for LSZ source-current kernels.
- 2026-05-27 issue #495 source-current differential pass: added local scaling
  degree and proved that replacing fields by LSZ source currents is the
  relative-coordinate differential operation
  \(\mathcal K_b(2\partial_x)\mathcal K_c(-2\partial_x)\).  The proposition
  proves preservation of causal support, punctured light-cone conormal
  wavefront avoidance, finite scaling degree, and finite scaling degree of
  the punctured six-dimensional Dyson product.  This removes the source-current
  differential step from the list of hidden assumptions; the remaining theorem
  is the genuine extension/Cauchy-data and support-pruning construction for
  the source-current kernels.
- 2026-06-05 issue #781 pass: added the Steinmann sequential-discontinuity
  section after Cutkosky and before crossing/edge-of-wedge.  The pass defines
  all-incoming channel variables, overlap versus compatible channels,
  sheet-labelled ordered discontinuities, states the vanishing only under a
  declared boundary-value hypothesis as a quoted theorem, proves the finite
  causal-order obstruction and double-spectral coefficient comparison, and
  links the result to Cutkosky, Landau, and fixed-\(t\) dispersion.  The
  companion script `calculation-checks/steinmann_channel_checks.py` checks the
  finite channel and causal-order algebra.
- 2026-06-05 issue #769 first architecture pass: inserted the
  generalized-unitarity and one-loop-reduction bridge immediately after
  Cutkosky.  The pass separates physical discontinuities from algebraic cuts,
  gives the one-loop scalar-integral coefficient workflow, reconstructs the
  complete massless \(\lambda\phi^4\) four-point cut-constructible amplitude
  with explicit state-sum normalization and negative controls, explains the
  four-dimensional rational blind spot, and reduces/solves the bubble master
  through IBP and a differential equation.  The companion script
  `calculation-checks/generalized_unitarity_reduction_checks.py` checks the
  cut matrix, nullspace, IBP, differential-equation, and branch-threshold
  ledger.
- 2026-06-05 issue #769 gauge-theory rational pass: added the
  MHV-box/all-plus rational-term control to prevent the generalized-unitarity
  section from remaining scalar-only.  The pass distinguishes the
  cut-constructible planar \(\mathcal N=4\) four-point MHV box from the
  strictly four-dimensional cut-invisible pure-Yang--Mills all-plus rational
  amplitude, explains the \(\mu_\perp^2\)/massive-scalar route to the missing
  rational term, and updates the companion script to check little-group
  weights, dimensions, four-dimensional all-plus cut vanishing, and the
  evanescent probe.
- 2026-06-05 issue #769 virtual-to-observable pass: added the
  finite-remainder assembly layer after the cut-equality warning.  The pass
  separates reconstructed virtual amplitudes from infrared-safe observables by
  requiring a common infrared subtraction convention, real-emission/subtraction
  construction, factorization/matching terms, and residual budget.  The
  companion script now checks exact Laurent-pole cancellation, omitted
  rational-term failure, finite IR-scheme transport, and underbudgeted
  observable residuals.
- 2026-06-05 issue #769 multi-master threshold pass: added a local
  two-master differential-system block after the bubble master equation.  The
  pass exposes nilpotent threshold mixing, path/sheet-labelled monodromy,
  Euclidean regular constants, and the global connection/transport data
  needed to evaluate master integrals in physical amplitudes.  The companion
  script checks the nilpotent residue, Fuchsian equation residual, diagonal
  shortcut failure, cut-only boundary ambiguity, and multi-master residual
  budget.
- 2026-06-05 issue #769 five-point all-plus pass: extended the gauge-theory
  rational-term control from the four-point warning to the leading-color
  five-gluon all-plus partial-amplitude template.  The text records the
  chiral trace numerator, all-plus denominator weights, strict \(D=4\)
  two-particle-cut vanishing, and the need for \(D\)-dimensional or
  massive-scalar unitarity data.  The companion script checks little-group
  neutrality of each trace term, all-plus weights, mass dimension, cyclic
  omitted-leg coverage, cut-invisibility, and the evanescent-probe power.
- 2026-06-05 issue #769 finite box master pass: added a physical two-scale
  massless box master between the all-plus rational controls and the IBP
  subsection.  The text defines the finite reduced box after soft/collinear
  pole subtraction, solves
  \(S\partial_S\mathcal F_{\Box}=\log(S/T)\),
  \(T\partial_T\mathcal F_{\Box}=-\log(S/T)\), fixes the Euclidean boundary
  constant \(\kappa_{\Box}\), records the \(s\)-channel branch
  \(\log(S/T)\mapsto \log(s/(-t))-\ii\pi\), and gives one-cut-only and
  branch-omission negative controls.  The companion script checks the
  polynomial log differential equations, scale invariance, Hessian rank,
  equal-scale boundary, one-cut deformation, and physical-branch imaginary
  coefficient.
- 2026-06-05 issue #769 master-transport pass: extended the multi-master
  discussion beyond a local threshold block by adding a two-letter transport
  audit.  The pass records a reduced Fuchsian system with noncommuting
  nilpotent residues, Euclidean boundary constants, separate \(x=0\) and
  \(x=1\) discontinuities, a cut-invisible boundary direction, path-order
  sensitivity, and a physical-observable residual budget with connection,
  boundary, branch, and lower-sector terms.  The companion script checks the
  exact rational transport, the boundary ambiguity, the second-order
  commutator contribution, and underbudgeting when branch/path or boundary
  residuals are omitted.
- 2026-06-05 issue #769 planar \(\mathcal N=4\) MHV supercut pass: expanded
  the previous MHV box control into an explicit four-gluon leading-color
  partial-amplitude reconstruction.  The text now displays the trace-sum
  convention, the MHV tree superamplitude, the box quadruple-cut Berezin
  state sum over the four internal on-shell multiplets, the resulting
  \(s t\,\mathcal A_4^{(0),\mathrm{MHV}}\) coefficient, and the negative
  controls showing that a single two-particle cut can hide lower-topology
  contamination and that a gluon-only state sum is not the \(\mathcal N=4\)
  theory.  The companion script checks the sixteen-state multiplet ledger,
  Parke--Taylor component extraction, maximal-cut normalization, lower
  topology ambiguity, vanishing lower-topology remainder, and cyclic trace
  count.
- 2026-06-05 issue #769 color--kinematics gateway pass: added a four-point
  tree-level bridge from cubic color factors to Jacobi-satisfying kinematic
  numerators and the gravity double-copy numerator square.  The text separates
  gauge-amplitude equivalence from Jacobi-compatible numerator data and states
  that loop-level color--kinematics representations remain future work.  The
  companion script checks exact color and kinematic Jacobi identities,
  generalized-gauge invariance of the gauge amplitude, failure of the naive
  numerator square under a non-Jacobi shift, and invariance under the
  four-point common denominator-weighted shift.
- 2026-06-05 issue #769 reconstruction-datum coherence pass: added the
  one-loop reconstruction datum near the opening of the generalized-unitarity
  section, collecting cut data, integrand representative choice,
  rational/regulator input, reduction, boundary/branch information,
  subtraction convention, and observable assembly into one named workflow.
  The companion script checks gate coverage, distinguishes single-gate
  omissions, and verifies that four-dimensional-cut-only and virtual-only
  shortcuts underbudget the full reconstruction.
- 2026-06-05 issue #769 loop-level color--kinematics obstruction pass: added
  `ca:loop-level-color-kinematics-surface-obstruction`, which promotes the
  tree gateway into a one-loop representative-level warning.  The block shows
  that contact, evanescent, or IBP-surface numerator shifts can be invisible to
  selected cuts and color-weighted gauge integration while breaking the local
  numerator Jacobi identity and changing a naive double-copy pairing.  The
  companion script verifies a finite Jacobi-triplet model with zero cut
  signature, gauge-null color weighting, nonzero Jacobi defect, nonzero
  double-copy shift, and representative-level repair.
- 2026-06-05 issue #769 sector-projection pass: added
  `ca:bubble-sector-projection` in the IBP subsection.  The pass shifts the
  reduction discussion from a squared-propagator identity to the amplitude
  assembly problem: a cut-generated bubble numerator is decomposed into the
  parent master and lower one-point sectors, the parent cut is shown to fix
  only \(c_0-c_P/2\), and the text distinguishes the valid massless
  dimensional-regularization collapse from the failure when lower sectors
  carry scale or boundary data.  The companion script checks the exact
  numerator projection, the parent-cut coefficient, vector
  Passarino--Veltman reduction, and the lower-sector negative control.
- 2026-06-05 issue #769 triple-cut projection pass: added
  `ca:triple-cut-triangle-projection` near the opening one-loop
  reconstruction bridge.  The pass makes the triangle step explicit:
  \(\Pi_0 C_{012}(t)\) is not the triangle coefficient until the known box
  residues sharing the same triple cut have been subtracted.  The companion
  script checks the Laurent constant projection, raw-constant contamination,
  post-box subtraction, omitted-box negative control, wrong-box-normalization
  negative control, and spurious nonzero-Laurent-power cancellation.
