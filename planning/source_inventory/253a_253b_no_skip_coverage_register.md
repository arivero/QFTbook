# 253a/253b/Selected 253c Source Coverage Register

This register is the working control for the instruction that the monograph
may deepen, reorganize, correct, and generalize the handwritten QFT notes, but
may not silently omit their substance.  The handwritten PDFs are primary; the
faithful transcription in `transcription/tex/` is the operational source
layer; Ben Lou's transcriptions in `references/` are comparison aids only.

PDF page counts:

| Source | PDF | Pages |
| --- | --- | ---: |
| 253a | `references/253a lectures 2022.pdf` | 244 |
| 253b | `references/253b lecture notes 2023.pdf` | 257 |
| 253c | `references/253c 2023.pdf` | 185 |

## Coverage Status Labels

- `certified`: checked against the source transcription and the relevant
  handwritten pages at derivation/figure level, then incorporated in the
  compiled monograph.
- `mapped`: the topic has a clear compiled monograph home, but a page-level
  derivation and figure audit is still required before it can be called
  certified.
- `partial`: the monograph contains neighboring material or the final result,
  but a source derivation, example, figure, or conceptual distinction is known
  to be compressed or missing.
- `deferred-special`: assigned to a later special-topic volume rather than the
  present compiled core volumes.
- `non-reader-metadata`: course-outline or administrative material that should
  not appear as reader-facing monograph prose.
- `needs-source-check`: the source block has not yet been compared against the
  handwritten PDF pages, even if a student transcription exists.

Compression is not coverage.  A result stated without the source calculation
is a gap whenever the source calculation carries conceptual content.

## 253a: First Sequence Coverage Map

| Source pages / block | Status | Compiled monograph home | Audit action |
| --- | --- | --- | --- |
| pp. 1--2, opening question and role of QFT | mapped | `volume_i/chapter01_what_is_qft.tex` | Verify that the opening gives positive definitions and does not import course framing. |
| pp. 3--9, relativistic particles, causality, local fields, Poincare covariance, microcausality | mapped | `volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex`; `volume_i/chapter03_local_field_operators_poincare_covariance_and_microcausality.tex`; early Wightman/AQFT chapters | Check all source figures for causal support, commutators, and representation logic. |
| pp. 10--14, Lagrangian/Hamiltonian mechanics and phase-space to configuration path integral | mapped | `volume_i/chapter04_lagrangian_formalism_and_quantum_mechanical_path_integrals.tex` | Verify phase-space measure, midpoint/ordering assumptions, and momentum integration exercise. |
| pp. 15--18, correlation functions, time ordering, Wick rotation | mapped | `volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex` | Check analytic-continuation hypotheses and sign conventions. |
| pp. 19--23, harmonic oscillator propagator | mapped | `volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex` | Check mode expansion, contour integral, and \(T\to\infty\) limit. |
| pp. 24--29, finite and functional Gaussian integrals, Wick contractions | mapped | `volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex` | Verify determinant normalizations and source-derivative conventions. |
| pp. 30--43, anharmonic oscillator, vacuum diagrams, two-point function, self-energy, spectrum extraction | mapped | `volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`; `volume_i/chapter10_perturbative_green_functions_and_feynman_graphs.tex` | Check every vacuum and two-point diagram against the source figures. |
| pp. 43--51, derivative interactions, regulator dependence, counterterms | certified after 2026-05-22 derivative-interaction source/figure audit | `volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`; `volume_ii/chapter08_renormalizability_and_local_counterterms.tex` | Handwritten pp. 43--51 and the rendered manuscript were rechecked end-to-end. The derivative-coupled oscillator includes the classical coordinate check, derivative-contraction figure with \(k,k'\) and cutoff support, cutoff self-energy, local counterterm, finite-part ambiguity, and pole/energy-gap interpretation. |
| pp. 52--62, classical and canonical free scalar field | certified after 2026-05-22 free scalar canonical source/figure audit | `volume_i/chapter06_relativistic_scalar_fields_and_canonical_quantization.tex` | The field variational calculus, free scalar mass shell, Cauchy-data inversion, canonical/path-integral distinction, equal-time brackets, oscillator normalization, Bogoliubov ambiguity, Hamiltonian diagonalization, vacuum-energy normalization, and covariance/microcausality page were patched and rendered against handwritten pp. 52--62 on 2026-05-22. |
| pp. 63--71, Noether theorem, stress tensor, Poincare generators | certified 2026-05-22 | `volume_i/chapter07_symmetries_noether_theorem_and_stress_tensors.tex` | Source visual trace `monograph/tex/build/source_visual_trace/253a_trace-063.png`--`253a_trace-071.png`; rendered audit `planning/build_audits/2026-05-22_noether_stress_tensor_source_figures.md`. |
| pp. 72--79, scalar field path integral and Euclidean propagators | certified 2026-05-22 | `volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex` | Source visual trace `monograph/tex/build/source_visual_trace/253a_trace-072.png`--`253a_trace-079.png`; rendered audit `planning/build_audits/2026-05-22_scalar_path_integrals_green_functions_source_figures.md`. |
| pp. 80--99, Green functions, Kallen--Lehmann representation, particle content, \(Z\) | certified 2026-05-22 | `volume_i/chapter09_kallen_lehmann_spectral_representation_and_particle_content.tex` | Source visual trace `monograph/tex/build/source_visual_trace/253a_trace-080.png`--`253a_trace-099.png`; rendered audit `planning/build_audits/2026-05-22_kallen_lehmann_particle_content_source_figures.md`. |
| pp. 100--112, \(\phi^4\) perturbation theory for Green functions | certified 2026-05-22 | `volume_i/chapter10_perturbative_green_functions_and_feynman_graphs.tex`; `volume_i/chapter11_lorentzian_green_functions_and_analytic_continuation.tex` | Source visual trace `monograph/tex/build/source_visual_trace/253a_trace-100.png`--`253a_trace-112.png`; rendered audit `planning/build_audits/2026-05-22_perturbative_green_functions_source_figures.md`. Green-function diagrams remain before scattering, LSZ, and any perturbative S-matrix interpretation. |
| pp. 113--145, asymptotic states, Haag--Ruelle logic, LSZ, unitary \(S\), cross sections, partial waves | mapped | `volume_i/chapter12_haag_ruelle_scattering_theory.tex`; `volume_i/chapter13_lsz_reduction_and_the_s_matrix.tex`; `volume_i/chapter14_cross_sections_partial_waves_and_unitarity.tex`; `volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex` | Check source order: nonperturbative scattering first, LSZ second, perturbative amplitudes only after LSZ. |
| pp. 146--165 and following source blocks, massive spin, little group, projective representations | mapped | `volume_i/chapter15_massive_particles_with_spin.tex` | Compare spin-state normalization, boost conventions, and little-group figures. |
| later 253a source blocks, Dirac field, spin-statistics motivation, Weyl/Majorana spinors | mapped | `volume_i/chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex` | Check gamma-matrix conventions and fermion Kallen--Lehmann statements. |
| later 253a source blocks, Grassmann mechanics, Dirac brackets, Berezin path integral, fermion LSZ | mapped | `volume_i/chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex` | Verify sign conventions in Berezin Gaussian integrals and LSZ residues. |
| later 253a source blocks, massless helicity and photon gauge redundancy | mapped | `volume_i/chapter17_massless_particles_helicity_and_gauge_redundancy.tex` | Check little-group translation/gauge-redundancy logic. |
| later 253a source blocks, Maxwell constraints and gauge fixing | mapped | `volume_i/chapter18_maxwell_theory_constraints_and_gauge_fixing.tex` | Verify canonical constraint analysis and Faddeev--Popov determinant. |
| later 253a source blocks, QED Feynman rules, external states, Compton scattering | mapped | `volume_i/chapter19_quantum_electrodynamics_and_external_states.tex` | Check external-state conventions and the Compton diagrams. |
| later 253a source blocks, QED renormalization, photon self-energy, electron form factor | mapped | `volume_i/chapter20_qed_renormalization_and_electromagnetic_form_factors.tex` | Check one-loop integrals, Ward identity use, and form-factor normalization. |

## 253b: Second Sequence Coverage Map

| Source pages / block | Status | Compiled monograph home | Audit action |
| --- | --- | --- | --- |
| pp. 1--6, Poincare symmetry to spectral data | mapped | `volume_ii/chapter01_local_qft_spectral_data_and_path_integrals_revisited.tex`; `volume_i/chapter09_kallen_lehmann_spectral_representation_and_particle_content.tex` | Check that this revisits, rather than delays, spectral representation. |
| pp. 7--12, in/out bases, LSZ, first scalar amplitude | mapped | `volume_ii/chapter02_the_s_matrix_and_lsz_revisited.tex` | Verify amplitude example occurs after nonperturbative \(S\)-matrix definition. |
| pp. 13--18, bound states, partial waves, first resonance | mapped | `volume_ii/chapter03_bound_states_from_exchange_amplitudes.tex`; `volume_i/chapter14_cross_sections_partial_waves_and_unitarity.tex` | Check pole convention and partial-wave normalization. |
| pp. 19--26, self-energy, branch cuts, second sheet | mapped | `volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex` | Check analytic continuation diagrams and width normalization. |
| pp. 27--33, composite bound states and Bethe--Salpeter | mapped | `volume_ii/chapter05_composite_bound_states_and_bethe_salpeter_amplitudes.tex` | Verify four-point factorization and kernel equation. |
| pp. 34--40, analyticity, crossing, Landau singularities | mapped | `volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex` | Check Landau-equation figures and Coleman--Norton interpretation status. |
| pp. 41--55, Lehmann ellipses, dispersion relations, Froissart--Martin | mapped | `volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex` | Verify all assumptions behind polynomial boundedness and subtractions. |
| pp. 56--70, infrared divergences and inclusive QED amplitudes | mapped | `volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex` | Check soft theorem, real/virtual cancellation, and regulator logic. |
| pp. 71--80, generating functionals and 1PI effective action | certified after 1PI source/figure audit | `volume_ii/chapter23_generating_functionals_and_the_one_particle_irreducible_effective_action.tex` | Source functional, source vertex, connected generator, Legendre transform, background split, tadpole/1PR cancellation, 1PI kernels, exact tree reconstruction, Euclidean concavity/convexity, Legendre--Fenchel convexification, and branch perturbation condition were patched and rendered against handwritten pp. 71--80 on 2026-05-22. |
| pp. 81--96, renormalizability and local counterterms | mapped | `volume_ii/chapter08_renormalizability_and_local_counterterms.tex`; `volume_ii/chapter09_subdivergences_and_bphz_subtractions.tex` | Check power-counting proof and local subtraction logic. |
| pp. 97--110, 1PI renormalization group | certified after 1PI RG source/figure audit | `volume_ii/chapter10_renormalization_group_and_running_couplings.tex` | Subdiagram reuse, scale-dependent field normalization, symmetric subtraction, one-loop \(\phi^4\) channels and tadpole distinction, nearby-scale comparison, Landau scale, general 1PI coordinates including \(g_{2,2}\) and \(\lambda_2\), logarithmic consistency, Callan--Symanzik derivation, and scheme-change formulas were patched and rendered against handwritten pp. 97--110 on 2026-05-22. |
| pp. 111--118, renormalized operators and minimal subtraction | mapped | `volume_ii/chapter12_renormalized_operators_and_minimal_subtraction.tex` | Check operator mixing and \(\partial\beta/\partial g\) relation. |
| pp. 119--123, stress-tensor trace and conformal currents | mapped | `volume_ii/chapter13_stress_tensor_trace_scale_invariance_and_conformal_currents.tex` | Verify local-translation derivation and separated/contact-term caveats. |
| pp. 124--135, Wilson--Fisher fixed point and scaling operators | mapped | `volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex` | Check anomalous-dimension calculations and descendant/irrelevant-operator discussion. |
| pp. 136--146, Ising universality | mapped | `volume_ii/chapter15_the_statistical_ising_model_and_universality.tex` | Check lattice-to-continuum scaling limit and universality statement. |
| pp. 147--156, Wilsonian effective actions and Polchinski flow | certified after Wilsonian source/figure audit | `volume_ii/chapter16_wilsonian_effective_field_theory.tex` | Smooth cutoff, source-supported generating functional equality, explicit shell-source split, covariance decomposition, shell integration, Wilson--Polchinski equation with sign derivation, irrelevant-coupling slaving, continuum-limit construction, finite irrelevant bare couplings, and all source figures were checked against handwritten pp. 147--156 and rendered PDF pages 243--252 on 2026-05-22. |
| pp. 157--168, classical Yang--Mills theory and matter | mapped | `volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex` | Check principal-bundle/connection language against source-level formulas. |
| pp. 169--181, gauge fixing, ghosts, and BRST cohomology | mapped | `volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex` | Check BRST nilpotence, gauge-fixing independence, and physical cohomology. |
| pp. 182--201, YM Feynman rules and one-loop QCD beta function | certified after ordinary-rule figure audit and background-field beta audit | `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`; `volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex` | Background-field determinant coefficients were checked on 2026-05-22.  The ordinary Lorenz-gauge ghost/gluon propagators, ghost-gluon vertex, no \(\bar c c A A\) vertex, \(B\)-field normalization, and cubic/quartic gluon self-interaction diagrams were patched and rendered against handwritten pp. 182--184 on 2026-05-22. |
| pp. 202--210, Banks--Zaks, confinement expectation, Wilson lines/loops, DIS/OPE | certified after infrared/DIS figure audit | `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex` | Banks--Zaks, confinement expectation, Wilson-line/loop diagnostics, inclusive DIS kinematics, Wightman tensor, forward-Compton relation, OPE/light-ray figure, local twist-two operators, and logarithmic scaling violation were patched and rendered against handwritten pp. 202--210 on 2026-05-22. |
| pp. 211--225, chiral anomalies | certified after chiral-anomaly contact-term figure audit | `volume_ii/chapter20_chiral_axial_anomalies.tex` | The 2D axial-vector contact-term calculation, conserved/anomalous contour-charge figures, 4D one-axial/two-vector triangle pair, evanescent-momentum coefficient extraction, abelian anomaly identity, and measure/index continuation were patched and rendered against handwritten pp. 211--225 on 2026-05-22. |
| pp. 226--238, global anomalies and spontaneous symmetry breaking | certified after global-anomaly/SSB figure audit | `volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex` | The perturbative global-anomaly contact term, finite background variation, vacuum-sector locality argument, double-well figure, Goldstone spectral proof, and \(U(1)\) Goldstone/explicit-breaking model were patched and rendered against handwritten pp. 226--238 on 2026-05-22. |
| pp. 239--248, chiral symmetry breaking and pion EFT | certified after chiral-EFT coordinate/WZW audit | `volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex` | The \(SU(N_f)_L\times SU(N_f)_R/SU(N_f)_V\) pattern, Vafa--Witten positivity caveat, axial phase, \(SU(2)\) stereographic chart, corrected \(\vec D_\mu\) transformation, four-derivative invariants, and WZW filling figure were patched and rendered against handwritten pp. 239--248 on 2026-05-22. |
| pp. 249--257, chiral perturbation theory, pion scattering, masses, \(\pi^0\to2\gamma\) | certified after pion-scattering/mass/anomaly figure audit | `volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex` | Pion scattering, source logarithms, \(C_4,C'_4\) running, two-flavor mass normalization, physical pion masses, microscopic electromagnetic triangle, and \(\pi^0\gamma\gamma\) vertex were patched and rendered against handwritten pp. 249--257 on 2026-05-22. |

## Selected 253c: Third Sequence Coverage Map

The current compiled core CFT material deliberately stops before the advanced
special-topic material that Xi asked us to keep out of the core manuscript for
now.  The following table records what is core-covered and what is deferred.

| Source pages / block | Status | Compiled monograph home | Audit action |
| --- | --- | --- | --- |
| pp. 1--6, QFT fixed points, stress trace, Ising fixed point | mapped | `volume_iii/chapter01_fixed_points_and_conformal_data.tex`; `volume_ii/chapter15_the_statistical_ising_model_and_universality.tex` | Check relation between RG fixed points and CFT assumptions. |
| pp. 7--18, conformal Killing vectors, conformal group, conformal vs Weyl | mapped | `volume_iii/chapter02_conformal_killing_vectors_and_the_conformal_group.tex`; `volume_iii/chapter03_stress_tensor_weyl_structure_and_improvement.tex` | Verify conformal coupling and stress-tensor improvement derivations. |
| pp. 19--28, basic consequences, state/operator correspondence, operator partition function | mapped | `volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex` | Check cylinder map, local-operator Hilbert-space assumptions, and free-scalar examples. |
| pp. 29--48, charges, Ward identities, conformal algebra, primaries, finite transformations | mapped | `volume_iii/chapter05_conformal_charges_and_ward_identities.tex`; `volume_iii/chapter06_primary_operators_and_finite_transformations.tex` | Check generator conventions and finite primary transformation formulas. |
| pp. 48--61, unitarity bounds, BPZ inner product, spinning two-point functions | mapped | `volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`; `volume_iii/chapter08_correlation_functions_and_conformal_frames.tex` | Verify Gram matrices and saturation/free-field claims. |
| pp. 62--89, conformal Ward identities, two-/three-/four-point kinematics, OPE, conformal blocks, crossing | mapped | `volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`; `volume_iii/chapter09_operator_product_expansion.tex` | Check all conformal-frame figures and block/crossing normalizations. |
| pp. 90--112, projective lightcone, Casimir equations, bootstrap bounds | deferred-special | Future CFT special volume; removed from compiled core by project decision | Preserve as source obligation for the CFT volume, not the core volumes. |
| pp. 113--115, survey of CFTs | deferred-special | Future CFT special volume | Treat as source leads, not as polished survey prose. |
| pp. 116--153, two-dimensional CFT, Virasoro, minimal models, modular invariance, Weyl anomaly | deferred-special | Future two-dimensional CFT/CFT special volume | Must be developed properly later with rigorous representation and modular assumptions. |
| pp. 154--170, four-dimensional superconformal field theory, \(N=4\) SYM | deferred-special | Future supersymmetric QFT volume | Do not rush into this from the core CFT chapters. |
| pp. 171--185, large-\(N\) expansion and spin chains | deferred-special | Future large-\(N\)/integrability/special-structures volume | Keep out of the current core unless a later architecture decision changes. |

## Immediate High-Priority Blocks

| Source block | Current status | Control file |
| --- | --- | --- |
| 253a pp. 43--51, derivative interactions and measure/counterterms | certified after 2026-05-22 derivative-interaction source/figure audit | `planning/build_audits/2026-05-22_derivative_interactions_measure_counterterms.md`; `planning/chapter_dossiers/volume_i/chapter05_euclidean_correlators_gaussian_perturbation.md` |
| 253b pp. 71--80, generating functionals and 1PI effective action | certified after 2026-05-22 1PI source/figure audit | `planning/build_audits/2026-05-22_1pi_effective_action_source_figures.md`; `planning/chapter_dossiers/volume_ii/chapter09_generating_functionals_1pi_effective_action.md` |
| 253b pp. 97--110, 1PI RG | certified after 2026-05-22 1PI RG source/figure audit | `planning/build_audits/2026-05-22_1pi_rg_source_figures.md`; `planning/chapter_dossiers/volume_ii/chapter12_1pi_renormalization_group.md` |
| 253b pp. 147--156, Wilsonian effective actions and Polchinski flow | certified after 2026-05-22 Wilsonian source/figure audit | `planning/build_audits/2026-05-22_wilsonian_effective_actions_source_figures.md`; `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md` |
| 253b pp. 182--201, QCD beta function | certified after ordinary-rule figure audit and background-field derivation audit | `planning/build_audits/2026-05-22_qcd_beta_background_field_derivation.md`; `planning/build_audits/2026-05-22_ordinary_yang_mills_feynman_rules.md` |
| 253b pp. 202--210, Banks--Zaks and Wilson-loop/DIS diagnostics | certified after infrared/DIS figure audit | `planning/build_audits/2026-05-22_qcd_ir_dis_block.md`; `planning/chapter_dossiers/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_dis.md` |
| 253b pp. 211--225, chiral anomaly contact terms | certified after chiral-anomaly contact-term figure audit | `planning/build_audits/2026-05-22_chiral_anomaly_contact_terms.md`; `planning/chapter_dossiers/volume_ii/chapter20_chiral_axial_anomalies.md` |
| 253b pp. 226--257, global anomalies, SSB, pions, WZW, and chiral perturbation theory | certified after 2026-05-22 end-to-end source/figure audit | `planning/build_audits/2026-05-22_global_anomalies_ssb_pions.md`; `planning/chapter_dossiers/volume_ii/chapter21_global_anomalies_ssb_pions.md` |

## Audit Requirements

- For 1PI material, verify that the Legendre transform, background-field
  tadpole-cancellation picture, convexity of the exact Euclidean effective
  action, and relation between exact 1PI vertices and connected functions are
  all present with correct hypotheses.
- For 1PI RG, verify that the scale-dependent field normalization,
  symmetric-subtraction coupling, nearby-scale comparison, logarithmic
  consistency, Callan--Symanzik derivation, and scheme-dependence formula are
  all present and not collapsed into textbook formulas.
- For Wilsonian RG, verify the smooth cutoff covariance, source-supported
  generating functional equality, covariance split, shell field integral,
  Wilson--Polchinski equation, irrelevant-coupling slaving, and
  continuum-limit construction.
- For gauge dynamics, retain the separation between gauge-fixed variables,
  BRST cohomology, physical states, gauge-invariant local operators, Wilson
  lines, and nonlocal confinement diagnostics.
- For QCD beta function, retain background-field covariance and determinant
  coefficient audit; colored gauge-fixed fields must not be assigned physical
  spectral decompositions.
- For pions, retain the chain from anomaly matching and symmetry breaking to
  the nonlinear sigma model, the low-energy scattering amplitude, the
  higher-derivative counterterms, mass spurions, and \(\pi^0\to2\gamma\).

## Next Pass

The next page-level audit should promote `mapped after repair` rows to
`certified` only after checking the handwritten PDF figures and derivations
against the compiled PDF.
For selected 253c, the core-covered material through OPE/crossing should be
audited now; the projective-lightcone, bootstrap, two-dimensional,
supersymmetric, and large-\(N\) blocks remain source obligations for later
special volumes, not omissions from the current core volumes.
