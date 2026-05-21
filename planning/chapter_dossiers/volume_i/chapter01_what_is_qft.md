# Volume I, Chapter 1 Dossier: Starting Data For Local Quantum Field Theory

## Status

Current status: re-audited under the stricter definition and symbol rules in
the 2026-05-22 development pass.  The chapter remains in the compiled
manuscript as the opening framework chapter.

## Logical Role

The chapter introduces the first working framework for the opening volume. It
does not present a final universal axiom system. It supplies local data from
which subsequent constructions begin.

## Framework

Working framework:

- \(D\)-dimensional Minkowski spacetime;
- complex Hilbert space;
- strongly continuous unitary Poincare representation;
- translation generators with spectrum condition;
- invariant vacuum vector;
- local observable assignment to bounded open regions;
- covariance, isotony, and locality;
- optional graded locality when fermionic fields enter later.

Existing axiom systems are comparison frameworks, not foundations for this
chapter.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`: opening local-field and locality
  discussion.
- `transcription/tex/253b/scattering_rg_qcd.tex`: recap of local QFT and
  spectral representation.
- handwritten PDFs in `references/` for disputed wording or figures.

## External Reference Needs

- Wightman fields and reconstruction;
- AQFT local nets;
- OS reconstruction;
- Haag--Ruelle scattering.

Use these only for theorem boundaries and later comparisons.

## Notation Inventory

| Symbol | Type | Framework |
| --- | --- | --- |
| \(D\) | positive integer spacetime dimension | Minkowski framework |
| \(\mathbb M^D\) | affine Minkowski space | spacetime |
| \(\eta_{\mu\nu}\) | Lorentzian metric components | convention |
| \(\Hilb\) | complex Hilbert space | quantum state space |
| \(U(a,\Lambda)\) | strongly continuous unitary representation | Poincare symmetry |
| \(P_\mu\) | self-adjoint translation generators | spectral calculus |
| \(\vac\) | invariant unit vector | vacuum sector |
| \(\mathcal O\) | bounded open spacetime region | localization |
| \(\Obs(\mathcal O)\) | local algebra assigned to \(\mathcal O\) | observable net |
| \(\widehat\Phi_A(f)\) | smeared field operator/distribution | field coordinate |

## Definition Ledger

- Vacuum Minkowski local quantum framework: working data for the opening
  volume.
- Local observable assignment: region-to-algebra assignment with covariance,
  isotony, and locality.
- Smeared field: operator-valued distribution evaluated on a test function.

Definitions must specify domains and support conditions.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The opening framework consists of Hilbert space, symmetry, spectrum, vacuum, and local observables. | Working definition | Defined in chapter |
| Fields in this framework are distributional coordinates on local data. | Framework statement | Defined and compared with Wightman language |
| Particles, S-matrix, LSZ, and perturbative scattering require further hypotheses. | Structural claim | Stated as dependency plan; derived later |
| Kallen--Lehmann will be the first bridge from local fields to particle content. | Ordering rule | Source spine |

## Required Revisions

- Completed: removed main-text framing organized around exclusion.
- Completed: typed the symbols used in the opening definition, including the
  Poincare group, \(\mathcal B(\Hilb)\), \(\mathcal U(\Hilb)\), spacelike
  separation of regions, and the joint spectral measure.
- Completed: stated that \(\Obs(\mathcal O)\) is a concrete unital
  \(*\)-subalgebra of \(\mathcal B(\Hilb)\), with \(C^*\)- or von Neumann
  closure imposed only when declared.
- Completed: moved non-vacuum and non-flat settings into a positive domain
  statement about changed data.

## Figure Ledger

- `fig:opening-framework-comparison`: TikZ comparison map among Wightman
  fields, local nets, Euclidean data, and the Hilbert-space vacuum sector.
  The figure must be checked after every layout-affecting edit to ensure arrow
  labels remain legible.
