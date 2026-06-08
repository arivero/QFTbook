# Volume VIII, Chapter 1 Dossier: Metric Independence And Cohomological Observables
Source-File: monograph/tex/volumes/volume_viii/chapter01_metric_independence_and_cohomological_observables.tex

## Logical Role

- Role in the monograph: open the topological/cohomological volume from
  renormalized metric response, cohomological Ward data, descent, and the
  distinction between metric-independent correlators and functorial TQFT.
- Provides the proof-status atlas for the TQFT/higher-symmetry volumes:
  local finite proof, local mechanism under model hypotheses, external
  mathematical theorem boundary, controlled QFT hypothesis, and open comparison
  problem.
- Immediate predecessor: gauge-theory BRST/BV material and CFT stress-tensor
  material.
- Immediate successor: Atiyah--Segal functoriality, BF theory, and
  Chern--Simons theory.

## Definitions And Results

- Stress-tensor response as a renormalized distributional insertion with
  explicit contact term \(C_{\delta g}(X)\).
- Proof-status map for topological claims across Volumes VIII and IX,
  separating finite calculations, local algebraic mechanisms, external
  mathematical inputs, continuum QFT hypotheses, and unresolved comparison
  theorems.
- Cohomological Ward datum: graded insertion algebra, odd nilpotent
  derivation \(\delta_Q\), admissible insertions, and Ward identity.
- Cohomological topological sector as the condition that the entire
  one-parameter metric response, including contact terms and moving insertion
  representatives, is \(Q\)-exact.
- Theorem proving metric independence from the Ward datum.
- Failure mechanisms: BV anomaly, boundary or noncompact field-space
  contributions, and contact terms changing the observable algebra.
- Descent equations \(\delta_QO^{(p+1)}+\dd O^{(p)}=0\) and proof that
  integrated descendants depend only on homology in \(Q\)-cohomology.
- Donaldson-type descent form as the first gauge-theory example.
- Finite-dimensional de Rham model of \(Q\)-Stokes and \(Q\)-exact
  deformation independence.
- Distinction between cohomological field theory and fully extended functorial
  TQFT as a theorem target.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(g_{\mu\nu}\) | background metric |
| \(T_{\mu\nu}\) | stress tensor coupled to metric variation |
| \(C_{\delta g}(X)\) | contact insertion produced by metric variation |
| \(Q\) | odd nilpotent cohomological charge |
| \(\delta_Q\) | odd derivation implementing the \(Q\)-variation |
| \(\mathcal O_i\) | \(Q\)-closed observable |
| \(G_{\mu\nu}\) | local operator satisfying \(T_{\mu\nu}=\{Q,G_{\mu\nu}\}\) |
| \(V_s\) | odd insertion whose \(Q\)-variation is the metric response |
| \(O^{(p)}\) | \(p\)-form-valued descended observable |
| \(\Sigma_p\) | closed \(p\)-cycle supporting an integrated descendant |
| \(Z(M)\) | partition function assigned to a closed manifold |
| `local finite proof` | finite-dimensional or finite-groupoid calculation |
| `external theorem boundary` | imported mathematical theorem with stated hypotheses |
| `controlled QFT hypothesis` | regulator/BV/Hilbert/anomaly/compactness datum still required |

## Claim Ledger

1. Metric independence is derived from the full renormalized metric-response
   formula, not from the symbolic absence of \(g_{\mu\nu}\).
2. Topological-volume claims carry distinct proof statuses: finite local
   proofs and model mechanisms do not prove the external higher-categorical or
   continuum QFT construction theorems they illuminate.
3. The \(Q\)-exactness of the entire metric response is a sufficient
   cohomological mechanism for metric-independent correlators.
4. A local formula \(T_{\mu\nu}=\{Q,G_{\mu\nu}\}\) is insufficient unless the
   contact and representative-variation terms are also \(Q\)-exact.
5. Ward identities can fail by BV anomaly, boundary terms, noncompact ends,
   or collision/contact contributions.
6. Descent equations make integrated observables homological in
   \(Q\)-cohomology when contact terms are absent or controlled.
7. A functorial TQFT contains gluing data beyond metric-independent numbers.

## Figures

- Metric-deformation surface with fixed operator insertions.
- Cofiber diagram from local cohomological theory to functorial closed
  manifolds and bordisms.

## Calculation Checks

- `calculation-checks/cohomological_metric_descent_checks.py` verifies the
  finite de Rham-model signs used in the chapter: \(Q^2=0\), graded Leibniz,
  Stokes' boundary term, and vanishing of a \(Q\)-exact deformation after the
  boundary contribution is zero.

## Audit Notes

- 2026-06-03 #698 proof-status atlas pass: added the topological-volume map
  distinguishing local finite proof, explicit-model mechanism, external
  theorem boundary, controlled QFT hypothesis, and open comparison problem.
  This is the organizing layer for the many local TQFT/higher-symmetry
  mechanisms added in the proof-debt wave.
