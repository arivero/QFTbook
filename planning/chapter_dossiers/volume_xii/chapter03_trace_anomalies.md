# Volume XII, Chapter 3 Dossier: Trace Anomalies And Background Variations
Source-File: monograph/tex/volumes/volume_xii/chapter03_trace_anomalies.tex

## Logical Role

- Role in the monograph: define and derive trace anomalies as local
  curved-background Weyl variations of the renormalized metric-source
  functional.
- Immediate predecessor: point splitting and stress-tensor renormalization.
- Immediate successor: Unruh/Hawking, cosmological particle creation, and
  semiclassical backreaction, which use the same locally covariant
  stress-source discipline.  The index-theoretic anomaly lane follows later as
  a separate background-gauge-field block.

## Definitions And Results

- Renormalized Euclidean effective action `W[g,lambda] = -log Z`.
- Stress-tensor convention
  `delta W = -1/2 int sqrt(g) <T^{mu nu}> delta g_{mu nu}`.
- Weyl variation and trace-anomaly density.
- Wess-Zumino consistency as commutativity of local Weyl variations.
- Counterterm shifts as Weyl coboundaries in local Weyl cohomology.
- Weyl variations of `sqrt(g)`, `R`, and the `R^2` counterterm.
- Two-dimensional trace anomaly and Wess-Zumino action.
- Four-dimensional `a,c,b` anomaly structure with explicit
  `E_4`, `W^2`, and `nabla^2 R` representatives.
- Heat-kernel derivation for the conformal scalar, explicit Dirac
  spin-bundle trace, Weyl local half-coefficient qualification, and Maxwell
  one-form/ghost subtraction.
- Free-field table for scalar, Weyl fermion, Dirac fermion, and Maxwell
  vector `a,c` coefficients.
- `N=4` Yang-Mills check: `a=c=dim(G)/4`.
- Trace anomalies as both separated stress-tensor CFT data and contact terms
  in curved-source Ward identities; `a` enters separated `TTT` and trace
  contacts.
- Nonperturbative open problem for trace anomalies from curved-background
  locally covariant QFT data.

## Symbols

| Symbol | Meaning |
| --- | --- |
| `M` | closed smooth background manifold |
| `g` | Riemannian metric |
| `lambda` | additional background sources |
| `W[g,lambda]` | renormalized Euclidean effective action |
| `T_{mu nu}` | stress tensor |
| `sigma` | local Weyl parameter |
| `A[g,lambda]` | trace-anomaly density |
| `A_sigma` | integrated local Weyl-anomaly functional |
| `E_4` | four-dimensional Euler density |
| `W^2` | squared Weyl tensor |
| `a,c,b` | four-dimensional trace-anomaly coefficients |
| `P` | Laplace-type operator |
| `mathcal E` | endomorphism in `P=-(nabla^2+mathcal E)` |
| `Omega_{mu nu}` | bundle curvature of the heat-kernel connection |
| `P_D`, `P_1`, `P_0` | squared Dirac, one-form Hodge, and scalar ghost operators |

## Claim Ledger

1. The trace is the response of the renormalized effective action to local
   Weyl rescaling, with sign fixed by the metric-source convention.
2. Locality plus commutativity of Weyl transformations gives the
   Wess-Zumino consistency condition.
3. Finite local counterterms shift the anomaly by Weyl coboundaries.
4. In `D=4`, the counterterm `int sqrt(g) R^2` shifts only the
   `nabla^2 R` representative by the displayed coefficient.
5. In `D=2`, the anomaly is `-c R/(24 pi)` and is integrated by the
   local Wess-Zumino action for the Weyl factor.
6. In `D=4`, the parity-even metric anomaly is
   `(16 pi^2)^{-1}(c W^2 - a E_4 + b nabla^2 R)` plus additional
   background-source terms when those sources are present.
7. The conformal-scalar coefficients `a=1/360`, `c=1/120` follow directly
   from the `a_4` heat-kernel coefficient.
8. The Dirac entry follows from the Lichnerowicz endomorphism
   `E_D=-R/4`, the spin-curvature trace
   `tr Omega^2=-Riem^2/2`, and the Grassmann local Weyl-response sign.
9. A Weyl fermion is half the local parity-even Dirac density, but this local
   statement is not a globally canonical determinant/Pfaffian square root.
10. The Maxwell entry follows in Lorenz gauge from the one-form Hodge
    operator minus the complex Faddeev-Popov ghost pair; gauge parameter,
    zero-mode, gauge-volume, and topological factors are separate from the
    local UV coefficient.
11. `N=4` Yang-Mills has `a=c=dim(G)/4` in the free-field normalization.
12. Trace anomalies define separated stress-tensor data and contact terms in
    stress-tensor Ward identities; in particular `a` enters separated `TTT`
    and the trace-contact identities, not contact data alone.

## Calculation Ledger

- `calculation-checks/trace_anomaly_checks.py` verifies the scalar
  heat-kernel curvature combination, Dirac spin-bundle `a_4` traces, Maxwell
  one-form/ghost subtraction, Weyl-versus-Dirac local factors, wrong-sign and
  omitted-ghost negative controls, the `R^2` Weyl variation, free-field `a,c`
  arithmetic, the role of `a` in separated `TTT`, `N=4` `a=c`,
  constant-curvature identities, and the two-dimensional Wess-Zumino
  variation.
- `calculation-checks/curvature_squared_euler_convention_checks.py` verifies
  that the `R^2` Weyl coboundary used for the `b nabla^2 R` scheme coordinate
  remains distinct from, and compatible with, the shared Ricci-squared
  Euler-tensor basis used in point splitting and semiclassical transport.

## Figures

- No figure is included.  A later visual pass should add a local-cohomology
  diagram showing `W`, Weyl variation, Wess-Zumino consistency, and
  counterterm coboundaries.

## Audit Notes

- 2026-06-08 issue #729 printed-order pass: added a point-of-use dependency
  paragraph tying the anomaly chapter to point-split stress tensors, finite
  local counterterms, and the local Hadamard subtraction class.  The paragraph
  also prevents the Weyl-response discussion from being read as a replacement
  for the microlocal state condition or pAQFT interacting composite-field
  construction.
- 2026-06-08 issue #929 convention-audit pass: included the trace-anomaly
  `R^2` Weyl-coboundary scheme coordinate in the shared curvature-squared
  regression that now also checks point-splitting finite ambiguity and
  semiclassical finite-scheme transport.
- 2026-06-08 issue #905 heat-kernel-depth pass: expanded the free-field table
  derivation to show the Dirac spin trace, Maxwell one-form/ghost subtraction,
  Weyl local half-density/global determinant-line boundary, and corrected the
  role of `a` in separated `TTT` versus trace contacts.
