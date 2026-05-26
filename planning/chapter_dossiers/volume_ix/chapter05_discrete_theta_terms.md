# Volume IX, Chapter 5 Dossier: Discrete Theta Terms

## Logical Role

- Role in the monograph: define topological gauge-theory phases depending on
  global bundle/cohomology data and relate them to line spectra, one-form
  backgrounds, and anomaly inflow.
- Immediate predecessor: confinement, screening, and oblique confinement.
- Immediate successor: anomaly inflow and invertible field theories.

## Definitions And Results

- Finite zero-form and higher-form gauge fields as cocycles modulo cochain
  gauge transformations.
- Discrete topological action as a local cohomology class evaluated on the
  fundamental cycle.
- Coboundary invariance of the exponentiated action on closed manifolds.
- Two-form \(\mathbb Z_N\) fields and the Pontryagin-square operation
  \(\mathcal P:H^2(-,\mathbb Z_N)\to H^4(-,\mathbb Z_{2N})\).
- Quadratic-refinement identity and the resulting phase ratio for
  Pontryagin-square counterterms.
- \(SU(N)/\mathbb Z_k\) obstruction class \(w_2^{(k)}\) from lifted transition
  functions.
- Fractional \(PSU(N)\) instanton-number characteristic class in terms of
  \(\mathcal P(w_2)\).
- Discrete theta coordinate \(p\in\mathbb Z_k\) as the electric tilt of the
  minimal magnetic line.
- Proof that \(L_{N,k,p}\) is the discrete-theta line lattice and that
  \(p\sim p+k\).
- Coupling to one-form backgrounds, gauging, local counterterms, and anomaly
  inflow status.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(A\) | finite abelian gauge group in the opening section |
| \(a\) | flat \(A\)-gauge cocycle |
| \(B\) | two-form \(\mathbb Z_N\) background |
| \(w_2^{(k)}\) | obstruction to lifting an \(SU(N)/\mathbb Z_k\)-bundle |
| \(\mathcal P(B)\) | Pontryagin square |
| \(p\) | discrete theta parameter |
| \(\gamma=(e,m)\) | electric/magnetic line label |
| \(L_{N,k,p}\) | finite Wilson-'t Hooft line lattice |

## Claim Ledger

1. Discrete theta terms are cohomology classes of finite topological actions.
2. On closed manifolds, changing representative by a coboundary preserves the
   exponentiated action.
3. The Pontryagin square is the correct quadratic refinement for two-form
   \(\mathbb Z_N\) fields in four dimensions.
4. The phase ratio of \(S_p[B+B']\) to \(S_p[B]S_p[B']\) is the bilinear
   cup-product pairing.
5. \(SU(N)/\mathbb Z_k\) bundles have a lift obstruction
   \(w_2^{(k)}\in H^2(-,\mathbb Z_k)\).
6. The discrete theta coordinate \(p\in\mathbb Z_k\) tilts the minimal
   magnetic line and determines \(L_{N,k,p}\).
7. Gauging a one-form symmetry requires choosing the corresponding finite
   counterterm, and its boundary variation is anomaly inflow data.

## Calculation Checks

- `calculation-checks/discrete_theta_terms_checks.py` verifies the finite
  quadratic-refinement arithmetic, classification periodicity of the
  counterterm group,
  \(p\sim p+k\) for \(SU(N)/\mathbb Z_k\), mutual locality of the line
  lattice, the \(SU(2)\)/\(SO(3)_\pm\) examples, and theta-shift electric
  tilting, plus tensor-line invariance of the projective second Chern
  coordinate and the fractional \(PSU(N)\) instanton-number convention.

## Figures

- None in this chapter.
