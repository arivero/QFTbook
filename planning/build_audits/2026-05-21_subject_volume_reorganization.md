# Subject Volume Reorganization

Date: 2026-05-21

## Scope

This pass reorganized the compiled manuscript by subject matter rather than
semester-like sequence.

The active compiled volumes are now:

1. Foundations of Local Quantum Field Theory
2. Particles, Scattering, and Analyticity
3. Renormalization, Effective Field Theory, and Critical Phenomena
4. Gauge Theory, Infrared Structure, and Anomalies
5. Conformal Field Theory

The former standalone nonperturbative-framework material was redistributed:
Wightman, AQFT, and superselection material now enter Volume I; mathematical
Haag--Ruelle scattering now enters Volume II; Osterwalder--Schrader
reconstruction appears in Volume I after Euclidean Green functions.  The CFT
material was moved to a new active Volume V wrapper.

Reader-facing hard-coded chapter-number references were replaced by
label-based references after the reorganization.

## Planning Updates

- Rewrote the master architecture to record the twelve-volume long-term
  program.
- Updated project decisions to record subject-matter volume boundaries and
  the decision that nonperturbative frameworks belong in the foundation.
- Updated the repository README and planning README with the active volume
  architecture.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- Deferred-topic scan over `monograph/tex/volumes`: clean.
- Hard-coded chapter-number prose scan over reader-facing TeX: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 325 pages.
