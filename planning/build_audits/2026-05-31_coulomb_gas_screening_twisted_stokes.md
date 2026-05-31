# Coulomb-Gas Screening Twisted-Stokes Pass

Date: 2026-05-31

Issue context:

- Advances #697, the Volume V CFT quoted-theorem/proof-boundary audit.
- Also advances #691 because the proof now carries the actual analytic
  mechanism rather than a compressed phrase about twisted-cycle boundary
  cancellation.

Scope:

- `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
- `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`

Substantive changes:

- Defined the configuration-space complement for Coulomb-gas screening
  variables and the rank-one local system of the multivalued integrand.
- Defined a twisted cycle as a chain with coefficients in the dual local
  system and vanishing twisted boundary, including relative endpoint data
  when a compactification prescription is used.
- Expanded the proof that screening charges are Virasoro intertwiners:
  the OPE gives `[L_n,S(u)] = d_u(u^{n+1}S(u))`; integration over a twisted
  cycle vanishes by twisted Stokes.
- Derived the neutrality condition from the background charge at infinity in
  the stress-tensor Ward identity, rather than leaving it as bookkeeping.
- Stated the meromorphic-continuation step: prove in a convergence chamber
  and continue within the same twisted homology class away from collision and
  resonance divisors.

Verification plan:

- Run the minimal-model/Coulomb-gas calculation check and the standard TeX,
  theorem-form, prose, display-label, and dossier audits.
