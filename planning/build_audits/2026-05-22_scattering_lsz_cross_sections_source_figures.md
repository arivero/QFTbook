# Scattering, LSZ, Cross Sections Source/Figure Audit

Date: 2026-05-22.

## Source Block

- Handwritten source: `references/253a lectures 2022.pdf`, pp. 113--145.
- Local source transcription: `transcription/tex/253a/foundations.tex`, roughly
  lines 4550--6075.
- Source visual trace rendered to:
  `monograph/tex/build/source_visual_trace/253a_trace-113.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-145.png`.

## Manuscript Files Updated

- `monograph/tex/volumes/volume_i/chapter12_haag_ruelle_scattering_theory.tex`
- `monograph/tex/volumes/volume_i/chapter13_lsz_reduction_and_the_s_matrix.tex`
- `monograph/tex/volumes/volume_i/chapter14_cross_sections_partial_waves_and_unitarity.tex`
- `planning/chapter_dossiers/volume_i/chapter12_haag_ruelle_scattering_theory.md`
- `planning/chapter_dossiers/volume_i/chapter13_lsz_reduction.md`
- `planning/chapter_dossiers/volume_i/chapter14_cross_sections_unitarity.md`
- `planning/source_inventory/253a_253b_no_skip_coverage_register.md`

## Content Certified

- The scattering block now begins with a nonperturbative Hilbert-space
  construction of in/out states and the \(S\)-operator before LSZ and before
  any perturbative scattering-amplitude interpretation.
- The Haag--Ruelle chapter now includes the point-field smearing form from the
  notes:
  - the one-particle projection of \(\hat\phi_f\Omega\);
  - the translated packet \(f^{(T)}\);
  - the propagation kernel \(K(\vec x;T)\);
  - group-velocity motion of the spacetime support;
  - the two-packet four-point/cluster Cauchy argument;
  - generalized in/out momentum kernels with symmetrized delta normalization.
- The LSZ chapter now includes the large-time oscillatory derivation of
  external residues, the incoming/outgoing pole prescriptions, the
  disconnected two-point identity contribution, the relation between
  \(\delta\)-normalized amplitudes and the invariant amplitude, and the
  connected \(S\)-kernel cluster decomposition.
- The cross-section chapter now includes the regulated sharp-momentum
  delta-square calculation, \(VT\) and \(V/(2\pi)^d\) factors, the direct
  identical \(2\to2\) phase-space integration, the COM partial-wave state
  normalization, and the reconstruction of the sharp-momentum partial-wave
  kernel from \(S_\ell(E)-1\).

## Figure and Rendering Check

- Manuscript render checked from:
  `monograph/tex/build/scattering_lsz_cross_sections_render_phys-112.png`
  through `monograph/tex/build/scattering_lsz_cross_sections_render_phys-137.png`,
  plus updated partial-wave pages rendered under
  `monograph/tex/build/scattering_lsz_cross_sections_render_phys2-131.png`
  through `monograph/tex/build/scattering_lsz_cross_sections_render_phys2-139.png`.
- Figures checked:
  - isolated mass-shell and continuum threshold schematic;
  - asymptotically separated velocity-support wave-packet schematic;
  - Haag--Ruelle wave-operator diagram;
  - LSZ external-amputation diagram;
  - connected \(S\)-kernel decomposition diagram;
  - invariant flux/cross-section schematic.
- No handwritten PDF page is embedded in the manuscript.  Source figures are
  rewritten as TikZ diagrams or as explicit displayed equations.

## Checks Run

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

The build completed cleanly and wrote
`monograph/tex/main.pdf`.
