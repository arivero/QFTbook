# Volume III, Chapter 3 Dossier: Stress Tensor, Weyl Structure, And Improvement

## Logical Role

- Role in the monograph: connect the fixed-point source functional to the
  stress tensor, trace equation, Weyl response, and improvement ambiguities.
- Immediate predecessor: conformal Killing vectors and global conformal maps.
- Immediate successor: radial quantization and the state--operator map.

## Definitions And Results

The chapter establishes:

- stress-tensor insertions as background-metric derivatives of
  \(W_\ast[g,\eta]\);
- local diffeomorphism and Weyl Ward identities as distributional identities
  with contact terms;
- the spinful stress-tensor Ward identity without an ellipsis: scalar
  insertions are the \(\mathsf R^{\mu\nu}=0\) special case, while spinning
  primaries produce the local rotation contact term
  \(-\frac i2\omega_\epsilon^{\mu\nu}S_{\mu\nu}\) in the conformal-current
  Ward identity;
- improvement transformations of \(T_{\mu\nu}\) and their effect on the trace;
- the assumptions under which scale invariance plus a removable virial current
  yields conformal current conservation;
- the difference between separated-point stress-tensor correlators and their
  contact-term extensions;
- the infrared proviso that, in massless theories, stress-tensor contact-term
  extensions presuppose an infrared state or regulator that has already made
  the separated-point correlators meaningful on the relevant test functions;
- the convention relating flat-space \(T_{\mu\nu}\) to curved-background
  derivatives.
- the trace-anomaly density \(\mathcal A[g]\), its sign convention relative to
  the metric-source stress tensor, and the fact that functional derivatives of
  \(\mathcal A[g]\) give contact terms in traced stress-tensor Ward identities;
- the Wess--Zumino consistency condition for Weyl anomalies and the
  parity-even local cohomological classification into type-A Euler-density
  terms, type-B Weyl-invariant densities, and type-D counterterm variations;
- the two-dimensional normalization
  \(\mathcal A_2[g]=-c_{2d}R/(24\pi)\), tied to
  \(\langle T(z)T(0)\rangle=c_{2d}/(2z^4)\);
- the four-dimensional anomaly coefficients \(a_{\rm W},c_{\rm W},b_{\rm D}\)
  in
  \(\mathcal A_4=(16\pi^2)^{-1}(c_{\rm W}W^2-a_{\rm W}E_4+
  b_{\rm D}\nabla^2R)\), with \(b_{\rm D}\) identified as scheme-dependent
  and \(a_{\rm W},c_{\rm W}\) as fixed-point data;
- the six-dimensional parity-even bulk classification
  \(\mathcal A_6=(4\pi)^{-3}(-a_6E_6+c_1I_1+c_2I_2+c_3I_3+
  \nabla_\mu J^\mu)\), where \(I_1,I_2\) are the independent cubic Weyl
  contractions and \(I_3\) is the two-Weyl-tensor/two-derivative class modulo
  type-D terms;
- the relation \(C_T=40c_{\rm W}/\pi^4\) in the chapter's stress-tensor
  two-point normalization;
- the link between the three separated four-dimensional \(TTT\) structures of
  Chapter 8 and the Weyl-anomaly coefficients: \(c_{\rm W}\) is the
  Ward-fixed \(C_T\) combination, \(a_{\rm W}\) is a second independent
  anomaly functional extracted from the traced three-point Ward identity, and
  a third combination remains separated \(TTT\) data.

## Claims To Verify

1. The stress tensor is source-defined; a Noether expression is a coordinate
   representative after a source chart has been chosen.
2. The trace equation at a fixed point is a local operator identity only after
   equation-of-motion, total-derivative, and contact-term conventions are
   fixed.
3. Improvement is a change of stress-tensor representative preserving
   translation and rotation charges under stated boundary conditions.
4. Weyl anomalies are local curvature terms in even dimension and do not
   change separated-point flat-space primary transformation laws.
5. Scaling-degree/contact-term arguments classify ultraviolet ambiguities at
   coincident stress insertions; they do not replace the infrared construction
   of the massless source functional.
6. The symbols \(a,b,c\) used for the Osborn--Petkou separated \(TTT\)
   structures must be distinguished from the Weyl-anomaly coefficients
   \(a_{\rm W},c_{\rm W}\); the chapter uses temporary notation
   \(a_{\rm OP},b_{\rm OP},c_{\rm OP}\) at the point where both appear.
7. The four-dimensional free-field stress-tensor structures form a convenient
   basis for parity-even \(TTT\) data; the anomaly map in that basis uses
   Dirac-fermion normalization, so a Weyl fermion contributes one half of the
   fermion entry.
8. The type-A/type-B/type-D classification is local to the parity-even bulk
   metric sector on closed manifolds; boundary, defect, global, and
   parity-odd orientation-dependent anomalies require separate data.

## Figures

- Use figures only for source-variation or improvement maps that would
  otherwise require several paragraphs of bookkeeping.

## Checks

- The chapter should not use conformal current conservation as an input before
  deriving the current from the source Ward identities.
- All claims about removable virial currents require stated assumptions.
- 2026-05-24 issue #279 pass: added the trace-anomaly central-charge section,
  including the \(2D\) \(c_{2d}\) normalization, the \(4D\)
  \(a_{\rm W},c_{\rm W}\) definitions, the \(C_T\)-\(c_{\rm W}\) relation, and
  the connection to the Chapter 8 \(TTT\) structures.
- 2026-05-24 issue #423 pass: tied the derivative contact term in the local
  stress-tensor Ward identity to the Chapter 6 primary spin contact operator,
  making clear that the scalar Ward identity is only the spinless special case.
- 2026-05-29 anti-wrapper audit: demoted the background-diffeomorphism Ward
  identity from proposition form to source-Noether prose, preserving the
  conservation equation while making explicit that coincident insertions carry
  contact terms depending on operator transformations and contact extensions.
- 2026-05-25 issue #473 pass: split the anomaly-density/contact-Ward material
  from the conformal-anomaly classification, added the Wess--Zumino consistency
  condition, type-A/type-B/type-D definitions, and explicit \(D=2,4,6\)
  parity-even bulk lists, with a calculation check for the finite
  dimension-counting and \(R^2\)-counterterm arithmetic.
