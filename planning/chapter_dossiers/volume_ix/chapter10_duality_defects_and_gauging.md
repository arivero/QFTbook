# Chapter 10: Duality Defects, Gauging, And Orbifold Data

## Source Position

Volume IX develops finite gauging and duality defects immediately after the
categorical-symmetry chapter.  This chapter now supplies the finite examples
and derivations needed there: groupoid gauging, gauging-interface slab fusion,
orbifold twisted-sector data, self-dual gauging defects, normal-subgroup
gauging, and electric-magnetic line-lattice duality walls.

## Notation Inventory

- `G`, `H`: finite internal symmetry group and a finite subgroup to be gauged.
- `P -> M`: principal finite-group background bundle.
- `Bun_G(M)`: finite groupoid of \(G\)-bundles on \(M\).
- `Aut(P)`: automorphism group of the finite background bundle \(P\).
- `Z_Q[M;P]`: partition function of \(\mathcal Q\) in finite background \(P\).
- `omega`, `Omega`, `S_omega`: Dijkgraaf-Witten class, cocycle representative,
  and topological action.
- `alpha`: one-degree-higher anomaly class.
- `N_G`, `N_G^dagger`: gauging interface and reverse gauging interface.
- `D_g`: invertible symmetry defect with transverse holonomy \(g\).
- `A_G`: regular algebra defect \(\oplus_{g\in G}D_g\).
- `V_g`, `C_G(g)`: \(g\)-twisted local-operator space and centralizer.
- `Phi`, `D_H`: self-duality equivalence \(\mathcal Q/H\to\mathcal Q\) and
  induced noninvertible defect.
- `Gamma`, `< , >`: electric-magnetic line-charge lattice and integral Dirac
  pairing.
- `S`, `T`, `T^p`: line-lattice duality transformations.
- `C_N`, `B`: finite center-sensitive charge group and finite Dirac pairing.

## Claim Ledger

1. Defines finite background fields as principal \(G\)-bundles, equivalently
   flat cocycles modulo gauge transformations.
2. Defines finite gauging as a groupoid-cardinality sum with explicit
   \(1/|\operatorname{Aut}(P)|\) weighting.
3. Proves disjoint-union multiplicativity of the groupoid gauging convention.
4. Defines Dijkgraaf-Witten twists and distinguishes degree-\(D\) twists from
   degree-\(D+1\) anomaly cancellation/trivialization.
5. Constructs the gauging interface and proves the slab fusion relation
   \(\mathcal N_G^\dagger\mathcal N_G\simeq\oplus_{g\in G}D_g\).
6. Defines the regular algebra defect \(A_G\) and proves
   \(A_G\otimes A_G\simeq |G|A_G\).
7. Derives the two-dimensional orbifold local-operator decomposition
   \(\oplus_{[g]}\mathcal V_g^{C_G(g)}\).
8. Proves the pair-of-pants monodromy selection rule
   \(g_1g_2g_3^{-1}=e\).
9. Proves that anomaly-free self-dual \(H\)-gauging gives a noninvertible
   defect \(D_H\) with \(D_H^\dagger D_H=A_H\) and
   \(d(D_H)=\sqrt{|H|}\).
10. Works out the Ising \(H=\mathbb Z_2\) case as Kramers-Wannier fusion.
11. Proves that normal-subgroup gauging leaves residual quotient symmetry
    \(G/H\) under anomaly-compatible choices.
12. Gives the explicit \(A_3\triangleleft S_3\) finite test case.
13. Defines gauge-theory line-lattice duality walls as automorphisms
    preserving the Dirac pairing.
14. Proves pairing preservation for the \(S\) and \(T\) walls.
15. Works out the finite \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\)
    line-lattice action and relates \(T^p(0,1)=(p,1)\) to oblique
    confinement.

## Calculation Checks

- `calculation-checks/duality_defect_gauging_checks.py` verifies the finite
  group and lattice arithmetic used in the chapter: regular algebra
  multiplicities, normality of \(A_3\subset S_3\), quotient multiplication,
  orbifold monodromy and centralizers, and preservation of the finite Dirac
  pairing by \(S\), \(T\), and \(T^p\).

## Figure Ledger

No figure is included in this pass.  Future figures can illustrate the
gauging-interface slab, pair-of-pants monodromy, and line-lattice \(S,T\)
actions; the present chapter keeps the examples algebraic and proof-focused.

## Audit Notes

- 2026-05-26 depth pass: rewrote the chapter from a thin sketch into a
  theorem-led finite construction chapter, directly addressing the
  promised-example gap flagged for categorical symmetry and duality defects.
