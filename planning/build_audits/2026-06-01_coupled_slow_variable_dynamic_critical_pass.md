# Coupled Slow-Variable Dynamic-Critical Pass

## Scope

Issue #703 statmech-to-QFT absorption, Volume X Chapter 10.

## Edit

Added a finite-regulator treatment of coupled slow-variable stochastic data
beyond Model A/B.  The new section defines the finite Ito datum
`dy=(R-M grad F)dt+sqrt(2T) sigma dB`, separates dissipative mobility from
reversible drift, gives the finite divergence condition for Gibbs
stationarity, characterizes exact conserved covectors, and explains Model C/H
labels as hypotheses about retained slow variables and continuum scaling
limits rather than theorem labels.  The finite MSRJD action for the coupled
datum is derived from the chapter's finite Gaussian Fourier identity.

## Calculation Check

`calculation-checks/nonequilibrium_open_system_checks.py` now verifies the
constant-antisymmetric reversible-current identities and a Model C-style
conserved-density block mobility.

## Verification

Passed:

- `python3 calculation-checks/nonequilibrium_open_system_checks.py`
- `python3 -m py_compile calculation-checks/nonequilibrium_open_system_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` gives `Pages: 2799`
