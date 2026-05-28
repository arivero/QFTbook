# Issue #630 Small-X/BFKL Pass

## Scope

Developed the small-\(x\) boundary of the DIS/QCD chapter as a regulated
Wilson-line problem rather than as colored parton scattering language.

## Manuscript Changes

- Added a regulated small-\(x\) dipole datum with Wilson-line endpoint and
  rapidity-subtraction data.
- Proved gauge invariance of the finite-regulator dipole matrix element.
- Stated the leading-logarithmic BFKL evolution datum with the trace-delta
  coefficient \(g^2C_A/(8\pi^3)\) and separated it from the large-\(N_c\)
  nonlinear BK closure assumption.
- Proved transverse kernel covariance under translations, rotations, scalings,
  and inversion.
- Derived the Mellin eigenvalue
  \(\chi(\gamma)=2\psi(1)-\psi(\gamma)-\psi(1-\gamma)\) by analytic
  regularization of the subtracted transverse integral.
- Added the fixed-coupling intercept and diffusion coefficient
  \(\chi(1/2)=4\log 2\) and
  \(\chi(1/2+\ii\nu)=4\log2-14\zeta(3)\nu^2+O(\nu^4)\), with a status label
  separating the kernel theorem from a nonperturbative hadronic cross-section
  theorem.

## Verification

- `python3 calculation-checks/qcd_bfkl_small_x_checks.py`
- `python3 -m py_compile calculation-checks/qcd_bfkl_small_x_checks.py`
- targeted `git diff --check`
- full monograph build after the pass
