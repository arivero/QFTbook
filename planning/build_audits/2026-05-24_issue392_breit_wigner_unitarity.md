# Issue #392: Breit-Wigner elastic unitarity

## Scope

- `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`
- `planning/chapter_dossiers/volume_ii/chapter04_resonances_dressed_propagators.md`

## Correction

The resonance chapter now separates two facts that had been compressed into an
ambiguous approximate equality.

1. The approximation is the construction of a single-channel elastic resonance
   model: keep the angle-independent resonant \(s\)-channel exchange, omit
   smooth background and crossed-channel pieces, and use the elastic width
   function \(W(s)=g^2\rho_1(s)/(32\pi)\).
2. Once this model has been chosen, the Breit--Wigner factor is the exact
   elastic-unitary rational function
   \[
     S_0^{\rm BW}(s)=
     {M_R^2-s+iW(s)\over M_R^2-s-iW(s)}.
   \]

For real \(s\) in the elastic interval, \(W(s)\) is real and the numerator is
the complex conjugate of the denominator, so \(|S_0^{\rm BW}(s)|=1\) exactly.
Corrections from background, crossed-channel, inelastic, and higher-order
effects are corrections to the single-channel model, not failures of the
Breit--Wigner factor to be unitary.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
