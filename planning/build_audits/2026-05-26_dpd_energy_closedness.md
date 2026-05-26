# Build Audit: DPD Energy Closedness

## Scope

- Continued the Volume XI stochastic-quantization proof chain in
  `volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Added a closedness theorem for the integrated Da Prato--Debussche energy
  inequality under smooth enhanced-noise approximation.
- Updated the calculation-check script and chapter dossier to record the
  exact \(L^p\) exponent arithmetic and weak lower-semicontinuity mechanism.

## Mathematical Content

- The new proposition assumes
  \[
    X_{1,n}\to X_1 \text{ in } L^4,\qquad
    X_{2,n}\to X_2 \text{ in } L^2,\qquad
    X_{3,n}\to X_3 \text{ in } L^{4/3}.
  \]
- Smooth remainders \(Y_n\) are assumed to converge weakly in the natural
  energy spaces \(L^2_tH^1_x\), \(L^4_{t,x}\), and at the terminal time in
  \(L^2_x\).
- The proof integrates the smooth energy estimate, passes the enhanced-noise
  terms to the limit by
  \[
    ||a|^p-|b|^p|
    \le p|a-b|(|a|+|b|)^{p-1},
  \]
  and applies weak lower semicontinuity to the endpoint \(L^2\), spacetime
  \(L^2_tH^1_x\), spacetime \(L^2_{t,x}\), and spacetime \(L^4_{t,x}\)
  energy terms.
- This theorem isolates the deterministic closedness component of the rough
  global energy argument; the compactness and enhanced-noise convergence
  estimates remain separate constructive inputs.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed for the edited files.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf` reports 1529 pages.
- `rg -n "LaTeX Warning|Undefined control sequence|Fatal error|Emergency stop|Overfull|Underfull" monograph/tex/main.log`
  returned no matches after the overfull display break was fixed.
