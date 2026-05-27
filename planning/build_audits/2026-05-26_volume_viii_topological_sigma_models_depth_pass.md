# 2026-05-26 Volume VIII Chapter 6 Topological Sigma Models Depth Pass

Status: completed and pushed-ready.

## Scope

- Rewrote the topological sigma-model chapter from a short overview into a
  proof-bearing development.
- Defined the mapping field space as a Frechet manifold with locally
  super-ringed fermionic directions.
- Developed the A-model scalar observable complex and proved
  `Q_A O_alpha = O_{d alpha}`.
- Proved the pointwise A-model energy identity with explicit normalization
  of `bar partial_J phi`.
- Derived the fixed-domain Fredholm index from Riemann-Roch and the
  stable-map virtual dimension by adding the moduli of marked curves.
- Defined stable maps, evaluation maps, virtual fundamental classes,
  primary Gromov-Witten functionals, and the degree-selection rule while
  keeping virtual integration input separate from continuum QFT construction.
- Defined the genus-zero small quantum product and proved associativity from
  the splitting axiom on `Mbar_{0,4}`.
- Added the projective-space example
  `QH^*(P^m)=C[H,Q]/(H^{m+1}-Q)`.
- Defined descendant invariants through cotangent-line classes on the
  universal curve and separated them from fixed-worldsheet descent.
- Developed the B-model Dolbeault polyvector complex, trace pairing, and
  complex-structure Maurer-Cartan equation.
- Recast the continuum topological sigma-model construction as an explicit
  open problem with regulator, cycle, anomaly-line, virtual-integration, and
  gluing data.

## Calculation Check

- Added `calculation-checks/topological_sigma_model_checks.py`.
- The check verifies the A-model pointwise energy identity, the
  projective-space quantum cohomology relation `H^{m+1}=Q`, associativity and
  degree selection for projective-space quantum products, the stable-map
  virtual-dimension formula, and the B-model top-form degree condition.

## Verification

- `python3 calculation-checks/topological_sigma_model_checks.py`
  passed with `All topological sigma-model checks passed.`
- `python3 -m py_compile calculation-checks/topological_sigma_model_checks.py`
  passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before this audit note was added.
- `tools/build_monograph.sh` completed cleanly, including log scan.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1812`.
