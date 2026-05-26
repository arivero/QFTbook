# Issue #581 Phi-Four-Three Proof Stack

## Scope

- GitHub issue: `#581`.
- Manuscript locus:
  `monograph/tex/volumes/volume_xi/chapter02_constructive_scalar_models_os_data.tex`.
- Calculation-check locus:
  `calculation-checks/constructive_scalar_spde_checks.py`.

## Content Added

- Added a finite-cutoff stability proposition for the local normal-ordered
  \(\Phi^4_3\) polynomial.  The proof rewrites
  \(\lambda:q^4:_\varepsilon+\alpha_\varepsilon:q^2:_\varepsilon+
  \beta_\varepsilon\) as a quadratic polynomial in \(y=q^2\) and derives the
  lower bound
  \(B_\varepsilon-(A_\varepsilon^-)^2/(4\lambda)\).
- Added a reflection-positivity proposition for split positive-time
  interactions.  The proof identifies the interacting reflection-positive
  form with the reference reflection-positive form applied to
  \(e^{-V_+}F\).
- Added an abstract multiscale phase-cell datum and a theorem proving
  cluster summability and ultraviolet Cauchy convergence from a scale-decay
  bound
  \[
    \sup_{\Delta\in\mathcal D_j}\sum_{X\ni\Delta}e^{a|X|_j}\kappa_j(X)
    \le C_0|\lambda|^{1+\delta}L^{-\alpha j}.
  \]
- Proved the geometric scale sum, the KP rooted-tree bound for the enlarged
  scale-labelled polymer set, and the ultraviolet tail estimate
  \(C_0|\lambda|^{1+\delta}L^{-\alpha J}/(1-L^{-\alpha})\).
- Narrowed the open \(\Phi^4_3\) proof obligation: the remaining gap is now
  the model-specific derivation of the actual phase-cell activities and the
  proof of the scale-decay bound for them, plus the vacuum-energy coordinate
  to matching precision.
- Extended the public calculation check with exact finite arithmetic for the
  local stability lower bound and the multiscale geometric tail.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed.
- Independent log scan passed:
  `rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Latex failed to resolve|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed" monograph/tex/main.log monograph/tex/build/latexmk.out`
  returned no matches.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1450`.

## Issue Status

This pass materially advances issue `#581` but does not close it.  A full
closure still requires the model-specific constructive estimates deriving
the actual \(\Phi^4_3\) phase-cell activities and proving their scale-decay
bound from the regulated scalar measure.
