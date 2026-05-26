# Build Audit: Issue #607 Planar N=4 Integrability Depth Pass

## Scope

- Branch: `codex/planar-n4-integrability`.
- Issue: #607, with cross-cutting relevance to #606.
- Files edited:
  - `monograph/tex/volumes/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.tex`
  - `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
  - `monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex`
  - `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
  - `planning/chapter_dossiers/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.md`
  - `planning/chapter_dossiers/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.md`
  - `planning/chapter_dossiers/volume_vii/chapter14_planar_n4_mirror_tba_y_system.md`
  - `planning/chapter_dossiers/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.md`
  - `calculation-checks/planar_n4_integrability_checks.py`

## Source Spine Checked

- `planning/agent_handoffs/00_common_agent_contract.md`
- `planning/agent_handoffs/README.md`
- `planning/agent_handoffs/01_planar_n4_integrability_depth_pass.md`
- `planning/12_strict_writing_harness.md`
- `claude_review.md`
- GitHub issues #607, #606, and #608 for scope exclusion.
- Stringbook source:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, especially
  `integrabilitychapter`, mirror TBA/QSC, Konishi wrapping, and
  Maldacena-Wilson/cusp/Bremsstrahlung sections.
- Stringbook calculation notebooks located:
  - `/Users/xiyin/ResearchIdeas/stringbook/codes/su(2|2) spin chain.nb`
  - `/Users/xiyin/ResearchIdeas/stringbook/codes/BES equation.nb`
  - `/Users/xiyin/ResearchIdeas/stringbook/codes/mirror TBA and wrapping corrections.nb`

## Full-Draft Orientation

- Reviewed the compiled monograph table of contents and volume include map
  after the forced build.
- Reviewed `frontmatter_volume_dependency_guide.tex` to keep the lane aligned
  with the monograph's dependency order.
- Reviewed the relevant cross-volume support chapters:
  - Vol VI algebraic Bethe ansatz and nested Bethe-Yang chapters, used here
    only as algebraic background;
  - Vol VI mirror-channel TBA chapter, used to keep the mirror/TBA language
    distinct from planar N=4 mirror kinematics;
  - Vol VII supersymmetric localization chapter, used for the status boundary
    of the Bremsstrahlung/localization formula;
  - Vol IX line-operator chapter, used for the general defect/Wilson-line
    definition discipline.

## Mathematical Additions

- Added planar single-trace inner product and spectral-datum definition.
- Added two-site scalar mixing proposition for the one-loop `SU(2)` sector.
- Added BMN scaling check, `su(2|2)_c` matrix-amplitude structure, dressing
  phase status ledger, nested-root first step, bound-state dispersion, and
  large-spin cusp scaling data.
- Added mirror-sheet status, Hirota-to-Y-system derivation, and Konishi
  four-loop wrapping coefficient assembly.
- Added QSC asymptotic coefficient constraints, small-spin Bessel-ratio
  expansion, and Maldacena-Wilson/cusp/Bremsstrahlung interface.

## Continuation Pass

- Added the full one-loop `SO(6)` scalar density `K+2I-2P` and its
  holomorphic `SU(2)` reduction.
- Added an explicit convention ledger aligning the monograph with the
  stringbook integrability convention `h=g=sqrt(lambda)/(4 pi)` and warning
  about reciprocal scalar-factor conventions in the literature.
- Corrected the Zhukovsky energy formula to
  `H=-1-2ig(x^+-x^-)=1+2ig(1/x^+-1/x^-)` and added a proof from the
  physical branch.
- Added physical-branch Zhukovsky map data, large-`u` expansion, cut
  reciprocal boundary values, shifted branch-point crossing paths, Janik
  scalar crossing, and the BES `chi(x,y)` contour-integral representation
  with sheet caveats.
- Derived the mirror bound-state dispersion from double Wick rotation and
  recorded the mirror-kernel datum and mirror Bethe-string node inventory.
- Added analytic Y-system data: shifted strips, meromorphy domains,
  discontinuities, and exact-root regularity conditions.
- Added QSC Pfaffian normalization, a rank-two discontinuity consistency
  lemma, the dual `Qomega` system, an explicit Konishi Baxter polynomial, and
  the scalar hexagon factor with crossing-path caveat.

## Calculation Checks

`calculation-checks/planar_n4_integrability_checks.py` now checks:

- `SO(6)` trace-operator reduction to the holomorphic `SU(2)` sector;
- one-magnon XXX finite-difference normalization;
- Konishi one-loop cyclic roots;
- explicit Konishi Baxter polynomial identity;
- central-extension dispersion;
- Zhukovsky defining equation, large-`u` expansion, cut reciprocal boundary
  values, `x^pm` relation, and corrected energy formula;
- non-invariance of the stringbook-orientation crossing RHS under a naive
  sheet-free `x -> 1/x` substitution;
- weak-coupling dispersion expansion;
- BMN scaling limit;
- bound-state shortening dispersion;
- mirror double-Wick dispersion;
- Konishi four-loop wrapping arithmetic;
- planar Bremsstrahlung weak-series Bessel-ratio coefficients through four
  displayed orders;
- local Hirota-to-Y-system algebra.
- QSC `Pmu` Pfaffian preservation under the rank-two discontinuity update.

## Status

This is a substantive partial depth pass.  It does not close #607 because the
handoff asks for all four chapters to be expanded beyond stringbook depth with
more complete self-contained derivations, including more comprehensive
analytic-continuation checks.  The issue should remain open.
