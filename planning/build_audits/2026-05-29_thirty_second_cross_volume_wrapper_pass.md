# 2026-05-29 Thirty-Second Cross-Volume Wrapper Pass

## Scope

This pass continues GitHub issue #691 after commit `efe943f8`.  I regenerated
a high-signal short/cue-heavy theorem-proof queue and read the leading
candidates in context.  The standard was unchanged: demote formula
verification, finite bookkeeping, and direct substitution; retain compact
proofs when they establish a reusable analytic, representation-theoretic,
geometric, or Ward-identity mechanism.

## Demotions

Seven theorem-family wrappers were demoted to paragraphs while preserving the
actual formulas and derivations:

- Volume I, Chapter 18: field-strength two-point function and photon helicity
  data, now a worked free-Maxwell verification rather than a proposition.
- Volume II, Chapter 19: open flux-tube oscillator labels, now Gaussian
  oscillator bookkeeping before the channel table.
- Volume VII, Chapter 6: topological-sector selection for pure-SYM
  \(S\)-correlators, now zero-mode degree counting rather than a proposition.
- Volume VII, Chapter 14: fused mirror kernels in the chosen orientation, now
  a formula-fusion paragraph rather than a proposition.
- Volume X, Chapter 9: canonical entropy divergence with anomaly, now an
  explicit sign-fixing calculation rather than a proposition.
- Volume X, Chapter 12: gauge-covariant HTL equations and transversality, now
  an explicit angular-kernel verification rather than a proposition.
- Volume XI, Chapter 9: finite-chaos kernels for tested nonlinear SPDE
  coordinates, now finite-chaos bookkeeping feeding the following covariance
  proposition.

The theorem-form audit guardrail was extended with these titles.

## Retained After Reading

The following leading candidates were read and retained because their short
proofs contain real machinery rather than decorative wrappers:

- Schwarzian stress-tensor transformation and the plane-cylinder shift.
- Microlocal status of the Dyson light-cone lift.
- The adjoint \(SU(2)\) Bogomolny bound.
- Forward-tube analyticity from the spectrum condition.
- Local anomalies as relative BRST classes.
- Stable-current three-point extraction from finite-volume spectral data.
- The first Seeley--DeWitt coefficients.
- The Knizhnik--Zamolodchikov equation.
- Spin-field form factors in the free massive fermion.
- Cutkosky cut rule for a perturbative physical cut.
- Haag--Ruelle scalar wave-operator isometry.
- Energy-correlator polynomial density.
- Local conformal-current Ward identity.
- Rest-frame BPS bound from singular values.
- Reflection adjoint of a topological-defect action.
- Scattering-chamber consistency in factorized scattering.
- Late-time Hawking packet occupation.
- Integrated nonsinglet axial Ward identity.

## Counts

After this pass:

- theorem environments: 96
- proposition environments: 376
- lemma environments: 29
- corollary environments: 10
- proof environments: 506
- total theorem-family environments: 511

The high-confidence remaining-demotion estimate is now roughly 3--6 for the
same visibly calculational wrapper class.  A slower second pass remains
necessary for hypothesis-heavy statements whose proofs may be compact because
the real substance is hidden in the assumptions.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- stale-label scan for all seven removed theorem-family labels
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reports `Pages: 2582`
