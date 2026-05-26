# Volume IX, Chapter 3 Dossier: Line, Surface, And Domain-Wall Operators

## Logical Role

- Role in the monograph: define principal classes of extended operators after
  topological defects.
- Immediate predecessor: extended operators and topological defects.
- Immediate successor: confinement, screening, oblique confinement, and
  anomaly inflow.

## Definitions And Results

- Defect datum supported on a submanifold \(Y\subset X\).
- Wilson lines as renormalized gauge-invariant line operators.
- Endpoint bookkeeping for Wilson intervals and gauge covariance of
  holonomy.
- Magnetic and dyonic line labels by cocharacters and stabilizer
  representations.
- Local Dirac monopole patch construction on linking two-spheres and the
  cocharacter criterion for a well-defined singular connection.
- Renormalized 't Hooft lines as tubular-neighborhood boundary conditions with
  fixed cocharacter flux, boundary-preserving gauge transformations, and
  regulator-dependent line counterterms.
- Dyonic Wilson--'t Hooft lines as a magnetic singularity plus a
  representation of \(G_m=Z_G(m(U(1)))\).
- Linking phase and mutual-locality condition
  \(\lambda(m')-\lambda'(m)\in\mathbb Z\).
- Screening by adjoint particles and smooth monopole cores, giving finite
  charges in
  \((\Lambda_{\rm wt}/\Lambda_{\rm rt})\oplus
  (\Lambda_{\rm cwt}/\Lambda_{\rm crt})\).
- Theta-angle Witten-effect automorphism and preservation of the Dirac
  pairing.
- Dependence of line spectra on gauge-group global form.
- Surface operators by singularity or defect degrees of freedom, with
  Cartan singularity parameter
  \(\alpha\in\mathfrak t/X_*(T)\) modulo Weyl equivalence and optional
  two-dimensional theta parameter \(\eta\).
- Domain walls and interfaces as codimension-one defects.
- Fusion of topological defects as a renormalized short-distance limit.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(X\) | spacetime manifold |
| \(Y\) | support submanifold of a defect |
| \(\gamma\) | curve supporting a line operator |
| \(R\) | electric representation label |
| \(m:U(1)\to G\) | magnetic cocharacter label |
| \(T,W\) | maximal torus and Weyl group of a compact connected gauge group |
| \(m_*\) | differential of the magnetic cocharacter in \(\mathfrak t\) |
| \(A_N,A_S\) | northern and southern embedded Dirac-monopole gauge potentials |
| \(g_{NS}\) | transition function \(m(e^{i\varphi})\) on the equatorial overlap |
| \(N_\epsilon(\gamma)\) | tubular neighborhood removed to define a regulated magnetic line |
| \(S^2_p\) | small linking sphere around a point \(p\in\gamma\) |
| \(\mathcal A_m,\mathcal G_m\) | regulated connections with magnetic boundary condition and boundary-preserving gauge transformations |
| \(H_m(\gamma)\) | renormalized 't Hooft line of magnetic charge \(m\) |
| \(G_m\) | centralizer \(Z_G(m(U(1)))\) of the magnetic singularity |
| \(\lambda,m\) | abelianized electric and magnetic line charges |
| \(I:X_*(T)\to X^*(T)\) | integral symmetric map induced by the theta-term quadratic form |
| \(\Sigma\) | surface supporting a surface operator |
| \(\alpha,\eta\) | Cartan surface holonomy parameter and two-dimensional theta parameter |
| \(D_1\otimes D_2\) | fusion of topological defects |

## Claim Ledger

1. Extended operators require extra defect data beyond local operator
   correlation functions.
2. Wilson lines require global-form, endpoint, framing, and renormalization
   data.
3. Magnetic line labels are cocharacters modulo conjugation/Weyl equivalence;
   the local Dirac monopole patching on a linking sphere exists exactly for
   \(m\in X_*(T)\).
4. A renormalized 't Hooft line is not just a formal singular field: it is a
   regulated path-integral boundary condition on \(X\setminus
   N_\epsilon(\gamma)\), followed by a line-counterterm-renormalized
   \(\epsilon\to0\) limit in a specified regulator or constructive framework.
5. Dyonic lines are labelled by the magnetic cocharacter plus a
   representation of the centralizer \(G_m\); the finite center-sensitive
   charge is the abelianized quotient only after screening.
6. The mutual-locality phase of two abelianized dyonic labels is
   \(\exp(2\pi i(\lambda(m')-\lambda'(m)))\).
7. The Witten-effect automorphism adds \(I(m)\) to the electric label and
   preserves the Dirac pairing by symmetry of \(I\).
8. In compact \(U(1)\), the minimal 't Hooft line has unit magnetic flux
   through each small linking sphere, and dynamical monopoles are endpoints for
   such lines, breaking the magnetic one-form symmetry.
9. Cartan surface singularities are equivalent under Weyl transformations and
   cocharacter shifts of the normal-circle holonomy parameter.
10. Fusion is a construction only after a topology and counterterm prescription
   for the defect collision limit are supplied.

## Calculation Checks

- `calculation-checks/thooft_line_local_model_checks.py` verifies the
  Dirac-monopole patch difference, flux normalization, integer Dirac phase,
  finite linking-pairing bilinearity, Witten-effect preservation of the
  pairing, and Cartan surface-parameter cocharacter shifts.

## Figures

- Codimension ladder for local, line, surface, and wall defects.
- Electric/magnetic line linking diagram.
- Fusion limit of two parallel topological defects.
