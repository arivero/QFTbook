# 2026-05-28 Issue #633: BPHZ Forest-Formula Depth Pass

## Scope

Reading-based correction to the reopened #633 backlog for Volume II,
Chapter 9, `Subdivergences and BPHZ Subtractions`.

The original audit used theorem-density as a proxy.  This pass instead
targeted concrete substance in the chapter: the Bogoliubov recursion,
Zimmermann forest formula, Hepp-sector extraction used in the finiteness
proof, and Zimmermann normal-product identity were present in prose but not
isolated as reusable mathematical statements with proofs.

## Manuscript Changes

- Added Proposition `prop:bogoliubov-preparation-recursion`, proving that the
  recursive preparation and counterterm maps are well founded by induction on
  internal-line number and produce local polynomial counterterm vertices.
- Added Theorem `thm:zimmermann-forest-formula`, proving the integrand-level
  forest formula from the recursive preparation map by induction and by
  decomposing forests according to their maximal proper elements.
- Added Lemma `lem:hepp-sector-forest-extraction`, isolating the sector-local
  extraction of a forest from an ordered ultraviolet hierarchy.
- Refactored the BPHZ finiteness proof so the Hepp-sector extraction is a
  named input and the remaining proof focuses on the Taylor-remainder
  estimates and sector-product convergence.
- Replaced the prose Zimmermann-identity paragraph with Proposition
  `prop:zimmermann-normal-product-identity`, including a graph-by-graph proof
  from the finite Taylor difference between subtraction degrees.

## Calculation Check

- Added `calculation-checks/bphz_forest_formula_checks.py`.
- The script verifies the finite recursive combinatorics in nested,
  disjoint, and overlapping subgraph configurations, including the diamond
  forest list and the fact that a counterterm appends the subgraph as the
  largest Taylor operator.

## Verification

To run before checkpoint:

- `python3 calculation-checks/bphz_forest_formula_checks.py`
- `python3 -m py_compile calculation-checks/bphz_forest_formula_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
