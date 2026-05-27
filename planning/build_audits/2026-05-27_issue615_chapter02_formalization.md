# 2026-05-27 Issue #615 Chapter 2 Formalization Pass

## Scope

- Addressed the remaining Volume I Chapter 2 item identified in the local
  `claude_review.md` issue #615 audit.
- Kept the pass within existing content: no architectural reordering and no
  replacement of the chapter's logic.

## Manuscript Changes

- Added formal definitions for Hilbert-space quantum data, Hamiltonian time
  evolution, rigged Hilbert spaces, generalized eigenvectors, direct-integral
  coordinate kets, one-particle mass-shell rigging, Poincare-covariant vacuum
  data, invariant mass projections, particle shells, Wigner data, Fock spaces,
  Fock test domains, local observable assignments, and free scalar fields.
- Added propositions with proofs for:
  - Schwartz-triple delta kernels and weak resolutions of identity;
  - the joint translation spectral measure;
  - isolated mass shells as one-particle subrepresentations;
  - the bosonic Fock inner product;
  - covariance of the free scalar field;
  - free scalar microcausality.
- Added labels to the infraparticle and odd-locality remarks.

## Calculation Check

- Re-ran `calculation-checks/haag_ruelle_fock_inner_product_checks.py`, which
  checks the Fock permanent formula used by the chapter's bosonic
  creation-operator normalization.

## Verification

- `python3 calculation-checks/haag_ruelle_fock_inner_product_checks.py`
- edited-file long-line scan: clean
- `git diff --check` on edited paths: clean
- `tools/build_monograph.sh`: clean
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2130`
