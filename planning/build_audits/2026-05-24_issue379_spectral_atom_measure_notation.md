# Issue 379: Spectral Atom Measure Notation

GitHub issue #379 flagged an overload in the Kallen-Lehmann chapter: the text
used \(Z\delta_{m^2}\) and \(Z\delta_{m^2}(\dd\mu^2)\) interchangeably.  Since
the one-particle contribution is a point mass of the positive spectral measure,
not an ordinary density, the notation has now been standardized.

Edits made:

- Defined \(\delta_{m^2}\) locally as the unit point measure at the invariant
  mass \(m^2\).
- Replaced the canonical sum-rule statement of the one-particle atom by
  \(Z\,\delta_{m^2}(\dd s)\).
- Rewrote the one-particle spectral contribution as
  \[
    \dd\rho_1(\mu^2)=Z\,\delta_{m^2}(\dd\mu^2),
  \]
  before decomposing \(\dd\rho=\dd\rho_1+\dd\rho_{\mathrm c}\).
- Updated the comparison with the invariant-mass decomposition to use
  \(\dd\rho_1(\mu^2)=Z\,\delta_{m^2}(\dd\mu^2)\).
- Replaced the local phrase "density notation" by "momentum-space measure" in
  the one-particle calculation.
- Updated the spectral-measure figure label and the infraparticle remark to
  use point-measure notation.
- Updated the chapter dossier notation inventory, claim ledger, and audit
  notes.

The numerical statement \(0\le Z\le1\) and the remainder \(1-Z\) are unchanged:
they refer to total masses of positive measures under the canonical
equal-time normalization, and \(\delta_{m^2}\) has total mass one.
