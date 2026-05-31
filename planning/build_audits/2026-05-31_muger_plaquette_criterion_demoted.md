# Mueger Plaquette Criterion Demotion

Date: 2026-05-31

GitHub issue: #691, theorem/proof substance audit.  Related proof-debt lane:
#698, TQFT and higher-symmetry mechanisms.

## Scope

Volume VIII, Chapter 9 had a proposition titled `M\"uger-center plaquette
criterion`.  The surrounding construction is important: in a non-pointed
Walker--Wang-type local model, dragging a plaquette loop labelled by \(x\)
through a transverse line \(a\) should act by the categorical monodromy
\(M_{a,x}=c_{x,a}c_{a,x}\).  The old proposition then concluded that lines
commuting with every plaquette recoupling are precisely simple objects in the
Mueger center.

## Audit Decision

The content is useful but the theorem/proof shell was too strong.  Once the
plaquette-crossing action is assumed to be monodromy, the proof only unpacks
the definition of the Mueger center and the direct-sum decomposition of loop
labels.  This is an operational criterion for a concrete Hamiltonian
construction, not a standalone theorem about all Walker--Wang models.

## Change

- Demoted the proposition/proof block to an operational paragraph.
- Kept the precise local criterion
  \(M_{a,x}=\operatorname{id}_{a\otimes x}\) for every simple \(x\).
- Kept the conclusion that the categorical candidates for bulk deconfined
  lines are the simple objects in \(\mathcal Z_2(\mathcal C)\), and that a
  nondegenerate input leaves only the tensor unit under this local test.
- Added a theorem-form audit guard so the old title cannot reappear as a
  theorem/proposition/lemma/corollary wrapper.

The non-pointed Ising example and its exact calculation check remain the
substantive test case.
