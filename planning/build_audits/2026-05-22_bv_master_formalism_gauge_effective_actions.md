# BV Master Formalism For Gauge Effective Actions

Date: 2026-05-22

Scope:
- Added the compiled BV master-formalism chapter in the gauge-theory volume.
- Removed the active placeholder status that treated BV as a future framework.

Files:
- `monograph/tex/volumes/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.tex`
- `monograph/tex/volumes/volume_iv/volume_iv_current.tex`
- `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`
- `planning/chapter_dossiers/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.md`

Content added:
- Field/antifield gradings, including parity and ghost-number assignments.
- BV antibracket with left/right variational derivatives.
- Classical master equation and proof that \(s_{\rm BV}=(S_{\rm BV},\cdot)\) is nilpotent.
- Minimal Yang--Mills BV action and the relation to the BRST transformations.
- Nonminimal sector, gauge-fixing fermion, and restriction to a Lagrangian submanifold.
- Regulator-dependent quantum master equation.
- 1PI master equation as the antifield form of the Slavnov--Taylor identity.
- Finite-dimensional BV pushforward proof preserving the quantum master equation, used as the regulated core of the Wilsonian BV identity.
- Counterterm, anomaly, and physical-operator classification by local BV cohomology.

Planning updates:
- Added a chapter dossier for the BV chapter.
- Updated the BRST dossier so BV is now the following compiled chapter rather than a deferred topic.
- Updated the architecture and dependency map to make future targets reducible/open gauge algebras, exact-RG realizations, and global BV integration-cycle issues.

Verification:
- `tools/build_monograph.sh` completed cleanly after resolving one overfull theorem statement.
- Rendered and inspected the actual BV chapter PDF pages, including the structural BV diagram and final logical-output page.
- `git diff --check` passed.
- Active scans for `BV.*later`, `later.*BV`, and common soft-phrase patterns in the new BV/BRST files returned no matches.

Residual boundaries:
- Reducible gauge symmetries and open algebras are identified but not developed in detail.
- The cutoff-dependent Wilsonian master equation is stated at the framework level; explicit exact-RG gauge implementations remain a later deepening target.
- Global BV integration cycles and Gribov-type questions remain outside this perturbative local chapter.
