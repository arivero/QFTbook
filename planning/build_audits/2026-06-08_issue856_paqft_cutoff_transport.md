# Issue #856 pAQFT cutoff-transport repair

Date: 2026-06-08.

Scope:

- Targeted Volume XII Chapter 10, the pAQFT calculation companion, and the
  chapter dossier.
- Repaired the cutoff-independence proof for Bogoliubov fields so it uses
  relative S-matrix cocycles and one-sided causal support identities.

Primary source checked:

- Fredenhagen--Rejzner, `arXiv:1503.07814`, Sec. 4: the algebraic
  adiabatic-limit construction via relative S-matrices, generalized
  Bogoliubov factorization, outside-past equality, outside-future
  relative-cocycle conjugation, and cutoff-independent local algebras.

Before:

- The proof decomposed `V'-V=A+B` and then treated `A` and `B` as if they could
  be pulled through the full background interaction by raw causal
  factorization.
- The displayed factorization used raw `S(A)` and `S(B)` factors even though
  those cutoff pieces are only ordered relative to the insertion, not relative
  to all of `V`.
- The resulting conjugation was by a raw S-matrix piece rather than the
  relative cocycle that transports cutoff representatives.

After:

- The chapter states the generalized relative Bogoliubov factorization
  identity and derives the two one-sided consequences used in the algebraic
  adiabatic limit.
- The proof removes the future cutoff piece with the outside-past identity and
  transports the past piece with
  `alpha_{V,B}(X)=S_V(B)^{-1} star X star S_V(B)`.
- The transition map is explicitly insertion-independent and the proof records
  cocycle composition/decomposition independence.

Negative controls added:

- `calculation-checks/paqft_algebra_checks.py` now checks the cutoff transport
  in an exact noncommutative `2 x 2` matrix model.
- The same finite model rejects the old raw factorization through an
  overlapping background and rejects replacing the relative cocycle by a raw
  S-matrix conjugator.

Boundary:

- This is a correctness repair for the construction of local interacting
  pAQFT algebras from compact cutoff representatives.  It does not claim a
  nonperturbative adiabatic limit, convergence of the formal S-matrix, or a
  new theorem beyond the cited algebraic adiabatic-limit framework.

Verification:

- `python3 calculation-checks/paqft_algebra_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_xii`
- `python3 tools/audit_negative_scope_prose.py --root ch10 --fail`
- `python3 tools/audit_theorem_form.py --root ch10`
- `tools/audit_monograph_text.sh ch10`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii --fail --limit 40`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_negative_scope_prose.py --fail`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

Audit-caught repairs:

- Adding `eq:paqft-bogoliubov-factorization-relative` triggered the
  source-derived factorization occurrence ledger.  The new pAQFT identity is
  now explicitly excluded as causal-factorization locality algebra, and stale
  Drell-Yan residual-budget rows/textual anchors in the same ledger were
  cleaned so the occurrence audit passes.
- The first build found that the new relative S-matrix display reused the
  Volume IV label `eq:paqft-relative-s-matrix`.  The Volume XII display now
  uses `eq:paqft-curved-relative-s-matrix`; the final build and log scan are
  clean.
