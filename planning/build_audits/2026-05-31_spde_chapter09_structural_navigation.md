# SPDE Chapter 09 Structural Navigation Pass

Date: 2026-05-31

Scope:
- `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`
- `planning/chapter_dossiers/volume_xi/chapter09_stochastic_quantization_singular_spde.md`
- `claude_review.md`

Purpose:
- Address the #701 C3 finding that Volume XI Chapter 09 had two
  mathematically dense sections spanning thousands of lines without
  subsection-level navigation.

Editorial change:
- The Da Prato--Debussche section now has subsections for local product and
  fixed-point estimates, energy compactness, invariant laws and tightness,
  regulator/OS assembly, and the three-dimensional obstruction.
- The regularity-structures section now has subsections for models and
  reconstruction, random model convergence and finite-chaos coordinates,
  multiscale local subtractions, finite-sector coordinate-to-model
  convergence, and nonlinear negative-coordinate shell bounds.

Mathematical status:
- No theorem, lemma, proposition, corollary, displayed equation, or label used
  by the manuscript was changed for mathematical content.
- This is a structural pass only; it makes existing proof infrastructure
  findable without adding wrappers or altering hypotheses.

Verification:
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
