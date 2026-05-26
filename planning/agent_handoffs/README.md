# Parallel Agent Handoff Packet

This directory contains handoff notes for agents working in parallel on
independent regions of the QFT monograph.  Each handoff is a work package,
not a complete specification of the final chapter.  The common contract in
`00_common_agent_contract.md` is binding for all packages.

## Active Parallel Lanes

- `01_planar_n4_integrability_depth_pass.md`: Volume VII chapters 12--15,
  issue #607, planar N=4 SYM integrability and stringbook-depth correction.
- `02_2d_cft_liouville_bcft_nlsm.md`: Volume V, issues #600--#602, 2D CFT,
  Liouville, BCFT, sigma models, orbifolds, twist fields, and conformal nets.
- `03_susy_gauge_dynamics_localization.md`: Volume VII, issues #588, #603,
  #605, and related SUSY gauge dynamics and localization.
- `04_solitons_monopoles_instantons.md`: Volume II / VII background for
  issues #597 and #592, classical solitons, monopoles, instantons, ADHM, and
  instanton calculus.
- `05_light_front_large_n_solvable_models.md`: issue #596, light-front
  quantization, the 't Hooft model, and 3D Chern-Simons matter in the
  't Hooft limit.
- `06_gauge_observables_energy_correlators_charged_sectors.md`: issues #519,
  #526, #527, and #528, energy correlators, IR-safe detector observables,
  jets when rigorously formulated, and charged-sector Haag-Ruelle/LSZ.
- `07_wilsonian_rg_resurgence_nonperturbative_fixed_points.md`: issues #503
  and #505, nonperturbative Wilsonian RG, rigorous fixed-point status,
  Borel-Laplace theory, Lefschetz thimbles, and renormalons with precise
  status.
- `08_tqft_donaldson_seiberg_witten.md`: issue #569, Witten-Donaldson theory
  and the Donaldson/Seiberg-Witten comparison in the cohomological TQFT
  volume.

## Coordination Rule

Each agent should work on one lane at a time, preferably on a branch named
`codex/<lane-short-name>`.  Do not edit the active SPDE files for issue #608
unless explicitly taking over that lane:

- `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`
- `planning/chapter_dossiers/volume_xi/chapter09_stochastic_quantization_singular_spde.md`

When a lane modifies shared planning files or calculation-check runners, keep
those edits minimal and mention them in the final report.
