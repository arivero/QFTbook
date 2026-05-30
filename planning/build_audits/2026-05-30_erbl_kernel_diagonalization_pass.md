# ERBL Kernel Diagonalization Pass

Date: 2026-05-30

Scope:
- Volume II, Chapter 19, exclusive-pion light-ray section.
- Former quoted theorem `qthm:qcd-erbl-gegenbauer-diagonalization`.

Edits:
- Replaced the quoted theorem with a proved proposition.
- Corrected the eigenvalue normalization for the kernel and evolution
  convention used in the chapter:
  \[
    \int_0^1 dy\,V(x,y)\varphi_n(y)
    =-\frac12\gamma_n^{(0)}\varphi_n(x).
  \]
- Corrected the Gegenbauer-moment RG equation to
  \(-\alpha_s\gamma_n^{(0)}a_n/(4\pi)\).
- Added the finite plus-prescribed polynomial action at fixed \(x\), so the
  singular subtraction is visible rather than hidden in the word "standard".
- Added the coefficient operator and the recurrence mechanism reducing the
  all-\(n\) identity to the Gegenbauer recurrence.
- Extended `calculation-checks/qcd_exclusive_pion_checks.py` to verify the
  exact rational polynomial action of the displayed ERBL kernel on
  \(6x(1-x)C_n^{3/2}(2x-1)\) for \(0\le n\le8\).
- Updated `calculation-checks/README.md` and the chapter dossier.

Verification:
- `python3 calculation-checks/qcd_exclusive_pion_checks.py` passed.

Remaining Boundary:
- The proposition now proves the displayed one-loop kernel identity as a
  finite polynomial calculation.  A later deeper light-ray chapter could add
  the full collinear \(SL(2,\mathbb R)\) representation-theoretic derivation
  of the one-loop kernel itself, including the scheme dependence beyond
  leading order.
