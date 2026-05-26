# Agent Handoff: Solitons, Monopoles, Instantons, ADHM, And Instanton Calculus

## Primary Scope

Issues: #597 and #592.
Likely files:

- new or expanded Volume II chapter(s) near nonperturbative gauge objects;
- `monograph/tex/volumes/volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`
- `monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`
- `monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex`
- possible new files added to the relevant `volume_*_current.tex`;
- calculation checks for instanton and monopole normalizations.

## Objective

Build a foundational treatment of classical and semiclassical
nonperturbative objects: kinks, vortices, monopoles, dyons, instantons,
collective coordinates, moduli-space measures, ADHM construction, and their
roles in supersymmetric gauge dynamics and resurgence.  This lane supplies
background needed by the SUSY and TQFT lanes.

## Conceptual Constraints

- A classical solution is not by itself a quantum state or path-integral
  saddle contribution.  State the transition carefully.
- A moduli-space integral is a regularized coordinate on a semiclassical
  approximation.  Define the regulator, zero modes, nonzero-mode determinant,
  quotient by gauge transformations, and compactification boundary.
- Do not call instanton calculus rigorous unless the measure, determinant,
  and convergence/compactification are specified.
- Distinguish Euclidean finite-action saddles from Lorentzian solitons.
- Preserve the monograph's gauge convention:
  \[
    S_{\rm YM}={1\over 4g^2}\int \operatorname{tr}(F_{\mu\nu}F^{\mu\nu})
  \]
  with the trace convention used elsewhere in the monograph.

## Required Development Targets

1. Define finite-energy sectors in scalar and gauge theories, including
   boundary conditions at spatial infinity and topological charge.
2. Work out the kink in 1+1 dimensions:
   energy functional, Bogomolny bound, fluctuation operator, zero mode,
   collective coordinate, and semiclassical mass shift status.
3. Work out Abelian vortices:
   vortex number, Bogomolny equations at critical coupling, moduli-space
   dimension statement, and limitations.
4. Work out 't Hooft-Polyakov monopoles:
   symmetry breaking data, magnetic charge as cocharacter/topological class,
   Bogomolny equations, Prasad-Sommerfield solution, and moduli.
5. Define dyons and the electric-magnetic charge lattice, with connection to
   Seiberg-Witten BPS central charges.
6. Work out BPST instantons:
   finite-action condition, self-duality, topological charge, action, and
   zero modes.
7. Develop the ADHM construction:
   data, moment-map equations, quotient, framing, dimension count, and at
   least the k=1 example.
8. Define instanton measure:
   collective-coordinate Jacobian, gauge quotient, one-loop determinant,
   ghost determinant, zero modes, and fermion zero modes.
9. Develop ADS superpotential and Nekrasov partition function only after the
   measure framework is stable; state formal versus rigorous status.
10. Add a bridge to resurgence only for well-defined finite-dimensional or
    semiclassical models; avoid renormalon slogans.

## Calculation Checks

Add/extend checks for:

- BPST action/topological charge normalization;
- 't Hooft symbol identities;
- monopole magnetic charge pairing;
- ADHM dimension counts;
- one-instanton measure power of \(g\) and scale dimension in selected
  examples.

## Completion Standard

Block N (#597) is foundational and should be done before Block I (#592) is
closed.  Do not close #592 until ADHM, instanton measure, Nekrasov, and ADS
are developed with status labels.
