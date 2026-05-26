# Issue #582 Dynamic Phi-Four-Three BPHZ Local Counterterm Pass

## Scope

- GitHub issue: `#582`.
- Manuscript locus:
  `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Calculation-check locus:
  `calculation-checks/constructive_scalar_spde_checks.py`.

## Content Added

- Added the parabolic homogeneity ledger for the dynamic \(\Phi^4_3\)
  regularity structure:
  \[
    |\Xi|=-5/2-\kappa,\qquad |X|=-1/2-\kappa,\qquad
    |X^2\mathcal I(X^3)|=-1/2-5\kappa .
  \]
  This identifies the negative two-loop tree that requires a second local
  linear coordinate.
- Defined finite-cutoff kernels \(G_\epsilon\) and \(K_\epsilon\), and fixed
  the local constants
  \[
    C_{1,\epsilon}=G_\epsilon(z,z),\qquad
    C_{2,\epsilon}=2\int K_\epsilon(z,w)G_\epsilon(z,w)^2\,\dd w .
  \]
- Proved the finite-cutoff local Wick-contraction calculation:
  \[
    \mathcal L[-\lambda X_\epsilon^3
      +3\lambda^2X_\epsilon^2K_\epsilon(X_\epsilon^3)]
    =
    (-3\lambda C_{1,\epsilon}
      +9\lambda^2C_{2,\epsilon})X_\epsilon .
  \]
- Separated the nested one-loop tadpole inside the two-loop tree from the new
  two-loop local coordinate by spelling out the recursive finite-cutoff
  forest subtraction.
- Derived the displayed drift counterterm
  \[
    (3\lambda C_{1,\epsilon}-9\lambda^2C_{2,\epsilon})\Phi_\epsilon
  \]
  as the negative of the local singular part, leaving \(c_{\rm fin}\) as the
  independent finite mass coordinate.
- Extended the calculation-check script to verify the homogeneity,
  one-loop/two-loop combinatorics, and signs of the local counterterm.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- Independent log scan passed:
  `rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Latex failed to resolve|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed" monograph/tex/main.log monograph/tex/build/latexmk.out`
  returned no matches after the reference-stabilizing no-op build pass.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1456`.

## Issue Status

This pass advances issue `#582` but does not close it.  The algebraic
finite-cutoff local-coordinate calculation is now present; the remaining
work is the analytic construction and convergence of the BPHZ-renormalized
random model, the nonlinear modelled-distribution fixed point, and the
SPDE-to-OS passage.
