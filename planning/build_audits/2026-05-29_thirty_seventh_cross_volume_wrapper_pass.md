# Thirty-seventh cross-volume theorem-form audit

Scope: continuation of GitHub issue #691 after commit `5c38a5d2`.
I regenerated the compact-proof queue from the current manuscript and read
the next shortest statement-proof units in context.  The first band no longer
contained obvious one-line algebra wrappers; the cases below were retained in
theorem-family form because their statements carry reusable mathematical
content, but their proofs were too compressed for the monograph's standard.

## Proofs expanded

- `lem:fredholm-canonical-coefficients`: expanded the Fredholm-minor proof
  through exterior powers, finite-rank Cauchy--Binet, trace-norm
  approximation, and the ABJM coefficient identification.
- `prop:largest-time-identity`: expanded the largest-time cancellation by
  working chamberwise away from equal-time hyperplanes, pairing circlings at
  the unique largest-time vertex, and tracking Wightman line factors.
- `prop:lattice-fermion-finite-rp-criterion`: expanded the finite Grassmann
  reflection-positivity argument with the ordered monomial basis, reflected
  Berezin pairing, and sum-of-squares structure.
- `prop:spde-invariant-measure-limit`: expanded the weak-limit invariance
  proof by separating tightness, high-probability compact convergence,
  Markov contraction, and weak convergence of both \(f\) and \(P_tf\).
- `prop:dw-triangulation-independence`: expanded the Dijkgraaf--Witten
  Pachner-move proof in terms of flat labels as simplicial maps to \(BG\),
  the \((D+1)\)-simplex coboundary, and telescoping coboundary factors.
- `prop:invariant-state-unitary-implementation`: expanded the GNS
  implementation proof, including quotient well-definedness, isometry,
  inverse, group law, strong continuity, and uniqueness.
- `prop:su2-bogomolny-bound`: expanded the monopole lower-bound proof with
  the square completion, Bianchi surface term, asymptotic \(U(1)\) reduction,
  and primitive magnetic cocharacter normalization.
- `prop:time-ordered-extension-contact-term-freedom`: expanded the support
  and normal-form proof for contact-term freedom of time-ordered extensions.
- `prop:loop-rotation-pinch-obstruction`: expanded the contour-deformation
  proof, distinguishing Euclidean external energies from Landau pinch
  obstruction at the sunset threshold.
- `prop:coulomb-slice-atlas`: expanded the Coulomb-slice proof through the
  Sobolev Hilbert-manifold setup, elliptic decomposition, explicit inverse
  for the longitudinal part, and Banach inverse-function theorem.
- `prop:trace-class-estimate-one-channel-sewing`: expanded the trace-class
  sewing estimate with trace-norm convergence, singular-value control, and
  basis independence.
- `thm:energy-correlator-polynomial-density`: expanded the compactness,
  point-separation, Stone--Weierstrass, and factorized-kernel identification
  steps.

No theorem-family demotion was made in this pass.  The audited statements
above were not decorative wrappers; they required fuller proofs rather than
removal of theorem-family status.

## Queue status after edits

- theorem-family counts: theorem 94, proposition 367, lemma 29, corollary 10;
  total 500.
- proof environments: 495.
- immediate compact-proof queue: zero entries at or below 170 tokens under
  the current tokenizer.
- next triage band: 33 entries at or below 220 tokens.  These are now
  dominated by genuine compact structural arguments and must still be read
  substantively before deciding expansion, demotion, or retention.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- direct missing-reference scan: `missing_count 0`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- primitive-TeX division scan: no `\over` occurrences outside control words
- `tools/build_monograph.sh` clean; `main.pdf` has 2591 pages.
