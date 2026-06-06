# Issue #597: Instanton Chirality-Source Gate

## Scope

This pass strengthens the hard instanton amplitude calculation in Volume II,
Chapter 20D by adding the finite zero-mode chirality-source selection rule
behind the massless 't Hooft vertex.  It sits after the two-flavor
`det(M+B)` coordinate and before the hard four-fermion benchmark, so the
reader must pass through Berezin saturation and anomalous chirality flow
before the coefficient is interpreted as a physical instanton amplitude.

This is a physics-depth pass, not an ADHM or moduli-space expansion.  It does
not add process language to the monograph.  The new proposition keeps the
topological sector, source chirality, mass/source coordinate, and zero-mode
determinant in the same finite calculation.

## Companion Evidence

`calculation-checks/instanton_physical_amplitude_architecture_checks.py` now
contains `check_chirality_source_selection_gate()`.  The finite check uses
exact two-by-two determinant blocks and explicit source-slot axial weights.

The check verifies:

- the \(Q=1\) hard source coordinate has axial weight \(-2N_f\);
- the \(Q=-1\) conjugate coordinate has the opposite axial weight;
- a nonzero determinant in the conjugate chirality block is still zero in the
  \(Q=1\) zero-mode gate;
- chirality-balanced four-source data has zero axial weight and is not the
  \(Q=1\) 't Hooft vertex;
- unlabeled four-source determinant sums mix instanton and anti-instanton
  chirality sectors;
- a mass-assisted coordinate can replace one matched zero-mode source pair but
  is not the massless hard four-source amplitude.

This companion checks the finite Berezin/source-selection identity and its
negative controls.  It does not compute the continuum determinant constant,
prove convergence of the instanton size integral, or establish a Lorentzian
scattering theorem.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "directive|claude_review|GitHub|issue #|monitor|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean, producing `monograph/tex/main.pdf` at
  3467 pages.
