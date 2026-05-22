# 2026-05-22 Free Scalar Canonical Source/Figure Audit

## Scope

- Source block: 253a handwritten pp. 52--62.
- Manuscript home:
  `monograph/tex/volumes/volume_i/chapter06_relativistic_scalar_fields_and_canonical_quantization.tex`.
- Handwritten source visual trace: `253a_trace-052.png` through
  `253a_trace-062.png`.
- Rendered manuscript pages inspected after the patch: physical PDF pages
  66--71, printed pages 50--55.

## Source Substance Required

- Field theory as infinitely many canonical coordinates
  \(\phi(t,\vec x)\), with \(\vec x\) as a continuous label.
- First-derivative variational calculus and the Euler--Lagrange equation.
- Free massive scalar Lagrangian in mostly-plus signature and the
  Klein--Gordon equation.
- Fourier-space mass-shell support, including positive and negative frequency
  branches.
- Cauchy data \(\phi(0,\vec x)\), \(\partial_t\phi(0,\vec x)\) determining
  the solution.
- Separation of canonical quantization from the formal Lagrangian path
  integral.
- Canonical momentum density, Hamiltonian density, Poisson brackets, and
  equal-time commutators.
- Spatial Fourier oscillator variables with an arbitrary positive even
  normalization \(\nu_{\vec k}\).
- Bogoliubov freedom among oscillator variables before the Hamiltonian is
  used.
- Hamiltonian diagonalization at
  \(\nu_{\vec k}=\omega_{\vec k}=\sqrt{\vec k^2+m^2}\).
- Vacuum-energy identity term as a regulated scalar shift, not an informal
  deletion.
- Poincare-covariant free field, invariant vacuum normalization, and the
  Pauli--Jordan verification of microcausality.

## Patch Made

- Added explicit inversion of the Cauchy data:
  \[
    A(\vec k)
    =
    \frac12\left(
      \widetilde\phi_0(\vec k)
      +\frac{\ii}{\omega_{\vec k}}\widetilde\pi_0(\vec k)
    \right).
  \]
- Inserted the canonical-versus-path-integral distinction before the canonical
  formalism begins.
- Added the explicit Bogoliubov transformation
  \[
    c_{\vec k}
    =
    \frac{\lambda_{\vec k}+\lambda_{\vec k}^{-1}}{2}b_{\vec k}
    +
    \frac{\lambda_{\vec k}-\lambda_{\vec k}^{-1}}{2}b^\dagger_{-\vec k}
  \]
  and the statement that a vector annihilated by the \(b\)'s is not generally
  annihilated by the \(c\)'s.
- Tightened the zero-point-energy paragraph: at finite regulator the term is
  a scalar multiple of the identity, and the additive normalization is chosen
  so the invariant vacuum has zero energy.

## Visual Certification

- The mass-shell figure is legible and agrees with the source distinction
  between positive and negative frequency branches.
- The Cauchy-data equations, Bogoliubov formulas, Hamiltonian diagonalization,
  and vacuum-energy normalization render without crowding or page breaks that
  obscure the logic.
- The source contains no figure that should be pasted as an image; the only
  diagrammatic content needed here is reproduced as TeX/TikZ.

## Register Update

- Promote 253a pp. 52--62 from `mapped` to `certified after 2026-05-22 free
  scalar canonical source/figure audit`.
