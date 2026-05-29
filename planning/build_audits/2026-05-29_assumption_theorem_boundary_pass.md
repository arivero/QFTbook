# Assumption/theorem boundary audit pass

Date: 2026-05-29.

This pass examined theorem-family statements whose conclusions explicitly
depend on assumptions or hypotheses.  The point was not to demote every
conditional result, but to separate three cases:

- genuine theorem/proposition content proved from explicit hypotheses;
- worked algebraic or coordinate derivations better written as paragraphs;
- statements where the hard content is the hypothesis itself and must not be
  disguised as a theorem conclusion.

Changes made:

- In the radial quantization chapter, the radial-completeness clause of
  `hyp:radial-reconstruction-data` no longer appeals forward to the
  operator-from-state theorem.  It now states the actual load-bearing
  existence assertion: every finite-energy eigenvector is assumed to admit
  local radial boundary-value data.  New prose explains that reflection
  positivity and the radial spectrum alone give an injection from local
  operators to states, while surjectivity requires this extra local
  boundary-value hypothesis.
- The theorem `thm:operator-from-state-radial-boundary-value` now proves only
  the construction from specified local radial boundary-value data.  The
  former converse sentence, which merely restated radial completeness, was
  moved to prose after the proof.
- The massive-SQCD mass-source/Konishi identities were demoted from
  proposition/proof form to a worked paragraph, since the derivation is the
  finite-dimensional envelope theorem plus the already assumed Wilsonian
  chiral-coordinate system.
- The BES equation from the large-spin ABA was demoted from proposition/proof
  form to a worked paragraph, since it is a convention-sensitive derivation
  from the assumed large-spin ABA scaling regime rather than an independent
  theorem about the gauge theory.
- `tools/audit_theorem_form.py` now rejects reintroduction of the two demoted
  titles as theorem-family statements.

Manual review notes:

- The Cook estimate form of Haag--Ruelle limits, isolated bound-state LSZ pole
  factorization, primitive Wightman tube-domain theorem, kinematic annihilation
  pole, Euclidean radial OPE convergence, conformal-block existence/uniqueness,
  Froissart--Martin finite-order statements, BPHZ--Wilsonian matching theorem,
  finite-regulator Euclidean convexity theorem, topological-sector zero-mode
  selection rule, and \(\Phi^4_2\) stochastic assembly theorem were read in
  context during this pass.  They remain theorem-family statements because
  their proofs use the hypotheses to derive structural consequences rather than
  merely restating the hypotheses.

Verification run before checkpoint:

- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh` (clean build and log scan; 2577-page PDF)
