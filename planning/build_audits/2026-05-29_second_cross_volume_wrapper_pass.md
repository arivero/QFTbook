# 2026-05-29 Second Cross-Volume Anti-Wrapper Pass

## Scope

Read the next high-scoring theorem/proof candidates after commit `b4a9120d`.
This pass focused on direct calculations that were still presented as
proposition/proof blocks, and on one conceptual coordinate claim whose proof
needed more detail.

## Demoted To Worked Paragraphs

- `BCS logarithm from the Fermi surface`: elementary mean-field shell integral
  once the local attractive-channel gap equation is assumed.
- `Planar chiral-primary normalization`: planar Wick-counting normalization
  and extremal three-point convention.
- `Discriminant of the cusp unfolding`: cubic discriminant algebra used to
  locate the Argyres-Douglas collision.
- `Semigroup property of BV Wilsonian pushforward`: Fubini/product-cycle
  consequence of the composable BV tower definition; the nontrivial content is
  the existence/admissibility of the tower.
- `Boundary Euler equation`: direct fixed-metric first variation of the
  boundary Liouville action.
- `Worldline dressing gives the soft eikonal denominator`: regulated
  half-line Fourier transform.
- `Contraction of the two-flavor baryon spin-flavor algebra`: Pauli-matrix
  one-slot algebra plus large-\(N_c\) scaling.
- `Threshold discontinuity of the one-loop self-energy`: logarithm branch-cut
  interval calculation.
- `First four-fermion direct-minus-exchange vertex`: first-order fermionic
  Wick-contraction sign calculation.

## Strengthened As Substantive Claim

- `Physical strong-CP phase coordinate`: expanded the proof through the
  one-quark axial rotation, anomalous Jacobian, multi-quark singular-value
  decomposition, determinant phase, and nonsingular-mass chart boundary.

## Retained For Later Reading

- `CFT-internal Cardy growth`, `Largest-time identity for a scalar graph`,
  and the fermionic coherent-state path-integral construction were read as
  candidates but not demoted in this pass.  Later manual reading demoted the
  Cardy-growth statement to a Tauberian-consequence paragraph, while the
  largest-time identity and the fermionic coherent-state construction remain
  retained as reusable mechanisms.

## Recurrence Guard

`tools/audit_theorem_form.py` now rejects the nine demoted titles if they
return to theorem-family environments.

## Verification

The theorem-form/text/prose/display-label audits, `git diff --check`, and
the full monograph build were clean.  The rebuilt PDF has 2580 pages.  The
cross-volume short-proof heuristic count decreased from 74 before this pass
to 64 after the pass.
