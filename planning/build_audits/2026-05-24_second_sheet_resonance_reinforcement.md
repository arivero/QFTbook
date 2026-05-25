# Second-sheet resonance reinforcement

## Scope

- `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`
- `planning/chapter_dossiers/volume_ii/chapter04_resonances_dressed_propagators.md`

## Reason

The 253b source material on resonances emphasizes that the resonance pole is a
pole on the sheet reached by analytic continuation through the physical
two-particle cut, not a pole of the physical boundary value on the first sheet.
The manuscript already contained this content and a dedicated second-sheet
section.  This pass strengthened the opening of that section so the statement is
attached explicitly to connected stable-channel \(S\)-matrix kernels.

## Content Check

The revised text now states:

- after removing the identity term and overall momentum delta function,
  \(\mathcal M_{ab}^{\rm I}(s)\) denotes a connected stable-channel amplitude or
  partial-wave coordinate on the first sheet;
- the physical value is the upper-edge boundary value
  \(\mathcal M_{ab}^{\rm I}(s+i0)\);
- a resonance is a pole of the adjacent analytic germ
  \(\mathcal M_{ab}^{\rm II}\), reached through the unitarity cut;
- in the scalar model the adjacent denominator locally has
  \[
    F_{\rm II}(s)=M_R^2-s-iW(s)+O(g^4,g^2(s-M_R^2)),
    \qquad W(s)=\frac{g^2}{32\pi}\rho_1(s),
  \]
  explaining why the pole can sit below the real axis on the second sheet while
  no first-sheet pole exists there.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
