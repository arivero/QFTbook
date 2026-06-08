# 2026-06-08 -- Issue 888, Volume X CME Protocol/Current Ledger

Scope:

- Monograph target:
  `monograph/tex/volumes/volume_x/chapter09_anomalous_and_topological_transport.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_x/chapter09_anomalous_and_topological_transport.md`.
- Check target:
  `calculation-checks/anomalous_transport_checks.py`.

Primary-source comparison:

- Landsteiner--Megias--Pena-Benitez, arXiv:1312.1204: used for the
  consistent/covariant current distinction, the axial-source versus axial
  chemical-potential implementation, and the source-only cancellation pattern.
- Banerjee et al., arXiv:1203.3544: used for the equilibrium partition
  function normalization, the `T_0 = 1/beta` current variation factor, and
  Bardeen--Zumino local-current bookkeeping.
- Fukushima--Kharzeev--Warringa, arXiv:0808.3382: used for the prepared
  chiral-imbalance density-matrix and lowest-Landau-level current route.

Substance added:

- The CME section now chooses the prepared, slowly relaxing chiral imbalance
  as the primary coefficient protocol.
- The axial source `a_0^5` is separated from the occupation imbalance
  `mu_5^occ`.
- The thermal reduction keeps the circle circumference:
  `W_3 = - beta a_0^5 A_V dA_V/(4 pi^2)`, and the current map divides by
  `beta`.
- The vector-preserving consistent current, Bardeen--Zumino current, and
  covariant current are displayed in one ledger:
  `J_cons,V = (mu_5^occ - a_0^5) B_V/(2 pi^2)`,
  `J_BZ,V = a_0^5 B_V/(2 pi^2)`,
  `J_cov,V = mu_5^occ B_V/(2 pi^2)`.
- The Kubo definition now derives the response-kernel sign from
  `delta S_L = int J delta A` and
  `H[A] = H[0] - int A_i J^i`, and assigns local
  Bardeen--Zumino/magnetization contact terms before transport extraction.
- A protocol table distinguishes axial source, prepared imbalance, modified
  axial charge, and transport measurement.

Regression checks:

- `anomalous_transport_checks.py` now checks the beta-normalized source
  current, Bardeen--Zumino shift, source-only covariant cancellation,
  combined consistent/covariant ledger, Kubo sign, and vanishing net flow of
  periodic magnetization curls.

Re-audit note:

- This pass deliberately avoided adding tangential anomaly mathematics.  The
  depth is physics-facing: state preparation, source coupling, regulator
  counterterm, current representative, and transport observable are separated
  before the coefficient is compared across methods.
