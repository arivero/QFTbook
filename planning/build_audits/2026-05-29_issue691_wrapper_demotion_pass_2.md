# Issue 691 theorem-form audit: wrapper demotion pass 2

Date: 2026-05-29.

This pass continued the end-to-end anti-wrapper audit for theorem-family
statements whose proof content is a convention-sensitive calculation,
finite-dimensional check, or consequence of a deliberately strong hypothesis.

Actions taken:

- Demoted worked perturbative calculations in Volume I from proposition/proof
  form to paragraphs: the scalar tadpole, sunset, pole-shift bookkeeping,
  tree-level \(\phi^4\) LSZ amplitude, representative QED Feynman rules, and
  tree-level Compton hard kernel.
- Demoted supersymmetric and integrability calculations whose force comes from
  explicit inputs rather than a theorem-level statement: pure-SYM instanton
  zero-mode ledgers, the ADS one-instanton test, Konishi leading wrapping
  coefficient, and weak-QSC one-loop dimension extraction.
- Demoted finite-cover, controlled-approximation, and stochastic-counterterm
  calculation wrappers that had been written as corollaries/propositions or
  proof environments.
- Moved the Wightman reconstruction interpretive prose to follow the actual
  reconstruction proof, so the theorem-proof structure is immediate and
  unambiguous.
- Tightened `tools/audit_theorem_form.py` so the demoted titles are rejected if
  they reappear as theorem-family statements, and so unnamed proofs must attach
  directly to theorem-family environments while proofs after definitions,
  controlled approximations, or quoted theorems are rejected.

Manual judgment notes:

- Short proofs were not demoted merely for being short.  For example, the
  large-time spectral extraction lemma, Noether identity, BV Stokes lemma, and
  free-field covariance/microcausality statements remain theorem-family
  statements because their hypotheses and conclusions are structural and used
  later.
- The local \(P\)-\(Q\) bridge issue had already been addressed before this
  pass: the bridge algebra is now a paragraph after the explicit local bridge
  assumption, with the global analytic existence problem stated separately.

Verification commands for this pass:

- `python3 tools/audit_theorem_form.py`

Full text/build audits are to be run before checkpointing this batch.
