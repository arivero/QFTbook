# Issue #387 Resonance Sheet Figure Audit

GitHub issue #387 flagged the nonrelativistic \(E\)-plane resonance figure in
Volume II, Chapter 4.  The text correctly states that the physical amplitude is
the upper-boundary value on the first sheet and that the resonance pole below
the positive real axis is reached only after continuation through the cut to
the adjacent sheet.  The figure, however, made the first-sheet arrow approach
the cut too closely and could be read as crossing into the lower half-plane.

## Correction

The TikZ figure now separates the three pieces:

- a purple first-sheet path staying visibly above the positive real-energy
  cut, labelled as the first-sheet upper lip;
- a dashed continuation marker through the cut;
- a green second-sheet path beginning after that continuation and running on
  the lower lip toward the resonance pole.

This matches the later analytic statement that the pole
\[
  s_\ast=M_R^2-iM_R\Gamma_R+O(g^4)
\]
is not a first-sheet pole but lies on the adjacent sheet reached through the
\(\phi_1\phi_1\) threshold cut.

## Files Changed

- `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`
- `planning/chapter_dossiers/volume_ii/chapter04_resonances_dressed_propagators.md`
