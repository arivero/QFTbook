# Issue #844 Ch19b Claim-Architecture Cleanup

## Scope

- Volume II Ch19b, SCET/QCD factorization reference map and finite-resolution
  EEC observable assembly.
- Planning harness rule for canonical claim architecture.
- This is an architecture-to-observable repair, not a new factorization theorem
  and not a new finite identity.

## Changes

- Replaced remaining visible `dependency ladder` / `hard-process ledger`
  wording in the Ch19b factorization-reference surface with comparison-map and
  reference-map language.
- Reclassified the finite-resolution EEC residual display as an
  `observable-error decomposition`.
- Made the error terms explicit: `B_bin` is the proved finite-resolution
  Lipschitz estimate; `B_contact` is a contact/endpoint convention;
  `B_pert` is perturbative truncation; `B_FG` is the factorization/Glauber
  hypothesis residual; `B_np` and `B_track` are nonperturbative inputs; and
  `B_cont` is continuum/regulator reconstruction.
- Updated `planning/12_strict_writing_harness.md` with the canonical
  observable-first claim architecture and the rule that displayed residual
  sums must classify their terms as identities, hypotheses, inputs, estimated
  residuals, or proved bounds.
- Updated the Ch19b dossier.

## Re-Audit

- No formula, label, theorem status, or factorization claim was strengthened.
- The repair makes the physical object easier to locate: an energy-correlator
  prediction is a tested detector functional with classified residuals, not a
  free-standing ledger.
- The style rule remains in planning, not in monograph TeX.
