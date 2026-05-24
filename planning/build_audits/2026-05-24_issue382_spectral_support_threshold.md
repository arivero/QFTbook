# Issue 382: Spectral Support Threshold Hypothesis

GitHub issue #382 noted that the Kallen-Lehmann integrals use the conventional
domain \([0,\infty)\) but the chapter did not state early enough the special
support hypothesis used later for a single stable massive scalar LSZ channel.

Edits made:

- Added Remark `rem:kallen-lehmann-single-massive-support`.
- Explained that the lower endpoint \(0\) in the Kallen-Lehmann integral is
  conventional and follows the possible invariant-mass-squared range from the
  spectrum condition; it does not assert spectral weight at zero.
- Stated the conditional assumptions:
  no massless particle seen by \(\widehat\phi\), a stable scalar atom at
  \(m^2>0\), no lighter particles or bound-state atoms in the channel, and
  non-one-particle support beginning with two-particle states.
- Displayed the resulting support statement
  \[
    \operatorname{supp}d\rho_\phi
    \subset
    \{m^2\}\cup[4m^2,\infty),
    \qquad
    \dd\rho_\phi(s)
    =
    Z_\phi\delta_{m^2}(\dd s)+\dd\rho_{\phi,\mathrm c}(s),
  \]
  with \(\operatorname{supp}d\rho_{\phi,\mathrm c}\subset[4m^2,\infty)\).
- Stated that this atom-continuum gap is the spectral input used later by
  Haag--Ruelle and LSZ, and that massless particles, infraparticle thresholds,
  or additional bound-state atoms require replacing the displayed support
  statement.
- Updated the chapter dossier claim ledger and certification notes.

This keeps the general Kallen-Lehmann representation on \([0,\infty)\) while
making the massive single-particle support assumptions explicit before they
are used downstream.
