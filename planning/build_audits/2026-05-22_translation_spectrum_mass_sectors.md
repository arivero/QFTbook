# Translation Spectrum and Mass Sectors Pass

Date: 2026-05-22.

Development pass:

- Added the joint spectral-measure formulation for translation generators in
  the early relativistic quantum-structure chapter.
- Defined energy-momentum spectral support of a vector, the invariant mass
  operator by functional calculus, and mass-range projections.
- Defined isolated positive-energy particle shells as spectral subspaces of
  the physical Hilbert space.
- Connected this early spectral definition to the later Kallen--Lehmann and
  Haag--Ruelle constructions.
- Added and visually checked a translation-spectrum figure showing the vacuum
  atom, an isolated massive shell, and a continuum threshold.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- active-volume orphan chapter scan
- `tools/build_monograph.sh`
- rendered page check for the new translation-spectrum figure

Result:

- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.
