# Multi-Insertion Contact Coordinates Audit

Date: 2026-05-22

This pass strengthens the renormalized-operators chapter by turning the
brief contact-term warning into an explicit finite-regulator construction.
The target is the source-coordinate origin of multi-insertion contact terms.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter12_renormalized_operators_and_minimal_subtraction.tex`.
- Added "Multiple Insertions and Contact-Term Coordinates."
- Defined the full local Taylor expansion
  \(\eta_0=\mathcal Z_\Lambda(\eta_\Lambda)\) of the source-coordinate map.
- Stated the locality condition on higher source jets as support on the
  small diagonal with derivative-delta structure.
- Derived the partition formula for connected distributions with multiple
  insertions under a nonlinear local source-coordinate change.
- Wrote the explicit two-insertion formula showing the contact term from the
  second source-coordinate derivative.
- Added the noncoincident/contact-term proposition: only the singleton
  partition survives on configuration space of distinct insertion points.
- Added the Wilsonian two-insertion identity
  \(G_{AB}=\langle O_A^{\rm W}O_B^{\rm W}\rangle_{\rm conn}
    -\langle O_{AB}^{\rm W}\rangle\).
- Added the 1PI source-Hessian identity for the Legendre transform and the
  low-field two-point subtraction.
- Added a figure separating the linear source jet from higher local jets.

## Planning Updates

- Updated the renormalized-operators dossier with the new construction task,
  claim, figure requirement, and audit note.
- Updated the master architecture and dependency map so the next target is
  using the operator-source/contact-coordinate framework to tighten
  observable correlation-function statements in the universality and CFT
  transition chapters.

## Verification

- Ran `git diff --check`; no whitespace errors.
- Ran strict phrase scans on the edited manuscript and planning files; hits
  were confined to planning source references and guardrails.
- Built the monograph with `tools/build_monograph.sh`; the strict monograph
  text audit and LaTeX log scan were clean.
- Rendered and inspected the new contact-coordinate figure page at
  `/tmp/qft_multi_insertion_contact_coordinates-285.png`; the linear/higher
  jet split, arrows, labels, caption, and adjacent text were legible and
  nonoverlapping.
