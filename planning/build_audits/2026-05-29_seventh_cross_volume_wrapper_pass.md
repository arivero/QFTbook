# Seventh Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: reviewed `claude_review.md`, the live open GitHub issue list, and the active issue #691 concern about trivial propositions, proof wrappers, and theorem-family statements whose substance is hidden in hypotheses.  This pass continues the end-to-end anti-wrapper audit; it does not exhaust #691.

## Demotions

The following theorem-family statements were demoted to worked prose because their former proof blocks were elementary identities, bookkeeping, or direct consequences of stronger cited hypotheses:

- `BV Stokes in a finite-cutoff Darboux chart`, in `volume_vii/chapter04_supersymmetric_wilsonian_schemes.tex`.
- `Large-time spectral extraction`, in `volume_ix/chapter07_phases_of_gauge_theories.tex`.
- `Four-dimensional parity-even Weyl anomaly`, in `volume_iii/chapter03_stress_tensor_weyl_structure_and_improvement.tex`.
- `Finite-dimensional invariant density`, in `volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- `Pseudoscalar-meson--baryon partial-wave quantum numbers`, in `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`.
- `Finite-cutoff stability of the local normal-ordered polynomial`, in `volume_xi/chapter02_constructive_scalar_models_os_data.tex`.
- `Cell averages approximate test functions`, in `volume_xi/chapter08_lattice_to_continuum_local_qft.tex`.

The removed labels were checked for stale references across `monograph/tex`, `planning`, and `tools`.

## Strengthened Proofs

The following retained statements were kept in theorem-family form but expanded because their mathematical content is substantive:

- `NS unitarity bound and chiral primaries`: corrected the equality condition for a general common-domain vector and separated it from the special NS-primary case.
- `Right-moving localization`: expanded the elliptic-genus proof using the Ramond zero-mode pairing and supertrace cyclicity.
- `Stationary covariance of the linear SPDE`: added the stationary Ornstein--Uhlenbeck construction, finite-cutoff Parseval identity, and negative-Sobolev convergence estimate.
- `BPZ differential equation`: added the contour-deformation derivation of the Ward identity before inserting the null vector.
- `BV pushforward preserves the quantum master equation`, plus the parallel BV pushforward results in Volumes II and VIII: made the high/low BV Laplacian split and BV-Stokes boundary term explicit.
- `Soft and collinear continuity of smeared energy flow`: expanded the argument in terms of finite-energy calorimetric measures and support-diameter estimates.
- Scalar and symmetric-traceless conformal unitarity bounds: expanded the radial-adjointness, Gram-matrix, null-radical, and separated-point conservation arguments.
- Four-dimensional conformal-collider inequalities: expanded the helicity decomposition and positivity argument.
- `Special-conformal invariance from radial spectrum positivity`: added the domain and spectral-theorem argument rather than treating the conformal generators formally.

## Guardrails

`tools/audit_theorem_form.py` now rejects recurrence of the seven demoted theorem-family titles above.

## Verification

Commands run:

- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- stale-label `rg` scan for all removed labels
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

Results:

- All audits passed after fixing one negative-scope phrase and one stale theorem label introduced during the pass.
- Full monograph build passed with log scan clean.
- Built PDF: `monograph/tex/main.pdf`, 2583 pages.

## Remaining Queue

The short-proof heuristic is only a triage queue, not a defect count.  This pass reduced the `<=105`-word immediate-proof queue from 37 candidates to 18 candidates.  The remaining candidates require manual reading in subsequent passes because short does not automatically mean trivial: several are likely genuine compact arguments, while others may still need demotion or expansion.
