# Volume VI, Chapter 3 Dossier: Yang--Baxter Consistency And Internal Symmetry
Source-File: monograph/tex/volumes/volume_vi/chapter03_yang_baxter_internal_symmetry.tex

## Logical Role

- Role in the monograph: define the internal two-body \(R\)-matrix datum and
  derive the Yang--Baxter consistency condition from equality of
  three-particle factorization channels.
- Immediate predecessor: two-dimensional scattering analyticity and bootstrap
  pole data.
- Immediate successor: algebraic Bethe ansatz and transfer matrices.

## Definitions And Results

- Internal two-body \(R\)-matrix datum
  \(\mathfrak R=(\mathcal I,\{m_a,V_a\},\{S_{ab}\},\iota,\{C_a\},\mathcal A,\{\rho_a\})\),
  including antiparticle/crossing and optional internal symmetry data.
- Species spaces \(V_a\) and two-body maps \(S_{ab}(\theta)\).
- \(R\)-matrix convention \(R_{ab}=P_{ab}S_{ab}\).
- Regular factorized datum condition: two-body unitarity, crossing/residue
  bootstrap data, and the additive spectral-parameter Yang-Baxter identity.
- Derivation of the Yang--Baxter equation from reduced decompositions of the
  three-particle permutation.
- Extension from three-particle consistency to \(n\)-particle reduced-word
  independence via Coxeter moves.
- Additive vs multiplicative spectral-parameter conventions and braid vs
  fixed-tensor-product \(R\)-matrix conventions.
- Formal classical limit \(R=\id+\hbar r+\cdots\), yielding the
  spectral-parameter classical Yang-Baxter equation.
- Internal-symmetry intertwiner condition.
- Projector decomposition of \(R\)-matrices under irreducible representation
  channels.
- \(O(N)\) vector-representation channel example.
- Universal-\(R\) algebraic mechanism for the matrix identity and its limits as
  QFT input.
- Boundary Yang-Baxter/reflection equation and its analytic bootstrap status.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\mathcal I\) | set of stable particle species |
| \(V_a\) | finite-dimensional species space of particle \(a\) |
| \(S_{ab}(\theta)\) | physical-order two-body scattering map |
| \(R_{ab}(\theta)\) | endomorphism-valued \(R\)-matrix |
| \(\check R_{ab}\) | braid-convention scattering map with reordered codomain |
| \(\iota\), \(C_a\) | antiparticle involution and crossing identification |
| \(\mathcal A\), \(\rho_a\) | optional internal symmetry algebra/group and representation |
| \(\theta_{ij}\) | rapidity difference \(\theta_i-\theta_j\) |
| \(G\) | internal symmetry group or algebra |
| \(P_\lambda\) | projector onto irreducible symmetry channel |
| \(\mathcal R\) | universal algebraic \(R\)-element |
| \(K_a(\theta)\) | boundary reflection matrix |

## Claim Ledger

1. The chapter's central object is an explicitly stated internal two-body
   \(R\)-matrix datum; factorized scattering is the datum plus analytic
   bootstrap requirements and the YBE.
2. The Yang--Baxter equation is derived from equality of the two reduced
   three-particle scattering decompositions.
3. The same YBE and disjoint-factor commutation imply reduced-word
   independence for \(n\)-particle factorized scattering.
4. A formal quantum \(R\)-matrix expansion implies the spectral classical
   Yang-Baxter equation at order \(\hbar^2\).
5. Internal symmetry places \(R_{ab}(\theta)\) in
   \(\operatorname{End}_G(V_a\otimes V_b)\).
6. Multiplicity-free tensor-product channels reduce the matrix equation to
   scalar meromorphic functions constrained by projectors and the
   Yang--Baxter equation.
7. A universal \(R\)-element satisfying quasitriangular coproduct identities
   gives a matrix YBE after representation, but still supplies only candidate
   on-shell data for QFT.
8. Boundary integrability requires reflection data satisfying the boundary
   Yang-Baxter equation, boundary unitarity/crossing, and pole interpretation.
9. The \(R\)-matrix datum is on-shell data and does not construct local
   algebras by itself.

## Calculation Checks

- `calculation-checks/yang_baxter_internal_symmetry_checks.py` verifies the
  additive fixed-tensor-product rational Yang-Baxter identity, the spectral
  classical Yang-Baxter commutator identity for \(r(u)=P/u\), and the
  \(O(N)\) vector-channel projector decomposition used in the internal-symmetry
  discussion.

## Audit Notes

- 2026-06-02 issue #561 companion-check pass: added the exact finite
  Yang-Baxter/internal-symmetry check so that the chapter's matrix conventions
  and projector algebra have a public reproducibility artifact distinct from
  the Chapter 1 factorized-scattering check.

## Figures

- Three-line braid/Yang--Baxter diagram.
- Projector decomposition diagram for \(V_a\otimes V_b\).
