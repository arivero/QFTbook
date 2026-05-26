# Issue 588 Supersymmetric Localization Rigor Pass

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Worktree: `/Users/xiyin/QFT_susy_gauge_dynamics_localization`

## Scope

This pass addresses the compact-space supersymmetric localization component of
issue #588.  It does not address string compactification; issue #590 was
closed separately as not planned after Xi clarified that superstring theory is
outside the QFT monograph.

## Source Review

- Read the common handoff contract, handoff README, SUSY
  gauge-dynamics/localization handoff, strict writing harness, `claude_review.md`,
  and the open issue text for #588.
- Corrected the SUSY handoff so that #590 is no longer listed as a lane target
  and so that "compactification" in the localization lane is explicitly
  field-theoretic or moduli-space compactification, not string
  compactification.
- Consulted local arXiv e-print payloads stored in
  `references/susy_gauge_dynamics_localization/issue588_localization/`:
  Pestun's round-\(S^4\) localization source, Kapustin-Willett-Yaakov's
  round-\(S^3\) Chern-Simons-matter localization source, and
  Hama-Hosomichi-Lee's double-sine/squashed-\(S^3\) source.

## Files Changed

- `planning/agent_handoffs/03_susy_gauge_dynamics_localization.md`
- `monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex`
- `planning/chapter_dossiers/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.md`
- `calculation-checks/susy_localization_matrix_checks.py`
- `calculation-checks/README.md`
- `references/susy_gauge_dynamics_localization/issue588_localization/README.md`
- `references/susy_gauge_dynamics_localization/issue588_localization/eprints/*`

## Mathematical Content Added

- Defined clean fixed loci and normal \(Q\)-complexes for finite-dimensional
  localization, with zero modes separated from one-loop determinants.
- Expanded the \(S^4\) localization datum: off-shell vector multiplet fields,
  conformal Killing spinor data, the \(Q^2\) decomposition into isometry,
  gauge, \(R\)-symmetry, and flavor terms, and the bulk fixed-locus statement
  leading to the Cartan integral.
- Made the north/south pole instanton factors part of the localization datum,
  not an informal afterthought.
- Proved convergence and logarithmic derivative formulae for the chapter
  \(H\)-function and stated the Barnes-\(G\) comparison including the local
  quadratic counterterm convention.
- Defined the double sine \(s_b\), related it to the round-\(S^3\) \(\ell\)
  function, stated the \(R=1/2\) conjugate-pair reflection identity, and made
  the pole hyperplanes and JK-type contour choice explicit.

## Calculation Checks

- Extended `calculation-checks/susy_localization_matrix_checks.py` with:
  - finite-product checks for the \(S^4\) \(H\)-function logarithmic
    derivative and evenness;
  - finite double-sine reflection checks;
  - the round-\(S^3\) chiral pole-location convention.
- Existing checks for the trace-delta \(S^4\) Gaussian, \(U(1)\) Gaussian
  integral, \(U(1)_k\) Fresnel completion, and conjugate-chiral-pair integral
  were retained.

## Verification

- `python3 calculation-checks/susy_localization_matrix_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed, including the Wolfram backend.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: passed.
- Log scan for undefined references, citation warnings, TeX fatal errors, and
  overfull/underfull boxes: clean.
- `pdfinfo monograph/tex/main.pdf`: 1536 pages.

## Remaining Obligations

Issue #588 remains open.  Further work remains on the full Seiberg-Witten
derivation-rigor pass, the broader \(N=4\) SCFT/operator-spectrum material, and
additional protected-observable localization applications.
