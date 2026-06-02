# Volume IX, Chapter 1 Dossier: Global Forms And Higher-Form Symmetry

## Logical Role

- Role in the monograph: launch the global-structure volume with gauge-group
  global form, character/cocharacter lattices, finite Wilson--'t Hooft line
  spectra, and higher-form symmetry.
- Immediate predecessor: nonabelian gauge theory, lattice gauge theory,
  anomalies, and confinement material.
- Immediate successor: extended operators, phase structure, and anomaly
  inflow.

## Definitions And Results

- Character and cocharacter lattices
  \(X^*(T)=\operatorname{Hom}(T,U(1))\) and
  \(X_*(T)=\operatorname{Hom}(U(1),T)\), with weight, root, coweight, and
  coroot specializations for \(G_{\rm sc}\).
- Global form \(G_{\rm sc}/\Gamma\) of a compact gauge group and the induced
  character/cocharacter lattices of \(T_G=T_{\rm sc}/\Gamma\).
- Descent criterion for Wilson charges: an irreducible \(G_{\rm sc}\)
  representation descends to \(G_{\rm sc}/\Gamma\) exactly when its central
  character is trivial on \(\Gamma\).
- \(SU(N)/\mathbb Z_k\) descent: Wilson \(N\)-alities are multiples of \(k\);
  magnetic cocharacter classes are multiples of \(N/k\).
- Genuine line operators and the finite Dirac pairing on center-sensitive
  Wilson--'t Hooft charges.
- Maximal isotropic finite line lattices
  \(L_{N,k,p}=\langle(k,0),(p,N/k)\rangle\subset
  \mathbb Z_N\oplus\mathbb Z_N\).
- Abelian group-like \(p\)-form symmetry as an action of codimension-\(p+1\)
  topological operators on \(p\)-dimensional charged operators.
- Chain-level mechanism for the higher-form linking phase:
  \(\operatorname{Link}(M,\Sigma)=B\cdot\Sigma\) when
  \(\partial B=M\), deformation invariance away from \(\Sigma\), and the
  single-crossing multiplication by the charged character.
- Electric one-form symmetry \(Z(G)\) and magnetic one-form symmetry
  \(\pi_1(G)^\vee\) of pure gauge theory.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(G_{\rm sc}\) | simply connected compact gauge group with a fixed Lie algebra |
| \(\Gamma\) | subgroup of the center divided out to form the gauge group |
| \(T_{\rm sc},T_G\) | maximal tori of \(G_{\rm sc}\) and \(G=G_{\rm sc}/\Gamma\) |
| \(X^*(T),X_*(T)\) | character and cocharacter lattices of a torus |
| \(\Lambda_{\rm wt},\Lambda_{\rm rt}\) | weight and root lattices |
| \(\Lambda_{\rm cwt},\Lambda_{\rm crt}\) | coweight and coroot lattices |
| \(\lambda,m\) | electric weight and magnetic cocharacter |
| \(B(\gamma,\gamma')\) | electric-magnetic Dirac pairing |
| \(L_{N,k,p}\) | finite line lattice for \(SU(N)/\mathbb Z_k\) with discrete theta \(p\) |
| \(W_R(C)\) | Wilson line in representation \(R\) along curve \(C\) |
| \(U_\alpha(\Sigma)\) | higher-form symmetry operator on \(\Sigma\) |
| \(L(C,\Sigma)\) | integer linking number |
| \(Z(G)\) | center of \(G\) |
| \(\pi_1(G)^\vee\) | Pontryagin-dual group of magnetic one-form symmetry defects |

## Claim Ledger

1. The Lie algebra does not determine the line-operator spectrum.
2. Wilson charges descend through \(G_{\rm sc}\to G_{\rm sc}/\Gamma\) exactly
   when their central character is trivial on \(\Gamma\).
3. For \(SU(N)/\mathbb Z_k\), allowed Wilson \(N\)-alities are \(k\mathbb Z_N\)
   and allowed finite magnetic cocharacter classes are \((N/k)\mathbb Z_N\).
4. The finite \(\mathfrak{su}(N)\) Dirac pairing is
   \((em'-e'm)/N\) modulo \(\mathbb Z\).
5. \(L_{N,k,p}=\langle(k,0),(p,N/k)\rangle\) is maximal isotropic; the proof
   explicitly computes its orthogonal complement.
6. Genuine line operators are classified only after the global form, discrete
   theta coordinate, and allowed attached surfaces are fixed.
7. Higher-form symmetry acts by a linking phase on charged extended
   operators; the phase is derived from oriented chain intersection and the
   local crossing rule, while existence of the topological defect remains
   part of the theory data.
8. Center symmetry and magnetic one-form symmetry give precise operator
   formulations of confinement and screening diagnostics in pure Yang--Mills.

## Figures

- Wilson and 't Hooft finite line-charge lattice for the
  \(\mathfrak{su}(5)\) example.
- Future: weight-lattice/global-form quotient diagram.
- Future: line operator linked by a codimension-two symmetry defect.

## Calculation Checks

- `calculation-checks/global_form_line_lattice_checks.py` verifies the
  finite \(\mathbb Z_N^{\mathrm e}\oplus\mathbb Z_N^{\mathrm m}\) Dirac
  pairing, \(SU(N)/\mathbb Z_k\) descent arithmetic, and maximal isotropy of
  \(L_{N,k,p}\) for \(2\leq N\leq 9\).  It also verifies the finite
  \(\mathbb Z_N\) higher-form linking phase bookkeeping under deformation
  away from the charged operator, a single crossing, orientation reversal,
  defect fusion, and charge fusion.

## Audit Notes

- 2026-06-02 higher-form linking pass: expanded the linking action from a
  bare defining formula into a chain-intersection mechanism.  The text now
  shows that \(\operatorname{Link}(M,\Sigma)=B\cdot\Sigma\) is invariant when
  the defect sweep stays away from \(\Sigma\), changes by one when the sweep
  crosses \(\Sigma\) once, and therefore gives the displayed character phase
  by iterating the local crossing rule.
