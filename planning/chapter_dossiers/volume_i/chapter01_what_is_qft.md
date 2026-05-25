# Volume I, Chapter 1 Dossier: Starting Data For Local Quantum Field Theory

## Status

Current status: certified against handwritten 253a pp. 1--2 in the
2026-05-22 development pass.  The chapter remains in the compiled manuscript
as the opening framework chapter.

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
- `references/253a lectures 2022.pdf`, pp. 1--2: opening distinction between
  continuum local QFT and EFT presentations, examples, and initial dependency
  plan.
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
| \(P^\mu\), \(P_\mu=\eta_{\mu\nu}P^\nu\) | self-adjoint energy-momentum generators; \(U(a,1)=\exp(i a_\mu P^\mu)=\exp(i a^\mu P_\mu)\) | spectral calculus |
| \(\vac\) | invariant unit vector | vacuum sector |
| \(\mathcal O\) | bounded open spacetime region | localization |
| \(\Obs(\mathcal O)\) | local algebra assigned to \(\mathcal O\) | observable net |
| \(\widehat\Phi_A(f)\) | smeared field operator/distribution | field coordinate |
| \(\Delta_n\) | collision locus in \(M^n\) where at least two insertion points coincide | contact-term geometry |
| \(J^A\) | compactly supported local source field | source chart |
| \(W[J]\) | source functional whose derivatives define inserted distributions | source-response data |
| \(\mathrm{EFT}\) | effective field theory presentation, not a separate axiom system | regulated/local expansion framework |

## Definition Ledger

- Vacuum Minkowski local quantum framework: working data for the opening
  volume.
- Continuum local quantum field theory: local data that exist after removing
  a UV regulator in a declared topology and framework.
- Effective field theory presentation: regulated or renormalized local
  prescription for a specified scale window, expansion, and observable class.
- Local observable assignment: region-to-algebra assignment with covariance,
  isotony, and locality.
- Smeared field: operator-valued distribution evaluated on a test function.
- Contact-term extension: an extension of a separated-point distribution from
  \(M^n\setminus\Delta_n\) to \(M^n\), with differences supported on collision
  diagonals.
- Local source chart: source fields, a source functional, and distributional
  source derivatives, modulo local finite changes that alter diagonal-supported
  contact terms.
- Four-dimensional constructive local QFT open problem: construction of
  Wightman/OS data, Hilbert space or local observable net, positivity,
  covariance, locality, and spectral properties for a non-Gaussian local
  scalar or gauge model.

Definitions must specify domains and support conditions.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The opening framework consists of Hilbert space, symmetry, spectrum, vacuum, and local observables. | Working definition | Defined in chapter |
| Continuum local QFT and EFT presentations share locality but make different mathematical-status claims. | Source-certified framework distinction | Added from handwritten pp. 1--2 with caveats about regulator removal, scale windows, and power counting |
| Fields in this framework are distributional coordinates on local data. | Framework statement | Defined and compared with Wightman language |
| Contact terms are coincident-point/source-response data supported on collision diagonals, not determined by separated-point correlators alone. | Framework definition | Added as Definition `contact-terms-source-chart` |
| Wightman/OS data for selected fields do not by themselves fix composite products, time-ordered products, nonlinear source couplings, or repeated source derivatives on diagonals. | Boundary statement | Stated in opening analytic-status section |
| Wightman, AQFT, OS, and path-integral presentations are connected by explicit comparison maps, each with its own hypotheses. | Theorem register | Added comparison-map register pointing to Wightman reconstruction, Wightman-to-net, net-to-Wightman, OS-II reconstruction, and path-integral-to-OS composition |
| Wightman, OS, AQFT/local-net, constructive, perturbative, and functorial/path-integral frameworks are theorem-bearing comparison frameworks whose hypotheses must be retained in theorem statements. | Framework-status statement | Added Section `sec:status-axiom-systems-constructive-examples` for issue #483 |
| Constructive examples calibrate expected properties: completed non-Gaussian constructions are concentrated in low-dimensional regimes, standard `D >= 4` positive `phi^4` routes are constrained by triviality, and four-dimensional gauge-theory construction remains open. | Constructive status statement | Cross-references Table `tab:constructive-master-status` and OS Remark `rem:os-constructive-status-inputs` for issues #480/#482 |
| The relationship among Wightman fields, OS data, local nets, and functorial/path-integral data is itself an open comparison problem. | Open problem | Added Open Problem `op:axiomatic-comparison-physical-examples` |
| OS Euclidean data for reconstruction are zero-diagonal Schwinger distributions with OS-II semigroup and linear-growth input, not merely Euclidean moments plus reflection positivity. | Historical/analytic correction | Aligned with OS II and the OSReconstruction formalization interface |
| Constructive existence of physically interacting four-dimensional local QFT is an open problem except for free/generalized-free examples and model-specific conditional or trivial regimes. | Status/open problem | Added as Open Problem `op:four-dimensional-constructive-qft`; cross-checks the path-integral status catalog |
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
- Completed: restored the handwritten opening fork as rigorous prose and a
  non-course-specific figure; course labels and semester arrows were not
  imported.
- Completed: issue #498 pass added the foundational contact-term/source-chart
  definition and separated Wightman/OS distributional field data from
  composite, time-ordered, source-response, Ward-identity, and anomaly contact
  conventions.
- Completed: issue #333 pass added the four-dimensional constructive-QFT open
  problem at the opening-framework level, separating low-dimensional
  constructive examples, scalar triviality regimes, finite regulators,
  perturbative expansions, and open four-dimensional gauge/scalar
  construction problems.
- Completed: issue #424 pass made the translation-generator sign and index
  convention explicit: the spectrum condition is imposed on contravariant
  \(P^\mu\), while \(a^\mu P_\mu=a_\mu P^\mu\) appears in the unitary
  translation exponent with the common \(+i\) convention.
- Completed: issues #480/#482/#483 pass added the framework-status section,
  constructive-status cross-reference to the Volume XI table, OS
  constructive-input remark, and open problem on axiomatic comparison and
  verification in physically central examples.

## Figure Ledger

- `fig:opening-local-qft-eft`: TikZ source-fork figure distinguishing
  continuum local QFT data from EFT presentations.  Must keep the examples
  status-qualified: constructive low-dimensional/scaling-limit examples on
  the continuum side, perturbative scale-window examples on the EFT side.
- `fig:opening-framework-comparison`: TikZ comparison map among Wightman
  fields, local nets, Euclidean data, and the Hilbert-space vacuum sector.
  The figure must be checked after every layout-affecting edit to ensure arrow
  labels remain legible.
