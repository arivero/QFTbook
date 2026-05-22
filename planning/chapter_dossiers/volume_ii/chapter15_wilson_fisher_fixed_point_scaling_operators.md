# Volume II, Chapter 15 Dossier: Wilson-Fisher Fixed Point And Scaling Operators

## Source Position

- Primary local source: second-sequence handwritten material, pages 124--135.
- Immediate predecessor: the stress-tensor trace identity and conformal
  currents at fixed points.
- Immediate successor in the source order: the statistical Ising model.
- Role in the monograph: give the first perturbatively controlled non-Gaussian
  fixed point, then compute the first operator dimensions from the same
  renormalized-operator logic developed in the preceding chapters.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 124--135;
  checked against rendered page images in
  `monograph/tex/build/source_visual_trace/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`, the
  Wilson-Fisher/scaling-operator section, used only as a comparison layer.
- `SRC-EXTERNAL`: standard Wilson-Fisher and scaling-operator facts, with
  Rosten's exact RG review kept in mind for fixed-point and scaling-operator
  terminology.  The construction in the chapter remains tied to the local
  source order and to 1PI/MS coordinates already introduced.

## Construction Task

The chapter must define and derive:

- scalar quartic theory in \(D=4-\epsilon\) dimensions with
  \(\mathcal L_E=\frac12(\partial\phi)^2+\frac12m_0^2\phi^2
  +\frac1{4!}g_0\phi^4\);
- the tuning of \(m_0^2\) as the condition for a massless infrared limit;
- the restriction to the \(\mathbb Z_2\)-even RG chart when odd sources are
  not introduced;
- the dimensionless 1PI quartic coupling
  \(\lambda(\mu)=-\mu^{-\epsilon}Z(\mu)^2\Gamma^{(4)}\) at the symmetric
  Euclidean subtraction point;
- the one-loop formula for \(\lambda(\mu)\) in terms of \(g_0\);
- the beta function
  \(\beta(\lambda)=-\epsilon\lambda+
  (3/(16\pi^2)+O(\epsilon))\lambda^2+O(\lambda^3)\);
- the fixed point
  \(\lambda_*=16\pi^2\epsilon/3+O(\epsilon^2)\) and its IR attractiveness
  for decreasing \(\mu\) along the massless critical surface;
- the distinction between the dimensionless bare coordinate
  \(\mu^{-\epsilon}g_0\) and the finite renormalized 1PI coordinate
  \(\lambda(\mu)\);
- the field dimension
  \(\Delta_\phi=1-\epsilon/2+O(\epsilon^2)\);
- why an \(x\)-independent \(\phi^2\) source is an IR-bad subtraction in the
  massless theory;
- the momentum-dependent source definition for \(\phi^2\);
- the one-loop anomalous dimension
  \(\gamma_{2*}=\epsilon/3+O(\epsilon^2)\) and
  \(\Delta_{\phi^2}=2-2\epsilon/3+O(\epsilon^2)\);
- the mass perturbation as the relevant direction dual to \([O_2]\);
- the thermal eigenvalue
  \(y_t=D-\Delta_{\phi^2}=2-\epsilon/3+O(\epsilon^2)\);
- the dimensionless mass/temperature coordinate
  \(\tau(\mu)=\mu^{-y_t}t\), its linearized flow
  \(\dd\tau/\dd\log\mu=-y_t\tau+\cdots\), and the critical surface
  \(\tau=0\);
- the correlation-length exponent
  \(\nu=1/y_t=1/2+\epsilon/12+O(\epsilon^2)\);
- the odd source \(h[\phi]\) and its eigenvalue
  \(y_h=D-\Delta_\phi=3-\epsilon/2+O(\epsilon^2)\), explaining that the
  codimension-one critical surface is a statement inside the
  \(\mathbb Z_2\)-even subspace;
- the scaling of two-point functions in momentum and position space;
- the point-splitting interpretation of the properly renormalized
  \(\phi^2\) operator;
- the equation-of-motion relation
  \(\phi^3\propto \Box\phi\) and the descendant dimension
  \(\Delta_{\phi^3}=\Delta_\phi+2\);
- the quartic operator anomalous dimension
  \(\gamma_{4*}=\beta'(\lambda_*)=\epsilon+O(\epsilon^2)\) and
  \(\Delta_{\phi^4}=4+O(\epsilon^2)>D\);
- the comparison table for \(d=4-\epsilon\), \(d=3\), and \(d=2\), with the
  last two rows explicitly not presented as consequences of the first-order
  epsilon expansion.

## Claim Ledger

1. In \(4-\epsilon\) dimensions the classical relevance of \(g_0\) and the
   one-loop screening term can balance.
2. The nonzero fixed point is perturbatively accessible for small positive
   \(\epsilon\).
3. The fixed point is attractive in the infrared along the quartic direction.
4. The mass parameter must be tuned separately; inside the
   \(\mathbb Z_2\)-even subspace the fixed point is reached on the massless
   critical surface.
5. Operator dimensions at the fixed point come from the same renormalized
   operator construction as before.
6. The \(\phi^2\) source must carry momentum to avoid an infrared-singular
   subtraction.
7. Without the \(\mathbb Z_2\) restriction, the odd source for \(\phi\) is
   also relevant.
8. The mass/temperature perturbation has eigenvalue
   \(y_t=D-\Delta_{\phi^2}\), hence
   \(\nu=1/y_t\) in the perturbative calculation.
9. Properly renormalized composite operators are finite local fields;
   unregulated products of distributions at coincident points are not
   definitions.
10. \(\phi^3\) is an equation-of-motion descendant of \(\phi\) at the fixed
   point.
11. \(\phi^4\) is irrelevant at the interacting fixed point even though it is
   needed to reach that fixed point.

## Figure Requirements

- Symmetric 1PI definition of the quartic coupling and the one-dimensional
  Wilson-Fisher flow.
- Comparison of the dimensionless bare coupling and the finite
  renormalized coupling at the fixed point.
- \(\phi^2\) operator renormalization figure: bad zero-momentum insertion,
  good momentum-carrying source, and one-loop graph.
- Critical surface figure in the \(\mathbb Z_2\)-even slice showing the
  relevant mass direction and the \(\tau=0\) trajectory into the
  Wilson-Fisher fixed point.
- Momentum-to-position scaling figure for \(\phi^2\) correlators.
- Operator-spectrum figure for \(\phi^3\) as descendant and \(\phi^4\) as
  irrelevant.

## Audit Notes

- Do not say that the epsilon expansion proves the \(d=3\) or \(d=2\) fixed
  points.
- Do not present composite operators as unregulated products of fields.
- Do not describe the Wilson-Fisher fixed point as an attractor for arbitrary
  massive scalar theories; the mass direction must be tuned away.
- When saying the critical surface has codimension one, state the
  \(\mathbb Z_2\)-even restriction; the odd field source is relevant in the
  full local chart.
- Keep the Ising model itself for the next chapter.
- No reader-facing source-page references or course-note references.
