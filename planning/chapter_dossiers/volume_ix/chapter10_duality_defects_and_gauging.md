# Chapter 10: Duality Defects, Gauging, And Orbifold Data
Source-File: monograph/tex/volumes/volume_ix/chapter10_duality_defects_and_gauging.tex

## Source Position

Volume IX develops finite gauging and duality defects immediately after the
categorical-symmetry chapter.  This chapter now supplies the finite examples
and derivations needed there: groupoid gauging, gauging-interface slab fusion,
the finite gauging mechanism map, orbifold twisted-sector data, self-dual
gauging defects, normal-subgroup gauging, and electric-magnetic line-lattice
duality walls.

## Notation Inventory

- `mathfrak D_{Q,G}`: finite gauging and duality-defect datum, including the
  QFT, finite symmetry, background-bundle groupoids, anomaly class,
  trivialization/counterterm, symmetry defects, gauging interfaces, optional
  self-duality equivalence, and line-charge lattice data.
- `G`, `H`: finite internal symmetry group and a finite subgroup to be gauged.
- `P -> M`: principal finite-group background bundle.
- `Bun_G(M)`: finite groupoid of \(G\)-bundles on \(M\).
- `Aut(P)`: automorphism group of the finite background bundle \(P\).
- `Z_Q[M;P]`: partition function of \(\mathcal Q\) in finite background \(P\).
- `alpha`, `tau`: anomaly class and chosen anomaly-trivialization /
  Dijkgraaf-Witten counterterm entry in the gauging datum.
- `omega`, `Omega`, `S_omega`: Dijkgraaf-Witten class, cocycle representative,
  and topological action.
- `N_G`, `N_G^dagger`: gauging interface and reverse gauging interface.
- `D_g`: invertible symmetry defect with transverse holonomy \(g\).
- `A_G`: regular algebra defect \(\oplus_{g\in G}D_g\).
- `V_H`, `e_h`: finite Abelian holonomy state space and its holonomy basis in
  the gauging-coordinate comparison.
- `Pi_H`: normalized finite slab/orbit-sum projector `|H|^{-1} A_H`.
- `widehat H`, `widehat A_H`: character group and the dual regular algebra
  acting on holonomy sectors of the gauged side.
- `V_g`, `C_G(g)`: \(g\)-twisted local-operator space and centralizer.
- `Phi`, `D_H`: self-duality equivalence \(\mathcal Q/H\to\mathcal Q\) and
  induced noninvertible defect.
- `Gamma`, `< , >`: electric-magnetic line-charge lattice and integral Dirac
  pairing.
- `S`, `T`, `T^p`: line-lattice duality transformations.
- `C_N`, `B`: finite center-sensitive charge group and finite Dirac pairing.

## Claim Ledger

1. States the finite gauging and duality-defect datum upfront: QFT with
   finite symmetry, background-bundle groupoids, anomaly line and
   trivialization/counterterm data, topological symmetry defects, gauging
   interfaces, optional self-duality equivalence, and line-charge lattice
   action.
2. Defines finite background fields as principal \(G\)-bundles, equivalently
   flat cocycles modulo gauge transformations.
3. Defines finite gauging as a groupoid-cardinality sum with explicit
   \(1/|\operatorname{Aut}(P)|\) weighting.
4. Proves disjoint-union multiplicativity of the groupoid gauging convention.
5. Defines Dijkgraaf-Witten twists and distinguishes degree-\(D\) twists from
   degree-\(D+1\) anomaly cancellation/trivialization.
6. Constructs the gauging interface and derives the slab fusion relation by
   a finite groupoid-sum calculation,
   \(\mathcal N_G^\dagger\mathcal N_G\simeq\oplus_{g\in G}D_g\).
7. Defines the regular algebra defect \(A_G\) and proves
   \(A_G\otimes A_G\simeq |G|A_G\).
8. Adds a finite gauging mechanism map: background-field groupoid sum,
   gauging-interface slab fusion, local-operator holonomy sectors, and
   symmetry-TFT boundary condensation are four coordinates for the same finite
   operation once anomaly and normalization data are fixed.
9. For finite Abelian \(H\), proves that the normalized regular algebra is the
   orbit-sum projector, while the dual character regular algebra is the
   holonomy-sector projector on the gauged side.
10. Derives the two-dimensional orbifold local-operator decomposition
   \(\oplus_{[g]}\mathcal V_g^{C_G(g)}\).
11. Proves the pair-of-pants monodromy selection rule
   \(g_1g_2g_3^{-1}=e\).
12. Proves that anomaly-free self-dual \(H\)-gauging gives a noninvertible
   defect \(D_H\) with \(D_H^\dagger D_H=A_H\) and
   \(d(D_H)=\sqrt{|H|}\).
13. Works out the Ising \(H=\mathbb Z_2\) case as Kramers-Wannier fusion.
14. Proves that normal-subgroup gauging leaves residual quotient symmetry
    \(G/H\) under anomaly-compatible choices.
15. Gives the explicit \(A_3\triangleleft S_3\) finite test case.
16. Defines gauge-theory line-lattice duality walls as automorphisms
    preserving the Dirac pairing.
17. Proves pairing preservation for the \(S\) and \(T\) walls.
18. Works out the finite \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\)
    line-lattice action and relates \(T^p(0,1)=(p,1)\) to oblique
    confinement.

## Calculation Checks

- `calculation-checks/duality_defect_gauging_checks.py` verifies the finite
  group and lattice arithmetic used in the chapter: regular algebra
  multiplicities, the normalized regular-algebra/orbit-sum projector, the
  dual-character holonomy projector, normality of \(A_3\subset S_3\), quotient
  multiplication, orbifold monodromy and centralizers, and preservation of the
  finite Dirac pairing by \(S\), \(T\), and \(T^p\).

## Figure Ledger

No figure is included in this pass.  Future figures can illustrate the
gauging-interface slab, pair-of-pants monodromy, and line-lattice \(S,T\)
actions; the present chapter keeps the examples algebraic and proof-focused.

## Audit Notes

- 2026-05-26 depth pass: rewrote the chapter from a thin sketch into a
  theorem-led finite construction chapter, directly addressing the
  promised-example gap flagged for categorical symmetry and duality defects.
- 2026-05-29 anti-wrapper pass: demoted the gauging-interface slab fusion
  from proposition form to derivation prose, because the real inputs are the
  anomaly-trivialized gauging datum and compatible groupoid normalization.
- 2026-06-03 #698 architecture pass: added the finite gauging mechanism map
  tying the background-field groupoid sum, slab-fusion regular algebra,
  orbit-sum projector, dual-character projector, and symmetry-TFT boundary
  interpretation into one dependency chain; this leaves the continuum
  self-duality/interface construction as an explicit QFT input.
