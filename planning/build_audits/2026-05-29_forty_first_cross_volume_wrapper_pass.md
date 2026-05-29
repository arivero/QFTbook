# Forty-First Cross-Volume Wrapper Pass

Date: 2026-05-29.

Scope: continued issue #691 semantic audit of assumption/hypothesis-heavy
statements, proof environments whose content is only finite algebra or
definition unwinding, and propositions whose substance is hidden in the
hypotheses.  This pass deliberately distinguished compact but real proof
infrastructure from numbered wrappers.

## Demoted or Reclassified

- `\(A_{N_c-1}\) sine profile and normalized tensions` was demoted from
  proposition to example.  The content is a useful finite-dimensional sine
  calculation inside the Abelianized Seiberg--Witten patch; the surrounding
  text now treats it as a worked calculation rather than as a theorem-family
  claim about nonperturbative \(k\)-strings.

- `Sharp spatial cutoff one-loop coordinate` was demoted from proposition to
  example.  The derivation is a concrete Ornstein--Uhlenbeck variance and
  lattice-shell count used to normalize the later two-loop coordinate; the
  calculation remains in full but no longer carries proposition form.

- `Relation of the mass notions` was demoted from proposition to remark.  The
  material is important conceptual bookkeeping among spectral pole mass, 1PI
  subtraction coordinates, MS coordinates, and lattice gap scaling.  The proof
  was an explanatory derivation from definitions and the pole equation, not
  an independent mathematical result.

- `Ideal CFL is electrically neutral at zero electric source` was demoted
  from proposition to remark.  The vanishing follows from the explicitly
  assumed ideal CFL symmetry realization and tracelessness of \(Q_{\rm em}\);
  the nontrivial work lies in justifying or replacing those ideal hypotheses.

- `Wigner cocycle and spin-frame change` was reclassified from proposition to
  lemma.  It is essential one-particle representation infrastructure, but the
  proof is the cocycle factorization and spin-frame gauge transformation.

- `Odd symplectic origin of the antibracket` was reclassified from proposition
  to lemma.  The statement is a finite-regulator Darboux-coordinate identity
  and a local proof of the BV bracket identities.

- `Dyadic parabolic convolution bound` was reclassified from proposition to
  lemma.  The estimate is real deterministic infrastructure for the SPDE BPHZ
  bounds, but lemma status better matches its role as a scale-arithmetic tool.

- `Locality passes through state convergence for spin nets` was reclassified
  from proposition to lemma.  The exact finite-lattice commutator and the GNS
  limit argument are useful, but they are a locality-transfer lemma rather
  than a proposition-level reconstruction theorem.

- `Delta-normalized and invariant scalar momentum states` was reclassified
  from proposition to lemma.  The normalization derivation remains because it
  fixes conventions used by the Kallen--Lehmann and LSZ chapters.

## Guardrails Added

The theorem-form audit now rejects reintroduction of the demoted sine-profile
calculation, sharp-cutoff one-loop coordinate, relation-of-mass-notions
bookkeeping statement, and ideal-CFL neutrality statement as theorem-family
wrappers.

## Read and Retained

The following compact candidates were read and retained:

- `Transfer-matrix commutativity`, because the proof is the RTT trace
  argument plus meromorphic continuation and is the algebraic source of
  commuting finite-volume charges.

- `NS unitarity bound and chiral primaries`, because it is a positivity result
  in a unitary \(N=2\) superconformal representation.

- `McKean--Singer identity`, because the proof is a spectral pairing theorem
  for the nonzero eigenvalues of \(D_A^2\).

- `Almost locality gives the commutator estimate`, because the proof imports
  the velocity-support stationary-phase lemma and gives the Haag--Ruelle
  Cook-bound input.

- `Cocharacter criterion for the monopole singularity`, because it classifies
  the local \(T\)-valued transition function by the cocharacter lattice and
  checks the Wilson-probe phase.

- `Local BEH mode count`, because the statement isolates the orbit
  differential \(q_v\), the Hessian on a transverse slice, and the local
  gauge-orbit coordinates; it is a conceptual mode-count proposition rather
  than a mere arithmetic count.

## Current Inventory

After this pass the monograph contains:

- theorem: 93
- proposition: 351
- lemma: 35
- corollary: 11
- theorem-family total: 490
- proof: 485
- remark: 310
- example: 74

The broad heuristic scan now flags 38 score-at-least-4 candidates.  The
remaining list is enriched in genuine compact infrastructure, so the estimate
of actual remaining demotions is lower than the raw count.  The working range
after this pass is roughly 15--35 further theorem-family statements needing
demotion or reclassification, and roughly 35--65 proof environments needing
strengthening, retitling, or tighter hypotheses.  This remains an estimate;
semantic reading of every proof continues to be required.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- direct missing-label scan: `missing_count 0`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` gives `Pages: 2592`
