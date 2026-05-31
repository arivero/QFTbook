# GLSM Coulomb Determinant Derivation Pass

Date: 2026-05-31

## Trigger

The Volume VII two-dimensional supersymmetric models chapter treated the
abelian Coulomb-branch one-loop twisted superpotential primarily as a
hypothesis.  The local perturbative determinant is a calculable part of the
GLSM/mirror material imported from the stringbook Appendix K lane, and should
not be hidden inside the hypothesis boundary.

## Edits

- Added a local determinant derivation after the abelian Coulomb one-loop
  determinant hypothesis in Volume VII, Chapter 09.
- Defined the Coulomb-region mass `M=Q sigma` and isolated the part of the
  massive Gaussian determinant linear in the background `D+iF_12`.
- Evaluated the proper-time subtracted coincident propagator
  `4 pi int ds/(4 pi s) (exp(-s |M|^2)-exp(-s mu^2))`.
- Explained how the real logarithm from the subtraction and the phase fixed
  by the axial anomaly combine into the holomorphic branch
  `Q log(Q Sigma/mu)`.
- Integrated the logarithmic derivative to recover the local twisted
  superpotential, while keeping vortex sectors, singular loci, and
  infrared-continuum existence outside the local proof boundary.
- Updated the Volume VII Chapter 09 dossier, stringbook crosswalk, and
  calculation-check inventory.
- Extended `calculation-checks/susy_2d_lg_glsm_checks.py` with a check that
  the one-loop primitive differentiates to the Coulomb logarithmic derivative
  and that determinant normalization constants are finite FI-coordinate
  shifts.

## Verification Plan

- Run the dedicated `susy_2d_lg_glsm_checks.py` script.
- Run text/proof/label/dossier audits.
- Build the monograph before checkpointing.
