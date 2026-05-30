# 2026-05-30 Strongly-Local VOA/Net Mechanism Pass

## Scope

- Continued the global quoted-theorem expansion directive.
- Targeted the strongly-local VOA/conformal-net theorem boundary in
  `volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`.

## Edits

- Added the local VOA-to-net mechanism:
  common smooth domain \(\cap_k\operatorname{Dom}(1+L_0)^k\), polynomial
  energy bounds, convergence of smooth smeared fields, closability from the
  unitary adjoint formula, and generation of local von Neumann algebras from
  closed smeared fields.
- Isolated the analytic step hidden in the word "strongly local": upgrading
  finite-energy common-domain commutators of unbounded smeared fields to
  commutation of the generated von Neumann algebras.
- Added the net-to-VOA reconstruction mechanism: Fredenhagen--Joerss fields
  affiliated with interval algebras, finite-energy vector normalization,
  covariance, locality, polynomial energy bounds, and closure of mode
  products on \(\Hilb^{\mathrm{fin}}\).
- Updated the chapter dossier and the calculation companion.

## Verification Added

- `calculation-checks/cft_voa_modular_checks.py` now checks the exact tail
  estimate behind the implication "polynomial energy bound plus smooth
  Fourier decay gives absolute convergence of the smeared field series."

## Remaining Boundary

- The CKLW/Fredenhagen--Joerss theorem remains a quoted theorem: the global
  proof that a whole VOA field family satisfies strong commutativity, and the
  converse proof that a conformal net supplies enough energy-bounded fields,
  are still theorem-boundary inputs.
