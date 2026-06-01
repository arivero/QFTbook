# Light-Front Framework Datum Pass

Date: 2026-06-01

Issue lane: #596, with cross-cutting support for #494 and #561.

## Scope

This pass addresses the part of #596 asking for a general light-front
framework rather than only model-specific light-cone calculations.  The
existing manuscript already contained the large-\(N\) two-dimensional QCD
light-front chapter, the Chern--Simons--matter light-cone construction, and
the DLCQ numerical benchmark.  The missing structural layer was a common
regulator datum explaining what has to be specified before a light-front
Hamiltonian computation is a definition of a finite problem.

## Manuscript Changes

- Added Section `Light-Front Kinematic And Constraint Datum` to Volume XI,
  Chapter 10.
- Fixed the mostly-plus light-front conventions
  \(x^\pm=(x^0\pm x^1)/\sqrt2\),
  \(ds^2=-2dx^+dx^-+dx_\perp^2\), and
  \(p\cdot x=-p^-x^+-p^+x^-+p_\perp x_\perp\).
- Added Definition `def:light-front-hamiltonian-regulator-datum`, whose
  entries include the positive-\(p^+\) nonzero-mode sector, zero-mode and
  constraint sector, finite physical Hilbert space, self-adjoint
  \(P^-_\Lambda\), fixed-sector invariant mass operator, and continuum
  diagnostic.
- Derived the free massive light-front one-particle measure
  \[
    \theta(p^0)\delta(p^2+m^2)\,d^D p
    =
    \frac{dp^+\,d^{D-2}p_\perp}{2p^+}
  \]
  on the positive-energy shell, displaying the \(p^-\) localization and the
  \(2p^+\) Jacobian.
- Reframed DLCQ as a compact positive-longitudinal-momentum specialization
  of the general datum.
- Cross-linked the large-\(N\) two-dimensional QCD chapter back to the
  general datum, so the model chapter is visibly a specialization rather
  than an implicit folklore framework.

## Calculation Check

Extended `calculation-checks/hamiltonian_truncation_dlcq_checks.py` with
exact rational checks for:

- the light-front mass-shell identity
  \(-2p^+p^-+p_\perp^2=-m^2\);
- the delta-function Jacobian \(2p^+\) and corresponding measure weight
  \(1/(2p^+)\);
- symmetry of the light-front bilinear form;
- the fixed-sector conversion between \(P^-\) eigenvalues and invariant
  \(M^2\) eigenvalues.

The README ledger and Chapter 10 dossier were updated accordingly.

## Verification

Targeted verification should include:

```bash
python3 calculation-checks/hamiltonian_truncation_dlcq_checks.py
python3 -m py_compile calculation-checks/hamiltonian_truncation_dlcq_checks.py
git diff --check
python3 tools/audit_theorem_form.py
python3 tools/audit_unnumbered_display_labels.py
tools/audit_negative_scope_prose.py
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
tools/build_monograph.sh
```

This pass does not close #596.  It supplies the shared light-front regulator
framework, but #596 still includes deeper continuum solution layers for
Chern--Simons vector models, broader light-front quantization examples, and
model-specific zero-mode analyses.
