# Core Depth Pass 8

Date: 2026-05-21

## Scope

This pass deepened five places in the core manuscript where a definition or
derivation benefited from being made explicit.

- Volume I, perturbative Green functions: added the derivation of graph
  symmetry factors from regulated Wick pairings, including the tadpole and
  labelled quartic-vertex checks.
- Volume I, scattering observables: added the geometric form of elastic and
  inelastic partial-wave unitarity, including the unitarity circle and the
  phase-shift parametrization.
- Volume II, analyticity: added the edge-of-the-wedge form needed to connect
  locality, tube analyticity, and later crossing arguments.
- Volume II, BPHZ renormalization: added Zimmermann normal products and the
  finite local relation between different subtraction degrees.
- Volume III, radial quantization: added the adjoint relations for conformal
  generators and their use in descendant norm computations.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- Deferred-topic scan over `monograph/tex/volumes`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 324 pages.
