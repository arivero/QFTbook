# Issue #449 KMS Condition

## Scope

- GitHub issue #449 reported that KMS appeared only as an undefined phrase in
  the Bisognano--Wichmann discussion.
- The fix needed a definition, a derivation from ordinary Gibbs traces, the
  modular KMS property, and the specific boost-temperature consequence of
  Bisognano--Wichmann.

## Resolution

- Added Section~\ref{sec:kms-states-modular-equilibrium} to the modular part
  of the locality/superselection chapter.
- Added Definition~\ref{def:kms-state}: the \(\beta\)-KMS condition as a
  bounded strip-analytic boundary-value condition for a state on a
  \(C^*\)- or von Neumann algebra with a one-parameter automorphism group.
- Added Proposition~\ref{prop:gibbs-trace-kms}, deriving KMS from an ordinary
  trace-class Gibbs state and displaying the two trace-cyclicity moves that
  become the KMS boundary condition in infinite volume.
- Added Theorem~\ref{thm:modular-kms-property}, stating and deriving the
  Tomita--Takesaki modular KMS property, including the convention conversion
  between the standard physical KMS strip and the modular group
  \(\sigma_t=\operatorname{Ad}_{\Delta^{it}}\).
- Expanded the Bisognano--Wichmann paragraph to state explicitly that
  \(\sigma_t=\alpha^R_{-2\pi t}\) implies that the vacuum restricted to the
  standard wedge algebra is a \(2\pi\)-KMS state for boost dynamics, with
  Unruh inverse temperature \(2\pi/a\) along an accelerated orbit.
- Cross-referenced the KMS definition from the earlier Euclidean thermal trace
  discussion.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 791 pages.

No calculation scripts were edited, so the calculation-check harness was not
rerun for this TeX-only change.
