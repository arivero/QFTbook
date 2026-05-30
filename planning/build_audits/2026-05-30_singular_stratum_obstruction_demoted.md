# Singular-Stratum Obstruction Demotion

Date: 2026-05-30

## Scope

- Continued the #691 anti-wrapper audit after the non-pointed Walker--Wang
  checkpoint.
- Read the singular-stratum obstruction block in Volume VIII, Chapter 10 as a
  statement/proof unit.

## Decision

- The formula
  \[
    \Delta_{\rm res}(\pi_*^{\mathcal M^{\rm sm}}\rho)
    =
    -\sum_\alpha \mathcal B_{S_\alpha}(\rho)
  \]
  is important and should remain in the main text.
- Its derivation is the collar-truncated version of the preceding BV
  pushforward-with-boundary formula, followed by the limit
  \(\epsilon\to0\).
- Therefore the content is an obstruction formula and proof-boundary warning,
  not an independent theorem-family statement.

## Changes

- Demoted the former proposition/proof wrapper to a named paragraph.
- Updated the Donaldson-Witten and supersymmetric-localization references to
  cite the displayed obstruction formula rather than a proposition label.
- Added a theorem-form audit guard so the same title cannot be reintroduced as
  theorem-family content without a deliberate harness change.

## Verification

- To be run before commit: theorem-form audit, strict text audit, negative
  scope audit, display-label audit, dossier audit, `git diff --check`, and the
  full monograph build.
