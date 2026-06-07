Issue: #597
Chapter: Volume II, Chapter 20D
Pass: retained hard-channel normal-source quotient

Scope
- Added `ca:instanton-retained-hard-normal-source-quotient` after the
  retained-window crossed hard-channel amplitude block.
- The edit expands the nonzero-mode source quotient in the named
  `SU(3)`, `N_f=2` hard channel as a pointwise Gaussian source mean plus the
  first cubic source-cumulant correction, then integrates it through the same
  signed hard measure as the zero-mode slots, Haar projection, amputation,
  crossing data, running collective factor, and size-window tails.
- This is a physical-amplitude repair, not a moduli-space or ADHM expansion.

Companion
- Extended `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  with `check_retained_hard_channel_normal_source_quotient()`.
- The finite rational model rejects determinant-only, Gaussian-only, unweighted
  post-projection quotient, and omitted-cubic-cumulant residual shortcuts.

Quality boundary
- The pass does not compute the continuum Pauli-Villars determinant constant or
  prove the continuum hard-channel LSZ theorem.  It narrows the retained
  finite-regulator hard-channel assembly by making the source-dependent
  normal-fluctuation quotient explicit where the physical amplitude is formed.
