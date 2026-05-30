# 2026-05-30 Conformal-Net DHR Mechanism Pass

## Scope

- Continued the Volume V CFT quoted-theorem proof-debt work for issues #625
  and #697.
- Targeted the complete-rational conformal-net theorem boundary in
  `volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`.

## Edits

- Added the local DHR mechanism behind the complete-rational-net theorem:
  localized endomorphisms, intertwiners, tensor product by composition,
  finite-index statistical dimensions, conjugate equations, charge-transporter
  braiding, the two-interval index, categorical \(S\)-matrix normalization,
  and the transparent-sector nondegeneracy criterion.
- Kept the subfactor proof that complete rationality forces finite
  nondegenerate DHR data as an explicit theorem boundary.
- Updated the chapter dossier and the public calculation companion.

## Verification Added

- `calculation-checks/cft_voa_modular_checks.py` now checks the Ising
  categorical \(S\)-matrix vacuum row from DHR dimensions and verifies that
  the Ising transparent sector is only the vacuum.

## Remaining Boundary

- The Kawahigashi--Longo--Muger theorem itself remains a quoted theorem:
  the full finite-index/subfactor proof that the two-interval index gives a
  nondegenerate braided DHR category is not reproduced in this pass.
