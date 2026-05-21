# Volume II, Chapter 18 Dossier: Classical Yang-Mills Theory And Matter

## Source Position

- Primary local source: second-sequence handwritten material, pages 157--168.
- Immediate predecessor: Wilsonian effective actions and exact cutoff flow.
- Immediate successor in the source order: gauge fixing, ghosts, and BRST.
- Role in the monograph: introduce nonabelian gauge fields as
  Lie-algebra-valued connections, construct their curvature and invariant
  action, state the trace and compactness assumptions needed for unitary
  Lorentzian gauge theory, and add matter fields in representations with QCD
  notation.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 157--168;
  checked against rendered page images in
  `monograph/tex/build/source_visual_trace/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  corresponding classical Yang-Mills section, used only as a comparison layer.
- `SRC-EXTERNAL`: standard Lie-algebra and principal-connection conventions
  used as guardrails only; the chapter follows the local source order and
  conventions.

## Construction Task

The chapter must define and derive:

- gauge potentials \(A_{a\mu}\) carrying spacetime and internal indices;
- Hermitian Lie-algebra generators \(t^a\) with
  \([t^a,t^b]=i f^{ab}{}_c t^c\);
- infinitesimal gauge transformation
  \(\delta A_\mu=\partial_\mu\zeta-i[A_\mu,\zeta]\);
- finite gauge transformation
  \(A_\mu'=gA_\mu g^{-1}+i g\partial_\mu g^{-1}\) with
  \(g(x)=\exp(i\zeta^a(x)t^a)\);
- BCH closure and the adjoint action \(e^X Y e^{-X}\);
- covariant derivative \(\nabla_\mu=\partial_\mu-iA_\mu\);
- field strength \(F_{\mu\nu}=i[\nabla_\mu,\nabla_\nu]\);
- covariant transformation \(F'_{\mu\nu}=gF_{\mu\nu}g^{-1}\);
- invariant trace \(\operatorname{tr}(t^a t^b)=\kappa^{ab}\), cyclicity, and
  complete antisymmetry of \(f^{abc}=f^{ab}{}_e\kappa^{ec}\);
- Yang-Mills Lagrangian
  \(-\frac1{2g_{\mathrm{YM}}^2}\operatorname{tr}F_{\mu\nu}F^{\mu\nu}\);
- positive definite invariant form and compact reductive Lie algebras;
- \(SU(2)\) and \(SU(N)\) examples with
  \(\operatorname{tr}(t^a t^b)=\frac12\delta^{ab}\);
- the four-dimensional \(\theta\)-term and its perturbative/topological roles;
- matter representations \(\rho_R:G\to GL(V_R)\), Lie-algebra generators
  \(t_R^a\), and the matter covariant derivative;
- fundamental, anti-fundamental, and adjoint representations of \(SU(N)\);
- QCD quark indices \(i,I,\alpha\), fermion kinetic term, Hermitian mass
  matrices \(m,\widetilde m\), and equivalent chiral complex mass matrix \(M\).

## Claim Ledger

1. The local Yang-Mills field is a connection one-form on a local
   trivialization of a principal \(G\)-bundle.
2. Closure of the local infinitesimal transformations is encoded by the Lie
   bracket of \(\mathfrak g\).
3. The finite transformation law is characterized by covariance of
   \(\partial_\mu-iA_\mu\).
4. Curvature transforms by conjugation, and invariant actions are built using
   invariant tensors on \(\mathfrak g\).
5. A positive invariant quadratic form gives the kinetic energy sign needed
   for unitary Lorentzian gauge fields.
6. In \(D=4\), the \(\theta\)-density is local and gauge invariant; as a total
   derivative it enters perturbatively only through global/topological sectors.
7. Matter fields carry representations of \(G\), and their covariant
   derivative transforms in the same representation.
8. QCD uses the fundamental and anti-fundamental representations for quarks
   and antiquarks; the adjoint representation describes the gauge field.
9. Chiral mass notation repackages scalar and pseudoscalar Hermitian mass
   matrices into a complex flavor matrix.

## Figure Requirements

- Index and Lie-algebra data for \(A_{a\mu}\), \(A_\mu=A_{a\mu}t^a\), and
  the infinitesimal transformation.
- Connection-curvature diagram showing covariance of \(\nabla_\mu\), curvature,
  invariant trace, and the Yang-Mills action.
- \(SU(N)\) representation diagram/table: fundamental, anti-fundamental,
  adjoint, and QCD quark indices.
- Chiral mass decomposition diagram relating \(m,\widetilde m\) to \(M\).

## Audit Notes

- Stop before Faddeev-Popov gauge fixing and BRST.
- State conventions for Hermitian generators and \(\gamma_5\) projectors.
- Avoid saying gauge symmetry is a physical symmetry; formulate it as local
  covariance/redundancy of field coordinates.
- No reader-facing source-page references or course labels.
