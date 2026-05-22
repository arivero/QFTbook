# Volume I, Chapter 18 Dossier: Maxwell Theory, Constraints, and Gauge Fixing

Status: rewritten and source-audited on 2026-05-22.

## Source Placement

- Follows massless helicity and gauge-representative structure.
- Supplies the free gauge-field dynamics whose one-particle sector realizes
  photon helicities \(h=\pm1\).
- Precedes QED, radiative corrections, nonabelian gauge theory, BRST, and BV.
- Source material used:
  - handwritten 253a trace pages
    `monograph/tex/build/source_visual_trace/253a_trace-197.png` through
    `253a_trace-211.png`;
  - `transcription/tex/253a/foundations.tex`, roughly lines 8366--9110;
  - `references/sound_references/harlow_wu_covariant_phase_space_1906.08616.pdf`
    and text sidecar for constraint and phase-space orientation.

## External Reference Boundary

- The chapter performs the elementary Maxwell constraint calculation directly.
- Dirac's terminology for first-class and second-class constraints is used as
  local finite-codimension phase-space language.
- Faddeev--Popov gauge fixing is derived first for Maxwell theory; nonabelian
  ghosts, BRST cohomology, and BV are deferred until their own constructions.

## Framework

- Four-dimensional Minkowski spacetime with mostly-plus metric.
- Classical vector-potential representatives \(A_\mu\) modulo
  \(A_\mu\mapsto A_\mu+\partial_\mu\xi\).
- Gauge-invariant local field strength \(F_{\mu\nu}\).
- Equal-time canonical phase space with explicit constraints.
- Gauge-fixed Gaussian functional integrals understood through regulators and
  after zero modes of gauge-fixing operators have been removed or separately
  fixed.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(A_\mu\) | vector-potential representative |
| \(\xi,\zeta\) | scalar gauge parameters |
| \(F_{\mu\nu}\) | Maxwell field strength |
| \(\Pi^\mu\) | canonical momentum conjugate to \(A_\mu\) |
| \(\chi_1,\chi_2\) | primary and secondary constraints |
| \(G[\zeta]\) | smeared generator of the representative shift |
| \(\mathcal G(A)\) | gauge-slice function |
| \(M_{\mathcal G}\) | linearized gauge-slice operator |
| \(\Delta_{\mathcal G}\) | Faddeev--Popov determinant |
| \(M_{\mathrm{ax}}\) | axial-gauge operator \(\partial_3\) |
| \(M_{\mathrm L}\) | Lorenz-gauge operator \(\Box\) |
| \(\xi_{\mathrm g}\) | covariant gauge parameter |
| \(\widetilde D_{\mathrm{ax}}^{\mu\nu}\) | axial-gauge quadratic operator |
| \(\widetilde D_{\xi_{\mathrm g}}^{\mu\nu}\) | covariant gauge-fixed quadratic operator |
| \(C_\mu(k)\) | auxiliary null covector used in photon polarization completeness |
| \(Z_A\) | photon field-strength pole normalization |

## Claims Established

- Maxwell theory is locally formulated through gauge-equivalence classes of
  vector-potential representatives; \(F_{\mu\nu}\) is the local
  gauge-invariant field strength.
- The canonical momentum conjugate to \(A_0\) vanishes, giving a primary
  constraint; preserving it gives Gauss' law as a secondary constraint.
- The two Maxwell constraints are first-class and generate
  \(A_\mu\mapsto A_\mu+\partial_\mu\zeta\) when combined with the correct
  time-derivative smearing.
- Axial gauge \(A_3=0\) is regular only after removing or separately fixing
  \(\partial_3\)-zero modes. On regular modes it pairs with Gauss' law to
  leave two canonical photon degrees of freedom.
- The Faddeev--Popov identity is a local statement about a gauge slice and
  its linearized orbit map. In abelian linear gauges the determinant is
  independent of \(A_\mu\).
- The finite-dimensional \((x,y)\) model shows explicitly how the
  gauge-slice Jacobian cancels the slice-dependent integration Jacobian for
  gauge-invariant observables.
- The axial-gauge \(3\times3\) quadratic block has inverse
  \(-k^{-2}(\eta_{\mu\nu}+k_\mu k_\nu/k_3^2)\) for \(k_3\ne0\).
- The covariant-gauge quadratic operator has inverse
  \(-\eta_{\mu\nu}/k^2+(1-\xi_{\mathrm g})k_\mu k_\nu/(k^2)^2\).
- Field-strength two-point functions are independent of the representative
  gauge parameter because longitudinal terms vanish under antisymmetrization.
- The free one-photon field-strength spectral representation is compatible
  with helicity completeness and fixes \(Z_A=1\).

## Figure Requirements

- Gauge-orbit and gauge-slice figure clarifying representative choice in the
  functional integral. Repaired on 2026-05-22 so labels no longer collide in
  the rendered manuscript.
- Feynman-gauge photon propagator line with momentum and Lorentz-index labels.

## Exclusions

- No interacting QED vertices.
- No nonabelian Faddeev--Popov ghosts.
- No BRST cohomology.
- No loop corrections.
