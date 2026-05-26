# Build Audit: Issue #608 Brascamp-Lieb Convex Cutoffs

## Scope

- Continued the issue #608 stochastic/constructive quantization proof chain
  in `volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Added a self-contained finite-dimensional Brascamp-Lieb covariance
  domination theorem for uniformly convex scalar cutoff measures.
- Derived an interacting negative-Sobolev moment bound from the covariance
  theorem under the hypothesis \(\nabla^2S_N\ge L_N+m^2{\bf 1}\).

## Mathematical Content

- For a finite-dimensional cutoff law
  \(\dd\nu_N=Z_N^{-1}e^{-S_N(\phi)}\dd\phi\) with Hessian lower bound
  \(\nabla^2S_N\ge A_N\), the chapter proves
  \[
    \operatorname{Var}_{\nu_N}((v,\phi))
    \le (v,A_N^{-1}v).
  \]
- The proof is written through the symmetric generator
  \(\mathcal L=\Delta-\nabla S_N\cdot\nabla\), the Friedrichs resolvent
  \(u_\varepsilon=(\varepsilon-\mathcal L)^{-1}f\), and the
  finite-dimensional Bochner identity
  \[
    \int(\mathcal Lu)^2d\nu_N
    =
    \int\|\nabla^2u\|_{\mathrm{HS}}^2d\nu_N
    +
    \int(\nabla u,\nabla^2S_N\nabla u)d\nu_N .
  \]
- If \(A_N\ge L_N+m^2{\bf 1}\) and the law is even, the spectral coordinate
  estimate gives
  \[
    \int\|\phi\|_{H_N^{-\eta}}^2d\nu_N
    \le
    \sum_\alpha(1+\lambda_{N,\alpha})^{-\eta}
      (\lambda_{N,\alpha}+m^2)^{-1}.
  \]
- This supplies a proved interacting moment mechanism for convex cutoff
  families.  The renormalized Wick-ordered \(\Phi^4_2\) family still requires
  its own renormalized stability estimate.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed for the edited files.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf` reports 1528 pages.
- `rg -n "LaTeX Warning|Undefined control sequence|Fatal error|Emergency stop|Overfull|Underfull" monograph/tex/main.log`
  returned no matches.
