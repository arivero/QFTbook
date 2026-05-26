# Volume X Hydrodynamic Fluctuations Deepening Audit

## Scope

This pass addresses the later-volume thinness directive for Volume X,
Chapter 11.  The chapter is rewritten from a brief sketch into a
derivation-level treatment of stochastic hydrodynamic fluctuations,
Schwinger-Keldysh noise normalization, hydrodynamic long-time tails, cutoff
separation, and stress-tensor noise positivity.

## Edits

- Rewrote
  `monograph/tex/volumes/volume_x/chapter11_hydrodynamic_fluctuations_long_time_tails.tex`.
- Fixed the convention that \(d\) is the number of spatial dimensions and
  aligned diffusion signs with Volume X Chapters 5 and 6.
- Defined static hydrodynamic covariance in the chemical-potential
  susceptibility convention, including the factor \(T\chi\).
- Derived the symmetrized diffusion correlator from the stochastic current
  noise and checked its equal-time limit.
- Displayed the classical hydrodynamic fluctuation-dissipation relation with
  the retarded density response kernel.
- Reconnected the Langevin equation to the local SK diffusion action through
  the Hubbard-Stratonovich transformation.
- Developed the quadratic hydrodynamic current vertex and the Gaussian
  time-domain long-time-tail calculation.
- Derived the basic frequency-domain loop integral and its nonanalytic
  infrared part, including the \(d=1,2,3\) cases and the explicit \(d=3\)
  cutoff split.
- Distinguished cutoff-dependent local transport renormalization from the
  universal nonanalytic low-frequency term.
- Added the stochastic stress-tensor noise tensor and proved positivity by
  trace/traceless decomposition.
- Added the momentum-tail mechanism from the convective stress tensor.
- Added `calculation-checks/hydrodynamic_long_time_tail_checks.py` and
  documented it in `calculation-checks/README.md`.
- Rewrote the Volume X Chapter 11 dossier.
- Widened the section-number box in the table of contents so three-digit
  chapter numbers with two-digit section numbers fit cleanly.

## Verification

- `python3 calculation-checks/hydrodynamic_long_time_tail_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed after the table-of-contents width fix.
- `pdfinfo monograph/tex/main.pdf` reports 1327 pages.
