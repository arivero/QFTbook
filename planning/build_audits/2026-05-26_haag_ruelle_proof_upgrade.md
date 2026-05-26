# 2026-05-26 Haag--Ruelle Proof Upgrade

Scope: foundational proof-depth pass prompted by the requirement that
Haag--Ruelle scattering be proved clearly in the monograph.

## Manuscript Changes

Volume IV, Chapter 5 now expands the ordinary massive Haag--Ruelle proof.

- Added Definition `def:haag-ruelle-estimate-package`, separating the
  analytic estimates needed for the theorem: vacuum annihilation and
  one-particle creation, rapid commutator decay, one-particle contraction,
  recursive scalar-product contraction, and Cook integrability.
- Added Proposition `prop:estimate-package-implies-haag-ruelle`, proving from
  these estimates that the outgoing/incoming limits exist, depend only on the
  one-particle vectors, and reproduce the bosonic Fock inner product.
- Added Lemma `lem:hr-stationary-phase-velocity-localization`, proving the
  velocity-tube localization of positive-energy Klein--Gordon packets by
  explicit integration by parts.
- Added Proposition `prop:almost-locality-gives-hr-commutator`, deriving the
  rapid commutator estimate from almost locality plus spacelike separation of
  velocity tubes.
- Added Proposition
  `prop:origin-of-remaining-haag-ruelle-estimates`, explaining how spectral
  transfer and spectral isolation supply the remaining contraction and Cook
  estimates.

The charged Wilson-line Haag--Ruelle construction remains explicitly open and
restricted to nonconfining charged sectors.

## Calculation Checks

Added `calculation-checks/haag_ruelle_fock_inner_product_checks.py`, which
checks in exact rational arithmetic:

- the vacuum base case;
- the two-particle bosonic inner product;
- equality between recursive contraction and direct permanent;
- particle-number orthogonality.

The calculation-check README and chapter dossier were updated.

## Verification

Completed before commit:

- `python3 calculation-checks/haag_ruelle_fock_inner_product_checks.py`
- `python3 -m py_compile calculation-checks/haag_ruelle_fock_inner_product_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The final build was clean and produced
`monograph/tex/main.pdf` with 1771 pages.
