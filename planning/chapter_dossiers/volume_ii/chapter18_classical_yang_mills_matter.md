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
- the distinction between the anti-Hermitian mathematical Lie algebra
  \(\mathfrak g_{\mathrm{ah}}=\operatorname{Lie}(G)\) and the Hermitian
  generator coordinate space \(\mathfrak g=i\,\mathfrak g_{\mathrm{ah}}\);
- the anti-Hermitian connection one-form
  \(\mathsf A_{\mathrm{ah}}=-iA\) corresponding to the Hermitian local
  representative \(A\);
- the Hermitian-coordinate bracket
  \([X,Y]_{\mathrm H}=-i[X,Y]_{\mathrm{mat}}\), so explicit factors of \(i\)
  in transformation laws keep \(A_\mu,\zeta,F_{\mu\nu}\) Hermitian;
- Hermitian Lie-algebra generators \(t^a\) with
  \([t^a,t^b]=i f^{ab}{}_c t^c\);
- infinitesimal gauge transformation
  \(\delta A_\mu=\partial_\mu\zeta-i[A_\mu,\zeta]\);
- finite gauge transformation
  \(A_\mu'=gA_\mu g^{-1}+i g\partial_\mu g^{-1}\) with
  \(g(x)=\exp(i\zeta^a(x)t^a)\);
- the overlap transformation law for local connection representatives on
  nontrivial principal bundles and the covariant gluing of curvature;
- BCH closure and the adjoint action \(e^X Y e^{-X}\);
- covariant derivative \(\nabla_\mu=\partial_\mu-iA_\mu\);
- field strength \(F_{\mu\nu}=i[\nabla_\mu,\nabla_\nu]\);
- covariant transformation \(F'_{\mu\nu}=gF_{\mu\nu}g^{-1}\);
- invariant trace \(\operatorname{tr}(t^a t^b)=\kappa^{ab}\), cyclicity, and
  complete antisymmetry of \(f^{abc}=f^{ab}{}_e\kappa^{ec}\);
- Yang-Mills Lagrangian
  \(-\frac1{2g_{\mathrm{YM}}^2}\operatorname{tr}F_{\mu\nu}F^{\mu\nu}\);
- positive definite invariant form and compact reductive Lie algebras;
- the status distinction between the classical local Yang--Mills action and
  the open four-dimensional continuum quantum Yang--Mills existence/mass-gap
  problem;
- \(SU(2)\) and \(SU(N)\) examples with
  \(\operatorname{tr}(t^a t^b)=\frac12\delta^{ab}\);
- the four-dimensional \(\theta\)-term and its perturbative/topological roles;
- matter representations \(\rho_R:G\to GL(V_R)\), Lie-algebra generators
  \(t_R^a\), and the matter covariant derivative;
- invariant Hermitian pairings on compact-group representations and the
  resulting gauge-invariant contractions for scalar and Dirac matter;
- fundamental, anti-fundamental, and complexified adjoint representations of
  \(SU(N)\);
- QCD quark indices \(i,I,\alpha\), fermion kinetic term, Hermitian mass
  matrices \(m,\widetilde m\), and equivalent chiral complex mass matrix \(M\).

## Claim Ledger

1. The local Yang-Mills field is a connection one-form on a local
   trivialization of a principal \(G\)-bundle.
2. With Hermitian generators, the compact real Lie bracket is represented by
   \([X,Y]_{\mathrm H}=-i[X,Y]_{\mathrm{mat}}\), while formulas use ordinary
   matrix commutators with explicit \(i\)'s.
3. Closure of the local infinitesimal transformations is encoded by the Lie
   bracket of \(\mathfrak g\).
4. The finite transformation law is characterized by covariance of
   \(\partial_\mu-iA_\mu\).
5. Local connection representatives on overlapping trivializations obey the
   same transformation law as local gauge changes; curvature glues by
   conjugation.
6. Curvature transforms by conjugation, and invariant actions are built using
   invariant tensors on \(\mathfrak g\).
7. A positive invariant quadratic form gives the kinetic energy sign needed
   for unitary Lorentzian gauge fields.
8. The four-dimensional pure Yang--Mills continuum existence and positive
   mass-gap problem is the Clay Millennium problem; the local classical action,
   perturbative gauge-fixed expansions, and finite-cutoff lattice systems are
   not by themselves a completed continuum quantum Yang--Mills construction.
9. In \(D=4\), the \(\theta\)-density is local and gauge invariant; as a total
   derivative it enters perturbatively only through global/topological sectors.
10. Matter fields carry representations of \(G\), and their covariant
   derivative transforms in the same representation.
11. QCD uses the fundamental and anti-fundamental representations for quarks
    and antiquarks; the complexified adjoint representation describes
    adjoint-valued fields, with real adjoint fields selected by a reality
    condition.
12. Chiral mass notation repackages scalar and pseudoscalar Hermitian mass
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

- 2026-05-22 source pass: compared handwritten pages 157--168, the local
  transcription, and Ben Lou's transcription against
  `volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`.
- Tightened the invariant trace discussion by adding the source-level cyclicity
  identity
  \(\operatorname{tr}([t^a,t^b]t^c)=\operatorname{tr}(t^a[t^b,t^c])\).
- Made explicit the positive-form classification as abelian \(\mathbb R\)
  factors plus compact simple Cartan types \(A,B,C,D,E,F,G\), with
  \(\operatorname{tr}(t^a t^b)=\frac12\delta^{ab}\) as the default
  normalization.
- Added a rendered \(SU(N)\) representation/QCD-index figure, including the
  source convention
  \(\rho_{\overline{\square}}(g)=g^*\) without transposition and
  \(t_{\overline{\square}}^a=-(t^a)^*\).
- Rechecked the \(\theta\)-term statement: total derivative locally, no local
  perturbative vertex around the trivial sector, but nonzero action on
  finite-action topological sectors.
- Stop before Faddeev-Popov gauge fixing and BRST.
- State conventions for Hermitian generators and \(\gamma_5\) projectors.
- Do not let Hermitian-generator notation obscure the anti-Hermitian
  mathematical connection convention used in Chern-Weil and descent formulas.
- Avoid saying gauge symmetry is a physical symmetry; formulate it as local
  covariance/redundancy of field coordinates.
- No reader-facing source-page references or course labels.
- 2026-05-24 issue #261 pass: added a status remark naming the
  four-dimensional pure Yang--Mills existence and mass-gap problem as the Clay
  Millennium problem and separating that open continuum construction from the
  classical local action, perturbative BRST expansions, and finite-cutoff
  lattice regularizations.
- 2026-05-24 issue #263 pass: linked the status remark to the new lattice
  Yang--Mills chapter, where the finite-cutoff compact Haar formulation and
  continuum-limit hypothesis are developed before covariant gauge fixing.
