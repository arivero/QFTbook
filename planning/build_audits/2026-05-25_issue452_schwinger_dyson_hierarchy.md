# 2026-05-25 Issue #452 Schwinger--Dyson Hierarchy Audit

## Scope

- GitHub issue: #452, `[Vol II] Schwinger-Dyson equations (functional) absent`.
- Manuscript target:
  `monograph/tex/volumes/volume_ii/chapter23_generating_functionals_and_the_one_particle_irreducible_effective_action.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_ii/chapter09_generating_functionals_1pi_effective_action.md`.

## Manuscript Changes

- Added a dedicated section, `Schwinger--Dyson Identities and the 1PI
  Hierarchy`, immediately after the reconstruction of connected functions from
  exact 1PI vertices and before Euclidean convexity.
- Stated the finite-regulator hypotheses needed for field-space integration by
  parts: translation-invariant scalar reference density or its logarithmic
  derivative, no boundary contribution for the chosen variation, and explicit
  accounting of Jacobian insertions.  Gauge theory is explicitly separated as a
  BRST/BV problem rather than treated by a naive scalar field translation.
- Introduced condensed DeWitt notation and derived the exact insertion
  identity
  \[
    \langle(S_i[\phi]+J_i)\mathcal O[\phi]\rangle_J
    =
    i\langle\delta\mathcal O/\delta\phi^i\rangle_J .
  \]
- Derived the source-functional identity
  \[
    [S_i((1/i)\delta/\delta J)+J_i]Z[J]=0
  \]
  and its connected form
  \[
    S_i(\varphi+(1/i)\delta/\delta J)1+J_i=0 .
  \]
- Derived the exact 1PI quantum equation of motion
  \[
    \Gamma_i[\varphi]=\langle S_i[\phi]\rangle_{J_\varphi}.
  \]
- Worked out the quartic scalar hierarchy through the first two nontrivial
  members:
  the full propagator equation involving the exact connected four-point
  kernel, and the full four-point vertex member both as an insertion identity
  and as a connected differentiated identity.
- Added the Legendre identities expressing the exact connected four- and
  six-point kernels in terms of \(\Gamma^{(4)}\), \(\Gamma^{(6)}\), and the
  exact tree made from two \(\Gamma^{(4)}\) vertices joined by one exact
  propagator in the \(\phi\mapsto-\phi\) symmetric case.
- Stated that Hartree/gap and vertex-closure equations are truncations of the
  exact hierarchy, not consequences of the Schwinger--Dyson identity itself.

## Dossier Changes

- Added Schwinger--Dyson hypotheses, notation, exact identities, 1PI equation
  of motion, propagator member, vertex member, and truncation caveats to the
  construction task and claim ledger.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 801 pages.
