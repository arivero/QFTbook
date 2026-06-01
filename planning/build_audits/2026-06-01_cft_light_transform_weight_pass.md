# CFT Light Transform Weight Pass

Date: 2026-06-01

Scope:
- `monograph/tex/volumes/volume_iii/chapter10_light_ray_operators_and_energy_correlators.tex`
- `calculation-checks/conformal_collider_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_iii/chapter10_light_ray_operators_energy_correlators.md`

Purpose:
- Reduce the light-ray-operator proof debt by making the conformal
  representation-theoretic input explicit before the ANEC and collider-bound
  discussion.

Mathematical change:
- Added the embedding-space definition of the light transform of a symmetric
  traceless primary \(\mathcal O_{\Delta,J}\),
  \[
    \mathbb L[\mathcal O_{\Delta,J}](P,Z)
    =
    \int_{-\infty}^{\infty} d\alpha\,
    \mathcal O_{\Delta,J}(Z-\alpha P,-P),
  \]
  with the warning that this formula is a distributional transform subject to
  Lorentzian analyticity and growth hypotheses, not an automatic operation on
  every Wightman field.
- Derived the homogeneity map
  \[
    (\Delta,J)\mapsto (1-J,1-\Delta)
  \]
  directly from embedding-space primary homogeneity and the change of
  null-line integration variable.
- Specialized the result to the stress tensor, clarifying why the energy
  detector at null infinity is a measure-valued operator on \(S^{D-2}\), not
  an ordinary local primary.

Calculation check:
- `calculation-checks/conformal_collider_checks.py` now checks the finite
  rational arithmetic of the light-transform homogeneity map and the
  four-dimensional stress-tensor specialization, alongside the existing
  conformal-collider helicity checks.

Remaining theorem boundary:
- This pass does not close the light-ray OPE theorem debt.  The construction
  of renormalized light-ray products, endpoint matching, and all-order
  anomalous-dimension/mixing theory remain open development items.
