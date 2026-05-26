# Issue #582 Singular-SPDE Energy And Invariance Pass

## Scope

- GitHub issue: `#582`.
- Manuscript locus:
  `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Calculation-check locus:
  `calculation-checks/constructive_scalar_spde_checks.py`.

## Content Added

- Added a smooth enhanced-noise energy estimate for the
  Da Prato--Debussche remainder equation
  \[
    \partial_tY=(\Delta-m^2)Y
    -\lambda(Y^3+3Y^2X_1+3YX_2+X_3).
  \]
  The proof multiplies by \(Y\), integrates by parts on the torus, and uses
  exact Young conjugate pairs \((4/3,4)\), \((2,2)\), and \((4,4/3)\) to
  absorb the mixed terms \(Y^3X_1\), \(Y^2X_2\), and \(YX_3\) into the
  positive quartic drift.
- Proved the resulting estimate
  \[
    \frac12\frac d{dt}\|Y\|_2^2+\|\nabla Y\|_2^2+m^2\|Y\|_2^2
    +\frac\lambda4\|Y\|_4^4
    \le C\lambda\bigl(\|X_1\|_4^4+\|X_2\|_2^2
    +\|X_3\|_{4/3}^{4/3}\bigr),
  \]
  and spelled out why this prevents finite-time blowup for smooth Galerkin
  approximations when the enhanced-noise norms are time-integrable.
- Added an invariant-measure cutoff-limit proposition.  The proof shows that
  weak convergence of invariant cutoff laws, tightness, and compact-uniform
  convergence of the corresponding Markov semigroups on high-probability
  compact sets imply invariance of the limiting measure.
- Updated the public calculation check to verify the Young-exponent
  arithmetic and a finite Markov-chain version of the invariant-measure
  identity.
- Updated the chapter dossier with the new notation, claim ledger entries,
  and remaining proof boundary.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- Independent log scan passed:
  `rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Latex failed to resolve|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed" monograph/tex/main.log monograph/tex/build/latexmk.out`
  returned no matches.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1452`.

## Issue Status

This pass advances issue `#582` but does not close it.  The remaining
components include the Hairer reconstruction theorem with model norms and
wavelet estimates, BPHZ-renormalized model construction and convergence for
dynamic \(\Phi^4_3\), the modelled-distribution fixed point, the concrete
local counterterm identification, and the SPDE-to-OS passage.
