# 2026-05-26 Volume IX Confinement Depth Pass

Scope: comprehensive depth pass on Volume IX, Chapter 4, a residual thin
later-volume chapter flagged by the active review.

## Manuscript Changes

Volume IX, Chapter 4 now develops confinement, screening, and oblique
confinement from line-operator data rather than slogans.

- Rebuilt the chapter around the external charge system
  \((\mathcal C,B,S)\), distinguishing full line-charge lattices, finite
  center-sensitive charge groups, external charges modulo screening, and the
  residual topological quotient \(S^\perp/S\).
- Proved that the finite Dirac pairing descends to \(S^\perp/S\) when the
  screened subgroup is isotropic.
- Defined area, perimeter, zero-tension, and static-potential laws for
  renormalized line operators with the line renormalization scheme and order
  of limits explicit.
- Proved transfer-matrix extraction of the static potential and a screening
  bound showing that finite-mass endpoint screening rules out a positive
  asymptotic linear potential for the screened charge.
- Strengthened the strong-coupling lattice area-law mechanism with an
  explicit Haar-projection surface-selection lemma and a convergent-polymer
  proposition.
- Developed finite condensate and oblique-confinement diagnostics, including
  the \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\) example and the
  condition \(e\equiv pm\pmod N\) for a dyonic condensate
  \(\langle(p,1)\rangle\).
- Added a finite charge-lattice figure for the oblique unconfined direction.

## Calculation Checks

Added `calculation-checks/oblique_confinement_checks.py`, which checks exact
finite arithmetic for:

- descent of the screened pairing to \(S^\perp/S\);
- maximal isotropy of dyonic condensates \(\langle(p,1)\rangle\);
- the oblique unconfined condition \(e\equiv pm\pmod N\);
- confinement of nonzero electric \(N\)-ality under magnetic condensation;
- incompatibility of simultaneously condensing mutually nonlocal electric and
  magnetic generators.

The calculation-check README and Volume IX chapter dossier were updated.

## Verification

Completed before commit:

- `python3 calculation-checks/oblique_confinement_checks.py`
- `python3 -m py_compile calculation-checks/oblique_confinement_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The build completed with a clean log scan and produced
`monograph/tex/main.pdf` with 1776 pages.
