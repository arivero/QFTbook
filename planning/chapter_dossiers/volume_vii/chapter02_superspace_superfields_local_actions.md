# Volume VII, Chapter 2 Dossier: Superspace, Superfields, And Local Actions

## Logical Role

- Role in the monograph: introduce superspace as supergeometry after the
  supersymmetry algebra and representation data.
- Immediate predecessor: supertranslation algebra and Hilbert-space
  positivity.
- Immediate successor: multiplets, supersymmetric gauge theory, and
  nonrenormalization.

## Definitions And Results

- Affine \(\mathcal N=1\) superspace as a locally super-ringed space.
- Superfields as sections of the structure sheaf.
- Off-shell superfield multiplet as field-variable data, not particle-state
  data.
- Supercharges and covariant derivatives as derivations.
- Chiral superfields and component expansion.
- Component supersymmetry transformations for a chiral multiplet, derived
  explicitly from the chiral-coordinate supercharge action with odd
  supersymmetry parameters.
- Off-shell closure of the chiral-multiplet component transformations.
- Berezin integration as top-coefficient projection on the odd coordinate
  algebra.
- Normalization of \(\theta^2=\theta^\alpha\theta_\alpha\), hence
  \(\theta^2=2\theta^1\theta^2\) with the monograph epsilon convention, and
  the corresponding Berezin-measure normalization.
- \(D\)-terms, \(F\)-terms, and component Lagrangian for chiral fields.
- Nilpotent Taylor coefficient for chiral \(F\)-terms:
  \([W(\Phi)]_{\theta^2}=F^i\partial_iW-\frac12
  \partial_i\partial_jW\,\psi^{i\alpha}\psi^j_\alpha\).
- Wess--Zumino model component action, auxiliary-field elimination, and scalar
  potential derivation for canonical Kahler potential and holomorphic
  superpotential.
- Real vector superfields, chiral gauge transformations, Wess--Zumino gauge as
  a local gauge representative, and the component expansion of the Abelian
  chiral field strength \(W_\alpha\).
- Gauge-kinetic component coefficient of \(W^\alpha W_\alpha\), including
  the inverse epsilon-raising convention, the finite
  \(\sigma^{\mu\nu}\)-contraction identity, and the recovery of
  \(-F_{\mu\nu}F^{\mu\nu}/(4g^2)+D^2/(2g^2)\) from the real superspace
  action.
- Distinction between operator-valued fermion fields and Grassmann-valued
  path-integral variables by correlation functional.
- Supersymmetric Wilsonian scheme as regulated field-variable data,
  coarse-graining maps, local coordinates, Ward identities, and operator
  insertion prescriptions.
- Distinction between BV/off-shell-superfield Wilsonian integration and the
  separate problem of manifest supersymmetric ultraviolet regularization.
- Status cautions for dimensional reduction, higher-covariant-derivative
  heat-kernel schemes, and Pauli--Villars-type completions.
- Open problem of developing \(4D\) \(\mathcal N=1\) and \(\mathcal N=2\)
  gauge dynamics in explicitly defined supersymmetric Wilsonian schemes.
- Open problem of developing supersymmetric examples across dimensions:
  \(2D\) Landau--Ginzburg/Calabi--Yau/GLSM models, \(3D\)
  Chern--Simons--matter theories, and \(6D\) superconformal theories, each with
  its own algebraic, regulator, anomaly, and observable data.
- Localization datum: regulated integration space or cycle, odd symmetry,
  \(Q^2\), \(Q\)-exact deformation, convergence and boundary conditions,
  fixed-locus normal complex, zero modes, and contour or residue prescription.
- Open problem of developing supersymmetric localization from regulated
  localization data, including Jeffrey--Kirwan residues, noncompact
  directions, and singular instanton strata.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\mathcal O_{\mathbb M^{4|4}}\) | superspace structure sheaf |
| \(\theta^\alpha,\bar\theta^{\dot\alpha}\) | odd superspace coordinates |
| \(Q_\alpha,\bar Q_{\dot\alpha}\) | supertranslation derivations |
| \(D_\alpha,\bar D_{\dot\alpha}\) | covariant superspace derivatives |
| \(\Phi\) | chiral superfield |
| \(\phi,\psi_\alpha,F\) | chiral multiplet component fields |
| \(K\), \(W\) | Kähler potential and superpotential coordinates |
| \([W(\Phi)]_{\theta^2}\) | top chiral coefficient selected by \(d^2\theta\) |
| \(V\) | real vector superfield |
| \(\Lambda\) | chiral gauge parameter for vector-superfield gauge transformations |
| \(A_\mu,\lambda_\alpha,D\) | Wess--Zumino gauge vector-multiplet representative fields |
| \(W_\alpha\) | chiral gauge field-strength superfield |
| \(\sigma^{\mu\nu}\) | antisymmetric two-spinor Lorentz generator \(\frac14(\sigma^\mu\bar\sigma^\nu-\sigma^\nu\bar\sigma^\mu)\) |
| \(F_{\mu\nu}\) | Abelian field strength in the vector-superfield calculation |
| \(\mathfrak F_\Lambda\) | regulated field-variable space at Wilsonian scale \(\Lambda\) |
| \(S_\Lambda\) | Lagrangian functional in a Wilsonian scheme |
| \(Q\) | odd localization symmetry in a regulated localization datum |
| \(t\,QV\) | \(Q\)-exact localization deformation |

## Claim Ledger

1. Superspace is a locally super-ringed space, not an ordinary set of
   fermionic points.
2. Off-shell superfield multiplets package field variables and auxiliary
   fields; they are not Hilbert-space particle multiplets by definition.
3. Chiral superfields are the kernel of \(\bar D_{\dot\alpha}\).
4. The chiral-multiplet transformations follow from coefficient extraction in
   the chiral-coordinate expansion; auxiliary fields make component
   supersymmetry close off shell.
5. Berezin integration is coefficient extraction in the odd algebra.
6. The \(\theta^2\) normalization is part of the component convention:
   with \(\theta^2=\theta^\alpha\theta_\alpha\), the identity
   \((\theta\psi^i)(\theta\psi^j)=-\frac12\theta^2
   \psi^{i\alpha}\psi^j_\alpha\) gives the Yukawa coefficient
   \(-\frac12\partial_i\partial_jW\,\psi^i\psi^j\).
7. Supersymmetric local actions are built from \(D\)-term and \(F\)-term
   integrals under the stated convention.
8. The Wess--Zumino model component Lagrangian is obtained by a nilpotent
   Taylor expansion of \(W(\Phi)\) and top-coefficient extraction; eliminating
   auxiliary fields gives \(V=\sum_i|\partial_i W|^2\).
9. Wess--Zumino gauge is a local representative of a vector superfield modulo
   chiral gauge transformations; supersymmetry in this gauge requires a
   compensating gauge transformation and is not a gauge-invariant realization.
10. The Abelian vector-superfield expansion gives
   \([W^\alpha W_\alpha]_{\theta^2,{\rm bos}}=
   D^2-\frac12F_{\mu\nu}F^{\mu\nu}
   -\frac{\ii}{4}\epsilon^{\mu\nu\rho\sigma}
   F_{\mu\nu}F_{\rho\sigma}\); hence the real superspace action has the
   Chapter 3 Yang--Mills normalization and auxiliary term.
11. Holomorphic and nonrenormalization statements require an explicitly
   defined supersymmetric Wilsonian scheme before they can be used in exact
   gauge dynamics.
12. BV/off-shell-superfield methods can organize the symmetry-preserving
   Wilsonian integration problem after a regulator is supplied, but do not
   themselves prove the existence of a manifest supersymmetric regulator.
13. Dimensional reduction and proposed higher-derivative or Pauli--Villars-type
   supersymmetric regulators require explicit loop-order or scheme-level
   consistency checks before they certify nonrenormalization or anomaly
   statements.
14. Supersymmetric examples in dimensions other than four must not be treated
   as analogies: \(2D\) LG/CY/GLSM, \(3D\) Chern--Simons--matter, and \(6D\)
   SCFT examples have distinct definitions, anomaly data, extended operators,
   and nonperturbative-status ledgers.
15. Localization formulae require a regulated localization datum; residue
   prescriptions and singular instanton sectors are not automatic consequences
   of formal \(Q\)-exact deformation.

## Calculation Checks

- `calculation-checks/susy_superspace_component_checks.py` verifies the
  \(\theta^2\) normalization, left-derivative rule, two-spinor Grassmann
  product identity, chiral \(F\)-term Yukawa coefficient, and auxiliary
  \(F\)-field square completion used in this chapter.
- `calculation-checks/susy_vector_superfield_checks.py` verifies the
  inverse epsilon-raising convention, the finite
  \(\sigma^{\mu\nu}\)-contraction identity, the bosonic \(\theta^2\)
  coefficient of \(W^\alpha W_\alpha\), and the real
  gauge-kinetic/auxiliary normalization.

## Figures

- Sheaf diagram for affine superspace.
- Chiral multiplet component ladder.
- \(D\)-term and \(F\)-term projection diagram.
