# ABA Exchange-Sign And Proof-Substance Pass

Date: 2026-05-30

Related issues: #691, #694

## Scope

This pass continued the theorem-form and proof-substance audit in Volume VI,
Chapter 4A.  The initial target was the short RTT and transfer-matrix
commutativity proofs.  Those statements remain substantive finite-dimensional
integrability algebra, but reading the surrounding proof uncovered a more
important formula-level issue in the rational \(XXX_{1/2}\) convention.

## Changes

- Corrected the \(AB\) and \(DB\) exchange relations for the convention
  \(R(u)=u1+iP\), \(L(u)=R(u-i/2)\), and
  \(T=\begin{psmallmatrix}A&B\\ C&D\end{psmallmatrix}\):
  \[
    A(u)B(v)=\frac{u-v-i}{u-v}B(v)A(u)+\frac{i}{u-v}B(u)A(v),
  \]
  \[
    D(u)B(v)=\frac{u-v+i}{u-v}B(v)D(u)-\frac{i}{u-v}B(u)D(v).
  \]
- Expanded the text explaining how these signs are fixed by the one-site
  monodromy and by the component RTT relation.
- Expanded the algebraic Bethe ansatz proof by displaying the normal-ordered
  \(A\)- and \(D\)-actions on a Bethe vector, including the unwanted-term
  coefficient whose vanishing gives the Bethe equations.
- Added executable checks of the corrected \(AB/DB\) exchange signs to
  `calculation-checks/nested_bethe_ansatz_checks.py`.
- Updated the Volume VI, Chapter 4A dossier to record the convention-sensitive
  exchange relations and the new calculation-check coverage.

## Status

The RTT relation and transfer-matrix commutativity were not demoted in this
pass.  They are compact but load-bearing consequences of the Yang--Baxter
equation and finite-dimensional trace cyclicity.  The weak spot was instead
the downstream proof using exchange relations whose signs were inconsistent
with the displayed transfer eigenvalue and \(TQ\) numerator.
