# Volume II, Chapter 10 Dossier: Renormalizability And Local Counterterms

## Source Position

- Primary local source: second-sequence handwritten material, pages 81--96.
- Immediate predecessor: generating functionals and the 1PI effective action.
- Immediate successor in the source order: subdivergences and forest formulas.
- Role in the monograph: use the 1PI effective action to formulate
  perturbative renormalizability as finite-parameter control of local
  counterterms.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 81--96;
  checked against rendered page images.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  renormalizability section, used only as a comparison layer.
- `SRC-EXTERNAL`: Fredenhagen--Rejzner for perturbative locality and
  extensions of time-ordered products; Rosten for Wilsonian context.  The
  chapter itself is written as a self-contained perturbative construction.
  Steinmann scaling degree is used only as a local ultraviolet tool, not as an
  infrared existence theorem.

## Construction Task

The chapter must define:

- the regulated Euclidean functional integral \(Z_\Lambda\);
- the scalar convention that \(D_\Lambda^{\rm ref}\phi\) is the
  finite-regulator reference density, while Gaussian-reference formulas use
  \(\dd\mu_{C_\Lambda}\) and keep only the remaining interaction in the
  exponential;
- local operators \(\mathcal O_I\) and bare couplings \(g_I\);
- regulator choices \(\Lambda\) and \(D=d-\varepsilon\);
- the finite-dimensional renormalized coordinate domain \(U\) and the
  regulator-dependent bare coordinate maps \(b_\Lambda,b_\varepsilon\);
- the distinction, cross-referenced to
  `tab:regulator-integration-status-catalog`, between cutoff regulators that
  may define finite field integrals and dimensional regularization as a
  meromorphic perturbative graph assignment;
- renormalized field \(\phi_R=Z_R^{-1/2}\phi\);
- the effective action \(\widetilde\Gamma[\phi_R]=\Gamma[Z_R^{1/2}\phi_R]\);
- the distinction between full distributional Green-function finiteness and
  the local Taylor coefficients \(g_I^{\rm eff}\) used for counterterm
  classification;
- renormalized coordinate parameters \(\lambda\);
- engineering dimension \(d_I\) and coupling dimension \(D-d_I\);
- the superficial degree condition for a local counterterm;
- the \(D=6\), \(\phi^3\) counterterm split;
- the large-momentum self-energy insertion and its local Taylor subtractions;
- the Schwinger-parameter picture of subdivergent regions.
- the boundary of the scaling-degree extension theorem: it assumes a
  distribution on the punctured configuration space and controls only the
  ultraviolet extension across a collision diagonal.
- the distinction between perturbative continuum-limit criteria and
  constructive existence/triviality theorems, with cross-reference to the
  Volume I catalog `tab:constructive-qft-status-catalog`.
- the \(D=4\), \(\phi^4\) field-strength census: the one-loop tadpole is
  independent of external momentum and gives
  \(\delta Z^{(1)}_{\phi^4}=0\), while the kinetic counterterm belongs to the
  local chart because the two-loop sunset generates the first logarithmically
  divergent \(p^2\) Taylor coefficient and power counting then proves closure of
  the finite list.

## Claim Ledger

1. Bare couplings are functions of the regulator and of a finite set of
   renormalized input coordinates.
2. A sufficient perturbative finiteness criterion is the finiteness of
   renormalized Euclidean Green functions as distributions.
2a. Existence of the continuum limit means a theorem or hypothesis for a
    specified regulator family; selected constructive and triviality regimes
    are catalogued in Volume I.
3. On infrared-regular Euclidean momentum domains with invertible two-point
   kernel, perturbative finiteness of connected functions is equivalent to
   finiteness of the corresponding renormalized 1PI kernels by the Legendre
   reconstruction.
4. The local effective couplings are Taylor coefficients of the local part of
   the 1PI action; nonlocal finite terms such as threshold logarithms are part
   of the continuum 1PI kernels.
5. Wavefunction, mass, and interaction counterterms are local terms in the
   same operator basis used to define the regulated action; they are
   regulator-dependent coordinates of that action, not a second Lagrangian.
5a. The chapter separates action regularization from insertion
    regularization: a regulated insertion is a functional or source derivative
    in the regulated path integral, while a renormalized operator is the
    finite source coordinate or finite linear combination obtained after the
    insertion map and the action-coordinate map are fixed.
6. In \(D=4\), after vacuum-energy and tadpole bookkeeping, \(\phi^3\) and
   \(\phi^4\) illustrate finite counterterm closure, while \(\phi^6\)
   first renormalizes its own sextic coupling and then illustrates
   proliferation of higher local terms \(\phi^8,\phi^{10},\ldots\).
6a. In \(D=4\), \(\phi^4\), the one-loop tadpole contributes to the mass
    coordinate but has no external-momentum dependence, so
    \(\delta Z^{(1)}_{\phi^4}=0\).  The field-strength coordinate is nevertheless
    part of the finite local chart: the two-loop sunset supplies the first
    logarithmically divergent \(p^2\) Taylor coefficient, and the subsequent
    power-counting argument closes the candidate list.
7. For an operator with \(n\) fields and \(\ell\) derivatives,
   \(d_I=\ell+n(D-2)/2\).
8. A diagram with inserted vertices \(J\) can generate a counterterm for
   \(O_I\) only when
   \[
     D-d_I-\sum_J(D-d_J)\ge0
   \]
   at the level of superficial power counting, assuming no infrared
   singularity.
9. If all couplings in the action have \(d_J\le D\), the required local
   counterterms are drawn from a finite-dimensional space.
10. In \(D=6\), \(\phi^3\), one-loop two- and three-point divergences are
    canceled by \(\delta Z\), \(\delta m^2\), and \(\delta g\); in
    \(D=6-\varepsilon\) the cubic vertex carries \(\mu^{\varepsilon/2}\).
    The one-loop self-energy should display the Feynman-parameter integral,
    the dimensional-regularization pole polynomial in \(k^2\) and \(m_R^2\),
    and the resulting large-\(k\) finite behavior
    \((\alpha k^2+\beta m_R^2)\log(k^2/\mu^2)\) up to local finite terms.
11. A renormalized one-loop self-energy insertion has large-momentum behavior
    \((\alpha q^2+\beta)\log(q^2/\mu^2)\), and Taylor subtraction of the
    remaining propagator leaves a finite integral.
12. Dimensional regularization exposes the pole part as a polynomial
    \(A_\varepsilon k^2+B_\varepsilon m_R^2\), hence as local.
12a. Dimensional regularization is not used as a measure on
     \(\mathcal F_\Lambda\); in this chapter it is a formal perturbative
     analytic regularization of graph distributions and tensor algebra.
13. In the two-loop diamond graph, Schwinger-parameter subdivergences occur
    when subgraph parameters shrink; counterterm insertions subtract these
    limiting pieces before the overall divergence is treated.
    The Schwinger-parameter matrix \(A\), nonnegative \(Q\), homogeneous
    scaling relation, and explicit \(\widetilde F\) subtraction should be
    written, not only described.
14. For massless graphs, finite scaling degree at a diagonal does not by
    itself prove infrared existence.  The punctured-space distribution must be
    supplied by an infrared-safe prescription before the local extension
    theorem can classify ultraviolet contact-term ambiguities.

## Figure Requirements

- Counterterm census comparing \(D=4\ \phi^3\), \(D=4\ \phi^4\), and
  \(D=4\ \phi^6\).
- Locality of higher-order subtractions: a renormalized subgraph insertion,
  Taylor subtraction of \(k^0,k^2\), and the two-loop diamond subdivergence
  picture.

## Audit Notes

- No reader-facing source-page references.
- Avoid slogan framing.  State the regulator, the criterion, and the local
  finite-parameter condition explicitly.
- Keep BPHZ as the theorem at the boundary of this chapter; the full forest
  formula belongs in the next chapter.
- 2026-05-22 pass: tightened the finite-parameter coordinate definition,
  separated full 1PI/Green-function finiteness from local Taylor-coefficient
  finiteness, added tadpole bookkeeping to the \(D=4\) census, and fixed the
  \(D=6-\varepsilon\) \(\phi^3\) dimensional factor and self-energy pole form.
- 2026-05-22 source-certification pass: handwritten pp. 81--96 checked
  against the chapter; missing \(D=4\ \phi^6\) sextic self-counterterm,
  explicit \(D=6\ \phi^3\) self-energy pole/large-momentum display,
  absence of \(\varepsilon^{-1}\log k^2\) pole, Schwinger \(Q\), scaling
  relation, \(\widetilde F\) subtraction, and final \(k^0,k^2\) subtraction
  formula were added.
- 2026-05-24 issue pass: addressed #220 by stating the massless caveat for
  the scaling-degree extension theorem and by linking downstream stress-tensor
  contact terms and Wilson--Fisher composite insertions to the same
  ultraviolet-versus-infrared distinction.
- 2026-05-24 issue #300 pass: added a cross-reference from the perturbative
  continuum-limit criterion to the Volume I constructive/triviality catalog.
- 2026-05-24 issue #310 pass: replaced ambiguous \([D\phi]_\Lambda\)-style
  scalar notation by \(D_\Lambda^{\rm ref}\phi\) in the regulated action
  setup and cross-referenced the central distinction among reference density,
  Gaussian measure, and full Euclidean density.
- 2026-05-24 issue #313 pass: cross-referenced the master regulator-status
  table and made explicit that dimensional regularization is formal
  perturbative analytic continuation, not a path-integral measure.
- 2026-05-24 issue #361 pass: sharpened the \(D=4\), \(\phi^4\) counterterm
  census so the vanishing of \(\delta Z\) at one loop is not used as the logic
  for excluding or including the kinetic counterterm; the two-loop sunset and
  the power-counting closure argument now carry that burden explicitly.
