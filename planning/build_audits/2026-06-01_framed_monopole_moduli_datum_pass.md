# Framed Monopole Moduli Datum Pass

Date: 2026-06-01

Issue lane: #597.

## Scope

This pass strengthens the monopole part of the soliton/monopole/instanton
development.  The manuscript already had the Bogomolny bound, the
Prasad--Sommerfield solution, the dyonic phase coordinate, and a finite
collective-coordinate stationary-phase theorem.  The weak point was the
placement and brevity of the monopole moduli-space construction: the phase
coordinate referred forward to the moduli metric, while the actual
low-velocity dynamics appeared later as a short paragraph.

## Manuscript Changes

- Added Subsection `Framed Monopole Moduli Data and Low-Velocity Dynamics`
  before the dyonic phase-coordinate discussion in Volume II, Chapter 17.
- Defined the framed BPS monopole moduli datum as the quotient of BPS
  finite-energy fields by based gauge transformations.
- Kept the residual \(U(1)_\infty\) action as the primitive phase coordinate
  used for dyonic quantization.
- Derived the linearized Bogomolny equation in the Hermitian-generator
  convention of the chapter.
- Derived the background-gauge horizontal condition from orthogonality to
  based gauge orbits.
- Defined the monopole \(L^2\) zero-mode metric and placed the \(4n\)
  dimension bookkeeping at the elliptic-complex/index boundary.
- Derived the low-velocity geodesic Lagrangian from Gauss' law and the
  restriction of the real-time kinetic energy to horizontal zero modes.
- Recorded the primitive unit-monopole metric block
  \(\mathbb R^3\times S^1\) with mass coefficient \(M_{\rm BPS}\) and phase
  inertia \(I_\chi\).
- Replaced the later duplicate low-velocity paragraph by a cross-reference
  to the new logically placed subsection.

## Calculation Check

Extended `calculation-checks/soliton_collective_coordinate_checks.py` with
finite checks for:

- framed and centered monopole dimension bookkeeping;
- the unit- and two-monopole relative-coordinate counts;
- the sign relating the background-gauge condition to orthogonality against
  infinitesimal based gauge transformations.

The calculation-check README and the Volume II Chapter 18 dossier were
updated.

## Verification

Targeted verification should include:

```bash
python3 calculation-checks/soliton_collective_coordinate_checks.py
python3 -m py_compile calculation-checks/soliton_collective_coordinate_checks.py
git diff --check
python3 tools/audit_theorem_form.py
python3 tools/audit_unnumbered_display_labels.py
tools/audit_negative_scope_prose.py
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
tools/build_monograph.sh
```

This pass does not close #597.  It supplies the framed monopole moduli datum
and the low-velocity dynamics layer, but the issue still calls for deeper
multi-monopole geometry, soliton quantization examples, full instanton
determinant constants, multi-instanton ADHM measure development, and
compactification/boundary-stratum analysis.
