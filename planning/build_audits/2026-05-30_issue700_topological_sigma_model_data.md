# Issue #700: Topological Sigma-Model Defining Data

## Target

Volume VIII, Chapter 6 was listed as a partial issue #700 gap: the chapter
defined mapping spaces, stable maps, Gromov-Witten functionals, and the small
quantum product, but the A-model and B-model frameworks themselves were not
aggregated as opening data.

## Edit

- Added `hyp:a-model-cohomological-sigma-datum` near the chapter opening.
  It collects the source Riemann surface, compact almost Kahler target,
  complexified Kahler weight, locally super-ringed field space, cohomological
  differential, localization section, virtual integration package, Novikov
  completion, and contact-term prescription.
- Added `hyp:b-model-cohomological-sigma-datum`, collecting the compact
  Calabi-Yau target, holomorphic volume form, locally super-ringed field
  space, Dolbeault polyvector complex, trace pairing, anomaly-free twist,
  regulated integration cycle, contact-term prescription, and
  Maurer-Cartan deformation complex.
- Rewrote the mapping-space and virtual-integration entry points to refer
  back to the new hypotheses.
- Updated the Chapter 6 dossier.

## Scope

The hypotheses do not construct the continuum A- or B-models.  They identify
the cohomological-QFT data from which the finite-dimensional
Gromov-Witten/B-model outputs should be derived once the construction problem
in `op:topological-sigma-model-continuum-qft` is solved.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh` (clean; `main.pdf` has 2677 pages)
