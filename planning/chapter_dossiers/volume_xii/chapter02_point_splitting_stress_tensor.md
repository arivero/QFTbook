# Volume XII, Chapter 2 Dossier: Point Splitting And Stress Tensor Renormalization
Source-File: monograph/tex/volumes/volume_xii/chapter02_point_splitting_stress_tensor.tex

## Logical Role

- Role in the monograph: develop composite fields and stress tensors from
  Hadamard short-distance structure.
- Printed predecessor: perturbative algebraic QFT on curved backgrounds.
- Logical inputs: microlocal spectrum condition and locally covariant
  Hadamard states.
- Printed successor: trace anomalies and background variations.

## Definitions And Results

- Hadamard parametrix \(H(x,y)\).
- Local Hadamard subtraction datum \(H_{\epsilon,\mu}\) with
  \(\sigma_\epsilon\), \(U_H=\Delta^{1/2}\), \(V_H\), and scale \(\mu\).
- Proposition: the leading \(U_H\) coefficient satisfies
  \(2\sigma^{;\mu}\nabla_\mu U_H+(\Box\sigma-4)U_H=0\), and the remaining
  singular coefficients are removed recursively by \(V_H\).
- Wick square by point-splitting subtraction.
- Proposition: the difference of two Hadamard-state Wick-square expectation
  values is the diagonal of the smooth two-point-function difference, and a
  smooth change \(H\mapsto H+S\) shifts the Wick square by
  \(-S(x,x)\mathbf 1\).
- Finite local freedom of Wick square in four dimensions.
- Definition: point-split stress-tensor prescription with local covariance,
  state-dependence, conservation, weak regularity, smooth parameter
  dependence, almost-homogeneous scaling, and flat-vacuum normalization
  conditions.
- Construction: explicit scalar bidifferential operator with parallel
  transport, symmetrization, and the four-dimensional equation-of-motion
  improvement \(\eta_4=1/3\), with the coefficient and conservation
  identity imported from Moretti's improved point-splitting theorem.
- Quoted structural theorem: in four dimensions the finite scalar
  stress-tensor freedom, after the Hollands--Wald finite-renormalization
  theorem has reduced local covariance/weak regularity/almost-homogeneous
  scaling to a finite natural polynomial, is
  \(a_0m^4g_{\mu\nu}+a_1m^2G_{\mu\nu}+a_2I_{\mu\nu}+a_3J_{\mu\nu}\), with
  \(I,J\) defined by metric variation of \(R^2\) and \(R_{\mu\nu}R^{\mu\nu}\).
- Explicit flat-space computation: vacuum subtraction, thermal KMS remainder,
  point-split \(T_{00}\) and \(T_{ij}\), Stefan-Boltzmann energy density,
  and traceless equation of state.
- Constant-curvature de Sitter diagnostic for the massless conformally
  coupled scalar using the four-dimensional trace-anomaly coefficients, with
  no shift from \(I_{\mu\nu}\) or \(J_{\mu\nu}\) on constant curvature.
- Conservation Ward identity.
- Trace identity
  \(T^\mu{}_\mu=-m^2\phi^2+(D-1)(\xi-\xi_c)\Box\phi^2\) plus local
  anomaly/contact terms after renormalization.
- Comparison between point splitting and flat-space operator renormalization
  schemes.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\omega\) | Hadamard state |
| \(\omega_2\) | two-point distribution |
| \(H(x,y)\) | locally covariant Hadamard parametrix |
| \(\sigma,\sigma_\epsilon\) | Synge world function and distributional \(i\epsilon\) prescription |
| \(U_H,V_H,\mu\) | Hadamard coefficients and subtraction scale |
| \(S(x,y)\) | smooth biscalar changing the subtraction prescription |
| \(:\!\Phi^2\!:\) | Wick square defined by point splitting |
| \(\mathcal D_{\mu\nu}(x,y)\) | stress-tensor bidifferential operator |
| \(C_{\mu\nu}\) | finite local curvature tensor freedom |
| \(G_{\mu\nu},I_{\mu\nu},J_{\mu\nu}\) | Einstein tensor and independent curvature-variation tensors in the finite stress-tensor freedom |
| \(\mathcal A[g,m,\xi]\) | local trace anomaly term |
| \(\Delta W_\beta\) | smooth thermal two-point remainder \(W_\beta-W_0\) |
| \(\rho_\beta,p_\beta\) | thermal energy density and pressure |
| \(E_4\) | four-dimensional Euler density |

## Claim Ledger

1. The leading \(U_H/\sigma_\epsilon\) singularity is fixed by the Synge
   transport equation; the \(V_H\log\sigma_\epsilon\) coefficient is fixed
   recursively by cancellation of the remaining singular part of \(P_MH\).
2. Wick powers are defined by subtracting the locally covariant singular
   parametrix in all contractions.
3. State differences cancel the common Hadamard singularity, while changing
   the smooth part of the subtraction shifts the composite field by a
   state-independent local identity term.
4. Stress-tensor prescriptions must state local covariance, state-dependence,
   conservation, weak regularity, almost-homogeneous scaling, and
   normalization conditions.
5. Under those conditions, the Hollands--Wald finite-renormalization theorem
   implies that scalar stress-tensor differences are finite natural
   polynomials; in four dimensions the allowed conserved generators are
   \(m^4g_{\mu\nu}\), \(m^2G_{\mu\nu}\), \(I_{\mu\nu}\), and
   \(J_{\mu\nu}\).  Dimension counting alone would not exclude nonpolynomial
   local functionals and is not the classification proof.
6. In flat Minkowski space \(H_0=W_0\), so the point-split vacuum stress
   tensor vanishes once the finite cosmological term is set to zero.
7. Applying the point-split stress operator to the smooth thermal remainder
   gives \(\rho_\beta=\pi^2/(30\beta^4)\) and \(p_\beta=\rho_\beta/3\).
8. For the massless conformally coupled scalar on de Sitter, maximal
   symmetry and the \(a=1/360\) trace anomaly fix the local curvature
   contribution \(C=-H^4/(960\pi^2)\) in
   \(\langle T_{\mu\nu}\rangle=Cg_{\mu\nu}\), subject to the stated finite
   local-term convention; the classified \(I,J\) tensors vanish on
   four-dimensional constant curvature.
9. Conservation is obtained by importing Moretti's Hadamard-coefficient
   coincidence-limit theorem: the local parametrix defect reduces to one
   covector and the \(\eta_D=D/[2(D+2)]\) equation-of-motion improvement
   cancels it.  The chapter's local calculation is the convention
   translation and downstream algebra, not a derivation of the analytic
   coefficient identities.
10. The scalar trace has mass coefficient \(-m^2\) and improvement
   coefficient \((D-1)(\xi-\xi_c)\); the trace anomaly is the remaining local
   term in the massless conformally coupled case.
11. Point splitting is an operator-definition scheme comparable to path-
   integral insertion schemes by finite local terms.

## Calculation Checks

- `calculation-checks/point_splitting_stress_checks.py` verifies the flat
  Synge identities and leading Hadamard \(U\)-transport equation, the
  point-splitting subtraction algebra, the Bose integral, the thermal
  massless stress-tensor computation, the downstream equation-of-motion
  conservation regression after the imported Moretti theorem boundary, text
  contracts for the quoted Moretti/Hollands--Wald status, the regularity
  filter in the finite-local-freedom theorem, the
  constant-curvature vanishing of \(I_{\mu\nu},J_{\mu\nu}\), scalar trace
  convention regressions, and the de Sitter anomaly specialization.

## Figures

- Point-splitting pair of nearby points in a normal neighborhood.
- Bidifferential operator followed by diagonal limit.
- Curvature-counterterm freedom diagram.

## Audit Notes

- 2026-06-08 issue #729 printed-order pass: rewrote the opening dependency
  sentence so point splitting names its upstream microlocal inputs explicitly:
  the Hadamard wavefront condition, local parametrix recursion, and product
  criterion.  The chapter's status remains finite local composite-field and
  stress-tensor renormalization, not a full interacting stress-tensor theorem.
- 2026-06-08 issues #903/#904 pass: replaced the placeholder stress-tensor
  operator with the explicit parallel-transported bidifferential operator,
  added the \(\eta_4=1/3\) parametrix-defect conservation repair, strengthened
  the finite-local-freedom hypotheses, corrected the scalar trace identity,
  and fixed the massless constant-curvature scheme statement.
- 2026-06-08 issue #932 pass: relabeled the conservation coefficient and
  finite-local-freedom classification as quoted structural theorems rather
  than locally proved lemmas.  Moretti supplies the Hadamard-coefficient
  coincidence-limit identity fixing \(\eta_D=D/[2(D+2)]\); Hollands--Wald
  supplies the Peetre--Slovak-type finite natural-polynomial reduction.
  The monograph text now confines itself to convention translation,
  four-dimensional basis enumeration, and downstream stress-tensor
  consequences.
